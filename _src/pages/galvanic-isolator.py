PAGE = dict(
    slug="galvanic-isolator", grp="Signals", name="Galvanic Isolator", kw="How a Galvanic Isolator Works",
    title="How a Galvanic Isolator Works: Animated Diagram and Formula",
    desc="How a galvanic isolator works, animated: a 4 to 20 mA signal crosses a transformer barrier while two earths at different voltages stay apart.",
    h1="How a Galvanic Isolator Works",
    hero="Change the transmitter current, the receiver load and the voltage difference between the field earth and the control room earth. Watch the signal cross the transformer while the barrier holds back the earth voltage.",
    quick="A galvanic isolator copies a signal from one circuit to another with no conductive path between them. The input is turned into an AC signal, passed through a small transformer or optocoupler, and rebuilt on the output side, so earth differences and ground loop currents cannot pass.",
    intro=["Two earth points in a plant are rarely at exactly the same voltage. If a 4 to 20 mA loop is earthed at both ends, that difference drives a ground loop current through the signal wires and the reading becomes wrong or noisy.",
           "A galvanic isolator breaks the wired connection while still passing the measurement. The input side, the output side and often the power supply each sit on their own island, joined only by magnetic or optical coupling.",
           "The same idea is used in intrinsically safe isolators for hazardous areas. There the isolator also limits the energy sent to the field, and unlike a zener barrier it needs no dedicated IS earth."],
    sliders=[("i", "Input current from transmitter", 4, 20, 12, 0.1, 1, "mA"), ("rl", "Receiver load resistance RL", 50, 750, 250, 10, 0, "Ω"), ("vg", "Ground potential difference Vg", 0, 30, 5, 0.5, 1, "V")],
    outs=[("io", "Output current (1 to 1 transfer)"), ("vl", "Voltage across receiver = Iout × RL"), ("pc", "Signal in percent of span"), ("cm", "Voltage held by the isolation barrier")],
    legend=["Field transmitter, 2 wire", "Input loop powered by the isolator", "Modulator (DC to AC)", "Isolation transformer and barrier", "Demodulator and output driver", "Receiver resistor in the DCS input", "Field earth and control room earth at different voltages"],
    steps=["The isolator powers the field transmitter and measures the 4 to 20 mA input current.",
           "A modulator chops the input signal into a high frequency AC signal that a transformer can pass.",
           "The transformer windings are separated by insulation, so energy crosses magnetically while no current can flow between the two sides.",
           "On the output side the AC signal is rectified and a driver rebuilds an identical 4 to 20 mA current.",
           "The output current flows through the receiver resistor in the DCS or PLC, while any voltage between the two earths appears only across the barrier."],
    formula=["Iout = Iin (1 to 1 transfer across the barrier)",
             "Voltage at receiver = Iout × RL",
             "Percent of span = (I − 4) ÷ 16 × 100",
             "Ground loop current = 0, because no conductive path joins the two earths",
             "Example: 12 mA into 250 Ω gives 3.00 V, which is 50.0 % of span; a 5 V earth difference sits across the barrier and drives no current"],
    parts=[("Input stage", "Supplies loop power to the transmitter and senses the input current"),
           ("Modulator", "Converts the DC measurement into an AC or pulse signal that can cross the barrier"),
           ("Isolation transformer or optocoupler", "Carries the signal across an insulation gap rated for a test voltage stated on the datasheet"),
           ("Demodulator and output driver", "Rebuilds the 4 to 20 mA output and drives it into the receiver load"),
           ("Isolated power supply", "Feeds each side from its own winding, so input, output and power are three separate circuits")],
    uses=[("Ground loop removal", "Breaking loops that are earthed at both the field device and the control system."),
          ("Hazardous areas", "Intrinsically safe isolators feeding transmitters in Zone 0, 1 or 2 without an IS earth."),
          ("Signal splitting", "Sending one transmitter signal to two systems such as a DCS and a separate recorder."),
          ("Mixed systems", "Connecting equipment from different panels or power systems that do not share a common earth.")],
    pros=["Removes ground loop errors and common mode noise", "Needs no dedicated low resistance IS earth", "Protects the control system input from field faults up to the rated isolation voltage"],
    cons=["Needs its own power supply and costs more than a zener barrier", "Adds a small accuracy error and response delay to the loop", "The output stage has a maximum load, so long cables plus large receivers can exceed it"],
    tips=["Check the maximum load resistance on the datasheet and add receiver, cable and any indicator resistances before connecting.",
          "If a reading changes when a second earth connection is made or removed, suspect a ground loop and fit an isolator.",
          "Earth the cable screen at one end only, normally the control room end, even when an isolator is fitted.",
          "During loop checks inject a known current at the input and confirm the same current at the output with a calibrated meter."],
    faq=[("What is the difference between a galvanic isolator and a zener barrier?", "A zener barrier limits energy with diodes and resistors and needs an IS earth. A galvanic isolator separates the circuits with a transformer or optocoupler, so it needs no IS earth but requires a power supply."),
         ("What does 3 port isolation mean?", "The input, the output and the power supply are each isolated from the other two. A fault or earth difference on any one port cannot reach the others."),
         ("Does an isolator change the signal value?", "Ideally no, the output current equals the input current. In practice there is a small error given on the datasheet, which should be checked during calibration."),
         ("Can an isolator fix electrical noise on a loop?", "It removes noise caused by ground loops and common mode voltages. Noise induced directly into the signal pair needs proper twisted, screened cable and correct routing.")],
    cal=[("instrumentation-signal/current-to-voltage-resistor-calculator", "Current to Voltage Resistor Calculator"), ("instrumentation-signal/loop-power-supply-calculator", "Loop Power Supply Calculator")],
    glo=[("galvanic-isolation", "Galvanic Isolation"), ("signal-isolator", "Signal Isolator"), ("ground-loop", "Ground Loop")],
    cmp=[("zener-barrier-vs-galvanic-isolator", "Zener Barrier vs Galvanic Isolator")],
    tool=[("tools/troubleshooting/4-20-ma-loop-fault-finder", "4 to 20 mA Loop Fault Finder")],
    blog=("what-is-galvanic-isolation", "What is galvanic isolation"))

