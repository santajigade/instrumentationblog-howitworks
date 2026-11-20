PAGE = dict(
    slug="sinking-sourcing-plc", grp="PLC", name="Sinking and Sourcing PLC Inputs", kw="How Sinking and Sourcing Inputs Work",
    title="How Sinking and Sourcing Inputs Work: Animated PLC Wiring",
    desc="How sinking and sourcing inputs work, animated: see current flow from a PNP sensor into a sinking input and from a sourcing input into an NPN sensor.",
    h1="How Sinking and Sourcing Inputs Work",
    hero="Change the supply voltage, the input resistance and the voltage drop of the sensor. Watch the target pass both sensors and follow the direction of current in each circuit.",
    quick="A sinking input receives current from the field device and returns it to 0 V through its common terminal, so it pairs with a PNP sensor. A sourcing input supplies current from its common at +24 V out through the input terminal, so it pairs with an NPN sensor that switches the signal to 0 V.",
    intro=["Sinking and sourcing describe the direction of DC current between a PLC input and the device wired to it. Getting the pair wrong is one of the most common reasons a new proximity sensor shows its own LED but the PLC input never turns on.",
           "The rule is simple: a sourcing device must feed a sinking input, and a sinking device must feed a sourcing input. A PNP sensor sources current, an NPN sensor sinks current.",
           "The common terminal of the input card tells you which type it is. If COM goes to 0 V the inputs are sinking, and if COM goes to +24 V the inputs are sourcing; some cards accept either."],
    sliders=[("v", "Supply voltage", 18, 30, 24, 0.5, 1, "V"), ("r", "Input resistance", 2.2, 10, 4.7, 0.1, 1, "kΩ"), ("vd", "Sensor output voltage drop", 0.5, 3, 2.0, 0.1, 1, "V")],
    outs=[("i", "Input current I = (V − Vdrop) ÷ R"), ("vin", "Voltage across the input when ON"), ("p", "Power in the input resistance"), ("rule", "Correct pairs")],
    legend=["PNP sensor: switches +24 V to its output", "Sinking input card: COM to 0 V", "NPN sensor: switches its output to 0 V", "Sourcing input card: COM to +24 V", "Direction of current when the input is ON", "Metal target passing both sensors", "24 V DC supply rails"],
    steps=["Both sensors take their own supply from the brown wire at +24 V and the blue wire at 0 V.",
           "When the target arrives, the PNP sensor connects its black output wire to +24 V; current flows into input I0.0 of the sinking card and returns to 0 V through COM.",
           "At the same moment the NPN sensor connects its black output wire to 0 V; current leaves the sourcing card at I0.0, having entered at COM from +24 V.",
           "In both circuits the current passes through the input resistance and the optocoupler LED, so the input turns ON.",
           "When the target leaves, the sensor output opens, the current stops and the input turns OFF."],
    formula=["Input current I = (V supply − V drop of the sensor) ÷ R input",
             "Voltage across the input = V supply − V drop",
             "Power in the input = (V supply − V drop) × I",
             "PNP (sourcing) sensor with a sinking input; NPN (sinking) sensor with a sourcing input",
             "Example: 24 V supply, 2.0 V sensor drop, 4.7 kΩ input: I = (24 − 2) ÷ 4.7 = 4.68 mA, voltage across input = 22 V, power = 22 × 4.68 = 103 mW"],
    parts=[("Input terminal I0.0", "Where the sensor output wire lands on the card"),
           ("Common terminal COM", "Shared return or feed for a group of inputs; its connection sets sinking or sourcing"),
           ("Input resistance and optocoupler", "Limit the current and pass the signal to the logic side with isolation"),
           ("PNP sensor", "Has a transistor between +24 V and its output, so it sources current"),
           ("NPN sensor", "Has a transistor between its output and 0 V, so it sinks current")],
    uses=[("Proximity and photoelectric sensors", "Choosing a PNP or NPN version to match the input card."),
          ("Panel retrofit", "Reusing old sensors on a new card by wiring COM the right way."),
          ("Mixed sensor groups", "Using a card that accepts either type, one group per common."),
          ("Troubleshooting", "Finding why a sensor LED turns on while the PLC input stays OFF.")],
    pros=["Simple rule that works on every DC input card", "Matching pairs give a clean ON and OFF with a few milliamps", "Many cards accept either type through the COM wiring"],
    cons=["A wrong pair leaves the input OFF even though the sensor LED works", "All inputs on one common must be the same type", "Terms are confusing because manufacturers sometimes describe the card and sometimes the device"],
    tips=["Measure between the input terminal and COM with the target present; you should see nearly the full supply minus the sensor drop.",
          "If a sensor LED turns on but the PLC input does not, check the sensor type against the COM wiring before replacing anything.",
          "Keep PNP and NPN sensors on different commons, or use an interposing relay.",
          "Use PNP sensors with sinking inputs where possible; with 0 V earthed, a short of the signal wire to earth then gives OFF rather than a false ON."],
    faq=[("Which sensor goes with a sinking input?", "A PNP sensor. It sources current from +24 V into the input, and the card returns it to 0 V through COM."),
         ("Which sensor goes with a sourcing input?", "An NPN sensor. The card feeds current out of the input terminal and the sensor sinks it to 0 V."),
         ("How do I tell if my input card is sinking or sourcing?", "Look at where COM is wired in the drawing or the manual. COM to 0 V means sinking inputs, COM to +24 V means sourcing inputs."),
         ("What happens if I connect an NPN sensor to a sinking input?", "Both devices try to sink current, so no current flows through the input and it never turns ON, even though the sensor LED works.")],
    cal=[("plc-signal/plc-io-count-calculator", "PLC IO Count Calculator"), ("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("sinking-and-sourcing", "Sinking and Sourcing")],
    cmp=[("pnp-vs-npn-sensor", "PNP vs NPN Sensor")],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("sinking-and-sourcing-in-plc", "Sinking and sourcing in PLC"))

SCENE = r"""
var ty=110,on=false,dots=[];for(var i=0;i<12;i++)dots.push(i/12);
function cur(){return(P.v-P.vd)/P.r;}
function upd(){var i=cur();o('i',m(i,2)+' mA');o('vin',m(P.v-P.vd,1)+' V');o('p',m((P.v-P.vd)*i,0)+' mW');o('rule','PNP to sinking, NPN to sourcing');}
function step(dt){ty=185+80*Math.sin(2*Math.PI*T/5);on=Math.abs(ty-185)<32;var sp=on?0.12+cur()*0.02:0;for(var i=0;i<dots.length;i++)dots[i]=(dots[i]+dt*sp)%1;}
function path(pts,c){var Lg=0,sg=[];for(var k=1;k<pts.length;k++){var d=Math.hypot(pts[k][0]-pts[k-1][0],pts[k][1]-pts[k-1][1]);sg.push(d);Lg+=d;}
dots.forEach(function(u){var t=u*Lg;for(var k=1;k<pts.length;k++){if(t<=sg[k-1]){var f=t/sg[k-1];ci(pts[k-1][0]+(pts[k][0]-pts[k-1][0])*f,pts[k-1][1]+(pts[k][1]-pts[k-1][1])*f,3.2,c);break;}t-=sg[k-1];}});}
function panel(px,sink){var cl=sink?'#1e63b8':'#c2410c';
L(sink?'Sinking input with PNP sensor':'Sourcing input with NPN sensor',px+150,46,12,'#1a2333','center',1);
ln(px+14,70,px+296,70,'#dc2626',3);ln(px+14,300,px+296,300,'#2563eb',3);L('+24 V',px+292,60,11,'#dc2626','right',1);L('0 V',px+292,312,11,'#2563eb','right',1);
rc(px+6,150,18,60,'#fef9c3','#a16207',4);L('DC',px+15,180,11,'#713f12','center',1);ln(px+15,150,px+15,70,'#dc2626',2);ln(px+15,210,px+15,300,'#2563eb',2);
rc(px+36,ty-22,22,44,'#94a3b8','#475569',3);
rc(px+70,130,80,110,'#f8fafc','#475569',8);rc(px+66,158,6,54,on?'#fde68a':'#cbd5e1');L(sink?'PNP':'NPN',px+110,144,12,'#1a2333','center',1);ci(px+138,144,5,on?'#f59e0b':'#e2e8f0','#475569');
var sx=px+120;if(sink){ln(px+150,160,sx,160,'#475569',1.5);ci(sx,160,3,'#475569');ln(sx,160,on?sx:sx-14,on?186:182,'#475569',2);ci(sx,190,3,'#475569');ln(sx,190,px+150,190,'#475569',1.5);ln(px+150,160,px+150,150,'#475569',1.5);}
else{ln(px+150,186,sx,186,'#475569',1.5);ci(sx,186,3,'#475569');ln(sx,186,on?sx:sx-14,on?212:208,'#475569',2);ci(sx,216,3,'#475569');ln(sx,216,px+150,216,'#475569',1.5);}
L('switch',px+96,226,11,'#5b6576','center');
ln(px+150,150,px+160,150,'#92400e',2.5);ln(px+160,150,px+160,70,'#92400e',2.5);ln(px+150,230,px+160,230,'#2563eb',2.5);ln(px+160,230,px+160,300,'#2563eb',2.5);ln(px+150,186,px+190,186,'#0f172a',2.5);
L('BN',px+168,110,11,'#92400e','left',1);L('BU',px+168,270,11,'#2563eb','left',1);L('BK',px+170,176,11,'#0f172a','center',1);
rc(px+190,120,96,140,'#1a2333',null,8);L('Input card',px+238,sink?132:250,11,'#cbd5e1','center',1);ci(px+190,186,4,'#e2e8f0');L('I0.0',px+196,198,11,'#fff','left',1);
ln(px+190,186,px+205,186,'#cbd5e1',1.5);rc(px+205,180,26,12,null,'#cbd5e1');L('R',px+218,170,11,'#cbd5e1','center',1);ln(px+231,186,px+250,186,'#cbd5e1',1.5);
var ly=sink?218:154;C.fillStyle=on?'#22c55e':'#475569';C.beginPath();C.moveTo(px+242,ly-8);C.lineTo(px+258,ly-8);C.lineTo(px+250,ly+6);C.closePath();C.fill();ln(px+242,ly+6,px+258,ly+6,on?'#22c55e':'#94a3b8',2);
if(on){ar(px+262,ly,px+274,ly-8,'#22c55e',1.5);}
if(sink){ln(px+250,186,px+250,ly-8,'#cbd5e1',1.5);ln(px+250,ly+6,px+250,260,'#cbd5e1',1.5);ci(px+250,260,4,'#e2e8f0');ln(px+250,260,px+250,300,'#2563eb',2.5);L('COM',px+256,248,11,'#fff','left',1);}
else{ln(px+250,186,px+250,ly+6,'#cbd5e1',1.5);ln(px+250,ly-8,px+250,120,'#cbd5e1',1.5);ci(px+250,120,4,'#e2e8f0');ln(px+250,120,px+250,70,'#dc2626',2.5);L('COM',px+244,132,11,'#fff','right',1);}
L('Input '+(on?'ON':'OFF'),sink?px+222:px+238,sink?152:230,11,on?'#86efac':'#94a3b8','center',1);
if(on){if(sink)path([[px+15,150],[px+15,70],[px+160,70],[px+160,150],[px+150,150],[px+150,186],[px+190,186],[px+250,186],[px+250,300],[px+15,300],[px+15,210]],'#f59e0b');
else path([[px+15,150],[px+15,70],[px+250,70],[px+250,186],[px+190,186],[px+150,186],[px+150,230],[px+160,230],[px+160,300],[px+15,300],[px+15,210]],'#f59e0b');}
L(sink?'Current flows INTO I0.0':'Current flows OUT of I0.0',px+150,328,12,cl,'center',1);if(on)L(m(cur(),2)+' mA',px+150,346,11,'#5b6576','center');}
function draw(){L('Simple resistive model of the input; target speed slowed down',20,22,11,'#5b6576','left');
panel(10,true);panel(330,false);ln(320,40,320,350,'#e2e8f0',1.5);
mk(1,92,118);mk(2,296,124);mk(3,412,118);mk(4,616,262);mk(5,182,94);mk(6,47,clamp(ty-34,82,280));mk(7,26,128);}
"""
