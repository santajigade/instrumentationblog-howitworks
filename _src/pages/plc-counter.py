PAGE = dict(
    slug="plc-counter", grp="PLC", name="PLC Up Counter (CTU)", kw="How a PLC Up Counter Works",
    title="How a PLC Up Counter Works: Animated CTU Diagram and Example",
    desc="How a PLC up counter works, animated: parts pass a sensor, each pulse adds one to the CTU count, the output turns on at the preset and a reset clears it.",
    h1="How a PLC Up Counter Works",
    hero="Set the preset value PV and how many parts per minute pass the sensor. Watch each pulse add one to the current value CV, see the output Q turn on at the preset and the reset input clear the count for the next batch.",
    quick="An up counter (CTU) adds one to its current value CV every time its count input CU changes from off to on. When CV reaches the preset value PV the output Q turns on, and a separate reset input R sets CV back to zero.",
    intro=["The up counter is the standard way to count parts, bottles, strokes or cycles in a PLC program. It is defined in the IEC 61131 standard as the CTU function block, with a down counter CTD and an up down counter CTUD alongside it.",
           "A CTU has a count input CU, a reset input R, a preset value PV, an output Q and a current value CV. It counts edges, not time, so a sensor that stays on gives only one count.",
           "Typical uses are batch counts on packaging lines, stroke counts for maintenance and counting machine cycles. Knowing how the counter handles reset, overflow and fast pulses avoids most counting faults on site."],
    sliders=[("pv", "Preset value PV", 2, 12, 5, 1, 0, ""), ("rate", "Parts per minute at the sensor", 10, 60, 30, 5, 0, "/min")],
    outs=[("tq", "Time to collect PV parts = PV × 60 ÷ rate"), ("cv", "Current value CV now"), ("q", "Output Q"), ("b", "Batches completed in the demo")],
    legend=["Part sensor wired to input I0.1 (CU)", "CTU counter block", "Preset value PV", "Current value CV", "Output Q driving coil Q0.0", "Reset input R from I0.2", "Timing diagram of CU, CV and Q"],
    steps=["The part sensor turns input I0.1 on each time a part passes, and this input drives the count input CU of the counter.",
           "On every off to on change of CU the counter adds one to its current value CV; holding CU on does not add more counts.",
           "When CV becomes equal to or greater than PV, the output Q turns on, for example to stop the conveyor or index a new box.",
           "CV keeps counting above PV if more parts arrive, until the counter is reset.",
           "A pulse on the reset input R sets CV back to zero and turns Q off, ready for the next batch."],
    formula=["Q = (CV ≥ PV)",
             "CV = CV + 1 on each off to on change of CU; R sets CV to 0",
             "Time to collect PV parts = PV × 60 ÷ parts per minute",
             "CV keeps counting above PV until reset, up to the limit of its data type, for example 32767 for a 16 bit INT",
             "Example: PV 5 and 30 parts per minute: time = 5 × 60 ÷ 30 = 10 s, so a batch of 5 parts takes about 10 s and Q turns on at the fifth part"],
    parts=[("CU count input", "Rung condition whose rising edge adds one to the count; usually a sensor contact"),
           ("R reset input", "Sets the current value to zero and turns the output off while it is on"),
           ("PV preset value", "The target count, entered as a constant or moved in from an HMI or recipe"),
           ("CV current value", "The running count, which can be shown on an HMI or compared in other rungs"),
           ("Q output", "Counter done bit that turns on when CV reaches PV")],
    uses=[("Batch packing", "Counts bottles or cartons into a case and signals when the case is full."),
          ("Maintenance counters", "Counts machine strokes or valve cycles so service is planned by use, not by date."),
          ("Production totals", "Keeps shift totals of good and rejected parts for display on the HMI."),
          ("Sequence steps", "Counts repeats of a step, such as the number of rinse cycles in a cleaning sequence.")],
    pros=["Simple and the same behaviour on almost every PLC", "Counts edges, so a part that stops under the sensor counts only once", "CV is easy to show on an HMI and to compare in other logic"],
    cons=["Pulses shorter than the scan time plus input filter can be missed", "A bouncing contact can add extra counts", "Counts can be lost on power failure unless the counter is retentive"],
    tips=["Make sure each pulse stays on and off for longer than one scan plus the input filter time; for fast pulses use a high speed counter input.",
          "Use a reset that is a single pulse, otherwise a held reset blocks all new counts.",
          "Check whether the counter is retentive if the count must survive a power cycle or a PLC restart.",
          "Debounce mechanical limit switches with a short on delay timer, or use a non contact sensor, to avoid double counts."],
    faq=[("What is the difference between CTU and CTD?", "A CTU counts up from zero towards the preset and sets Q when CV reaches PV. A CTD counts down from the preset and sets Q when CV reaches zero."),
         ("Does a PLC counter stop counting at the preset?", "No, in most PLCs CV keeps counting above PV until it is reset or reaches the limit of its data type. Q simply stays on while CV is at or above PV."),
         ("Why does my PLC counter miss counts?", "Usually the pulse is shorter than the scan time plus the input filter, so the PLC never sees it. Use a high speed counter input or slow the pulses down."),
         ("What happens when CU and R are on at the same time?", "The reset has priority in the IEC 61131 CTU, so CV stays at zero. Counting starts again once R turns off.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator"), ("plc-signal/encoder-rpm-calculator", "Encoder RPM Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time"), ("encoder", "Encoder")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("plc-counter-instructions-ctu-ctd", "PLC counter instructions CTU and CTD"))

SCENE = r"""
var pts=[],sp=80,SX=170,spawn=0,cn=0,q=false,cu=false,rt=-1,rp=0,bat=0,hist=[],pre=0;
function upd(){if(!pre){pre=1;for(var k=0;k<760;k++){T+=0.02;step(0.02);}bat=0;}o('tq',m(P.pv*60/P.rate,1)+' s');o('cv',cn+' of '+P.pv);o('q',q?'On: preset reached':'Off');o('b',bat+' batches');}
function step(dt){spawn-=dt;if(spawn<=0){spawn+=60/P.rate;pts.push({x:-20});}
for(var i=pts.length-1;i>=0;i--){pts[i].x+=sp*dt;if(pts[i].x>304)pts.splice(i,1);}
var now=false;for(var i=0;i<pts.length;i++)if(Math.abs(pts[i].x-SX)<15)now=true;
var r=rp>0;if(rp>0)rp-=dt;
if(now&&!cu&&!r)cn++;cu=now;if(r)cn=0;
var wq=q;q=cn>=P.pv;if(q&&!wq){rt=2;bat++;}if(rt>0){rt-=dt;if(rt<=0){rp=0.3;rt=-1;}}
o('cv',cn+' of '+P.pv);o('q',q?'On: preset reached':'Off');o('b',bat+' batches');
hist.push([T,cu,cn,q,r]);while(hist.length&&T-hist[0][0]>15)hist.shift();}
function pw(x1,y1,x2,y2,on){if(on){C.setLineDash([6,5]);C.lineDashOffset=-T*30;ln(x1,y1,x2,y2,'#16a34a',3.5,[6,5]);C.setLineDash([]);C.lineDashOffset=0;}else ln(x1,y1,x2,y2,'#475569',2);}
function ct(x,y,lab,on){var c=on?'#16a34a':'#475569';ln(x-6,y-12,x-6,y+12,c,2.5);ln(x+6,y-12,x+6,y+12,c,2.5);L(lab,x,y-22,11,'#1a2333','center',1);}
function draw(){var r=rp>0;
L('Demo resets the counter 2 s after Q turns on',20,22,11,'#5b6576','left');
rc(20,120,300,12,'#475569',null,4);C.setLineDash([10,10]);C.lineDashOffset=-T*sp;ln(24,126,316,126,'#94a3b8',2);C.setLineDash([]);C.lineDashOffset=0;
for(var i=0;i<pts.length;i++){var x=pts[i].x;if(x<0||x>330)continue;rc(x-15,92,30,28,'#d6a86a','#8a5a2b',3);}
rc(SX-16,44,32,20,'#334155',null,4);L('I0.1',SX,54,11,'#fff','center',1);C.globalAlpha=cu?1:0.45;ln(SX,64,SX,92,'#ef4444',3,[4,4]);C.globalAlpha=1;ci(SX+22,54,5,cu?'#f59e0b':'#475569');
L('Part sensor',SX-24,54,11,'#5b6576','right',1);ar(40,150,96,150,'#475569',2);L('Conveyor',110,150,11,'#475569','left',1);
var R0=340,R1=620,y1=70,y2=128;ln(R0,36,R0,160,'#1a2333',3);ln(R1,36,R1,160,'#1a2333',3);
pw(R0,y1,362,y1,true);ct(368,y1,'I0.1',cu);pw(374,y1,430,y1,cu);
pw(R0,y2,362,y2,true);ct(368,y2,'I0.2',r);pw(374,y2,430,y2,r);
rc(430,44,100,110,'#ffffff','#c2410c',8);C.lineWidth=2.5;C.strokeStyle='#c2410c';C.stroke();L('CTU   C1',480,56,12,'#1a2333','center',1);
L('CU',436,y1,11,'#1a2333','left',1);L('R',436,y2,11,'#1a2333','left',1);L('Q',524,y1,11,'#1a2333','right',1);L('PV',436,98,11,'#1a2333','left',1);L('CV',524,98,11,'#1a2333','right',1);
rc(384,90,40,18,'#fff7ed','#c2410c',3);L(String(P.pv),404,99,11,'#c2410c','center',1);ln(424,98,430,98,'#475569',2);
rc(536,90,40,18,'#eff6ff','#1e63b8',3);L(String(cn),556,99,12,'#1e63b8','center',1);ln(530,98,536,98,'#475569',2);
rc(446,112,68,8,'#e2e8f0');rc(446,112,68*Math.min(1,cn/P.pv),8,q?'#16a34a':'#1e63b8');
pw(530,y1,566,y1,q);C.strokeStyle=q?'#16a34a':'#475569';C.lineWidth=2.5;C.beginPath();C.arc(580,y1,12,Math.PI*0.65,Math.PI*1.35);C.stroke();C.beginPath();C.arc(580,y1,12,-Math.PI*0.35,Math.PI*0.35);C.stroke();L('Q0.0',580,y1-22,11,'#1a2333','center',1);pw(594,y1,R1,y1,q);
var x0=110,x1=620,X=function(t){return x1-(T-t)/15*(x1-x0);};
L('CU',x0-12,195,12,'#1a2333','right',1);L('CV',x0-12,250,12,'#1a2333','right',1);L('Q',x0-12,300,12,'#1a2333','right',1);L('R',x0-12,330,12,'#1a2333','right',1);
var mx=Math.max(P.pv+3,6),Yc=function(c){return 275-c/mx*55;};ln(x0,Yc(P.pv),x1,Yc(P.pv),'#c2410c',1,[4,3]);L('PV',x0+4,Yc(P.pv)-8,11,'#c2410c','left',1);ln(x0,275,x1,275,'#cbd5e1',1);
function tr(idx,base,hi,col,step){C.strokeStyle=col;C.lineWidth=2.2;C.beginPath();hist.forEach(function(h,i){var x=X(h[0]),y=idx==2?Yc(h[2]):(h[idx]?hi:base);if(i){var py=idx==2?Yc(hist[i-1][2]):(hist[i-1][idx]?hi:base);C.lineTo(x,py);C.lineTo(x,y);}else C.moveTo(x,y);});C.stroke();}
tr(1,205,185,'#16a34a');tr(2,0,0,'#1e63b8');tr(3,310,292,'#c2410c');tr(4,338,324,'#7c3aed');
ln(x1,180,x1,342,'#1a2333',1.5);L('now',x1-4,174,11,'#5b6576','right');L('last 15 s',x0,174,11,'#5b6576','left');
mk(1,SX-60,80);mk(2,480,164);mk(3,404,82);mk(4,556,82);mk(5,604,y1+20);mk(6,368,y2+26);mk(7,x0-58,250);}
"""
