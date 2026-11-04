"""RF-002 a RF-009: regras de tickets; T-02 a T-20."""
from fastapi import HTTPException
from .auth import require
CATEGORIES=("Equipamento","Software","Acessos")
def error(msg,code=400):raise HTTPException(code,msg)
def get(d,i):
 t=d.execute("SELECT * FROM tickets WHERE id=?",(i,)).fetchone()
 if not t:error("Ticket inexistente",404)
 return dict(t)
def allowed(u,t):
 return u["role"]=="responsavel" or u["role"]=="colaborador" and t["creator_id"]==u["id"] or u["role"]=="tecnico" and t["technician_id"]==u["id"]
def view(d,u,i):
 t=get(d,i)
 if not allowed(u,t):error("Sem acesso",403)
 return t
def listing(d,u):
 if u["role"]=="responsavel":r=d.execute("SELECT * FROM tickets ORDER BY id DESC")
 elif u["role"]=="tecnico":r=d.execute("SELECT * FROM tickets WHERE technician_id=? ORDER BY id DESC",(u["id"],))
 else:r=d.execute("SELECT * FROM tickets WHERE creator_id=? ORDER BY id DESC",(u["id"],))
 return [dict(t) for t in r]
def create(d,u,title,description,category):
 require(u,"colaborador")
 if not title.strip() or not description.strip() or category not in CATEGORIES:error("Título, descrição e categoria são obrigatórios")
 c=d.execute("INSERT INTO tickets(title,description,category,creator_id) VALUES(?,?,?,?)",(title.strip(),description.strip(),category,u["id"]));d.commit();return get(d,c.lastrowid)
def assign(d,u,i,tech):
 require(u,"responsavel");t=get(d,i)
 if t["state"] not in ("Aberto","Em tratamento"):error("Estado inválido")
 v=d.execute("SELECT role FROM users WHERE id=?",(tech,)).fetchone()
 if not v or v["role"]!="tecnico":error("Técnico inválido")
 d.execute("UPDATE tickets SET technician_id=? WHERE id=?",(tech,i));d.commit();return get(d,i)
def assigned(d,u,i,state):
 require(u,"tecnico");t=get(d,i)
 if t["technician_id"]!=u["id"]:error("Outro técnico",403)
 if t["state"]!=state:error("Estado inválido")
def start(d,u,i):
 assigned(d,u,i,"Aberto");d.execute("UPDATE tickets SET state='Em tratamento' WHERE id=?",(i,));d.commit();return get(d,i)
def resolve(d,u,i,solution):
 assigned(d,u,i,"Em tratamento")
 if not solution.strip():error("Solução obrigatória")
 d.execute("UPDATE tickets SET state='Resolvido',resolution=? WHERE id=?",(solution.strip(),i));d.commit();return get(d,i)
def reopen(d,u,i):
 require(u,"colaborador");t=get(d,i)
 if t["creator_id"]!=u["id"]:error("Outro colaborador",403)
 if t["state"]!="Resolvido":error("Estado inválido")
 d.execute("UPDATE tickets SET state='Em tratamento' WHERE id=?",(i,));d.commit();return get(d,i)
def close(d,u,i,confirmed):
 require(u,"responsavel");t=get(d,i)
 if t["state"]!="Resolvido" or not confirmed:error("Sofia deve verificar a resolução")
 d.execute("UPDATE tickets SET state='Fechado' WHERE id=?",(i,));d.commit();return get(d,i)
