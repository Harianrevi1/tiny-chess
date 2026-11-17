import json,os,sys,urllib.request as H,random
E=os.environ["MAKEFUN_ENV_URL"]
def post(p,b):
 q=H.Request(E+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with H.urlopen(q) as r:return json.load(r)
 except Exception as e:
  try:return json.loads(e.read())
  except Exception:return {}
V=(0,100,320,330,500,900,0)
T='::::::::DDDDDDDD<<>@@><<;;<??<;;:::>>:::;98::89;;<<66<<;::::::::0244442026::::624:<==<:44;=>>=;44:=>>=:44;<==<;426:;;:6202444420688888868::::::88:;<<;:88;;<<;;88:<<<<:88<<<<<<88;::::;868888886::::::::;<<<<<<;9::::::99::::::99::::::99::::::99::::::9:::;;:::688998868::::::88:;;;;:89:;;;;:9::;;;;:98;;;;;:88:;::::868899886422002244220022442200224422002246442244686666668>>::::>>>@<::<@>02466420468::86448>@@>8448@BB@8448@BB@8448>@@>8444::::4404444440'
KN=(14,18,31,33,-14,-18,-31,-33)
KG=(1,15,16,17,-1,-15,-16,-17)
BD=(15,17,-15,-17)
RD=(1,16,-1,-16)
R=random.Random(7)
Z=[R.getrandbits(64) for _ in range(1561)]
MATE=100000
LIM=100000
nodes=0
TT={}
KIL=[0]*256
SQ=tuple(x for x in range(128) if not x&136)
B=[0]*128
CAST=0
EP=-1
HASH=0
HM=0
KS=[0,0]
ST=[]
HC={}
class A(Exception):pass
def zi(p,s):return ((abs(p)-1)*2+(p<0))*128+s
def atk(b,s,o):
 if o>0:
  if (s-17)&136==0 and b[s-17]==1:return 1
  if (s-15)&136==0 and b[s-15]==1:return 1
 else:
  if (s+17)&136==0 and b[s+17]==-1:return 1
  if (s+15)&136==0 and b[s+15]==-1:return 1
 for d in KN:
  g=s+d
  if g&136==0 and b[g]==2*o:return 1
 for d in KG:
  g=s+d
  if g&136==0 and b[g]==6*o:return 1
 for d in BD:
  g=s+d
  while g&136==0:
   p=b[g]
   if p:
    if p==3*o or p==5*o:return 1
    break
   g+=d
 for d in RD:
  g=s+d
  while g&136==0:
   p=b[g]
   if p:
    if p==4*o or p==5*o:return 1
    break
   g+=d
 return 0
def gen(w,c,e,cap):
 m=[]
 for s in SQ:
  p=B[s]
  if p*w<=0:continue
  t=abs(p)
  if t==1:
   d=16*w;f=s+d
   if not cap and not f&136 and not B[f]:
    if (w>0 and f>111) or (w<0 and f<8):
     for q in (5,4,3,2):m.append(s|f<<7|q<<14)
    else:
     m.append(s|f<<7)
     if (w>0 and s>>4==1) or (w<0 and s>>4==6):
      if not B[f+d]:m.append(s|(f+d)<<7)
   for df in (d-1,d+1):
    g=s+df
    if g&136:continue
    if B[g]*w<0 or g==e:
     if (w>0 and g>111) or (w<0 and g<8):
      for q in (5,4,3,2):m.append(s|g<<7|q<<14)
     else:m.append(s|g<<7)
  elif t==2 or t==6:
   for d in KN if t==2 else KG:
    g=s+d
    if g&136:continue
    if B[g]*w<=0 and (not cap or B[g]):m.append(s|g<<7)
  else:
   for d in BD if t==3 else RD if t==4 else BD+RD:
    g=s+d
    while not g&136:
     if not B[g]:
      if not cap:m.append(s|g<<7)
     elif B[g]*w<0:
      m.append(s|g<<7);break
     else:break
     g+=d
 if not cap:
  if w>0:
   if c&1 and not B[5] and not B[6] and B[7]==4 and not atk(B,4,-1) and not atk(B,5,-1) and not atk(B,6,-1):m.append(4|6<<7)
   if c&2 and not B[3] and not B[2] and not B[1] and B[0]==4 and not atk(B,4,-1) and not atk(B,3,-1) and not atk(B,2,-1):m.append(4|2<<7)
  else:
   if c&4 and not B[117] and not B[118] and B[119]==-4 and not atk(B,116,1) and not atk(B,117,1) and not atk(B,118,1):m.append(116|118<<7)
   if c&8 and not B[115] and not B[114] and not B[113] and B[112]==-4 and not atk(B,116,1) and not atk(B,115,1) and not atk(B,114,1):m.append(116|114<<7)
 return m
def make(m,w):
 global CAST,EP,HASH,HM
 f=m&127;t=(m>>7)&127;q=(m>>14)&7
 pc=B[f];cap=B[t];epc=0
 if abs(pc)==1 and t==EP and not cap:
  epc=t-16*w;cap=B[epc];B[epc]=0
 ST.append((m,cap,CAST,EP,HASH,HM,epc))
 HASH^=Z[zi(pc,f)]
 if cap:HASH^=Z[zi(cap,epc or t)]
 HASH^=Z[zi(w*q if q else pc,t)]
 if abs(pc)==6 and abs(t-f)==2:
  rf=(7 if t>f else 0) if w>0 else (119 if t>f else 112)
  rt=(5 if t>f else 3) if w>0 else (117 if t>f else 115)
  B[rt]=B[rf];B[rf]=0
  HASH^=Z[zi(B[rt],rf)]^Z[zi(B[rt],rt)]
 B[t]=w*q if q else pc;B[f]=0
 if abs(pc)==6:KS[(w+1)//2]=t
 nc=CAST
 if abs(pc)==6:nc&=~(3 if w>0 else 12)
 if f==7 or t==7:nc&=~1
 if f==0 or t==0:nc&=~2
 if f==119 or t==119:nc&=~4
 if f==112 or t==112:nc&=~8
 if nc!=CAST:HASH^=Z[1537+CAST]^Z[1537+nc];CAST=nc
 nep=-1
 if abs(pc)==1 and abs(t-f)==32:nep=(f+t)//2
 if EP>=0:HASH^=Z[1553+(EP&7)]
 if nep>=0:HASH^=Z[1553+(nep&7)]
 EP=nep
 HASH^=Z[1536]
 HM=0 if cap or abs(pc)==1 else HM+1
 HC[HASH]=HC.get(HASH,0)+1
def unmake(m,w):
 global CAST,EP,HASH,HM
 HC[HASH]-=1
 m2,cap,oc,oe,oh,ohm,epc=ST.pop()
 f=m&127;t=(m>>7)&127;q=(m>>14)&7
 pc=B[t]
 B[f]=w if q else pc
 B[t]=0
 if cap:
  if epc:B[epc]=cap
  else:B[t]=cap
 if abs(pc)==6 and abs(t-f)==2:
  rt=(5 if t>f else 3) if w>0 else (117 if t>f else 115)
  rf=(7 if t>f else 0) if w>0 else (119 if t>f else 112)
  B[rf]=B[rt];B[rt]=0
 if abs(pc)==6:KS[(w+1)//2]=f
 CAST,EP,HASH,HM=oc,oe,oh,ohm
def ev(w):
 s=0;ph=0;nb=[0,0]
 for i in SQ:
  p=B[i]
  if not p:continue
  t=abs(p)
  if t==6:continue
  if t==3:nb[p<0]+=1
  j=i if p>0 else i^112
  v=V[t]+(ord(T[(t-1)*64+(j&7)|((7-(j>>4))<<3)])-58)*5
  s+=v if p>0 else -v
  ph+=V[t]
 if nb[0]>1:s+=30
 if nb[1]>1:s-=30
 k=320 if ph>1300 else 384
 for x in (1,-1):
  j=KS[(x+1)//2]
  if x<0:j^=112
  v=(ord(T[k+(j&7)|((7-(j>>4))<<3)])-58)*5
  s+=v if x>0 else -v
 return s if w>0 else -s
def order(ms,w,tt,ply):
 def sc(m):
  f=m&127;t=(m>>7)&127
  s=0
  if m==tt:s+=10000000
  v=B[t]
  if v:s+=1000*V[abs(v)]-V[abs(B[f])]
  elif (m>>14)&7:s+=9000
  if m==KIL[ply]:s+=5000
  return s
 return sorted(ms,key=sc,reverse=True)
def qs(w,a,b,ply):
 global nodes
 nodes+=1
 if nodes>LIM:raise A
 s=ev(w)
 if s>=b:return b
 if s>a:a=s
 inchk=atk(B,KS[(w+1)//2],-w)
 ms=order(gen(w,CAST,EP,not inchk),w,0,ply)
 n=0
 for m in ms:
  make(m,w)
  if atk(B,KS[(w+1)//2],-w):unmake(m,w);continue
  n+=1
  s=-qs(-w,-b,-a,ply+1)
  unmake(m,w)
  if s>a:a=s
  if a>=b:break
 if n==0 and inchk:return -MATE+ply
 return a
def ab(w,d,a,b,ply):
 global nodes,HASH,EP,HM
 nodes+=1
 if nodes>LIM:raise A
 if HC.get(HASH,0)>1 or HM>=100:return 0
 inchk=atk(B,KS[(w+1)//2],-w)
 if d<=0:return qs(w,a,b,ply)
 if inchk:d+=1
 e=TT.get(HASH)
 if e and e[0]>=d:
  s=e[1]
  if e[2]==0:return s
  if e[2]==1 and s>=b:return s
  if e[2]==2 and s<=a:return s
 if d>=3 and not inchk:
  oe=EP;oh=HASH
  if oe>=0:HASH^=Z[1553+(oe&7)]
  EP=-1;HASH^=Z[1536];HM+=1
  HC[HASH]=HC.get(HASH,0)+1
  s=-ab(-w,d-3,-b,-b+1,ply+1)
  HC[HASH]-=1
  EP=oe;HASH=oh;HM-=1
  if s>=b:return b
 ms=order(gen(w,CAST,EP,False),w,e[3] if e else 0,ply)
 best=-MATE;bm=0;n=0;oa=a
 for m in ms:
  f=m&127;t=(m>>7)&127
  cap=B[t] or (t==EP and abs(B[f])==1)
  make(m,w)
  if atk(B,KS[(w+1)//2],-w):unmake(m,w);continue
  n+=1
  s=-ab(-w,d-1,-b,-a,ply+1)
  unmake(m,w)
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not cap:KIL[ply]=m
   break
 if n==0:return -MATE+ply if inchk else 0
 TT[HASH]=(d,best,2 if best<=oa else 1 if best>=b else 0,bm)
 return best
def rd(w,d,ms):
 a=-MATE;b=MATE;best=-MATE;bm=ms[0]
 for m in ms:
  make(m,w)
  if atk(B,KS[(w+1)//2],-w):unmake(m,w);continue
  s=-ab(-w,d-1,-b,-a,1)
  unmake(m,w)
  if s>best:best=s;bm=m
  if s>a:a=s
 return best,bm
def root(w,ms):
 global nodes,LIM
 nodes=0;best=ms[0];L0=LIM;LIM=10**9
 for d in range(1,99):
  try:
   s,bm=rd(w,d,ms)
   best=bm;ms.remove(bm);ms.insert(0,bm)
  except A:break
  LIM=L0
 return best
def sq(s):return "abcdefgh"[s&7]+str((s>>4)+1)
def uci(m):
 q=(m>>14)&7
 return sq(m&127)+sq((m>>7)&127)+("nbrq"[q-2] if q else "")
def pu(u):
 f=(ord(u[0])-97)+(int(u[1])-1)*16
 t=(ord(u[2])-97)+(int(u[3])-1)*16
 q='nbrq'.index(u[4])+2 if len(u)==5 else 0
 return f|t<<7|q<<14
def parse(f):
 global CAST,EP,HASH,HM,KS,B
 B=[0]*128;p=f.split();r=0;c=0
 for ch in p[0]:
  if ch=='/':r+=1;c=0
  elif ch.isdigit():c+=int(ch)
  else:
   v='PNBRQK'.index(ch.upper())+1
   s=(7-r)*16+c
   B[s]=v if ch.isupper() else -v
   if v==6:KS[1 if ch.isupper() else 0]=s
   c+=1
 w=1 if p[1]=='w' else -1
 CAST=0
 for ch in p[2]:CAST|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
 EP=-1
 if p[3]!='-':EP=(int(p[3][1])-1)*16+ord(p[3][0])-97
 HM=int(p[4])
 HASH=0
 for s in range(128):
  if s&136:continue
  v=B[s]
  if v:HASH^=Z[zi(v,s)]
 if w<0:HASH^=Z[1536]
 HASH^=Z[1537+CAST]
 if EP>=0:HASH^=Z[1553+(EP&7)]
 return w
def setup(g):
 parse(g['start_fen'])
 ST.clear();HC.clear();HC[HASH]=1
 w=1 if g['start_fen'].split()[1]=='w' else -1
 for u in g['moves']:
  make(pu(u),w)
  w=-w
 return w
if __name__=="__main__":
 while True:
  g=post('/game',{})
  if g['status']=='done':break
  me=1 if g['colour']=='white' else -1
  S=setup(g)
  while g['status']=='your_move':
   ms=gen(S,CAST,EP,False)
   m=root(S,ms)
   S=setup(g)  # restore board: an aborted search leaves makes unbalanced
   u=uci(m)
   if u not in g['legal_moves']:
    u=g['legal_moves'][0];m=pu(u)
   make(m,S)
   r=post('/move',{'game':g['game'],'move':u})
   if 'error' in r:
    unmake(m,S)
    for u2 in g['legal_moves']:
     if u2==u:continue
     m2=pu(u2);make(m2,S)
     r=post('/move',{'game':g['game'],'move':u2})
     if 'error' not in r:u=u2;m=m2;break
     unmake(m2,S)
    else:sys.exit('no move accepted')
   S=-S
   g=r
   if g['status']=='your_move':
    om=pu(g['last_move']);make(om,S);S=-S
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
