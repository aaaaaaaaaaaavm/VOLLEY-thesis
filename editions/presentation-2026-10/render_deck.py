#!/usr/bin/env python3
"""VOLLEY slide renderer. One primitive list drives editable PPTX, PDF and HTML."""
import argparse, base64, hashlib, html, io, json, math, re, shutil
from pathlib import Path
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parent
W,H=960,540
C={'navy':'102238','ink':'172D43','muted':'596C7B','copper':'B97149','blue':'236D9B','pale':'EDF3F7','line':'D4DFE7','white':'FFFFFF','paper':'FAFCFD','green':'246E60'}
FONTDIR=ROOT/'assets' if (ROOT/'assets'/'LiberationSans-Regular.ttf').exists() else Path('/usr/share/fonts/truetype/liberation')
for fn,stem in [('Liberation','LiberationSans-Regular.ttf'),('Liberation-Bold','LiberationSans-Bold.ttf'),('Liberation-Italic','LiberationSans-Italic.ttf')]:
    fp=FONTDIR/stem
    if not fp.exists():fp=Path('/usr/share/fonts/truetype/liberation')/stem
    pdfmetrics.registerFont(TTFont(fn,str(fp)))

def width(s,size,bold=False):return pdfmetrics.stringWidth(str(s),'Liberation-Bold' if bold else 'Liberation',size)
def wrap(s,size,maxw,bold=False):
    out=[]
    for para in str(s).replace('\r','').split('\n'):
        words=para.split(); line=''
        for word in words:
            test=(line+' '+word).strip()
            if width(test,size,bold)>maxw and line: out.append(line);line=word
            else:line=test
        out.append(line)
    return out

class Page:
    def __init__(self,slide,index,total):self.s=slide;self.index=index;self.total=total;self.ops=[];self.text_bounds=[]
    def rect(self,x,y,w,h,fill,stroke=None,r=0):self.ops.append(dict(t='rect',x=x,y=y,w=w,h=h,fill=fill,stroke=stroke,r=r))
    def line(self,x,y,x2,y2,color,lw=1):self.ops.append(dict(t='line',x=x,y=y,x2=x2,y2=y2,color=color,lw=lw))
    def text(self,s,x,y,w,size=20,color=None,bold=False,leading=1.18,maxlines=None,align='left',italic=False):
        if s is None:return 0
        lines=wrap(str(s),size,w,bold)
        if maxlines is not None and len(lines)>maxlines:
            raise ValueError(f'Slide {self.index}: text requires {len(lines)} lines (max {maxlines}): {str(s)[:80]}')
        for i,line in enumerate(lines):
            ly=y+i*size*leading
            self.ops.append(dict(t='text',s=line,x=x,y=ly,w=w,h=size*1.28,size=size,color=color or C['ink'],bold=bold,align=align,italic=italic))
            self.text_bounds.append((x,ly,x+w,ly+size*leading,line))
        return len(lines)*size*leading
    def image(self,path,x,y,w,h):
        if not path:return
        src=Path(path)
        if not src.exists():raise FileNotFoundError(src)
        key=hashlib.sha256(src.read_bytes()).hexdigest()[:12]
        dst=src if src.parent.resolve()==(ROOT/'assets').resolve() else ROOT/'assets'/f'{src.stem}-{key}.jpg'
        dst.parent.mkdir(exist_ok=True)
        if not dst.exists():
            im=Image.open(src).convert('RGB'); im.thumbnail((1500,1100))
            im.save(dst,'JPEG',quality=89,optimize=True)
        im=Image.open(dst); iw,ih=im.size
        scale=min(w/iw,h/ih); dw,dh=iw*scale,ih*scale
        self.ops.append(dict(t='image',path=str(dst),x=x+(w-dw)/2,y=y+(h-dh)/2,w=dw,h=dh))
    def movie(self,path,poster,x,y,w,h):
        dst=ROOT/'assets'/Path(path).name
        if Path(path).resolve()!=dst.resolve():shutil.copyfile(path,dst)
        ip=Path(poster);pdst=ROOT/'assets'/ip.name
        if ip.resolve()!=pdst.resolve():shutil.copyfile(ip,pdst)
        scale=min(w/960,h/540);dw,dh=960*scale,540*scale
        self.ops.append(dict(t='video',path=str(dst),poster=str(pdst),x=x+(w-dw)/2,y=y+(h-dh)/2,w=dw,h=dh))
    def bullet(self,s,x,y,w,size=21,color=None):
        self.rect(x,y+8,5,5,C['copper'])
        return self.text(s,x+18,y,w-18,size,color,maxlines=5)+14
    def link(self,s,x,y,w,size,url,bold=False):
        before=len(self.ops);h=self.text(s,x,y,w,size,C['blue'],bold)
        for o in self.ops[before:]:o['url']=url
        return h
    def footer(self,dark=False):
        color='C7D3DD' if dark else C['muted']
        self.line(36,503,924,503,'3B5064' if dark else C['line'])
        source=self.s.get('source') or self.s.get('sources') or ''
        if isinstance(source,list):source=' • '.join(str(x) for x in source)
        if len(source)>160:source=source[:157]+'…'
        self.text(source,36,512,790,9.2,color,maxlines=2)
        self.text(f'{self.index:02d}  /  {self.total:02d}',847,512,77,10,color,align='right')
    def header(self):
        s=self.s
        self.rect(0,0,W,H,C['paper'])
        self.rect(36,29,24,4,C['copper'])
        kicker=s.get('section') or s.get('kicker') or 'VOLLEY · COMPUTATIONAL DESIGN'
        if s.get('appendix'):kicker='APPENDIX '+str(s.get('id',''))+' · '+kicker
        self.text(str(kicker).upper(),71,25,820,10.5,C['muted'],bold=True,maxlines=1)
        title=s.get('title','')
        size=30 if width(title,31,True)>875 else 31
        self.text(title,36,54,888,size,C['navy'],bold=True,maxlines=2)
        if s.get('subtitle'):self.text(s['subtitle'],36,108,888,15,C['muted'],maxlines=2)
    def callout(self,s,y=451,dark=False):
        if not s:return
        self.rect(36,y,888,39,'213B52' if dark else C['pale'],r=5)
        self.rect(36,y,4,39,C['copper'])
        self.text(s,51,y+9,858,16,'FFFFFF' if dark else C['ink'],bold=True,maxlines=1)

