"""Editable 17-slide, two-speaker VOLLEY computational-study presentation."""
from pathlib import Path
import json,hashlib,shutil,datetime
from PIL import Image
from pptx import Presentation
from pptx.util import Inches,Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE,MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN,MSO_ANCHOR
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;ASSET=HERE/'assets';ASSET.mkdir(exist_ok=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assets={p.name:{'source':'assets/'+p.name,'sha256':sha(p)} for p in ASSET.glob('*') if p.is_file()}
(HERE/'ASSET_SOURCES.json').write_text(json.dumps(assets,indent=2)+'\n')
input_paths=[ROOT/'cad/release/FINAL_CAD_MANIFEST.json',ROOT/'analysis/COUPLED_SHOT.json',ROOT/'analysis/FINITE_MOTOR.json',ROOT/'analysis/CURRENT_FIELD_FORCE.json',ROOT/'analysis/DESIGN_BUDGETS.json',ROOT/'verification/COUPLED_SHOT_REVIEW.json',ROOT/'mission/MISSION_CAPTURE.json',ROOT/'mission/MISSION_COMPARISON.json',ROOT/'academic/GEN5_FINAL_YEAR_REPORT.md']
inputs={str(p.relative_to(ROOT)):sha(p)for p in input_paths}
shot=json.loads((ROOT/'analysis/COUPLED_SHOT.json').read_text());case=next(c for c in shot['cases']if c['target_m_s']==3 and not c['adverse']and c['inductance_H']==2e-5)
budgets=json.loads((ROOT/'analysis/DESIGN_BUDGETS.json').read_text());review=json.loads((ROOT/'verification/COUPLED_SHOT_REVIEW.json').read_text());assert review['summary']['all_refined_cases_pass']
assert abs(shot['sled_mass_from_home_capture_kg']-13.127805767068676)<1e-8
P=Presentation();P.slide_width=Inches(13.333333);P.slide_height=Inches(7.5)
P.core_properties.title='VOLLEY: Design and Computational Evaluation of a Commanded Electromagnetic CubeSat Deployment Mechanism';P.core_properties.author='Adityavardhan Mishra; Pratham Chawla';P.core_properties.subject='B.Tech Mechanical Engineering computational design study';P.core_properties.keywords='VOLLEY, CubeSat, electromagnetic deployment, Gen5 ACR1';P.core_properties.last_modified_by='Adityavardhan Mishra; Pratham Chawla'
NAVY='102A43';COPPER='A9683D';INK='26384B';MUTED='617386';PALE='EFF3F7';BLUE='E4EDF5';WHITE='FFFFFF';LINE='CFD8E1'
FONT='Liberation Sans';records=[];notes=[]
times=[30,20,65,90,70,60,80,35,70,70,55,65,65,65,30,20,10]

def rect(s,x,y,w,h,fill=WHITE,line=None,radius=False):
 q=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h));q.fill.solid();q.fill.fore_color.rgb=RGBColor.from_string(fill)
 if line:q.line.color.rgb=RGBColor.from_string(line);q.line.width=Pt(.6)
 else:q.line.fill.background()
 return q

def text(s,value,x,y,w,h,size=20,color=INK,bold=False,align=PP_ALIGN.LEFT):
 q=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));tf=q.text_frame;tf.clear();tf.word_wrap=True;tf.margin_left=0;tf.margin_right=0;tf.margin_top=0;tf.margin_bottom=0
 for i,line in enumerate(value.split('\n')):
  p=tf.paragraphs[0]if i==0 else tf.add_paragraph();p.text=line;p.alignment=align;p.space_before=Pt(0);p.space_after=Pt(3);p.line_spacing=1.08
  for r in p.runs:r.font.name=FONT;r.font.size=Pt(size);r.font.bold=bold;r.font.color.rgb=RGBColor.from_string(color)
 return q

def bullet(s,items,x,y,w,size=21,gap=.74,color=INK):
 for i,value in enumerate(items):text(s,'•',x,y+i*gap,.20,.35,size=size,color=COPPER,bold=True);text(s,value,x+.30,y+i*gap,w-.30,gap-.08,size=size,color=color)

def line(s,x1,y1,x2,y2,color=COPPER,width=1.2):
 q=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2));q.line.color.rgb=RGBColor.from_string(color);q.line.width=Pt(width);return q

def picture(s,name,x,y,w,h,cad=False):
 path=ASSET/name
 with Image.open(path)as im:iw,ih=im.size
 ch=.79 if cad else 1;ratio=iw/(ih*ch);dw=min(w,h*ratio);dh=dw/ratio
 q=s.shapes.add_picture(str(path),Inches(x+(w-dw)/2),Inches(y+(h-dh)/2),width=Inches(dw),height=Inches(dh))
 if cad:q.crop_top=.095;q.crop_bottom=.115
 records[-1]['images'].append({'asset':name,'source':assets[name],'cad_caption_crop':{'top':.095,'bottom':.115}if cad else None})
 return q

