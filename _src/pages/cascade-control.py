PAGE = dict(
    slug="cascade-control", grp="DCS", name="Cascade Control Loop", kw="How Cascade Control Works",
    title="How Cascade Control Works: Animated Loop Diagram and Example",
    desc="How cascade control works, animated: a master temperature loop sets a fast steam flow loop. Compare it with a single loop when the steam supply pressure drops.",
    h1="How Cascade Control Works",
    hero="Set the size of the steam pressure upset and how slow the temperature responds. Watch the inner flow loop cancel the upset before it reaches the temperature, and compare the trend with a single loop.",
    quick="Cascade control uses two controllers in series. The master controller watches the main variable, such as temperature, and its output becomes the setpoint of a fast slave controller, such as steam flow, which corrects supply upsets before they disturb the main variable.",
    intro=["In a single loop the temperature controller moves the steam valve directly. If the steam header pressure drops, the flow falls at once, but the controller only reacts after the temperature has already moved.",
           "Cascade control adds a flow transmitter and a flow controller inside the temperature loop. The inner loop sees the flow drop within a second and opens the valve further, so the heat input stays almost constant.",
           "Cascade is one of the most used advanced control schemes in a DCS. It appears on heat exchangers, reactors, boiler drums, distillation reboilers and valve positioners."],
    sliders=[("d", "Steam supply pressure drop", 5, 40, 20, 5, 0, "%"), ("tau", "Temperature time constant", 3, 20, 6, 1, 0, "s")],
    outs=[("loss", "Instant steam flow loss at the upset"), ("ratio", "Inner loop speed ratio (temperature lag ÷ flow lag)"), ("pks", "Peak temperature error, single loop"), ("pkc", "Peak temperature error, cascade")],
    legend=["Steam control valve", "Flow transmitter FT", "Slave flow controller FIC (inner loop)", "Master temperature controller TIC (outer loop)", "Temperature transmitter TT", "Heat exchanger", "Trend: single loop against cascade"],
    steps=["The master controller TIC compares the product temperature with its setpoint and calculates the steam flow needed.",
           "That output is sent as a remote setpoint to the slave controller FIC, which is switched to cascade mode.",
           "The FIC compares measured steam flow with this setpoint and moves the control valve to hold the flow.",
           "When the steam supply pressure drops, the flow falls and the FIC opens the valve within about a second, long before the temperature changes.",
           "The TIC only has to correct slow changes such as load or feed temperature, so the temperature stays close to setpoint."],
    formula=["Slave setpoint = master controller output; valve = slave PID (flow setpoint − flow measurement)",
             "Instant flow loss at a supply upset ≈ valve flow × pressure drop fraction",
             "Rule: the inner loop should respond at least about 3 to 5 times faster than the outer loop",
             "Tune the inner loop first in auto, then put it in cascade and tune the outer loop",
             "Example: steam flow 50 % of span and a 20 % pressure drop: flow falls by 0.2 × 50 = 10 % at once; with a 6 s temperature lag and a 0.3 s flow lag the inner loop is 20 times faster"],
    parts=[("Master controller (TIC)", "Controls the main process variable and writes the setpoint of the slave"),
           ("Slave controller (FIC)", "Controls the fast secondary variable and drives the valve"),
           ("Flow transmitter", "Measures the secondary variable so upsets are seen early"),
           ("Temperature transmitter", "Measures the primary variable the plant cares about"),
           ("Control valve", "Final element, moved only by the slave controller")],
    uses=[("Heat exchangers and reboilers", "Temperature master on a steam or hot oil flow slave."),
          ("Boiler drum level", "Level master on a feedwater flow slave in three element control."),
          ("Reactor jackets", "Reactor temperature master on a jacket temperature slave."),
          ("Valve positioners", "Any flow or pressure loop with a positioner is a cascade onto valve position.")],
    pros=["Upsets in the inner loop are corrected before they reach the main variable", "The outer loop can be tuned tighter because the inner loop makes the valve more linear", "Uses standard PID blocks available in every DCS"],
    cons=["Needs an extra transmitter and controller", "Gives little benefit if the inner loop is not much faster than the outer loop", "Mode handling and setpoint tracking must be configured correctly for bumpless transfer"],
    tips=["Tune the slave loop first with the master in manual; a slow or oscillating slave makes the cascade worse than a single loop.",
          "Use setpoint tracking so the slave setpoint follows its measurement while the loop is not in cascade.",
          "Make sure the master output range matches the slave setpoint range in engineering units.",
          "Check that the slave really is in cascade mode on the faceplate; a slave left in auto ignores the master."],
    faq=[("What is the difference between master and slave in cascade control?", "The master or primary controller controls the variable you care about. The slave or secondary controller receives its setpoint from the master and drives the valve."),
         ("When should I use cascade control?", "Use it when a measurable secondary variable responds much faster than the main variable and carries most of the disturbances, such as steam flow ahead of temperature."),
         ("Which loop is tuned first in cascade?", "The inner slave loop is tuned first, with the master in manual. After it responds well, the master is tuned with the slave in cascade."),
         ("Is cascade control the same as ratio control?", "No. In ratio control one flow setpoint is a fixed ratio of another measured flow. In cascade the setpoint comes from a controller of a different variable.")],
    cal=[],
    glo=[],
    cmp=[],
    tool=[("tools/pid-tuning/pid-simulator", "PID Simulator"), ("tools/pid-tuning/lambda-tuning-calculator", "Lambda Tuning Calculator"), ("tools/practice-tests/control-valve-and-pid-quiz", "Control Valve and PID Quiz")],
    blog=("what-is-cascade-control", "What is cascade control"))

