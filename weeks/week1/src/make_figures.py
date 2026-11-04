#!/usr/bin/env python3
"""Generate all figures for the week 1 plan using matplotlib. Consistent palette, 150 dpi, optimised."""
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

# palette: warm navy/teal/amber, high contrast, colour-blind-safe
NAVY = "#1F4E5F"
TEAL = "#2A9D8F"
AMBER = "#E9C46A"
CORAL = "#E76F51"
GREY = "#6C757D"
LIGHT = "#F4F6F7"

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

# ---------------------------------------------------------------- figure 1
def fig1():
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Figure 1: Curriculum structure — 10 modules building to a capstone", color=NAVY, pad=14)
    modules = [
        ("M1\nComputational\nthinking", 0.5, 7.2),
        ("M2\nVariables &\ndata types", 2.7, 7.2),
        ("M3\nInput &\noutput", 4.9, 7.2),
        ("M4\nConditionals\n(if / else)", 7.1, 7.2),
        ("M5\nLoops\n(repeat)", 0.5, 4.6),
        ("M6\nFunctions\n(reusable steps)", 2.7, 4.6),
        ("M7\nLists &\ndictionaries", 4.9, 4.6),
        ("M8\nFiles &\nsimple data", 7.1, 4.6),
        ("M9\nDebugging &\nreading errors", 2.0, 1.8),
        ("M10\nFinal mini-project\n(capstone)", 5.6, 1.8),
    ]
    colours = [TEAL, TEAL, TEAL, TEAL, NAVY, NAVY, NAVY, CORAL, CORAL, AMBER]
    tcol = ["white", "white", "white", "white", "white", "white", "white", "white", "white", NAVY]
    for (label, x, y), c, tc in zip(modules, colours, tcol):
        box(ax, x, y, 1.9, 1.7, label, c, fontsize=7.5, textcolor=tc)
    # snakes
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
    # dependency note
    ax.text(5, 0.6, "Reading note: each module builds on the one before it. Spread through M9 (debugging)\nand practise it inside every later module. M10 is the capstone — one useful small program.",
            ha="center", va="center", fontsize=7, color=GREY, style="italic")
    save(fig, "fig1_curriculum_structure.png")

