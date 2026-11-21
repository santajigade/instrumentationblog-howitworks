PAGE = dict(
    slug="override-control", grp="DCS", name="Override (Selector) Control", kw="How Override Control Works",
    title="How Override Control Works: Animated Diagram and Example",
    desc="How override control works, animated: a flow loop and a low level loop feed a low selector, and the lower output takes the valve when the tank runs low.",
    h1="How Override Control Works",
    hero="Set the flow demand, the average inflow to the tank and the low level override setpoint. Watch the flow controller drive the valve until the level falls to the limit, then see the level controller take over through the low selector.",
    quick="Override control lets two or more controllers share one valve through a high or low selector. The normal controller drives the valve, and a constraint controller takes over only when a limit such as low level, high pressure or motor current is reached.",
    intro=["A plant often needs to meet a normal target, such as a flow to the next unit, while never crossing a safe limit, such as an empty tank. Override control, also called selector or constraint control, handles both with one valve.",
           "Each controller works out its own output, and a low or high selector passes only one of them to the valve. The controller that asks for the safer valve position wins, so the constraint takes over only when it is needed.",
           "The controller that is not selected must not wind up. In a DCS the selected output is fed back as external reset to all controllers, so the idle one stays ready to take over smoothly."],
    sliders=[("sp", "Flow demand (FIC setpoint)", 20, 100, 60, 1, 0, "m³/h"), ("fin", "Average inflow to the tank", 20, 100, 50, 1, 0, "m³/h"), ("ls", "Low level override setpoint", 10, 50, 30, 1, 0, "%")],
    outs=[("vf", "Valve opening with FIC in control = SP ÷ 100 m³/h"), ("net", "Net change of tank contents at average inflow"), ("ov", "When LIC holds the level"), ("now", "Controller in charge now")],
    legend=["Level transmitter and override controller LIC", "Flow controller FIC", "Low selector", "Control valve on the outlet", "Flow transmitter", "External reset feedback to both controllers", "Trend: level, outflow and controller in charge"],
    steps=["In normal operation the flow controller asks for the valve opening that gives the required flow to the next unit.",
           "The level controller works on the same valve; while the level is above its low limit, its output is higher than the flow controller output.",
           "The low selector passes the lower of the two outputs to the valve, so the flow controller stays in charge.",
           "If inflow drops and the level falls to the override setpoint, the level controller output becomes the lower one and takes the valve, cutting outflow to match inflow.",
           "When inflow recovers and the level rises again, the flow controller output becomes the lower one and takes back control without a bump."],
    formula=["Valve signal = lower of (FIC output, LIC output)",
             "Valve opening with FIC in control = flow demand ÷ maximum valve flow",
             "With LIC in control at steady state: outflow = inflow, so valve opening = inflow ÷ maximum valve flow",
             "External reset: each controller output = Kc × error + selected output filtered by the integral time",
             "Example: maximum valve flow 100 m³/h, demand 60 m³/h, inflow 50 m³/h, low limit 30 %: FIC asks 60 % open, tank loses 60 − 50 = 10 m³/h, LIC then holds 30 % level with outflow 50 m³/h and the valve 50 % open"],
    parts=[("Normal controller", "Flow controller that meets the production target"),
           ("Override controller", "Level, pressure, temperature or current controller that guards a limit"),
           ("Selector block", "Low or high select block that passes one output to the valve"),
           ("External reset feedback", "Selected output fed back to the integral action of every controller to prevent windup"),
           ("Control valve", "Single final element shared by all controllers")],
    uses=[("Pump suction protection", "A low level or low suction pressure controller limits the outlet flow."),
          ("Compressor limits", "Discharge pressure control with motor current or temperature override."),
          ("Fired heaters", "Outlet temperature control with a high fuel gas pressure override."),
          ("Steam headers", "Pressure control with a high flow or low pressure limit on the users.")],
    pros=["Keeps the process inside its limits without operator action", "Uses one valve and standard DCS blocks", "Switches between controllers without a bump when external reset is used"],
    cons=["Needs careful choice of high or low select from the valve fail action", "Windup and slow takeover if external reset is not configured", "Harder for operators to follow; the active controller must be shown clearly"],
    tips=["Work out the selector type from what is safe: if closing the valve is safe, use a low selector; if opening is safe, use a high selector.",
          "Configure external reset or the equivalent feedback in your DCS so the idle controller does not wind up.",
          "Show the selected controller on the faceplate and alarm when the override is active for a long time.",
          "Tune each controller in auto on its own before connecting it to the selector, then test the takeover in both directions."],
    faq=[("What is the difference between override control and a trip?", "Override control keeps running and just limits the valve. A trip shuts the equipment down through the safety system."),
         ("Why does the idle controller not wind up?", "Its integral action is driven from the selected output instead of its own output, so it stays close to the valve position and is ready to take over."),
         ("Is override control the same as split range control?", "No. In split range one controller drives two valves; in override control two controllers share one valve."),
         ("Can there be more than two controllers?", "Yes, selectors can be cascaded, for example a low select of flow and level followed by a high select with a minimum flow limit.")],
    cal=[("control-valve/control-valve-opening-calculator", "Control Valve Opening Calculator")],
    glo=[],
    cmp=[],
    tool=[("tools/pid-tuning/pid-simulator", "PID Simulator"), ("tools/practice-tests/control-valve-and-pid-quiz", "Control Valve and PID Quiz")],
    blog=("override-control-selector-dcs", "Override control and selectors in DCS"))

