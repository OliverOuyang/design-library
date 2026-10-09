import sys,numpy as np
from PIL import Image
S=sys.argv[1]; a0=np.asarray(Image.open(S+'/sty/src/astronaut.png').convert('RGB').resize((720,720))); rng=np.random.default_rng(1)
out=sys.stdout.buffer
for f in range(120):
  a=a0.copy(); h,w,_=a.shape; burst=rng.random()<0.35
  for _ in range(rng.integers(3,18) if burst else 1):
    y=rng.integers(0,h-30); hh=rng.integers(3,30); a[y:y+hh]=np.roll(a[y:y+hh],rng.integers(-60,60),1)
  s=int(8*np.sin(f*0.5))+(rng.integers(-12,12) if burst else 0)
  a=np.stack([np.roll(a[...,0],s,1),a[...,1],np.roll(a[...,2],-s,1)],-1).astype(float)
  a+=rng.normal(0,14,(h,w))[...,None]; a[(np.arange(h)+f)%3==0]*=0.55
  roll=(f*9)%h; a[roll:roll+40]*=1.15
  out.write(np.clip(a,0,255).astype('uint8').tobytes())
