PAGE = dict(
    slug="flow-switch", grp="Switches", name="Paddle Flow Switch", kw="How a Paddle Flow Switch Works",
    title="How a Paddle Flow Switch Works: Animated Diagram and Formula",
    desc="How a paddle flow switch works, animated: water drag swings the paddle against a spring and the contact makes when the flow passes the set velocity.",
    h1="How a Paddle Flow Switch Works",
    hero="Set the pump flow, the pipe inside diameter and the switching velocity. Watch the pump start and stop, the paddle swing with the water drag and the contact make on rising flow and drop out on falling flow.",
    quick="A paddle flow switch hangs a thin paddle across the pipe. Flowing liquid pushes the paddle with a drag force that grows with the square of velocity, and when that force beats the range spring the lever trips a microswitch.",
    intro=["A paddle flow switch tells you whether liquid is flowing in a pipe, not how much. It is used to prove flow for pumps, chillers, boilers and cooling water lines, and to stop equipment when the flow is lost.",
           "The paddle is mounted on a lever that passes through a flexible seal or bellows into the switch head. A range spring holds the paddle upright, and the spring setting decides the velocity at which the switch operates.",
           "Drag on the paddle depends on the liquid velocity, not directly on the volume flow. So the same switch setting gives a different flow in a different pipe size, which is why manufacturers give switching tables for each pipe diameter."],
    sliders=[("q", "Pump flow when running", 5, 40, 20, 1, 0, "m³/h"), ("d", "Pipe inside diameter", 50, 150, 80, 5, 0, "mm"), ("vs", "Set velocity (contact makes)", 0.3, 2, 0.8, 0.05, 2, "m/s")],
    outs=[("v", "Velocity at pump flow, v = Q ÷ A"), ("f", "Drag on paddle, F = ½ ρ v² Cd A p (A p = 0.0015 m²)"), ("qs", "Flow at switch point, rising and falling"), ("st", "Contact now")],
    legend=["Pump starting and stopping", "Pipe with flowing water", "Paddle swung by the drag force", "Range spring and lever through the seal", "Microswitch in the switch head", "PLC input: flow proven", "Trend: flow, switch points and contact"],
    steps=["With no flow the range spring holds the paddle upright across the pipe and the microswitch is in its no flow position.",
           "When the pump starts, the liquid pushes on the paddle with a drag force that rises with the square of the velocity.",
           "The paddle swings downstream and the lever moves through the flexible seal against the range spring.",
           "When the velocity passes the set value, the lever trips the microswitch and the PLC sees flow proven.",
           "When the flow falls, the spring pushes the paddle back and the contact drops out at a lower velocity than it made, which gives a deadband."],
    formula=["Velocity: v = Q ÷ A, with A = π × D² ÷ 4",
             "Drag on the paddle: F = ½ × ρ × v² × Cd × A p, with Cd about 1.2 for a flat plate across the flow",
             "The contact makes at the set velocity v s, so the flow at the switch point is Q s = v s × A",
             "The reset on falling flow is lower; this demo uses 80 % of the set velocity, real values come from the switching table",
             "Example: Q 20 m³/h in D 80 mm: A = 0.005027 m², v = (20 ÷ 3600) ÷ 0.005027 = 1.105 m/s; F = 0.5 × 1000 × 1.105² × 1.2 × 0.0015 = 1.10 N; v s 0.8 m/s gives Q s = 0.8 × 0.005027 × 3600 = 14.48 m³/h, reset at 11.58 m³/h"],
    parts=[("Paddle", "Thin stainless steel blade, often trimmed to suit the pipe size"),
           ("Lever and seal", "Carries the paddle movement through a bellows or diaphragm seal into the dry head"),
           ("Range spring", "Holds the paddle against the flow and sets the switching velocity"),
           ("Microswitch", "Snap acting contact with C, NC and NO terminals"),
           ("Switch head", "Enclosure with the adjustment screw, terminals and cable entry")],
    uses=[("Pump protection", "Stops a pump or raises an alarm when the flow is lost, before the pump runs dry or overheats."),
          ("Chiller and boiler flow proving", "Permits the compressor or burner only when water is flowing through the heat exchanger."),
          ("Cooling water lines", "Alarms on loss of cooling water to bearings, seals or furnaces."),
          ("Fire and sprinkler systems", "Signals water flow when a sprinkler head opens.")],
    pros=["Simple, rugged and low cost", "Needs no power for the sensing part and gives a direct contact", "Easy to understand and to test by stopping the flow"],
    cons=["Moving parts in the flow that can wear, clog or break", "Switch point depends on pipe size and paddle length", "Not suitable for dirty, fibrous or very viscous liquids that build up on the paddle"],
    tips=["Install it with at least five pipe diameters of straight pipe on each side so a disturbed flow profile does not cause chatter.",
          "Trim the paddle to the length given for the pipe size so it does not touch the far wall.",
          "Check the arrow on the body; a paddle mounted against the flow direction will not switch correctly.",
          "Use a time delay in the PLC on pump start so the flow has time to build up before the low flow trip is armed."],
    faq=[("Does a paddle flow switch measure flow rate?", "No. It only says whether the flow is above or below its switching point. To know the actual flow you need a flow meter."),
         ("Why do switching flows depend on pipe size?", "The paddle responds to velocity, and the same flow gives a lower velocity in a larger pipe. Switching tables list the flow on and flow off values for each diameter and paddle length."),
         ("Can I mount a paddle flow switch in a vertical pipe?", "Many models allow it with upward flow, but the paddle weight shifts the switching point. Follow the mounting and adjustment notes of the switch."),
         ("What is the difference between a paddle and a thermal flow switch?", "A paddle switch uses a moving blade pushed by the flow. A thermal switch has no moving parts and senses the cooling of a heated tip by the flowing medium.")],
    cal=[("flow/pipe-flow-velocity-calculator", "Pipe Flow Velocity Calculator"), ("flow/reynolds-number-calculator", "Reynolds Number Calculator")],
    glo=[("velocity-profile", "Velocity Profile"), ("volumetric-flow-rate", "Volumetric Flow Rate")],
    cmp=[],
    tool=[("tools/practice-tests/flow-measurement-quiz", "Flow Measurement Quiz")],
    blog=("flow-switch-working-principle-paddle-dp-thermal", "Flow switch working principle"))

