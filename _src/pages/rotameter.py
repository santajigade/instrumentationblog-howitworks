PAGE = dict(
    slug="rotameter", grp="Flow", name="Rotameter (Variable Area Flow Meter)", kw="How a Rotameter Works",
    title="How a Rotameter Works: Animated Diagram and Density Correction",
    desc="How a rotameter works, animated: the float rises in a tapered tube until drag and buoyancy balance its weight. See how liquid density shifts the reading.",
    h1="How a Rotameter Works",
    hero="Change the actual flow and watch the float rise until the forces on it balance. Then change the liquid density to see how far a water calibrated scale reads off.",
    quick="A rotameter is a vertical tapered tube with a float inside. Flow from below lifts the float until the gap around it is wide enough for the drag and buoyancy to balance the float weight, and the float position on the scale shows the flow rate.",
    intro=["The rotameter is the simplest flow meter in most plants: no power, no electronics, and the reading is visible at a glance. It is also called a variable area flow meter, because the flow area around the float changes with flow.",
           "At any steady flow the float sits where its weight equals buoyancy plus the drag of the fluid squeezing through the annular gap. More flow needs a bigger gap, and the taper gives that gap higher up the tube.",
           "Because the balance depends on the fluid, a scale made for water reads wrong on a lighter or heavier liquid. The correction is simple once you know the float and fluid densities."],
    sliders=[("q", "Actual flow through the meter", 0, 1000, 600, 10, 0, "L/h"), ("rho", "Liquid density", 700, 1300, 850, 10, 0, "kg/m³")],
    outs=[("cf", "Density correction factor"), ("ind", "Scale reading (scale made for water)"), ("pos", "Float height on the scale"), ("er", "Error if the reading is not corrected")],
    legend=["Tapered tube, narrow at the bottom", "Float, read at its widest top edge", "Annular gap where the flow passes", "Scale made for water, 0 to 1000 L/h", "Forces on the float: weight, buoyancy, drag", "Inlet at the bottom, outlet at the top"],
    steps=["Fluid enters at the bottom of a vertical tube that widens toward the top.",
           "The flow pushes up on the float through drag, and the fluid also gives a small buoyancy force.",
           "The float rises, the annular gap around it grows, and the velocity through the gap falls.",
           "The float stops where weight equals buoyancy plus drag; this height is a direct measure of flow.",
           "The reading is taken at the float edge marked by the maker, usually the widest part, against the scale on the tube."],
    formula=["Q = Cd × Aa × √(2 g Vf (ρf − ρ) ÷ (Af ρ)), where Aa is the annular area around the float",
             "At balance: weight of float = buoyancy + drag",
             "In a linear taper the annular area grows almost linearly with height, so the scale is close to linear",
             "Density correction: Q actual = Q read × √((ρf − ρ) × ρcal ÷ ((ρf − ρcal) × ρ))",
             "Example: stainless float 8000 kg/m³, water scale 1000 kg/m³, liquid 850 kg/m³: factor = √(7150 × 1000 ÷ (7000 × 850)) = 1.096, so an actual 600 L/h reads 547 L/h"],
    parts=[("Tapered tube", "Glass or plastic for direct reading, or metal with a magnetic follower for higher pressure"),
           ("Float", "Stainless steel, aluminium or plastic; its shape sets how much viscosity affects the reading"),
           ("Scale", "Printed or etched on the tube, made for one fluid, density and, for gases, pressure and temperature"),
           ("Float stops", "Keep the float inside the measuring range at zero and maximum flow"),
           ("End fittings", "Connect the tube to the process at the bottom inlet and top outlet")],
    uses=[("Purge flows", "Setting the air or nitrogen purge on bubbler level systems and instrument housings."),
          ("Analyser sample lines", "Checking sample and bypass flow to gas and liquid analysers."),
          ("Cooling and seal water", "Local indication of water to pump seals, bearings and coolers."),
          ("Chemical dosing", "Visual check of small dosing and laboratory flows.")],
    pros=["No power supply needed and the reading is visible at once", "Low cost with a nearly constant pressure drop", "Good for small flows of clean liquids and gases"],
    cons=["Must be mounted vertical with flow upward", "Reading depends on fluid density and viscosity, and on pressure and temperature for gases", "Glass tubes have limited pressure and temperature ratings and do not suit opaque fluids"],
    tips=["Install the meter truly vertical; a tilted tube lets the float rub on the wall and read wrong.",
          "Read the float at the edge the maker specifies, and keep your eye level with it to avoid parallax.",
          "If the fluid differs from the scale fluid, apply the density correction or order a scale made for the real fluid.",
          "For gases, put the needle valve where the maker states and read at the stated pressure, or the reading will be off."],
    faq=[("Why is the pressure drop across a rotameter almost constant?", "At balance the pressure difference across the float supports the float weight minus buoyancy. That force does not change with flow, so the pressure drop stays roughly the same over the whole range."),
         ("Why must a rotameter be vertical?", "The measurement relies on gravity pulling the float down against the flow. In a tilted or horizontal tube the balance changes and the float rubs on the wall."),
         ("Can a water rotameter be used for another liquid?", "Yes, if you correct the reading for density using the float and liquid densities, and the viscosity is close to that of water. For very different fluids, ask for a dedicated scale."),
         ("What is the difference between glass and metal tube rotameters?", "Glass tubes let you see the float directly but have low pressure and temperature limits. Metal tubes use a magnet in the float and an outside follower, which allows higher pressure and opaque fluids and can add a transmitter.")],
    cal=[("flow/rotameter-correction-calculator", "Rotameter Correction Calculator"), ("flow/flow-meter-accuracy-calculator", "Flow Meter Accuracy Calculator")],
    glo=[("rotameter", "Rotameter"), ("turndown-ratio", "Turndown Ratio")],
    cmp=[],
    tool=[("tools/practice-tests/flow-measurement-quiz", "Flow Measurement Quiz")],
    blog=("variable-area-flow-meter-working", "Variable area flow meter working"))

