PAGE = dict(
    slug="temperature-switch", grp="Switches", name="Bimetal Temperature Switch", kw="How a Bimetal Temperature Switch Works",
    title="How a Bimetal Temperature Switch Works: Diagram and Formula",
    desc="How a bimetal temperature switch works, animated: the strip bends as it heats, opens the heater contact at the set point and recloses it below the differential.",
    h1="How a Bimetal Temperature Switch Works",
    hero="Move the set point and the differential and watch the water tank cycle between the two. Change the strip length to see how much the bimetal tip moves for every degree.",
    quick="A bimetal temperature switch uses two metals with different expansion bonded into one strip. As the temperature rises the strip bends, and at the set point it moves a contact that switches a heater, fan or alarm.",
    intro=["Metals grow when heated, but not all by the same amount. Brass grows roughly fifteen times more than invar for the same temperature rise, so a strip made of the two bonded together must curl toward the invar side.",
           "A bimetal temperature switch turns that curl into a contact movement. An adjusting screw sets how far the strip must travel, and a snap mechanism makes the contact jump cleanly open and shut.",
           "These switches need no power and switch the load directly, which is why they are found in water heaters, motors, panels and overheat cut outs. Knowing the set point, the differential and the contact rating is enough to apply most of them correctly."],
    sliders=[("sp", "Set point (contact opens on rising temperature)", 40, 120, 70, 1, 0, "°C"), ("df", "Differential", 2, 15, 5, 1, 0, "°C"), ("L", "Free strip length L (thickness t 0.5 mm)", 20, 60, 40, 1, 0, "mm")],
    outs=[("k", "Tip movement per °C, 3 × Δα × L² ÷ (4 × t)"), ("g", "Contact travel from 20 °C to the set point"), ("rs", "Reset point (contact closes on falling temperature)"), ("st", "Contact now")],
    legend=["Water tank with immersion heater", "Bimetal strip: brass bonded to invar", "Contacts: closed when cold, open on rising temperature", "Set point adjusting screw", "Heater circuit state, set and reset points", "Trend: temperature with set and reset lines"],
    steps=["The sensing element sits in a thermowell or against the surface, and reaches the process temperature.",
           "The brass layer expands more than the invar layer, so the bonded strip bends toward the invar side.",
           "The tip carries a moving contact that rests on a fixed contact while the strip is cool.",
           "At the set point the strip has moved far enough to lift the contact, and a snap mechanism opens it quickly to cut the heater.",
           "As the process cools the strip straightens, and the contact recloses at the set point minus the differential."],
    formula=["Tip deflection d = 3 × Δα × ΔT × L² ÷ (4 × t), for two layers of equal thickness and stiffness",
             "Δα is the difference in expansion coefficients, about 17 × 10⁻⁶ per °C for brass on invar",
             "The contact opens when d reaches the travel set by the adjusting screw",
             "Reset point = set point − differential",
             "Example: L 40 mm and t 0.5 mm give 3 × 0.000017 × 1600 ÷ 2 = 0.0408 mm per °C, so a 70 °C set point needs 2.04 mm of travel from 20 °C and the switch resets at 65 °C"],
    parts=[("Bimetal element", "A flat strip, coil, spiral or snap disc made of two bonded metals with different expansion"),
           ("Contacts", "Moving and fixed contacts, often silver alloy, wired as normally closed or normally open"),
           ("Adjusting screw or knob", "Moves the fixed contact or preloads the strip to change the set point"),
           ("Snap mechanism", "A small magnet or a domed snap disc that makes the contact jump and sets the differential"),
           ("Housing and well", "Protects the element and lets it be removed without draining the process")],
    uses=[("Water heaters and tanks", "Cut the heater at the set point and switch it back on as the water cools."),
          ("Motor and transformer protection", "Thermal cut outs in windings open the control circuit on overheating."),
          ("Panel climate", "Switch panel heaters on in cold weather and cooling fans on in hot weather."),
          ("Overheat cut outs", "Manual reset safety cut outs on heaters, dryers and boilers.")],
    pros=["Needs no power supply and switches the load directly", "Simple, robust and low cost", "Snap action gives a clear on off signal with little contact chatter"],
    cons=["Lower set point accuracy and repeatability than a transmitter with a trip", "Slow response, especially inside a thick thermowell", "Contacts wear and have a limited current rating"],
    tips=["Check the contact rating against the real load; use the switch to drive a contactor for large heaters or inductive loads.",
          "Do not set the differential so small that the load cycles every few seconds; frequent switching shortens contact life.",
          "Verify the set point in a calibrated bath with the switch in its own well, rising slowly, and note both the trip and the reset temperature.",
          "Use heat transfer paste in the thermowell if the maker allows it, to cut the response time."],
    faq=[("What is the differential of a temperature switch?", "It is the gap between the temperature where the contact operates on rising temperature and where it resets on falling temperature. It stops the contact from chattering when the temperature hovers near the set point."),
         ("Why does the strip bend instead of just getting longer?", "Both layers are bonded along their full length, so the layer that expands more is forced to sit on the outside of a curve. The strip curls toward the layer with the lower expansion."),
         ("What is the difference between a strip and a snap disc?", "A strip moves gradually with temperature and needs a magnet or toggle for clean switching. A domed snap disc flips over suddenly at its rated temperature, which gives built in snap action and a fixed differential."),
         ("Should I use a temperature switch or a transmitter?", "A switch is cheaper and needs no power for a simple on off job. A transmitter gives a live value, diagnostics and an adjustable trip, which is usually preferred for control and safety functions.")],
    cal=[("temperature/thermal-expansion-calculator", "Thermal Expansion Calculator"), ("temperature/sensor-response-time-calculator", "Sensor Response Time Calculator")],
    glo=[("bimetallic-thermometer", "Bimetallic Thermometer"), ("hysteresis", "Hysteresis")],
    cmp=[],
    tool=[("tools/practice-tests/temperature-measurement-quiz", "Temperature Measurement Quiz")],
    blog=("temperature-switch-vs-temperature-transmitter", "Temperature switch vs temperature transmitter"))

