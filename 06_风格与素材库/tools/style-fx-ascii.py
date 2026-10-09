import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
S=sys.argv[1]; O=S+'/out/'
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',11); cw,ch=7,12
ramp=" .`:-=+*cox%#&@"
for n,W in [('astronaut.png',120),('chelsea.png',130)]:
  im=Image.open(S+'/sty/src/'+n).convert('RGB'); H=int(W*im.height/im.width*cw/ch)
  g=np.asarray(ImageOps.autocontrast(im.convert('L'),cutoff=2).resize((W,H))).astype(float)/255; g=g**0.8
  col=np.asarray(ImageOps.autocontrast(im,cutoff=2).resize((W,H))).astype(float)
  for mode in ['color','green']:
    out=Image.new('RGB',(W*cw,H*ch),'#050605'); d=ImageDraw.Draw(out)
    for y in range(H):
      for x in range(W):
        c=ramp[int(g[y,x]*(len(ramp)-1))]
        fill=tuple(int(min(255,v*1.15+25)) for v in col[y,x]) if mode=='color' else (int(60+195*g[y,x]),255,int(80+100*g[y,x]))
        d.text((x*cw,y*ch),c,font=f,fill=fill)
    out.save(O+f"ascii-pixel/ascii-{mode}-{n.split('.')[0]}.png")
  open(O+f"ascii-pixel/ascii-{n.split('.')[0]}.txt",'w').write('\n'.join(''.join(ramp[int(g[y,x]*(len(ramp)-1))] for x in range(W)) for y in range(H)))
