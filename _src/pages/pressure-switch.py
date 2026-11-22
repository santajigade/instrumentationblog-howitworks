PAGE = dict(
    slug="pressure-switch", grp="Switches", name="Pressure Switch", kw="How a Pressure Switch Works",
    title="How a Pressure Switch Works: Animated Diagram and Formula",
    desc="How a pressure switch works, animated: the diaphragm pushes against the range spring, the contact snaps at the set point and resets after the deadband.",
    h1="How a Pressure Switch Works",
    hero="Set the cut out pressure and the deadband of the switch. Watch the compressor charge the receiver, the contact snap over at the set point and the compressor restart only when the pressure has fallen by the deadband.",
    quick="A pressure switch lets the process pressure act on a diaphragm, piston or bellows that pushes against an adjustable range spring. When the pressure force beats the spring force, a snap acting microswitch changes over, and it changes back only after the pressure has fallen by the deadband.",
    intro=["A pressure switch is a point device: it does not give a continuous signal, it only tells you that the pressure is above or below a set value. It is used for compressor and pump control, low pressure alarms, high pressure trips and permissives in interlocks.",
           "Inside, the pressure acts on a sensing element with a known area, so it produces a force. A range spring holds that force back, and turning the adjusting screw changes the spring preload and with it the set point.",
           "Every pressure switch has a deadband, the difference between the switching point on rising pressure and the reset point on falling pressure. The deadband stops the contact from chattering when the pressure hovers near the set point."],
    sliders=[("sp", "Set point (cut out, rising)", 3, 9, 6, 0.1, 1, "bar"), ("db", "Deadband", 0.3, 2, 1, 0.1, 1, "bar")],
    outs=[("f", "Spring force at set point, F = P × A (A = 2 cm²)"), ("ci", "Reset point (cut in, falling)"), ("dp", "Deadband as % of the 10 bar range"), ("st", "Contact now")],
    legend=["Compressor driven through the NC contact", "Air receiver", "Impulse line to the switch", "Diaphragm: pressure force P × A", "Range spring and set point screw", "Snap acting microswitch C, NC, NO", "Motor starter and contact state", "Trend: pressure, set and reset points"],
    steps=["The process pressure reaches the diaphragm through the impulse line and pushes it up with a force equal to pressure times area.",
           "The range spring pushes down; its preload, set with the adjusting screw, decides the pressure at which the forces balance.",
           "When the rising pressure passes the set point, the pushrod trips the snap acting microswitch, so the common terminal moves from NC to NO.",
           "In this demo the NC contact opens and drops the compressor starter, so the compressor stops and the air users start to lower the pressure.",
           "The contact snaps back only when the pressure has fallen below the set point minus the deadband, so the compressor restarts at the reset point."],
    formula=["Switch point: P set = F spring ÷ A, where the diaphragm force P × A just equals the spring force",
             "Reset point on falling pressure: P reset = P set − deadband",
             "Deadband in % of range = deadband ÷ range × 100",
             "A larger diaphragm area gives more force per bar, so the switch can be set more finely at low pressures",
             "Example: A = 2 cm² = 0.0002 m², P set 6 bar = 600 000 Pa: F = 600 000 × 0.0002 = 120 N; deadband 1 bar: reset = 6 − 1 = 5 bar, which is 10 % of a 10 bar range"],
    parts=[("Sensing element", "Diaphragm, piston or bellows that turns the pressure into a force"),
           ("Range spring", "Holds back the pressure force; its preload sets the switching point"),
           ("Adjusting screw", "Changes the spring preload to move the set point within the range"),
           ("Snap acting microswitch", "Changes over quickly with C, NC and NO terminals so the contact does not arc slowly"),
           ("Deadband adjustment", "On adjustable models, a second spring or screw that sets the gap between switch and reset points")],
    uses=[("Compressor control", "Stops the compressor at the cut out pressure and restarts it at the cut in pressure."),
          ("Pump protection", "Low suction or low discharge pressure trip to stop a pump running dry or against a closed line."),
          ("Lube oil permissive", "Proves oil pressure before a large motor or turbine is allowed to start."),
          ("Low pressure alarm", "Warns the operator when instrument air or a utility header drops.")],
    pros=["Simple, robust and needs no power supply for the sensing part", "Direct contact output that can switch a starter or a PLC input", "Low cost compared with a transmitter and trip amplifier"],
    cons=["Gives only on off information, no trend of the actual pressure", "Set point can drift with spring fatigue and must be checked on a test bench", "A fixed deadband may be too wide or too narrow for the application"],
    tips=["Choose a range so the set point sits between about 30 % and 70 % of the switch range; the set point is more stable there.",
          "Remember the set point is usually adjusted on rising pressure; check the datasheet to know whether the deadband is added above or below it.",
          "For a low pressure alarm wire the contact so it opens on alarm; a broken wire then gives an alarm instead of hiding one.",
          "Fit a snubber or a pulsation damper on pump discharge service so pressure spikes do not make the contact chatter."],
    faq=[("What is the deadband of a pressure switch?", "It is the difference between the pressure at which the contact switches on rising pressure and the pressure at which it resets on falling pressure. It stops the contact chattering near the set point."),
         ("Should I use the NO or NC contact?", "It depends on what must happen on failure. For alarms and trips use the contact that opens on the abnormal condition, so a broken wire or a loose terminal also gives the safe result."),
         ("How do I calibrate a pressure switch?", "Connect it to a pressure source with a reference gauge, raise the pressure slowly and note where the contact changes, then lower it and note the reset point. Adjust the range screw and repeat until both points are within tolerance."),
         ("Is a pressure switch the same as a pressure transmitter?", "No. A transmitter gives a continuous 4 to 20 mA or digital value over the whole range, while a switch only changes a contact at one pressure.")],
    cal=[("pressure/pressure-force-calculator", "Pressure Force Calculator"), ("pressure/pressure-gauge-range-selector", "Pressure Gauge Range Selector")],
    glo=[("pressure-switch-deadband", "Pressure Switch Deadband"), ("hysteresis", "Hysteresis"), ("set-pressure", "Set Pressure")],
    cmp=[],
    tool=[("tools/practice-tests/pressure-measurement-quiz", "Pressure Measurement Quiz")],
    blog=("what-is-a-pressure-switch", "What is a pressure switch"))

