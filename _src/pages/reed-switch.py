PAGE = dict(
    slug="reed-switch", grp="Switches", name="Reed Switch", kw="How a Reed Switch Works",
    title="How a Reed Switch Works: Animated Diagram and Formula",
    desc="How a reed switch works, animated: a moving magnet magnetises two thin reeds in a glass tube until they snap together, with pull in and drop out distance.",
    h1="How a Reed Switch Works",
    hero="Set the magnet strength, the operate field of the reed and the release ratio. Watch the magnet move in and out, and see the reeds close at one distance and open again at a larger one.",
    quick="A reed switch has two thin ferromagnetic blades sealed in a glass tube with a small gap between their tips. A nearby magnet magnetises the blades with opposite poles at the gap, they attract and touch, and the contact opens again when the magnet moves away.",
    intro=["Reed switches are tiny, sealed contacts operated only by a magnetic field. Because the contacts sit in glass filled with inert gas or vacuum, they do not corrode and can switch millions of times.",
           "They are used in float level switches, cylinder position sensors, door contacts, flow switches and magnetic level gauges. In every case a magnet carried by the moving part works the switch through a non magnetic wall.",
           "A reed switch closes at a higher field than the one at which it opens. This hysteresis keeps the contact from chattering when the magnet hovers near the switching point."],
    sliders=[("b", "Magnet field at 10 mm", 2, 20, 8, 0.5, 1, "mT"), ("bo", "Reed operate field", 0.5, 5, 1.0, 0.1, 1, "mT"), ("rr", "Release to operate ratio", 0.4, 0.9, 0.6, 0.05, 2, "")],
    outs=[("dop", "Operate (pull in) distance"), ("drel", "Release (drop out) distance"), ("hy", "Hysteresis distance"), ("st", "Contact now")],
    legend=["Glass capsule filled with inert gas", "Ferromagnetic reed blades", "Contact gap where the tips overlap", "Permanent magnet moving in and out", "Load circuit with lamp", "Field strength against distance"],
    steps=["With no magnet nearby the two blades are straight and the contact gap is open.",
           "As the magnet approaches, its field passes along the blades and makes them magnetic, with a north pole on one tip and a south pole on the other.",
           "When the field reaches the operate value, the magnetic pull beats the spring force of the blades and the tips snap together.",
           "The closed contact completes the load circuit, so the lamp, relay or PLC input switches on.",
           "As the magnet moves away, the field falls; below the release value the blades spring apart and the circuit opens."],
    formula=["Magnet field (dipole approximation): B(d) = B10 × (10 ÷ d)³, with d in mm",
             "Operate distance = 10 × (B10 ÷ B operate)^(1/3)",
             "Release distance = 10 × (B10 ÷ (ratio × B operate))^(1/3)",
             "Hysteresis distance = release distance − operate distance",
             "Example: B10 8 mT, operate 1.0 mT, ratio 0.6 gives 10 × 8^(1/3) = 20.0 mm to close and 10 × 13.3^(1/3) = 23.7 mm to open"],
    parts=[("Glass capsule", "Hermetically seals the contacts in inert gas or vacuum"),
           ("Reed blades", "Thin nickel iron strips that act as magnetic paths, springs and contacts at the same time"),
           ("Contact plating", "Hard metal layer on the tips that resists wear and keeps contact resistance low"),
           ("Operating magnet", "Permanent magnet or coil that provides the field; its position and orientation set the switching point"),
           ("Housing", "Plastic or metal body that protects the fragile glass and sets the mounting distance")],
    uses=[("Float level switches", "A magnet in the float closes a reed inside the stem at the set level."),
          ("Cylinder position sensing", "A magnet on the piston operates a reed sensor clamped on the outside of the cylinder."),
          ("Magnetic level gauges", "A chain of reed switches along the chamber gives a resistor ladder level signal."),
          ("Door and guard contacts", "A magnet on the door keeps the reed closed while the door is shut.")],
    pros=["No power needed to switch, so it suits simple dry contact inputs", "Sealed contacts work in dust, moisture and many hazardous area designs", "Very low cost and small size"],
    cons=["Limited current and voltage rating; inductive or lamp loads can weld the contacts", "Glass capsule can crack from shock or bending the leads too close", "Stray magnetic fields or nearby steel can shift the switching point"],
    tips=["Use a relay, a contact protection circuit or a PLC input for inductive loads, because a reed contact can weld or wear quickly.",
          "Bend the leads at least a few millimetres away from the glass and support them while bending.",
          "Keep the magnet orientation as designed; a magnet turned across the reed can give two closing points or none.",
          "Check the switching point after replacing a magnet or float, because magnet strength varies between parts."],
    faq=[("Is a reed switch normally open or normally closed?", "Most are normally open and close when the magnet comes near. Changeover types and magnet biased designs give normally closed behaviour."),
         ("What is ampere turns (AT) on a reed switch datasheet?", "It is the sensitivity measured in a standard test coil. A lower AT value means the switch closes with a weaker field."),
         ("Why does the switch open at a different distance from where it closed?", "Once the tips touch, the magnetic gap is closed and less field is needed to hold them. This is the hysteresis between pull in and drop out."),
         ("Can a reed switch go into a PLC input directly?", "Yes, it is a dry contact. Check that the PLC input current is within the reed rating and add a series resistor or suppression if there is a long cable with high capacitance.")],
    cal=[("level/float-buoyancy-calculator", "Float Buoyancy Calculator"), ("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("hysteresis", "Hysteresis"), ("dry-contact", "Dry Contact"), ("magnetic-level-gauge", "Magnetic Level Gauge")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("reed-switch-working-principle", "Reed switch working principle"))

SCENE = r"""
var cl=false,cc=0,d=30,hist=[];
function BF(x){return P.b*Math.pow(10/x,3);}
function dop(){return 10*Math.pow(P.b/P.bo,1/3);}
function drl(){return 10*Math.pow(P.b/(P.rr*P.bo),1/3);}
function upd(){var a=dop(),b=drl();o('dop',m(a,1)+' mm'+(a<13?' (stroke never reaches it)':''));o('drel',m(b,1)+' mm');o('hy',m(b-a,1)+' mm');o('st',(cl?'Closed':'Open')+' at '+m(d,0)+' mm');}
function step(dt){d=30+17*Math.sin(2*Math.PI*T/8);var B=BF(d),w=cl;if(!cl&&B>=P.bo)cl=true;else if(cl&&B<P.rr*P.bo)cl=false;cc=clamp(cc+(cl?dt:-dt)*12,0,1);
o('st',(cl?'Closed':'Open')+' at '+m(d,0)+' mm');hist.push([d,cl]);if(hist.length>400)hist.shift();}
function draw(){var cy=200,ym=cy-3*d,B=BF(d),mg=clamp(B/P.bo,0,1);
L('Gap and blade bending exaggerated; field uses the dipole 1/d³ approximation',20,22,11,'#5b6576','left');
C.save();C.beginPath();C.rect(0,36,470,324);C.clip();C.setLineDash([5,6]);C.lineDashOffset=-T*30;C.lineWidth=1.5;for(var k=1;k<=3;k++){C.strokeStyle='rgba(124,58,237,'+(0.55-k*0.1)+')';C.beginPath();C.ellipse(300,ym,60+k*26,14+k*13,0,0,Math.PI);C.stroke();C.beginPath();C.ellipse(300,ym,60+k*26,14+k*13,0,Math.PI,2*Math.PI);C.stroke();}C.setLineDash([]);C.lineDashOffset=0;C.restore();
rc(240,ym-14,60,28,'#dc2626',null,3);rc(300,ym-14,60,28,'#2563eb',null,3);L('N',270,ym,13,'#fff','center',1);L('S',330,ym,13,'#fff','center',1);
ln(415,ym,415,cy-22,'#1a2333',1,[3,3]);ar(415,cy-26,415,ym+4,'#1a2333',1);L('d = '+m(d,0)+' mm',421,ym-18,11,'#1a2333','left',1);
C.fillStyle='rgba(224,242,254,0.7)';C.strokeStyle='#0369a1';C.lineWidth=1.5;C.beginPath();if(C.roundRect)C.roundRect(170,cy-18,260,36,18);else C.rect(170,cy-18,260,36);C.fill();C.stroke();
var tu=cy-5+cc*4,td=cy+5-cc*4;ln(120,cy-5,230,cy-5,'#475569',3);C.strokeStyle='#475569';C.lineWidth=3;C.beginPath();C.moveTo(230,cy-5);C.quadraticCurveTo(275,cy-5,312,tu);C.stroke();
ln(480,cy+5,370,cy+5,'#475569',3);C.beginPath();C.moveTo(370,cy+5);C.quadraticCurveTo(325,cy+5,288,td);C.stroke();
if(mg>0.25){L('N',306,cy-13,11,'#dc2626','center',1);L('S',294,cy+14,11,'#2563eb','center',1);}
ln(120,cy-5,120,300,'#334155',2);ln(120,300,480,300,'#334155',2);ln(480,300,480,cy+5,'#334155',2);
rc(206,284,6,32,'#334155');rc(218,292,4,16,'#334155');rc(204,296,22,8,'#ffffff');L('24 V DC',214,330,11,'#1a2333','center',1);
ci(400,300,15,cl?'#fde047':'#f1f5f9','#475569',2);ln(390,290,410,310,'#475569',1.5);ln(410,290,390,310,'#475569',1.5);if(cl){for(var k=0;k<8;k++){var a=k*Math.PI/4+T;ln(400+20*Math.cos(a),300+20*Math.sin(a),400+27*Math.cos(a),300+27*Math.sin(a),'#f59e0b',2);}}L('Lamp',400,336,11,'#1a2333','center',1);
if(cl){C.setLineDash([4,10]);C.lineDashOffset=-T*40;C.strokeStyle='#16a34a';C.lineWidth=3;C.beginPath();C.moveTo(120,cy-5);C.lineTo(120,300);C.lineTo(480,300);C.lineTo(480,cy+5);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
var gx0=500,gx1=628,gy0=60,gy1=200,GX=function(x){return gx0+(x-10)/40*(gx1-gx0);},YM=4*P.bo,GY=function(b){return gy1-clamp(b,0,YM)/YM*(gy1-gy0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');L('B (mT)',gx0,gy0-10,11,'#5b6576','left',1);L('10',gx0,gy1+12,11,'#5b6576','center');L('50 mm',gx1,gy1+12,11,'#5b6576','right');
C.strokeStyle='#7c3aed';C.lineWidth=2;C.beginPath();for(var x=10;x<=50;x+=0.5){var y=GY(BF(x));if(x==10)C.moveTo(GX(x),y);else C.lineTo(GX(x),y);}C.stroke();
ln(gx0,GY(P.bo),gx1,GY(P.bo),'#d9622b',1.5,[4,3]);ln(gx0,GY(P.rr*P.bo),gx1,GY(P.rr*P.bo),'#1e63b8',1.5,[4,3]);L('operate',gx0-4,GY(P.bo)-4,11,'#d9622b','right',1);L('release',gx0-4,GY(P.rr*P.bo)+6,11,'#1e63b8','right',1);
ci(GX(d),GY(B),5,cl?'#16a34a':'#475569','#fff',1.5);
rc(500,232,128,62,cl?'#dcfce7':'#f1f5f9',cl?'#16a34a':'#94a3b8',8);L('Contact',564,248,11,'#5b6576','center',1);L(cl?'CLOSED':'OPEN',564,268,14,cl?'#15803d':'#475569','center',1);L('B '+m(B,2)+' mT',564,286,11,'#1a2333','center');
mk(1,440,cy-16);mk(2,170,cy-18);mk(3,300,cy+30);mk(4,232,ym-14);mk(5,428,284);mk(6,gx0+58,gy0-10);}
"""
