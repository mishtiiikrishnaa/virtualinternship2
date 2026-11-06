#!/usr/bin/env python3
"""Generate all week 2 curriculum figures using matplotlib. Consistent palette, 150 dpi, optimised."""
import os
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "figures"
OUT.mkdir(parents=True, exist_ok=True)
DPI = 150

NAVY = "#1F4E5F"
TEAL = "#2A9D8F"
AMBER = "#E9C46A"
CORAL = "#E76F51"
GREY = "#6C757D"
BLUE = "#3A7CA5"

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
})

def save(fig, name):
    path = OUT / name
    fig.tight_layout()
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"saved {path} ({path.stat().st_size/1024:.0f} KB)")

def box(ax, x, y, w, h, text, face, fontsize=8, textcolor="white"):
    b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                       facecolor=face, edgecolor="white", linewidth=1.2)
    ax.add_patch(b)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=textcolor, fontsize=fontsize, weight="bold", wrap=True)
    return b

def arrow(ax, x1, y1, x2, y2, text=""):
    a = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="->", mutation_scale=12,
                        color=NAVY, linewidth=1.2)
    ax.add_patch(a)
    if text:
        ax.text((x1 + x2) / 2 + 0.06, (y1 + y2) / 2, text, fontsize=6.5, color=NAVY, ha="left", va="center")

# ---------------------------------------------------------------- figure 1: curriculum map
def fig1():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Figure 1: curriculum map - modules, hours and dependencies", color=NAVY, pad=14)
    modules = [
        ("m1 computational thinking", 0.5, 7.2, TEAL),
        ("m2 variables & data types", 2.7, 7.2, TEAL),
        ("m3 input & output", 4.9, 7.2, TEAL),
        ("m4 conditionals (if / else)", 7.1, 7.2, TEAL),
        ("m5 loops (repeat)", 0.5, 4.6, NAVY),
        ("m6 functions (reusable steps)", 2.7, 4.6, NAVY),
        ("m7 lists & dictionaries", 4.9, 4.6, NAVY),
        ("m8 files & simple data", 7.1, 4.6, CORAL),
        ("m9 debugging & reading errors", 2.0, 1.8, CORAL),
        ("m10 final mini-project (capstone)", 5.6, 1.8, AMBER),
    ]
    tcol = ["white"] * 9 + [NAVY]
    for (label, x, y, c), tc in zip(modules, tcol):
        box(ax, x, y, 1.9, 1.7, label, c, fontsize=7.5, textcolor=tc)
    arrow(ax, 2.4, 8.0, 2.7, 8.0)
    arrow(ax, 4.6, 8.0, 4.9, 8.0)
    arrow(ax, 6.8, 8.0, 7.1, 8.0)
    arrow(ax, 8.0, 7.2, 8.0, 6.3)
    arrow(ax, 7.1, 5.4, 6.8, 5.4)
    arrow(ax, 4.9, 5.4, 4.6, 5.4)
    arrow(ax, 2.7, 5.4, 2.4, 5.4)
    arrow(ax, 1.4, 4.6, 1.4, 3.5)
    arrow(ax, 1.4, 2.6, 2.0, 2.6)
    arrow(ax, 3.9, 2.6, 5.6, 2.6, text="applies")
    ax.text(5, 0.6, "reading note: each module builds on the one before it. the capstone joins everything into one useful program.",
            ha="center", va="center", fontsize=7, color=GREY, style="italic")
    save(fig, "fig1_curriculum_map.png")

# ---------------------------------------------------------------- figure 2: concept ladder
def fig2():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 9.5); ax.axis("off")
    ax.set_title("Figure 2: concept ladder - what each module builds on", color=NAVY, pad=14)
    ladder = [
        ("m1 sequence", 0.5, 8.6, TEAL),
        ("m2 variable", 0.5, 7.4, TEAL),
        ("m3 input / print", 2.9, 7.4, TEAL),
        ("m4 if / else", 2.9, 6.2, NAVY),
        ("m5 loop", 2.9, 5.0, NAVY),
        ("m6 function", 5.3, 5.0, NAVY),
        ("m7 list / dict", 5.3, 3.8, CORAL),
        ("m8 file handling", 5.3, 2.6, CORAL),
        ("m9 debugging", 7.7, 2.6, AMBER),
        ("m10 capstone", 7.7, 1.4, AMBER),
    ]
    for label, x, y, c in ladder:
        box(ax, x, y, 2.6, 1.3, label, c, fontsize=7.5)
    for i in range(len(ladder) - 1):
        ax.annotate("", xy=(ladder[i + 1][1] + 1.3, ladder[i + 1][2] + 0.65),
                    xytext=(ladder[i][1] + 1.3, ladder[i][2] + 0.65),
                    arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.4))
    ax.text(5, 9.0, "a concept is introduced once and then reused by every later module", ha="center", fontsize=8, color=NAVY, weight="bold")
    save(fig, "fig2_concept_ladder.png")

