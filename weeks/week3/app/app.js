// Interactive module controller
let pyodide = null;
let pyReady = false;
const PROGRESS_KEY = "w3_progress_v1";
let progress = JSON.parse(localStorage.getItem(PROGRESS_KEY) || "{}");

function saveProgress() { localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress)); updateProgress(); }
function markDone(id) { progress[id] = true; saveProgress(); }
function isDone(id) { return !!progress[id]; }
function updateProgress() {
  const total = 12;
  const done = Object.keys(progress).filter(k=>progress[k]).length;
  const pct = Math.round((done/total)*100);
  document.getElementById("progress-text").textContent = pct + "% complete";
  document.getElementById("progress-fill").style.width = pct + "%";
}

async function initPyodide() {
  try {
    pyodide = await loadPyodide();
    pyReady = true;
  } catch (e) {
    pyReady = false;
    console.error("pyodide load failed", e);
  }
}
initPyodide();

async function runPython(code) {
  if (!pyReady) return { stdout: "", error: "Python runtime still loading. Please wait a moment and retry." };
  try {
    pyodide.runPython(`
import sys, io
sys.stdout = io.StringIO()
sys.stderr = io.StringIO()
`);
    await pyodide.runPythonAsync(code);
    const stdout = pyodide.runPython("sys.stdout.getvalue()");
    const stderr = pyodide.runPython("sys.stderr.getvalue()");
    pyodide.runPython("sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__");
    if (stderr && stderr.trim()) return { stdout: stdout, error: stderr };
    return { stdout: stdout, error: null };
  } catch (e) {
    try { pyodide.runPython("import sys; sys.stdout = sys.__stdout__; sys.stderr = sys.__stderr__"); } catch(_) {}
    return { stdout: "", error: String(e) };
  }
}

