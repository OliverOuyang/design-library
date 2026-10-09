import sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
S=sys.argv[1]; O=S+'/out/'; rng=np.random.default_rng(3)
im=Image.open(S+'/sty/src/chelsea.png').convert('RGB'); W=110; H=int(W*im.height/im.width*0.5)
g=np.asarray(im.convert('L').resize((W,H)))/255; col=np.clip(np.asarray(im.resize((W,H))).astype(float)*1.6+30,0,255)
ramp=" .:-=+*#%@"; f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',12)
out=Image.new('RGB',(W*7,H*13),'#050605'); d=ImageDraw.Draw(out)
for y in range(H):
  for x in range(W): d.text((x*7,y*13),ramp[int(g[y,x]*(len(ramp)-1))],font=f,fill=tuple(int(v) for v in col[y,x]))
out.save(O+'ascii-pixel/ascii-color.png')
# green terminal mono version
out2=Image.new('RGB',out.size,'#020802'); d=ImageDraw.Draw(out2)
for y in range(H):
  for x in range(W): d.text((x*7,y*13),ramp[int(g[y,x]*(len(ramp)-1))],font=f,fill=(90,255,120))
out2.save(O+'ascii-pixel/ascii-terminal-green.png')
# riso
a=np.asarray(ImageOps.autocontrast(im.convert('L').resize((902,600)))).astype(float)/255; h,w=a.shape; yy,xx=np.mgrid[0:h,0:w]
def screen(val,ang,per):
  t=np.deg2rad(ang); u=(xx*np.cos(t)+yy*np.sin(t))/per*2*np.pi; v=(-xx*np.sin(t)+yy*np.cos(t))/per*2*np.pi
  return ((np.cos(u)+np.cos(v))/4+0.5) < val
pink=screen(np.clip((1-a)*0.95,0,1),15,7); blue=screen(np.clip((0.55-a)*2.0,0,1),75,7); blue=np.roll(np.roll(blue,5,1),-4,0)
paper=np.array([247,242,231.]); out=np.ones((h,w,3))*paper
out=np.where(pink[...,None],out*np.array([1.0,0.32,0.66]),out); out=np.where(blue[...,None],out*np.array([0.1,0.45,0.78]),out)
out=np.clip(out+rng.normal(0,9,(h,w))[...,None],0,255).astype('uint8'); Image.fromarray(out).save(O+'grain-riso/riso-pink-blue.png')
