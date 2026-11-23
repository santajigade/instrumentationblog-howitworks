PAGE = dict(
    slug="sequential-function-chart", grp="PLC", name="Sequential Function Chart (SFC)", kw="How a Sequential Function Chart Works",
    title="How a Sequential Function Chart Works: Animated SFC Example",
    desc="How a sequential function chart works, animated: steps, transitions and actions run a fill, mix and drain batch while a token marks the active step.",
    h1="How a Sequential Function Chart Works",
    hero="Set the fill, mix and drain times with the sliders. Watch the active step token move down the chart each time a transition condition becomes true, and see the tank follow the actions.",
    quick="A sequential function chart (SFC) splits a machine or batch process into steps joined by transitions. Only the active step runs its actions, and the chart moves to the next step when the transition condition below it becomes true.",
    intro=["SFC is one of the five PLC languages defined in IEC 61131 3, and it is based on the GRAFCET method of IEC 60848. It is drawn like a flowchart, but it has strict rules about which step is active and when it changes.",
           "Each step holds actions such as open a valve or start a motor, and each transition holds a Boolean condition such as a level switch or a timer. The step before a transition must be active and the condition must be true before the chart can move on.",
           "This makes sequences easy to read, test and troubleshoot, because the active step tells you exactly where the machine is waiting. Batch reactors, filling machines, CIP systems and start up sequences are common uses."],
    sliders=[("tf", "Fill time", 4, 20, 8, 1, 0, "s"), ("tm", "Mix time (step timer)", 4, 30, 10, 1, 0, "s"), ("td", "Drain time", 4, 20, 6, 1, 0, "s")],
    outs=[("ct", "Batch cycle time (with 2 s wait for Start)"), ("bph", "Batches per hour"), ("as", "Active step"), ("tmr", "Step elapsed time")],
    legend=["Initial step 0 (double box), active at power up", "Transition with its condition", "Action block with qualifier N", "Active step token",
            "Inlet valve XV1", "Agitator motor M1", "Level switches LSH and LSL", "Drain valve XV2"],
    steps=["At start up the initial step 0 is active and the chart waits for the Start command.",
           "When Start is true, transition 0 fires: step 0 is deactivated and step 1 Fill becomes active, opening inlet valve XV1.",
           "When the high level switch LSH closes, the chart moves to step 2 Mix; the agitator runs and the step timer counts.",
           "When the step elapsed time reaches the mix time, step 3 Drain opens XV2 until the low level switch LSL shows the tank is empty.",
           "The last transition jumps back to the initial step, so the sequence is ready for the next batch."],
    formula=["Batch cycle time = wait for Start + fill time + mix time + drain time",
             "Batches per hour = 3600 ÷ batch cycle time (s)",
             "A transition fires only when the step above it is active and its condition is true",
             "Mix transition condition: Mix.T ≥ mix time, where .T is the step elapsed time",
             "Example: 2 s wait + 8 s fill + 10 s mix + 6 s drain = 26 s, so 3600 ÷ 26 = 138.5 batches per hour"],
    parts=[("Step", "A state of the sequence; it is either active or inactive, and the initial step is drawn as a double box"),
           ("Transition", "A horizontal bar with a Boolean condition that moves the chart from one step to the next"),
           ("Action block", "Tells what a step does, with a qualifier such as N (while active), S (set), R (reset), L (time limited) or P (pulse)"),
           ("Step flags and timers", "Each step has an active flag .X and an elapsed time .T that logic and transitions can use"),
           ("Divergence and convergence", "A single line branch selects one path; a double line branch runs parallel paths at the same time")],
    uses=[("Batch processes", "Fill, heat, react, mix and discharge phases of a reactor or blending tank."),
          ("Packaging and filling machines", "Index, fill, cap and eject steps that repeat for every product."),
          ("Clean in place", "Rinse, caustic wash, rinse and acid wash phases with timers and temperature checks."),
          ("Equipment start up", "Ordered start of pumps, fans and valves with permissives checked at each step.")],
    pros=["The active step shows at a glance where a sequence is waiting", "Each step and transition can be tested on its own", "Parallel and alternative branches are drawn clearly"],
    cons=["Less suited to continuous control loops, which are better in function blocks", "Large charts need careful naming and layout to stay readable", "Mixing set and reset actions across steps can leave outputs on unexpectedly"],
    tips=["When a sequence stops, look at the active step and then check only the transition condition directly below it.",
          "Prefer N qualifiers for outputs so they switch off automatically when the step ends; use S and R only with a clear reset step.",
          "Add a step time limit alarm using .T so a valve that never reaches its limit switch raises a fault instead of waiting forever.",
          "Keep interlocks and emergency stops outside the SFC in plain logic so they act in every step."],
    faq=[("Is SFC a real PLC language?", "Yes. IEC 61131 3 defines SFC together with ladder diagram, function block diagram, structured text and instruction list. The actions and transitions inside an SFC are written in one of the other languages."),
         ("What is the difference between SFC and GRAFCET?", "GRAFCET, standardised in IEC 60848, is the design method for describing sequences. SFC is the PLC programming language built on the same idea of steps and transitions."),
         ("Can two steps be active at the same time?", "Yes, after a simultaneous divergence drawn with a double line. Both branches run in parallel and meet again at a double line convergence, which waits for all branches."),
         ("What does the N qualifier mean?", "N means non stored: the action is on only while the step is active. When the chart leaves the step, the action switches off.")],
    cal=[("plc-signal/plc-timer-preset-calculator", "PLC Timer Preset Calculator"), ("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time"), ("signals-plc-terms", "Signals and PLC Terms")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("sequential-function-chart-sfc-plc", "Sequential function chart in PLC programming"))

SCENE = r"""
var st=0,tm=0,lv=0.1,ang=0,fl=0,NM=['0 Idle','1 Fill','2 Mix','3 Drain'],SY=[44,110,176,242];
function dur(){return [2,P.tf,P.tm,P.td][st];}
function upd(){var c=2+P.tf+P.tm+P.td;o('ct',m(c,0)+' s');o('bph',m(3600/c,1));o('as','Step '+NM[st]);o('tmr',m(tm,1)+' s of '+m(dur(),0)+' s');}
function step(dt){tm+=dt;if(st==2)ang+=dt*7;if(fl>0)fl-=dt;
if(st==1)lv=0.1+0.8*Math.min(tm/P.tf,1);if(st==3)lv=0.9-0.8*Math.min(tm/P.td,1);
if(tm>=dur()){st=(st+1)%4;tm=0;fl=0.5;}
o('as','Step '+NM[st]);o('tmr',m(tm,1)+' s of '+m(dur(),0)+' s');}
function draw(){L('Sequence runs in real time; Start is given 2 s after Idle',20,22,11,'#5b6576','left');
var cx=110,TL=['Start','LSH','Mix.T ≥ '+m(P.tm,0)+' s','LSL'],AC=['N  Ready lamp','N  XV1 inlet open','N  M1 agitator on','N  XV2 drain open'];
ln(cx,36,cx,300,'#334155',2);
for(var i=0;i<4;i++){var y=SY[i],on=st==i;rc(cx-35,y,70,30,on?'#fff1e9':'#ffffff',on?'#d9622b':'#334155',3);if(on){C.lineWidth=2.5;C.strokeStyle='#d9622b';C.stroke();}
if(i==0)rc(cx-31,y+4,62,22,null,on?'#d9622b':'#334155',2);L(NM[i],cx,y+15,12,'#1a2333','center',1);
ln(cx+35,y+15,170,y+15,'#334155',1.5);rc(170,y+3,130,24,on?'#ecfdf5':'#f8fafc',on?'#16a34a':'#94a3b8');ln(188,y+3,188,y+27,on?'#16a34a':'#94a3b8',1.2);L(AC[i].slice(0,1),179,y+15,11,'#1a2333','center',1);L(AC[i].slice(3),194,y+15,11,'#1a2333','left',on?1:0);
var ty=y+47,fire=fl>0&&st==(i+1)%4;ln(cx-16,ty,cx+16,ty,fire?'#16a34a':'#1a2333',fire?5:3.5);L(TL[i],cx+24,ty,11,fire?'#16a34a':'#5b6576','left',1);}
ln(cx,300,40,300,'#334155',2);ln(40,300,40,36,'#334155',2);ln(40,36,cx,36,'#334155',2);ar(cx,36,cx,43,'#334155',2);
var ay=SY[st]+15,bl=0.5+0.5*Math.sin(T*6);ci(cx-22,ay,5+bl*1.5,'#d9622b');
L('Step timer',40,316,11,'#5b6576','left',1);rc(40,324,260,12,'#e2e8f0');rc(40,324,260*Math.min(tm/dur(),1),12,'#6b3fb0');
var X0=400,X1=560,YB=300,YT=90,yl=YB-lv*(YB-YT);
ln(340,62,430,62,'#64748b',8);ln(430,58,430,YT,'#64748b',8);var o1=st==1;C.fillStyle=o1?'#16a34a':'#94a3b8';C.beginPath();C.moveTo(368,52);C.lineTo(368,72);C.lineTo(392,52);C.lineTo(392,72);C.closePath();C.fill();L('XV1',380,42,11,'#1a2333','center',1);
rc(X0,YT,X1-X0,YB-YT,'#f8fafc','#475569',6);wave(X0+2,X1-2,yl,YB-2,'rgba(147,197,253,0.85)');if(o1)stream(430,YT,yl);
rc(466,48,32,24,st==2?'#16a34a':'#475569',null,4);L('M1',482,60,11,'#fff','center',1);ln(482,72,482,268,'#334155',3);
var bw=26*Math.cos(ang);rc(482-Math.abs(bw),264,Math.abs(bw)*2,6,'#334155');ln(482,267,482+bw,262,'#334155',3);
var hy=YB-0.9*(YB-YT),ly=YB-0.1*(YB-YT),hs=lv>=0.899,ls=lv>0.101;
rc(X1,hy-8,26,16,hs?'#bbf7d0':'#e2e8f0','#475569',3);L('LSH',X1+30,hy,11,'#1a2333','left',1);rc(X1,ly-8,26,16,ls?'#bbf7d0':'#e2e8f0','#475569',3);L('LSL',X1+30,ly,11,'#1a2333','left',1);
ln(480,YB,480,326,'#64748b',8);ln(480,326,628,326,'#64748b',8);var o2=st==3;C.fillStyle=o2?'#16a34a':'#94a3b8';C.beginPath();C.moveTo(532,316);C.lineTo(532,336);C.lineTo(556,316);C.lineTo(556,336);C.closePath();C.fill();L('XV2',544,346,11,'#1a2333','center',1);
if(o2){C.setLineDash([6,8]);C.lineDashOffset=-T*60;C.strokeStyle='#3b82f6';C.lineWidth=4;C.beginPath();C.moveTo(484,326);C.lineTo(626,326);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
L(m(lv*100,0)+' %',X1-8,YT+14,11,'#1e3a8a','right',1);
mk(1,cx+46,SY[0]-2);mk(2,cx-30,SY[1]+47);mk(3,310,SY[2]+3);mk(4,cx-48,ay);mk(5,404,62);mk(6,512,52);mk(7,X1+13,hy-20);mk(8,516,342);}
"""