// ---------- helpers ----------
function el(html) { const d = document.createElement("div"); d.innerHTML = html.trim(); return d.firstElementChild; }
function setView(html) { document.getElementById("app").innerHTML = html; }
function codeBlock(code) { return `<pre class="code">${escapeHtml(code)}</pre>`; }
function escapeHtml(s) { return s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function section(title, body) { return `<section class="card"><h2>${title}</h2>${body}</section>`; }

// ---------- home ----------
function renderHome() {
  setView(`
    <h1>Programming Fundamentals: Interactive Module</h1>
    <p>This module follows the Week 2 curriculum. It teaches six core ideas using real Python that runs in your browser. No installation is needed.</p>
    <div class="card">
      <h3>How to use this module</h3>
      <ol>
        <li>Read the short explanation and analogy.</li>
        <li>Study the annotated example and run it.</li>
        <li>Try the visualiser and predict the output.</li>
        <li>Complete exercises and debugging challenges.</li>
        <li>Finish with the mini-project.</li>
      </ol>
      <p class="hint">Progress is saved automatically in this browser.</p>
    </div>
    <div class="row">
      <div class="col card"><h3>Variables</h3><p>Store and change information.</p><button class="btn" data-goto="variables">Start</button></div>
      <div class="col card"><h3>Operators</h3><p>Do maths and make decisions.</p><button class="btn" data-goto="operators">Start</button></div>
      <div class="col card"><h3>Conditionals</h3><p>Choose a path.</p><button class="btn" data-goto="conditionals">Start</button></div>
      <div class="col card"><h3>Loops</h3><p>Repeat work.</p><button class="btn" data-goto="loops">Start</button></div>
      <div class="col card"><h3>Functions</h3><p>Reuse steps.</p><button class="btn" data-goto="functions">Start</button></div>
      <div class="col card"><h3>Debugging</h3><p>Find and fix errors.</p><button class="btn" data-goto="debugging">Start</button></div>
    </div>
    <div class="card"><h3>Mini-project</h3><p>Combine everything in a small program.</p><button class="btn" data-goto="project">Open project</button></div>
  `);
  wireGoto();
}

function wireGoto() {
  document.querySelectorAll("[data-goto]").forEach(b => {
    b.addEventListener("click", () => showModule(b.dataset.goto));
  });
}

// ---------- variables ----------
function renderVariables() {
  setView(`
    <h1>Variables and Data Types</h1>
    ${section("Explanation", `<p>A variable is a named box that holds a value. You can put a number, some text, or true/false inside it. The name lets you use the value later.</p>`)}
    ${section("Real-world analogy", `<p>Think of a labelled jar in a kitchen. The label is the variable name. What is inside the jar is the value. You can replace what is inside without changing the label.</p>`)}
    ${section("Annotated example", codeBlock(`# a variable stores a value\nname = "Aisha"       # text (string)\nage = 22            # whole number (int)\nheight = 1.68       # decimal (float)\nis_student = True   # true/false (bool)\nprint(name, age, height, is_student)`))}
    <div class="card">
      <h3>Variable assignment visualiser</h3>
      <p>Enter a name and value, then assign.</p>
      <div class="row">
        <div class="col"><label>Name</label><input id="varname" value="score"></div>
        <div class="col"><label>Value</label><input id="varval" value="10"></div>
      </div>
      <button class="btn" id="assignBtn">Assign</button>
      <button class="btn secondary" id="resetVar">Reset</button>
      <div class="viz" id="varviz">No variables yet.</div>
    </div>
    ${section("Predict the output", `<p>What does this print?</p>${codeBlock(`x = 5\nx = x + 3\nprint(x)`)}
      <button class="btn" data-quiz="v1" data-ans="8">8</button>
      <button class="btn" data-quiz="v1" data-ans="5">5</button>
      <button class="btn" data-quiz="v1" data-ans="53">53</button>
      <div id="v1fb"></div>`)}
    ${section("Hands-on", `<p>Try your own code:</p>
      <textarea id="varcode"># change the values\nname = "Sam"\nprint("hello", name)</textarea>
      <button class="btn" id="runVar">Run</button>
      <div class="viz" id="varout"></div>`)}
    ${section("Common mistakes", `<ul>
      <li>Using a variable before giving it a value: <code>print(x)</code> before <code>x = 1</code>.</li>
      <li>Confusing <code>=</code> (assign) with <code>==</code> (compare).</li>
      <li>Forgetting quotes around text.</li>
    </ul>`)}
    ${section("Practical activity", `<p>Make variables for your own details: name, age, city. Print a sentence using them.</p>`)}
    <button class="btn" id="doneVar">Mark module complete</button>
  `);
  // visualiser
  const state = {};
  document.getElementById("assignBtn").onclick = () => {
    const n = document.getElementById("varname").value.trim();
    const v = document.getElementById("varval").value;
    if (!/^[a-zA-Z_][a-zA-Z0-9_]*$/.test(n)) { alert("Invalid variable name"); return; }
    state[n] = v;
    document.getElementById("varviz").innerHTML = Object.entries(state).map(([k,v])=>`<div>${k} = ${v}</div>`).join("") || "No variables yet.";
  };
  document.getElementById("resetVar").onclick = () => { for (const k in state) delete state[k]; document.getElementById("varviz").textContent = "No variables yet."; };
  document.getElementById("runVar").onclick = async () => {
    const r = await runPython(document.getElementById("varcode").value);
    document.getElementById("varout").textContent = r.error ? "Error: " + r.error : (r.stdout || "(no output)");
    document.getElementById("varout").className = "viz" + (r.error ? " feedback err" : " feedback ok");
  };
  // quiz
  document.querySelectorAll("[data-quiz='v1']").forEach(b => {
    b.onclick = () => {
      const fb = document.getElementById("v1fb");
      if (b.dataset.ans === "8") { fb.innerHTML = `<div class="feedback ok">Correct. x becomes 5, then 5+3=8.</div>`; markDone("variables_quiz"); }
      else { fb.innerHTML = `<div class="feedback err">Not quite. Reassigning x updates its value: 5 + 3 = 8.</div>`; }
    };
  });
  document.getElementById("doneVar").onclick = () => { markDone("variables"); alert("Marked complete."); };
  wireGoto();
}

// ---------- operators ----------
function renderOperators() {
  setView(`
    <h1>Operators and Expressions</h1>
    ${section("Explanation", `<p>Operators are symbols that act on values. + - * / do maths. ==, !=, <, > compare values. and, or, not combine true/false.</p>`)}
    ${section("Real-world analogy", `<p>Like a calculator plus a set of yes/no questions. You combine numbers and conditions to decide things.</p>`)}
    ${section("Annotated example", codeBlock(`a = 7\nb = 3\nprint(a + b)   # 10\nprint(a // b)  # 2 (whole division)\nprint(a % b)   # 1 (remainder)\nprint(a > b)   # True\nprint(a > 5 and b < 5)  # True`))}
    ${section("Hands-on", `<textarea id="opcode">print(10 % 3)\nprint(10 / 3)\nprint(10 // 3)</textarea>
      <button class="btn" id="runOp">Run</button><div class="viz" id="opout"></div>`)}
    ${section("Predict the output", `<p>Result?</p>${codeBlock(`print(2 + 3 * 4)`)}
      <button class="btn" data-q="o1" data-a="14">14</button>
      <button class="btn" data-q="o1" data-a="20">20</button>
      <div id="o1fb"></div>`)}
    ${section("Common mistakes", `<ul><li>Forgetting operator precedence: * before +.</li><li>Using = instead of == in comparisons.</li></ul>`)}
    ${section("Practical activity", `<p>Compute the total and average of three prices you choose.</p>`)}
    <button class="btn" id="doneOp">Mark module complete</button>
  `);
  document.getElementById("runOp").onclick = async () => {
    const r = await runPython(document.getElementById("opcode").value);
    document.getElementById("opout").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.querySelectorAll("[data-q='o1']").forEach(b=>{
    b.onclick=()=>{ const fb=document.getElementById("o1fb");
      if(b.dataset.a==="14"){ fb.innerHTML=`<div class="feedback ok">Correct. 3*4=12, +2=14.</div>`; markDone("operators_quiz"); }
      else fb.innerHTML=`<div class="feedback err">No. Multiplication happens first: 3*4=12, then +2.</div>`; };
  });
  document.getElementById("doneOp").onclick=()=>{markDone("operators"); alert("Marked complete.");};
  wireGoto();
}

// ---------- conditionals ----------
function renderConditionals() {
  setView(`
    <h1>Conditional Statements</h1>
    ${section("Explanation", `<p>An if statement runs code only when a condition is true. else runs when it is false. elif adds more branches.</p>`)}
    ${section("Real-world analogy", `<p>Like a fork in a road: if it rains, take an umbrella; otherwise walk normally.</p>`)}
    ${section("Annotated example", codeBlock(`temp = 30\nif temp > 35:\n    print("hot")\nelif temp > 20:\n    print("warm")\nelse:\n    print("cool")`))}
    <div class="card">
      <h3>Conditional decision simulator</h3>
      <p>Enter a temperature.</p>
      <input id="temp" value="28">
      <button class="btn" id="decBtn">Decide</button>
      <div class="viz" id="decOut"></div>
    </div>
    ${section("Predict the output", `<p>Output?</p>${codeBlock(`x = 4\nif x % 2 == 0:\n    print("even")\nelse:\n    print("odd")`)}
      <button class="btn" data-q="c1" data-a="even">even</button>
      <button class="btn" data-q="c1" data-a="odd">odd</button>
      <div id="c1fb"></div>`)}
    <div class="card">
      <h3>Parsons problem: reorder lines</h3>
      <p>Arrange to print "pass" if score >= 50.</p>
      <select multiple id="parsonsC" size="5">
        <option>if score >= 50:</option>
        <option>    print("pass")</option>
        <option>else:</option>
        <option>    print("fail")</option>
        <option>score = 60</option>
      </select>
      <button class="btn" id="checkParsonsC">Check</button>
      <div id="pcfb"></div>
    </div>
    ${section("Hands-on", `<textarea id="ccode">score = 72\nif score >= 90:\n    print("A")\nelif score >= 70:\n    print("B")\nelse:\n    print("C")</textarea>
      <button class="btn" id="runC">Run</button><div class="viz" id="cout"></div>`)}
    ${section("Common mistakes", `<ul><li>Forgetting colon at end of if line.</li><li>Wrong indentation.</li><li>Using = instead of ==.</li></ul>`)}
    ${section("Practical activity", `<p>Ask the user for a number and say if it is positive, negative, or zero.</p>`)}
    <button class="btn" id="doneC">Mark module complete</button>
  `);
  document.getElementById("decBtn").onclick = () => {
    const t = Number(document.getElementById("temp").value);
    let r = t > 35 ? "hot" : (t > 20 ? "warm" : "cool");
    document.getElementById("decOut").textContent = "Decision: " + r;
  };
  document.querySelectorAll("[data-q='c1']").forEach(b=>{
    b.onclick=()=>{ const fb=document.getElementById("c1fb");
      if(b.dataset.a==="even"){ fb.innerHTML=`<div class="feedback ok">Correct. 4 % 2 == 0, so even.</div>`; markDone("cond_quiz"); }
      else fb.innerHTML=`<div class="feedback err">No. 4 is divisible by 2.</div>`; };
  });
  document.getElementById("checkParsonsC").onclick = () => {
    const sel = document.getElementById("parsonsC");
    const order = Array.from(sel.selectedOptions).map(o=>o.value);
    const expected = ["score = 60","if score >= 50:","    print(\"pass\")","else:","    print(\"fail\")"];
    const fb = document.getElementById("pcfb");
    if (order.join("|") === expected.join("|")) { fb.innerHTML=`<div class="feedback ok">Correct order.</div>`; markDone("cond_parsons"); }
    else fb.innerHTML=`<div class="feedback err">Try again. Start with score = 60, then if, then print pass, else, print fail.</div>`;
  };
  document.getElementById("runC").onclick = async () => {
    const r = await runPython(document.getElementById("ccode").value);
    document.getElementById("cout").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("doneC").onclick=()=>{markDone("conditionals"); alert("Marked complete.");};
  wireGoto();
}

// ---------- loops ----------
function renderLoops() {
  setView(`
    <h1>Loops</h1>
    ${section("Explanation", `<p>A loop repeats a block of code. for loops repeat a known number of times; while loops repeat until a condition becomes false.</p>`)}
    ${section("Real-world analogy", `<p>Like turning pages of a book until you reach the end, or stirring soup 10 times.</p>`)}
    ${section("Annotated example", codeBlock(`for i in range(5):\n    print(i)\n\ntotal = 0\nfor n in [2, 4, 6]:\n    total = total + n\nprint("total", total)`))}
    <div class="card">
      <h3>Step-by-step loop visualiser</h3>
      <p>Loop from 1 to N.</p>
      <input id="nval" value="5">
      <button class="btn" id="loopBtn">Run step by step</button>
      <div class="viz" id="loopViz"></div>
    </div>
    ${section("Predict the output", `<p>Output?</p>${codeBlock(`i = 0\nwhile i < 3:\n    print(i)\n    i = i + 1`)}
      <button class="btn" data-q="l1" data-a="012">0 1 2</button>
      <button class="btn" data-q="l1" data-a="123">1 2 3</button>
      <div id="l1fb"></div>`)}
    ${section("Debugging challenge", `<p>This loop never stops. Fix it.</p>${codeBlock(`i = 0\nwhile i < 5:\n    print(i)\n    # missing update`)}
      <textarea id="fixLoop">i = 0\nwhile i < 5:\n    print(i)\n    i = i + 1</textarea>
      <button class="btn" id="runFixLoop">Run fixed</button><div class="viz" id="fixLoopOut"></div>`)}
    ${section("Hands-on", `<textarea id="lcode">for i in range(1, 6):\n    print(i * i)</textarea>
      <button class="btn" id="runL">Run</button><div class="viz" id="lout"></div>`)}
    ${section("Common mistakes", `<ul><li>Infinite loops (forgetting to update counter).</li><li>Off-by-one errors in range.</li></ul>`)}
    ${section("Practical activity", `<p>Print a multiplication table for a number you choose.</p>`)}
    <button class="btn" id="doneL">Mark module complete</button>
  `);
  document.getElementById("loopBtn").onclick = () => {
    const n = Number(document.getElementById("nval").value);
    let lines = [];
    for (let i=1;i<=n;i++){ lines.push(`iteration ${i}: i = ${i}`); }
    lines.push("done");
    document.getElementById("loopViz").textContent = lines.join("\n");
  };
  document.querySelectorAll("[data-q='l1']").forEach(b=>{
    b.onclick=()=>{ const fb=document.getElementById("l1fb");
      if(b.dataset.a==="012"){ fb.innerHTML=`<div class="feedback ok">Correct. Prints 0,1,2 then stops.</div>`; markDone("loops_quiz"); }
      else fb.innerHTML=`<div class="feedback err">No. i starts at 0 and stops before 3.</div>`; };
  });
  document.getElementById("runFixLoop").onclick = async () => {
    const r = await runPython(document.getElementById("fixLoop").value);
    document.getElementById("fixLoopOut").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("runL").onclick = async () => {
    const r = await runPython(document.getElementById("lcode").value);
    document.getElementById("lout").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("doneL").onclick=()=>{markDone("loops"); alert("Marked complete.");};
  wireGoto();
}

// ---------- functions ----------
function renderFunctions() {
  setView(`
    <h1>Functions</h1>
    ${section("Explanation", `<p>A function is a named reusable block of code. You define it once, then call it with inputs (arguments). It may return a result.</p>`)}
    ${section("Real-world analogy", `<p>Like a recipe: define steps once, then use them whenever you want a dish. Inputs are ingredients; output is the meal.</p>`)}
    ${section("Annotated example", codeBlock(`def greet(name):\n    return "hello " + name\n\nprint(greet("Aisha"))\nprint(greet("Ben"))`))}
    <div class="card">
      <h3>Function input/output simulator</h3>
      <p>Function: square(x) = x * x</p>
      <input id="fnin" value="4">
      <button class="btn" id="fnBtn">Call</button>
      <div class="viz" id="fnOut"></div>
    </div>
    ${section("Predict the output", `<p>Output?</p>${codeBlock(`def f(x):\n    return x + 1\nprint(f(f(3)))`)}
      <button class="btn" data-q="f1" data-a="5">5</button>
      <button class="btn" data-q="f1" data-a="4">4</button>
      <div id="f1fb"></div>`)}
    ${section("Hands-on", `<textarea id="fcode">def add(a, b):\n    return a + b\nprint(add(2, 3))</textarea>
      <button class="btn" id="runF">Run</button><div class="viz" id="fout"></div>`)}
    ${section("Common mistakes", `<ul><li>Forgetting to call the function (just defining it prints nothing).</li><li>Mismatched number of arguments.</li></ul>`)}
    ${section("Practical activity", `<p>Write a function that converts Celsius to Fahrenheit.</p>`)}
    <button class="btn" id="doneF">Mark module complete</button>
  `);
  document.getElementById("fnBtn").onclick = () => {
    const x = Number(document.getElementById("fnin").value);
    document.getElementById("fnOut").textContent = "square(" + x + ") = " + (x*x);
  };
  document.querySelectorAll("[data-q='f1']").forEach(b=>{
    b.onclick=()=>{ const fb=document.getElementById("f1fb");
      if(b.dataset.a==="5"){ fb.innerHTML=`<div class="feedback ok">Correct. f(3)=4, f(4)=5.</div>`; markDone("func_quiz"); }
      else fb.innerHTML=`<div class="feedback err">No. Apply f twice: 3+1=4, then 4+1=5.</div>`; };
  });
  document.getElementById("runF").onclick = async () => {
    const r = await runPython(document.getElementById("fcode").value);
    document.getElementById("fout").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("doneF").onclick=()=>{markDone("functions"); alert("Marked complete.");};
  wireGoto();
}

// ---------- debugging ----------
function renderDebugging() {
  setView(`
    <h1>Debugging and Algorithmic Thinking</h1>
    ${section("Explanation", `<p>Debugging is finding and fixing errors. Read the error message, locate the line, and check types and names.</p>`)}
    ${section("Real-world analogy", `<p>Like proofreading a recipe: find the step that does not make sense and correct it.</p>`)}
    ${section("Annotated example", codeBlock(`# NameError example\ndef total(items):\n    s = 0\n    for x in items:\n        s = s + x\n    return s\nprint(total([1,2,3]))`))}
    <div class="card">
      <h3>Debugging challenge 1</h3>
      <p>Fix the code so it prints 6.</p>
      <textarea id="dbg1">def total(items):\n    s = 0\n    for x in items:\n        s = s + x\n    return s\nprint(total([1, 2, 3]))</textarea>
      <button class="btn" id="runDbg1">Run</button><div class="viz" id="dbg1out"></div>
    </div>
    <div class="card">
      <h3>Debugging challenge 2</h3>
      <p>Fix type error.</p>
      <textarea id="dbg2">age = 20\nprint("age: " + str(age))</textarea>
      <button class="btn" id="runDbg2">Run</button><div class="viz" id="dbg2out"></div>
    </div>
    ${section("Algorithmic thinking", `<p>Break a problem into steps: input, process, output. Example: average of three numbers.</p>`)}
    ${section("Practical activity", `<p>Write steps in plain English for making tea, then turn them into code.</p>`)}
    <button class="btn" id="doneD">Mark module complete</button>
  `);
  document.getElementById("runDbg1").onclick = async () => {
    const r = await runPython(document.getElementById("dbg1").value);
    document.getElementById("dbg1out").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("runDbg2").onclick = async () => {
    const r = await runPython(document.getElementById("dbg2").value);
    document.getElementById("dbg2out").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("doneD").onclick=()=>{markDone("debugging"); alert("Marked complete.");};
  wireGoto();
}

// ---------- project ----------
function renderProject() {
  setView(`
    <h1>Guided Mini-Project</h1>
    <p>Build a small grade checker using variables, conditionals, loops, and a function.</p>
    ${section("Starter code", codeBlock(`def grade(score):\n    if score >= 90:\n        return "A"\n    elif score >= 70:\n        return "B"\n    else:\n        return "C"\n\nscores = [88, 72, 95, 60]\nfor s in scores:\n    print(s, grade(s))`))}
    <textarea id="projcode">def grade(score):\n    if score >= 90:\n        return "A"\n    elif score >= 70:\n        return "B"\n    else:\n        return "C"\n\nscores = [88, 72, 95, 60]\nfor s in scores:\n    print(s, grade(s))</textarea>
    <button class="btn" id="runProj">Run</button>
    <button class="btn secondary" id="resetProj">Reset</button>
    <div class="viz" id="projout"></div>
    <button class="btn" id="doneProj">Mark project complete</button>
  `);
  document.getElementById("runProj").onclick = async () => {
    const r = await runPython(document.getElementById("projcode").value);
    document.getElementById("projout").textContent = r.error ? "Error: "+r.error : (r.stdout || "(no output)");
  };
  document.getElementById("resetProj").onclick = () => {
    document.getElementById("projcode").value = `def grade(score):\n    if score >= 90:\n        return "A"\n    elif score >= 70:\n        return "B"\n    else:\n        return "C"\n\nscores = [88, 72, 95, 60]\nfor s in scores:\n    print(s, grade(s))`;
  };
  document.getElementById("doneProj").onclick=()=>{markDone("project"); alert("Marked complete.");};
  wireGoto();
}

function showModule(name) {
  document.querySelectorAll(".nav-btn").forEach(b=>b.classList.toggle("active", b.dataset.nav===name));
  if (name==="home") renderHome();
  else if (name==="variables") renderVariables();
  else if (name==="operators") renderOperators();
  else if (name==="conditionals") renderConditionals();
  else if (name==="loops") renderLoops();
  else if (name==="functions") renderFunctions();
  else if (name==="debugging") renderDebugging();
  else if (name==="project") renderProject();
  updateProgress();
}

document.querySelectorAll(".nav-btn").forEach(b=>{
  b.addEventListener("click", ()=>showModule(b.dataset.nav));
});
showModule("home");
updateProgress();