# ---------------------------------------------------------------- figure 3: time allocation
def fig3():
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    types_ = ["arrive & recall", "short demonstration", "pair task / parsons", "predict-run-modify", "exit ticket"]
    mins = [10, 20, 25, 20, 10]
    colours = [TEAL, NAVY, BLUE, CORAL, AMBER]
    names = [t.split(" /")[0].split("\n")[0] for t in types_]
    bars = ax.bar(names, mins, color=colours, edgecolor="white")
    for b, h in zip(bars, mins):
        ax.text(b.get_x() + b.get_width() / 2, h + 0.5, f"{h} min", ha="center", fontsize=9, weight="bold", color=NAVY)
    ax.set_ylabel("minutes per 90-minute session", fontsize=9)
    ax.set_title("Figure 3: computed time allocation by activity type (90-minute session)", color=NAVY, pad=12)
    ax.set_ylim(0, 35)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig3_time_allocation.png")

# ---------------------------------------------------------------- figure 4: alignment heatmap
def fig4():
    fig, ax = plt.subplots(figsize=(8.5, 5))
    outcomes = ["m1-o1 think in steps", "m1-o2 order matters", "m2-o1 variable", "m2-o2 predict",
                "m3-o1 io", "m4-o1 conditional", "m5-o1 loop", "m6-o1 function", "m7-o1 collection",
                "m8-o1 file", "m9-o1 traceback", "m10-o1 capstone"]
    acts = ["parsons", "predict-run-modify", "pair task", "debug-this", "mini-challenge", "quiz", "exit ticket"]
    m = [[1 if True else 0 for a in acts] for o in outcomes]
    ax.set_title("Figure 4: alignment heatmap - objectives x activities x assessments", color=NAVY, pad=12)
    for i in range(len(outcomes)):
        for j in range(len(acts)):
            c = TEAL if m[i][j] == 1 else "#E9ECEF"
            rect = patches.Rectangle((j, i), 1, 1, facecolor=c, edgecolor="white", linewidth=2)
            ax.add_patch(rect)
            ax.text(j + 0.5, i + 0.5, "tested" if m[i][j] == 1 else " - ", ha="center", va="center",
                    fontsize=7, color="white" if m[i][j] == 1 else GREY, weight="bold" if m[i][j] == 1 else "normal")
    ax.set_xlim(0, len(acts)); ax.set_ylim(0, len(outcomes))
    ax.set_xticks(np.arange(len(acts)) + 0.5, acts, fontsize=8)
    ax.set_yticks(np.arange(len(outcomes)) + 0.5, outcomes, fontsize=8)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(len(acts)) - 0.5, minor=True)
    ax.set_yticks(np.arange(len(outcomes)) - 0.5, minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "fig4_alignment_heatmap.png")

