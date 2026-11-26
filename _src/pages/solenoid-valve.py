PAGE = dict(
    slug="solenoid-valve", grp="Control Valve", name="Solenoid Valve", kw="How a Solenoid Valve Works",
    title="How a Solenoid Valve Works: Animated Diagram and Formula",
    desc="How a solenoid valve works, animated: the energised coil lifts the plunger off the orifice, liquid flows, and the spring closes it again when power is removed.",
    h1="How a Solenoid Valve Works",
    hero="Change the valve flow coefficient Kv, the pressure drop across the valve and the orifice diameter. The coil switches on and off every 3 seconds so you can watch the plunger lift, the flow start and the spring close the valve.",
    quick="A solenoid valve is an on off valve moved by an electromagnet. When current flows in the coil, the magnetic field pulls an iron plunger up and opens the orifice; when the coil is switched off, a spring pushes the plunger back onto the seat and the valve closes.",
    intro=["Solenoid valves are the most common electrically operated valves in plants and machines. They switch water, air, oil and gas on or off, and they pilot larger pneumatic actuators on process valves.",
           "In a direct acting valve the coil force alone lifts the plunger against the spring and the line pressure. The pressure force grows with the orifice area, so direct acting valves are limited to small orifices or low pressures.",
           "Larger valves are pilot operated and use the line pressure itself to open a diaphragm or piston. The valve shown here is a direct acting 2 way normally closed type, the simplest form to understand."],
    sliders=[("kv", "Flow coefficient Kv", 0.2, 5, 1.5, 0.1, 1, "m³/h"), ("dp", "Pressure drop across the valve ΔP", 0.5, 10, 4, 0.1, 1, "bar"), ("d", "Orifice diameter", 1, 6, 3, 0.1, 1, "mm")],
    outs=[("q", "Water flow when open Q = Kv √ΔP"), ("cv", "Equivalent Cv = 1.156 × Kv"), ("f", "Pressure force on the closed seat"), ("st", "Valve state")],
    legend=["Coil (electromagnet)", "Plunger (iron armature)", "Return spring", "Seal and orifice", "Inlet port", "Outlet port", "Fixed core (plunger stop)"],
    steps=["With the coil off, the return spring and the inlet pressure hold the plunger seal down on the orifice, so the valve is closed.",
           "When the control system energises the coil, current produces a magnetic field concentrated in the fixed core and plunger.",
           "The magnetic force pulls the plunger up toward the fixed core, against the spring and the pressure force on the seal.",
           "The orifice opens and liquid flows from the inlet chamber, up through the orifice and out of the outlet port.",
           "When the coil is switched off the field collapses, the spring pushes the plunger back down and the flow stops."],
    formula=["Q = Kv × √(ΔP ÷ SG), Q in m³/h and ΔP in bar (SG = 1 for water)",
             "Cv = 1.156 × Kv (Cv in US gallons per minute at 1 psi)",
             "Pressure force on the seat F = ΔP × π d² ÷ 4",
             "The coil must give a force greater than F plus the spring force, which sets the maximum operating pressure differential",
             "Example: Kv 1.5 and ΔP 4 bar give Q = 1.5 × √4 = 3.0 m³/h of water; a 3 mm orifice at 4 bar carries 2.83 N of pressure force"],
    parts=[("Coil", "Copper winding that creates the magnetic field when energised, rated for a voltage such as 24 V DC or 230 V AC"),
           ("Plunger", "Movable iron armature with a soft seal on its tip that opens and closes the orifice"),
           ("Fixed core and tube", "Guides the plunger and completes the magnetic circuit; AC valves add a shading ring here to stop hum"),
           ("Return spring", "Pushes the plunger onto the seat so the valve closes when power is lost"),
           ("Valve body and orifice", "Holds the inlet, outlet and seat; the orifice size sets the Kv and the pressure force")],
    uses=[("Water and air lines", "On off control of cooling water, compressed air and washdown supplies."),
          ("Pneumatic actuators", "3 way and 5 way solenoid valves pilot air to process valve actuators."),
          ("Emergency shutdown", "De energise to trip solenoids that vent the actuator and drive an ESD valve to its safe position."),
          ("Dosing and burners", "Fuel gas and chemical dosing lines where a fast, fail closed valve is needed.")],
    pros=["Fast opening and closing, usually in a fraction of a second", "Simple to control directly from a PLC or relay output", "Normally closed types fail closed on loss of power"],
    cons=["Only on off service, not throttling control", "Direct acting types are limited to small orifices or low pressure differentials", "Coils get hot when energised for long periods and can burn out at wrong voltage"],
    tips=["Check that the coil voltage and type (AC or DC) on the nameplate match the supply before energising.",
          "Pilot operated valves need a minimum pressure differential to open; if a valve will not open at low pressure, check this value on the datasheet.",
          "Install a strainer upstream, because dirt on the seat is the most common cause of a valve that leaks or will not close.",
          "To test a coil, hold a steel screwdriver near the coil when energised to feel the field, then measure the coil resistance with power isolated."],
    faq=[("What does normally closed mean?", "The valve is closed when the coil is not energised. It opens only while power is applied, so it closes on a power failure."),
         ("What is the difference between direct acting and pilot operated?", "In a direct acting valve the coil lifts the main plunger itself. In a pilot operated valve the coil opens a small pilot hole and the line pressure then moves a diaphragm or piston to open the main orifice."),
         ("Why does an AC solenoid valve hum?", "The AC magnetic force falls to zero twice each cycle and the plunger vibrates. A shading ring on the core keeps some force during those zeros; a worn or missing ring causes loud hum."),
         ("How is a solenoid valve sized?", "Find the required flow and the available pressure drop, then use Q = Kv √(ΔP ÷ SG) to find the Kv. Check that the maximum pressure differential of the valve is above the highest line pressure.")],
    cal=[("control-valve/cv-calculator-liquid", "Cv Calculator for Liquids"), ("control-valve/valve-pressure-drop-calculator", "Valve Pressure Drop Calculator")],
    glo=[("fail-safe-position", "Fail Safe Position"), ("interposing-relay", "Interposing Relay"), ("valve-actuator", "Valve Actuator")],
    cmp=[],
    tool=[("tools/troubleshooting/esd-valve-fault-finder", "ESD Valve Fault Finder")],
    dl=("downloads/templates/solenoid-valve-datasheet", "Solenoid Valve Datasheet Template"),
    blog=("solenoid-valve-working-principle", "Solenoid valve working principle"))

