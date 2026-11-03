#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import math
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'assets/diagrams';OUT.mkdir(parents=True,exist_ok=True)
NAVY='#163A59';A='#D97706';BG='#F8FAFC';LINE='#CBD5E1';DARK='#16283A';MUTED='#516174';WHITE='#FFFFFF';GREEN='#2C866B';PURPLE='#6D5AC1'
F='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';FB='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n,b=False):return ImageFont.truetype(FB if b else F,n)
def base(t,w=1200,h=1200):
 im=Image.new('RGB',(w,h),BG);d=ImageDraw.Draw(im)
 d.text((47,35),t,font=font(42,True),fill=NAVY);d.line((48,104,w-50,104),fill=A,width=6)
 return im,d
def card(d,box,t,desc='',c=NAVY):
 x0,y0,x1,y1=box;d.rounded_rectangle(box,radius=17,fill=WHITE,outline=c,width=4)
 d.rounded_rectangle((x0+12,y0+13,x0+26,y1-13),radius=7,fill=c)
 d.text((x0+43,y0+20),t,font=font(31,True),fill=c)
 for i,l in enumerate(desc.split('|')):d.text((x0+43,y0+72+i*44),l,font=font(24),fill=DARK)
def arrow(d,p1,p2,c=A,th=7):
 d.line((*p1,*p2),fill=c,width=th);ang=math.atan2(p2[1]-p1[1],p2[0]-p1[0]);r=19
 q=[p2,(p2[0]-r*math.cos(ang-.53),p2[1]-r*math.sin(ang-.53)),(p2[0]-r*math.cos(ang+.53),p2[1]-r*math.sin(ang+.53))];d.polygon(q,fill=c)
def small(d,p,t):d.text(p,t,font=font(21),fill=MUTED)
# 3 agent evolution
im,d=base('From chat to a persistent assistant')
for i,(t,sub) in enumerate([('Chatbot','Active conversation'),('Agent','Tools + permissions'),('Second Brain','Persistent state + skills')]):
 y=165+i*328;card(d,(95,y,1105,y+232),t,sub,NAVY if i!=2 else GREEN)
 if i<2:arrow(d,(600,y+236),(600,y+314))
im.save(OUT/'chat-to-brain.png')
# portability
im,d=base('One vault, several agents')
card(d,(265,180,930,382),'MARKDOWN VAULT','general/   areas/   skills/',NAVY)
for j,(name,x) in enumerate([('Codex',65),('Claude',425),('OpenCode',785)]):
 card(d,(x,705,x+326,918),name,'workspace access',GREEN if j==1 else NAVY)
 arrow(d,(596,387),(x+164,690))
small(d,(135,1005),'Adapters differ; canonical files and decisions remain portable')
im.save(OUT/'portable-vault.png')
# tokens
im,d=base('Input context: illustrative')
d.text((90,215),'Full prompt',font=font(30,True),fill=NAVY)
d.rounded_rectangle((90,295,1110,444),radius=16,fill='#8D9BAA')
d.text((126,340),'100,000 input tokens',font=font(36,True),fill=WHITE)
d.text((90,560),'Selective context',font=font(30,True),fill=NAVY)
d.rounded_rectangle((90,642,1110,791),radius=16,fill='#E6EDF3')
d.rounded_rectangle((90,642,172,791),radius=16,fill=A)
d.text((224,682),'8,000 tokens',font=font(36,True),fill=DARK)
d.text((90,880),'92% fewer input tokens for this request',font=font(31,True),fill=GREEN)
small(d,(90,972),'Illustrative only: total-system cost includes ingest and maintenance')
im.save(OUT/'tokens-example.png')
# rag
im,d=base('RAG: retrieve evidence at query time')
for y,t,s in [(168,'Sources','PDFs, notes, code'),(390,'Index','Chunks / BM25 / vectors'),(612,'Retrieval','Find relevant passages'),(834,'LLM answer','Cited response')]:
 card(d,(160,y,1040,y+152),t,s,GREEN if 'Retrieval' in t else NAVY)
 if y<834:arrow(d,(600,y+160),(600,y+210))
im.save(OUT/'rag-pipeline.png')
# wiki
im,d=base('LLM Wiki: cumulative knowledge')
card(d,(65,170,1120,360),'RAW','Original sources retained',NAVY)
card(d,(65,500,1120,690),'WIKI','Interlinked distilled pages',PURPLE)
card(d,(65,835,1120,1030),'SCHEMA','Agent update and lint rules',GREEN)
arrow(d,(610,370),(610,485));arrow(d,(610,820),(610,710),A)
small(d,(665,742),'governs update')
im.save(OUT/'llm-wiki.png')
# hybrid
im,d=base('Hybrid knowledge architecture')
card(d,(100,155,1110,340),'SOURCE DOCUMENTS','Original evidence and provenance',NAVY)
card(d,(60,492,570,710),'RETRIEVAL','Search detailed evidence',PURPLE)
card(d,(640,492,1140,710),'CURATED WIKI','Stable decisions / concepts',GREEN)
card(d,(205,862,1004,1050),'AGENT + REVIEW','Use, validate, update',NAVY)
arrow(d,(500,345),(330,474));arrow(d,(700,345),(870,474));arrow(d,(330,720),(515,848));arrow(d,(870,720),(710,848))
im.save(OUT/'hybrid-brain.png')
# bootstrap
im,d=base('Agent session lifecycle')
for i,(t,desc) in enumerate([('BOOTSTRAP','Global index, project route'),('LOAD','State, decisions, next actions'),('WORK','Files, sources, tools and tests'),('CLOSEOUT','Distill, audit and commit')]):
 y=165+i*254;card(d,(92,y,1100,y+190),t,desc,GREEN if i==3 else NAVY)
 if i<3:arrow(d,(610,y+196),(610,y+246))
im.save(OUT/'bootstrap-loop.png')
# stack
im,d=base('The tool stack is modular')
for i,(t,s) in enumerate([('KNOWLEDGE','Obsidian · Markdown · Dropbox'),('RECALL','Memanto local · targeted retrieval'),('CODE','Git · CodeGraph · review graph'),('PROCEDURES','Caveman · skills · Econoclast')]):
 y=170+i*246;card(d,(95,y,1100,y+185),t,s,[NAVY,GREEN,PURPLE,A][i])
im.save(OUT/'tool-stack.png')
print('Created',len(list(OUT.glob('*.png'))),'diagrams')
