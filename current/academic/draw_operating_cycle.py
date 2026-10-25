"""Draw the selected custody sequence as an exportable engineering diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
A=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,4.8));fig.patch.set_facecolor('white');ax.set(xlim=(0,12),ylim=(0,4.8));ax.axis('off')
items=[('1  INDEX','Lift grips hold pallet;\nreceiver aligns with cell.'),('2  TRANSFER','Selected pusher feeds payload;\nend frames and keepers retain it.'),('3  DOCK','Pallet feet land; carrier caps\nand bayonet locks engage.'),('4  CLEAR','Lift grips retract only after\ncarrier capture; lift rises.'),('5  ACCELERATE','Home index withdraws;\nLSM drives sled + payload.'),('6  RELEASE','Cams open keepers; contact\nreaction reaches zero.'),('7  ARREST','LSM stops the retained\ncarrier + pallet in 210 mm.'),('8  RETURN','Powered return; home indexing\nprecedes reverse pallet handoff.')]
positions=[(0.15,2.72),(3.15,2.72),(6.15,2.72),(9.15,2.72),(9.15,.35),(6.15,.35),(3.15,.35),(.15,.35)]
for i,((title,detail),(x,y)) in enumerate(zip(items,positions)):
 box=FancyBboxPatch((x,y),2.7,1.45,boxstyle='round,pad=0.02,rounding_size=0.06',facecolor='#edf3f7',edgecolor='#334e68',linewidth=1.2);ax.add_patch(box)
 ax.text(x+.13,y+1.10,title,fontsize=11,fontweight='bold',color='#17364c',va='center')
 ax.text(x+.13,y+.60,detail,fontsize=9,va='center',linespacing=1.5,color='#172b3a')
 if i<7:
  xx,yy=positions[i+1]
  if yy==y:
   begin=(x+2.7,y+.72) if xx>x else (x,y+.72);end=(xx,yy+.72) if xx>x else (xx+2.7,yy+.72)
  else:begin=(x+1.35,y);end=(xx+1.35,yy+1.45)
  ax.add_patch(FancyArrowPatch(begin,end,arrowstyle='-|>',mutation_scale=13,linewidth=1.3,color='#334e68'))
ax.text(6,2.30,'ONE PHYSICAL PALLET  •  POSITIVE CUSTODY THROUGH HANDOFF  •  MOTOR ARREST AND RETURN',ha='center',va='center',fontsize=10,color='#17364c',fontweight='bold')
fig.subplots_adjust(0,0,1,1)
for suffix in ['png','pdf','svg']:fig.savefig(A/'assets'/('operating_cycle.'+suffix),dpi=180,bbox_inches='tight',pad_inches=.08)
