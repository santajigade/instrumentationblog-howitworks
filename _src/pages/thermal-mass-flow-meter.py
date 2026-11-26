PAGE = dict(
    slug="thermal-mass-flow-meter", grp="Flow", name="Thermal Mass Flow Meter", kw="How a Thermal Mass Flow Meter Works",
    title="How a Thermal Mass Flow Meter Works: Animated Diagram",
    desc="How a thermal mass flow meter works, animated: gas carries heat away from a heated RTD, and the power needed to hold it hotter gives the mass flow.",
    h1="How a Thermal Mass Flow Meter Works",
    hero="Change the gas velocity, the gas density and the overheat of the heated sensor. Watch the gas sweep heat off the hot RTD and see the heater power climb along the King's law curve.",
    quick="A thermal mass flow meter keeps one RTD heated a fixed number of degrees above a second RTD that reads the gas temperature. Flowing gas cools the heated sensor, and the electrical power needed to hold the temperature difference rises with the mass velocity of the gas, so the meter reads mass flow directly.",
    intro=["Most gas flow meters measure volume, and the volume of a gas changes with pressure and temperature. A thermal mass flow meter responds to the number of molecules that carry heat away, so it reads mass flow without separate pressure and temperature compensation.",
           "The common industrial design is an insertion probe with two platinum RTDs. One measures the gas temperature, and the other is heated and held a constant amount hotter, for example 30 K above the gas.",
           "The heat lost from the hot sensor follows King's law: a fixed part from conduction and natural convection plus a part that grows with the square root of mass velocity. The meter is calibrated on the actual gas because the heat transfer also depends on the gas properties."],
    sliders=[("v", "Gas velocity v", 0, 30, 10, 0.5, 1, "m/s"), ("rho", "Gas density ρ", 0.5, 5, 1.2, 0.05, 2, "kg/m³"), ("dt", "Overheat ΔT of the heated RTD", 10, 60, 30, 1, 0, "K")],
    outs=[("gv", "Mass velocity ρv"), ("p", "Heater power P (example sensor)"), ("qm", "Mass flow in a 100 mm pipe"), ("nq", "Normal flow of air (0 °C, 1.013 bar)")],
    legend=["Transmitter electronics", "Insertion probe stem", "Reference RTD (gas temperature)", "Heated RTD held ΔT above the gas", "Gas flow", "Heat carried away by the gas", "Power versus mass velocity curve"],
    steps=["The reference RTD measures the gas temperature at the probe tip.",
           "The electronics heat the second RTD and hold it a constant ΔT above the reference temperature.",
           "Flowing gas carries heat away from the heated RTD; more molecules passing each second remove more heat.",
           "The electronics raise the heater power to keep ΔT constant, so the power is a measure of the mass velocity ρv.",
           "Using the calibration curve, the transmitter converts power into mass velocity and multiplies by the pipe area to give mass or normal flow."],
    formula=["P = ΔT × (a + b √(ρv)), King's law for a heated sensor",
             "ρv = [(P ÷ ΔT − a) ÷ b]², solved by the transmitter",
             "Mass flow qm = ρv × A, with A = π D² ÷ 4 for the pipe",
             "Normal flow = qm ÷ ρn, with ρn = 1.293 kg/m³ for air at 0 °C and 1.013 bar",
             "Example with a = 0.010 W/K and b = 0.005: v 10 m/s and ρ 1.2 kg/m³ give ρv 12 kg/m²s, P = 30 × (0.010 + 0.005 × 3.46) = 0.82 W, qm 339 kg/h, 262 Nm³/h"],
    parts=[("Heated RTD", "Platinum sensor held a fixed overheat above the gas; its heating power is the measurement"),
           ("Reference RTD", "Unheated platinum sensor that tracks the gas temperature so the overheat stays constant"),
           ("Probe stem and shield", "Holds both sensors at the right depth in the pipe and protects them from direct impact"),
           ("Bridge and control circuit", "Wheatstone bridge and amplifier that adjust the heater current to keep ΔT fixed"),
           ("Transmitter", "Applies the gas calibration, pipe area and totaliser, and gives 4 to 20 mA, pulse or digital outputs")],
    uses=[("Compressed air", "Monitoring consumption and leaks in plant air headers."),
          ("Natural gas and biogas", "Fuel flow to boilers, furnaces and gas engines."),
          ("Combustion air and flare gas", "Large ducts and flare lines where low pressure drop is essential."),
          ("Nitrogen and process gases", "Inerting and blanketing gas measured directly in mass or normal units.")],
    pros=["Reads mass flow directly with no pressure or temperature compensation", "Very wide turndown and good sensitivity at low velocities", "No moving parts and very low pressure drop"],
    cons=["Calibration is valid only for the gas composition it was calibrated on", "Moisture droplets or condensation cause large errors and spikes", "Insertion types need a good velocity profile and correct insertion depth"],
    tips=["Order the meter calibrated for the actual gas mixture; a meter calibrated on air will read wrong on methane or biogas.",
          "Give the meter the straight pipe run upstream and downstream stated in the manual, because it measures the velocity at one point.",
          "Mount the probe from the side or top in wet gas lines and fit a drain, so water droplets do not hit the heated sensor.",
          "Check the zero at no flow; a reading at zero usually means convection, a leaking valve or a sensor that needs cleaning."],
    faq=[("Why is it called a mass flow meter?", "The heat carried away depends on the mass of gas passing the sensor each second, not its volume. So the meter responds to ρv and gives mass flow directly."),
         ("Can a thermal mass flow meter measure liquids?", "Industrial insertion types are mainly for gases. Liquids remove far more heat and are usually measured with Coriolis or other meters."),
         ("What is constant ΔT operation?", "The heated RTD is kept a fixed amount above the gas temperature and the heater power is measured. The other method, constant power, measures the falling ΔT instead."),
         ("What is normal flow?", "Normal flow is the mass flow expressed as a volume at reference conditions, such as 0 °C and 1.013 bar. It is written as Nm³/h.")],
    cal=[("flow/mass-flow-to-volume-flow-calculator", "Mass Flow to Volume Flow Calculator"), ("flow/gas-flow-conversion-calculator", "Gas Flow Conversion Calculator")],
    glo=[("mass-flow-rate", "Mass Flow Rate"), ("transmitter-turndown", "Transmitter Turndown")],
    cmp=[("thermal-mass-vs-coriolis-flow-meter", "Thermal Mass vs Coriolis Flow Meter"), ("mass-flow-vs-volumetric-flow", "Mass Flow vs Volumetric Flow")],
    tool=[],
    blog=("thermal-mass-flow-meter-working", "Thermal mass flow meter working"))

