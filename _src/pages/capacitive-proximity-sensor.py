PAGE = dict(
    slug="capacitive-proximity-sensor", grp="Switches", name="Capacitive Proximity Sensor", kw="How a Capacitive Proximity Sensor Works",
    title="How a Capacitive Proximity Sensor Works: Animated Diagram",
    desc="How a capacitive proximity sensor works, animated: the electric field at the face, a non metal target raising capacitance and the oscillator that switches.",
    h1="How a Capacitive Proximity Sensor Works",
    hero="Set the rated sensing distance, the material correction factor of the target and the gap to the passing boxes. Watch the oscillator build up as a target enters the field and see when the output switches reliably.",
    quick="A capacitive proximity sensor builds an electric field in front of its face between an active electrode and an earth electrode. Any target with a dielectric constant higher than air raises the capacitance, the oscillator starts to swing above a threshold and the output switches.",
    intro=["A capacitive proximity sensor detects almost any material without touching it: plastic, glass, wood, paper, grain, powder, water and metal. That makes it the usual choice when the target is not metal, or when a level must be seen through the wall of a plastic tank or chute.",
           "Inside the sensing face sit two electrodes that form an open capacitor, connected to an RC oscillator. A target in front of the face adds capacitance, the oscillator starts to swing, and a trigger turns that change into a clean on off output.",
           "How far the sensor reaches depends on the dielectric constant of the target, so the rated distance on the datasheet applies only to an earthed metal plate or water. Most installations also need a sensitivity adjustment on site, done with the real target in place."],
    sliders=[("sn", "Rated sensing distance Sn", 4, 30, 15, 1, 0, "mm"), ("k", "Material correction factor", 0.1, 1.0, 0.5, 0.05, 2, ""),
             ("g", "Gap from sensor face to target", 1, 30, 5, 0.5, 1, "mm")],
    outs=[("sr", "Real switching distance Sr = Sn × factor"), ("sa", "Assured distance Sa = 0.81 × Sr"), ("st", "Target at this gap"), ("cnt", "Targets counted in the demo")],
    legend=["Active and earth electrodes at the sensing face", "Electric field in front of the face", "Non metal target raising the capacitance", "Oscillator amplitude and trigger threshold", "Sensitivity potentiometer", "Trigger and output stage"],
    steps=["The active electrode and the earth electrode at the face form an open capacitor, and their electric field spreads out in front of the sensor.",
           "With only air in the field the capacitance is small, so the RC oscillator stays below its oscillation point or swings with a very small amplitude.",
           "A target entering the field has a dielectric constant higher than air; its molecules polarise and the capacitance between the electrodes rises.",
           "The extra capacitance lets the oscillator build up; when its amplitude crosses the trigger threshold the output transistor switches.",
           "When the target leaves, the amplitude falls again; a small hysteresis keeps the output from chattering, and the potentiometer sets how much capacitance change is needed."],
    formula=["C = ε0 × εr × A ÷ d (a higher εr or a smaller gap gives a higher capacitance)",
             "Real switching distance Sr = Sn × material correction factor",
             "Assured operating distance Sa = 0.81 × Sn × factor (allows ±10 % unit spread and ±10 % drift)",
             "Typical factors: metal and water about 1.0, glass about 0.5, PVC and wood about 0.2 to 0.6, oil about 0.1 (use the datasheet curve)",
             "Example: Sn 15 mm, factor 0.5: Sr = 7.5 mm and Sa = 0.81 × 7.5 = 6.1 mm, so a box at a 5 mm gap is detected reliably"],
    parts=[("Active and earth electrodes", "Form an open capacitor whose field reaches out in front of the sensing face"),
           ("RC oscillator", "Starts to swing as the capacitance rises; its amplitude is the quantity the target changes"),
           ("Sensitivity potentiometer", "Sets the switching point so the sensor sees the target but ignores the wall or dust"),
           ("Trigger and output stage", "Compares the amplitude with a threshold, adds hysteresis and drives a PNP or NPN transistor"),
           ("Housing and LED", "Plastic or metal barrel for mounting, with an LED that shows the switching state")],
    uses=[("Level through a tank wall", "Detects liquid or granules behind a plastic or glass wall without any process connection."),
          ("Packaging lines", "Senses cartons, bottles, paper stacks and plastic parts that an inductive sensor cannot see."),
          ("Bulk solids", "Gives high and low level alarms for grain, pellets and powder in hoppers and silos."),
          ("Presence of liquid in tubes", "Checks for liquid in a transparent hose or a pipette on filling and dosing machines.")],
    pros=["Detects metal and non metal targets, liquids and solids", "Can sense through a thin non metal wall", "Non contact, with no mechanical wear"],
    cons=["Range depends strongly on the target material and must be adjusted on site", "Humidity, condensation and build up on the face can cause false switching", "Shorter range and slower switching than an inductive sensor of the same size"],
    tips=["Adjust the potentiometer with the real target in place, then back it off until the empty state switches off cleanly with some margin.",
          "For level through a tank wall, keep the wall thickness within what the datasheet allows and press the face firmly against it.",
          "Keep the face clean; a film of wet product or dust can look like a target and hold the output on.",
          "Follow the flush and non flush mounting rules, and keep the spacing between two sensors so their fields do not interact."],
    faq=[("What is the difference between inductive and capacitive proximity sensors?", "An inductive sensor uses a magnetic field and detects only metal. A capacitive sensor uses an electric field and detects any material whose dielectric constant is higher than air."),
         ("Why does the sensing distance change with the material?", "The capacitance change depends on the dielectric constant of the target. Water and metal give a large change and the full range, while oil or dry plastic give a small change and a short range."),
         ("Can a capacitive sensor detect liquid through a pipe or tank wall?", "Yes, if the wall is non metal and thin enough. The sensitivity is set so the wall alone does not switch the output but the liquid behind it does."),
         ("Why does my capacitive sensor switch on by itself?", "Usually because of build up, condensation or a sensitivity set too high. Clean the face, reduce the sensitivity and check that nothing conductive sits near the field.")],
    cal=[("level/capacitance-level-probe-calculator", "Capacitance Level Probe Calculator")],
    glo=[("dielectric-constant", "Dielectric Constant"), ("hysteresis", "Hysteresis")],
    cmp=[("pnp-vs-npn-sensor", "PNP vs NPN Sensor")],
    blog=("inductive-vs-capacitive-proximity-sensors", "Inductive vs capacitive proximity sensors"))