def metric(s,value,label,x,y,w=3.0,h=1.1,fill=PALE,value_size=31):
 rect(s,x,y,w,h,fill);rect(s,x,y,.055,h,COPPER)
 if h<1:text(s,value,x+.18,y+.04,w-.30,.44,size=value_size,color=NAVY,bold=True);text(s,label,x+.18,y+.52,w-.30,h-.54,size=12.8,color=MUTED)
 else:text(s,value,x+.18,y+.12,w-.30,.48,size=value_size,color=NAVY,bold=True);text(s,label,x+.18,y+.67,w-.30,h-.69,size=14,color=MUTED)

def table(s,heads,rows,x,y,widths,row_h=.68,font=18):
 xx=x
 for head,w in zip(heads,widths):rect(s,xx,y,w,row_h,NAVY);text(s,head,xx+.12,y+.12,w-.22,row_h-.16,size=font,color=WHITE,bold=True);xx+=w
 for n,row in enumerate(rows):
  xx=x;yy=y+(n+1)*row_h
  for cell,w in zip(row,widths):rect(s,xx,yy,w,row_h,PALE if n%2==0 else WHITE);text(s,str(cell),xx+.12,yy+.11,w-.22,row_h-.12,size=font,color=INK);xx+=w

def new(title,section,source='',subtitle=''):
 s=P.slides.add_slide(P.slide_layouts[6]);n=len(P.slides);records.append({'slide':n,'title':title,'section':section,'images':[],'sources':source,'speaker':'Adityavardhan Mishra'if n<=8 else'Pratham Chawla','planned_seconds':times[n-1]})
 rect(s,0,0,13.333,.065,NAVY);text(s,'VOLLEY  /  GEN5 ACR1',.55,.16,7,.22,size=11,color=COPPER,bold=True);text(s,section.upper(),10.1,.16,2.68,.22,size=11,color=MUTED,align=PP_ALIGN.RIGHT)
 text(s,title,.55,.51,12.2,.70,size=28,color=NAVY,bold=True)
 if subtitle:text(s,subtitle,.55,1.18,12.2,.45,size=15.5,color=MUTED)
 line(s,.55,6.97,12.78,6.97,color=LINE,width=.7);text(s,source,.55,7.07,11.4,.24,size=10.2,color=MUTED);text(s,f'{n:02d} / 17',11.9,7.04,.86,.30,size=12,color=NAVY,align=PP_ALIGN.RIGHT)
 return s

def note(s,body):
 r=records[-1];start=sum(times[:r['slide']-1]);end=start+r['planned_seconds'];fmt=lambda t:f'{t//60}:{t%60:02d}'
 value=f"Speaker: {r['speaker']}\nPlanned time: {r['planned_seconds']} s ({fmt(start)}–{fmt(end)})\n\n{body}\n\nSource basis: {r['sources']}"
 s.notes_slide.notes_text_frame.text=value;notes.append({'slide':r['slide'],'title':r['title'],'speaker':r['speaker'],'seconds':r['planned_seconds'],'start_s':start,'end_s':end,'script':body,'source_basis':r['sources']})

# 1 — title
s=new('', 'B.Tech project presentation','Symbiosis Institute of Technology, Pune | October 2026')
text(s,'DEPARTMENT OF MECHANICAL ENGINEERING',.55,.61,8,.34,size=14,color=MUTED,bold=True);text(s,'VOLLEY',.55,1.30,7,.67,size=42,color=NAVY,bold=True)
text(s,'Design and Computational Evaluation\nof a Commanded Electromagnetic\nCubeSat Deployment Mechanism',.55,2.12,7.35,2.10,size=27,color=NAVY,bold=True)
text(s,'GEN5 ACR1  |  COMPUTATIONAL DESIGN STUDY',.57,4.28,7.2,.38,size=13.5,color=COPPER,bold=True)
text(s,'Adityavardhan Mishra\nPRN: 23070125054',.55,5.02,3.7,.85,size=18,color=INK);text(s,'Pratham Chawla\nPRN: 23070125029',4.20,5.02,3.6,.85,size=18,color=INK)
text(s,'Project guide: Vikas Gulia',.55,6.15,7,.42,size=19,color=INK);picture(s,'sit-logo.jpg',10.30,.53,2.45,.80);picture(s,'01_assembly_isometric.png',7.9,2.1,4.9,3.9,cad=True)
text(s,'Symbiosis Institute of Technology, Pune',7.9,6.22,4.9,.45,size=16,color=MUTED,align=PP_ALIGN.RIGHT)
note(s,'Good morning. We are Adityavardhan Mishra and Pratham Chawla, presenting VOLLEY under the guidance of Vikas Gulia. This project develops and computationally evaluates a commanded electromagnetic CubeSat deployment mechanism. The presentation focuses on the completed Gen5 ACR1 computational reference and the physical validation proposed for Gen6.')
# 2 — outline
s=new('Presentation outline','Outline','College presentation structure adapted to the VOLLEY study')
for n,(head,detail)in enumerate([('01  Motivation and prior work','Introduction, literature, research gap and objectives'),('02  Method and progress','Controlled configuration and dependent numerical models'),('03  Mechanism and results','Payload custody, finite motor, source, structure and mission'),('04  Conclusions and next steps','Study outcome, Gen6 prototype and references')]):
 y=1.65+n*1.18;rect(s,.65,y,12.0,.94,PALE);text(s,head,.87,y+.15,4.6,.44,size=23,color=NAVY,bold=True);text(s,detail,5.45,y+.21,6.95,.52,size=18,color=MUTED)