SCENE = r"""
var A,B,ph=0,ts=0,hist=[],pks=0,pkc=0,pt=[],TF=0.3;for(var i=0;i<40;i++)pt.push(Math.random()*300);
function rs(){A={T:50,Fm:50,v:50,I:50};B={T:50,Fm:50,v:50,I1:50,I2:50,Fs:50};}
function sup(p){return p>=2&&p<12?1-P.d/100:1;}
function sim(dt){var s=sup(ph),Kc=1.5,Ti=0.8*P.tau,F,e,es;
F=A.v*s;A.Fm+=(F-A.Fm)*dt/TF;e=50-A.T;A.I+=Kc*e*dt/Ti;A.v=clamp(Kc*e+A.I,0,100);A.T+=(A.Fm-A.T)*dt/P.tau;
F=B.v*s;B.Fm+=(F-B.Fm)*dt/TF;e=50-B.T;B.I1+=Kc*e*dt/Ti;B.Fs=clamp(Kc*e+B.I1,0,100);es=B.Fs-B.Fm;B.I2+=es*dt/TF;B.v=clamp(es+B.I2,0,100);B.T+=(B.Fm-B.T)*dt/P.tau;
ph+=dt;ts+=dt;if(ph>=20)ph-=20;}
function rec(){hist.push([ts,A.T,B.T,sup(ph)]);while(hist.length&&ts-hist[0][0]>20)hist.shift();}
function upd(){rs();ph=0;ts=0;hist=[];pks=0;pkc=0;for(var k=0;k<1000;k++){sim(0.02);pks=Math.max(pks,Math.abs(A.T-50));pkc=Math.max(pkc,Math.abs(B.T-50));if(k%5==4)rec();}
o('loss',m(50*P.d/100,1)+' % of span (50 % × '+m(P.d,0)+' %)');o('ratio',m(P.tau/TF,0)+' times faster');o('pks',m(pks,2)+' % of span');o('pkc',m(pkc,2)+' % of span');}
var acc=0;function step(dt){acc+=dt;while(acc>=0.02){sim(0.02);acc-=0.02;if(Math.round(ts/0.02)%5==0)rec();}var sp=B.Fm*1.6;for(var i=0;i<pt.length;i++){pt[i]+=sp*dt;if(pt[i]>300)pt[i]-=300;}}
function tag(x,y,t,c){ci(x,y,13,'#fff',c||'#1a2333',2);L(t,x,y+1,11,'#1a2333','center',1);}
function draw(){var s=sup(ph),ups=s<1;
L('Temperature and flow in % of span; simulated in real time',20,22,11,'#5b6576','left');
rc(20,80,300,10,'#fde2cf','#b45309');C.fillStyle='#d9622b';for(var i=0;i<pt.length;i++){var x=20+pt[i];if(x>142&&x<158)continue;C.fillRect(x-1.5,83.5,3,3);}
L('Supply '+m(s*100,0)+' %',20,66,11,ups?'#b02a52':'#1a2333','left',1);
C.fillStyle='#475569';C.beginPath();C.moveTo(138,74);C.lineTo(162,96);C.lineTo(162,74);C.lineTo(138,96);C.closePath();C.fill();ln(150,85,150,56,'#475569',3);C.fillStyle='#94a3b8';C.beginPath();C.ellipse(150,56,18,10,0,Math.PI,0);C.fill();rc(132,56,36,4,'#64748b');
L(m(B.v,0)+' % open',150,108,11,'#1a2333','center',1);
ln(240,90,240,96,'#1a2333',2);tag(240,108,'FT');ln(240,121,240,128,'#6b3fb0',1.5,[4,3]);
rc(194,128,96,40,'#1a2333',null,6);L('FIC slave',242,140,11,'#fff','center',1);L('SP '+m(B.Fs,1)+'  PV '+m(B.Fm,1),242,156,11,'#bbf7d0','center');
C.setLineDash([4,3]);C.lineDashOffset=-T*20;C.strokeStyle='#6b3fb0';C.lineWidth=1.5;C.beginPath();C.moveTo(194,148);C.lineTo(184,148);C.lineTo(184,48);C.lineTo(168,48);C.stroke();
C.beginPath();C.moveTo(470,52);C.lineTo(306,52);C.lineTo(306,148);C.lineTo(290,148);C.stroke();C.beginPath();C.moveTo(500,148);C.lineTo(500,76);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L('remote SP',312,62,11,'#6b3fb0','left');
var hot=clamp((B.T-40)/20,0,1);rc(320,70,120,120,'rgb('+Math.round(190+60*hot)+','+Math.round(220-60*hot)+','+Math.round(250-120*hot)+')','#475569',10);
C.strokeStyle='rgba(217,98,43,'+(0.35+B.Fm/100)+')';C.lineWidth=3;C.beginPath();C.moveTo(320,85);for(var k=0;k<6;k++){C.lineTo(430,95+k*14);C.lineTo(332,102+k*14);}C.stroke();
L('Heat exchanger',380,202,11,'#5b6576','center',1);
rc(20,172,300,9,'#bfdbfe');rc(440,172,180,9,'#fecaca');for(var k=0;k<6;k++){var xx=20+((T*40+k*50)%300);rc(xx,174.5,6,4,'#1e63b8');var x2=440+((T*40+k*30)%180);rc(x2,174.5,6,4,'#b02a52');}
L('Product in',24,194,11,'#5b6576','left');L('Product out',616,194,11,'#5b6576','right');
ln(500,160,500,172,'#1a2333',2);tag(500,148,'TT');
rc(470,30,150,46,'#1a2333',null,6);L('TIC master',545,43,11,'#fff','center',1);L('SP 50.0  PV '+m(B.T,2),545,61,11,'#bbf7d0','center');
var x0=70,x1=620,y0=226,y1=340,cy=(y0+y1)/2,sp=Math.max(2,Math.ceil(pks*1.15)),k=(y1-y0)/2/sp;
rc(x0,y0,x1-x0,y1-y0,'#f8fafc','#e2e8f0');
var st=-1;for(var i=0;i<=hist.length;i++){var lo=i<hist.length&&hist[i][3]<1;if(lo&&st<0)st=i;if(!lo&&st>=0){var xa=x1-(ts-hist[st][0])/20*(x1-x0),xb=x1-(ts-hist[i-1][0])/20*(x1-x0);rc(xa,y0,xb-xa,y1-y0,'rgba(176,42,82,0.08)');st=-1;}}
ln(x0,cy,x1,cy,'#94a3b8',1,[4,4]);L('SP',x0-6,cy,11,'#5b6576','right',1);L('+'+sp+' %',x0-6,y0+8,11,'#5b6576','right');L('−'+sp+' %',x0-6,y1-8,11,'#5b6576','right');
[[1,'#b02a52'],[2,'#16a34a']].forEach(function(c){C.strokeStyle=c[1];C.lineWidth=2.2;C.beginPath();hist.forEach(function(h,i){var x=x1-(ts-h[0])/20*(x1-x0),y=cy-(h[c[0]]-50)*k;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();});
L('Temperature error, last 20 s:',x0+8,y0+12,11,'#1a2333','left',1);L('single loop',x0+190,y0+12,11,'#b02a52','left',1);L('cascade',x0+270,y0+12,11,'#16a34a','left',1);L('shaded = supply pressure low',x1-8,y0+12,11,'#b02a52','right');
mk(1,124,58);mk(2,264,104);mk(3,200,124);mk(4,458,40);mk(5,524,140);mk(6,452,84);mk(7,x0+170,y1-14);}
"""
