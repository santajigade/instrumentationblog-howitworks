PAGE = dict(
    slug="positive-displacement-flow-meter", grp="Flow", name="Positive Displacement Flow Meter", kw="How a Positive Displacement Flow Meter Works",
    title="How a Positive Displacement Flow Meter Works: Animated Diagram",
    desc="How a positive displacement flow meter works, animated: oval gears trap fixed pockets of liquid, a pickup counts pulses and the K factor gives volume.",
    h1="How a Positive Displacement Flow Meter Works",
    hero="Change the flow rate, the volume displaced per revolution and the pulses per revolution. Watch the oval gears carry pockets of liquid from inlet to outlet and see the K factor, pulse frequency and totalizer respond.",
    quick="A positive displacement (PD) flow meter divides the flow into fixed pockets of liquid and counts them. Every revolution of the rotors passes a known volume, so counting revolutions or pulses gives total volume directly, and the pulse rate gives flow rate.",
    intro=["PD meters are the only flow meters that measure volume directly instead of inferring it from velocity. That is why they are widely used for fuel, oil and chemical transfer where the totalized volume matters most.",
           "The pressure drop across the meter turns the rotors, and each turn sweeps a fixed volume from inlet to outlet. Common designs are the oval gear, the nutating disc, the rotary vane, the piston and the helical rotor.",
           "A small amount of liquid slips through the clearances between rotors and housing without being counted. Slip falls as viscosity rises, so PD meters are at their best on oils and other viscous liquids."],
    sliders=[("q", "Flow rate", 5, 100, 40, 1, 0, "L/min"), ("vr", "Volume per revolution Vr", 10, 100, 50, 5, 0, "mL"), ("ppr", "Pulses per revolution", 1, 8, 4, 1, 0, "")],
    outs=[("n", "Rotor speed = Q ÷ Vr"), ("k", "K factor = pulses per revolution ÷ Vr"), ("f", "Pulse frequency = K × Q"), ("tot", "Totalizer = pulses counted ÷ K")],
    legend=["Inlet: liquid pushes on the rotors", "Measuring chamber in the housing", "Oval gear rotors", "Trapped pocket of fixed volume", "Magnet and pulse pickup", "Pulse train to the totalizer", "Outlet"],
    steps=["Liquid enters the meter and the pressure difference between inlet and outlet pushes on the oval gears.",
           "The meshed gears turn in opposite directions, and each gear closes off a pocket of liquid between itself and the housing wall.",
           "The pocket is carried around the outside of the gear and released at the outlet; one revolution of the pair moves four pockets.",
           "A magnet in a gear passes a pickup sensor, giving a fixed number of pulses for each revolution.",
           "The totalizer divides the pulse count by the K factor to show volume, and the pulse rate divided by K gives flow rate."],
    formula=["Rotor speed N = Q ÷ Vr, where Vr is the volume moved per revolution",
             "K factor = pulses per revolution ÷ Vr (pulses per litre)",
             "Pulse frequency f = K × Q, with Q in litres per second",
             "Volume = pulse count ÷ K; for an oval gear meter one pocket = Vr ÷ 4",
             "Example: Q 40 L/min, Vr 50 mL, 4 pulses per revolution: N = 40 ÷ 0.05 = 800 rpm (13.33 rev/s), K = 4 ÷ 0.05 = 80 pulses per litre, f = 80 × 40 ÷ 60 = 53.33 Hz, one pocket = 12.5 mL"],
    parts=[("Housing and measuring chamber", "Precision machined body that forms the pockets with the rotors"),
           ("Rotors", "Oval gears, disc, vanes, pistons or helical screws that sweep a fixed volume"),
           ("Magnet and pickup", "Hall effect or reed sensor that gives pulses as the rotor turns"),
           ("Register or transmitter", "Counts pulses, applies the K factor and gives total and rate outputs"),
           ("Strainer", "Fitted upstream to keep solids out of the tight clearances")],
    uses=[("Fuel and oil transfer", "Diesel, furnace oil and lube oil dispensing and loading with a local totalizer."),
          ("Custody transfer", "Volume for billing of petroleum products, with meter proving and a meter factor."),
          ("Batching and dosing", "Fixed volumes of resins, additives and chemicals delivered to a batch."),
          ("Hydraulic and process oils", "Viscous liquids where velocity meters struggle.")],
    pros=["Measures volume directly and needs no straight pipe run", "Accuracy improves with viscosity, ideal for oils", "Works without external power when a mechanical register is used"],
    cons=["Moving parts wear and can jam if solids enter, so a strainer is needed", "Pressure drop rises with flow and viscosity", "Low viscosity liquids such as water give more slip and lower accuracy"],
    tips=["Always fit a strainer upstream and clean it on a schedule; a blocked strainer looks like a flow drop.",
          "Flush the line before installing a new meter so weld slag and debris do not reach the rotors.",
          "Prove the meter on the actual liquid and enter a meter factor, because slip depends on viscosity.",
          "Use an air eliminator where the line can carry gas, since the meter counts gas pockets as liquid."],
    faq=[("Why is a positive displacement flow meter more accurate on viscous liquids?", "Thick liquid seals the small clearances between rotors and housing, so less liquid slips past uncounted. On thin liquids slip is larger, especially at low flow."),
         ("What is the K factor of a PD meter?", "It is the number of pulses per unit volume, for example pulses per litre. The totalizer divides counted pulses by K to get volume."),
         ("Does a PD meter need straight pipe runs?", "No. It traps and counts fixed volumes, so the flow profile upstream has almost no effect on the reading."),
         ("What happens if gas enters a PD meter?", "Gas fills the pockets just like liquid and is counted as volume, so the meter reads high. An air eliminator upstream removes the gas.")],
    cal=[("flow/k-factor-calculator", "K Factor Calculator"), ("flow/meter-factor-calculator", "Meter Factor Calculator"), ("flow/flow-totalizer-calculator", "Flow Totalizer Calculator"), ("instrumentation-signal/pulse-output-scaling-calculator", "Pulse Output Scaling Calculator")],
    glo=[("k-factor", "K Factor"), ("meter-factor", "Meter Factor"), ("flow-totalizer", "Flow Totalizer")],
    cmp=[("turbine-vs-positive-displacement-flow-meter", "Turbine vs Positive Displacement Flow Meter")],
    tool=[],
    blog=("positive-displacement-flow-meter", "Positive displacement flow meter"))