SCENE = r"""
var tg=[],on=false,cnt=0,sp=60,amp=0,hist=[],pre=0,S=5,F=130;[406,176,636].forEach(function(x){tg.push({x:x});});
function sr(){return P.sn*P.k;}
function mat(k){return k>=0.9?'water or metal':k>=0.45?'glass':k>=0.2?'PVC or wood':'oil or dry powder';}
function upd(){if(!pre){pre=1;for(var k=0;k<300;k++){T+=0.02;step(0.02);}cnt=0;}var r=sr(),a=0.81*r;o('sr',m(r,1)+' mm (factor '+m(P.k,2)+', about '+mat(P.k)+')');o('sa',m(a,1)+' mm');
o('st',P.g<=a?'Reliable: inside Sa':P.g<=r?'Marginal: between Sa and Sr':'Not detected: beyond Sr');o('cnt',cnt+' counted');}
function q(t){var c=Math.max(0,80-Math.abs(t.x-290))/80;return c*Math.min(sr()/P.g,2);}
function step(dt){var qm=0;for(var i=0;i<tg.length;i++){var t=tg[i];t.x+=sp*dt;if(t.x>700)t.x-=690;qm=Math.max(qm,q(t));}
var was=on;if(!on&&qm>=1)on=true;else if(on&&qm<0.9)on=false;if(on&&!was){cnt++;upd();}amp=0.04+0.6*Math.min(qm,1.6);
hist.push([T,on]);while(hist.length&&T-hist[0][0]>6)hist.shift();}
function draw(){var ty=F+P.g*S,r=sr(),bt=ty+20;
L('Gap drawn at 5 px per mm, oscillator slowed down',20,22,11,'#5b6576','left');
rc(20,bt,600,9,'#475569',null,3);C.setLineDash([10,10]);C.lineDashOffset=-T*sp;ln(24,bt+4.5,616,bt+4.5,'#94a3b8',2);C.setLineDash([]);C.lineDashOffset=0;
for(var j=0;j<3;j++){var ry=Math.max(6,r*S*(j+1)/3);C.globalAlpha=0.3+0.25*Math.sin(T*5-j);C.strokeStyle='#6b3fb0';C.lineWidth=1.5;C.setLineDash([3,4]);C.lineDashOffset=-T*20;C.beginPath();C.ellipse(290,F,22+j*10,ry,0,0,Math.PI);C.stroke();}C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
var nt=tg[0];for(var i=0;i<tg.length;i++){var t=tg[i],qq=q(t);if(Math.abs(t.x-290)<Math.abs(nt.x-290))nt=t;if(t.x<-40||t.x>680)continue;rc(t.x-40,ty,80,20,'#dbeafe','#3b82f6',3);
if(qq>0.3){C.globalAlpha=Math.min(1,qq*0.8);for(var d=-24;d<=24;d+=16){L('+',t.x+d,ty+6,11,'#b02a52','center',1);L('−',t.x+d,ty+15,11,'#1e63b8','center',1);}C.globalAlpha=1;}}
ln(244,F+r*S,430,F+r*S,'#d9622b',1.2,[5,4]);ln(244,F+0.81*r*S,452,F+0.81*r*S,'#1d7a46',1.2,[2,4]);
rc(432,F+r*S-7,20,14,'#fff');L('Sr',434,F+r*S,11,'#d9622b','left',1);rc(456,F+0.81*r*S-7,22,14,'#fff');L('Sa',458,F+0.81*r*S,11,'#1d7a46','left',1);
ln(290,24,290,30,'#1a2333',4);rc(250,30,80,F-30,'#e2e8f0','#64748b',6);for(var y=40;y<F-30;y+=7)ln(252,y,328,y+3,'#cbd5e1',1);
rc(262,F-36,56,22,'#334155',null,3);L('RC osc',290,F-25,11,'#fff','center',1);
rc(252,F-9,16,7,'#475569');rc(270,F-9,40,7,'#6b3fb0');rc(312,F-9,16,7,'#475569');
ci(270,56,7,'#f8fafc','#1a2333');var pa=-2.2+P.k*1.2;ln(270,56,270+6*Math.cos(pa),56+6*Math.sin(pa),'#1a2333',2);
ci(312,56,6,on?'#f59e0b':'#475569','#1a2333');if(on){ci(312,56,10,null,'rgba(245,158,11,0.5)',3);}
rc(20,40,180,72,'#1a2333',null,8);L('Trigger and output',110,54,12,'#fff','center',1);rc(34,66,152,24,on?'#22c55e':'#334155',null,4);L(on?'Output ON':'Output OFF',110,78,13,'#fff','center',1);L('Count '+cnt+', '+mat(P.k),110,100,11,'#cbd5e1','center');
ln(200,84,250,84,on?'#22c55e':'#94a3b8',3);
rc(440,40,190,104,'#f6f8fc','#dde3ee',8);L('Oscillator amplitude',535,54,11,'#5b6576','center',1);var cy=96;
ln(448,cy-0.6*34,622,cy-0.6*34,'#d9622b',1,[3,3]);ln(448,cy+0.6*34,622,cy+0.6*34,'#d9622b',1,[3,3]);L('threshold',622,cy+0.6*34+11,11,'#d9622b','right');
C.strokeStyle='#6b3fb0';C.lineWidth=2;C.beginPath();for(var x=448;x<=622;x+=2){var yy=cy-amp*34*Math.sin((x-448)/6-T*8);if(x==448)C.moveTo(x,yy);else C.lineTo(x,yy);}C.stroke();
ln(184,F,198,F,'#1a2333',1);ln(184,ty,198,ty,'#1a2333',1);ln(191,F,191,ty,'#1a2333',1.2);L('gap '+m(P.g,1)+' mm',180,Math.max(F+10,(F+ty)/2),11,'#1a2333','right',1);
var y0=318,x0=150,x1=620;L('Output (last 6 s)',20,y0+12,11,'#5b6576','left',1);rc(x0,y0,x1-x0,24,'#f6f8fc');C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();
hist.forEach(function(h,i){var x=x1-(T-h[0])/6*(x1-x0),y=h[1]?y0+4:y0+20;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
mk(1,236,F-12);mk(2,356,F+Math.max(10,Math.min(30,r*S*0.5)));mk(3,Math.max(52,Math.min(600,nt.x+54)),ty+10);mk(4,452,70);mk(5,236,52);mk(6,200,40);}
"""
