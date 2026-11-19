PAGE = dict(
    slug="pid-controller", grp="DCS", name="PID Controller", kw="How a PID Controller Works",
    title="How a PID Controller Works: Animated Loop, Formula and Example",
    desc="How a PID controller works, animated: see the P, I and D terms build the output, the valve move and the temperature follow setpoint steps in a live trend.",
    h1="How a PID Controller Works",
    hero="Change the controller gain, integral time and derivative time. Watch the P, I and D bars build the valve output and see how the temperature follows each setpoint step, with less or more overshoot.",
    quick="A PID controller compares the measured value with the setpoint and moves its output to remove the error. The proportional term acts on the size of the error, the integral term on how long it has lasted and the derivative term on how fast it is changing.",
    intro=["PID control is the workhorse of process plants. Nearly every flow, pressure, level and temperature loop in a DCS or PLC uses a PID block to drive a control valve, a damper or a drive.",
           "The controller works on the error, the difference between setpoint and process value. Its output is the sum of three actions: proportional, integral and derivative, each set by one tuning parameter.",
           "Good tuning balances speed and stability. Too much gain or too short an integral time makes the loop oscillate, while too little makes it slow and leaves the process away from setpoint for a long time."],
    sliders=[("kc", "Controller gain Kc", 0.2, 6, 2, 0.1, 1, ""), ("ti", "Integral time Ti", 1, 40, 8, 0.5, 1, "s"), ("td", "Derivative time Td", 0, 5, 1, 0.1, 1, "s")],
    outs=[("pb", "Proportional band (100 ÷ Kc)"), ("p", "P action for a 10 % error (Kc × e)"), ("i", "I action ramp for a 10 % error (Kc × e ÷ Ti)"), ("os", "Overshoot on a 20 % setpoint step (simulated)")],
    legend=["Setpoint", "Summing junction: error = SP − PV", "P, I and D terms inside the controller", "Controller output to the steam valve", "Heated tank with temperature transmitter", "Trend of SP, PV and output"],
    steps=["The transmitter measures the process value, here the tank temperature, and sends it to the controller.",
           "The controller calculates the error e = SP − PV every execution cycle.",
           "The P term gives an output change in proportion to the error, so a bigger error moves the valve further.",
           "The I term keeps adding the error over time until it is zero, removing the offset that P alone leaves.",
           "The D term reacts to the rate of change of the PV and brakes the output as the PV approaches setpoint, reducing overshoot."],
    formula=["Output = Kc × (e + (1 ÷ Ti) × ∫e dt + Td × de/dt)",
             "Proportional band PB = 100 ÷ Kc (%)",
             "With a constant error, the I term ramps at Kc × e ÷ Ti per second",
             "Many controllers apply derivative to the PV only, so a setpoint step does not kick the output",
             "Example: Kc 2, Ti 8 s, Td 1 s, e = 10 %: P = 2 × 10 = 20 %, I ramps at 2 × 10 ÷ 8 = 2.5 % per s, D for a PV rising 1 % per s = −2 × 1 × 1 = −2 %, PB = 50 %"],
    parts=[("Process value input", "Measurement from the transmitter, scaled to engineering units or percent"),
           ("Setpoint", "Target value entered by the operator or sent by another controller"),
           ("PID algorithm", "Calculates the P, I and D terms every execution cycle"),
           ("Output and limits", "Sends 0 to 100 % to the final element and stops the I term winding up at the limits"),
           ("Final control element", "Control valve, damper or drive that changes the process")],
    uses=[("Temperature control", "Steam or fuel valves on heat exchangers, furnaces and reactors."),
          ("Flow control", "Fast loops on feeds and utilities, usually PI with little or no derivative."),
          ("Pressure control", "Vessel, header and compressor pressure loops."),
          ("Level control", "Tank and drum levels, often with gentle tuning to smooth the outflow.")],
    pros=["Works on most process loops with only three settings", "Integral action removes steady offset", "Well understood, available in every DCS and PLC"],
    cons=["Needs tuning, and the best settings change with the process", "Derivative amplifies measurement noise", "Large dead time limits how fast any PID loop can respond"],
    tips=["Check the controller form and units first; gain or proportional band and repeats or minutes per repeat change the meaning of the numbers.",
          "Leave derivative at zero for flow and noisy loops and use it mainly on slow temperature loops.",
          "Check the valve for stiction and the transmitter for noise before retuning a loop that cycles.",
          "Make one change at a time and record the old values so you can return to them."],
    faq=[("What does each term of a PID controller do?", "P reacts to the present error, I to the accumulated past error and D to the rate of change, which predicts where the error is heading."),
         ("Why does a P only controller leave an offset?", "With P alone the output only changes when there is an error, so the loop settles where a small error is needed to hold the required output. Integral action removes it."),
         ("What is integral windup?", "When the output is at a limit and the error stays, the integral term keeps growing. When the error reverses, the output stays at the limit too long and the PV overshoots; anti windup logic stops this."),
         ("What is the difference between gain and proportional band?", "They describe the same thing. Proportional band in percent is 100 divided by the gain, so a gain of 2 equals a band of 50 %.")],
    cal=[],
    glo=[],
    cmp=[],
    tool=[("tools/pid-tuning/pid-simulator", "PID Simulator"), ("tools/pid-tuning/proportional-band-calculator", "Proportional Band Calculator"), ("tools/practice-tests/control-valve-and-pid-quiz", "Control Valve and PID Quiz")],
    blog=("pid-controller-types-explained", "PID controller types explained"))

