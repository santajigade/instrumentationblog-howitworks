PAGE = dict(
    slug="limit-switch", grp="Switches", name="Limit Switch", kw="How a Limit Switch Works",
    title="How a Limit Switch Works: Animated Diagram and Coast Formula",
    desc="How a limit switch works, animated: a cam on a moving carriage lifts the roller lever, snap action contacts change over and the drive coasts to a stop.",
    h1="How a Limit Switch Works",
    hero="Set the carriage speed, the length of the cam and the braking time of the drive. Watch the roller ride onto the cam, the contacts snap over and the carriage coast to a stop, either safely on the cam or past it.",
    quick="A limit switch is a mechanical switch operated by physical contact. A cam or dog on a moving part pushes the actuator lever, and a snap action mechanism changes the contacts over so the normally open contact closes and the normally closed contact opens.",
    intro=["A limit switch tells a control system that a moving part has reached a position. It is used on conveyors, cranes, lifts, machine tools, gates and valve actuators wherever a definite end of travel must be confirmed.",
           "The switch has three main sections: an actuator such as a roller lever or plunger, a head that converts that movement, and a contact block with snap action contacts. The snap mechanism makes the contacts change over quickly at one point, no matter how slowly the lever moves.",
           "Picking the switch is only half the job. The cam must be long enough to hold the lever while the drive brakes, otherwise the carriage coasts past the cam and the switch releases again."],
    sliders=[("v", "Carriage speed", 50, 500, 200, 10, 0, "mm/s"), ("L", "Cam (dog) length", 20, 200, 60, 5, 0, "mm"),
             ("ts", "Braking time to standstill", 20, 400, 150, 10, 0, "ms")],
    outs=[("dw", "Time the lever is held at full speed (L ÷ v)"), ("co", "Coast after trip (v × t ÷ 2)"), ("rs", "Result"), ("cnt", "Cycles in the demo")],
    legend=["Roller lever actuator", "Snap action contacts NC and NO", "Cam (dog) on the carriage", "Moving carriage on its rail", "PLC input wired to the NO contact", "Expected coast distance on the cam"],
    steps=["The carriage moves towards the end of its travel with the cam fixed on top of it.",
           "The cam ramp lifts the roller, rotating the lever and pushing the switch mechanism.",
           "At the operating point the snap action contacts change over: NO closes and NC opens, giving a clean signal.",
           "The PLC or relay sees the NO contact close and removes the run command, so the drive brakes.",
           "The carriage coasts to a stop with the roller still on the cam; when it reverses, the lever returns and the contacts reset at the release point."],
    formula=["Coast distance after trip ≈ v × t ÷ 2 for a steady deceleration from speed v in braking time t",
             "Lever hold time when the cam passes at full speed = L ÷ v",
             "Safe stop needs coast distance less than the cam length L, with margin",
             "Add v × reaction time for the PLC scan and contactor delay before braking starts",
             "Example: v 200 mm/s, t 150 ms, L 60 mm: coast = 200 × 0.15 ÷ 2 = 15 mm, hold time = 60 ÷ 200 = 0.30 s, spare = 45 mm"],
    parts=[("Actuator", "Roller lever, adjustable rod, plunger or wobble stick that the moving part touches"),
           ("Head", "Converts lever rotation into plunger movement and sets the operating and release points"),
           ("Snap action contact block", "Changes over the NO and NC contacts quickly at one point with a spring mechanism"),
           ("Cam or dog", "Shaped piece on the moving part that pushes the actuator and holds it during overtravel"),
           ("Body and cable entry", "Sealed housing that protects the contacts from dust, oil and water")],
    uses=[("Conveyor and transfer cars", "Stops a car or carriage at the end of its travel."),
          ("Cranes and hoists", "Confirms the upper and lower hook limits and the long travel ends."),
          ("Machine tool axes", "Gives end of travel and home position signals for slides and tables."),
          ("Valve and damper position", "Confirms the open and closed positions of manual and actuated valves.")],
    pros=["Simple, rugged and easy to understand in the field", "Contacts switch real load current, often without an interposing relay", "Works on any material and is not affected by colour, dust or light"],
    cons=["Moving parts and contacts wear over many cycles", "Needs physical contact, so the cam and lever must be aligned", "Slower and less precise than proximity sensors for fast or frequent switching"],
    tips=["Make the cam long enough to hold the lever through the full coast distance, including the reaction time of the PLC and contactor.",
          "Use the NC contact for safety and stopping functions so a broken wire stops the machine instead of hiding the limit.",
          "Set the cam so it does not push the lever past its maximum overtravel; check the lever angle at the final stop position.",
          "Lock the lever on its shaft and mark the position; a slipping lever is a common cause of missed limits."],
    faq=[("What is the difference between NO and NC contacts in a limit switch?", "The NO contact is open at rest and closes when the switch operates. The NC contact is closed at rest and opens when the switch operates."),
         ("What are pretravel and overtravel?", "Pretravel is the lever movement from rest to the operating point. Overtravel is the extra movement allowed after the operating point before the lever hits its mechanical stop."),
         ("Why do limit switches use snap action?", "A spring mechanism makes the contacts change over quickly at one point. This avoids slow, arcing contact movement and gives a clean on off signal even if the lever moves slowly."),
         ("Why does the switch release again after the machine stops?", "If the cam is shorter than the coast distance, the roller rides off the end of the cam. Make the cam longer or reduce speed before the limit.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("dry-contact", "Dry Contact")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("what-is-a-limit-switch", "What is a limit switch"))

SCENE = r"""
var S=1,SL=2,RX=420,ST=270,lead=ST,spd=0,st=0,tm=0,op=false,lift=0,cyc=0,ovr=0,hist=[];
function dpx(){return clamp(P.L*S,15,200);}
function hgt(x){var d=dpx(),r=Math.min(8,d/3),a=lead-d;if(x>lead||x<a)return 0;if(x>lead-r)return 18*(lead-x)/r;if(x<a+r)return 18*(x-a)/r;return 18;}
function coast(){return P.v*P.ts/1000/2;}
function upd(){var c=coast();o('dw',m(P.L/P.v*1000,0)+' ms');o('co',m(c,1)+' mm');o('rs',c<P.L?'Stops on the cam, '+m(P.L-c,1)+' mm to spare':'Overruns the cam: switch releases');o('cnt',cyc+' cycles, '+ovr+' overruns');}
function step(dt){var vv=P.v*S/SL;
if(st==0){spd=vv;}else if(st==1){spd-=vv/(P.ts/1000*SL)*dt;if(spd<=0){spd=0;st=2;tm=0;cyc++;if(!op)ovr++;upd();}}
else if(st==2){tm+=dt;if(tm>1.2)st=3;}else if(st==3){spd=-vv*1.5;if(lead<=ST){lead=ST;spd=0;st=4;tm=0;}}else{tm+=dt;if(tm>0.8)st=0;}
lead+=spd*dt;lift=Math.max(0,hgt(RX)-10);if(!op&&lift>=5)op=true;else if(op&&lift<=2)op=false;
if(st==0&&op)st=1;
hist.push([T,lead,op]);while(hist.length&&T-hist[0][0]>10)hist.shift();}
function draw(){var d=dpx(),cl=lead-d-40,cr=lead+12,cy=196-lift,cpx=coast()*S;
L('Motion shown 2 times slower; cam and coast drawn to scale',20,22,11,'#5b6576','left');
ln(20,252,620,252,'#475569',3);for(var x=30;x<620;x+=24)ln(x,254,x-8,262,'#94a3b8',1);
rc(cl,214,cr-cl,34,'#1e63b8',null,6);L('Carriage',cl+28,231,11,'#fff','left',1);ci(cl+16,250,6,'#1a2333');ci(cr-16,250,6,'#1a2333');
var r=Math.min(8,d/3);C.fillStyle='#64748b';C.beginPath();C.moveTo(lead-d,214);C.lineTo(lead-d+r,196);C.lineTo(lead-r,196);C.lineTo(lead,214);C.closePath();C.fill();
if(cpx>0){var e=lead-Math.min(cpx,d);rc(e,206,lead-e,8,'rgba(217,98,43,0.75)');if(cpx>d)rc(lead-cpx,206,cpx-d,8,'rgba(185,28,28,0.75)');}
rc(300,50,120,90,'#f8fafc','#475569',8);L('Limit switch',360,62,11,'#5b6576','center',1);
ci(330,82,4,'#1a2333');ci(396,82,4,'#1a2333');ci(330,116,4,'#1a2333');ci(396,116,4,'#1a2333');L('NC',322,82,11,'#1a2333','right',1);L('NO',322,116,11,'#1a2333','right',1);
var by=op?111:87;ln(334,by,392,by,op?'#16a34a':'#d9622b',5);ln(363,by,363,140,'#475569',2);
ln(363,140,378,152,'#475569',3);ci(378,152,5,'#1a2333');ln(378,152,RX,cy,'#334155',5);ci(RX,cy,8,'#e2e8f0','#1a2333',2);
var a=-lead/8;ln(RX,cy,RX+7*Math.cos(a),cy+7*Math.sin(a),'#1a2333',1.5);
ln(400,116,470,116,op?'#16a34a':'#94a3b8',2.5);ln(400,82,440,82,'#94a3b8',2);ln(440,82,440,40,'#94a3b8',2);L('to safety circuit',446,40,11,'#5b6576','left');
rc(470,60,150,110,'#1a2333',null,8);L('PLC input',545,76,11,'#cbd5e1','center',1);ci(496,116,10,op?'#22c55e':'#334155','#94a3b8');L('I0.2 = '+(op?1:0),514,116,12,'#fff','left',1);
var sts=['Run forward','Braking','Stopped','Returning','Waiting'][st];L('Drive: '+sts,545,150,11,op?'#bbf7d0':'#fde68a','center',1);
var x0=70,x1=620,ya=298,yb=326;L('Position',x0-6,ya,11,'#5b6576','right');L('I0.2',x0-6,yb+8,11,'#5b6576','right');
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(h,i){var x=x1-(T-h[0])/10*(x1-x0),y=ya+14-(h[1]-ST)/240*28;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
C.strokeStyle='#16a34a';C.beginPath();hist.forEach(function(h,i){var x=x1-(T-h[0])/10*(x1-x0),y=h[2]?yb:yb+16;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
L('last 10 s',x1,350,11,'#5b6576','right');
mk(1,RX+22,cy-24);mk(2,420,50);mk(3,lead-d-14,200);mk(4,cl+14,231);mk(5,606,60);mk(6,lead+24,204);}
"""
