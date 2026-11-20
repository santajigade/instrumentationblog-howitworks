PAGE = dict(
    slug="float-level-switch", grp="Switches", name="Float Level Switch", kw="How a Float Level Switch Works",
    title="How a Float Level Switch Works: Animated Diagram and Buoyancy",
    desc="How a float level switch works, animated: the float rides the liquid, its magnet operates a reed switch in the stem and the switch point moves with density.",
    h1="How a Float Level Switch Works",
    hero="Change the liquid specific gravity and the float mass. Watch how deep the float sinks, where the reed contact changes over as the tank fills and when a light liquid can no longer lift the float.",
    quick="A float level switch uses a buoyant float that rises and falls with the liquid surface. A magnet inside the float moves along a sealed stem and operates a reed switch at a fixed height, so the contact changes over when the level reaches that point.",
    intro=["A float level switch is one of the simplest point level devices in a plant. It is used for high and low level alarms, pump start and stop and overflow protection in sumps, day tanks and lube oil reservoirs.",
           "The most common industrial design is a vertical stem with a ring float. The float carries a permanent magnet, and a hermetically sealed reed switch inside the stem changes over when the magnet reaches it.",
           "The float sinks into the liquid until the displaced liquid weighs as much as the float. That immersion depth depends on density, so the actual switching level shifts when the liquid is lighter or heavier than water."],
    sliders=[("sg", "Liquid specific gravity", 0.5, 1.4, 1.0, 0.05, 2, ""), ("m", "Float mass", 20, 90, 50, 1, 0, "g")],
    outs=[("h", "Immersion depth h = m ÷ (ρ × A)"), ("sw", "Level at switch point, rising (reed at 150 mm)"), ("lift", "Spare lift when fully submerged"), ("st", "Reed contact now")],
    legend=["Ring float with magnet", "Reed switch sealed inside the stem", "Stop collars that limit float travel", "Liquid level", "Switch output to PLC or alarm", "Immersion depth h of the float", "Trend: level and contact state"],
    steps=["Liquid enters the tank and the level rises towards the float.",
           "Once the float is wetted it sinks in only to its immersion depth, where buoyancy equals its weight, and then rises with the surface.",
           "The magnet inside the float moves up the stem towards the reed switch.",
           "When the magnet reaches the reed, the magnetic field pulls the reed blades together and the contact changes over, giving a high level signal.",
           "As the level falls the float follows it down, the magnet moves away and the reed contact returns to its rest state."],
    formula=["Immersion depth h = m ÷ (ρ × A), where A is the float cross section area",
             "Float floats only if m < ρ × V, where V is the total float volume",
             "Switching level = reed height + (h − distance from float bottom to magnet)",
             "Spare lift when submerged = ρ × V − m",
             "Example: float 50 mm diameter and 50 mm high, A = 19.63 cm², V = 98.2 cm³, m 50 g in water: h = 50 ÷ (1.0 × 19.63) = 2.55 cm = 25.5 mm, switch level = 150 + 25.5 − 25 = 150.5 mm, spare lift = 98.2 − 50 = 48.2 g"],
    parts=[("Float", "Hollow ring or ball of stainless steel or plastic that floats on the liquid"),
           ("Permanent magnet", "Fixed inside the float so it moves with the level"),
           ("Reed switch", "Glass sealed contact inside the stem, operated by the magnet without any mechanical link"),
           ("Stem", "Non magnetic tube that guides the float and protects the reed and wiring"),
           ("Stop collars", "Clips on the stem that limit float travel around the switch point")],
    uses=[("Pump control", "Starts and stops sump and transfer pumps at set levels."),
          ("High level alarm", "Warns the operator before a tank overflows."),
          ("Low level protection", "Stops a pump before it runs dry."),
          ("Lube and hydraulic oil tanks", "Confirms that the reservoir has enough oil for the machine.")],
    pros=["Simple, low cost and easy to test by lifting the float", "Needs no power for the reed contact itself", "Works on most clean liquids regardless of colour or conductivity"],
    cons=["Switch point shifts with liquid density", "Sticky, viscous or dirty liquids can jam the float on the stem", "Reed contacts have a low current rating and need care with inductive loads"],
    tips=["Check the minimum specific gravity on the float datasheet against the lightest liquid the tank will ever hold.",
          "Use an interposing relay when the reed contact drives a contactor coil or other inductive load.",
          "Keep the float away from the inlet stream and agitator; turbulence makes the contact chatter.",
          "Test the switch by raising the level or lifting the float and confirm the alarm in the control room, not only at the terminal."],
    faq=[("Why does the switch point change with a different liquid?", "The float sinks deeper in a lighter liquid to displace the same weight. The magnet then reaches the reed at a higher liquid level."),
         ("Can a float switch work in oil?", "Yes, if the float is light enough. The float mass must be less than the oil density times the float volume, with some spare lift."),
         ("What is the difference between NO and NC in a float switch?", "It depends on whether the contact is described with the float at its lowest or highest position. Always check the datasheet and the mounting direction, because turning the stem upside down reverses the logic."),
         ("Why use a reed switch instead of a mechanical contact?", "The reed is sealed in glass inside the stem, so the liquid never touches the contact. The magnet operates it through the stem wall.")],
    cal=[("level/float-buoyancy-calculator", "Float Buoyancy Calculator"), ("level/sump-pump-cycle-time-calculator", "Sump Pump Cycle Time Calculator")],
    glo=[("float-level-switch", "Float Level Switch"), ("point-level-measurement", "Point Level Measurement")],
    cmp=[("float-switch-vs-vibrating-fork", "Float Switch vs Vibrating Fork")],
    tool=[("tools/practice-tests/level-measurement-quiz", "Level Measurement Quiz")],
    blog=("float-level-switch-working-principle-and-applications", "Float level switch working principle and applications"))

