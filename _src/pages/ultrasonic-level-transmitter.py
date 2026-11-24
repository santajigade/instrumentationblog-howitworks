PAGE = dict(
    slug="ultrasonic-level-transmitter", grp="Level", name="Ultrasonic Level Transmitter", kw="How an Ultrasonic Level Transmitter Works",
    title="How an Ultrasonic Level Transmitter Works: Animated Diagram",
    desc="How an ultrasonic level transmitter works, animated: a sound pulse leaves the transducer, echoes off the liquid and the time of flight gives the level.",
    h1="How an Ultrasonic Level Transmitter Works",
    hero="Move the level and the air temperature sliders. Watch the sound pulse travel down to the liquid and back, see the echo move on the echo curve and check how much error appears without temperature compensation.",
    quick="An ultrasonic level transmitter sends a short burst of sound from a transducer at the top of the tank and listens for the echo from the liquid surface. The time of flight multiplied by the speed of sound and divided by two gives the distance, and level is the reference height minus that distance.",
    intro=["Ultrasonic level measurement is non contact: only the sound pulse touches the liquid. That makes it a simple choice for water, wastewater, slurries and many chemicals in open or vented tanks.",
           "The transducer is a piezoelectric element that works as both loudspeaker and microphone. It sends a burst at an ultrasonic frequency, then switches to listening and waits for the surface echo.",
           "Sound travels through the air above the liquid, and its speed changes with air temperature. For that reason almost every ultrasonic transmitter has a built in temperature sensor and corrects the speed of sound on every reading."],
    sliders=[("l", "Liquid level", 0.5, 5.0, 2.5, 0.1, 2, "m"), ("t", "Air temperature in the tank", -20, 60, 20, 1, 0, "°C")],
    outs=[("c", "Speed of sound in air at this temperature"), ("tof", "Round trip time of flight"), ("err", "Level error if the transmitter assumed 20 °C"), ("ma", "Output for a 0 to 5 m range")],
    legend=["Transducer: piezo element sends and receives", "Built in temperature sensor", "Blanking distance (dead zone)", "Ultrasonic pulse travelling down", "Liquid surface reflects the echo", "Echo curve: transmit burst and surface echo"],
    steps=["The electronics drive the piezo transducer with a short burst of ultrasonic sound aimed straight down at the liquid.",
           "The transducer rings for a short time after the burst, so echoes from inside the blanking distance cannot be read.",
           "The pulse spreads in a narrow cone, reflects at the liquid surface and returns to the transducer, which now acts as a receiver.",
           "The transmitter finds the surface echo on its echo curve, measures the time of flight and corrects the speed of sound with the measured air temperature.",
           "Distance is converted to level, and level is sent as 4 to 20 mA, HART or a fieldbus value, often with volume or open channel flow calculated in the transmitter."],
    formula=["Distance d = c × t ÷ 2, where t is the round trip time of flight",
             "Speed of sound in air c = 331.3 × √(1 + T ÷ 273.15) m/s, with T in °C",
             "Level = H − d, where H is the distance from the transducer face to 0 %",
             "Output = 4 + 16 × level ÷ span mA",
             "Example: H 6 m, level 2.50 m, 20 °C: c = 343.2 m/s, d = 3.50 m, t = 7.00 ÷ 343.2 = 20.40 ms, output 12.00 mA; if the air is at 40 °C but the transmitter assumes 20 °C, it reads 2.614 m, an error of 0.114 m"],
    parts=[("Piezo transducer", "Sends the ultrasonic burst and receives the echo through the same face"),
           ("Temperature sensor", "Measures the air temperature near the transducer for speed of sound correction"),
           ("Signal processing", "Builds the echo curve, rejects false echoes and picks the true surface"),
           ("Blanking distance setting", "Ignores the zone just below the face where the transducer is still ringing"),
           ("Output stage", "Gives 4 to 20 mA, relays or digital communication to the PLC or DCS")],
    uses=[("Water and wastewater", "Wet wells, sumps, clarifiers and reservoirs where non contact sensing avoids fouling."),
          ("Open channel flow", "Level over a flume or weir is converted to flow inside the transmitter."),
          ("Chemical storage", "Vented tanks of acids, alkalis and other liquids that would attack a probe."),
          ("Bulk solids", "Bins and hoppers with coarse material, using a low frequency transducer.")],
    pros=["Non contact, so no wetted parts and nothing to coat or corrode", "Simple to install on top of open or vented tanks", "Built in calculations for volume and open channel flow"],
    cons=["Foam, heavy vapour, dust or a turbulent surface can absorb or scatter the echo", "Cannot work in vacuum and is affected by gases other than air", "Blanking distance means the highest level must stay below the face by a set margin"],
    tips=["Mount the transducer away from the tank wall, inlet streams and ladders so the beam cone sees only the liquid surface.",
          "Keep the maximum level below the blanking distance, or use a standpipe or extension nozzle to raise the transducer.",
          "Shade the transducer from direct sun, because heating at the face makes the internal temperature reading differ from the air in the tank.",
          "Run a false echo map with the tank empty or low, so fixed objects inside the beam are suppressed."],
    faq=[("Why does an ultrasonic level transmitter need temperature compensation?", "The speed of sound in air rises by about 0.6 m/s for each °C. Without correction a 20 °C change gives an error of a few percent of the measured distance."),
         ("What is the blanking distance?", "After sending the burst the transducer keeps vibrating for a short time and cannot hear echoes. Any surface closer than this distance is not measured, so the 100 % level must be set below it."),
         ("Can an ultrasonic transmitter measure through foam?", "Thick or soft foam absorbs sound and may give no echo or an echo from the foam top. Radar or guided wave radar is usually a better choice for foaming liquids."),
         ("What is the difference between ultrasonic and radar level?", "Ultrasonic uses sound waves that need air or gas to travel and depend on temperature. Radar uses microwaves that are not affected by vapour temperature or pressure in the same way and also work in vacuum.")],
    cal=[("level/ultrasonic-level-calculator", "Ultrasonic Level Calculator"), ("level/tank-ullage-calculator", "Tank Ullage Calculator")],
    glo=[("ultrasonic-level-transmitter", "Ultrasonic Level Transmitter"), ("false-echo-suppression", "False Echo Suppression")],
    cmp=[("radar-vs-ultrasonic-level-transmitter", "Radar vs Ultrasonic Level Transmitter")],
    tool=[("tools/troubleshooting/level-transmitter-fault-finder", "Level Transmitter Fault Finder")],
    blog=("ultrasonic-level-transmitter-working", "Ultrasonic level transmitter working"))

