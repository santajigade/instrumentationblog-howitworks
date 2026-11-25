PAGE = dict(
    slug="strain-gauge-pressure-sensor", grp="Pressure", name="Strain Gauge Pressure Sensor", kw="How a Strain Gauge Pressure Sensor Works",
    title="How a Strain Gauge Pressure Sensor Works: Diagram and Formula",
    desc="How a strain gauge pressure sensor works, animated: pressure bends a diaphragm, four gauges change resistance and a Wheatstone bridge gives a millivolt signal.",
    h1="How a Strain Gauge Pressure Sensor Works",
    hero="Change the pressure and watch the diaphragm bend, the gauge resistances shift and the bridge output rise. Then change the excitation and the rated output to see how the millivolt signal scales.",
    quick="A strain gauge pressure sensor has a thin metal diaphragm with strain gauges bonded to it. Pressure bends the diaphragm, the gauges stretch or compress, and a Wheatstone bridge turns their tiny resistance change into a millivolt signal proportional to pressure.",
    intro=["Most electronic pressure sensors start with the same idea: convert pressure into a small mechanical strain, then measure that strain electrically. The strain gauge diaphragm is the classic way to do it and is still used in a huge range of transmitters and transducers.",
           "The resistance change of a single gauge is very small, well under one percent at full pressure. Four gauges in a Wheatstone bridge, two stretched and two compressed, add their effects and cancel most of the temperature drift.",
           "Understanding the bridge explains the numbers on a data sheet such as 2 mV/V rated output and 10 V excitation. It also explains common field faults like zero drift, noisy readings and errors from long cables."],
    sliders=[("p", "Process pressure (sensor range 0 to 10 bar)", 0, 10, 6, 0.1, 1, "bar"), ("vx", "Bridge excitation Vex", 2, 10, 10, 0.5, 1, "V"), ("ro", "Rated output at full scale", 1, 3, 2, 0.1, 1, "mV/V")],
    outs=[("e", "Strain on each gauge, ±ε (gauge factor 2.0)"), ("dr", "Change in each 350 Ω gauge, ΔR = R × GF × ε"), ("v", "Bridge output Vout = Vex × GF × ε"), ("ma", "Transmitter output, 4 to 20 mA")],
    legend=["Process pressure on the diaphragm", "Metal diaphragm, bending exaggerated", "Centre gauges R1 and R3 in tension", "Edge gauges R2 and R4 in compression", "Wheatstone bridge with excitation Vex", "Signal conditioner and 4 to 20 mA output"],
    steps=["Process pressure acts on one side of a thin metal diaphragm, and the other side is open to atmosphere or sealed.",
           "The diaphragm bends; on its dry surface the centre is stretched and the area near the clamped edge is compressed.",
           "Foil or thin film strain gauges bonded at those spots change resistance in proportion to the strain.",
           "The four gauges form a Wheatstone bridge; opposite arms change the same way, so the output adds up while equal temperature changes cancel.",
           "The electronics amplify the millivolt bridge output, correct zero and span, and send a 4 to 20 mA or digital signal."],
    formula=["Vout = Vex × GF × ε, for a full bridge with two gauges in tension and two in compression",
             "ΔR ÷ R = GF × ε, with a gauge factor GF of about 2 for metal foil gauges",
             "ε = (rated output ÷ GF) × P ÷ P full scale",
             "Output current = 4 + 16 × P ÷ P full scale (mA)",
             "Example: 6 bar on a 0 to 10 bar sensor with 2 mV/V and 10 V excitation gives ε = 600 µε, ΔR = 0.42 Ω, Vout = 12.0 mV and 13.6 mA"],
    parts=[("Diaphragm", "Thin stainless steel disc welded to the process connection; its thickness sets the pressure range"),
           ("Strain gauges", "Metal foil or sputtered thin film resistors, typically 350 Ω, bonded or deposited on the diaphragm"),
           ("Wheatstone bridge", "Four gauges connected so the strain signals add and temperature effects cancel"),
           ("Compensation resistors", "Trim the zero and the temperature coefficient of the bridge"),
           ("Signal conditioner", "Supplies excitation, amplifies the millivolt signal and produces 4 to 20 mA or a digital output")],
    uses=[("Hydraulic systems", "Pump, press and cylinder pressure with high overpressure ratings."),
          ("Process transmitters", "Gauge and sealed gauge pressure on pipes, vessels and pumps."),
          ("Tank level", "Hydrostatic level from the pressure at the bottom of a tank."),
          ("Test benches", "Millivolt output sensors logged directly by data acquisition systems.")],
    pros=["Robust metal diaphragm suits high pressures and pressure spikes", "Linear output with good long term stability", "Simple, well understood bridge circuit"],
    cons=["Millivolt signal is sensitive to noise and cable resistance", "Lower sensitivity than piezoresistive silicon sensors, so low ranges are harder", "Zero shifts permanently if the overpressure limit is exceeded"],
    tips=["For millivolt sensors on long cables, use the sense wires (6 wire connection) or measure the excitation at the sensor.",
          "Use shielded twisted pair cable and earth the shield at one end only.",
          "Check the zero with the sensor vented to atmosphere before blaming the process, and keep the vent clean on gauge types.",
          "Fit a snubber or damper on lines with water hammer or pump pulsation to protect the diaphragm."],
    faq=[("What does 2 mV/V mean?", "It is the rated output: at full scale pressure the bridge gives 2 mV for every volt of excitation. With 10 V excitation the full scale output is 20 mV."),
         ("Why use four gauges instead of one?", "A full bridge gives four times the output of a single active gauge and cancels changes that affect all gauges equally, such as temperature. It also makes the output nearly linear."),
         ("How is a strain gauge sensor different from a piezoresistive one?", "Metal foil or thin film gauges have a gauge factor of about 2. Silicon piezoresistive gauges have a much higher gauge factor, so they give more signal but need more temperature compensation."),
         ("Why does the zero drift after a pressure spike?", "If the pressure goes beyond the overpressure limit, the diaphragm or the gauge bond yields slightly and does not return to the same shape. The result is a permanent zero shift that needs recalibration or replacement.")],
    cal=[("instrumentation-signal/strain-gauge-calculator", "Strain Gauge Calculator"), ("electronics/wheatstone-bridge-calculator", "Wheatstone Bridge Calculator")],
    glo=[("piezoresistive-pressure-sensor", "Piezoresistive Pressure Sensor"), ("gauge-pressure", "Gauge Pressure"), ("overpressure-limit", "Overpressure Limit")],
    cmp=[("capacitive-vs-piezoresistive-pressure-sensor", "Capacitive vs Piezoresistive Pressure Sensor")],
    tool=[("tools/practice-tests/pressure-measurement-quiz", "Pressure Measurement Quiz")],
    blog=("strain-gauge-working-principle", "Strain gauge working principle"))