note(s,'We begin with the deployment problem and relevant prior work, then define the research gap and objectives. We explain the computational method and progress before moving to the mechanism and results. We close with the mission trade, conclusions and the proposed Gen6 validation programme.')
# 3 — introduction
s=new('Commanded release adds a local delivery variable','Introduction','Sources: JAXA deployment ICD; Cal Poly CDS Rev. 14.1; Foster et al. (2018); Vallado (2013)')
rect(s,.65,1.55,5.35,4.95,PALE);text(s,'DEPLOYMENT EVENT - SCHEMATIC',.90,1.80,4.9,.35,size=15,color=COPPER,bold=True)
planet=s.shapes.add_shape(MSO_SHAPE.OVAL,Inches(1.23),Inches(2.62),Inches(2.75),Inches(2.75));planet.fill.solid();planet.fill.fore_color.rgb=RGBColor.from_string(BLUE);planet.line.color.rgb=RGBColor.from_string(LINE)
text(s,'Earth',2.05,3.75,1.15,.40,size=21,color=MUTED,align=PP_ALIGN.CENTER);rect(s,4.35,2.68,.60,.42,NAVY);rect(s,5.06,2.40,.22,.22,COPPER);line(s,4.96,2.77,5.54,2.77,COPPER,2.2);text(s,'Host',4.30,3.25,1.2,.35,size=18,color=NAVY);text(s,'Relative\nrelease',4.65,3.85,1.0,.76,size=17,color=COPPER);text(s,'Concept only; arrows are not to scale.',.90,5.78,4.8,.45,size=13,color=MUTED)
bullet(s,['Host manoeuvres establish the carrier state.','A release command changes the payload initial condition relative to the host.','Retention, guidance, arrest and host recoil complete the system boundary.'],6.55,1.84,6.1,size=22,gap=1.27)
text(s,'Research question',6.85,5.86,5.5,.35,size=15,color=COPPER,bold=True);text(s,'Can a twelve-payload system complete a\ncoupled, reusable deployment cycle?',6.85,6.18,5.4,.66,size=19,color=NAVY,bold=True)
note(s,'A deployer is an interface between a host platform and a free-flying spacecraft. The host can manoeuvre before release, while the deployer sets a local relative velocity at a specific event. These are related but distinct controls. A release impulse can change orbital energy and subsequent phasing, and its usefulness depends on the delivery objective and the available host resources. Our schematic identifies the event rather than depicting a flight vehicle. The design question is therefore broader than generating force. The payload must remain retained and guided before command, the moving carrier must be arrested and returned, and its momentum and installed mass must remain in the mission budget. This is the system boundary used throughout the study.')
# 4 — literature
s=new('Prior work establishes the mechanisms and comparison context','Literature review','Sources: Zhao et al. (2022, 2025); Feng et al. (2025); Halbach (1980); Yamaguchi & Morishita (2023)')
table(s,['Published work','Evidence / interface','Implication for VOLLEY'],[
 ['Zhao et al., 2022\nStacked EM deployment','Gravity-compensated tests;\nstacked CubeSat release','Distinguish published measurements\nfrom the present computational results.'],
 ['Zhao et al., 2025\nHigh-volume storage','Receiving guides and magnetic transfer;\npayload grooves and iron patches','Define the passive payload interface\nand receiving custody explicitly.'],
 ['Feng et al., 2025\nEM reachable domain','Higher-speed launcher and\nmission-domain analysis','Couple the selected operating regime\nto its energy and mission assumptions.'],
 ['Halbach; finite-motor studies','Permanent-magnet field shaping\nand longitudinal end effects','Use finite magnet and conductor\ngeometry at launch and arrest.']
],.65,1.62,[3.05,4.48,4.50],row_h=.88,font=17)
text(s,'Study focus: integration and same-revision evaluation of a retained-carrier architecture.',.80,6.40,11.8,.40,size=20,color=NAVY,bold=True)
note(s,'Electromagnetic CubeSat deployment and high-volume storage are established prior art. Zhao and colleagues reported stacked electromagnetic release in 2022, including gravity-compensated laboratory tests. Their measured velocities belong to their mechanism, payloads and test conditions. The 2025 storage study examines pushing, receiving guides and magnetic transport, including spacecraft-side grooves and iron patches. That interface differs from the passive rectangular envelope represented here. Feng and colleagues examine a higher-speed launcher and reachable domain, which provides mission context but uses a different operating regime. Halbach supplies the permanent-magnet field concept, while finite-motor literature identifies the importance of longitudinal end effects. The present contribution is the integration and evaluation of one explicit retained-carrier reference: custody, finite force, source limits, arrest and host burden are assessed together. We preserve the distinction between third-party experimental evidence and our numerical results.')
# 5 — research gap
s=new('Research gap: closing the complete retained-carrier cycle','Research gap','Basis: literature synthesis and the defined Gen5 ACR1 system boundary')
for x,head,body in [( .65,'Who holds the payload?','A complete custody path through cell opening, receiving, docking and commanded departure.'),(4.80,'Can the source deliver it?','Finite force, actual moving mass, current dynamics and post-release arrest evaluated together.'),(8.95,'What does the host retain?','The reusable carrier, installed hardware, power allowance and recoil carried into mission comparison.')]:
 rect(s,x,1.85,3.73,3.75,PALE);rect(s,x,1.85,3.73,.07,COPPER);text(s,head,x+.22,2.20,3.28,.80,size=25,color=NAVY,bold=True);text(s,body,x+.22,3.28,3.28,1.90,size=21,color=INK)
