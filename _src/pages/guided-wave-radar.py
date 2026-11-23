PAGE = dict(
    slug="guided-wave-radar", grp="Level", name="Guided Wave Radar Level Transmitter", kw="How a Guided Wave Radar Level Transmitter Works",
    title="How a Guided Wave Radar Level Transmitter Works: Animated Diagram",
    desc="How a guided wave radar level transmitter works, animated: a pulse runs down the probe, reflects at the surface and the echo curve gives the level.",
    h1="How a Guided Wave Radar Level Transmitter Works",
    hero="Move the level and the dielectric constant sliders. Watch the pulse travel down the probe, see how strong the surface echo is and where the end of probe echo appears.",
    quick="A guided wave radar (GWR) transmitter sends very short microwave pulses down a rod, cable or coaxial probe. At the liquid surface the impedance changes, part of the pulse reflects, and the time of flight gives the distance; level is the reference height minus that distance.",
    intro=["Guided wave radar uses time domain reflectometry, the same method used to find faults in long cables. The probe guides the pulse, so the signal stays strong even in narrow nozzles, foam, vapour or tanks with internal obstructions.",
           "The pulse travels at nearly the speed of light in the vapour space and returns in a few tens of nanoseconds. The transmitter samples many pulses to build an echo curve, then finds the surface echo on that curve.",
           "How much of the pulse reflects depends on the dielectric constant of the liquid. Water gives a large echo, while oils and solvents give a small one, and part of the pulse then continues down to the end of the probe."],
    sliders=[("l", "Liquid level", 0.5, 5.5, 3.0, 0.1, 2, "m"), ("er", "Liquid dielectric constant εr", 1.5, 80, 2.0, 0.5, 1, "")],
    outs=[("d", "Distance flange to surface"), ("tof", "Round trip time of flight"), ("g", "Surface echo amplitude"), ("eop", "End of probe appears at")],
    legend=["Transmitter head and electronics", "Process connection: zero distance reference", "Single rod probe with end weight", "Transmitted pulse",
            "Liquid surface", "Surface echo (inverted) on the echo curve", "End of probe echo"],
    steps=["The electronics generate a pulse about a nanosecond long and launch it into the probe at the process connection.",
           "The pulse travels down the probe through the vapour at almost the speed of light.",
           "At the liquid surface the probe impedance falls, so part of the energy reflects back as an inverted echo.",
           "The transmitter measures the time between the reference pulse and the surface echo and converts it to distance.",
           "Level is the reference height minus the distance, scaled to 4 to 20 mA or sent over HART or a fieldbus."],
    formula=["Distance d = c × t ÷ 2, with c = 299 792 458 m/s in air",
             "Level = H − d, where H is the reference height from the flange to 0 %",
             "Reflection amplitude ≈ (√εr − 1) ÷ (√εr + 1)",
             "In the liquid the pulse slows to c ÷ √εr, so the end of probe appears at d + level × √εr",
             "Example: H 6 m, level 3.00 m gives d 3.00 m and t 20.0 ns; with εr 2.0 the echo is 17.2 % and the probe end appears at 7.24 m"],
    parts=[("Electronics head", "Generates the pulses, samples the echoes and computes level"),
           ("Process connection", "Flange or thread that seals the tank and acts as the zero reference"),
           ("Probe", "Single rod, twin rod, cable or coaxial waveguide that guides the pulse"),
           ("End weight or centring disc", "Keeps a cable probe straight or a rod probe away from the wall"),
           ("Echo processing", "Threshold, blocking distance and echo tracking settings that pick the true surface")],
    uses=[("Storage and process tanks", "Level of water, chemicals, oils and solvents, even with vapour or foam."),
          ("Interface measurement", "Oil and water interface in separators, using the second echo at the interface."),
          ("Bridles and chambers", "Direct replacement for displacers in external cages."),
          ("Low dielectric liquids", "Coaxial probes keep enough signal for liquefied gases and light hydrocarbons.")],
    pros=["No moving parts and no recalibration for density changes", "Works in vapour, foam, dust and turbulent surfaces", "Probe guided energy handles narrow nozzles and obstructions"],
    cons=["The probe contacts the process, so coating and buildup can cause false echoes", "Long cable probes need anchoring and can be stressed in agitated tanks", "Very low dielectric liquids give weak echoes and may need a coaxial probe"],
    tips=["Enter the correct probe length and confirm the end of probe echo on the echo curve during commissioning.",
          "Keep a single rod probe away from the tank wall, ladders and inlet streams, or use a coaxial or twin probe.",
          "Check the blocking distance near the flange; do not set the 100 % point inside it.",
          "Save an echo curve when the transmitter reads correctly, so you can compare it during later troubleshooting."],
    faq=[("How is guided wave radar different from non contact radar?", "GWR guides the pulse along a probe in contact with the liquid, while non contact radar radiates it from an antenna. The guided signal loses less energy, so GWR handles low dielectric liquids, foam and obstructions better."),
         ("Why is the surface echo inverted?", "The liquid raises the dielectric around the probe, which lowers its impedance. A step down in impedance reflects a pulse of opposite polarity."),
         ("What is end of probe tracking?", "Below the surface the pulse travels slower, so the probe end appears further away than it really is. The shift depends on level and dielectric constant, and the transmitter can use it to estimate level when the surface echo is weak."),
         ("Does density or temperature affect GWR?", "No direct effect, because the reading is a time of flight. Only very high pressure or dense vapour can slightly slow the pulse, which some transmitters compensate.")],
    cal=[("level/radar-level-calculator", "Radar Level Calculator"), ("level/radar-level-dielectric-calculator", "Radar Level Dielectric Calculator")],
    glo=[("guided-wave-radar", "Guided Wave Radar"), ("dielectric-constant", "Dielectric Constant"), ("blocking-distance", "Blocking Distance")],
    cmp=[("displacer-vs-guided-wave-radar", "Displacer vs Guided Wave Radar"), ("radar-vs-ultrasonic-level-transmitter", "Radar vs Ultrasonic Level Transmitter")],
    tool=[("tools/troubleshooting/guided-wave-radar-fault-finder", "Guided Wave Radar Fault Finder")],
    blog=("guided-wave-radar-level-transmitter", "Guided wave radar level transmitter"))