SCENE = r"""
var pd=[];for(var i=0;i<70;i++)pd.push([Math.random(),Math.random(),Math.random()*6.28]);
function wr(v){return ((v%1)+1)%1;}
function ue(){return P.ro*500*P.p/10;}
function upd(){var e=ue();o('e','± '+m(e,0)+' µε');o('dr','± '+m(350*2*e*1e-6,3)+' Ω');o('v',m(P.vx*P.ro*P.p/10,2)+' mV');o('ma',m(4+16*P.p/10,2)+' mA');}
function step(dt){}
function dy(x){var u=(x-155)/93;u=clamp(u,-1,1);return 170-24*P.p/10*Math.pow(1-u*u,2);}
function dots(pts,off,col){var acc=0;for(var i=0;i<pts.length-1;i++){var a=pts[i],b=pts[i+1],l=Math.hypot(b[0]-a[0],b[1]-a[1]);for(var s=((off-acc)%22+22)%22;s<l;s+=22){ci(a[0]+(b[0]-a[0])*s/l,a[1]+(b[1]-a[1])*s/l,2.6,col);}acc+=l;}}
function res(x,y,col,t){rc(x-17,y-7,34,14,'#ffffff',col,3);C.lineWidth=2;C.strokeStyle=col;C.stroke();L(t,x,y,10,col,'center',1);}
function draw(){var e=ue(),dr=350*2*e*1e-6,vo=P.vx*P.ro*P.p/10,TC='#16a34a',CC='#7c3aed';
L('Diaphragm bending greatly exaggerated',20,22,11,'#5b6576','left');
L('Sensor cross section',155,74,12,'#1a2333','center',1);
C.fillStyle='#dbeafe';C.beginPath();C.moveTo(62,260);for(var x=62;x<=248;x+=3)C.lineTo(x,dy(x)+6);C.lineTo(248,260);C.closePath();C.fill();
rc(140,258,30,82,'#dbeafe');ln(140,262,140,340,'#64748b',3);ln(170,262,170,340,'#64748b',3);
var n=Math.round(18+5*P.p);for(var i=0;i<n;i++){var d=pd[i],x=66+178*wr(d[0]+0.02*Math.sin(T*3+d[2])),y=wr(d[1]+0.03*Math.cos(T*2.5+d[2]));y=dy(x)+12+y*(250-dy(x)-12);ci(x,y,2.2,'#1e63b8');}
for(var i=0;i<8;i++){var y=338-((T*30+i*10)%80);ci(147+(i%3)*8,y,2.2,'#1e63b8');}
rc(40,120,22,154,'#9aa5b8','#64748b');rc(248,120,22,154,'#9aa5b8','#64748b');rc(62,260,78,14,'#9aa5b8');rc(170,260,78,14,'#9aa5b8');
C.fillStyle='#64748b';C.beginPath();C.moveTo(62,dy(62));for(var x=62;x<=248;x+=3)C.lineTo(x,dy(x));for(var x=248;x>=62;x-=3)C.lineTo(x,dy(x)+6);C.closePath();C.fill();
var gs=[[135,TC,'R1 +ε',128],[175,TC,'R3 +ε',128],[77,CC,'R4 −ε',150,96],[233,CC,'R2 −ε',150,214]];
gs.forEach(function(g){var y=dy(g[0]);rc(g[0]-8,y-5,16,5,g[1]);L(g[2],g[4]||g[0],g[3],11,g[1],'center',1);});
rc(100,212,110,24,'rgba(255,255,255,0.92)','#94a3b8',5);L('P = '+m(P.p,1)+' bar',155,224,12,'#1e63b8','center',1);
ar(155,336,155,300,'#1e3a8a',2);L('From process',178,322,11,'#1e3a8a','left',1);
var Tn=[420,70],Rn=[520,160],Bn=[420,250],Ln=[320,160];
ln(Tn[0],Tn[1],Ln[0],Ln[1],TC,2);ln(Tn[0],Tn[1],Rn[0],Rn[1],CC,2);ln(Rn[0],Rn[1],Bn[0],Bn[1],TC,2);ln(Ln[0],Ln[1],Bn[0],Bn[1],CC,2);
var off=T*(10+3*P.vx);dots([Tn,Ln,Bn],off,'#f59e0b');dots([Tn,Rn,Bn],off,'#f59e0b');
res(370,115,TC,'R1');res(470,115,CC,'R2');res(470,205,TC,'R3');res(370,205,CC,'R4');
L(m(350+dr,2)+' Ω',350,115,11,TC,'right',1);L(m(350-dr,2)+' Ω',490,115,11,CC,'left',1);L(m(350+dr,2)+' Ω',490,205,11,TC,'left',1);L(m(350-dr,2)+' Ω',326,228,11,CC,'left',1);
[Tn,Rn,Bn,Ln].forEach(function(q){ci(q[0],q[1],4,'#1a2333');});
L('+ '+m(P.vx,1)+' V excitation',420,52,11,'#b45309','center',1);L('0 V',420,268,11,'#475569','center',1);
ln(320,160,385,160,'#334155',1.5);ln(455,160,520,160,'#334155',1.5);rc(385,146,70,28,'#0f172a',null,5);L(m(vo,2)+' mV',420,160,12,'#4ade80','center',1);L('Vout',420,186,11,'#1a2333','center',1);
ln(520,160,580,160,'#334155',1.5);ln(580,160,580,214,'#334155',1.5);ln(320,160,320,296,'#334155',1.5);ln(320,296,580,296,'#334155',1.5);ln(580,296,580,284,'#334155',1.5);
rc(530,214,100,70,'#1a2333',null,8);L('Signal',580,230,11,'#cbd5e1','center',1);L('conditioner',580,244,11,'#cbd5e1','center',1);L(m(4+16*P.p/10,1)+' mA',580,266,13,'#fde68a','center',1);
L('R1 and R3: centre gauges in tension, +ε',300,320,11,TC,'left',1);L('R2 and R4: edge gauges in compression, −ε',300,340,11,CC,'left',1);
mk(1,122,300);mk(2,155,dy(155)+22);mk(3,155,108);mk(4,46,150);mk(5,420,98);mk(6,618,214);}
"""
