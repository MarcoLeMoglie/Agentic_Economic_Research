#!/usr/bin/env python3
"""Create reproducible *illustrative* UI captures for a course demo.
These are clearly labeled demo mockups, NOT screenshots of an installed Obsidian release.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math, random
random.seed(12)
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'assets/screens'; OUT.mkdir(parents=True,exist_ok=True)
W,H=1600,900
B='#0F1724'; SIDE='#141D2C'; PANEL='#1A2638'; LINE='#2B3D51'; WHITE='#EDF4FA'; MUTED='#93A5B7'; BLUE='#79B6E8'; AMBER='#F5A646'; GREEN='#65D7B1'; PURPLE='#B19BEA'
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if not Path(FONT).exists(): FONT='/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf';FONT_B=FONT
fs=lambda z,b=False:ImageFont.truetype(FONT_B if b else FONT,z)
def rr(d,coords,fill,outline=None,r=14,width=2):d.rounded_rectangle(coords,radius=r,fill=fill,outline=outline,width=width)
def text(d,xy,t,size=25,color=WHITE,b=False):d.text(xy,t,font=fs(size,b),fill=color)
def header(d,title):
 d.rectangle((0,0,W,66),fill='#0A1220');text(d,(29,18),'●',21,AMBER);text(d,(64,20),'SECOND BRAIN • TEACHING DEMO',22,WHITE,True)
 text(d,(W-330,23),title,18,MUTED)
def footer(d):
 d.rectangle((0,H-38,W,H),fill='#0B1422');text(d,(27,H-28),'ILLUSTRATIVE UI — rebuilt from synthetic demo content; not a product screenshot',16,'#92A3B6')
def basic(title):
 im=Image.new('RGB',(W,H),B);d=ImageDraw.Draw(im);header(d,title);footer(d);return im,d
def tree(d,x=27,y=102):
 text(d,(x,y),'FILE EXPLORER',21,MUTED,True);y+=60
 for s,lev,col,bold in [('▾ demo-brain',0,WHITE,True),('▾ general',1,BLUE,True),('INDEX.md',2,MUTED,False),('MEMORY.md',2,MUTED,False),('▾ agent',2,BLUE,False),('BOOTSTRAP.md',3,MUTED,False),('SESSION_CLOSE.md',3,MUTED,False),('▾ areas',1,BLUE,True),('▾ Research',2,BLUE,False),('▾ transport-employment',3,WHITE,True),('CURRENT_STATE.md',4,MUTED,False),('DECISIONS.md',4,MUTED,False),('NEXT_ACTIONS.md',4,MUTED,False),('▾ wiki',4,BLUE,False),('identification.md',5,MUTED,False),('▾ skills',4,BLUE,False)]:
  text(d,(x+lev*20,y),s,18,col,bold);y+=37

def notes():
 im,d=basic('Vault / Research');d.rectangle((0,66,425,H-38),fill=SIDE);tree(d)
 d.rectangle((425,66,1205,H-38),fill=PANEL)
 text(d,(472,101),'transport-employment_CURRENT_STATE.md',25,WHITE,True)
 d.line((472,151,1162,151),fill=LINE,width=2)
 text(d,(472,183),'# Current State',34,WHITE,True)
 text(d,(473,254),'Last updated: 2026-10-25',22,MUTED)
 entries=[('Research question','Does reliable transit access improve employment?'),('Data','Synthetic municipal panel, 2015–2024'),('Identification','Staggered adoption: assumptions under review'),('Current bottleneck','Pre-trends and rollout timing validation'),('Next action','Verify pre-treatment characteristics')]
 yy=324
 for a,b in entries:
  text(d,(480,yy),a.upper(),19,AMBER,True);text(d,(481,yy+29),b,22,WHITE);yy+=94
 d.rectangle((1205,66,W,H-38),fill=SIDE)
 text(d,(1240,103),'BACKLINKS',21,MUTED,True)
 for k,s in enumerate(['PROJECT_BRIEF.md','DECISIONS.md','identification.md','data-sources.md','weekly-review.md']):
  rr(d,(1230,166+k*89,1564,229+k*89),PANEL,LINE,8)
  text(d,(1254,181+k*89),s,18,BLUE)
 im.save(OUT/'obsidian-notes-illustrative.png')

def graph():
 im,d=basic('Graph view');d.rectangle((0,66,385,H-38),fill=SIDE);tree(d,27,108)
 center=(1026,471);nodes=[('Research',1025,274,38),('transport-employment',1007,460,37),('identification',1320,327,31),('DECISIONS',1378,541,29),('CURRENT_STATE',1134,701,30),('SOURCES',675,617,33),('wiki',760,315,25),('skills',860,725,30),('SESSION_CLOSE',1375,741,23),('BOOTSTRAP',619,386,29)]
 edges=[(1,i) for i in (0,2,3,4,5,6,7,8,9)]+[(0,6),(0,9),(2,5),(3,4),(7,8),(5,9)]
 for a,b in edges:
  x1,y1=nodes[a][1:3];x2,y2=nodes[b][1:3];d.line((x1,y1,x2,y2),fill='#315E7F',width=3)
 for i,(name,x,y,r) in enumerate(nodes):
  c=AMBER if i==1 else BLUE if i in (0,3,4) else PURPLE
  d.ellipse((x-r,y-r,x+r,y+r),fill=c,outline='#DDE8F6',width=2)
  text(d,(x-r*2 if x>760 else x+24,y+r+8),name,18,WHITE,True if i==1 else False)
 text(d,(428,98),'LINKS ARE NAVIGATION, NOT A SEMANTIC DATABASE',19,MUTED,True)
 im.save(OUT/'obsidian-graph-illustrative.png')

def canvas():
 im,d=basic('Canvas');d.rectangle((0,66,345,H-38),fill=SIDE);tree(d,24,110)
 # grid background
 for x in range(345,W,44):d.line((x,66,x,H-38),fill='#1C2D41',width=1)
 for y in range(66,H-38,44):d.line((345,y,W,y),fill='#1C2D41',width=1)
 cards=[(417,146,826,342,'QUESTION','#24435B',['Does better transit','improve employment?']),
        (970,139,1507,362,'DATA','#2A3D50',['Synthetic panel 2015–24','Treatment rollout dates','Outcome: employed share']),
        (480,492,927,752,'IDENTIFICATION','#253D47',['DiD with staggered entry','Check pre-trends','Document assumptions']),
        (1050,521,1492,721,'RESULTS','#463F40',['Preliminary estimates','SIMULATED – DO NOT CITE'])]
 for x0,y0,x1,y1,title,color,lines in cards:
  rr(d,(x0+6,y0+8,x1+8,y1+9),'#09101B',r=12);rr(d,(x0,y0,x1,y1),color,'#57728E',12)
  text(d,(x0+25,y0+22),title,20,AMBER,True)
  for k,s in enumerate(lines):text(d,(x0+25,y0+76+k*40),s,24,WHITE)
 for coords in [((824,251),(966,250)),((692,343),(702,490)),((931,634),(1046,636))]:
  (x1,y1),(x2,y2)=coords;d.line((x1,y1,x2,y2),fill=BLUE,width=6);d.ellipse((x2-7,y2-7,x2+7,y2+7),fill=BLUE)
 im.save(OUT/'obsidian-canvas-illustrative.png')

def git():
 im,d=basic('Git history + diff');d.rectangle((0,66,510,H-38),fill=SIDE)
 text(d,(38,107),'GIT CHANGES',24,WHITE,True)
 text(d,(38,159),'branch: demo-main',21,BLUE)
 for i,s in enumerate(['M   general/MEMORY.md','M   transport/INDEX.md','A   wiki/audit-notes.md','M   NEXT_ACTIONS.md']):
  rr(d,(26,221+i*81,484,284+i*81),PANEL,LINE,9)
  text(d,(54,237+i*81),s,21,AMBER if s.startswith('M') else GREEN)
 d.rectangle((510,66,W,H-38),fill=PANEL)
 text(d,(546,106),'Diff: transport/INDEX.md',26,WHITE,True)
 rr(d,(541,157,1553,749),'#172539',LINE,9)
 for i,s in enumerate(['@@ -7,6 +7,8 @@','## Wiki','- [identification](wiki/identification.md)','+ [identification](wiki/identification.md)','+ [audit notes](wiki/audit-notes.md)','', 'Reviewed by human before commit','git commit -m "docs: index wiki and update state"']):
  y=202+i*64
  col=GREEN if s.startswith('+') else '#F19C98' if s.startswith('-') else MUTED if s.startswith('@') else WHITE
  if s.startswith('+'):d.rectangle((545,y-7,1552,y+45),fill='#1F423C')
  if s.startswith('-'):d.rectangle((545,y-7,1552,y+45),fill='#4A2A34')
  text(d,(570,y),s,22,col)
 im.save(OUT/'obsidian-git-illustrative.png')

def skills():
 im,d=basic('Portable skills');d.rectangle((0,66,515,H-38),fill=SIDE)
 text(d,(35,108),'SKILL CATALOG',24,WHITE,True)
 for i,s in enumerate(['anti-slop-prose','academic-de-ai','overleaf-review-workflow','sample-construction-report','news-corpus-rebuild']):
  rr(d,(32,172+i*101,485,249+i*101),PANEL,LINE,10)
  text(d,(52,186+i*101),s,21,BLUE,True)
 d.rectangle((515,66,W,H-38),fill=PANEL)
 text(d,(561,113),'SKILL.md — sample-construction-report',26,WHITE,True)
 lines=['---','name: sample-construction-report','description: Validate and document a research sample','---','# When to use','A repeatable corpus / panel construction report','# Steps','1. Read validated data and inclusion rules','2. Reproduce sample counts and exclusions','3. Check data provenance before summarising','4. Output report and unresolved issues']
 for j,s in enumerate(lines):text(d,(563,176+j*51),s,21,GREEN if s.startswith('name:') or s.startswith('description:') else AMBER if s.startswith('#') else WHITE)
 im.save(OUT/'brain-skills-illustrative.png')

def audit():
 im,d=basic('Sunday maintenance');d.rectangle((0,66,W,H-38),fill=PANEL)
 text(d,(50,107),'BRAIN MANAGEMENT  /  SUNDAY AUDIT',29,WHITE,True)
 rr(d,(44,168,1553,748),'#101B2B',LINE,12)
 lines=[('2026-10-25  10:55','Manual rerun: scheduled machine was offline',AMBER),
        ('SCAN','939 Markdown files; recent raw and core checked',WHITE),
        ('STATE','Research projects and dashboards reconciled',WHITE),
        ('LINKS','Broken links and obsolete paths repaired',WHITE),
        ('CLEANUP','19 redundant files removed after Git snapshot',WHITE),
        ('GIT','pre-clean snapshot 939fc3c; changes reversible',GREEN),
        ('VALIDATE','validate_vault.py : OK',GREEN)]
 for i,(tag,desc,col) in enumerate(lines):
  y=216+i*74
  text(d,(81,y),tag,22,col,True);text(d,(461,y),desc,22,WHITE)
  d.line((81,y+58,1490,y+58),fill=LINE,width=2)
 im.save(OUT/'sunday-audit-illustrative.png')

if __name__=='__main__':
 notes();graph();canvas();git();skills();audit();print('created illustrative UI assets in',OUT)