def strbody(s):
    v=s.get('bullets',s.get('body',s.get('points',[])))
    if isinstance(v,str):return [v]
    return v or []
def assets(s):
    v=s.get('assets',s.get('images',s.get('image',s.get('asset',s.get('visual',[])))))
    if isinstance(v,(str,dict)):v=[v]
    return [dict(path=x,caption=s.get('caption','')) if isinstance(x,str) else x for x in (v or [])]
def cap(x):return x.get('caption','')
def path(x):return x.get('path',x.get('src',x.get('asset','')))

def render_page(s,index,total):
    p=Page(s,index,total);layout=s.get('layout','image_split' if assets(s) else 'bullets')
    if layout in ['title','closing','cover']:
        p.rect(0,0,W,H,C['navy']);p.rect(36,40,32,5,C['copper'])
        p.text(s.get('kicker','DEPARTMENT OF MECHANICAL ENGINEERING'),36,59,840,11,'B4C9D8',bold=True)
        if layout!='closing':
            p.text('VOLLEY',36,99,620,59,'FFFFFF',bold=True)
            p.text(s.get('subtitle',s.get('title','A Commanded Electromagnetic CubeSat Deployment Mechanism')).replace('VOLLEY: ',''),38,177,555,28,'FFFFFF',bold=True,maxlines=4)
            p.text('Adityavardhan Mishra · 23070125054',38,326,730,18,'FFFFFF',bold=True)
            p.text('Pratham Chawla · 23070125029',38,353,730,18,'FFFFFF',bold=True)
            p.text(s.get('institution','Symbiosis Institute of Technology, Pune\nB.Tech · Mechanical Engineering'),38,396,700,16,'C7D3DD',maxlines=2)
            p.text(s.get('guide','Guide: Vikas Gulia'),38,453,700,15,'C7D3DD')
            aa=assets(s)
            if aa:p.image(path(aa[0]),615,125,310,310)
        else:
            p.text(s.get('title','A controlled release begins with a controlled design.'),36,98,855,38,'FFFFFF',bold=True,maxlines=3)
            p.text(s.get('message',''),36,220,855,22,'DCE7EE',bold=True,maxlines=2)
            p.text('Questions',36,292,855,29,'FFFFFF',bold=True)
            y=352
            for b in strbody(s):y+=p.bullet(b,42,y,850,14.5,'DCE7EE')
        p.footer(True);return p
    p.header();aa=assets(s);bs=strbody(s)
    ytop=143 if s.get('subtitle') else 127
    bottom=435 if s.get('takeaway') or s.get('callout') else 479
    avail=bottom-ytop
    if layout in ['image_split','split','feeder','results'] and aa:
        left=s.get('image_side','right')=='left';tx=577 if left else 36;ix=36 if left else 402
        tw=347 if left else 330;iw=515 if left else 522
        metrics=s.get('metrics',[])
        ibottom=bottom-58 if metrics else bottom
        p.rect(ix,ytop,iw,ibottom-ytop-28,C['white'],C['line'],5)
        fy=0
        if s.get('formula_position')=='image_top':
            p.text(s['formula'],ix+17,ytop+12,iw-34,21,C['blue'],True,maxlines=1);fy=39
        if s.get('movie'):p.movie(s['movie'],s['poster'],ix+9,ytop+8+fy,iw-18,ibottom-ytop-45-fy)
        else:p.image(path(aa[0]),ix+9,ytop+8+fy,iw-18,ibottom-ytop-45-fy)
        if cap(aa[0]):p.text(cap(aa[0]),ix+8,ibottom-20,iw-16,10.5,C['muted'],maxlines=2)
        y=ytop+3
        for b in bs:y+=p.bullet(b,tx,y,tw,20 if len(bs)>3 else 21)
        if s.get('formula') and s.get('formula_position')!='image_top':
            p.text(s['formula'],tx,max(y+8,381 if not metrics else 338),tw,19,C['blue'],True,maxlines=2)
        if metrics:
            cw=888/len(metrics)
            for j,metric in enumerate(metrics):
                mx=36+j*cw;p.rect(mx,bottom-46,cw-10,46,C['pale'],r=4)
                p.text(metric.get('value',''),mx+10,bottom-42,cw-26,23,C['blue'],True,maxlines=1)
                p.text(metric.get('label',''),mx+10,bottom-15,cw-26,10.5,C['muted'],maxlines=1)
    elif layout in ['plot_big','full_image','image','diagram','plot'] and aa:
        top=ytop
        if bs:
            top+=p.text('  •  '.join(str(x) for x in bs),36,top,888,17,C['ink'],maxlines=2)+8
        if len(aa)==1:
            p.rect(36,top,888,bottom-top-22,C['white'],C['line'],5);p.image(path(aa[0]),45,top+7,870,bottom-top-38)
            if cap(aa[0]):p.text(cap(aa[0]),40,bottom-17,880,10.5,C['muted'],maxlines=2)
        else:
            gap=18;cw=(888-gap*(len(aa)-1))/len(aa)
            for j,a in enumerate(aa):
                x=36+j*(cw+gap);p.rect(x,top,cw,bottom-top-23,C['white'],C['line'],5)
                p.image(path(a),x+5,top+7,cw-10,bottom-top-50)
                p.text(cap(a),x+5,bottom-36,cw-10,12,C['muted'],maxlines=2)
    elif layout in ['two_columns','columns','cards']:
        cols=s.get('columns',s.get('cards',[]))
        if not cols:cols=[{'title':'Design intent','bullets':bs[:math.ceil(len(bs)/2)]},{'title':'Engineering evidence','bullets':bs[math.ceil(len(bs)/2):]}]
        gap=20;cw=(888-(len(cols)-1)*gap)/len(cols)
        for j,c in enumerate(cols):
            x=36+j*(cw+gap);p.rect(x,ytop,cw,avail-1,C['white'],C['line'],5)
            p.rect(x,ytop,4,avail-1,C['blue'] if j%2==0 else C['copper'])
            y=ytop+19;y+=p.text(c.get('title',c.get('heading','')),x+19,y,cw-38,23,C['navy'],True,maxlines=2)+18
            cb=c.get('bullets',c.get('body',c.get('text',[])));cb=[cb] if isinstance(cb,str) else cb
            for b in cb:y+=p.bullet(b,x+18,y,cw-36,19 if len(cols)==2 else 18)
        if s.get('formula'):p.text(s['formula'],56,391,848,22,C['blue'],True,maxlines=2)
    elif layout in ['roadmap','timeline','sequence']:
        stages=s.get('stages',s.get('steps',s.get('timeline',[])))
        if not stages:stages=[{'title':str(i+1),'body':b} for i,b in enumerate(bs)]
        n=len(stages);gap=15;cw=(888-gap*(n-1))/n
        for j,c in enumerate(stages):
            x=36+j*(cw+gap);p.rect(x,ytop+17,cw,avail-20,C['white'],C['line'],5)
            p.rect(x,ytop+17,cw,4,C['blue'] if j==0 else C['copper'])
            p.text(f'{j+1:02d}',x+16,ytop+37,cw-32,32,C['blue'],True)
            y=ytop+85;y+=p.text(c.get('title',c.get('label','')),x+16,y,cw-32,20,C['navy'],True,maxlines=3)+15
            body=c.get('body',c.get('text',c.get('bullets',[])));body=[body] if isinstance(body,str) else body
            for b in body:y+=p.text(b,x+16,y,cw-32,18,C['muted'],maxlines=6)+11
    elif layout=='table':
        rows=s.get('rows',[]);heads=s.get('headers',[])
        if heads:rows=[heads]+rows
        if not rows:rows=[[str(i+1),b] for i,b in enumerate(bs)]
        widths=s.get('column_widths',[1/len(rows[0])]*len(rows[0]));rowh=min(60,avail/len(rows));y=ytop
        for i,row in enumerate(rows):
            x=36
            for j,cell in enumerate(row):
                cw=888*widths[j];p.rect(x,y,cw,rowh,C['navy'] if i==0 else (C['white'] if i%2 else C['pale']),C['line'])
                p.text(str(cell),x+10,y+12,cw-20,16 if len(rows)<7 else 14,'FFFFFF' if i==0 else C['ink'],i==0,maxlines=2)
                x+=cw
            y+=rowh
    elif layout=='references':
        y=ytop
        for ref in s.get('references',[]):
            y+=p.text(ref['text'],40,y,880,15,C['ink'],maxlines=3)+4
            y+=p.link(ref['doi'],40,y,880,13,'https://doi.org/'+ref['doi'].replace('doi:',''))+12
        p.text('Architectural and mission context',40,374,880,14,C['navy'],True)
        for j,ref in enumerate(s.get('links',[])):p.link(ref['label'],40+j*295,400,280,12.5,ref['url'])
        p.text('Planned IEEE-formatted paper · venue unselected · manuscript unsubmitted',40,427,880,12,C['muted'])
    else:
        y=ytop
        for b in bs:y+=p.bullet(b,44,y,872,24 if len(bs)<=3 else 22)
    p.callout(s.get('takeaway',s.get('callout')),451)
    p.footer();return p

