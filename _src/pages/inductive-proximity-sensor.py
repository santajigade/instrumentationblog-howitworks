PAGE = dict(
    slug="inductive-proximity-sensor", grp="Switches", name="Inductive Proximity Sensor", kw="How an Inductive Proximity Sensor Works",
    title="How an Inductive Proximity Sensor Works: Animated Diagram",
    desc="How an inductive proximity sensor works, animated: the coil field, eddy currents in the metal target and the damped oscillator that switches the output.",
    h1="How an Inductive Proximity Sensor Works",
    hero="Set the rated sensing distance, the target material and the gap to the passing targets. Watch the oscillator get damped by eddy currents and see when the output switches reliably.",
    quick="An inductive proximity sensor drives a coil with a high frequency oscillator to create a magnetic field at its face. A metal target entering the field takes energy through eddy currents, the oscillation amplitude falls below a threshold and the output switches.",
    intro=["An inductive proximity sensor detects metal objects without touching them. It is the most common non contact sensor on conveyors, machine tools, valve position feedback and lifting equipment.",
           "Inside the sensing face sits a coil wound on a ferrite core, fed by an oscillator. Metal in front of the face absorbs energy from the field, and the electronics turn that drop in oscillation into a clean on off output.",
           "The rated sensing distance on the datasheet applies only to a mild steel target. Stainless steel, brass, aluminium and copper switch at shorter distances, which is the cause of many detection problems in the field."],
    sliders=[("sn", "Rated sensing distance Sn", 2, 15, 8, 1, 0, "mm"), ("k", "Target material factor", 0.3, 1.0, 0.7, 0.05, 2, ""),
             ("g", "Gap from sensor face to target", 0.5, 15, 4, 0.5, 1, "mm")],
    outs=[("sr", "Real switching distance Sr = Sn × factor"), ("sa", "Assured distance Sa = 0.81 × Sr"), ("st", "Target at this gap"), ("cnt", "Targets counted in the demo")],
    legend=["Coil on ferrite core at the sensing face", "Oscillator amplitude and trigger threshold", "High frequency magnetic field", "Metal target with eddy currents", "Trigger and output stage", "Output LED"],
    steps=["The oscillator drives the coil, and the ferrite core shapes the alternating magnetic field so it spreads out in front of the sensing face.",
           "When a metal target enters this field, the changing flux induces eddy currents in the surface of the metal.",
           "The eddy currents take energy from the field, so the oscillator is damped and its amplitude falls.",
           "A trigger circuit compares the amplitude with a threshold and switches the output transistor when the amplitude drops below it.",
           "When the target moves away the amplitude recovers; a small hysteresis keeps the output from chattering at the switching point."],
    formula=["Real switching distance Sr = Sn × material correction factor",
             "Assured operating distance Sa = 0.81 × Sn × factor (allows ±10 % unit spread and ±10 % drift with temperature)",
             "Typical factors: mild steel 1.0, stainless steel about 0.7, brass about 0.4 to 0.5, aluminium and copper about 0.3 to 0.4 (check the datasheet)",
             "Release distance ≈ Sr × (1 + hysteresis); hysteresis is usually up to about 10 % of Sr",
             "Example: Sn 8 mm, stainless factor 0.7: Sr = 5.6 mm and Sa = 4.5 mm, so a target at a 4 mm gap is detected reliably"],
    parts=[("Coil and ferrite core", "Create a focused high frequency magnetic field in front of the sensing face"),
           ("Oscillator", "Drives the coil; its amplitude is the quantity that the target changes"),
           ("Trigger circuit", "Compares the oscillation amplitude with a threshold and adds hysteresis"),
           ("Output stage", "PNP or NPN transistor, or a NAMUR current output, that drives the PLC input"),
           ("Housing and LED", "Threaded barrel for mounting and an LED that shows the switching state")],
    uses=[("Conveyor and machine sensing", "Detects metal parts, cams and pallets passing on a line."),
          ("Valve position feedback", "Confirms open and closed positions of on off valves through a metal flag."),
          ("Speed and rotation monitoring", "Counts gear teeth or bolt heads to detect shaft rotation or underspeed."),
          ("End of travel", "Replaces mechanical limit switches on cylinders, cranes and doors where wear is a problem.")],
    pros=["Non contact, so there is no mechanical wear", "Not affected by dust, oil, water or non metal objects", "Fast switching and long life in harsh duty"],
    cons=["Detects only metal targets", "Short sensing range, usually a few millimetres to a few tens of millimetres", "Range drops for stainless steel, brass, aluminium and copper"],
    tips=["Set the gap at or below the assured distance Sa, not at the rated distance printed on the label.",
          "Apply the material factor when the target is not mild steel; a stainless flag can be missed at the rated gap.",
          "Follow the flush and non flush mounting rules for spacing to the metal around the face and to the next sensor.",
          "Match PNP or NPN output to the PLC input card; a wrong pairing gives an LED that lights while the PLC sees nothing."],
    faq=[("What is the difference between Sn, Sr and Sa?", "Sn is the rated distance on the datasheet. Sr is the real switching distance of one unit, and Sa is the assured distance where every unit switches over temperature and supply variation."),
         ("Why does my sensor not detect an aluminium target?", "Aluminium and copper take less energy from the field in the way the sensor expects, so the switching distance is much shorter. Move the sensor closer or use a sensor rated for all metals."),
         ("What is the difference between flush and non flush sensors?", "A flush sensor has a shielded face that can be mounted level with metal, with a shorter range. A non flush sensor has a longer range but needs free space around the face."),
         ("Can an inductive sensor detect a target through plastic?", "Yes, plastic, glass and wood do not affect the field, so a metal target behind a thin non metal cover can be detected within the sensing distance.")],
    cal=[("instrumentation-signal/namur-sensor-calculator", "NAMUR Sensor Calculator")],
    glo=[("namur-sensor", "NAMUR Sensor"), ("hysteresis", "Hysteresis")],
    cmp=[("pnp-vs-npn-sensor", "PNP vs NPN Sensor")],
    blog=("inductive-proximity-sensor-selection", "How to select an inductive proximity sensor"))

