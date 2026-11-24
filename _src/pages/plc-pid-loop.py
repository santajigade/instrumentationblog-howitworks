PAGE = dict(
    slug="plc-pid-loop", grp="PLC", name="PLC PID Loop Control", kw="How PLC PID Loop Control Works",
    title="How PLC PID Loop Control Works: Loop Update Time and Example",
    desc="How PLC PID loop control works, animated: the PID instruction runs every loop update time, adds P and I steps and drives the valve in a live trend.",
    h1="How PLC PID Loop Control Works",
    hero="Change the gain, the integral time and the loop update time. Watch the PID instruction execute on each update, see the output move in steps and check how the process value follows the setpoint changes.",
    quick="A PLC runs its PID instruction at a fixed loop update time, not continuously. On every update it reads the scaled process value, calculates the error and changes the analog output by a P step and an I step, so the output trend is a staircase.",
    intro=["Most PLCs offer a PID instruction or function block that turns a scaled analog input into an analog output. The block itself is standard, but how often it runs and how it is scaled decide how well the loop performs.",
           "The PID block is executed in a timed task or a cyclic interrupt at the loop update time, often called the sample time. Between updates the output is held, so a long update time adds delay to the loop.",
           "Many PLC PID blocks use the velocity form, which calculates a change in output on each update. That form gives bumpless transfer between manual and auto and stops integral windup at the output limits."],
    sliders=[("kc", "Controller gain Kc", 0.3, 4, 1.5, 0.1, 1, ""), ("ti", "Integral time Ti", 2, 30, 10, 0.5, 1, "s"), ("dt", "Loop update time Δt", 0.1, 3, 0.5, 0.1, 1, "s")],
    outs=[("p", "P step for a 10 % error step (Kc × Δe)"), ("i", "I step per update for a 10 % error (Kc × e × Δt ÷ Ti)"), ("r", "Updates per second and I ramp per second"), ("live", "Live SP, PV and CV (simulated)")],
    legend=["Analog input card: 4 to 20 mA to PV in %", "Timed task clock: loop update time", "PID instruction with P and I terms", "Analog output card: CV to 4 to 20 mA", "Control valve", "Process and transmitter", "Trend: SP, PV and stepped CV"],
    steps=["The analog input card converts the 4 to 20 mA signal to a raw count, and the program scales it to the process value in percent or engineering units.",
           "A timed task starts the PID instruction once every loop update time Δt, independent of the main scan.",
           "The block calculates the error e = SP − PV for direct or reverse action as configured.",
           "It adds a proportional step Kc × (e − previous e) and an integral step Kc × e × Δt ÷ Ti to the output, and clamps the result to the output limits.",
           "The new output is scaled to the analog output card, which drives the valve with 4 to 20 mA until the next update."],
    formula=["Velocity form: ΔCV = Kc × [(eₙ − eₙ₋₁) + (Δt ÷ Ti) × eₙ], then CVₙ = CVₙ₋₁ + ΔCV",
             "Position form: CVₙ = Kc × [eₙ + (Δt ÷ Ti) × Σe] + bias",
             "Integral ramp for a constant error = Kc × e ÷ Ti per second, whatever the update time",
             "Rule of thumb: keep Δt at or below one tenth of the process time constant and well below Ti",
             "Example: Kc 1.5, Ti 10 s, Δt 0.5 s, error steps from 0 to 10 %: P step = 1.5 × 10 = 15.0 %, I step = 1.5 × 10 × 0.5 ÷ 10 = 0.75 % per update, so the first update moves CV by 15.75 % and the I ramp is 2 × 0.75 = 1.5 % per second"],
    parts=[("Analog input and scaling", "Raw counts scaled to PV in percent or engineering units, with a fault check for broken wire"),
           ("Timed task", "Runs the PID instruction at a fixed loop update time"),
           ("PID instruction", "Holds gain, integral and derivative settings, action, limits and the manual and auto mode"),
           ("Analog output and scaling", "Converts CV in percent to counts for the 4 to 20 mA output card"),
           ("HMI faceplate", "Lets the operator change SP, mode and manual output and view the trend")],
    uses=[("Pump speed control", "Drive speed trims header pressure or flow in water systems."),
          ("Skid temperature control", "Heater or steam valve loops on packaged units."),
          ("Tank level control", "Inlet or outlet valve holds a buffer tank level."),
          ("Dosing control", "Chemical pump stroke or speed follows a flow or analyser signal.")],
    pros=["Built into almost every PLC, with no separate controller to buy", "Velocity form gives bumpless manual to auto transfer and simple anti windup", "Loop logic, interlocks and alarms live in one program"],
    cons=["A long or irregular update time adds delay and makes the loop less stable", "Scaling or action errors are easy to make and hard to see", "Parameter units differ between blocks, so tuning values do not copy directly"],
    tips=["Call the PID block from a timed task or cyclic interrupt, not the free running main scan, so Δt is constant.",
          "Check the units of Ti: some blocks use seconds, some minutes and some repeats per minute.",
          "Set the action correctly: reverse action for a valve that opens to raise the PV, direct action for one that opens to lower it.",
          "Initialise the output from the valve position on start up so the loop goes to auto without a bump."],
    faq=[("What is the loop update time in a PLC PID block?", "It is the interval at which the PID instruction is executed and the output is recalculated. The block uses it in the integral and derivative terms, so it must match the real task time."),
         ("Why does the PLC output move in steps?", "The block runs only once per update and holds the output in between. A short update time gives small, frequent steps that look smooth on the trend."),
         ("Does a longer update time change the integral action?", "The integral ramp per second stays the same because each I step grows with Δt. The extra delay between updates still reduces the stability margin."),
         ("What is the difference between velocity and position form?", "The position form calculates the full output on each update from the sum of all errors. The velocity form calculates only the change, which makes bumpless transfer and anti windup simpler.")],
    cal=[("plc-signal/analog-scaling-calculator", "Analog Scaling Calculator"), ("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time")],
    cmp=[],
    tool=[("tools/pid-tuning/pid-simulator", "PID Simulator"), ("tools/pid-tuning/pid-form-converter", "PID Form Converter"), ("tools/pid-tuning/lambda-tuning-calculator", "Lambda Tuning Calculator")],
    blog=("plc-pid-instruction-configuration", "PLC PID instruction configuration"))