def rgb(s):return RGBColor.from_string(s)
def pptx_export(pages,out):
    prs=Presentation();prs.slide_width=Inches(13.3333333);prs.slide_height=Inches(7.5)
    for p in pages:
        sl=prs.slides.add_slide(prs.slide_layouts[6])
        for o in p.ops:
            x,y,w,h=[o.get(k,0)/72 for k in ['x','y','w','h']]
            if o['t']=='rect':
                sh=sl.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if o.get('r') else MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h));sh.fill.solid();sh.fill.fore_color.rgb=rgb(o['fill'])
                if o.get('stroke'):sh.line.color.rgb=rgb(o['stroke']);sh.line.width=Pt(.7)
                else:sh.line.fill.background()
                if o.get('r'):
                    try:sh.adjustments[0]=.06
                    except Exception:pass
            elif o['t']=='line':
                from pptx.enum.shapes import MSO_CONNECTOR
                sh=sl.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x),Inches(y),Inches(o['x2']/72),Inches(o['y2']/72));sh.line.color.rgb=rgb(o['color']);sh.line.width=Pt(o['lw'])
            elif o['t']=='image':sl.shapes.add_picture(o['path'],Inches(x),Inches(y),Inches(w),Inches(h))
            elif o['t']=='video':sl.shapes.add_movie(o['path'],Inches(x),Inches(y),Inches(w),Inches(h),poster_frame_image=o['poster'],mime_type='video/mp4')
            elif o['t']=='text':
                sh=sl.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=sh.text_frame;tf.margin_left=tf.margin_right=tf.margin_top=tf.margin_bottom=0;tf.word_wrap=False
                pp=tf.paragraphs[0];pp.space_before=pp.space_after=0
                from pptx.enum.text import PP_ALIGN
                pp.alignment=PP_ALIGN.RIGHT if o['align']=='right' else PP_ALIGN.CENTER if o['align']=='center' else PP_ALIGN.LEFT
                r=pp.add_run();r.text=o['s'];r.font.name='Liberation Sans';r.font.size=Pt(o['size']);r.font.bold=o['bold'];r.font.italic=o['italic'];r.font.color.rgb=rgb(o['color'])
                if o.get('url'):r.hyperlink.address=o['url']
        note=p.s.get('notes',p.s.get('speaker_notes',''))
        if isinstance(note,list):note='\n\n'.join(str(x) for x in note)
        meta=[]
        if p.s.get('speaker'):meta.append('Speaker: '+p.s['speaker'])
        if p.s.get('seconds'):meta.append('Planned duration: '+str(p.s['seconds'])+' seconds')
        sl.notes_slide.notes_text_frame.text='\n'.join(meta)+'\n\n'+str(note)
    prs.core_properties.title='VOLLEY: A Commanded Electromagnetic CubeSat Deployment Mechanism'
    prs.core_properties.author='Adityavardhan Mishra and Pratham Chawla'
    prs.core_properties.subject='Computational design and engineering evaluation'
    prs.save(out)

