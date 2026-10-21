"""Build one coherent blackbook PDF and editable DOCX from the local report source."""
from pathlib import Path
import subprocess,json,hashlib,platform,copy,re
from docx import Document
from docx.shared import Pt,Mm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
R=Path(__file__).resolve().parents[1];U=R/'university';L=U/'layout'

def field(p,command):
 r=OxmlElement('w:r');f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),command);r.append(f);p._p.append(r)

def reference(path):
 d=Document();sec=d.sections[0];sec.page_width=Mm(210);sec.page_height=Mm(297)
 sec.left_margin=Mm(32);sec.right_margin=Mm(25);sec.top_margin=sec.bottom_margin=Mm(25)
 for name,size in [('Normal',12),('Body Text',12),('Title',18),('Subtitle',12),('Heading 1',18),('Heading 2',14),('Heading 3',12),('Caption',10)]:
  s=d.styles[name];s.font.name='Times New Roman';s.font.size=Pt(size);s.paragraph_format.line_spacing=1.35
  if name.startswith('Heading'):s.font.bold=True
 d.styles['Heading 1'].paragraph_format.page_break_before=True
 d.styles['Normal'].paragraph_format.space_after=Pt(6)
 p=sec.footer.paragraphs[0];p.alignment=1;field(p,'PAGE')
 setting=OxmlElement('w:updateFields');setting.set(qn('w:val'),'true');d.settings.element.append(setting)
 d.save(path)

