PAGE = dict(
    slug="capacitance-level-probe", grp="Level", name="Capacitance Level Probe", kw="How a Capacitance Level Probe Works",
    title="How a Capacitance Level Probe Works: Animated Diagram",
    desc="How a capacitance level probe works, animated: rising liquid replaces air between the rod and tube, so capacitance and the 4 to 20 mA output rise with level.",
    h1="How a Capacitance Level Probe Works",
    hero="Change the liquid level, the dielectric constant of the liquid and the reference tube diameter. Watch the capacitance between the rod and the tube grow as the liquid covers more of the probe.",
    quick="A capacitance level probe forms a capacitor between a metal rod and the tank wall or a reference tube. Liquid has a higher dielectric constant than air, so as the level rises the capacitance rises in proportion, and the transmitter converts that change into a 4 to 20 mA signal.",
    intro=["Any two conductors separated by an insulating material form a capacitor. In a capacitance level probe the rod is one plate, the tank wall or a coaxial tube is the other, and the material between them is either vapour or the process liquid.",
           "Air has a dielectric constant of about 1, while oils and solvents are around 2 and water is about 80. Each centimetre of liquid that covers the probe therefore adds more capacitance than the same length in air.",
           "For conductive liquids such as water the rod is covered with an insulating sleeve, and the sleeve itself becomes the dielectric. The principle is the same, but the probe must then be calibrated on the actual liquid."],
    sliders=[("h", "Liquid level h", 0, 2, 1.2, 0.01, 2, "m"), ("er", "Liquid dielectric constant εr", 1.5, 20, 2.2, 0.1, 1, ""), ("D", "Reference tube inner diameter D", 30, 100, 50, 1, 0, "mm")],
    outs=[("ca", "Capacitance per metre in air"), ("c0", "Empty probe capacitance (L = 2 m)"), ("c", "Capacitance now"), ("ma", "Output (0 to 2 m = 4 to 20 mA)")],
    legend=["Transmitter head with oscillator", "Probe rod (inner plate, d = 16 mm)", "Reference tube or tank wall (outer plate)", "Insulating seal at the process connection", "Liquid (dielectric εr)", "Vapour space (air, εr about 1)", "Capacitance versus level line"],
    steps=["The transmitter applies a small AC voltage between the probe rod and the reference tube or tank wall.",
           "With the tank empty, only air sits between the plates and the transmitter measures the empty capacitance.",
           "As liquid rises it replaces air along the covered length, and its higher dielectric constant raises the capacitance.",
           "The rise in capacitance is directly proportional to the covered length, so the signal is linear with level.",
           "After an empty and a full calibration the electronics scale the capacitance to 4 to 20 mA."],
    formula=["C = 2π ε0 [L + (εr − 1) h] ÷ ln(D ÷ d)",
             "Air capacitance per metre = 2π ε0 ÷ ln(D ÷ d), with ε0 = 8.854 pF/m",
             "Rise in C = 2π ε0 (εr − 1) h ÷ ln(D ÷ d), proportional to level h",
             "Output = 4 + 16 × h ÷ L mA after empty and full calibration",
             "Example: rod 16 mm, tube 50 mm, L 2 m gives 48.8 pF/m and 97.6 pF empty; 1.2 m of oil with εr 2.2 gives 168.0 pF and 13.6 mA"],
    parts=[("Probe rod", "Metal electrode inserted into the tank, bare for insulating liquids or sleeved for conductive liquids"),
           ("Reference tube or tank wall", "Second plate of the capacitor; a coaxial tube gives a fixed geometry in non metallic tanks"),
           ("Insulating seal", "Isolates the rod from the tank flange so the only path is through the capacitance"),
           ("Transmitter electronics", "Measures capacitance with a high frequency signal and scales it to 4 to 20 mA or a switch output"),
           ("Guard or shield section", "Optional active section near the top that reduces errors from build up and condensation")],
    uses=[("Oil and diesel tanks", "Continuous level in storage and day tanks with stable, low dielectric liquids."),
          ("Water and effluent", "Insulated probes for conductive liquids in sumps and small vessels."),
          ("Point level switches", "High or low alarms in liquids and dry powders such as cement and plastic granules."),
          ("Interface level", "Detecting an oil and water interface where the two dielectric constants are very different.")],
    pros=["No moving parts and a simple, rugged probe", "Works at high pressure and temperature with suitable seals", "Linear output and low cost for continuous level"],
    cons=["Reading shifts if the dielectric constant changes with product or temperature", "Coating and build up on the rod can cause errors", "Needs calibration on the actual product, especially with insulated probes"],
    tips=["Find the dielectric constant of the actual product before choosing a probe; a low value gives a small capacitance change and poor resolution.",
          "In plastic or concrete tanks use a coaxial probe or a separate earth rod, because there is no metal wall to act as the second plate.",
          "Do the empty and full calibration with the real liquid at normal temperature rather than with water.",
          "If the reading drifts high over weeks, inspect the rod for coating and consider a probe with an active guard."],
    faq=[("Can a capacitance probe measure water level?", "Yes, using an insulated rod. Water is conductive, so the insulating sleeve becomes the dielectric and the probe acts as a capacitor between the rod and the water itself."),
         ("Why does the dielectric constant matter so much?", "The change in capacitance is proportional to εr minus 1. A liquid with εr 2 gives only a small change, while water gives a very large one."),
         ("What is the reference tube for?", "It gives a fixed outer plate at a known distance from the rod. This makes the capacitance predictable and is needed in non metallic tanks."),
         ("Does foam affect a capacitance probe?", "Light foam has a dielectric constant close to air and has little effect. Dense or conductive foam can add capacitance and make the reading high.")],
    cal=[("level/capacitance-level-probe-calculator", "Capacitance Level Probe Calculator"), ("electrical/capacitor-energy-calculator", "Capacitor Energy Calculator")],
    glo=[("capacitance-level-probe", "Capacitance Level Probe"), ("dielectric-constant", "Dielectric Constant"), ("point-level-measurement", "Point Level Measurement")],
    cmp=[],
    tool=[("tools/troubleshooting/level-transmitter-fault-finder", "Level Transmitter Fault Finder")],
    blog=("capacitance-level-measurement", "Capacitance level measurement"))