SCENE = r"""
var A0=0.01,B0=0.005,AR=Math.PI*0.05*0.05,gp=[],hp=[];for(var i=0;i<70;i++)gp.push([Math.random(),Math.random()]);
function gv(){return P.rho*P.v;}
function pw(g){return P.dt*(A0+B0*Math.sqrt(g));}
function upd(){var g=gv(),qm=g*AR*3600;o('gv',m(g,2)+' kg/m²s');o('p',m(pw(g),3)+' W');o('qm',m(qm,1)+' kg/h');o('nq',m(qm/1.293,1)+' Nm³/h');}
function step(dt){var n=Math.round(4+P.v*0.6);for(var k=0;k<n*dt*10;k++)hp.push([216,256+8*(Math.random()-0.5),0]);
for(var i=hp.length-1;i>=0;i--){var h=hp[i];h[0]+=dt*(12+P.v*9);h[1]+=dt*(P.v<0.5?-14:(Math.random()-0.5)*14);h[2]+=dt;if(h[2]>1.6||h[0]>620)hp.splice(i,1);}}
function draw(){var g=gv(),p=pw(g);
L('Gas speed and heat plume exaggerated',20,22,11,'#5b6576','left');
pipe(20,620,250,40);L('Pipe ID 100 mm',600,316,11,'#5b6576','right',1);
var nv=Math.round(clamp(10+P.rho*12,10,70));for(var i=0;i<nv;i++){var q=gp[i],x=20+((q[0]*600+T*(P.v*14))%600),y=214+q[1]*72;ci(x,y,2.2,'#1e63b8');}
for(var i=0;i<hp.length;i++){var h=hp[i],a=Math.max(0,1-h[2]/1.6);ci(h[0],h[1],2.6,'rgba(220,38,38,'+(0.75*a)+')');}
rc(150,40,110,60,'#1a2333',null,8);L('Transmitter',205,54,11,'#cbd5e1','center',1);L('P '+m(p,3)+' W',205,74,13,'#fbbf24','center',1);L('ΔT '+m(P.dt,0)+' K',205,90,11,'#cbd5e1','center');
rc(194,100,14,128,'#94a3b8','#475569',3);rc(186,226,30,8,'#64748b',null,2);
rc(184,234,8,30,'#cbd5e1','#334155',2);var gl=0.55+0.45*Math.sin(T*7);rc(210,234,8,30,'rgba(220,38,38,'+gl+')','#7f1d1d',2);ci(214,262,7+2*gl,null,'rgba(248,113,113,0.6)',2);
ar(40,226,92,226,'#1e63b8',2.5);L('Gas '+m(P.v,1)+' m/s',40,186,11,'#1e63b8','left',1);
var gx0=330,gx1=615,gy0=50,gy1=168,gm=150,pm=pw(gm)*1.05,GX=function(x){return gx0+(gx1-gx0)*x/gm;},GY=function(v){return gy1-(gy1-gy0)*v/pm;};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();for(var x=0;x<=gm;x+=2){var yy=GY(pw(x));if(x)C.lineTo(GX(x),yy);else C.moveTo(GX(x),yy);}C.stroke();
var pr=1+0.25*Math.sin(T*6);ci(GX(Math.min(g,gm)),GY(p),5*pr,'#d9622b');ln(GX(Math.min(g,gm)),GY(p),GX(Math.min(g,gm)),gy1,'#d9622b',1,[3,3]);
L('Heater power P versus ρv',gx0,gy0-12,11,'#1e63b8','left',1);L('0',gx0,gy1+12,11,'#5b6576','left');L('150 kg/m²s',gx1,gy1+12,11,'#5b6576','right');L(m(pm,2)+' W',gx0+4,gy0+10,11,'#5b6576','left');
L('ρv '+m(g,1)+' kg/m²s',GX(Math.min(g,gm))+8,gy1-28,11,'#d9622b','left',1);
L('Mass flow '+m(g*AR*3600,0)+' kg/h',470,340,12,'#1a2333','center',1);
mk(1,272,50);mk(2,222,150);mk(3,170,262);mk(4,232,250);mk(5,60,246);mk(6,330,272);mk(7,gx1-14,gy0+14);}
"""