# ---------------------------------------------------------------- figure 2
def fig2():
    fig, ax = plt.subplots(figsize=(9, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    ax.set_title("Figure 2: Learner journey — from “never coded” to “I built something”", color=NAVY, pad=10)
    steps = [
        ("Never\ncoded", 0.4, TEAL),
        ("Ran a\nfirst program", 2.0, TEAL),
        ("Predicted &\nran code", 3.6, NAVY),
        ("Wrote small\nprograms", 5.2, NAVY),
        ("Debugged\nwith help", 6.8, CORAL),
        ("Built\nthe capstone", 8.4, AMBER),
    ]
    for label, x, c in steps:
        tc = NAVY if c == AMBER else "white"
        box(ax, x, 1.4, 1.4, 1.3, label, c, fontsize=7.5, textcolor=tc)
    for i in range(len(steps) - 1):
        arrow(ax, steps[i][1] + 1.4, 2.05, steps[i + 1][1], 2.05)
    ax.text(5, 0.6, "Small wins early, harder challenges later. Confidence is part of the curriculum, not an accident.",
            ha="center", fontsize=7, color=GREY, style="italic")
    save(fig, "fig2_learner_journey.png")

# ---------------------------------------------------------------- figure 3
def fig3():
    # planned timeline from 2026-11-05, 12 milestones, weekday only
    fig, ax = plt.subplots(figsize=(9, 5))
    phases = ["Discovery", "Design", "Content creation", "Review & pilot", "Revision", "Launch"]
    starts = [0, 3, 6, 15, 20, 25]   # working-day index from baseline
    ends   = [3, 6, 15, 20, 25, 30]
    colours = [TEAL, NAVY, "#3A7CA5", "#9A7B4F", "#B08968", CORAL]
    for i, (p, s, e) in enumerate(zip(phases, starts, ends)):
        ax.barh(i, e - s, left=s, height=0.55, color=colours[i], edgecolor="white")
        ax.text((s + e) / 2, i, p, ha="center", va="center", fontsize=7.5, color="white", weight="bold")
    milestones = [(0, "Baseline\n5 Nov"), (3, "MS-01"), (6, "MS-02"), (15, "MS-03"), (20, "MS-04"), (25, "MS-05"), (30, "MS-06 launch")]
    for x, label in milestones:
        ax.plot([x], [-1], marker="D", color=AMBER, markeredgecolor=NAVY, markersize=8)
        ax.text(x, -1.55, label, ha="center", va="top", fontsize=6.5, color=NAVY)
    ax.set_ylim(-2, 6.3)
    ax.set_yticks(range(len(phases))); ax.set_yticklabels([f"P{i+1} {p}" for i, p in enumerate(phases)], fontsize=7.5)
    ax.set_xlabel("Planned working days from baseline (5 Nov 2026, all dates planned)", fontsize=8)
    ax.set_title("Figure 3: Planned curriculum-development timeline (Gantt) with milestones", color=NAVY, pad=12)
    ax.invert_yaxis()
    ax.grid(axis="x", alpha=0.25)
    ax.text(15, 6.15, "Bar stops mark phase ends. Diamonds mark milestone dates. Dates are planned, skipping weekends and govind jayanti (25 Nov).",
            ha="center", fontsize=6.5, color=GREY, style="italic")
    save(fig, "fig3_gantt_timeline.png")

# ---------------------------------------------------------------- figure 4
def fig4():
    fig, ax = plt.subplots(figsize=(9, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.5); ax.axis("off")
    ax.set_title("Figure 4: What one typical 90-minute session looks like", color=NAVY, pad=10)
    blocks = [
        ("Arrive &\nrecall\n(10 min)", 0.3, TEAL),
        ("Worked example\n(live code)\n(20 min)", 2.1, NAVY),
        ("Pair task /\nParsons problem\n(25 min)", 4.1, "#3A7CA5"),
        ("Predict–run–\nmodify\n(20 min)", 6.1, CORAL),
        ("Exit ticket\n(10 min)", 8.2, AMBER),
    ]
    for label, x, c in blocks:
        tc = NAVY if c == AMBER else "white"
        box(ax, x, 1.5, 1.7, 1.8, label, c, fontsize=7.5, textcolor=tc)
    for i in range(len(blocks) - 1):
        arrow(ax, blocks[i][1] + 1.7, 2.4, blocks[i + 1][1], 2.4)
    ax.text(5, 0.7, "Roughly one-third instruction, two-thirds practice. That ratio is deliberate — beginners learn by typing, not by watching.",
            ha="center", fontsize=7, color=GREY, style="italic")
    save(fig, "fig4_session_structure.png")

# ---------------------------------------------------------------- figure 5
def fig5():
    # assessment map matrix: outcomes (rows) vs assessments (cols)
    fig, ax = plt.subplots(figsize=(8.5, 5))
    outcomes = ["LO1 think in steps", "LO2 explain code", "LO3 write small programs",
                "LO4 choose if/repeat", "LO5 organise data", "LO6 read errors", "LO7 build + finish"]
    assesses = ["Quizzes", "Exit tickets", "Small exercises", "Capstone"]
    # 1 = assessed, 0 = not
    m = np.array([
        [1, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
    ], dtype=float)
    ax.set_title("Figure 5: Assessment map — every outcome is tested somewhere", color=NAVY, pad=12)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            c = TEAL if m[i, j] == 1 else "#E9ECEF"
            rect = patches.Rectangle((j, i), 1, 1, facecolor=c, edgecolor="white", linewidth=2)
            ax.add_patch(rect)
            ax.text(j + 0.5, i + 0.5, "● tested" if m[i, j] == 1 else "—", ha="center", va="center",
                    fontsize=7, color="white" if m[i, j] == 1 else GREY, weight="bold" if m[i, j] == 1 else "normal")
    ax.set_xlim(0, 4); ax.set_ylim(0, 7)
    ax.set_xticks(np.arange(4) + 0.5, assesses, fontsize=8)
    ax.set_yticks(np.arange(7) + 0.5, outcomes, fontsize=8)
    ax.invert_yaxis()
    ax.set_xticks(np.arange(5) - 0.5, minor=True)
    ax.set_yticks(np.arange(8) - 0.5, minor=True)
    ax.grid(which="minor", color="white", linewidth=2)
    ax.tick_params(which="minor", length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.text(2, 7.45, "Each row has at least two checks. Nothing is assessed only once.",
            ha="center", fontsize=7, color=GREY, style="italic")
    save(fig, "fig5_assessment_map.png")

# ---------------------------------------------------------------- figure 6 (optional resource allocation)
def fig6():
    fig, ax = plt.subplots(figsize=(8.5, 4))
    roles = ["Lead\ninstructor", "Tutor x2", "Learner support", "Reviewer /\npilot lead", "Project\ncoordinator"]
    hours = [48, 32, 16, 14, 10]
    cols = [NAVY, TEAL, "#3A7CA5", AMBER, CORAL]
    bars = ax.bar(roles, hours, color=cols, edgecolor="white")
    for b, h in zip(bars, hours):
        ax.text(b.get_x() + b.get_width() / 2, h + 1, f"{h}h", ha="center", fontsize=9, weight="bold", color=NAVY)
    ax.set_ylabel("Planned hours (total 120h)", fontsize=9)
    ax.set_title("Figure 6: Planned effort by role (120 hours total)", color=NAVY, pad=10)
    ax.set_ylim(0, max(hours) * 1.2)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "fig6_resource_allocation.png")

if __name__ == "__main__":
    print(f"figures -> {OUT}")
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6()
    total = sum(p.stat().st_size for p in OUT.glob("*.png"))
    print(f"total png size: {total/1024:.0f} KB")