SCENE = r"""
var FM=100,h=60,F=50,R=50,uf=50,ul=60,v=50,sel='FIC',fin=50,pts=[],hist=[],pre=0;for(var i=0;i<10;i++)pts.push(i/10);
function upd(){if(!pre){pre=1;for(var q=0;q<600;q++){T+=0.04;step(0.04);}}o('vf',m(P.sp/FM*100,0)+' % open');var n=P.fin-P.sp;o('net',(n<0?'Falls by ':'Rises by ')+m(Math.abs(n),0)+' m³/h');
o('ov',P.fin<P.sp?'Level '+m(P.ls,0)+' %, outflow '+m(P.fin,0)+' m³/h, valve '+m(P.fin/FM*100,0)+' %':'Not reached at this inflow');o('now',sel==='FIC'?'FIC (flow)':'LIC (low level override)');}
function step(dt){fin=Math.max(0,P.fin+20*Math.sin(2*Math.PI*T/28));F+=(FM*v/100-F)*Math.min(1,dt/0.8);
uf=clamp(R+0.6*(P.sp-F)/FM*100,0,100);ul=clamp(R+2*(h-P.ls),0,100);var s=uf<=ul?'FIC':'LIC';v=Math.min(uf,ul);R+=(v-R)*Math.min(1,dt/1.5);
h=clamp(h+(fin-F)/8*dt,0,100);if(s!==sel){sel=s;upd();}
for(var i=0;i<pts.length;i++)pts[i]=(pts[i]+dt*F/160)%1;hist.push([T,h,F,sel==='LIC']);while(hist.length&&T-hist[0][0]>30)hist.shift();}
function bub(x,y,t,c){ci(x,y,17,'#fff',c,2);L(t,x,y,11,c,'center',1);}
function draw(){var tx=30,ty=50,tw=140,th=180,Y=function(l){return ty+th-l/100*th;},lic=sel==='LIC';
L('Tank and loops sped up; maximum valve flow 100 m³/h',20,22,11,'#5b6576','left');
rc(tx-6,ty-6,tw+12,th+12,'#e2e8f0','#64748b',6);rc(tx,ty,tw,th,'#f8fafc');wave(tx,tx+tw,Y(h),ty+th,'rgba(147,197,253,0.85)');
ln(tx,Y(P.ls),tx+tw,Y(P.ls),'#d9622b',1.5,[5,4]);ln(tx+tw,Y(P.ls),tx+tw+8,Y(P.ls),'#d9622b',1.5);L('low limit '+m(P.ls,0)+' %',tx+tw+10,Y(P.ls),11,'#d9622b','left',1);
stream(tx+30,ty,Y(h));L('Inflow '+m(fin,0)+' m³/h',tx+38,ty+12,11,'#1e63b8','left',1);L('Level '+m(h,1)+' %',tx+tw/2,ty+th-12,12,'#1a2333','center',1);
rc(tx+tw,226,300,14,'#dbeafe','#94a3b8');pts.forEach(function(p){var x=tx+tw+300*p;if(x<258||x>282)ci(x,233,3,'#1e63b8');});ar(tx+tw+300,233,tx+tw+330,233,'#1e63b8',2);L(m(F,0)+' m³/h',tx+tw+320,252,11,'#1e63b8','center',1);
var vx=270,vy=233;C.fillStyle='#1e63b8';C.beginPath();C.moveTo(vx-14,vy-10);C.lineTo(vx+14,vy+10);C.lineTo(vx+14,vy-10);C.lineTo(vx-14,vy+10);C.closePath();C.fill();ln(vx,vy,vx,vy-20,'#475569',2);C.fillStyle='#e2e8f0';C.beginPath();C.arc(vx,vy-20,11,Math.PI,0);C.fill();C.strokeStyle='#475569';C.lineWidth=1.5;C.stroke();L(m(v,0)+' %',vx-18,vy+18,11,'#1a2333','right',1);
ln(380,226,380,212,'#475569',2);bub(380,196,'FT','#1e63b8');
ln(tx+tw+6,120,212,120,'#475569',2);bub(230,120,'LIC','#c2410c');bub(380,120,'FIC','#0e7490');
rc(286,150,44,30,'#1a2333',null,5);L('<',308,165,16,'#fbbf24','center',1);
C.setLineDash([5,5]);C.lineDashOffset=-T*24;C.lineWidth=2;C.strokeStyle='#16a34a';C.beginPath();C.moveTo(380,179);C.lineTo(380,137);C.stroke();
function sig(x1,y1,x2,y2,x3,y3,on){C.strokeStyle=on?'#16a34a':'#94a3b8';C.lineWidth=on?3:2;C.beginPath();C.moveTo(x1,y1);C.lineTo(x2,y2);C.lineTo(x3,y3);C.stroke();}
sig(230,137,230,160,286,160,lic);C.beginPath();C.moveTo(363,120);C.lineTo(340,120);C.lineTo(340,170);C.lineTo(330,170);C.strokeStyle=lic?'#94a3b8':'#16a34a';C.lineWidth=lic?2:3;C.stroke();
C.strokeStyle='#16a34a';C.lineWidth=3;C.beginPath();C.moveTo(308,180);C.lineTo(308,196);C.lineTo(vx,196);C.lineTo(vx,202);C.stroke();
C.strokeStyle='#7c3aed';C.lineWidth=1.5;C.setLineDash([3,4]);C.lineDashOffset=T*20;C.beginPath();C.moveTo(300,150);C.lineTo(300,70);C.lineTo(230,70);C.lineTo(230,103);C.moveTo(300,70);C.lineTo(380,70);C.lineTo(380,103);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L('external reset',355,62,11,'#7c3aed','center',1);
rc(440,46,180,150,'#1a2333',null,8);L('Selector inputs',530,60,11,'#cbd5e1','center',1);
function bar(y,lab,val,on,col){L(lab,452,y,11,'#fff','left',1);rc(492,y-8,116,16,'#334155');rc(492,y-8,116*val/100,16,on?'#22c55e':col);L(m(val,0)+' %',550,y,11,'#fff','center',1);}
bar(86,'FIC',uf,!lic,'#64748b');bar(116,'LIC',ul,lic,'#64748b');L('Lower one wins',530,142,11,'#cbd5e1','center');
var g=0.5+0.5*Math.sin(T*6);rc(456,156,148,28,lic?'rgba(251,146,60,'+(0.6+0.4*g)+')':'#16a34a',null,6);L(lic?'Override: LIC':'Normal: FIC',530,170,12,'#fff','center',1);
var gx0=70,gx1=620,gy0=276,gy1=340,TX=function(t){return gx1-(T-t)/30*(gx1-gx0);},TY=function(x){return gy1-x/100*(gy1-gy0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');for(var i=1;i<hist.length;i++)if(hist[i][3]){rc(TX(hist[i-1][0]),gy0,TX(hist[i][0])-TX(hist[i-1][0])+0.5,gy1-gy0,'rgba(251,146,60,0.22)');}
function tr(ix,c){C.strokeStyle=c;C.lineWidth=2;C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=TY(p[ix]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();}
ln(gx0,TY(P.ls),gx1,TY(P.ls),'#d9622b',1,[4,4]);tr(1,'#c2410c');tr(2,'#1e63b8');
L('Level %',gx0+6,gy0-10,11,'#c2410c','left',1);L('Outflow m³/h',gx0+70,gy0-10,11,'#1e63b8','left',1);L('Shaded: LIC in charge',gx0+170,gy0-10,11,'#c2410c','left');L('last 30 s',gx1,gy0-10,11,'#5b6576','right');
mk(1,200,96);mk(2,412,136);mk(3,286,140);mk(4,vx+26,vy-26);mk(5,404,204);mk(6,292,52);mk(7,gx0-38,gy0+30);}
"""