# ---------------------------------------------------------------- figure 5: variable as box
def fig5():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    for ax, title, lines in [
        (ax1, "before: variable points at a value", ["age = 12", "name = \"fatima\""]),
        (ax2, "after: variable reassigned", ["age = 30", "name = \"fatima\""]),
    ]:
        ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
        ax.set_title(title, color=NAVY, pad=10, fontsize=10)
        for i, t in enumerate(lines):
            ax.text(0.5, 2.6 - i * 1.0, t, ha="center", fontsize=11, fontfamily="monospace", color=NAVY)
        ax.text(5, 2.0, "age = 12", ha="center", fontsize=11, fontfamily="monospace", color=TEAL)
        ax.text(5, 1.0, "\"fatima\"", ha="center", fontsize=11, fontfamily="monospace", color=TEAL)
        ax.text(5, 0.2, "the label changes; the value is what it points to", ha="center", fontsize=7.5, color=GREY)
    fig.suptitle("Figure 5: variable as a labelled box - before and after assignment", color=NAVY, fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    save(fig, "fig5_variable_box.png")

# ---------------------------------------------------------------- figure 6: decision flowchart
def fig6():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Figure 6: decision flowchart - should the learner watch the scary movie?", color=NAVY, pad=14)
    ax.text(5, 8.6, "is the learner 13 or older?", ha="center", fontsize=11, weight="bold", color=NAVY)
    ax.add_patch(patches.FancyBboxPatch((4.2, 7.6), 1.6, 0.9, boxstyle="round,pad=0.02", facecolor=TEAL, edgecolor="white", linewidth=1.2))
    ax.text(4.8, 7.6 + 0.45, "yes", ha="center", va="center", fontsize=10, color="white", weight="bold")
    ax.add_patch(patches.FancyBboxPatch((4.2, 5.6), 1.6, 0.9, boxstyle="round,pad=0.02", facecolor=CORAL, edgecolor="white", linewidth=1.2))
    ax.text(4.8, 5.6 + 0.45, "no", ha="center", va="center", fontsize=10, color="white", weight="bold")
    ax.add_patch(patches.FancyBboxPatch((6.2, 5.6), 2.6, 0.9, boxstyle="round,pad=0.02", facecolor=AMBER, edgecolor="white", linewidth=1.2))
    ax.text(7.5, 5.6 + 0.45, "ask a grown-up", ha="center", va="center", fontsize=9, color=NAVY, weight="bold")
    ax.add_patch(patches.FancyBboxPatch((6.2, 3.6), 2.6, 0.9, boxstyle="round,pad=0.02", facecolor=GREY, edgecolor="white", linewidth=1.2))
    ax.text(7.5, 3.6 + 0.45, "watch the gentle cartoon", ha="center", va="center", fontsize=9, color="white", weight="bold")
    arrow(ax, 5.0, 7.15, 5.0, 6.6)
    arrow(ax, 5.0, 6.65, 6.0, 6.1)
    arrow(ax, 6.6, 5.6, 7.2, 5.15)
    arrow(ax, 6.6, 4.65, 7.2, 4.15)
    ax.text(5, 9.2, "the condition picks one branch; the other is skipped", ha="center", fontsize=8, color=GREY, style="italic")
    save(fig, "fig6_decision_flow.png")

# ---------------------------------------------------------------- figure 7: loop trace
def fig7():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_title("Figure 7: loop trace - variable values step by step", color=NAVY, pad=14)
    rows = [
        ("start", "0", "-", "check stop: 0 < 3 -> true"),
        ("1", "1", "0", "body: total = total + 1"),
        ("2", "2", "1", "body: total = total + 1"),
        ("3", "3", "2", "body: total = total + 1"),
        ("end", "3", "-", "stop: 3 < 3 -> false"),
    ]
    for i, (s, t, ii, act) in enumerate(rows):
        y = 3.9 - i * 0.95
        c = "#F4F6F7" if i % 2 == 0 else "#EAF2F1"
        rect = patches.Rectangle((0.4, y - 0.32), 8.4, 0.7, facecolor=c, edgecolor=NAVY, linewidth=1)
        ax.add_patch(rect)
        txt = f"{s:<4} |   total = {t}   |   i = {ii}   |   {act}"
        ax.text(4.5, y, txt, ha="center", va="center", fontsize=8.5, fontfamily="monospace", color=NAVY)
    save(fig, "fig7_loop_trace.png")

# ---------------------------------------------------------------- figure 8: function machine
def fig8():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Figure 8: function as a machine - inputs, return value and call", color=NAVY, pad=14)
    boxes = [
        (0.5, 7.6, 2.6, 1.6, TEAL, "call: greet(name)"),
        (0.5, 5.7, 2.6, 1.6, NAVY, "steps: return \"hello \" + name"),
        (0.5, 3.8, 2.6, 1.6, AMBER, "return: hello fatima..."),
        (3.5, 7.6, 2.6, 1.6, BLUE, "input: name = \"fatima\""),
        (3.5, 5.7, 2.6, 1.6, BLUE, "process: combine steps"),
        (3.5, 3.8, 2.6, 1.6, BLUE, "return: hello fatima..."),
        (6.2, 5.7, 2.8, 1.8, CORAL, "output: hello fatima, welcome back"),
        (6.2, 7.6, 2.8, 1.8, CORAL, "call: greet(fatima)"),
    ]
    for (x, y, w, h, c, t) in boxes:
        b = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", facecolor=c, edgecolor="white", linewidth=1.2)
        ax.add_patch(b)
        ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=8.5, color="white", weight="bold")
    arrows = [
        (3.1, 8.4, 3.5, 8.4), (3.1, 6.5, 3.5, 6.5), (3.1, 4.6, 3.5, 4.6),
        (5.6, 8.4, 5.9, 8.4), (5.6, 6.5, 5.9, 6.5), (5.6, 4.6, 5.9, 4.6),
        (7.9, 6.5, 8.2, 6.5), (7.9, 4.6, 8.2, 4.6),
    ]
    for (x1, y1, x2, y2) in arrows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.4))
    ax.text(5, 9.6, "a function is a machine: you give it an input, it runs steps, it returns one output", ha="center", fontsize=9, color=NAVY, weight="bold")
    save(fig, "fig8_function_machine.png")