SCENE = r"""
var ok=false,sp=40,pv=40,cvo=40,ep=0,acc=0,fl=0,hist=[],buf=[],TAU=8,TD=1,WIN=40,ns=0,lastP=0,lastI=0;
function upd(){o('p',m(P.kc*10,2)+' %');o('i',m(P.kc*10*P.dt/P.ti,3)+' % per update');o('r',m(1/P.dt,2)+' per s, '+m(P.kc*10/P.ti,2)+' % per s');o('live','SP '+m(sp,0)+' %, PV '+m(pv,1)+' %, CV '+m(cvo,1)+' %');}
function dlv(t){for(var i=buf.length-1;i>=0;i--)if(buf[i][0]<=t)return buf[i][1];return buf.length?buf[0][1]:cvo;}
function sim(dt){ns+=dt;sp=(Math.floor(ns/20)%2)?60:40;acc+=dt;if(acc>=P.dt){acc-=P.dt;var e=sp-pv;lastP=P.kc*(e-ep);lastI=P.kc*e*P.dt/P.ti;cvo=clamp(cvo+lastP+lastI,0,100);ep=e;fl=0.25;}
buf.push([ns,cvo]);while(buf.length&&ns-buf[0][0]>TD+0.5)buf.shift();var u=dlv(ns-TD);pv+=(u-pv)*dt/TAU;hist.push([ns,sp,pv,cvo]);while(hist.length&&ns-hist[0][0]>WIN)hist.shift();}
function step(dt){if(!ok){ok=true;ep=0;for(var k=0;k<520;k++)sim(0.05);}var n=Math.ceil(dt/0.02);for(var k=0;k<n;k++)sim(dt/n);fl=Math.max(0,fl-dt);upd();}
function bx(x,y,w,h,t,c){rc(x,y,w,h,'#f8fafc',c||'#94a3b8',8);L(t,x+w/2,y+14,11,'#1a2333','center',1);}
function draw(){
L('Simulated process: time constant 8 s, dead time 1 s; setpoint changes every 20 s',20,22,11,'#5b6576','left');
bx(20,48,96,82,'Analog input');L('PV '+m(pv,1)+' %',68,84,12,'#1e63b8','center',1);L('12 mA = 50 %',68,106,11,'#5b6576','center');
rc(140,40,250,132,'#ffffff','#475569',10);L('PLC timed task',265,54,11,'#5b6576','center',1);
var cx=180,cy=110,f=acc/P.dt;ci(cx,cy,26,'#f1f5f9','#94a3b8',2);C.strokeStyle='#c2410c';C.lineWidth=4;C.beginPath();C.arc(cx,cy,26,-Math.PI/2,-Math.PI/2+f*Math.PI*2);C.stroke();ln(cx,cy,cx+20*Math.sin(f*Math.PI*2),cy-20*Math.cos(f*Math.PI*2),'#1a2333',2);L('Δt '+m(P.dt,1)+' s',cx,cy+40,11,'#1a2333','center',1);
rc(222,66,156,96,fl>0?'#fff1e9':'#f8fafc',fl>0?'#d9622b':'#cbd5e1',8);L(fl>0?'PID executes':'PID instruction',300,80,11,fl>0?'#d9622b':'#1a2333','center',1);
L('e = '+m(sp-pv,1)+' %',300,98,11,'#1a2333','center');
var s=1.6;rc(236,112,58,14,'#e2e8f0');rc(265,112,clamp(lastP*s*4,-29,29),14,'#1e63b8');L('P '+m(lastP,2),265,138,11,'#1e63b8','center',1);
rc(306,112,58,14,'#e2e8f0');rc(335,112,clamp(lastI*s*8,-29,29),14,'#7c3aed');L('I '+m(lastI,2),335,138,11,'#7c3aed','center',1);
L('step added to CV',300,154,11,'#5b6576','center');
ar(116,90,140,90,'#1e63b8',2);ar(390,90,414,90,'#c2410c',2);
bx(414,48,96,82,'Analog output');L('CV '+m(cvo,1)+' %',462,84,12,'#c2410c','center',1);L(m(4+0.16*cvo,2)+' mA',462,106,11,'#5b6576','center');
var vx=560,vy=64,op=cvo/100;ln(500,vy+56,616,vy+56,'#cbd5e1',7);for(var k=0;k<5;k++){var px=((T*20*(0.2+op)+k*24)%116);ci(500+px,vy+56,2.5,'#3b82f6');}ln(510,90,vx,90,'#c2410c',2);C.fillStyle='#475569';C.beginPath();C.moveTo(vx-18,vy+46);C.lineTo(vx+18,vy+66);C.lineTo(vx+18,vy+46);C.lineTo(vx-18,vy+66);C.closePath();C.fill();ln(vx,vy+56,vx,vy+26,'#475569',3);rc(vx-16,vy+10,32,16,'#94a3b8',null,4);L(m(cvo,0)+' %',vx+24,vy+18,11,'#1a2333','left',1);
rc(500,140,120,40,'#e0f2fe','#0e7490',6);L('Process',540,160,11,'#0e7490','center',1);ci(598,160,9,'#fff','#0e7490',1.5);L('TT',598,160,9,'#0e7490','center',1);
ln(598,140,598,124,'#1e63b8',1.5,[3,3]);ln(598,124,620,124,'#1e63b8',1.5,[3,3]);ln(620,124,620,36,'#1e63b8',1.5,[3,3]);ln(620,36,20,36,'#1e63b8',1.5,[3,3]);ln(20,36,20,48,'#1e63b8',1.5,[3,3]);
var x0=40,x1=620,y0=208,y1=338,Y=function(v){return y1-(v-20)/60*(y1-y0);},X=function(t){return x1-(ns-t)/WIN*(x1-x0);};
rc(x0,y0,x1-x0,y1-y0,'#f6f8fc','#dde3ee',6);for(var v=20;v<=80;v+=20){ln(x0,Y(v),x1,Y(v),'#e2e8f0',1);L(v+' %',x0-4,Y(v),11,'#5b6576','right');}
function tr(i,col,w,stp){C.strokeStyle=col;C.lineWidth=w;C.beginPath();var py=null;hist.forEach(function(h,j){var x=X(h[0]),y=Y(clamp(h[i],20,80));if(!j)C.moveTo(x,y);else{if(stp)C.lineTo(x,py);C.lineTo(x,y);}py=y;});C.stroke();}
C.setLineDash([5,4]);tr(1,'#16a34a',1.5,0);C.setLineDash([]);tr(3,'#d9622b',1.8,1);tr(2,'#1e63b8',2.2,0);
L('SP',x0+8,y0+12,11,'#16a34a','left',1);L('PV',x0+34,y0+12,11,'#1e63b8','left',1);L('CV (stepped)',x0+60,y0+12,11,'#d9622b','left',1);L('last 40 s',x1-8,y0+12,11,'#5b6576','right');
mk(1,26,140);mk(2,148,74);mk(3,384,72);mk(4,414,130);mk(5,vx-30,vy+40);mk(6,490,184);mk(7,x1-14,y0+34);}
"""