text(s,'One controlled design links mechanical interfaces, electromechanics and mission resources.',.85,6.10,11.5,.64,size=24,color=NAVY,bold=True)
note(s,'The research gap addressed here is integration at a defined reference boundary. First, a storage-to-release mechanism needs an explicit answer to who holds the payload at every transition. Second, a useful electromagnetic result requires the force map, real moving mass and electrical source to be solved as one problem, including what happens after the spacecraft separates. Third, the retained carrier and installed hardware affect the host even when the payload has departed. The study connects these questions using one controlled mechanical revision. This supplies a reproducible basis for evaluating operating cases and for deciding which measurements a physical prototype must provide. It is a design-specific integration contribution rather than a claim that adjustable electromagnetic ejection is a new principle.')
# 6 — objectives
s=new('Objectives and controlled reference requirements','Objectives','Sources: frozen CAD manifest; PARAMETERS.json; coupled operating-study definition')
for x,y,value,label in [(.65,1.75,'12 × 4 kg','Identical 3U envelope surrogates'),(6.82,1.75,'1–3 m/s','Analysed commanded-speed cases'),(.65,3.23,'2250 mm','Guide-rail allocation'),(6.82,3.23,'210 mm','Post-release arrest allocation')]:metric(s,value,label,x,y,5.86,1.16,value_size=33)
bullet(s,['Define continuous payload custody and a reusable carrier cycle.','Evaluate finite motor force with the represented winding and magnet geometry.','Couple source, release and arrest; assess structural and mission consequences.'],.82,4.92,11.75,size=20,gap=.57)
note(s,'The reference manifest contains twelve identical four-kilogram 3U envelope surrogates. The represented contact envelope is 340.5 by 100 by 100 millimetres. The current computational operating study covers commands from one to three metres per second. The rail is 2250 millimetres long, and the post-release arrest allocation is 210 millimetres. Within this boundary, the objectives are to define continuous payload custody, evaluate the finite motor geometry, solve the coupled source and mechanical cycle, and carry the retained burden into structural and mission evaluation. These values identify the analysed configuration. The later mixed-size prototype will need its own payload interfaces and verification rather than inheriting this twelve-3U definition.')
# 7 — methods
s=new('Methodology follows the physical dependency chain','Research methodology','Sources: engineering manifests; finite field/current models; STEP readback and reviewed 5 µs timestep-audit records')
steps=[('1','Controlled CAD','Solids and\ncustody states'),('2','Mass and inertia','Solid ledger\nand allowances'),('3','Finite motor','Field and\ncurrent paths'),('4','Coupled shot','Source and\nrelease/arrest'),('5','Mechanical budgets','Chassis and\ninterfaces'),('6','Mission boundary','Release map\nand host mass')]
for i,(num,head,body)in enumerate(steps):
 x=.65+i*2.06;rect(s,x,2.0,1.88,2.32,PALE);text(s,num,x+.15,2.18,1.50,.48,size=31,color=COPPER,bold=True);text(s,head,x+.15,2.92,1.58,.66,size=18,color=NAVY,bold=True);text(s,body,x+.15,3.62,1.58,.59,size=14.5,color=MUTED)
 if i<5:line(s,x+1.90,3.10,x+2.04,3.10,COPPER,2)
