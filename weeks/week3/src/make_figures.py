#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(parents=True, exist_ok=True)
DPI=150
NAVY="#1F4E5F"; TEAL="#2A9D8F"; AMBER="#E9C46A"; CORAL="#E76F51"; GREY="#6C757D"; BLUE="#3A7CA5"
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.family":"DejaVu Sans","font.size":9,"axes.titlesize":11,"axes.titleweight":"bold"})

def save(fig,name):
    p=OUT/name; fig.tight_layout(); fig.savefig(p,dpi=DPI,bbox_inches="tight"); plt.close(fig); print("saved",p)

def box(ax,x,y,w,h,text,face,fontsize=8,textcolor="white"):
    b=FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.04",facecolor=face,edgecolor="white",linewidth=1.2)
    ax.add_patch(b); ax.text(x+w/2,y+h/2,text,ha="center",va="center",color=textcolor,fontsize=fontsize,weight="bold",wrap=True)

def arrow(ax,x1,y1,x2,y2,text=""):
    a=FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="->",mutation_scale=12,color=NAVY,linewidth=1.2); ax.add_patch(a)
    if text: ax.text((x1+x2)/2,(y1+y2)/2+0.15,text,fontsize=7,color=NAVY,ha="center")

# 1 input-process-output
def f1():
    fig,ax=plt.subplots(figsize=(8,3.5)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis("off"); ax.set_title("Figure 1: input-process-output diagram",color=NAVY,pad=10)
    box(ax,0.5,1.2,2.2,1.4,"Input\n(score = 72)",TEAL,9)
    box(ax,3.9,1.2,2.2,1.4,"Process\nif score >= 70",NAVY,9)
    box(ax,7.3,1.2,2.2,1.4,"Output\nprint(\"pass\")",CORAL,9)
    arrow(ax,2.7,1.9,3.9,1.9); arrow(ax,6.1,1.9,7.3,1.9)
    save(fig,"fig1_ipo.png")

# 2 variable assignment state change
def f2():
    fig,ax=plt.subplots(figsize=(8,4)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off"); ax.set_title("Figure 2: variable assignment and state change",color=NAVY,pad=10)
    for i,(name,val) in enumerate([("x","5"),("x","8"),("y","3")]):
        y=4.5-i*1.3
        ax.text(1,y+0.5,name,fontsize=10,weight="bold",color=NAVY)
        box(ax,2,y,2,1,val,TEAL,9)
        if i<2: arrow(ax,3, y-0.05 if False else y+0.5,3,y-0.8)
    ax.text(5,3,"x = 5 then x = x + 3 gives x = 8",fontsize=9,color=GREY)
    save(fig,"fig2_variable_state.png")

# 3 conditional flowchart
def f3():
    fig,ax=plt.subplots(figsize=(7,5.5)); ax.set_xlim(0,8); ax.set_ylim(0,8); ax.axis("off"); ax.set_title("Figure 3: conditional branching flowchart",color=NAVY,pad=10)
    box(ax,2.5,6.5,3,1,"score >= 50?",NAVY,9)
    box(ax,0.5,4,2.2,1,"print pass",TEAL,9)
    box(ax,5.3,4,2.2,1,"print fail",CORAL,9)
    arrow(ax,2.5,7,2.5,6.5); 
    a=FancyArrowPatch((2.5,6.5),(1.6,5.0),arrowstyle="->",mutation_scale=12,color=NAVY,linewidth=1.2); ax.add_patch(a)
    ax.text(1.7,5.8,"True",fontsize=8,color=NAVY)
    a2=FancyArrowPatch((5.5,6.5),(6.4,5.0),arrowstyle="->",mutation_scale=12,color=NAVY,linewidth=1.2); ax.add_patch(a2)
    ax.text(6.0,5.8,"False",fontsize=8,color=NAVY)
    arrow(ax,1.6,4,1.6,2.5); arrow(ax,6.4,4,6.4,2.5)
    box(ax,2.5,1.5,3,1,"end",GREY,9)
    arrow(ax,1.6,2.5,2.5,2.5); arrow(ax,6.4,2.5,5.5,2.5)
    save(fig,"fig3_conditional_flow.png")

# 4 loop flowchart
def f4():
    fig,ax=plt.subplots(figsize=(7,6)); ax.set_xlim(0,8); ax.set_ylim(0,8); ax.axis("off"); ax.set_title("Figure 4: loop execution flowchart",color=NAVY,pad=10)
    box(ax,2.5,6.5,3,1,"i = 0",TEAL,9)
    box(ax,2.5,5,3,1,"i < 5 ?",NAVY,9)
    box(ax,2.5,3.2,3,1,"print(i); i += 1",CORAL,9)
    box(ax,2.5,1.4,3,1,"done",GREY,9)
    arrow(ax,4,6.5,4,6.0); arrow(ax,4,5,4,4.2); arrow(ax,4,3.2,4,2.4)
    a=FancyArrowPatch((5.5,3.7),(5.5,5.5),arrowstyle="->",mutation_scale=12,color=NAVY,linewidth=1.2); ax.add_patch(a)
    ax.text(5.7,4.6,"repeat",fontsize=8,color=NAVY)
    a2=FancyArrowPatch((5.5,5.0),(4.0,5.0),arrowstyle="->",mutation_scale=12,color=NAVY,linewidth=1.2); ax.add_patch(a2)
    ax.text(5.0,4.6,"False",fontsize=8,color=NAVY) if False else None
    save(fig,"fig4_loop_flow.png")

# 5 function call return
def f5():
    fig,ax=plt.subplots(figsize=(8,4.5)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off"); ax.set_title("Figure 5: function call and return value",color=NAVY,pad=10)
    box(ax,0.5,3.5,2.6,1.6,"Caller\ngreet(\"Aisha\")",TEAL,9)
    box(ax,3.7,3.5,2.6,1.6,"Function\ndef greet(name)",NAVY,9)
    box(ax,6.9,3.5,2.6,1.6,"Return\n\"hello Aisha\"",CORAL,9)
    arrow(ax,3.1,4.3,3.7,4.3,text="argument")
    arrow(ax,6.3,4.3,6.9,4.3,text="result")
    save(fig,"fig5_function_call.png")

# 6 learning progression
def f6():
    fig,ax=plt.subplots(figsize=(9,3.5)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis("off"); ax.set_title("Figure 6: learning progression diagram",color=NAVY,pad=10)
    steps=["Variables","Operators","Conditionals","Loops","Functions","Debugging","Mini-project"]
    for i,s in enumerate(steps):
        x=0.3+i*1.35
        box(ax,x,1.3,1.25,1.2,s,TEAL if i<5 else CORAL,8)
        if i<len(steps)-1: arrow(ax,x+1.25,1.9,x+1.35,1.9)
    save(fig,"fig6_learning_progression.png")

# 7 application architecture
def f7():
    fig,ax=plt.subplots(figsize=(9,5)); ax.set_xlim(0,10); ax.set_ylim(0,7); ax.axis("off"); ax.set_title("Figure 7: application architecture diagram",color=NAVY,pad=10)
    box(ax,3.5,5.5,3,1,"index.html",TEAL,9)
    box(ax,1,3.5,2.2,1,"styles.css",NAVY,9)
    box(ax,3.9,3.5,2.2,1,"app.js",NAVY,9)
    box(ax,6.8,3.5,2.2,1,"Pyodide CDN",CORAL,9)
    box(ax,3.9,1.5,2.2,1,"localStorage",GREY,9)
    arrow(ax,5,5.5,5,4.5); arrow(ax,2.1,3.5,3.9,3.5); arrow(ax,6.1,3.5,6.8,3.5); arrow(ax,5,3.5,5,2.5)
    save(fig,"fig7_architecture.png")

# 8 learner feedback cycle
def f8():
    fig,ax=plt.subplots(figsize=(7,6)); ax.set_xlim(0,8); ax.set_ylim(0,8); ax.axis("off"); ax.set_title("Figure 8: learner feedback cycle",color=NAVY,pad=10)
    items=["Attempt","Feedback","Reflect","Retry"]
    positions=[(4,7),(6.5,4),(4,1.5),(1.5,4)]
    for (x,y),lab in zip(positions,items):
        box(ax,x-0.9,y-0.5,1.8,1,lab,TEAL,9)
    for i in range(4):
        x1,y1=positions[i]; x2,y2=positions[(i+1)%4]
        arrow(ax,x1,y1,x2,y2)
    save(fig,"fig8_feedback_cycle.png")

for f in [f1,f2,f3,f4,f5,f6,f7,f8]: f()
print("done")