SCENE = r"""
var tp=50,on=true,hist=[],pre=0,bub=[];for(var i=0;i<26;i++)bub.push([Math.random(),Math.random()]);
function kk(){return 3*17e-6*P.L*P.L/(4*0.5);}
function rs(){return P.sp-P.df;}
function upd(){if(!pre){pre=1;tp=rs()-2;for(var q=0;q<300;q++){T+=0.04;step(0.04);}}o('k',m(kk(),4)+' mm per °C');o('g',m(kk()*(P.sp-20),2)+' mm');o('rs',m(rs(),0)+' °C');o('st',on?'Closed: heater ON':'Open: heater OFF');}
function step(dt){tp+=(on?3.0:-(tp-20)*0.04-0.5)*dt;var w=on;if(on&&tp>=P.sp)on=false;else if(!on&&tp<=rs())on=true;if(w!==on)upd();
hist.push([T,tp]);while(hist.length&&T-hist[0][0]>20)hist.shift();}
function draw(){
L('Strip bending exaggerated; heating cycle sped up',20,22,11,'#5b6576','left');
var hot=clamp((tp-20)/110,0,1);rc(30,70,170,230,'#e2e8f0','#475569',12);
wave(36,194,112,294,'#bfdbfe');
rc(110,46,14,170,'#cbd5e1','#475569',4);L('Thermowell',130,58,11,'#5b6576','left');
var hc=on?'#ef4444':'#64748b';C.strokeStyle=hc;C.lineWidth=on?4:3;C.beginPath();C.moveTo(30,262);for(var k=0;k<=8;k++)C.lineTo(48+k*16,k%2?250:274);C.lineTo(190,262);C.stroke();
if(on){for(var i=0;i<bub.length;i++){var b=bub[i],y=274-((T*40+b[1]*180)%160);ci(48+b[0]*140,y,2.5,'rgba(255,255,255,0.9)','#93c5fd',1);}}
rc(136,128,58,24,'rgba(255,255,255,0.92)','#94a3b8',5);L(m(tp,1)+' °C',165,140,12,'#b91c1c','center',1);
L('Heater '+(on?'ON':'OFF'),115,288,11,on?'#b91c1c':'#475569','center',1);L('Water tank',115,316,12,'#1a2333','center',1);
ln(124,60,230,150,'#94a3b8',1,[3,3]);
rc(230,40,270,200,'#f8fafc','#cbd5e1',8);L('Switch close up',240,54,11,'#5b6576','left',1);
var S=Math.min(14,45/Math.max(0.1,kk()*(P.sp-20))),gap=kk()*(P.sp-20)*S,y0=200,yc=y0-gap,tip=on?yc:yc-10;
rc(250,182,30,40,'#475569',null,3);
for(var ly=0;ly<2;ly++){C.strokeStyle=ly?'#ea580c':'#94a3b8';C.lineWidth=4;C.beginPath();for(var s=0;s<=1.0001;s+=0.05){var x=280+150*s,y=tip+(y0-tip)*(1-s*s)+(ly?4:0);if(s)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();}
L('Invar layer',290,140,11,'#475569','left',1);L('Brass layer',290,230,11,'#c2410c','left',1);

rc(424,tip-2,12,6,'#f59e0b','#92400e',2);rc(424,yc+4,12,6,'#cbd5e1','#475569',2);
rc(426,yc+10,8,Math.max(4,226-yc),'#a8620a','#4a2a04',2);for(var yy=yc+14;yy<234;yy+=6)ln(426,yy,434,yy+3,'#4a2a04',1);rc(420,232,20,6,'#4a2a04');
L('Set screw',446,226,11,'#a8620a','left',1);
L(on?'Contacts closed':'Contacts open, heater cut',365,80,12,on?'#16a34a':'#b91c1c','center',1);
rc(510,40,120,124,'#1a2333',null,8);L('Heater circuit',522,54,11,'#cbd5e1','left',1);ci(538,88,12,on?'#f97316':'#334155','#94a3b8',2);
if(on){var g=0.5+0.5*Math.sin(T*8);ci(538,88,16+3*g,null,'rgba(251,146,60,0.7)',2);}L(on?'ON':'OFF',558,88,12,'#fff','left',1);
L('Opens at '+m(P.sp,0)+' °C',570,122,11,'#fde68a','center',1);L('Closes at '+m(rs(),0)+' °C',570,144,11,'#bfdbfe','center',1);
var gx0=270,gx1=620,gy0=262,gy1=340,TY=function(v){return gy1-(v-20)/110*(gy1-gy0);},TX=function(t){return gx1-(T-t)/20*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');ln(gx0,TY(P.sp),gx1,TY(P.sp),'#b91c1c',1,[4,4]);ln(gx0,TY(rs()),gx1,TY(rs()),'#16a34a',1,[4,4]);
L('set '+m(P.sp,0),gx0+6,TY(P.sp)-8,11,'#b91c1c','left');L('reset '+m(rs(),0),gx0+6,TY(rs())+9,11,'#16a34a','left');
L('130',gx0-4,gy0,11,'#5b6576','right');L('20',gx0-4,gy1,11,'#5b6576','right');
C.strokeStyle='#dc2626';C.lineWidth=2;C.beginPath();hist.forEach(function(q,i){var x=TX(q[0]),y=TY(q[1]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
L('Temperature, °C',gx0,gy0-10,11,'#dc2626','left',1);L('last 20 s',gx1,gy0-10,11,'#5b6576','right');
mk(1,40,80);mk(2,355,166);mk(3,452,yc+2);mk(4,412,226);mk(5,618,52);mk(6,gx1-16,gy1-14);}
"""
