"""FastAPI e HTML simples — interface, API, regras e dados."""
import os,html
from contextlib import asynccontextmanager
from fastapi import FastAPI,Request,Form,HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from .database import connect,initialize
from .auth import verify,current
from . import services
def esc(x):return html.escape(str(x),quote=True)
def page(title,body,u=None):
 nav='<a href="/tickets">Tickets</a> <a href="/tickets/new">Novo ticket</a> <form method="post" action="/logout"><button>Sair</button></form>' if u else ''
 return HTMLResponse('<!doctype html><html lang="pt"><meta charset="utf-8"><title>SmartDesk</title><style>body{font:16px system-ui;margin:3em auto;max-width:850px;color:#18344c}input,textarea,select{display:block;margin:.5em 0 1em;padding:.5em}button{padding:.6em;background:#145b8c;color:white;border:0;border-radius:4px}article{padding:1em;border-bottom:1px solid #ddd}a{color:#145b8c}</style><h1>SmartDesk</h1>'+nav+'<h2>'+esc(title)+'</h2>'+body+'</html>')
def form(action,fields,button):
 return '<form method="post" action="'+action+'">'+fields+'<button>'+button+'</button></form>'
def create_app(path=None,secret=None):
 @asynccontextmanager
 async def lifespan(app):
  with connect(path) as d:initialize(d)
  yield
 app=FastAPI(title="SmartDesk",lifespan=lifespan)
 app.add_middleware(SessionMiddleware,secret_key=secret or os.getenv("SMARTDESK_SESSION_SECRET","local-only-not-for-production"),same_site="lax")
 def db():return connect(path)
 def redirect(t):return RedirectResponse("/tickets/"+str(t["id"]),status_code=303)
 @app.get("/")
 def root():return RedirectResponse("/tickets")
 @app.get("/login")
 def login_page():return page("Iniciar sessão",form("/login",'<label>Email<input type="email" name="email" required></label><label>Palavra-passe<input type="password" name="password" required></label>',"Entrar"))
 @app.post("/login")
 def login(request:Request,email:str=Form(...),password:str=Form(...)):
  with db() as d:r=d.execute("SELECT * FROM users WHERE email=?",(email.lower().strip(),)).fetchone()
  if not r or not verify(password,r["secret"]):return page("Erro","Credenciais inválidas. <a href='/login'>Tentar novamente</a>")
  request.session.clear();request.session["uid"]=r["id"];return RedirectResponse("/tickets",303)
 @app.post("/logout")
 def logout(request:Request):request.session.clear();return RedirectResponse("/login",303)
 @app.get("/tickets")
 def tickets(request:Request):
  with db() as d:
   u=current(request,d);items=services.listing(d,u)
  body="".join('<article><a href="/tickets/'+str(t["id"])+'">'+esc(t["title"])+'</a> — '+esc(t["category"])+' — '+esc(t["state"])+'</article>' for t in items) or "Sem tickets."
  return page("Tickets",body,u)
 @app.get("/tickets/new")
 def new(request:Request):
  with db() as d:u=current(request,d)
  if u["role"]!="colaborador":raise HTTPException(403,"Sem permissão")
  fields='<label>Título<input name="title" required></label><label>Descrição<textarea name="description" required></textarea></label><label>Categoria<select name="category" required><option value="">Escolher</option>'+''.join('<option>'+x+'</option>' for x in services.CATEGORIES)+'</select></label>'
  return page("Novo ticket",form("/tickets/new",fields,"Criar"),u)
 @app.post("/tickets/new")
 def create(request:Request,title:str=Form(""),description:str=Form(""),category:str=Form("")):
  with db() as d:t=services.create(d,current(request,d),title,description,category)
  return redirect(t)
 @app.get("/tickets/{i}")
 def detail(request:Request,i:int):
  with db() as d:
   u=current(request,d);t=services.view(d,u,i);techs=[dict(x) for x in d.execute("SELECT id,name FROM users WHERE role='tecnico'")]
  body='<p>'+esc(t["description"])+'</p><p>Categoria: '+esc(t["category"])+' | Estado: '+esc(t["state"])+'</p><p>Solução: '+esc(t["resolution"] or "Por registar")+'</p><p>Técnico ID: '+esc(t["technician_id"] or "Por atribuir")+'</p>'
  prefix="/api/tickets/"+str(i)
  if u["role"]=="responsavel" and t["state"] in ("Aberto","Em tratamento"):
   opts="".join('<option value="'+str(x["id"])+'">'+esc(x["name"])+'</option>' for x in techs)
   body+=form(prefix+"/assign",'<select name="technician_id">'+opts+'</select>', "Atribuir/reatribuir")
  if u["role"]=="tecnico" and t["technician_id"]==u["id"]:
   if t["state"]=="Aberto":body+=form(prefix+"/start","","Iniciar tratamento")
   if t["state"]=="Em tratamento":body+=form(prefix+"/resolve",'<textarea name="resolution" required></textarea>',"Resolver")
  if u["role"]=="colaborador" and t["creator_id"]==u["id"] and t["state"]=="Resolvido":body+=form(prefix+"/return","","Problema persiste")
  if u["role"]=="responsavel" and t["state"]=="Resolvido":body+=form(prefix+"/close",'<label><input type="checkbox" name="confirmed" value="true" required> Verifiquei a resolução</label>',"Fechar")
  return page("Ticket #"+str(i)+" — "+t["title"],body,u)
 @app.post("/api/tickets/{i}/assign")
 def assign(request:Request,i:int,technician_id:int=Form(...)):
  with db() as d:t=services.assign(d,current(request,d),i,technician_id)
  return redirect(t)
 @app.post("/api/tickets/{i}/start")
 def start(request:Request,i:int):
  with db() as d:t=services.start(d,current(request,d),i)
  return redirect(t)
 @app.post("/api/tickets/{i}/resolve")
 def resolve(request:Request,i:int,resolution:str=Form("")):
  with db() as d:t=services.resolve(d,current(request,d),i,resolution)
  return redirect(t)
 @app.post("/api/tickets/{i}/return")
 def ret(request:Request,i:int):
  with db() as d:t=services.reopen(d,current(request,d),i)
  return redirect(t)
 @app.post("/api/tickets/{i}/close")
 def close(request:Request,i:int,confirmed:bool=Form(False)):
  with db() as d:t=services.close(d,current(request,d),i,confirmed)
  return redirect(t)
 return app
app=create_app()
