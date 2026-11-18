PAGE = dict(
    slug="photoelectric-sensor", grp="Switches", name="Photoelectric Sensor", kw="How a Photoelectric Sensor Works",
    title="How a Photoelectric Sensor Works: Animated Excess Gain Diagram",
    desc="How a photoelectric sensor works, animated: a pulsed light beam, boxes breaking it on a conveyor, excess gain at the receiver and a dark operate output.",
    h1="How a Photoelectric Sensor Works",
    hero="Set the rated range of the through beam pair, the distance between emitter and receiver and the dirt on the lenses. Watch the light at the receiver against the switching threshold and see when boxes are counted reliably or when the output sticks on.",
    quick="A photoelectric sensor sends a pulsed beam of light from an emitter and checks how much of it arrives at a receiver. When a target blocks or reflects the beam, the received light crosses a threshold and the output switches.",
    intro=["A photoelectric sensor detects objects with light instead of contact or magnetic fields. It sees almost any material at distances from a few millimetres to tens of metres, which makes it the standard sensor for conveyors, packaging and door safety.",
           "There are three main modes: through beam with a separate emitter and receiver, retroreflective with a reflector, and diffuse where the target itself reflects the light back. All of them modulate the light in fast pulses so the receiver can ignore sunlight and lamps.",
           "The key number for a reliable installation is excess gain, the ratio of light that reaches the receiver to the light needed to switch. Dust, mist and dirty lenses eat into that margin long before the sensor actually fails."],
    sliders=[("sn", "Rated range Sn of the pair", 2, 20, 10, 1, 0, "m"), ("d", "Distance emitter to receiver", 1, 20, 4, 0.5, 1, "m"),
             ("dirt", "Light lost to dirt on lenses", 0, 95, 50, 5, 0, "%")],
    outs=[("eg0", "Clean excess gain (Sn ÷ d)²"), ("eg", "Excess gain with dirt"), ("st", "Detection margin"), ("cnt", "Boxes counted in the demo")],
    legend=["Emitter with LED and lens", "Pulsed light beam across the conveyor", "Box breaking the beam", "Receiver with photodiode", "Received light against the switching threshold", "Output stage in dark operate mode"],
    steps=["The emitter drives an LED or laser diode in short, fast pulses and a lens forms them into a beam aimed at the receiver.",
           "The receiver photodiode turns the light it gets into a current and a demodulator keeps only light that matches the emitter pulses.",
           "With a clear path the received light is above the switching threshold, so the sensor reports light.",
           "A box entering the beam blocks the light; the received signal falls below the threshold and the output switches.",
           "In dark operate mode the output is on while the beam is blocked, so every box gives one pulse that a PLC can count."],
    formula=["Excess gain EG = light reaching the receiver ÷ light needed to switch",
             "Through beam in the far field: EG ≈ (Sn ÷ d)² × lens transmission, where Sn is the range at which EG falls to 1",
             "Lens transmission = 1 − fraction of light lost to dirt",
             "EG below 1: the receiver never sees enough light, so a dark operate output stays on as if a target were present",
             "Example: Sn 10 m, d 4 m, 50 % dirt loss: EG = (10 ÷ 4)² × 0.5 = 6.25 × 0.5 = 3.1, a good margin for a clean area"],
    parts=[("Emitter", "LED or laser diode with a lens, driven in pulses to make the light easy to recognise"),
           ("Receiver", "Photodiode or phototransistor with a lens and an optical filter matched to the emitter colour"),
           ("Demodulator and threshold", "Keeps only pulses in step with the emitter and compares their strength with the switching level"),
           ("Light on and dark on selector", "Chooses whether the output is on when light is received or when the beam is blocked"),
           ("Output stage", "PNP, NPN or relay output with a status LED and often a stability LED for margin")],
    uses=[("Counting on conveyors", "Counts cartons, bottles and bags as they break a beam across the line."),
          ("Position and jam detection", "Confirms a part has arrived at a station or that a chute is blocked."),
          ("Door and gate protection", "Stops a closing door or gate when a person or vehicle is in the beam."),
          ("Label and mark detection", "Diffuse and contrast sensors see printed marks or labels on a moving web.")],
    pros=["Detects almost any material, metal or non metal", "Long ranges, up to tens of metres in through beam mode", "Fast switching with no contact or wear"],
    cons=["Dust, mist, steam and dirty lenses reduce the margin", "Clear or shiny targets can fool retroreflective and diffuse modes", "Needs careful alignment, especially over long distances"],
    tips=["Align the pair by moving the emitter slowly until the stability LED is solid, then lock it in the middle of that window, not at the edge.",
          "Keep excess gain well above 1; many engineers aim for 1.5 or more in clean areas and much higher where dust or mist builds up.",
          "Use a through beam pair for dirty areas and long distances, because the light crosses the path only once.",
          "Choose dark operate for counting blocked targets and check that the PLC input filter and scan time can see the shortest pulse."],
    faq=[("What are the three types of photoelectric sensors?", "Through beam uses a separate emitter and receiver, retroreflective uses one housing and a reflector, and diffuse uses one housing and the target itself as the reflector. Through beam has the longest range and the best margin."),
         ("What is the difference between light operate and dark operate?", "In light operate the output is on when the receiver sees light. In dark operate the output is on when the light is blocked, which is the usual choice for counting objects that break a beam."),
         ("What is excess gain in a photoelectric sensor?", "It is the ratio of the light reaching the receiver to the light needed to switch. An excess gain of 1 means the sensor is just at its limit, so any dirt makes it fail."),
         ("Why is the light pulsed?", "Pulsing lets the receiver pick out its own light from sunlight and lamps. The receiver only reacts to light that arrives in step with the emitter pulses.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("hysteresis", "Hysteresis")],
    cmp=[("pnp-vs-npn-sensor", "PNP vs NPN Sensor")],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("different-types-of-photoelectric-sensors", "Different types of photoelectric sensors"))

SCENE = r"""
var bx=[],sp=70,on=false,cnt=0,hist=[],lev=0,pre=0,BX=320,BY0=82,BY1=198;[120,330,540].forEach(function(x){bx.push({x:x});});
function eg0(){return Math.pow(P.sn/P.d,2);}
function eg(){return eg0()*(1-P.dirt/100);}
function upd(){if(!pre){pre=1;for(var k=0;k<200;k++){T+=0.02;step(0.02);}cnt=0;}var e=eg();o('eg0',m(eg0(),2));o('eg',m(e,2));
o('st',e>=1.5?'Reliable: margin above 1.5':e>=1?'Marginal: between 1 and 1.5':'Fails: output stuck on');o('cnt',cnt+' counted');}
function blk(){for(var i=0;i<bx.length;i++){if(Math.abs(bx[i].x-BX)<35)return bx[i];}return null;}
function step(dt){for(var i=0;i<bx.length;i++){bx[i].x+=sp*dt;if(bx[i].x>680)bx[i].x-=630;}
var b=blk();lev=b?0:eg();var was=on;if(!on&&lev<1)on=true;else if(on&&lev>1.1)on=false;if(on&&!was){cnt++;upd();}
hist.push([T,on]);while(hist.length&&T-hist[0][0]>6)hist.shift();}
function lx(v){if(v<=0.1)return 0;return clamp((Math.log(v)/Math.LN10+1)/3,0,1);}
function draw(){var b=blk(),e=eg();
L('Top view; beam pulses slowed down',20,22,11,'#5b6576','left');
rc(20,96,600,88,'#cbd5e1','#94a3b8',4);C.save();C.beginPath();C.rect(20,96,600,88);C.clip();for(var x=20-((T*sp)%40);x<640;x+=40)ln(x,98,x,182,'#b6c2d2',2);C.restore();
ar(30,140,80,140,'#475569',2);L('Conveyor',56,126,11,'#475569','center',1);
rc(290,40,60,40,'#334155',null,5);L('Emitter',320,52,11,'#fff','center',1);ci(320,68,6,'#ef4444');rc(304,78,32,6,'#93c5fd');
rc(290,200,60,40,'#334155',null,5);L('Receiver',320,228,11,'#fff','center',1);rc(304,196,32,6,'#93c5fd');
var yEnd=b?110:196;var al=clamp(0.25+0.75*Math.min(e,2)/2,0.25,1);C.globalAlpha=al;C.strokeStyle='#ef4444';C.lineWidth=5;C.setLineDash([8,8]);C.lineDashOffset=-T*40;C.beginPath();C.moveTo(BX,86);C.lineTo(BX,yEnd);C.stroke();C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
for(var i=0;i<bx.length;i++){var q=bx[i];if(q.x<-40||q.x>680)continue;rc(q.x-35,110,70,60,'#d6a86a','#8a5a2b',3);ln(q.x-35,140,q.x+35,140,'#b9874a',2);}
if(P.dirt>0){C.globalAlpha=clamp(P.dirt/100,0,0.8);for(var k=0;k<6;k++){ci(306+k*5,81,1.6,'#5b4636');ci(308+k*5,199,1.6,'#5b4636');}C.globalAlpha=1;}
rc(20,212,240,62,'#1a2333',null,8);L('Output, dark operate',140,226,12,'#fff','center',1);rc(34,238,212,24,on?'#22c55e':'#334155',null,4);L(on?(b?'ON: beam blocked':'ON: not enough light'):'OFF: light received',140,250,12,'#fff','center',1);
ln(260,232,290,232,on?'#22c55e':'#94a3b8',3);
var gx=380,gw=240,gy=212;rc(gx-10,gy-12,gw+20,96,'#f6f8fc','#dde3ee',8);L('Light at receiver (log scale)',gx+gw/2,gy+2,11,'#5b6576','center',1);
rc(gx,gy+16,gw,18,'#e2e8f0');var lw=lx(lev);rc(gx,gy+16,gw*lw,18,lev>=1.5?'#22c55e':lev>=1?'#f59e0b':'#ef4444');
var flick=0.04*Math.sin(T*25);if(lev>0)rc(gx+gw*lw-3,gy+16,3,18,'rgba(255,255,255,'+(0.5+flick*8)+')');
[[0.1,'0.1'],[1,'1'],[10,'10'],[100,'100']].forEach(function(t){var x=gx+gw*lx(t[0]+0.0001);ln(x,gy+36,x,gy+42,'#475569',1);L(t[1],x,gy+52,11,'#5b6576','center');});
var tx=gx+gw*lx(1);ln(tx,gy+12,tx,gy+38,'#1a2333',2);L('threshold',tx+4,gy+70,11,'#1a2333','left',1);L('EG '+m(e,1),gx+gw,gy+70,11,'#1e63b8','right',1);
ln(350,220,370,220,'#94a3b8',2);
var y0=316,x0=150,x1=620;L('Output (last 6 s)',20,y0+12,11,'#5b6576','left',1);rc(x0,y0,x1-x0,24,'#f6f8fc');C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();
hist.forEach(function(h,i){var x=x1-(T-h[0])/6*(x1-x0),y=h[1]?y0+4:y0+20;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();L('Count '+cnt,20,y0-10,11,'#1a2333','left',1);
mk(1,272,52);mk(2,BX+22,yEnd>150?175:92);var nb=bx[0];for(var i=1;i<bx.length;i++)if(Math.abs(bx[i].x-200)<Math.abs(nb.x-200))nb=bx[i];mk(3,clamp(nb.x,50,590),156);mk(4,368,226);mk(5,gx+gw+2,gy-10);mk(6,20,206);}
"""
