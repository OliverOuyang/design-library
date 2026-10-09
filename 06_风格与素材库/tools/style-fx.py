import sys, numpy as np, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
S=sys.argv[1]; src=S+'/sty/src/'; O=S+'/out/'
def ld(n): return Image.open(src+n).convert('RGB')
def sv(im,d,n): os.makedirs(O+d,exist_ok=True); im.save(O+d+'/'+n); print(d,n,im.size)
rng=np.random.default_rng(7)
# 1 ASCII
im=ld('chelsea.png'); W=110; H=int(W*im.height/im.width*0.5); g=np.asarray(im.convert('L').resize((W,H)))/255
ramp=" .:-=+*#%@"[::-1]; ramp=" .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::-1]
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',12); cw,ch=7,13
out=Image.new('RGB',(W*cw,H*ch),'#0b0d0b'); d=ImageDraw.Draw(out); col=np.asarray(im.resize((W,H)))
for y in range(H):
  for x in range(W):
    c=ramp[int((1-g[y,x])*(len(ramp)-1))]; d.text((x*cw,y*ch),c,font=f,fill=tuple(int(v) for v in col[y,x]))
sv(out,'ascii-pixel','ascii-color.png')
txt='\n'.join(''.join(ramp[int((1-g[y,x])*(len(ramp)-1))] for x in range(W)) for y in range(H)); open(O+'ascii-pixel/ascii.txt','w').write(txt)
# pixel art PICO-8
pico=[0,0,0,29,43,83,126,37,83,0,135,81,171,82,54,95,87,79,194,195,199,255,241,232,255,0,77,255,163,0,255,236,39,0,228,54,41,173,255,131,118,156,255,119,168,255,204,170]
pal=Image.new('P',(1,1)); pal.putpalette(pico+[0]*(768-len(pico)))
for n in ['chelsea.png','astronaut.png']:
  small=ld(n).resize((96,int(96*ld(n).height/ld(n).width)),Image.BILINEAR).quantize(palette=pal,dither=Image.Dither.NONE).convert('RGB')
  sv(small.resize((small.width*6,small.height*6),Image.NEAREST),'ascii-pixel','pixel-pico8-'+n.split('.')[0]+'.png')
# 8 dither / halftone
im=ld('astronaut.png').convert('L')
sv(im.convert('1').convert('RGB'),'dither-halftone','floyd-steinberg-1bit.png')
bayer=np.array([[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]])/16
a=np.asarray(im)/255; t=np.tile(bayer,(a.shape[0]//4+1,a.shape[1]//4+1))[:a.shape[0],:a.shape[1]]
b=(a>t); duo=np.where(b[...,None],np.array([240,232,214]),np.array([36,32,88])).astype('uint8'); sv(Image.fromarray(duo),'dither-halftone','bayer-duotone.png')
# halftone dots
step=8; hb=Image.new('RGB',im.size,(245,240,228)); hd=ImageDraw.Draw(hb); sm=np.asarray(im.resize((im.width//step,im.height//step)))/255
for y in range(sm.shape[0]):
  for x in range(sm.shape[1]):
    r=(1-sm[y,x])*step*0.72; cx,cy=x*step+step/2,y*step+step/2; hd.ellipse((cx-r,cy-r,cx+r,cy+r),fill=(20,20,20))
sv(hb,'dither-halftone','halftone-dots.png')
# 5 lomo
for n in ['rocket.jpg','coffee.png']:
  im=ld(n); a=np.asarray(im).astype(float)/255
  a[...,0]=np.clip(a[...,0]**0.85*1.08,0,1); a[...,1]=np.clip(a[...,1]**0.95,0,1); a[...,2]=np.clip(a[...,2]*0.75+0.12,0,1)  # cross process
  h,w=a.shape[:2]; yy,xx=np.mgrid[0:h,0:w]; r=np.sqrt(((xx-w/2)/(w/2))**2+((yy-h/2)/(h/2))**2); v=np.clip(1-0.75*r**2.2,0,1); a*=v[...,None]
  leak=np.exp(-(((xx-w*0.95)/(w*0.25))**2+((yy-h*0.1)/(h*0.5))**2))[...,None]*np.array([1,0.45,0.1]); a=np.clip(a+leak*0.55,0,1)
  a=np.clip(a+rng.normal(0,0.045,a.shape[:2])[...,None],0,1)
  o=ImageEnhance.Contrast(ImageEnhance.Color(Image.fromarray((a*255).astype('uint8'))).enhance(1.5)).enhance(1.25)
  sv(o,'lomo','lomo-'+n.split('.')[0]+'.png')
# 10 grain / riso
im=ld('chelsea.png').convert('L'); a=np.asarray(ImageOps.autocontrast(im)).astype(float)/255; h,w=a.shape
paper=np.array([246,241,230]); ink1=np.array([255,72,176]); ink2=np.array([0,120,191])
def dith(x): return (x>rng.random(x.shape)).astype(float)
l1=dith(np.clip((1-a)*1.1,0,1)*0.85); l2=dith(np.clip(a*(1-a)*3.2,0,1))
l2=np.roll(np.roll(l2,4,1),-3,0)
out=paper*np.ones((h,w,3)); out=out*(1-l1[...,None]*0.75)+ink1*l1[...,None]*0.75*0+out*0; 
out=paper*np.ones((h,w,3)); out=np.where(l1[...,None]>0,out*(ink1/255),out); out=np.where(l2[...,None]>0,out*(ink2/255+0.25).clip(0,1),out)
out=np.clip(out+rng.normal(0,10,(h,w))[...,None],0,255).astype('uint8'); sv(Image.fromarray(out).resize((w*2,h*2),Image.NEAREST),'grain-riso','riso-pink-blue.png')
# grain texture tile
gt=np.clip(240+rng.normal(0,14,(512,512)),0,255).astype('uint8'); g3=np.stack([gt,gt-4,gt-14],-1).clip(0,255).astype('uint8'); sv(Image.fromarray(g3).filter(ImageFilter.GaussianBlur(0.4)),'grain-riso','paper-grain-tile.png')
# 9 glitch / CRT
im=ld('astronaut.png'); a=np.asarray(im).copy(); h,w,_=a.shape
for _ in range(14):
  y=rng.integers(0,h-20); hh=rng.integers(4,26); s=rng.integers(-40,40); a[y:y+hh]=np.roll(a[y:y+hh],s,1)
r=np.roll(a[...,0],6,1); b=np.roll(a[...,2],-6,1); a=np.stack([r,a[...,1],b],-1)
a[::3]=(a[::3]*0.55).astype('uint8'); sv(Image.fromarray(a),'glitch-crt','glitch-rgbsplit-scanlines.png')
# 3 impressionism via PIL-ish: handled by primitive & magick