SCENE = r"""
var TAU=8,TH=2,DT=0.05,SPD=4,X,acc=0,hist=[],pt=[];for(var k=0;k<14;k++)pt.push(Math.random());
function mk0(sp){return {pv:sp,sp:sp,u:sp,I:sp,P:0,D:0,buf:[],t:0,lp:sp,df:0};}
function sim(s){s.buf.push(s.u);var nd=Math.round(TH/DT);var ud=s.buf.length>nd?s.buf.shift():s.buf[0];
s.pv+=(ud-s.pv)*DT/TAU;var e=s.sp-s.pv;s.P=P.kc*e;var dp=(s.pv-s.lp)/DT;s.lp=s.pv;var a=P.td>0?DT/(DT+0.1*P.td):1;s.df+=a*(dp-s.df);s.D=-P.kc*P.td*s.df;
s.I+=P.kc*e*DT/P.ti;var u=s.P+s.I+s.D;if(u>100){u=100;s.I=Math.min(s.I,100-s.P-s.D);}if(u<0){u=0;s.I=Math.max(s.I,-s.P-s.D);}s.u=u;s.t+=DT;}
function upd(){var s=mk0(40);for(var k=0;k<40;k++)sim(s);s.sp=60;var mx=40,lt=0;for(var k=0;k<2400;k++){sim(s);mx=Math.max(mx,s.pv);if(k>2000)lt=Math.max(lt,Math.abs(s.pv-60));}
var os=(mx-60)/20*100;o('pb',m(100/P.kc,1)+' %');o('p',m(P.kc*10,1)+' %');o('i',m(P.kc*10/P.ti,2)+' % per s');o('os',lt>1?'Loop oscillates, reduce Kc or raise Ti':m(Math.max(0,os),1)+' % of the step');
X=mk0(40);hist=[];for(var k=0;k<1100;k++)adv();}
function adv(){X.sp=(Math.floor(X.t/30)%2)?60:40;sim(X);if(Math.round(X.t/DT)%4==0){hist.push([X.t,X.sp,X.pv,X.u]);while(hist.length&&X.t-hist[0][0]>60)hist.shift();}}
function step(dt){acc+=dt*SPD;while(acc>=DT){acc-=DT;adv();}
for(var k=0;k<pt.length;k++){pt[k]+=dt*X.u/100*0.9;if(pt[k]>1)pt[k]-=1;}}
function bar(x,y,lb,v,c){L(lb,x-6,y+7,12,'#fff','right',1);rc(x,y,100,14,'#334155');var w=clamp(v,-50,100);var z=x+(lb=='I'?0:33);if(lb=='I')rc(x,y,w,14,c);else rc(w>=0?z:z+w*0.67,y,Math.abs(w)*0.67,14,c);if(lb!='I')ln(z,y-2,z,y+16,'#94a3b8',1);L(m(v,1),x+104,y+7,11,'#e2e8f0','left');}
function draw(){var s=X;
L('Simulated 4 times faster than real time; process lag 8 s, dead time 2 s',20,22,11,'#5b6576','left');
rc(20,66,70,44,'#ffffff','#1a2333',6);L('SP',55,78,11,'#5b6576','center',1);L(m(s.sp,0)+' %',55,96,13,'#1a2333','center',1);ar(90,88,114,88,'#1a2333',2);
ci(128,88,14,'#fff','#1a2333',2);L('+',121,80,11,'#1a2333','center',1);L('−',128,98,11,'#1a2333','center',1);L('e '+m(s.sp-s.pv,1),118,122,11,'#b02a52','right',1);ar(142,88,166,88,'#1a2333',2);
rc(166,46,170,96,'#1a2333',null,8);L('PID controller',251,60,11,'#cbd5e1','center',1);bar(186,74,'P',s.P,'#60a5fa');bar(186,96,'I',s.I,'#a78bfa');bar(186,118,'D',s.D,'#f59e0b');
C.setLineDash([5,4]);C.lineDashOffset=-T*25;C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();C.moveTo(336,60);C.lineTo(392,60);C.lineTo(392,71);C.stroke();C.setLineDash([]);C.lineDashOffset=0;L('OUT '+m(s.u,1)+' %',342,46,11,'#d9622b','left',1);
var vx=392,vy=104;ln(vx,vy,vx,80,'#475569',3);C.fillStyle='#94a3b8';C.beginPath();C.ellipse(vx,80,16,9,0,Math.PI,0);C.fill();
C.fillStyle='#475569';C.beginPath();C.moveTo(vx-12,vy-10);C.lineTo(vx+12,vy+10);C.lineTo(vx+12,vy-10);C.lineTo(vx-12,vy+10);C.closePath();C.fill();
rc(330,100,50,8,'#e2e8f0');rc(404,100,46,8,'#e2e8f0');L('Steam',336,122,11,'#5b6576','left');
for(var k=0;k<pt.length;k++){var x=330+pt[k]*120;if(x>vx-12&&x<vx+12)continue;ci(x,104,2.5,'#94a3b8');}
var hot=clamp((s.pv-30)/40,0,1);rc(450,48,130,120,'rgb('+Math.round(190+60*hot)+','+Math.round(220-70*hot)+','+Math.round(250-130*hot)+')','#475569',10);
C.strokeStyle='#64748b';C.lineWidth=3;C.beginPath();C.moveTo(450,104);for(var k=0;k<5;k++){C.lineTo(560,112+k*10);C.lineTo(462,117+k*10);}C.stroke();
L('Heated tank',515,180,11,'#5b6576','center',1);ln(580,80,600,80,'#1a2333',2);ci(612,80,12,'#fff','#1a2333',2);L('TT',612,81,11,'#1a2333','center',1);L('PV '+m(s.pv,1),612,104,11,'#16a34a','center',1);
C.setLineDash([4,3]);C.strokeStyle='#16a34a';C.lineWidth=1.5;C.beginPath();C.moveTo(612,116);C.lineTo(612,190);C.lineTo(128,190);C.lineTo(128,102);C.stroke();C.setLineDash([]);
var x0=60,x1=620,y0=206,y1=344,Y=function(v){return y1-(v-0)/100*(y1-y0);};rc(x0,y0,x1-x0,y1-y0,'#f8fafc','#e2e8f0');
[0,50,100].forEach(function(v){L(v+' %',x0-6,Y(v),11,'#5b6576','right');ln(x0,Y(v),x1,Y(v),'#e2e8f0',1);});
[[1,'#64748b',1.5,[5,4]],[3,'#d9622b',1.5],[2,'#16a34a',2.4]].forEach(function(c){C.strokeStyle=c[1];C.lineWidth=c[2];C.setLineDash(c[3]||[]);C.beginPath();hist.forEach(function(h,i){var x=x1-(s.t-h[0])/60*(x1-x0),y=Y(h[c[0]]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();C.setLineDash([]);});
L('Last 60 s:',x0+8,y0+12,11,'#1a2333','left',1);L('SP',x0+76,y0+12,11,'#64748b','left',1);L('PV',x0+102,y0+12,11,'#16a34a','left',1);L('output',x0+128,y0+12,11,'#d9622b','left',1);
mk(1,20,62);mk(2,128,60);mk(3,176,46);mk(4,428,46);mk(5,592,54);mk(6,x0+190,y0+12);}
"""