SCENE = r"""
var E0=8.854,Lp=2,dd=16;
function cpm(){return 2*Math.PI*E0/Math.log(P.D/dd);}
function cap(h){return cpm()*(Lp+(P.er-1)*h);}
function Y(h){return 320-110*h;}
function upd(){o('ca',m(cpm(),1)+' pF/m');o('c0',m(cpm()*Lp,1)+' pF');o('c',m(cap(P.h),1)+' pF');o('ma',m(4+16*P.h/Lp,2)+' mA');}
function step(dt){}
function draw(){var s=Y(P.h),c=cap(P.h);
L('Liquid surface motion exaggerated',20,22,11,'#5b6576','left');
rc(40,78,230,264,'#e2e8f0','#64748b',6);rc(46,84,218,252,'#f8fafc');
wave(46,264,s,336,'rgba(253,224,71,0.75)');
rc(134,84,6,236,'#64748b');rc(170,84,6,236,'#64748b');for(var k=0;k<4;k++){rc(134,130+k*50,6,10,'#f8fafc');rc(170,155+k*50,6,10,'#f8fafc');}
rc(152,84,6,236,'#94a3b8','#334155');
var off=-T*30;C.setLineDash([3,4]);C.lineDashOffset=off;for(var y=100;y<318;y+=12){var wet=y>s+2;C.strokeStyle=wet?'rgba(217,98,43,0.95)':'rgba(30,99,184,0.55)';C.lineWidth=wet?2:1.2;C.beginPath();C.moveTo(141,y);C.lineTo(151,y);C.moveTo(159,y);C.lineTo(169,y);C.stroke();}C.setLineDash([]);C.lineDashOffset=0;
rc(144,70,22,16,'#fff7ed','#334155',3);rc(150,58,10,12,'#64748b');
rc(110,30,100,30,'#1a2333',null,6);var a=0.6+0.4*Math.sin(T*10);ci(124,45,4,'rgba(251,191,36,'+a+')');L(m(c,1)+' pF',166,45,12,'#fbbf24','center',1);
L('h = '+m(P.h,2)+' m',54,Math.max(96,s-14),11,'#1e63b8','left',1);ln(270,s,286,s,'#1e63b8',1.5);ln(286,320,296,320,'#5b6576',1);L('0',300,320,11,'#5b6576','left');
var cx=380,cy=118,rO=P.D*0.6,rI=dd*0.6;rc(300,40,160,156,'#f8fafc','#cbd5e1',8);L('Section at the liquid',380,52,11,'#5b6576','center',1);
ci(cx,cy,rO+4,'#64748b');ci(cx,cy,rO,P.h>0.01?'rgba(253,224,71,0.75)':'#f8fafc');ci(cx,cy,rI,'#94a3b8','#334155');
C.setLineDash([3,4]);C.lineDashOffset=off;C.strokeStyle='rgba(217,98,43,0.9)';C.lineWidth=1.5;for(var q=0;q<8;q++){var an=q*Math.PI/4+T*0.4;C.beginPath();C.moveTo(cx+rI*Math.cos(an),cy+rI*Math.sin(an));C.lineTo(cx+rO*Math.cos(an),cy+rO*Math.sin(an));C.stroke();}C.setLineDash([]);C.lineDashOffset=0;
L('D '+m(P.D,0)+' mm',380,186,11,'#1a2333','center',1);
rc(470,40,155,156,'#1a2333',null,8);L('Transmitter',548,56,11,'#cbd5e1','center',1);L('C = '+m(c,1)+' pF',548,82,14,'#fbbf24','center',1);
L('Empty '+m(cpm()*Lp,1)+' pF',548,106,11,'#cbd5e1','center');L('Full '+m(cap(Lp),1)+' pF',548,124,11,'#cbd5e1','center');
L(m(4+16*P.h/Lp,2)+' mA',548,152,16,'#4ade80','center',1);L('εr '+m(P.er,1),548,178,11,'#cbd5e1','center');
var gx0=340,gx1=615,gy0=222,gy1=318,cm=cap(Lp)*1.05,GX=function(h){return gx0+(gx1-gx0)*h/Lp;},GY=function(v){return gy1-(gy1-gy0)*v/cm;};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');ln(GX(0),GY(cap(0)),GX(Lp),GY(cap(Lp)),'#1e63b8',2);
var pr=1+0.25*Math.sin(T*6);ci(GX(P.h),GY(c),5*pr,'#d9622b');L('Capacitance versus level',gx0,gy0-10,11,'#1e63b8','left',1);
L('0 m',gx0,gy1+12,11,'#5b6576','left');L('2 m',gx1,gy1+12,11,'#5b6576','right');L(m(cap(Lp),0)+' pF',gx0+4,gy0+10,11,'#5b6576','left');
mk(1,222,45);mk(2,155,110);mk(3,188,236);mk(4,182,70);mk(5,230,Math.min(326,s+28));mk(6,230,s>110?Math.max(98,s-24):92);mk(7,gx1-14,gy1-14);}
"""