def pdf_export(pages,out):
    c=canvas.Canvas(str(out),pagesize=(W,H),pageCompression=1)
    c.setTitle('VOLLEY: A Commanded Electromagnetic CubeSat Deployment Mechanism');c.setAuthor('Adityavardhan Mishra and Pratham Chawla')
    for p in pages:
        c.bookmarkPage('slide'+str(p.index));c.addOutlineEntry(f'{p.index:02d} · {p.s.get("title","")}', 'slide'+str(p.index),0)
        for o in p.ops:
            if o['t']=='rect':
                c.setFillColor('#'+o['fill']);c.setStrokeColor('#'+(o.get('stroke') or o['fill']));c.setLineWidth(.7)
                c.roundRect(o['x'],H-o['y']-o['h'],o['w'],o['h'],o.get('r',0),fill=1,stroke=bool(o.get('stroke')))
            elif o['t']=='line':c.setStrokeColor('#'+o['color']);c.setLineWidth(o['lw']);c.line(o['x'],H-o['y'],o['x2'],H-o['y2'])
            elif o['t'] in ['image','video']:c.drawImage(o.get('poster',o['path']),o['x'],H-o['y']-o['h'],o['w'],o['h'])
            elif o['t']=='text':
                fn='Liberation-Italic' if o['italic'] else 'Liberation-Bold' if o['bold'] else 'Liberation';c.setFont(fn,o['size']);c.setFillColor('#'+o['color'])
                y=H-o['y']-o['size']*.92
                if o['align']=='right':c.drawRightString(o['x']+o['w'],y,o['s'])
                elif o['align']=='center':c.drawCentredString(o['x']+o['w']/2,y,o['s'])
                else:c.drawString(o['x'],y,o['s'])
                if o.get('url'):c.linkURL(o['url'],(o['x'],H-o['y']-o['h'],o['x']+o['w'],H-o['y']),relative=0,thickness=0)
        c.showPage()
    c.save()