SCENE = r"""
var tc=0,HT=6,YT=78,SC=38,BL=0.3,CX=225;
function cs(t){return 331.3*Math.sqrt(1+t/273.15);}
function dd(){return HT-P.l;}
function tof(){return 2*dd()/cs(P.t);}
function upd(){var d=dd(),dr=d*cs(20)/cs(P.t),e=(HT-dr)-P.l;o('c',m(cs(P.t),1)+' m/s');o('tof',m(tof()*1000,2)+' ms (d = '+m(d,2)+' m)');o('err',(e>=0.0005?'+':'')+m(e,3)+' m');o('ma',m(P.l,2)+' m = '+m(4+16*P.l/5,2)+' mA');}
function step(dt){var t1=dd()*SC/150;tc=(tc+dt)%(2*t1+0.35);}
function wf(y,dir,col,a){var w=12+(y-YT)*0.22;C.globalAlpha=a;C.strokeStyle=col;C.lineWidth=2.5;for(var k=0;k<3;k++){var yy=y-dir*k*7;C.beginPath();C.moveTo(CX-w,yy-dir*5);C.quadraticCurveTo(CX,yy+dir*7,CX+w,yy-dir*5);C.stroke();}C.globalAlpha=1;}
function draw(){var ys=YT+dd()*SC,yb=YT+HT*SC,yB=YT+BL*SC;
L('Pulse travel slowed down for viewing; reference height 6 m',20,22,11,'#5b6576','left');
rc(120,YT,210,yb-YT,'#f8fafc','#475569',4);wave(122,328,ys,yb-2,'rgba(147,197,253,0.85)');
rc(120,YT,210,yB-YT,'rgba(251,191,36,0.25)');ln(120,yB,330,yB,'#b45309',1,[4,3]);L('blanking',318,yB-5,11,'#92400e','right');
rc(195,44,60,30,'#1a2333',null,6);L('ULT',225,59,11,'#fff','center',1);rc(203,74,44,6,'#64748b',null,2);ci(255,52,5,'#ef4444','#fff',1.5);
L(m(P.t,0)+' °C',268,40,11,'#b91c1c','left',1);
var bw=12+(ys-YT)*0.22;ln(CX-12,YT+2,CX-bw,ys,'#94a3b8',1,[3,4]);ln(CX+12,YT+2,CX+bw,ys,'#94a3b8',1,[3,4]);
var v=150,t1=(ys-YT)/v,t=tc;if(t<t1)wf(YT+6+v*t,1,'#7c3aed',1);else{var yr=ys-v*(t-t1);if(yr>YT+6)wf(yr,-1,'#d9622b',0.9);}
ln(345,YT,345,ys,'#1a2333',1,[4,3]);ar(345,YT+4,345,ys-2,'#1a2333',1.2);L('d',352,(YT+ys)/2,13,'#1a2333','left',1);
ln(335,yb,345,yb,'#1a2333',1);L('0 %',350,yb-2,11,'#5b6576','left');
var X0=392,X1=624,Y0=92,Y1=262,B=240,TM=0.04,X=function(s){return X0+10+s/TM*(X1-X0-20);};
rc(X0,Y0,X1-X0,Y1-Y0,'#f6f8fc','#dde3ee',6);L('Echo curve',X0,Y0-12,11,'#5b6576','left',1);
ln(X(0),B,X(TM),B,'#94a3b8',1);for(var k=0;k<=4;k++){var s=k*0.01;ln(X(s),B,X(s),B+4,'#94a3b8',1);L(k*10+' ms',X(s),B+13,11,'#5b6576','center');}
var tb=2*BL/cs(P.t),te=tof();ln(X(tb),Y0+6,X(tb),B,'#b45309',1,[3,3]);
C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();for(var x=X(0);x<=X(TM);x+=1.5){var s=(x-X0-10)/(X1-X0-20)*TM,a=110*Math.exp(-Math.pow(s/(tb*0.6),2))+70*Math.exp(-Math.pow((s-te)/0.0007,2))+2*Math.sin(x*1.3+T*9);var y=B-a;if(x==X(0))C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
L('Transmit burst',X(0)+14,Y0+20,11,'#1a2333','left',1);L('Surface echo',X(te),B-80,11,'#1e3a8a','center',1);L(m(te*1000,2)+' ms',X(te),B-94,11,'#1e3a8a','center');
if(t<2*t1)ln(X(te*t/(2*t1)),Y0+4,X(te*t/(2*t1)),B,'#7c3aed',1.5);
rc(X0,288,X1-X0,40,'#1a2333',null,6);L('Level '+m(P.l,2)+' m',X0+12,308,13,'#fff','left',1);L(m(4+16*P.l/5,2)+' mA',X1-12,308,13,'#fbbf24','right',1);
mk(1,180,59);mk(2,284,58);mk(3,140,(YT+yB)/2+2);mk(4,CX-bw-16,Math.min(ys-24,YT+60));mk(5,300,ys+16);mk(6,X1-14,Y0+20);}
"""