SCENE = r"""
var cy=4,PER=16,TON=9,q=0,sw=false,hist=[],pre=0,pts=[];for(var i=0;i<40;i++)pts.push([Math.random(),Math.random()]);
function AR(){return Math.PI*Math.pow(P.d/1000,2)/4;}
function qs(){return P.vs*AR()*3600;}
function upd(){if(!pre){pre=1;for(var k=0;k<500;k++){T+=0.04;step(0.04);}}var a=AR(),v=P.q/3600/a;o('v',m(v,3)+' m/s');o('f',m(0.5*1000*v*v*1.2*0.0015,2)+' N');
o('qs',m(qs(),2)+' m³/h on, '+m(qs()*0.8,2)+' m³/h off'+(P.q<qs()?' (pump flow too low, never switches)':''));o('st',sw?'Flow proven, contact made':'No flow, contact open');}
function pon(){return cy<TON;}
function step(dt){cy+=dt;if(cy>=PER)cy-=PER;q+=((pon()?P.q:0)-q)*Math.min(1,dt/1.2);var v=q/3600/AR(),w=sw;if(!sw&&v>=P.vs)sw=true;else if(sw&&v<0.8*P.vs)sw=false;if(w!==sw)upd();
hist.push([T,q,sw]);while(hist.length&&T-hist[0][0]>20)hist.shift();}
function draw(){var v=q/3600/AR(),vr=v/P.vs,th=clamp(0.42*vr*vr,0,1)*0.6,on=pon();
L('Pump cycle sped up; paddle swing exaggerated',20,22,11,'#5b6576','left');
ci(46,140,26,'#e2e8f0','#334155',2);var ra=T*(on?10:0)+0.0;for(var k=0;k<4;k++){var a=ra+k*1.571;ln(46,140,46+18*Math.cos(a),140+18*Math.sin(a),'#475569',3);}ci(46,140,5,'#334155');
L('Pump',46,180,11,'#1a2333','center',1);L(on?'Running':'Stopped',46,194,11,on?'#16a34a':'#b91c1c','center',1);
pipe(72,440,140,30);L('D '+m(P.d,0)+' mm',120,86,11,'#5b6576','center',1);
var sp=v*60;pts.forEach(function(p){var y=112+56*p[1],prof=1-Math.pow((y-140)/30,2)*0.6;var x=74+((p[0]*366+T*sp*prof*2)%366);ci(x,y,2.6,'#1e63b8');});
rc(362,114,66,40,'rgba(255,255,255,0.9)',null,6);ar(370,144,420,144,'#1e63b8',2.5);L(m(v,2)+' m/s',395,126,11,'#1e63b8','center',1);
rc(232,96,36,14,'#94a3b8','#334155',2);rc(214,40,72,56,'#cbd5e1','#334155',6);L('Head',232,50,11,'#1a2333','left',1);
var px=250,py=104,len=54,ex=px+len*Math.sin(th),ey=py+len*Math.cos(th);ln(px,py,ex,ey,'#475569',3);
C.save();C.translate(ex,ey);C.rotate(-th);rc(-3,-18,6,22,'#64748b','#1e293b',2);C.restore();ci(px,py,4,'#1a2333');
if(v>0.02){ar(ex-34,ey-6,ex-6,ey-6,'#1e63b8',2);L('drag',ex-36,ey+6,11,'#1e63b8','right',1);}
var lx=px-22*Math.sin(th),ly=py-22*Math.cos(th);ln(px,py,lx,ly,'#475569',3);
C.strokeStyle='#0f7b80';C.lineWidth=2;C.beginPath();var s0=lx,s1=218;for(var k=0;k<=8;k++){var x=s0+(s1-s0)*k/8,y=ly+(k%2?4:-4);if(k==0||k==8)y=ly;if(k)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
rc(256,56,26,30,'#1a2333',null,4);var cnt=sw?62:76;ln(262,66,276,cnt,'#fbbf24',2.5);ci(262,66,2.5,'#fde68a');ci(276,62,2.5,sw?'#22c55e':'#94a3b8');ci(276,76,2.5,sw?'#94a3b8':'#22c55e');ln(lx,ly,256,ly,'#475569',1.5);
ln(286,58,460,58,sw?'#16a34a':'#94a3b8',2.5);
rc(460,40,170,124,'#1a2333',null,8);L('PLC input FSL',545,54,11,'#cbd5e1','center',1);ci(486,88,12,sw?'#22c55e':'#334155','#94a3b8',2);if(!sw&&on){var g=0.5+0.5*Math.sin(T*8);ci(486,88,16+3*g,null,'rgba(251,191,36,0.7)',2);}
L(sw?'Flow proven':'No flow',506,88,13,'#fff','left',1);L('Q now '+m(q,1)+' m³/h',545,120,11,'#cbd5e1','center');L('on '+m(qs(),1)+', off '+m(qs()*0.8,1),545,142,11,'#fde68a','center',1);
var gx0=70,gx1=620,gy0=236,gy1=322,top=Math.max(P.q,qs())*1.2,TY=function(x){return gy1-x/top*(gy1-gy0);},TX=function(t){return gx1-(T-t)/20*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');ln(gx0,TY(qs()),gx1,TY(qs()),'#16a34a',1,[4,4]);ln(gx0,TY(qs()*0.8),gx1,TY(qs()*0.8),'#b91c1c',1,[4,4]);

C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=TY(p[1]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
C.strokeStyle='#0f7b80';C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=p[2]?gy1+12:gy1+24;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
rc(gx0+30,TY(qs())-16,92,13,'rgba(248,250,252,0.92)');L('flow on '+m(qs(),1),gx0+32,TY(qs())-9,11,'#16a34a','left',1);rc(gx0+30,TY(qs()*0.8)+3,92,13,'rgba(248,250,252,0.92)');L('flow off '+m(qs()*0.8,1),gx0+32,TY(qs()*0.8)+10,11,'#b91c1c','left',1);L('Flow, m³/h',gx0,gy0-10,11,'#1e63b8','left',1);L('last 20 s',gx1,gy0-10,11,'#5b6576','right');L('Contact',gx0-4,gy1+18,11,'#0f7b80','right',1);L(m(top,0),gx0-4,gy0+4,11,'#5b6576','right');L('0',gx0-4,gy1,11,'#5b6576','right');
mk(1,20,116);mk(2,150,140);mk(3,ex+20,ey-4);mk(4,200,ly);mk(5,296,84);mk(6,616,54);mk(7,gx0+14,gy0+14);}
"""