text(s,'Computational cross-checks',.80,4.88,11.7,.42,size=22,color=NAVY,bold=True)
for x,head,body in [(.80,'Geometry','Native / STEP readback'),(4.95,'Electromagnetics','Source-face and current-FEM checks'),(9.10,'Dynamics','5 µs timestep audit (shared solver)')]:text(s,head,x,5.54,3.5,.37,size=18,color=COPPER,bold=True);text(s,body,x,5.99,3.5,.73,size=18,color=INK)
note(s,'The method follows the physical dependencies. CAD defines contact paths and conductor and magnet placement. The same solids and assigned reference masses produce the mass and inertia ledger. Finite electromagnetic and current models then define the force and resistance used by the source-coupled shot model. The shot includes unilateral payload contact, electrical braking, mechanical separation and active arrest of the retained carrier. Actual-chassis elasticity and declared clearance, thermal and contact budgets assess the mechanical consequences. Finally, the achieved release map and installed burden enter the host mission comparison. Independent checks supplement these models: STEP imports are compared with native geometry, a source-face field formulation and conductor-current FEM check the electromagnetic calculation, and an independently reviewed five-microsecond timestep audit checks the principal three-metre-per-second cases using the shared production solver. These are computational checks with distinct purposes; they do not replace future physical correlation.')
# 8 — progress
s=new('Timeline and work progress','Timeline / work progress','Current submission: October 2026 | Gen6 physical prototype is future development')
stages=[('Problem and literature','Complete'),('Gen5 ACR1 definition','Complete'),('Coupled computational study','Complete'),('Report and presentation','Current submission'),('Gen6 instrumented prototype','Future work')]
for i,(head,status)in enumerate(stages):
 x=.65+i*2.49;fill=PALE if i<4 else BLUE;rect(s,x,2.08,2.29,2.80,fill);text(s,f'{i+1:02d}',x+.17,2.31,1.9,.43,size=28,color=COPPER,bold=True);text(s,head,x+.17,3.08,1.96,.86,size=20,color=NAVY,bold=True);text(s,status,x+.17,4.24,1.96,.45,size=15.5,color=MUTED)
text(s,'Completed outcome',.80,5.55,3.4,.35,size=15,color=COPPER,bold=True);text(s,'A controlled computational design reference with defined operating cases and a hardware validation programme.',.80,5.98,11.7,.72,size=24,color=NAVY,bold=True)
note(s,'The work has progressed from literature and problem framing to the Gen5 ACR1 reference, followed by the coupled computational study. The current stage is the academic report and presentation capture. The computational design study is complete within its stated reference cases. Gen6 is the proposed physical development stage, beginning with an instrumented mixed 1U and 3U prototype. Pratham will now explain the reference mechanism and the engineering results.')
# 9 — architecture
s=new('Reference architecture: fixed banks and one captive pallet','Architecture','Native CAD render: final Gen5 ACR1 home state; represented masses include declared reference components')
picture(s,'01_assembly_isometric.png',.53,1.53,8.35,4.97,cad=True)
metric(s,'2 × 6 cells','Fixed, individually retained storage',9.13,1.68,3.55,1.10)
metric(s,'13.128 kg','Retained moving carrier + pallet',9.13,3.00,3.55,1.10)
metric(s,'149.557 kg','Represented dry CAD mass',9.13,4.32,3.55,1.10)
text(s,'+7 kg power/control allowance',9.20,5.76,3.5,.40,size=16,color=COPPER,bold=True);text(s,'Magnet arrays stay on the carrier.',9.20,6.28,3.45,.42,size=15.5,color=MUTED)
note(s,'The reference mechanism has two fixed banks with six cells per bank. Positive guided pushers feed one selected payload toward the central lift. The lift carries a single captive pallet, and that same physical pallet docks to the launch carrier. The magnet arrays remain on the reusable carrier rather than on the payload. This is the complete native CAD home state, including the storage banks and generic mounting ladder. The retained moving carrier, pallet, lock pins and reference actuators total 13.128 kilograms. Represented dry CAD mass is 149.557 kilograms, with a separate seven-kilogram power and control allowance. These masses are part of the system assessment. They are material-volume and assigned-reference totals, rather than a weighed physical article.')
# 10 — custody
s=new('Capture before release: three explicit custody states','Feeder and pallet','Native CAD states; handoff detail hides banks, host ladder and fixed lift frame as disclosed in its provenance')
for x,name,head,body in [(.58,'03_captured_source_level.png','1  Capture at the source','Lift grips support the pallet; end frames and Y keepers contain the payload.'),(4.78,'02_handoff_pallet_locks.png','2  Dock and lock','Carrier caps and both bayonets engage before the outboard lift grips open.'),(8.98,'04_clear_docked.png','3  Raise clear','The pallet stays on the carrier through release, arrest and return.')]:
 picture(s,name,x,1.64,3.79,2.60,cad=True);text(s,head,x,4.44,3.8,.54,size=21,color=NAVY,bold=True);text(s,body,x,5.12,3.77,1.08,size=18,color=INK)