SCENE = r"""
var AR=19.635,VOL=98.17,ZR=150,BL=100,BH=160,sw=false,lvl=150,hist=[];
function hmm(){return P.m/(P.sg*AR)*10;}
function Y(mm){return 330-mm*0.9;}
var pre=0;function upd(){if(!pre){pre=1;for(var q=0;q<500;q++){T+=0.04;step(0.04);}}var h=hmm();o('h',m(h,1)+' mm');o('sw',h>=50?'Float sinks, never switches':m(ZR+h-25,1)+' mm');var sp=VOL*P.sg-P.m;o('lift',sp>0?m(sp,1)+' g':'None: float sinks');o('st',sw?'Closed (high level)':'Open');}
function fbot(){var h=hmm();if(h>=50)return BL;return clamp(lvl-h,BL,BH);}
function step(dt){lvl=150+108*Math.sin(2*Math.PI*T/16);var mc=fbot()+25;var w=sw;if(!sw&&mc>=ZR)sw=true;else if(sw&&mc<ZR-3)sw=false;if(w!==sw)upd();
hist.push([T,lvl,sw]);while(hist.length&&T-hist[0][0]>20)hist.shift();}
function draw(){var h=hmm(),fb=fbot(),sx=150,rise=Math.cos(2*Math.PI*T/16)>0;
L('Level cycle sped up; float, stem and collars drawn to scale',20,22,11,'#5b6576','left');
rc(46,60,208,274,'#e2e8f0','#64748b',6);rc(52,66,196,264,'#f8fafc');
wave(52,248,Y(lvl),330,'rgba(147,197,253,0.85)');
if(rise){stream(82,52,Y(lvl));L('Filling',82,46,11,'#1e63b8','center',1);}else{ar(240,322,290,322,'#1e63b8',3);L('Draining',236,344,11,'#1e63b8','right',1);}
ln(sx,50,sx,330,'#64748b',6);rc(sx-14,42,28,12,'#475569',null,3);
rc(sx-10,Y(BL)-1,20,6,'#334155');rc(sx-10,Y(BH+50)-5,20,6,'#334155');
var ry=Y(ZR);rc(sx-3,ry-12,6,24,sw?'#bbf7d0':'#e0f2fe','#0369a1');ln(sx,ry-12,sx,ry-2+(sw?2:0),'#0f172a',1.5);ln(sx,ry+12,sx,ry+2,'#0f172a',1.5);
var ft=Y(fb+50),fbt=Y(fb);rc(sx-22,ft,44,fbt-ft,'rgba(203,213,225,0.82)','#334155',6);
var my=Y(fb+25);rc(sx-18,my-4,10,8,'#b91c1c');rc(sx+8,my-4,10,8,'#b91c1c');L('N',sx-13,my,11,'#fff','center',1);L('S',sx+13,my,11,'#fff','center',1);
if(h<50&&lvl>fb&&lvl<fb+50){ln(sx+28,fbt,sx+28,Y(lvl),'#d9622b',2);ln(sx+24,fbt,sx+32,fbt,'#d9622b',2);}
ln(sx,42,sx,32,'#334155',2);ln(sx,32,550,32,sw?'#16a34a':'#94a3b8',2.5);ln(550,32,550,48,sw?'#16a34a':'#94a3b8',2.5);
rc(292,62,180,112,'#f8fafc','#cbd5e1',8);L('Float close up',382,74,11,'#5b6576','center',1);
var cx=400,cb=158,ch=50,wl=h>=50?cb-62:cb-h;rc(298,Math.max(wl,86),168,cb+6-Math.max(wl,86),'rgba(147,197,253,0.6)');ln(298,Math.max(wl,86),466,Math.max(wl,86),'#1e3a8a',1.5);
var top=h>=50?cb+4-ch:cb-ch;var bo=h>=50?cb+4:cb;rc(cx-25,top,50,bo-top,'#cbd5e1','#334155',4);
var b=Math.sin(T*4)*2;ar(cx-8,bo-6,cx-8,top-14+b,'#1e63b8',2.5);ar(cx+8,top+8,cx+8,bo+14-b,'#b91c1c',2.5);
L('Buoyancy',cx-30,top+6,11,'#1e63b8','right',1);L('Weight '+m(P.m,0)+' g',cx-30,bo-2,11,'#b91c1c','right',1);
if(h<50){ln(cx+30,cb,cx+30,wl,'#d9622b',2);L('h '+m(h,1),cx+33,(cb+wl)/2,11,'#d9622b','left',1);}else L('Sinks',cx+30,cb-20,11,'#b91c1c','left',1);
rc(480,48,140,96,'#1a2333',null,8);L('PLC input LSH',550,64,11,'#cbd5e1','center',1);ci(506,98,13,sw?'#fbbf24':'#334155','#94a3b8',2);if(sw){var g=0.5+0.5*Math.sin(T*8);ci(506,98,18+3*g,null,'rgba(251,191,36,0.6)',2);}
L(sw?'HIGH':'Normal',528,98,12,sw?'#fde68a':'#fff','left',1);L('Reed '+(sw?'closed':'open'),550,128,11,'#cbd5e1','center');
var gx0=330,gx1=620,gy0=200,gy1=318,TY=function(v){return gy1-v/280*(gy1-gy0);},TX=function(t){return gx1-(T-t)/20*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');ln(gx0,TY(ZR),gx1,TY(ZR),'#0369a1',1,[4,4]);L('reed 150 mm',gx0+4,TY(ZR)-8,11,'#0369a1','left');
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=TY(p[1]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
C.strokeStyle='#16a34a';C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=p[2]?gy1+10:gy1+22;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
L('Level',gx0,gy0-10,11,'#1e63b8','left',1);L('Contact',gx0-4,gy1+16,11,'#16a34a','right',1);L('last 20 s',gx1,gy0-10,11,'#5b6576','right');
mk(1,sx+40,Y(fb+40));mk(2,112,ry);mk(3,188,Y(BL)+3);mk(4,226,Y(lvl)-16);mk(5,606,48);mk(6,458,76);mk(7,316,gy0+2);}
"""