def frontmatter(path):
 d=Document(path);new=Document();new.styles['Normal'].font.name='Times New Roman';new.styles['Normal'].font.size=Pt(12)
 for text,bold,size in [('A THESIS ON',True,12),('VOLLEY',True,18),('Design and Computational Feasibility Assessment of a Commanded Electromagnetic CubeSat Deployment Mechanism',True,16),('THESIS SUBMITTED IN PARTIAL FULFILLMENT OF THE REQUIREMENT FOR THE AWARD OF THE DEGREE',False,12),('BACHELOR OF TECHNOLOGY IN MECHANICAL ENGINEERING',True,14),('SUBMITTED BY',True,12),('Adityavardhan Mishra — 23070125054',False,12),('Pratham Chawla — 23070125029',False,12)]:
  p=new.add_paragraph();p.alignment=1;r=p.add_run(text);r.bold=bold;r.font.size=Pt(size)
 p=new.add_paragraph();p.alignment=1;p.add_run().add_picture(str(U/'final_review_2026_10_10/assets/sit-logo.jpg'),height=Mm(18))
 for text in ['Under the Guidance of Vikas Gulia','SYMBIOSIS INSTITUTE OF TECHNOLOGY','A constituent of Symbiosis International (Deemed University), Pune — 412115','2026','First similarity-review issue · 21 October 2026']:
  p=new.add_paragraph(text);p.alignment=1
 new.add_page_break();new.add_paragraph('Certification','Heading 1');new.add_paragraph('Unsigned review issue')
 new.add_paragraph('This report is presented by Adityavardhan Mishra (23070125054) and Pratham Chawla (23070125029) for academic review in the Bachelor of Technology programme in Mechanical Engineering at Symbiosis Institute of Technology, Pune. The project guide identified for the report is Vikas Gulia.')
 new.add_paragraph('The certification fields are reserved for institutional review and approval. No signature, approval, similarity result or completed certification is represented in this issue.')
 for role in ['Adityavardhan Mishra','Pratham Chawla','Project guide','Head of Department','Director','Date']:new.add_paragraph(role+': __________________________')
 new.add_page_break();new.add_paragraph('Acknowledgements','Heading 1');new.add_paragraph('The authors acknowledge the Department of Mechanical Engineering at Symbiosis Institute of Technology and project guide Vikas Gulia. Published research, public interface specifications and scientific software are credited in the bibliography and technical records. Their use does not imply endorsement of the design.')
 new.add_page_break();new.add_paragraph('Contents','Heading 1');field(new.add_paragraph(),'TOC \\o "1-2" \\h \\z \\u');new.add_page_break()
 for label in ['Figure','Table']:
  new.add_paragraph('List of '+label.lower()+'s','Heading 1');field(new.add_paragraph(),'TOC \\h \\z \\c "'+label+'"');new.add_page_break()
 # Copy only body blocks, preserving the content's own section properties and embedded media.
 # The sole front-matter image reuses an existing image relationship from the report only after registration.
 for el in list(new.element.body)[:-1]:
  for blip in el.xpath('.//a:blip'):
   old=blip.get(qn('r:embed'));part=new.part.related_parts[old]
   import io
   relation,_=d.part.get_or_add_image(io.BytesIO(part.blob));blip.set(qn('r:embed'),relation)
 for el in reversed(list(new.element.body)[:-1]):d.element.body.insert(0,copy.deepcopy(el))
 # Supply editable chapter labels and native caption sequence fields.
 chapters=['Introduction and problem definition','Objectives and study scope','Literature review and research contribution','Research methodology and governing models','Controlled Gen5 configuration','Electromagnetic drive, power and control analysis','CAD integration, packaging and installed mass','Orbital mechanics and matched mission comparison','Results and engineering discussion','Computational resources and limitations','Conclusion and future development']
 appendices=['Numerical and CAD evidence trail','Development history','Separate Gen6 research studies']
 roman=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI'];prefix=None;sub=0
 for p in d.paragraphs:
  text=p.text
  if p.style.name=='Heading 1':
   sub=0
   if text in chapters:
    i=chapters.index(text);prefix=str(i+1);p.text='CHAPTER '+roman[i]+' — '+text
   elif text in appendices:
    prefix=chr(65+appendices.index(text));p.text='APPENDIX '+prefix+' — '+text
   else:prefix=None
  elif p.style.name=='Heading 2' and prefix:
   sub+=1;p.text=prefix+'.'+str(sub)+' '+text
  match=re.match(r'^(Figure|Table) (\d+):\s*(.*)',text,re.S)
  if match:
   kind,number,caption=match.groups();p.clear();p.style='Caption';p.add_run(kind+' ')
   f=OxmlElement('w:fldSimple');f.set(qn('w:instr'),'SEQ '+kind+' \\* ARABIC')
   run=OxmlElement('w:r');t=OxmlElement('w:t');t.text=number;run.append(t);f.append(run);p._p.append(f);p.add_run(': '+caption)
 d.core_properties.title='VOLLEY: Design and Computational Feasibility Assessment of a Commanded Electromagnetic CubeSat Deployment Mechanism'
 d.core_properties.author='Adityavardhan Mishra; Pratham Chawla'
 d.core_properties.subject='First similarity-review issue,21 October2026;no approval or similarity result asserted'
 d.core_properties.comments=''
 d.save(path)

def main():
 import tempfile
 with tempfile.TemporaryDirectory(prefix='volley-report-') as tmp:
  ref=Path(tmp)/'reference.docx';reference(ref)
  common=['pandoc',str(U/'GEN5_FINAL_YEAR_REPORT.md'),'--resource-path='+str(U)+':'+str(R),'--lua-filter='+str(L/'evidence-links.lua'),'-M','title=','-M','author=','-M','date=']
  subprocess.run(common+['--pdf-engine=xelatex','-V','documentclass=report','--top-level-division=chapter','--number-sections','--include-in-header='+str(L/'blackbook-header.tex'),'--include-before-body='+str(L/'blackbook-frontmatter.tex'),'-o',str(U/'GEN5_FINAL_YEAR_REPORT.pdf')],cwd=R,check=True)
  subprocess.run(common+['--reference-doc='+str(ref),'-o',str(U/'GEN5_FINAL_YEAR_REPORT.docx')],cwd=R,check=True)
  frontmatter(U/'GEN5_FINAL_YEAR_REPORT.docx')
 print('Built blackbook PDF and editable DOCX; review approval and similarity result remain external.')
if __name__=='__main__':main()