rect(s,.65,6.36,12.0,.40,PALE);text(s,'Passive cam: 12 mm forekeeper opening over 50 mm travel, complete 5 mm before release.',.83,6.41,11.6,.30,size=17,color=COPPER,bold=True)
note(s,'These are three native CAD states of the same mechanism. At the source level, the lift grips support the pallet while the end frames and Y keepers contain the spacecraft envelope. At docking, four pallet feet land on the carrier. The upper capture caps and the two keyed bayonet locks engage before the lift grip pins retract, so the sequence explicitly captures before releasing custody. The lift then raises clear while the pallet remains attached to the carrier for launch, arrest and return. The handoff view omits the banks, host ladder and fixed lift frame to expose the interfaces, and that omission is disclosed. During the shot, fixed passive cams open the two forekeepers over fifty millimetres of carrier travel. Their twelve-millimetre opening completes five millimetres before release. This separates the slow transfer actuation from the position-defined release motion.')
# 11 — finite motor
s=new('Finite motor geometry enters the force model','Electromagnetic simulation','Sources: FINITE_MOTOR.json; CURRENT_FIELD_FORCE.json | coefficients use peak phase amperes')
picture(s,'magnetic_gap_section.png',.55,1.58,5.05,3.30);picture(s,'finite_force_coefficient.png',5.92,1.58,6.85,3.30)
metric(s,'42 + 42 magnets','8 mm blocks on opposed retained arrays',.65,5.10,3.80,1.11,value_size=29)
metric(s,'216 active bars','42 mm² bars; 21 mm² return necks',4.77,5.10,3.80,1.11,value_size=29)
metric(s,'0.172%','Interior current-FEM force difference',8.89,5.10,3.80,1.11,value_size=29)
text(s,'At x = 0.65 m: active 1.3287 N/A; represented returns included 1.3991 N/A.',.80,6.49,11.8,.35,size=17,color=NAVY,bold=True)
note(s,'The motor uses forty-two discrete eight-millimetre magnet blocks on each opposed carrier array and a finite three-phase stator with two hundred and sixteen active bars. The active bar section is forty-two square millimetres, while the minimum represented return neck is twenty-one. Force is obtained by integrating current density crossed with the finite permanent-magnet field over copper. At the checked interior station, active conductors give 1.3287 newtons per peak phase ampere; including the represented returns gives 1.3991. The conductor-current finite-element comparison differs by 0.172 percent at that interior station. Position dependence is retained for launch and arrest. These comparisons support the specified numerical model; static force and back-emf measurements remain part of Gen6.')
# 12 — shot and thermal
s=new('Coupled shot: release, source and active arrest','Simulation results','Numerical source-coupled model; nominal 3 m/s, 20 µH trace | sensitivity values retain their declared assumptions')
picture(s,'coupled_shot_reference.png',.55,1.55,5.60,5.16);picture(s,'shot_energy_ledger.png',6.40,1.60,6.32,2.75)
metric(s,f"{case['release']['relative_speed_m_s']:.3f} m/s",'Model release speed',6.55,4.50,2.91,1.01,value_size=25)
metric(s,f"{case['cap_draw_J']:.1f} J",'Nominal source draw',9.68,4.50,2.91,1.01,value_size=25)
text(s,'6/6 cases pass the 5 µs timestep audit',6.55,5.73,6.05,.38,size=18,color=NAVY,bold=True)
text(s,'Worst reviewed single-shot adiabatic estimates:\nBulk ≤0.0667 K; local DC-FE mesh observation 2.495 K.',6.55,6.22,6.05,.56,size=14.5,color=MUTED)
note(s,'The left plot shows the nominal twenty-microhenry, three-metre-per-second source-coupled reference. Current accelerates the retained carrier and spacecraft, then reverses for active arrest after mechanical separation. The signed current is therefore negative during braking. Model release is 2.999864 metres per second, and the carrier stops at 1.507 metres of relative travel, inside the 210-millimetre post-release allocation. Nominal source draw is 379.7 joules, apportioned in the energy ledger. All six principal three-metre-per-second cases, spanning nominal and adverse assumptions and three inductance values, pass the independently reviewed five-microsecond timestep audit, which shares the production simulation implementation. The thermal values shown are the worst reviewed sensitivity estimates, not the nominal trace alone: 0.0667 kelvin bulk copper rise and a 2.495-kelvin local DC-current-FEM adiabatic mesh observation. They define physical correlation priorities rather than a measured hotspot rating.')
# 13 — structure and contact
s=new('Mechanical evaluation: actual chassis and declared contact budgets','Structure and contact','Sources: actual-chassis CalculiX solve; DESIGN_BUDGETS.json | simulations and analytical bounds')
picture(s,'ACTUAL_CHASSIS_RESULT.png',.55,1.66,8.10,3.42)
text(s,'Linear-elastic FEA; 3.010 kN per array; displacement shown ×20.',.70,5.11,7.8,.52,size=15.5,color=MUTED)
metric(s,'0.286 mm','Maximum paired face closure',.70,5.87,3.76,.82,value_size=27)
metric(s,'0.372 mm','Declared 1.3× linear load sensitivity',4.65,5.87,3.76,.82,value_size=27)
text(s,'Allocated per-face gap margin',9.00,1.84,3.45,.72,size=20,color=NAVY,bold=True);text(s,'0.264 mm',9.00,2.61,3.50,.59,size=31,color=COPPER,bold=True)
text(s,'Four-rail contact surrogate',9.00,3.57,3.55,.61,size=20,color=NAVY,bold=True);text(s,'Elastic-energy rate bounds',9.00,4.20,3.52,.50,size=16,color=MUTED)
text(s,'1.044°/s  pitch/yaw\n2.619°/s  all-axis',9.00,4.86,3.55,1.09,size=23,color=COPPER,bold=True)
text(s,'Declared stiffness and inertia.\nGen6 physical correlation.',9.00,6.15,3.55,.57,size=14.5,color=MUTED)
note(s,'The structural figure uses the actual connected chassis, including its final shaft and axle bores, rather than an idealised rectangular section. Linear elasticity assumes seventy gigapascals Young’s modulus and Poisson’s ratio 0.33, with 3.010 kilonewtons applied inward on each magnet-array patch. Displacements are enlarged twenty times in the visualisation. Maximum paired face closure is 0.286 millimetres. Scaling the same linear solution by 1.3 gives 0.372 millimetres. Combining this with the declared centring, flatness, assembly and thermal allocations leaves a 0.264-millimetre per-face design margin. The contact figures are a separate elastic-energy bound for a declared four-rail surrogate: 1.044 degrees per second in pitch or yaw and 2.619 degrees per second over all axes. These are analytical bounds, not measured tip-off. Physical stiffness, inertia, friction and contact behaviour are future correlation measurements.')
# 14 — mission
s=new('Mission trade: retain the complete mass and control boundary','Mission results','Accepted finite-burn comparison: same 500 kg wet bus and twelve 4 kg payloads; tested policy families')
picture(s,'MISSION_RESOURCES.png',.55,1.55,12.22,4.50)
text(s,'Ideal pretrim uses less fuel and retained mass in this comparison.',.75,6.26,11.9,.38,size=20,color=NAVY,bold=True)
text(s,'Control families: Gen5 has 400 s coast-only releases; spring policies allow broader burns.',.75,6.68,11.9,.25,size=12.5,color=MUTED)
note(s,'The mission comparison keeps the same five-hundred-kilogram wet bus, including twenty kilograms of propellant, and twelve four-kilogram payloads. Corrected Gen5 initial wet mass is 704.557 kilograms, compared with 620 kilograms for the declared spring class assumption. For uniform two-metre-per-second targets, Gen5 uses 0.05244 kilograms of fuel and the fixed two-metre-per-second spring case uses 0.04696. For alternating one and three targets, Gen5 meets the five-newton ceiling with about 0.28987 kilograms, while ideal ground pretrim uses about 0.05365 at five newtons and also has a tested one-newton solution. The fixed-two spring family’s minimum tested peak is 7.537 newtons; this is not a global infeasibility proof. Gen5 uses four-hundred-second coast-only release windows while spring policies allow broader burns. The result establishes no mass or fuel advantage over ideal pretrim under these stated families. A separate native Orekit replay checks the accepted mission trajectories.')
# 15 — conclusions
s=new('Conclusions of the computational design study','Conclusion','Basis: controlled Gen5 ACR1 geometry, coupled simulations, independent checks and mission comparison')
for i,(head,body)in enumerate([('A complete reference cycle is defined','Fixed cells, guided feed, positive pallet capture, commanded release, active arrest and return.'),('The declared low-speed cases are computationally supported','1–3 m/s cases analysed; the principal 3 m/s matrix passes a reviewed shared-solver timestep audit.'),('The retained system burden is visible','149.557 kg represented dry CAD plus 7 kg allowance; no resource advantage over ideal pretrim in the stated mission comparison.')]):
 y=1.72+i*1.52;rect(s,.65,y,12.0,1.35,PALE);rect(s,.65,y,.065,1.35,COPPER);text(s,head,.90,y+.15,11.45,.40,size=23,color=NAVY,bold=True);text(s,body,.90,y+.68,11.45,.62,size=19,color=INK)