SCENE = r"""
var th=0,cnt=0,lp=-1,pt=[],CX=300,YC=150,D=35,A=44,B=26,RC=47,fl=0;
function rr(){return P.q/60/(P.vr/1000);}
function kf(){return P.ppr/(P.vr/1000);}
function upd(){var r=rr();o('n',m(r*60,0)+' rpm ('+m(r,2)+' rev/s)');o('k',m(kf(),1)+' pulses per L');o('f',m(kf()*P.q/60,2)+' Hz');o('tot',m(cnt/kf(),2)+' L');}
function step(dt){var r=rr(),vs=0.9*r/(r+15);th+=vs*2*Math.PI*dt;cnt+=kf()*P.q/60*dt;var ph=Math.floor(th/(2*Math.PI)*P.ppr);if(ph!=lp){if(lp>=0){pt.push(T);fl=0.12;}lp=ph;}fl=Math.max(0,fl-dt);while(pt.length&&T-pt[0]>5)pt.shift();upd();}
function gear(cx,cy,an,col){C.fillStyle=col;C.strokeStyle='#334155';C.lineWidth=1.5;C.beginPath();for(var k=0;k<=240;k++){var u=k/240*2*Math.PI,r=A*B/Math.sqrt(Math.pow(B*Math.cos(u),2)+Math.pow(A*Math.sin(u),2))-2+1.5*Math.cos(u*20),x=cx+r*Math.cos(u+an),y=cy+r*Math.sin(u+an);if(!k)C.moveTo(x,y);else C.lineTo(x,y);}C.closePath();C.fill();C.stroke();ci(cx,cy,5,'#1a2333');}
function draw(){var y1=YC-D,y2=YC+D,ex=Math.sqrt(RC*RC-D*D);
L('Rotation slowed down for viewing; one pair revolution moves 4 pockets',20,22,11,'#5b6576','left');
pipe(40,CX-ex+2,YC,14);pipe(CX+ex-2,600,YC,14);
var sp=20+P.q*1.2;for(var k=0;k<6;k++){var u=((T*sp+k*36)%(CX-ex-50));ci(48+u,YC+(k%2?5:-5),3,'#3b82f6');ci(CX+ex+4+u*(600-CX-ex-8)/(CX-ex-50),YC+(k%2?-5:5),3,'#3b82f6');}
ar(70,YC-34,120,YC-34,'#1e63b8',2);L('Inlet',95,YC-46,11,'#1e63b8','center',1);ar(500,YC-34,550,YC-34,'#1e63b8',2);L('Outlet',525,YC-46,11,'#1e63b8','center',1);
ci(CX,y1,RC+10,'#9aa5b8');ci(CX,y2,RC+10,'#9aa5b8');rc(CX-ex-4,YC-14,8,28,'#e6f0fd');rc(CX+ex-4,YC-14,8,28,'#e6f0fd');ci(CX,y1,RC,'#bfdbfe');ci(CX,y2,RC,'#bfdbfe');rc(CX-ex,YC-14,2*ex,28,'#bfdbfe');
var s=Math.cos(th);if(Math.abs(s)>0.8){C.fillStyle='rgba(30,99,184,0.45)';C.beginPath();C.arc(CX,y1,RC,Math.PI,2*Math.PI);C.closePath();C.fill();}
if(Math.abs(s)<0.6){C.fillStyle='rgba(30,99,184,0.45)';C.beginPath();C.arc(CX,y2,RC,0,Math.PI);C.closePath();C.fill();}
gear(CX,y1,th,'#e2e8f0');gear(CX,y2,Math.PI/2-th,'#cbd5e1');
var mx=CX+30*Math.cos(th),my=y1+30*Math.sin(th);ci(mx,my,4,'#dc2626','#fff',1);
rc(CX-12,y1-RC-34,24,18,fl>0?'#fde047':'#1a2333',null,4);L('PU',CX,y1-RC-25,10,fl>0?'#1a2333':'#fff','center',1);ln(CX,y1-RC-16,CX,y1-RC-10,'#475569',2);
ln(CX+12,y1-RC-25,420,y1-RC-25,'#475569',1.5);ln(420,y1-RC-25,420,250,'#475569',1.5,[4,3]);
var x0=40,x1=400,yb=320,yt=290,X=function(t){return x1-(T-t)/5*(x1-x0);};rc(x0,262,x1-x0,76,'#f6f8fc','#dde3ee',6);L('Pickup pulses (last 5 s, slowed)',x0+6,274,11,'#5b6576','left',1);
C.strokeStyle='#7c3aed';C.lineWidth=2;C.beginPath();C.moveTo(x0+2,yb);pt.forEach(function(t){var x=X(t);if(x>x0+2){C.lineTo(x,yb);C.lineTo(x,yt);C.lineTo(x+4,yt);C.lineTo(x+4,yb);}});C.lineTo(x1-2,yb);C.stroke();
rc(420,250,200,88,'#1a2333',null,8);L('Totalizer',520,266,11,'#cbd5e1','center',1);L(m(cnt/kf(),2)+' L',520,292,18,'#fbbf24','center',1);L('K '+m(kf(),1)+' p/L, '+m(P.q,0)+' L/min',520,320,11,'#fff','center');
mk(1,40,YC-30);mk(2,CX-RC-22,y2+24);mk(3,CX+RC+22,y1+10);mk(4,CX-RC+8,y1-RC+10);mk(5,CX+28,y1-RC-25);mk(6,x0+14,300);mk(7,600,YC-30);}
"""