SCENE = r"""
var lf=0,en=false,hist=[];
function q(){return P.kv*Math.sqrt(P.dp);}
function fs(){return P.dp*1e5*Math.PI*Math.pow(P.d/1000,2)/4;}
function upd(){o('q',m(q(),2)+' m³/h');o('cv',m(1.156*P.kv,2));o('f',m(fs(),2)+' N');o('st',en?(lf>0.9?'Coil on: open, flowing':'Coil on: plunger lifting'):(lf<0.1?'Coil off: closed':'Coil off: spring closing'));}
function step(dt){var e=(T%6)<3;if(e!==en){en=e;upd();}var pl=lf;lf+=((en?1:0)-lf)*Math.min(1,dt*9);if((pl<0.9)!==(lf<0.9)||(pl<0.1)!==(lf<0.1))upd();
hist.push([T,en?1:0,lf]);while(hist.length&&T-hist[0][0]>12)hist.shift();}
function dots(pts,off,col){var acc=0;for(var i=0;i<pts.length-1;i++){var a=pts[i],b=pts[i+1],l=Math.hypot(b[0]-a[0],b[1]-a[1]);for(var s=((off-acc)%20+20)%20;s<l;s+=20){ci(a[0]+(b[0]-a[0])*s/l,a[1]+(b[1]-a[1])*s/l,2.8,col);}acc+=l;}}
function draw(){var lift=12*lf,pt=128-lift,pb=240-lift,open=lf>0.15;
L('Coil switched on and off every 3 s for the demo',20,22,11,'#5b6576','left');
pipe(20,182,270,14);pipe(338,630,270,14);
rc(180,200,160,110,'#9aa5b8','#475569',6);rc(190,252,68,48,'#e6f0fd');rc(196,212,134,28,'#e6f0fd');rc(268,212,62,88,'#e6f0fd');
rc(190,240,36,12,'#9aa5b8');rc(244,240,24,12,'#9aa5b8');rc(258,252,10,48,'#9aa5b8');rc(182,256,10,28,'#e6f0fd');rc(328,256,12,28,'#e6f0fd');
if(open){var sp=T*(30+q()*14);dots([[20,270],[225,270],[235,262],[235,236],[300,226],[300,270],[630,270]],sp,'#1e63b8');}
else{for(var k=0;k<7;k++)ci(30+k*25+3*Math.sin(T*3+k),270,2.8,'#1e63b8');for(var k=0;k<5;k++)ci(198+k*12,262+16*((k*7)%3)/2+2*Math.sin(T*3+k),2.8,'#1e63b8');}
ln(219,84,219,212,'#475569',1.5);ln(251,84,251,212,'#475569',1.5);
var cc=en?'#d97706':'#b45309';rc(186,100,32,82,cc,'#78350f',3);rc(252,100,32,82,cc,'#78350f',3);
C.strokeStyle='rgba(255,255,255,0.45)';C.lineWidth=1;for(var y=106;y<180;y+=8){C.beginPath();C.moveTo(188,y);C.lineTo(216,y);C.moveTo(254,y);C.lineTo(282,y);C.stroke();}
rc(222,84,26,28,'#475569','#1e293b',3);
C.strokeStyle='#1a2333';C.lineWidth=1.8;C.beginPath();C.moveTo(235,112);var n=6,hh=(pt-112)/n;for(var k=0;k<n;k++)C.lineTo(235+(k%2?-8:8),112+hh*(k+0.5));C.lineTo(235,pt);C.stroke();
rc(222,pt,26,pb-pt,'#64748b','#1e293b',3);rc(222,pb-4,26,4,'#111827');
if(en){var g=0.35+0.3*Math.sin(T*8);C.strokeStyle='rgba(30,99,184,'+g+')';C.lineWidth=1.5;C.setLineDash([5,5]);C.lineDashOffset=-T*20;C.beginPath();C.ellipse(235,141,70,56,0,0,Math.PI*2);C.stroke();C.beginPath();C.ellipse(235,141,88,70,0,0,Math.PI*2);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
rc(40,96,100,70,'#1a2333',null,8);L('24 V DC',90,112,12,'#cbd5e1','center',1);ln(60,140,78,140,'#cbd5e1',2);ln(102,140,120,140,'#cbd5e1',2);if(en)ln(78,140,102,140,'#4ade80',2.5);else ln(78,140,99,128,'#fda4af',2.5);L(en?'ON':'OFF',90,156,11,en?'#4ade80':'#fda4af','center',1);
ln(140,120,186,120,'#334155',2);ln(140,160,186,160,'#334155',2);
L('Inlet',90,236,11,'#1a2333','center',1);L('Outlet',480,236,11,'#1a2333','center',1);L('ΔP '+m(P.dp,1)+' bar',480,312,11,'#1a2333','center',1);
rc(380,36,245,190,'#1a2333',null,8);L(en?'Coil energised':'Coil de energised',392,54,12,en?'#4ade80':'#fda4af','left',1);
L('Plunger lift '+m(lf*100,0)+' %',392,74,11,'#cbd5e1','left');L('Flow now '+m(open?q()*sm((lf-0.15)/0.85):0,2)+' m³/h',392,92,11,'#fbbf24','left',1);L('Seat force '+m(fs(),2)+' N when closed',392,110,11,'#cbd5e1','left');
var gx0=400,gx1=612,TX=function(t){return gx1-(T-t)/12*(gx1-gx0);};L('Coil',gx0,132,11,'#cbd5e1','left',1);L('Lift',gx0,178,11,'#cbd5e1','left',1);
C.lineWidth=2;C.strokeStyle='#4ade80';C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=160-p[1]*16;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
C.strokeStyle='#fbbf24';C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=212-p[2]*24;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();L('last 12 s',gx1,132,11,'#94a3b8','right');
mk(1,202,141);mk(2,235,196);ln(254,pt-6,289,118,'#d9622b',1.2);mk(3,300,118);mk(4,207,226);mk(5,60,312);mk(6,600,312);ln(248,96,289,90,'#d9622b',1.2);mk(7,300,88);}
"""