text(s,'Gen5 ACR1 completes the computational reference for physical validation.',.85,6.46,11.6,.41,size=22,color=NAVY,bold=True)
note(s,'The study produces a complete computational reference for a repeated deployment cycle, from retained storage to carrier return. The declared low-speed cases are evaluated with finite motor geometry, actual retained mass and a stated source, and the principal three-metre-per-second cases receive an independently reviewed shared-solver timestep audit. The system burden remains substantial and the mission comparison supplies no mass or fuel advantage over ideal pretrim. This defines the outcome and the next physical validation step.')
# 16 — future
s=new('Gen6: an instrumented mixed 1U / 3U physical prototype','Future work','Proposed development programme; no measured VOLLEY prototype performance is reported')
for x,head,body in [(.65,'1  Characterise','Force / back emf\nResistance and inductance\nSource ESR and switching'),(4.80,'2  Correlate custody','Pusher and guide forces\nPallet and lock repeatability\nPayload contact and angular rate'),(8.95,'3  Demonstrate the cycle','Release and active arrest\nRepeated thermal duty\nMixed-envelope handling')]:
 rect(s,x,1.85,3.73,3.65,PALE);text(s,head,x+.22,2.18,3.28,.66,size=23,color=NAVY,bold=True);text(s,body,x+.22,3.14,3.28,1.94,size=20,color=INK)