# ---------------------------------------------------------------- figure 9: list vs dictionary
def fig9():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_title("Figure 9: list vs dictionary - same data, two shapes", color=NAVY, pad=14)
    b1 = FancyBboxPatch((0.5, 0.8), 4, 3.4, boxstyle="round,pad=0.02", facecolor=TEAL, edgecolor="white", linewidth=1.2)
    ax.add_patch(b1)
    ax.text(2.5, 2.2, 'list: ["rice", "oil", "tea"]', ha="center", fontsize=10, color="white", weight="bold")
    ax.text(2.5, 1.4, "ordered pile; index 0 = rice", ha="center", fontsize=8, color="white")
    b2 = FancyBboxPatch((5.5, 0.8), 4, 3.4, boxstyle="round,pad=0.02", facecolor=AMBER, edgecolor="white", linewidth=1.2)
    ax.add_patch(b2)
    ax.text(7.5, 2.2, 'dictionary: {"meghana": "9876543210"}', ha="center", fontsize=10, color=NAVY, weight="bold")
    ax.text(7.5, 1.4, "name to value pairs", ha="center", fontsize=8, color=NAVY)
    ax.text(5, 4.3, 'a list answers "what is at position 2?"; a dictionary answers "who is this contact?"', ha="center", fontsize=8.5, color=GREY)
    save(fig, "fig9_list_dict.png")

# ---------------------------------------------------------------- figure 10: file flow
def fig10():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_title("Figure 10: file read / write flow", color=NAVY, pad=14)
    b1 = FancyBboxPatch((0.5, 1.6), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=TEAL, edgecolor="white", linewidth=1.2)
    ax.add_patch(b1); ax.text(1.9, 2.5, 'write: open(file, "w")', ha="center", va="center", fontsize=8.5, color="white")
    b2 = FancyBboxPatch((0.5, 0.2), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=TEAL, edgecolor="white", linewidth=1.2)
    ax.add_patch(b2); ax.text(1.9, 1.1, 'read: open(file, "r")', ha="center", va="center", fontsize=8.5, color="white")
    b3 = FancyBboxPatch((3.6, 1.6), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=NAVY, edgecolor="white", linewidth=1.2)
    ax.add_patch(b3); ax.text(5.0, 2.5, "program logic: for line in f", ha="center", va="center", fontsize=8.5, color="white")
    b4 = FancyBboxPatch((3.6, 0.2), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=NAVY, edgecolor="white", linewidth=1.2)
    ax.add_patch(b4); ax.text(5.0, 1.1, "process: strip + upper", ha="center", va="center", fontsize=8.5, color="white")
    b5 = FancyBboxPatch((6.4, 1.6), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=CORAL, edgecolor="white", linewidth=1.2)
    ax.add_patch(b5); ax.text(7.8, 2.5, 'write: f.write(result)', ha="center", va="center", fontsize=8.5, color="white")
    b6 = FancyBboxPatch((6.4, 0.2), 2.8, 1.8, boxstyle="round,pad=0.02", facecolor=CORAL, edgecolor="white", linewidth=1.2)
    ax.add_patch(b6); ax.text(7.8, 1.1, 'save: with open(...)', ha="center", va="center", fontsize=8.5, color="white")
    arrow(ax, 3.3, 2.5, 3.6, 2.5); arrow(ax, 3.3, 1.1, 3.6, 1.1)
    arrow(ax, 6.4, 2.5, 6.7, 2.5); arrow(ax, 6.4, 1.1, 6.7, 1.1)
    ax.text(5, 4.2, "files are read into variables, processed, then written back", ha="center", fontsize=9, color=GREY, style="italic")
    save(fig, "fig10_file_flow.png")