SCENE = r"""
var tc=0,HT=6,YT=90,SC=40;
function se(){return Math.sqrt(P.er);}
function gm(){var s=se();return (s-1)/(s+1);}
function dd(){return HT-P.l;}
function ep(){return dd()+P.l*se();}
function upd(){o('d',m(dd(),2)+' m');o('tof',m(2*dd()/299792458*1e9,1)+' ns');o('g',m(gm()*100,1)+' % (inverted)');o('eop',m(ep(),2)+' m (true 6.00 m)');}
function step(dt){tc=(tc+dt)%2.6;}
function pulse(y,col,a,up){var g=C.createLinearGradient(0,y-14,0,y+14);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(0.5,col);g.addColorStop(1,'rgba(0,0,0,0)');C.globalAlpha=a;C.fillStyle=g;C.fillRect(226,y-14,28,28);C.globalAlpha=1;ar(268,up?y+8:y-8,268,up?y-8:y+8,col,2);}
function draw(){var px=240,ys=YT+dd()*SC,yb=YT+HT*SC;
L('Pulse travel slowed down for viewing; probe 6 m long',20,22,11,'#5b6576','left');
rc(150,YT,180,yb-YT,'#f8fafc','#475569',4);wave(152,328,ys,yb-2,'rgba(147,197,253,0.85)');
rc(205,YT-8,70,8,'#64748b');rc(222,30,36,52,'#1a2333',null,6);L('GWR',240,48,11,'#fff','center',1);rc(232,82,16,8,'#475569');
ln(px,YT,px,yb-12,'#334155',4);rc(px-6,yb-14,12,12,'#334155',null,2);
var v=300,t1=(ys-YT)/v,t=tc,a=gm();
if(t<t1)pulse(YT+v*t,'rgba(124,58,237,0.95)',1,0);
else{var yr=ys-v*(t-t1);if(yr>YT)pulse(yr,'rgba(217,98,43,0.95)',0.35+0.65*a,1);var yt=ys+v/se()*(t-t1);if(yt<yb-12)pulse(yt,'rgba(124,58,237,0.95)',Math.max(0.25,1-a),0);}
ln(345,YT,345,ys,'#1a2333',1,[4,3]);ar(345,YT+4,345,ys-2,'#1a2333',1.2);L('d',352,(YT+ys)/2,13,'#1a2333','left',1);
ln(335,yb,345,yb,'#1a2333',1);L('0 %',338,yb+12,11,'#5b6576','left');
var X0=400,X1=630,bx=478,S2=30,Y=function(q){return YT+q*S2;};rc(X0,YT,X1-X0,8*S2,'#f6f8fc','#dde3ee',6);L('Echo curve',X0+4,YT-12,11,'#5b6576','left',1);
ln(bx,YT,bx,YT+8*S2,'#cbd5e1',1);for(var k=0;k<=8;k+=2)L(k+' m',X1-4,Y(k)+(k==8?-6:6),11,'#5b6576','right');
ln(X0,Y(HT),X1,Y(HT),'#94a3b8',1,[3,3]);L("true end",X0+4,Y(HT)-7,11,'#5b6576','left');
C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();for(var y=Y(0)+1;y<=Y(8)-1;y+=1.5){var q=(y-YT)/S2,am=0.85*Math.exp(-Math.pow(q/0.18,2))-a*Math.exp(-Math.pow((q-dd())/0.14,2))+0.75*(1-a)*Math.exp(-Math.pow((q-ep())/0.18,2));var x=bx+am*80;if(y==Y(0)+1)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
var ey=Y(dd()),eo=ep()<7.8;L('Surface',bx+32,ey+10,11,'#1e3a8a','left',1);if(eo)L('End of probe',bx+0.75*(1-a)*80+6,Y(ep()),11,'#334155','left',1);else L('End of probe beyond 8 m',bx+6,Y(7.2),11,'#334155','left',1);
mk(1,276,40);mk(2,192,YT-4);mk(3,px+20,yb-24);mk(4,214,YT+20);mk(5,312,ys-14);mk(6,bx+16,ey+10);mk(7,eo?Math.min(X1-14,bx+0.75*(1-a)*80+14):bx-14,eo?Y(ep())+18:Y(7.2));}
"""