SCENE = r"""
function upd(){o('io',m(P.i,2)+' mA');o('vl',m(P.i*P.rl/1000,2)+' V');o('pc',m((P.i-4)/16*100,1)+' %');o('cm',m(P.vg,1)+' V, no loop current');}
function step(dt){}
function dots(pts,off,col){var acc=0;for(var i=0;i<pts.length-1;i++){var a=pts[i],b=pts[i+1],l=Math.hypot(b[0]-a[0],b[1]-a[1]);for(var s=((off-acc)%22+22)%22;s<l;s+=22){ci(a[0]+(b[0]-a[0])*s/l,a[1]+(b[1]-a[1])*s/l,3,col);}acc+=l;}}
function zz(x,y1,y2){C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(x,y1);var n=6,h=(y2-y1)/(n+1);for(var k=0;k<n;k++)C.lineTo(x+(k%2?-7:7),y1+h*(k+0.5)+h/2);C.lineTo(x,y2);C.stroke();}
function coil(x,dir,col){C.strokeStyle=col;C.lineWidth=2.5;for(var k=0;k<5;k++){C.beginPath();C.arc(x,136+k*12+6,6,dir>0?-Math.PI/2:Math.PI/2,dir>0?Math.PI/2:Math.PI*1.5);C.stroke();}}
function earth(x,y,col){ln(x,y,x,y+12,col,2);ln(x-14,y+12,x+14,y+12,col,2.5);ln(x-9,y+18,x+9,y+18,col,2.5);ln(x-4,y+24,x+4,y+24,col,2.5);}
function draw(){var sp=T*(10+P.i*3);
L('Signal dots and AC wave speed exaggerated',20,22,11,'#5b6576','left');
L('FIELD SIDE',95,52,12,'#b45309','center',1);L('CONTROL ROOM SIDE',540,52,12,'#1d7a46','center',1);
rc(190,70,250,200,'#eef2f7','#475569',10);L('Galvanic isolator',250,90,11,'#5b6576','center',1);
ln(315,58,315,300,'#b91c1c',2,[7,5]);L('Isolation barrier',315,312,11,'#b91c1c','center',1);
ln(80,120,80,110,'#334155',2);ln(80,110,240,110,'#334155',2);ln(240,110,240,120,'#334155',2);ln(240,210,240,230,'#334155',2);ln(240,230,80,230,'#334155',2);ln(80,230,80,210,'#334155',2);
ln(390,120,390,110,'#334155',2);ln(390,110,560,110,'#334155',2);ln(560,110,560,135,'#334155',2);zz(560,135,205);ln(560,205,560,230,'#334155',2);ln(560,230,390,230,'#334155',2);ln(390,230,390,210,'#334155',2);
rc(30,120,100,90,'#ffffff','#475569',8);ci(80,150,15,'#e0f2fe','#0369a1',2);L('PT',80,150,11,'#0369a1','center',1);L('Transmitter',80,180,11,'#1a2333','center',1);L(m(P.i,1)+' mA',80,197,11,'#1e63b8','center',1);
rc(205,120,70,90,'#1a2333',null,6);L('Modulator',240,140,11,'#cbd5e1','center',1);
C.strokeStyle='#fbbf24';C.lineWidth=2;C.beginPath();for(var x=212;x<=268;x+=2){var y=175+9*Math.sin((x-212)/56*4*Math.PI-T*9)*(P.i/20);if(x==212)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
rc(355,120,70,90,'#1a2333',null,6);L('Output',390,140,11,'#cbd5e1','center',1);L('driver',390,154,11,'#cbd5e1','center',1);L(m(P.i,1)+' mA',390,190,12,'#4ade80','center',1);
ln(275,142,296,142,'#334155',2);ln(275,190,296,190,'#334155',2);ln(334,142,355,142,'#334155',2);ln(334,190,355,190,'#334155',2);
var g=0.55+0.45*Math.sin(T*12);var cc='rgba(217,98,43,'+g+')';coil(296,1,cc);coil(334,-1,cc);ln(310,132,310,200,'#475569',2.5);ln(320,132,320,200,'#475569',2.5);
L('AC',300,122,11,'#d9622b','right',1);
dots([[80,120],[80,110],[240,110],[240,120]],sp,'#1e63b8');dots([[240,210],[240,230],[80,230],[80,210]],sp,'#1e63b8');
dots([[390,120],[390,110],[560,110],[560,135]],sp,'#16a34a');dots([[560,205],[560,230],[390,230],[390,210]],sp,'#16a34a');
L('RL '+m(P.rl,0)+' Ω',575,160,11,'#1a2333','left',1);L(m(P.i*P.rl/1000,2)+' V',575,178,11,'#16a34a','left',1);L('DCS input',560,96,11,'#1a2333','center',1);
ln(80,230,80,262,'#b45309',2);earth(80,262,'#b45309');ln(560,230,560,262,'#1d7a46',2);earth(560,262,'#1d7a46');
L('Field earth',120,278,11,'#b45309','left',1);L('Control earth',520,278,11,'#1d7a46','right',1);
var pa=0.5+0.5*Math.sin(T*3);ln(110,334,530,334,'rgba(185,28,28,'+(0.4+0.6*pa)+')',2,[6,4]);L('Vg = '+m(P.vg,1)+' V between earths',190,348,11,'#b91c1c','left',1);L('Ground loop current 0 mA',530,348,11,'#1d7a46','right',1);
mk(1,30,120);mk(2,160,110);mk(3,240,226);mk(4,345,250);mk(5,390,226);mk(6,600,135);mk(7,48,292);}
"""