def html_export(pages,out):
    ss=[]
    for p in pages:
        oo=[]
        for o in p.ops:
            style=f'left:{o.get("x",0)}px;top:{o.get("y",0)}px;'
            if o['t']=='text':
                st=html.escape(o['s'])
                if o.get('url'):st=f'<a style="color:inherit" href="{html.escape(o["url"],quote=True)}">{st}</a>'
                oo.append(f'<div class="text" style="{style}width:{o["w"]}px;height:{o["h"]}px;font-size:{o["size"]}px;color:#{o["color"]};font-weight:{700 if o["bold"] else 400};font-style:{"italic" if o["italic"] else "normal"};text-align:{o["align"]}">{st}</div>')
            elif o['t']=='rect':oo.append(f'<div class="shape" style="{style}width:{o["w"]}px;height:{o["h"]}px;background:#{o["fill"]};border:{.7 if o.get("stroke") else 0}px solid #{o.get("stroke") or o["fill"]};border-radius:{o.get("r",0)}px"></div>')
            elif o['t']=='image':oo.append(f'<img style="{style}width:{o["w"]}px;height:{o["h"]}px" src="assets/{Path(o["path"]).name}" alt="{html.escape(p.s.get("title",""))}">')
            elif o['t']=='video':oo.append(f'<video controls playsinline preload="metadata" style="{style}width:{o["w"]}px;height:{o["h"]}px" src="assets/{Path(o["path"]).name}" poster="assets/{Path(o["poster"]).name}" aria-label="CAD-derived explanatory motion"></video>')
            elif o['t']=='line':oo.append(f'<div class="shape" style="{style}width:{o["x2"]-o["x"]}px;height:{o["lw"]}px;background:#{o["color"]}"></div>')
        note=p.s.get('notes',p.s.get('speaker_notes',''));note='\n\n'.join(note) if isinstance(note,list) else str(note)
        ss.append(f'<section class="slide" data-notes="{html.escape(note,quote=True)}" aria-label="Slide {p.index}: {html.escape(p.s.get("title",""),quote=True)}">'+''.join(oo)+'</section>')
    doc='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>VOLLEY presentation</title><style>