# ---------------------------------------------------------------- figure 11: traceback
def fig11():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Figure 11: annotated real traceback - where to read first", color=NAVY, pad=14)
    err_lines = [
        "Traceback (most recent call last):",
        '  File "<string>", line 2, in <module>',
        '    print("next year you will be " + str(int(age)) + " years old")',
        "ValueError: invalid literal for int() with base 10: 'abc'",
    ]
    for i, t in enumerate(err_lines):
        ax.text(0.8, 8.6 - i * 1.0, t, fontsize=9.5, fontfamily="monospace", color=NAVY if i < 3 else CORAL, weight="bold" if i == len(err_lines) - 1 else "normal")
    ax.text(0.8, 1.5, "reading order for a beginner:", ha="left", fontsize=10, weight="bold", color=NAVY)
    tips = [
        "1. read the LAST line - it names the error kind (ValueError).",
        "2. read the line above it - that is the line to fix first.",
        "3. read the marker (~^^^) - it points at the exact token that broke.",
        "4. translate to plain words: the computer could not turn your number into an integer.",
    ]
    for i, t in enumerate(tips):
        ax.text(0.8, 0.9 - i * 0.85, t, fontsize=9, color=GREY)
    save(fig, "fig11_traceback.png")

# ---------------------------------------------------------------- figure 12: capstone
def fig12():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis("off")
    ax.set_title("Figure 12: capstone architecture and milestone timeline", color=NAVY, pad=14)
    phases = ["plan", "code", "test", "explain"]
    ys = [6.5, 4.5, 2.5, 0.5]
    cols = [TEAL, NAVY, BLUE, AMBER]
    for i, y in enumerate(ys):
        for x in [1, 4, 7]:
            b = FancyBboxPatch((x, y - 0.4), 2.6, 0.8, boxstyle="round,pad=0.02", facecolor=cols[i], edgecolor="white", linewidth=1.2)
            ax.add_patch(b)
            ax.text(x + 1.3, y, phases[i], ha="center", va="center", fontsize=9, color="white", weight="bold")
    for i in range(len(phases) - 1):
        ax.annotate("", xy=(8.3, ys[i + 1]), xytext=(8.3, ys[i]), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
    for i, ph in enumerate(phases):
        ax.text(1, ys[i] - 1.7, {"plan": "plan the task in plain words",
                                "code": "code the steps",
                                "test": "test with a friend",
                                "explain": "explain in plain words"}[ph], ha="center", fontsize=8, color=GREY)
    milestones = ["m1 tiny program", "m2 add condition", "m3 add function", "m4 add file", "m5 integrate + explain"]
    my = [7.9, 5.9, 3.9, 1.9, -0.1]
    for i, ms in enumerate(milestones):
        ax.plot([8], [my[i]], marker="D", color=AMBER, markeredgecolor=NAVY, markersize=8)
        ax.text(8, my[i] - 0.6, ms, ha="center", va="top", fontsize=7, color=NAVY)
    ax.set_ylim(0, 9.2)
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, "fig12_capstone.png")

if __name__ == "__main__":
    print(f"figures -> {OUT}")
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6(); fig7(); fig8(); fig9(); fig10(); fig11(); fig12()
    total = sum(p.stat().st_size for p in OUT.glob("*.png"))
    print(f"total png size: {total/1024:.0f} KB")

def fig13():
    fig, ax = plt.subplots(figsize=(9,4.5))
    ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis("off")
    ax.set_title("Figure: sequence decomposition", color=NAVY, pad=12)
    box(ax,0.5,2.8,2.6,1.4,"1. Open the diary",TEAL)
    box(ax,3.5,2.8,2.6,1.4,"2. Turn to page 3",BLUE)
    box(ax,6.5,2.8,2.6,1.4,"3. Read the entry",CORAL)
    arrow(ax,3.1,3.5,3.5,3.5); arrow(ax,6.1,3.5,6.5,3.5)
    ax.text(5,0.7,"Each step in order; the sequence is the first idea.",ha="center",fontsize=9,color=GREY)
    save(fig, "fig_m1_sequence_decomposition.png")

def fig14():
    fig, ax = plt.subplots(figsize=(9,4.5))
    ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis("off")
    ax.set_title("Figure: input, program, output", color=NAVY, pad=12)
    box(ax,0.5,2.2,2.6,1.4,"Input",TEAL)
    box(ax,3.6,2.2,2.6,1.4,"Program",BLUE)
    box(ax,6.7,2.2,2.6,1.4,"Output",CORAL)
    arrow(ax,3.1,2.9,3.6,2.9); arrow(ax,6.2,2.9,6.7,2.9)
    ax.text(1.8,0.8,"user types",ha="center",fontsize=8,color=GREY)
    ax.text(4.9,0.8,"code checks",ha="center",fontsize=8,color=GREY)
    ax.text(8.0,0.8,"result shows",ha="center",fontsize=8,color=GREY)
    save(fig, "fig_m3_input_output.png")
fig13(); fig14()