SCENE = r"""
var p=4.5,mot=true,hist=[],pre=0,ang=0,dots=[];for(var i=0;i<60;i++)dots.push([Math.random(),Math.random(),Math.random()*6.28]);
function rs(){return Math.max(0,P.sp-P.db);}
function upd(){if(!pre){pre=1;for(var q=0;q<500;q++){T+=0.04;step(0.04);}}o('f',m(P.sp*1e5*2e-4,0)+' N');o('ci',m(rs(),1)+' bar');o('dp',m(P.db/10*100,0)+' %');o('st',mot?'Below set point: C to NC closed, compressor running':'Tripped: C to NO, compressor stopped');}
function step(dt){p+=(mot?0.9:-0.6)*dt;p=clamp(p,0,10);var w=mot;if(mot&&p>=P.sp)mot=false;else if(!mot&&p<=rs())mot=true;if(w!==mot)upd();ang+=mot?dt*12:0;
hist.push([T,p]);while(hist.length&&T-hist[0][0]>20)hist.shift();}
function draw(){
L('Pressure cycle sped up; diaphragm movement exaggerated',20,22,11,'#5b6576','left');
ci(64,250,30,'#e2e8f0','#334155',2);for(var k=0;k<3;k++){var a=ang+k*2.094;ln(64,250,64+22*Math.cos(a),250+22*Math.sin(a),'#475569',4);}ci(64,250,6,'#334155');
L('Compressor',64,294,11,'#1a2333','center',1);L(mot?'Running':'Stopped',64,308,11,mot?'#16a34a':'#b91c1c','center',1);
ln(94,250,140,250,'#64748b',6);if(mot){C.setLineDash([5,8]);C.lineDashOffset=-T*40;ln(94,250,140,250,'#bfdbfe',2,[5,8]);C.setLineDash([]);C.lineDashOffset=0;}
rc(140,110,100,190,'#e2e8f0','#475569',30);var den=Math.round(p*6);for(var i=0;i<den;i++){var d=dots[i],x=152+76*((d[0]+0.03*Math.sin(T*3+d[2]))%1),y=132+150*((d[1]+0.03*Math.cos(T*2.6+d[2]))%1);ci(x,y,2.4,'#1e63b8');}
rc(152,192,76,40,'rgba(255,255,255,0.92)','#94a3b8',6);L('Receiver',190,204,12,'#1a2333','center',1);L(m(p,2)+' bar',190,221,12,'#1e63b8','center',1);
ln(240,280,282,280,'#64748b',5);C.setLineDash([4,8]);C.lineDashOffset=-T*20;ln(240,280,282,280,'#bfdbfe',2,[4,8]);C.setLineDash([]);C.lineDashOffset=0;ar(270,294,286,294,'#1e63b8',2);L('To air users',244,308,11,'#1e63b8','left',1);
ln(190,110,190,92,'#475569',3);ci(190,72,20,'#fff','#334155',2);var ga=Math.PI*0.75+p/10*Math.PI*1.5;ln(190,72,190+15*Math.cos(ga),72+15*Math.sin(ga),'#b91c1c',2);ci(190,72,3,'#334155');L('0 to 10 bar',190,42,11,'#5b6576','center');
ln(232,130,268,130,'#475569',3);ln(268,130,268,214,'#475569',3);ln(268,214,312,214,'#475569',3);
rc(290,36,190,196,'#f8fafc','#cbd5e1',8);L('Switch close up',298,48,11,'#5b6576','left',1);
var dfl=p/10*8;rc(312,206,150,18,'rgba(147,197,253,0.6)','#334155',3);L('P',326,215,11,'#1e63b8','center',1);
C.strokeStyle='#1a2333';C.lineWidth=3;C.beginPath();C.moveTo(332,206);C.quadraticCurveTo(387,206-2*dfl,442,206);C.stroke();
var top=196-dfl;ar(370,214,370,top+4,'#1e63b8',2);ar(404,214,404,top+4,'#1e63b8',2);
rc(382,top-50,10,50,'#64748b','#334155',2);rc(362,top-56,50,6,'#334155');
var sy0=74,sy1=top-56;C.strokeStyle='#0f7b80';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=12;k++){var y=sy0+(sy1-sy0)*k/12,x=387+(k%2?14:-14);if(k==0||k==12)x=387;if(k)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
rc(362,66,50,8,'#334155');rc(381,54,12,12,'#a8620a','#4a2a04',2);L('Set screw',412,60,11,'#a8620a','left',1);
rc(418,96,56,62,'#1a2333',null,6);L('C',430,108,11,'#fde68a','center',1);L('NC',448,108,11,'#cbd5e1','center',1);L('NO',448,146,11,'#cbd5e1','center',1);
var ty=mot?118:136;ci(430,127,3,'#fde68a');ln(430,127,462,ty,'#fbbf24',3);ci(462,118,3,mot?'#22c55e':'#94a3b8');ci(462,136,3,mot?'#94a3b8':'#22c55e');
ln(392,top-30,418,top-30,'#475569',2);
rc(496,40,134,124,'#1a2333',null,8);L('Motor starter',563,54,11,'#cbd5e1','center',1);ci(520,84,12,mot?'#22c55e':'#334155','#94a3b8',2);if(!mot){var g=0.5+0.5*Math.sin(T*8);ci(520,84,16+3*g,null,'rgba(251,113,133,0.7)',2);}
L(mot?'Running':'Stopped',540,84,12,'#fff','left',1);L('Cut out '+m(P.sp,1)+' bar',563,116,11,'#fde68a','center',1);L('Cut in '+m(rs(),1)+' bar',563,136,11,'#bfdbfe','center',1);L('Now '+m(p,2)+' bar',563,154,11,'#cbd5e1','center');
var gx0=330,gx1=620,gy0=254,gy1=334,TY=function(v){return gy1-v/10*(gy1-gy0);},TX=function(t){return gx1-(T-t)/20*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');ln(gx0,TY(P.sp),gx1,TY(P.sp),'#b91c1c',1,[4,4]);ln(gx0,TY(rs()),gx1,TY(rs()),'#16a34a',1,[4,4]);
L('set '+m(P.sp,1),gx1-4,TY(P.sp)-8,11,'#b91c1c','right');L('reset '+m(rs(),1),gx1-4,TY(rs())+9,11,'#16a34a','right');
L('10',gx0-4,gy0,11,'#5b6576','right');L('0',gx0-4,gy1,11,'#5b6576','right');
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(q,i){var x=TX(q[0]),y=TY(q[1]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
L('Pressure, bar',gx0,gy0-10,11,'#1e63b8','left',1);L('last 20 s',gx1,gy0-10,11,'#5b6576','right');
mk(1,30,214);mk(2,150,126);mk(3,268,172);mk(4,452,196);mk(5,346,120);mk(6,474,90);mk(7,616,164);mk(8,gx0+16,gy1-14);}
"""
