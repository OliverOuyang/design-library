import json,subprocess,os
from PIL import Image,ImageDraw,ImageFont
D='/mnt/project-files/design-assets'; T='/tmp/claude-0/-home-claude/eec654ea-a38c-5554-8c60-4783117f35cc/scratchpad/gtiles'; os.makedirs(T,exist_ok=True)
cat=json.load(open(D+'/catalog.json'))['entries']
fb=ImageFont.truetype('/tmp/claude-0/-home-claude/eec654ea-a38c-5554-8c60-4783117f35cc/scratchpad/web/a/lxgw.ttf',30); fs=ImageFont.truetype('/tmp/claude-0/-home-claude/eec654ea-a38c-5554-8c60-4783117f35cc/scratchpad/web/a/lxgw.ttf',21)
tiles=[]
for e in cat:
  img=[f['path'] for f in e['files'] if f['kind'] in('official','reference') and f['path'].lower().endswith(('.png','.jpg','.webp','.gif'))]
  if img: tiles.append((e['kind']+'/'+e['slug'],D+'/'+img[0]+('[0]' if img[0].endswith('.gif') else ''))); continue
  if e['kind']=='styles':
    im=Image.new('RGB',(840,560),'#F4EFE6'); d=ImageDraw.Draw(im); d.text((36,30),e['title'],font=fb,fill='#2B2925')
    d.text((36,78),'参考作品（点 README 链接看原作）',font=fs,fill='#8a8170')
    for i,r in enumerate(e['references'][:9]):
      t=r['title'];t=t if len(t)<34 else t[:33]+'…'; d.text((36,124+i*46),f'{i+1}. {t}',font=fs,fill='#2B2925')
    p=f'{T}/{e["slug"]}.png'; im.save(p); tiles.append((e['kind']+'/'+e['slug'],p))
args=[]
for l,p in tiles: args+=['-label',l,p]
subprocess.run(['montage',*args,'-tile','4x','-geometry','420x280+8+8','-background','#14161c','-fill','#eee','-pointsize','18','-depth','8','-quality','88',D+'/gallery.jpg'],check=True)
print(len(tiles))