@font-face{font-family:Liberation;src:url('assets/LiberationSans-Regular.ttf')}@font-face{font-family:Liberation;src:url('assets/LiberationSans-Bold.ttf');font-weight:700}*{box-sizing:border-box}body{margin:0;background:#091522;font-family:Liberation,Arial,sans-serif;overflow:hidden}.slide{position:absolute;left:50%;top:50%;width:960px;height:540px;display:none;transform:translate(-50%,-50%) scale(var(--scale,1));transform-origin:center center;overflow:hidden;background:#FAFCFD}.slide.active{display:block}.slide>*{position:absolute}.text{white-space:nowrap;line-height:1.18}.controls{position:fixed;bottom:9px;left:50%;transform:translateX(-50%);display:flex;gap:8px;align-items:center;background:#102238dc;padding:7px;border-radius:5px;color:#dce7ee;font-size:12px}button{color:#fff;background:#27465f;border:1px solid #587086;border-radius:3px;padding:5px 11px;cursor:pointer}.notes{position:fixed;right:12px;top:12px;width:340px;max-height:70vh;overflow:auto;color:#172D43;background:white;padding:18px;display:none;white-space:pre-wrap;font-size:16px;line-height:1.4}.notes.visible{display:block}@media print{body{overflow:visible;background:white}.slide{position:relative;left:0;top:0;display:block;transform:none;page-break-after:always}.controls,.notes{display:none}@page{size:13.333in 7.5in;margin:0}}</style><main>'''+''.join(ss)+'''</main><nav class="controls" aria-label="Presentation controls"><button onclick="go(-1)">←</button><span id="counter"></span><button onclick="go(1)">→</button><button onclick="toggleNotes()">Notes</button><button onclick="document.documentElement.requestFullscreen?.()">Full screen</button></nav><aside id="notes" class="notes"></aside><script>const slides=[...document.querySelectorAll('.slide')];let n=0;function resize(){document.documentElement.style.setProperty('--scale',Math.min(innerWidth/960,(innerHeight-42)/540))}function show(){slides.forEach((s,i)=>s.classList.toggle('active',i===n));document.getElementById('counter').textContent=`${n+1} / ${slides.length}`;document.getElementById('notes').textContent=slides[n].dataset.notes;location.hash=n+1}function go(d){n=Math.max(0,Math.min(slides.length-1,n+d));show()}function toggleNotes(){document.getElementById('notes').classList.toggle('visible')}document.addEventListener('keydown',e=>{if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(-1)}if(e.key==='Home'){n=0;show()}if(e.key==='End'){n=slides.length-1;show()}if(e.key.toLowerCase()==='n')toggleNotes()});addEventListener('resize',resize);n=Math.max(0,Math.min(slides.length-1,parseInt(location.hash.slice(1)||1)-1));resize();show();</script></html>'''
    for name in ['LiberationSans-Regular.ttf','LiberationSans-Bold.ttf','LiberationSans-Italic.ttf']:
        if (FONTDIR/name).resolve()!=(ROOT/'assets'/name).resolve():shutil.copyfile(FONTDIR/name,ROOT/'assets'/name)
    out.write_text(doc)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',nargs='?');ap.add_argument('--data');args=ap.parse_args()
    input_path=Path(args.data or args.input or (ROOT/'SLIDES.json' if (ROOT/'SLIDES.json').exists() else ROOT.parent/'SLIDES.json')).resolve()
    data=json.loads(input_path.read_text())
    slides=data if isinstance(data,list) else data.get('slides',[])
    appendix=[] if isinstance(data,list) else data.get('appendix',[])
    slides=[dict(s) for s in slides]+[dict(s,appendix=True) for s in appendix]
    for s in slides:
        for key in ['asset','movie','poster']:
            if s.get(key) and not Path(s[key]).is_absolute():s[key]=str((input_path.parent/s[key]).resolve())
        if s.get('message') and s.get('layout') not in ['title','closing']:s['takeaway']=s['message']
        if s.get('layout')=='title':
            s['subtitle']=s.get('message',data.get('title','').replace('VOLLEY: ',''))
            s['authors']='  ·  '.join(data.get('authors',[]))
            s['institution']=data.get('institution','')+'\nB.Tech · '+data.get('department','')
            s['guide']='Guide: '+data.get('guide','')
    # Presentation structure changes layout only; canonical claims remain in SLIDES.json.
    byid={str(s.get('id')):s for s in slides}
    for sid in ['8','9']:
        first=byid[sid]['bullets'][0]
        if ': ' in first:
            formula,explanation=first.split(': ',1)
            byid[sid]['formula']=formula;byid[sid]['formula_position']='image_top'
            byid[sid]['bullets'][0]=explanation[0].upper()+explanation[1:]
    def columns(sid,titles):
        s=byid[sid];s['columns']=[dict(title=t,bullets=[b]) for t,b in zip(titles,s['bullets'])]
    columns('2',['Problem and objectives','Mechanism and evaluation','Research programme'])
    byid['4']['headers']=['Prior work / study','Engineering focus']
    byid['4']['column_widths']=[.30,.70]
    byid['4']['rows']=[['Zhao et al. (2022)','Stacked electromagnetic deployment'],['Zhao et al. (2025)','Storage and transport interfaces'],['Feng et al. (2025)','Reachable-domain study'],['VOLLEY','Integrated custody, finite motor/source, arrest and mission burden']]
    for sid,summary in [('10','3 m/s command → 2.999864 m/s release · carrier stop position 1.507289 m'),('12','Paired closure: 0.285983 mm (CalculiX) · 0.286392 mm (primary ANSYS sample)'),('14','Host propellant: 0.2899 kg (VOLLEY) · 0.0536 kg (ideal ground-pretrim spring)')]:
        s=byid[sid];s['layout']='plot_big';s['takeaway']=summary
        s['notes']=s.get('notes','')+'\n\nDisplayed result context: '+'; '.join(s['bullets'])
        s['bullets']=[]
    columns('15',['Operating cycle','Coupled model','Engineering checks'])
    columns('17',['VOLLEY Labs','Reusable tools','Future interfaces'])
    for sid,titles in [('16',['Concept and architecture','Integrated evaluation','Prototype requirements']),('18',['Gen6 prototype','Higher-speed study','Long-term architecture'])]:
        byid[sid]['stages']=[dict(title=t,body=b) for t,b in zip(titles,byid[sid]['bullets'])]
    for sid,titles in [('A5',['Nominal source','Adverse source','Power stage']),('A8',['Temperature and time','Thermal measures','Encoded logic']),('A10',['New configuration','Model checks','Alternative design']),('A11',['Parking-orbit screen','Departure energy','Capture design']),('A12',['Publication','Reusable tools','Future interface'])]:columns(sid,titles)
    byid['A4']['formula']='Fₓ = ∫ (J × B)ₓ dV'
    byid['A7']['asset']=str(ROOT/'assets'/'chassis_mesh_and_paired_closure.jpg')
    byid['A7']['caption']='Native bare-chassis mesh and paired closure. Deformation ×20; assembled allowances are separate.'
    byid['A12']['layout']='references';byid['A12']['title']='Selected bibliography and research record'
    byid['A12']['references']=[
        dict(text='Y. Zhao et al. (2022). “Design and analysis of a new deployer for the in-orbit release of multiple stacked CubeSats.” Remote Sensing 14(17), 4205.',doi='doi:10.3390/rs14174205'),
        dict(text='Y. Zhao et al. (2025). “Simulation analysis and experimental verification of the transport characteristics of a high-volume CubeSat storage device.” Aerospace 12(6), 466.',doi='doi:10.3390/aerospace12060466'),
        dict(text='H. Feng, Y. Yang and Y. Wu (2025). “Design and reachable domain analysis of on-orbit electromagnetic launcher for CubeSats.” International Journal of Aerospace Engineering, 3000765.',doi='doi:10.1155/ijae/3000765')]
    byid['A12']['links']=[dict(label='ISRO · POEM-3 mission account',url='https://www.isro.gov.in/POEM-3_Mission_achieves_Payload_objectives.html'),dict(label='Rocket Lab · Electron guide v7.0',url='https://rocketlabcorp.com/assets/Electron-Payload-User-Guide-7.0-v6.pdf'),dict(label='NASA · Lunar surface technology',url='https://www.nasa.gov/lunar-surface-technology/')]
    # Both clips derive from the represented CAD sequence; display timing is edited.
    for sid,movie,poster in [('6','feed_and_capture.mp4','feed_poster.jpg'),('9','release_arrest_return.mp4','release_poster.jpg')]:
        mp=ROOT.parent/'media'/movie
        if mp.exists() and (ROOT/poster).exists():
            byid[sid]['movie']=str(mp);byid[sid]['poster']=str(ROOT/poster)
            byid[sid]['caption']='CAD-derived operating sequence; display timing edited. Static fallback shown.'
    pages=[render_page(s,i+1,len(slides)) for i,s in enumerate(slides)]
    (ROOT/'layout.json').write_text(json.dumps([dict(index=p.index,title=p.s.get('title'),ops=p.ops) for p in pages],ensure_ascii=False,indent=2))
    issues=[]
    for p in pages:
        for x,y,x2,y2,text in p.text_bounds:
            if x<0 or y<0 or x2>W+1 or y2>H:issues.append(dict(slide=p.index,text=text,bounds=[x,y,x2,y2]))
    (ROOT/'bounds_check.json').write_text(json.dumps({'slides':len(pages),'text_bounds_issues':issues},indent=2))
    if issues:raise ValueError(f'{len(issues)} text bounds errors; see bounds_check.json')
    pptx_export(pages,ROOT/'VOLLEY_Presentation.pptx');pdf_export(pages,ROOT/'VOLLEY_Presentation.pdf');html_export(pages,ROOT/'VOLLEY_Presentation.html')
    portable={k:data.get(k) for k in ['title','subtitle','authors','guide','institution','department','date','planned_duration_seconds','speaker_seconds']}
    portable_slides=[]
    for p in pages:
        s=dict(p.s)
        for key in ['asset','movie','poster']:
            if s.get(key):
                if key=='asset':
                    candidates=[o for o in p.ops if o['t']=='image'];s[key]='assets/'+Path(candidates[0]['path']).name if candidates else 'assets/'+Path(s.get('poster',s[key])).name
                else:s[key]='assets/'+Path(s[key]).name
        portable_slides.append(s)
    portable['slides']=portable_slides[:len(slides)-len(appendix)];portable['appendix']=portable_slides[len(slides)-len(appendix):]
    (ROOT/'SLIDES.json').write_text(json.dumps(portable,ensure_ascii=False,indent=2))
    manifest={'source':input_path.name,'source_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),'slide_count':len(pages),'core_count':len(slides)-len(appendix),'appendix_count':len(appendix),'exports':{}}
    for name in ['VOLLEY_Presentation.pptx','VOLLEY_Presentation.pdf','VOLLEY_Presentation.html']:
        f=ROOT/name;manifest['exports'][name]={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
    (ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(manifest,indent=2))
    route={'core_count':19,'appendix_count':12,'planned_seconds':sum(s.get('seconds',0) for s in slides),'slides':[]}
    notes=['# VOLLEY speaker notes','', 'Planned 15-minute route; actual rehearsal timing is recorded separately.','']
    for i,s in enumerate(slides):
        route['slides'].append({k:s.get(k) for k in ['id','title','speaker','seconds'] }|{'page':i+1,'appendix':bool(s.get('appendix'))})
        notes.extend([f'## {s.get("id")} · {s["title"]}',f'Page {i+1} · {s.get("speaker","")} · planned {s.get("seconds",0)} seconds','',s.get('notes','') or 'Technical question slide: use the displayed source and configuration boundaries.','', 'Sources: '+'; '.join(s.get('sources',[])),''])
    (ROOT/'ROUTE.json').write_text(json.dumps(route,ensure_ascii=False,indent=2));(ROOT/'SPEAKER_NOTES.md').write_text('\n'.join(notes))
if __name__=='__main__':main()