text(s,'Further scaling requires fresh stroke, acceleration, energy, arrest and heat-rejection budgets.',.85,6.12,11.5,.66,size=23,color=COPPER,bold=True)
note(s,'Gen6 is the proposed physical prototype stage. It should characterise the motor and source, correlate custody and contact behaviour, and then demonstrate instrumented release, arrest and repeated duty. Mixed one-unit and three-unit handling needs fresh envelopes, retention definitions and mass accounting. Higher-speed scaling requires new coupled energy, acceleration, arrest and thermal budgets.')
# 17 — references
s=new('Selected references','References','Full bibliography, source data sheets and engineering provenance accompany the report')
refs=[
 'Cal Poly, CubeSat Design Specification, Rev. 14.1, 2022; JAXA, JEM small-satellite deployment ICD.',
 'Zhao et al., “Design and analysis of a new deployer for the in-orbit release of multiple stacked CubeSats,” Remote Sensing 14, 4205, 2022. doi:10.3390/rs14174205.',
 'Zhao et al., “Simulation analysis and experimental verification of the transport characteristics of a high-volume CubeSat storage device,” Aerospace 12, 466, 2025. doi:10.3390/aerospace12060466.',
 'Feng, Yang and Wu, “Design and reachable domain analysis of on-orbit electromagnetic launcher for CubeSats,” IJAE, 3000765, 2025.',
 'Halbach, “Design of permanent multipole magnets with oriented rare earth cobalt material,” NIM 169, 1–10, 1980.',
 'Yamaguchi and Morishita, “End effects of Halbach field magnet-type linear motor,” Electrical Engineering in Japan, 2023. doi:10.1002/eej.23450.',
 'Foster et al., “Constellation phasing with differential drag on Planet Labs satellites,” Journal of Spacecraft and Rockets 55(2), 2018.',
 'Vallado, Fundamentals of Astrodynamics and Applications, 4th ed., 2013.',
 'Component references: Eaton TV cells; Infineon IRFP4668PbF; Texas Instruments UCC21520; FAULHABER 3242 BX4 and 32GPT.',
 'Methods: FreeCAD; Magpylib (SoftwareX 11, 100466); Gmsh (IJNME 79, 1309–1331); CalculiX; Blender.'
]
for i,r in enumerate(refs):
 col=0 if i<5 else 1;row=i%5;text(s,f'{i+1:02d}',.65+col*6.18,1.63+row*.95,.35,.32,size=13,color=COPPER,bold=True);text(s,r,1.06+col*6.18,1.63+row*.95,5.56,.92,size=12.8,color=INK)
text(s,'Questions',.80,6.57,11.8,.39,size=22,color=NAVY,bold=True)
note(s,'These selected references support the interface assumptions, prior-work comparison and numerical methods. The full bibliography and traceable engineering records accompany the report. Thank you; we welcome questions.')
assert len(P.slides)==17 and sum(times)==900 and sum(times[:8])==450 and sum(times[8:])==450
out=HERE/'VOLLEY_BTech_Presentation.pptx';temporary=HERE/'VOLLEY_BTech_Presentation.tmp.pptx';P.save(temporary);temporary.replace(out)
(HERE/'SPEAKER_NOTES.json').write_text(json.dumps(notes,indent=2)+'\n')
lines=['# VOLLEY — 15-minute two-speaker presentation','', 'Delivery allocation: Adityavardhan Mishra, slides 1–8 (7 min 30 s); Pratham Chawla, slides 9–17 (7 min 30 s). This allocates speaking time without assigning individual research contributions.','']
for n in notes:lines += [f"## {n['slide']:02d}. {n['title']}",f"{n['speaker']} — {n['seconds']} seconds",'',n['script'],'']
(HERE/'SPEAKER_NOTES.md').write_text('\n'.join(lines))
manifest={'title':P.core_properties.title,'authors':[{'name':'Adityavardhan Mishra','PRN':'23070125054'},{'name':'Pratham Chawla','PRN':'23070125029'}],'guide':'Vikas Gulia','slide_count':17,'planned_duration_s':900,'speakers':[{'name':'Adityavardhan Mishra','slides':[1,8],'seconds':450},{'name':'Pratham Chawla','slides':[9,17],'seconds':450}],'template_structure_source':'Department B.Tech presentation format; implemented in this source','input_sha256':inputs,'asset_sources':assets,'slides':records,'build_script_sha256':sha(Path(__file__)),'pptx_sha256':sha(out),'statement':'Completed computational design study; Gen6 physical prototype is proposed future work. No individual research contributions are assigned.'}
(HERE/'PRESENTATION_PROVENANCE.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('BUILT',out,len(P.slides),sum(times),flush=True)