SCENE = r"""
var RF=8000,RC=1000,pts=[],yf=300;for(var i=0;i<46;i++)pts.push([Math.random(),Math.random()]);
function cf(){return Math.sqrt((RF-P.rho)*RC/((RF-RC)*P.rho));}
function ind(){return P.q/cf();}
function hw(y){return 14+20*(320-y)/264;}
function yS(v){return 300-224*v/1000;}
function upd(){var c=cf(),r=ind();o('cf',m(c,3));o('ind',r>1000?'Over range (above 1000 L/h)':m(r,0)+' L/h');o('pos',m(Math.min(r,1000)/10,1)+' % of scale');o('er',m((1/c-1)*100,1)+' %');}
function step(dt){var tg=yS(Math.min(ind(),1000))+(P.q>0?1.5*Math.sin(T*5):0);yf+=(tg-yf)*Math.min(1,dt*3);}
function draw(){var r=ind(),ov=r>1000,fy=yf,sp=P.q/1000;
L('Float bobbing and particle speed exaggerated',20,22,11,'#5b6576','left');
pipe(300,630,40,8);pipe(40,300,335,8);
for(var k=0;k<14;k++){if(P.q<=0)break;var x=40+((T*120*sp+k*20)%260);ci(x,335,2.6,'#1e63b8');var x2=320+((T*120*sp+k*24)%310);ci(x2,40,2.6,'#1e63b8');}
C.fillStyle='rgba(224,242,254,0.9)';C.beginPath();C.moveTo(300-hw(320),320);C.lineTo(300-hw(56),56);C.lineTo(300+hw(56),56);C.lineTo(300+hw(320),320);C.closePath();C.fill();
C.strokeStyle='#475569';C.lineWidth=2.5;C.beginPath();C.moveTo(300-hw(320),320);C.lineTo(300-hw(56),56);C.moveTo(300+hw(320),320);C.lineTo(300+hw(56),56);C.stroke();
rc(262,44,76,14,'#64748b',null,3);rc(272,318,56,14,'#64748b',null,3);
if(P.q>0){for(var i=0;i<pts.length;i++){var q=pts[i],y=320-264*((q[1]+T*0.35*sp)%1),h=hw(y),x;if(y>fy-2&&y<fy+30){var g=h-13;x=300+(q[0]<0.5?-1:1)*(13+g*(0.2+0.6*((q[0]*2)%1)));}else x=300+(2*q[0]-1)*h*0.85;ci(x,y,2.2,'#1e63b8');}}
for(var v=0;v<=1000;v+=100){var y=yS(v),xl=300-hw(y);ln(xl-(v%200?5:10),y,xl,y,'#334155',1.5);if(v%200==0)L(String(v),xl-14,y,11,'#1a2333','right',v==0||v==1000?1:0);}
L('L/h',300-hw(56)-14,62,11,'#5b6576','right',1);
C.fillStyle='#94a3b8';C.strokeStyle='#334155';C.lineWidth=1.5;C.beginPath();C.moveTo(287,fy+8);C.lineTo(313,fy+8);C.lineTo(300,fy+32);C.closePath();C.fill();C.stroke();
rc(287,fy,26,8,'#cbd5e1','#334155',2);for(var k=0;k<3;k++){var sx=287+((T*30*sp+k*9)%26);ln(sx,fy+1,sx+3,fy+7,'#334155',1.2);}
ln(212,fy,286,fy,'#d9622b',1.2,[4,3]);L('Read at top edge',208,fy,11,'#d9622b','right',1);L((ov?'Over range':m(r,0)+' L/h'),208,fy+16,12,'#1a2333','right',1);
if(ov)L('Float at top stop',300,72,11,'#b91c1c','center',1);
rc(380,80,250,164,'#f8fafc','#cbd5e1',8);L('Forces on the float',392,96,12,'#1a2333','left',1);
var Wl=44,Bl=Wl*P.rho/RF,Dl=P.q>0?Wl-Bl:0;
rc(472,160,56,10,'#cbd5e1','#334155',2);C.fillStyle='#94a3b8';C.beginPath();C.moveTo(476,170);C.lineTo(524,170);C.lineTo(500,198);C.closePath();C.fill();C.stroke();
ar(500,198,500,198+Wl,'#dc2626',2.5);L('Weight ρf V g',508,228,11,'#dc2626','left',1);
if(Dl>0){ar(484,160,484,160-Dl,'#16a34a',2.5);L('Drag',478,134,11,'#16a34a','right',1);}else L('Resting on bottom stop',440,124,11,'#5b6576','center',1);
ar(516,160,516,160-Math.max(Bl,8),'#1e63b8',2.5);L('Buoyancy ρ V g',524,150,11,'#1e63b8','left',1);
L('At balance:',392,196,11,'#1a2333','left',1);L('W = B + D',392,214,11,'#1a2333','left',0);
rc(380,252,250,90,'#1a2333',null,8);L('Scale: water, 1000 kg/m³',392,268,11,'#cbd5e1','left',1);L('Float: stainless, 8000 kg/m³',392,288,11,'#cbd5e1','left',1);
L('Liquid now: '+m(P.rho,0)+' kg/m³',392,308,11,'#fde68a','left',1);L('Reads '+(ov?'over range':m(r,0)+' L/h')+', actual '+m(P.q,0)+' L/h',392,328,11,'#4ade80','left',1);
L('Flow in',70,306,11,'#1e63b8','left',1);L('Flow out',626,70,11,'#1e63b8','right',1);
var m1=fy>150?90:290;mk(1,346,m1);mk(2,350,fy+26);mk(3,350,fy-16);ln(339,fy-12,300+13+(hw(fy)-13)/2+2,fy+2,'#d9622b',1.2);mk(4,236,282);mk(5,618,92);mk(6,30,335);}
"""