SCENE = r"""
var tg=[],on=false,cnt=0,sp=70,amp=1,hist=[];[406,176,636].forEach(function(x){tg.push({x:x});});
function sr(){return P.sn*P.k;}
function mat(k){return k>=0.9?'mild steel':k>=0.6?'stainless steel':k>=0.4?'brass':'aluminium or copper';}
function upd(){if(!pre){pre=1;for(var k=0;k<300;k++){T+=0.02;step(0.02);}cnt=0;}var r=sr(),a=0.81*r;o('sr',m(r,1)+' mm (factor '+m(P.k,2)+', about '+mat(P.k)+')');o('sa',m(a,1)+' mm');
o('st',P.g<=a?'Reliable: inside Sa':P.g<=r?'Marginal: between Sa and Sr':'Not detected: beyond Sr');o('cnt',cnt+' counted');}
function q(t){var c=Math.max(0,80-Math.abs(t.x-290))/80;return c*Math.min(sr()/P.g,2);}
function step(dt){var qm=0;for(var i=0;i<tg.length;i++){var t=tg[i];t.x+=sp*dt;if(t.x>700)t.x-=690;qm=Math.max(qm,q(t));}
var was=on;if(!on&&qm>=1)on=true;else if(on&&qm<0.9)on=false;if(on&&!was){cnt++;upd();}amp=1-0.5*Math.min(qm,1.8);
hist.push([T,on,amp]);while(hist.length&&T-hist[0][0]>6)hist.shift();}
var S=7,pre=0;
function draw(){var F=160,ty=F+P.g*S,r=sr(),bt=ty+18;
L('Gap drawn at 7 px per mm, oscillator slowed down',20,22,11,'#5b6576','left');
rc(20,bt,600,9,'#475569',null,3);C.setLineDash([10,10]);C.lineDashOffset=-T*sp;ln(24,bt+4.5,616,bt+4.5,'#94a3b8',2);C.setLineDash([]);C.lineDashOffset=0;
for(var j=0;j<3;j++){var ry=r*S*(j+1)/3;C.globalAlpha=0.25+0.25*Math.sin(T*6-j);C.strokeStyle='#1e63b8';C.lineWidth=1.5;C.beginPath();C.ellipse(290,F,40+j*10,ry,0,0,Math.PI);C.stroke();}C.globalAlpha=1;
var nt=tg[0];for(var i=0;i<tg.length;i++){var t=tg[i],qq=q(t);if(Math.abs(t.x-290)<Math.abs(nt.x-290))nt=t;if(t.x<-40||t.x>680)continue;rc(t.x-40,ty,80,18,'#94a3b8','#475569',3);
if(qq>0.3){C.globalAlpha=Math.min(1,qq*0.7);C.setLineDash([4,4]);C.lineDashOffset=-T*40;C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();C.ellipse(t.x,ty+9,28,5,0,0,Math.PI*2);C.stroke();C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;}}
ln(244,F+r*S,592,F+r*S,'#d9622b',1.2,[5,4]);ln(244,F+0.81*r*S,592,F+0.81*r*S,'#1d7a46',1.2,[2,4]);
rc(596,F+r*S-8,26,16,'#fff');L('Sr',598,F+r*S,11,'#d9622b','left',1);rc(206,F+0.81*r*S-8,34,16,'#fff');L('Sa',236,F+0.81*r*S,11,'#1d7a46','right',1);
ln(290,30,290,56,'#1a2333',4);rc(250,56,80,104,'#cbd5e1','#64748b',6);for(var y=66;y<128;y+=7)ln(252,y,328,y+3,'#94a3b8',1);
rc(262,130,56,24,'#334155',null,3);for(var c=0;c<4;c++){ci(272+c*12,142,4,'#d9622b');}rc(250,154,80,6,'#1e63b8');
ci(310,74,6,on?'#f59e0b':'#475569','#1a2333');if(on){ci(310,74,10,null,'rgba(245,158,11,0.5)',3);}
rc(24,56,190,84,'#1a2333',null,8);L('Trigger and output',119,72,12,'#fff','center',1);rc(40,86,158,26,on?'#22c55e':'#334155',null,4);L(on?'Output ON':'Output OFF',119,99,13,'#fff','center',1);L('Count '+cnt+', target '+mat(P.k),119,126,11,'#cbd5e1','center');
ln(214,98,250,98,on?'#22c55e':'#94a3b8',3);
rc(440,40,190,104,'#f6f8fc','#dde3ee',8);L('Oscillator amplitude',535,54,11,'#5b6576','center',1);var cy=98;
ln(448,cy-0.5*34,622,cy-0.5*34,'#d9622b',1,[3,3]);ln(448,cy+0.5*34,622,cy+0.5*34,'#d9622b',1,[3,3]);L('threshold',622,cy+0.5*34+11,11,'#d9622b','right');
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();for(var x=448;x<=622;x+=2){var y=cy-amp*34*Math.sin((x-448)/6-T*8);if(x==448)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
ln(336,F,350,F,'#1a2333',1);ln(336,ty,350,ty,'#1a2333',1);ln(343,F,343,ty,'#1a2333',1.2);L('gap '+m(P.g,1)+' mm',352,P.g>=2?(F+ty)/2:F+8,11,'#1a2333','left',1);
var y0=310,x0=150,x1=620;L('Output (last 6 s)',20,y0+12,11,'#5b6576','left',1);rc(x0,y0,x1-x0,28,'#f6f8fc');C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();
hist.forEach(function(h,i){var x=x1-(T-h[0])/6*(x1-x0),y=h[1]?y0+5:y0+24;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
mk(1,236,138);mk(2,452,70);mk(3,224,F+14);mk(4,Math.max(52,Math.min(600,nt.x+52)),ty+9);mk(5,212,64);mk(6,336,74);}
"""
