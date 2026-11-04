"""RF-001: PBKDF2, sessões assinadas e permissões."""
import hashlib,hmac,secrets
from fastapi import HTTPException
def hash_password(p):
 s=secrets.token_hex(16);return s+":"+hashlib.pbkdf2_hmac("sha256",p.encode(),bytes.fromhex(s),310000).hex()
def verify(p,v):
 try:
  s,h=v.split(":");return hmac.compare_digest(hashlib.pbkdf2_hmac("sha256",p.encode(),bytes.fromhex(s),310000).hex(),h)
 except (ValueError,TypeError):return False
def current(request,d):
 uid=request.session.get("uid")
 u=d.execute("SELECT id,name,email,role FROM users WHERE id=?",(uid,)).fetchone() if uid else None
 if not u:raise HTTPException(401,"Autenticação necessária")
 return dict(u)
def require(u,role):
 if u["role"]!=role:raise HTTPException(403,"Permissão negada")
