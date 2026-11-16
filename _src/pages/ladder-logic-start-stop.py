PAGE = dict(
    slug="ladder-logic-start-stop", grp="PLC", name="Start Stop Latch in Ladder Logic", kw="Start Stop Ladder Logic",
    title="Start Stop Ladder Logic: How the Seal In Latch Works, Animated",
    desc="Start stop ladder logic animated: watch the seal in contact hold the motor on, the stop button break the rung and why the stop button is wired normally closed.",
    h1="How a Start Stop Latch Works in Ladder Logic",
    hero="Choose whether the stop button is wired normally closed or normally open and set the PLC scan time. Watch the demo press Start and Stop, then break the stop wire and see which wiring stops the motor safely.",
    quick="A start stop latch uses the output's own contact in parallel with the Start button, so the coil stays on after Start is released. A normally closed Stop button in series breaks the rung and drops the latch.",
    intro=["The start stop circuit with a seal in contact is the first program almost every PLC engineer writes. It copies the classic hard wired motor starter, where an auxiliary contact of the contactor holds its own coil.",
           "In ladder logic the Start contact and a contact of the output coil sit in parallel branches, and the Stop and overload contacts sit in series after them. One rung gives a memory that survives the release of the Start button.",
           "The detail that matters in the field is how the Stop button is wired. A normally closed stop button makes a broken wire act like a stop command, which is why it is the standard practice."],
    sliders=[("nc", "Stop button contact (1 = NC wired, 0 = NO wired)", 0, 1, 1, 1, 0, ""), ("scan", "PLC scan time", 5, 50, 10, 1, 0, "ms")],
    outs=[("q", "Motor output Q0.0"), ("eq", "Rung result now"), ("brk", "When the stop wire breaks"), ("rt", "Worst case PLC reaction to a button")],
    legend=["Start pushbutton, NO, input I0.0", "Stop pushbutton, input I0.1", "Seal in contact Q0.0 in parallel with Start", "Output coil Q0.0", "Contactor and motor", "PLC input card with status LEDs", "Demo sequence and motor state"],
    steps=["At rest the Stop and overload contacts are closed and the Start contact is open, so no power reaches the coil Q0.0.",
           "Pressing Start closes I0.0; the rung becomes true, Q0.0 turns on and the contactor starts the motor.",
           "In the same moment the seal in contact Q0.0 in the parallel branch closes, so the rung stays true after Start is released.",
           "Pressing Stop opens the NC field contact, the input I0.1 goes to 0 and the series contact breaks the rung; Q0.0 and its seal in contact drop out.",
           "A broken stop wire or a tripped overload also removes the input signal, so the motor stops instead of running out of control."],
    formula=["Q0.0 = (Start I0.0 OR Q0.0) AND Stop I0.1 AND Overload I0.2",
             "Stop and overload are wired NC in the field and examined as closed in the program, so a 1 means healthy",
             "Press Start: (1 OR 0) AND 1 AND 1 = 1; release Start: (0 OR 1) AND 1 AND 1 = 1, the latch holds",
             "Press Stop: (0 OR 1) AND 0 AND 1 = 0, the latch drops",
             "Example: NC stop button and 10 ms scan: the output reacts within about 2 × 10 = 20 ms, plus input filter and contactor time"],
    parts=[("Start pushbutton (NO)", "Momentary contact that sets the latch"),
           ("Stop pushbutton (NC)", "Momentary contact that breaks the latch; wired NC for fail safe stopping"),
           ("Seal in contact", "Contact of the output Q0.0 placed in parallel with Start to hold the rung on"),
           ("Output coil Q0.0", "Drives the contactor coil through the PLC output card"),
           ("Overload contact", "NC auxiliary contact of the overload relay that stops the motor on overcurrent")],
    uses=[("Motor starters", "Pumps, fans, conveyors and agitators started and stopped from a local station."),
          ("Process sequences", "Holding a step active after a momentary command."),
          ("Alarm acknowledge", "Latching an alarm until an operator resets it."),
          ("Training and testing", "The first rung used to learn contacts, coils and the scan cycle.")],
    pros=["Simple logic that every technician can read", "Copies the familiar hard wired starter", "Fail safe when Stop and overload are wired NC"],
    cons=["The latch is lost on PLC power cycle unless a retentive bit is used", "A Stop wired NO will not stop the motor if its wire breaks", "Not a substitute for a hard wired emergency stop and safety relay"],
    tips=["Wire Stop and overload contacts NC and examine them as closed in the program.",
          "Keep emergency stop in a hard wired safety circuit that removes power to the contactor, not only in PLC logic.",
          "Use the contactor auxiliary contact as a run feedback input to detect a contactor that did not pull in.",
          "Check the input LED on the card first: if Stop LED is off while nobody presses it, look for a broken wire or loose terminal."],
    faq=[("Why is the stop button wired normally closed?", "With an NC stop button the input is 1 when healthy. A broken wire or loose terminal makes it 0, which the program treats as a stop, so the fault is safe."),
         ("What is a seal in contact?", "It is a contact of the output coil placed in parallel with the Start button. Once the output is on, this contact keeps the rung true after Start is released."),
         ("Can I use set and reset instructions instead?", "Yes, set and reset coils give the same latch. Many engineers prefer the seal in rung because all conditions are visible on one line."),
         ("What happens if Start and Stop are pressed together?", "In this rung Stop is in series after the branch, so Stop wins and the motor stays off. This stop dominant behaviour is the safe choice.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time"), ("interposing-relay", "Interposing Relay")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("ladder-logic-for-beginners", "Ladder logic for beginners"))

SCENE = r"""
var cy=0,Q=false,st=[],ang=0,ev=[[1,1.6,'s'],[4,4.6,'p'],[6,6.6,'s'],[11,11.6,'p'],[15,15.6,'p']];
function inp(t){var sP=false,pP=false;ev.forEach(function(e){if(t>=e[0]&&t<e[1]){if(e[2]=='s')sP=true;else pP=true;}});var br=t>=9&&t<14;
var i1=P.nc?(!pP&&!br):(pP&&!br);return{s:sP,p:pP,br:br,i0:sP,i1:i1,ok:P.nc?i1:!i1};}
function evt(t){if(t>=9&&t<14)return t>=11&&t<11.6?'Stop pressed while the stop wire is broken':'Stop wire broken';var r='Waiting';ev.forEach(function(e){if(t>=e[0]&&t<e[1])r=e[2]=='s'?'Start pressed':'Stop pressed';});if(r=='Waiting'&&t>=14)r='Wire repaired';if(r=='Waiting'&&Q)r='Motor running, held by the seal in contact';return r;}
function upd(){var s=inp(cy);o('q',Q?'ON (motor running)':'OFF (motor stopped)');
o('eq',P.nc?'('+(s.i0?1:0)+' OR '+(Q?1:0)+') AND '+(s.i1?1:0)+' AND 1 = '+(Q?1:0):'('+(s.i0?1:0)+' OR '+(Q?1:0)+') AND NOT '+(s.i1?1:0)+' AND 1 = '+(Q?1:0));
o('brk',P.nc?'Input drops to 0, motor stops (fail safe)':'Input stays 0, motor keeps running (unsafe)');o('rt','up to '+m(2*P.scan,0)+' ms (2 scans)');}
function step(dt){cy+=dt;if(cy>=16){cy-=16;st=[];}var s=inp(cy),q0=Q;Q=(s.i0||Q)&&s.ok;if(q0!=Q||Math.random()<0.05)upd();st.push([cy,Q]);if(Q)ang+=dt*6;}
function cont(x,y,on,nc,lab,tag){var c=on?'#16a34a':'#475569';ln(x-6,y-12,x-6,y+12,c,2.5);ln(x+6,y-12,x+6,y+12,c,2.5);if(nc)ln(x-9,y+12,x+9,y-12,c,2);L(tag,x,y-22,11,'#1a2333','center',1);L(lab,x,y+24,11,'#5b6576','center');}
function pw(x1,y1,x2,y2,on){if(on){C.setLineDash([6,5]);C.lineDashOffset=-T*30;ln(x1,y1,x2,y2,'#16a34a',3.5,[6,5]);C.setLineDash([]);C.lineDashOffset=0;}else ln(x1,y1,x2,y2,'#475569',2);}
function fc(x,y,pressed,closedNow,head,lab){ci(x,y,11,head,'#1a2333',1.5);if(pressed)ci(x,y,15,null,head,2);L(lab,x,y+22,11,'#1a2333','center',1);
ci(104,y,3,'#1a2333');ci(140,y,3,'#1a2333');var by=closedNow?y-3:y-12;ln(100,by,144,by,'#1a2333',3);ln(122,by,122,by-8,'#1a2333',1.5);ln(x+11,y,98,y,'#94a3b8',1,[2,3]);}
function draw(){var s=inp(cy);
L('Demo time slowed down; one sequence lasts 16 s',20,22,11,'#5b6576','left');
ln(40,56,40,180,'#b02a52',3);L('+24 V',40,46,11,'#b02a52','center',1);
fc(70,80,s.s,s.s,'#22c55e','Start NO');var sc=P.nc?!s.p:s.p;fc(70,136,s.p,sc,'#ef4444',P.nc?'Stop NC':'Stop NO');
ln(40,80,104,80,'#b02a52',2);ln(40,136,104,136,'#b02a52',2);ln(40,180,104,180,'#b02a52',2);ln(104,180,140,180,'#475569',2);L('OL NC',122,170,11,'#1a2333','center',1);
ln(140,80,210,80,s.i0?'#b02a52':'#94a3b8',2);ln(140,180,210,180,'#b02a52',2);
if(s.br){ln(140,136,160,136,sc?'#b02a52':'#94a3b8',2);ln(176,136,210,136,'#94a3b8',2);ln(162,128,174,144,'#ef4444',2.5);ln(162,144,174,128,'#ef4444',2.5);}else ln(140,136,210,136,(sc)?'#b02a52':'#94a3b8',2);
rc(210,40,62,156,'#1a2333',null,6);L('Inputs',241,54,11,'#fff','center',1);[['I0.0',80,s.i0],['I0.1',136,s.i1],['I0.2',180,true]].forEach(function(r){ci(224,r[1],5,r[2]?'#22c55e':'#334155');L(r[0],252,r[1],11,'#fff','center',1);});
var R0=300,R1=620,y=90,y2=160;ln(R0,46,R0,204,'#1a2333',3);ln(R1,46,R1,204,'#1a2333',3);
var a=s.i0,b=Q,n1=a||b,n2=n1&&s.ok;
pw(R0,y,342,y,true);cont(354,y,a,false,'Start','I0.0');pw(366,y,402,y,a);
pw(R0+10,y,R0+10,y2,true);pw(R0+10,y2,342,y2,true);cont(354,y2,b,false,'Seal in','Q0.0');pw(366,y2,402,y2,b);pw(402,y2,402,y,b);
pw(402,y,436,y,n1);cont(448,y,n1&&s.ok,!P.nc,'Stop','I0.1');pw(460,y,496,y,n2);cont(508,y,n2,false,'OL','I0.2');pw(520,y,550,y,n2);
C.strokeStyle=n2?'#16a34a':'#475569';C.lineWidth=2.5;C.beginPath();C.arc(566,y,12,Math.PI*0.65,Math.PI*1.35);C.stroke();C.beginPath();C.arc(566,y,12,-Math.PI*0.35,Math.PI*0.35);C.stroke();L('Q0.0',566,y-22,11,'#1a2333','center',1);L('Motor',566,y+24,11,'#5b6576','center');pw(582,y,R1,y,n2);
rc(20,226,150,110,'#f6f8fc','#dde3ee',8);rc(30,240,46,30,Q?'#bbf7d0':'#e2e8f0','#475569',4);L('K1',53,255,12,'#1a2333','center',1);L('contactor',53,282,11,'#5b6576','center');
ci(124,270,28,Q?'#dbeafe':'#e2e8f0','#475569',2);L('M',124,270,13,'#1a2333','center',1);for(var k=0;k<3;k++){var aa=ang+k*2.094;ln(124+16*Math.cos(aa),270+16*Math.sin(aa),124+25*Math.cos(aa),270+25*Math.sin(aa),Q?'#1e63b8':'#94a3b8',3);}
L(Q?'Running':'Stopped',124,318,12,Q?'#16a34a':'#b02a52','center',1);
var x0=200,x1=620,ty=300;L(evt(cy),x0,236,12,'#1a2333','left',1);
rc(x0,ty-26,x1-x0,52,'#f8fafc','#e2e8f0');rc(x0+9/16*(x1-x0),ty-26,5/16*(x1-x0),52,'rgba(239,68,68,0.10)');
ev.forEach(function(e){var xa=x0+e[0]/16*(x1-x0);rc(xa,ty+14,(e[1]-e[0])/16*(x1-x0),10,e[2]=='s'?'#22c55e':'#ef4444');});
L('wire broken',x0+11.5/16*(x1-x0),ty+40,11,'#b02a52','center');L('Start',x0+1.3/16*(x1-x0),ty+40,11,'#16a34a','center');L('Stop',x0+4.3/16*(x1-x0),ty+40,11,'#b02a52','center');
C.strokeStyle='#1e63b8';C.lineWidth=2.5;C.beginPath();st.forEach(function(h,i){var xx=x0+h[0]/16*(x1-x0),yy=h[1]?ty-18:ty+4;if(i)C.lineTo(xx,yy);else C.moveTo(xx,yy);});C.stroke();L('motor',x0-6,ty-18,11,'#1e63b8','right');
ln(x0+cy/16*(x1-x0),ty-30,x0+cy/16*(x1-x0),ty+28,'#1a2333',2);
mk(1,190,64);mk(2,190,118);mk(3,322,y2-22);mk(4,566,y+46);mk(5,160,240);mk(6,262,40);mk(7,x1-14,ty-38);}
"""
