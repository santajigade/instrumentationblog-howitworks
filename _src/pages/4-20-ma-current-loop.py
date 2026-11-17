PAGE = dict(
    slug="4-20-ma-current-loop", grp="Signals", name="4 to 20 mA Current Loop", kw="How a 4 to 20 mA Current Loop Works",
    title="How a 4 to 20 mA Current Loop Works: Animated Diagram",
    desc="How a 4 to 20 mA current loop works, animated: the supply, the transmitter regulating current, the receiver resistor and the voltage budget of the loop.",
    h1="How a 4 to 20 mA Current Loop Works",
    hero="Move the process value, the loop supply voltage and the total loop resistance. Watch the loop current change, see the voltage left for the transmitter and find out when the loop can no longer reach 20 mA.",
    quick="In a 4 to 20 mA loop the transmitter acts as a current regulator in series with a DC supply and a receiver resistor. It sets the loop current between 4 mA at 0 % and 20 mA at 100 % of range, and the receiver reads the voltage across its resistor.",
    intro=["The 4 to 20 mA current loop is still the most common analog signal between field instruments and a PLC or DCS. One pair of wires carries both the power for a two wire transmitter and the measurement itself.",
           "Current is used instead of voltage because the same current flows through every part of a series loop. Cable resistance, terminals and long distances do not change the reading, as long as the supply has enough voltage left over.",
           "The live zero at 4 mA lets the receiver tell a real zero from a broken wire. Values below about 3.6 mA or above about 21 mA are treated as faults, as described in NAMUR NE43."],
    sliders=[("pv", "Process value", 0, 100, 50, 1, 0, "%"), ("vs", "Loop supply voltage", 18, 30, 24, 0.5, 1, "V"),
             ("r", "Total loop resistance (receiver and cable)", 100, 1200, 250, 10, 0, "Ω")],
    outs=[("i", "Loop current I = 4 + 16 × PV ÷ 100"), ("vr", "Voltage across the loop resistance"), ("vt", "Voltage left at the transmitter"), ("rmax", "Maximum loop resistance at 20 mA")],
    legend=["DC loop power supply", "Two wire transmitter regulating the loop current", "Loop wires: the same current flows everywhere", "Receiver resistor in the PLC analog input", "Voltage budget of the loop", "Loop current scale with NAMUR NE43 fault zones"],
    steps=["The DC supply, the transmitter and the receiver resistor are wired in one series loop, so a single current flows through all of them.",
           "The transmitter takes a small part of the 4 mA for its own electronics and keeps the loop current fixed for the value it measures.",
           "It sets the current to 4 mA at 0 % of range and 20 mA at 100 %, a straight line in between.",
           "The receiver measures the voltage across its resistor, for example 1 to 5 V across 250 Ω, and scales it back to engineering units.",
           "The supply voltage must cover the drop across all loop resistance at 20 mA plus the minimum voltage the transmitter needs at its terminals."],
    formula=["I = 4 mA + 16 mA × PV ÷ 100 %",
             "Voltage across the loop resistance VR = I × R",
             "Voltage at the transmitter Vtx = Vsupply − I × R, and it must stay above the transmitter minimum (12 V assumed here)",
             "Maximum loop resistance R max = (Vsupply − Vmin) ÷ 0.020 A",
             "Example: PV 50 %, 24 V, 250 Ω: I = 12 mA, VR = 3.0 V, Vtx = 21.0 V and R max = (24 − 12) ÷ 0.020 = 600 Ω"],
    parts=[("Loop power supply", "Usually 24 V DC from the PLC, DCS or a separate supply; powers the whole loop"),
           ("Two wire transmitter", "Measures the process and regulates the loop current between 4 and 20 mA"),
           ("Receiver resistor", "Turns the current into a voltage for the analog input, often 250 Ω for 1 to 5 V"),
           ("Loop cable", "Twisted pair, often shielded, whose resistance adds to the loop load"),
           ("Barriers and isolators", "Optional parts in hazardous area or noisy loops; each adds its own voltage drop")],
    uses=[("Process transmitters", "Pressure, level, flow and temperature transmitters sending their value to a PLC or DCS."),
          ("Control valve signals", "Analog outputs driving valve positioners with 4 mA closed and 20 mA open, or the reverse."),
          ("HART communication", "A digital HART signal rides on top of the analog current for configuration and diagnostics."),
          ("Long cable runs", "Signals carried hundreds of metres across a plant with little loss of accuracy.")],
    pros=["Immune to cable resistance and voltage drops", "Live zero makes a broken wire easy to detect", "Power and signal on the same two wires"],
    cons=["Only one value per pair of wires without HART or a fieldbus", "Loop voltage budget limits cable length and the number of devices in series", "Needs care with grounding to avoid ground loops"],
    tips=["Measure the voltage at the transmitter terminals at 20 mA; if it is near the minimum, the reading will clip at the top of the range.",
          "Size the loop for the upscale fault current of about 21 to 22 mA, not only 20 mA, so alarms can still be signalled.",
          "To read the current without opening the loop, measure the voltage across a known resistor or use a clamp meter rated for mA.",
          "Earth the cable shield at one end only, usually at the control room, to avoid ground loops."],
    faq=[("Why does the signal start at 4 mA and not 0 mA?", "The live zero powers the transmitter electronics and lets the receiver tell a 0 % reading from a broken wire, which gives 0 mA."),
         ("What resistor is used to convert 4 to 20 mA to 1 to 5 V?", "A 250 Ω resistor. By Ohm's law 4 mA gives 1 V and 20 mA gives 5 V across it."),
         ("How long can a 4 to 20 mA cable be?", "It is limited by the voltage budget, not by the signal. The total of cable, receiver and barrier resistance at 20 mA plus the transmitter minimum voltage must stay below the supply voltage."),
         ("What do 3.6 mA and 21 mA mean?", "In NAMUR NE43 a current below 3.6 mA or above 21 mA is a fault signal, for example a sensor failure, and the receiver should raise an alarm instead of showing a value.")],
    cal=[("instrumentation-signal/loop-power-supply-calculator", "Loop Power Supply Calculator"), ("instrumentation-signal/current-to-voltage-resistor-calculator", "Current to Voltage Resistor Calculator"),
         ("plc-signal/analog-scaling-calculator", "Analog Scaling Calculator")],
    glo=[("4-20-ma-current-loop", "4 to 20 mA Current Loop"), ("live-zero", "Live Zero"), ("namur-ne43", "NAMUR NE43")],
    cmp=[("4-20-ma-vs-0-10-v", "4 to 20 mA vs 0 to 10 V")],
    dl=("downloads/cheat-sheets/4-20-ma-cheat-sheet", "4 to 20 mA Cheat Sheet"),
    blog=("4-to-20-ma-current-loop-explained", "4 to 20 mA current loop explained"))

SCENE = r"""
var VM=12,dots=[],pv=50;for(var k=0;k<28;k++)dots.push(k/28);
var PTH=[[80,110],[80,60],[405,60],[405,90],[405,170],[405,250],[80,250],[80,190]];
var LEN=[],TOT=0;for(var k=1;k<PTH.length;k++){var d=Math.hypot(PTH[k][0]-PTH[k-1][0],PTH[k][1]-PTH[k-1][1]);LEN.push(d);TOT+=d;}
function at(u){var s=u*TOT;for(var k=0;k<LEN.length;k++){if(s<=LEN[k]){var f=s/LEN[k];return[PTH[k][0]+(PTH[k+1][0]-PTH[k][0])*f,PTH[k][1]+(PTH[k+1][1]-PTH[k][1])*f,k];}s-=LEN[k];}return PTH[PTH.length-1].concat([0]);}
function cur(){var it=4+16*pv/100,lim=(P.vs-VM)/P.r*1000;return Math.min(it,lim);}
function upd(){var it=4+16*P.pv/100,i=Math.min(it,(P.vs-VM)/P.r*1000);o('i',m(i,2)+' mA'+(i<it-0.005?' (limited, should be '+m(it,2)+' mA)':''));o('vr',m(i*P.r/1000,2)+' V');
o('vt',m(P.vs-i*P.r/1000,2)+' V'+(P.vs-0.02*P.r<VM?', too low at 20 mA':', OK at 20 mA'));o('rmax',m((P.vs-VM)/0.02,0)+' Ω');}
function step(dt){pv+=(P.pv-pv)*Math.min(1,dt*3);var i=cur(),v=(i/20)*0.09;for(var k=0;k<dots.length;k++){dots[k]+=v*dt;if(dots[k]>=1)dots[k]-=1;}}
function draw(){var i=cur(),vr=i*P.r/1000,vt=P.vs-vr,it=4+16*pv/100,lim=i<it-0.005;
L('Dots show conventional current, speed scaled to the loop current',20,22,11,'#5b6576','left');
C.strokeStyle='#475569';C.lineWidth=3;C.beginPath();C.moveTo(PTH[0][0],PTH[0][1]);for(var k=1;k<PTH.length;k++)C.lineTo(PTH[k][0],PTH[k][1]);C.stroke();
rc(40,110,80,80,'#1a2333',null,8);L('Supply',80,130,11,'#cbd5e1','center',1);L(m(P.vs,1)+' V DC',80,150,13,'#fff','center',1);L('+',100,118,13,'#f87171','center',1);L('−',100,182,13,'#93c5fd','center',1);
rc(360,90,90,80,'#ffffff','#0e7490',8);C.lineWidth=2.5;C.strokeStyle='#0e7490';C.stroke();L('Transmitter',405,104,11,'#1a2333','center',1);
ci(405,136,18,'#f6f8fc','#475569');var na=Math.PI*(0.75+1.5*pv/100);ln(405,136,405+14*Math.cos(na),136+14*Math.sin(na),'#b02a52',2.5);ci(405,136,3,'#1a2333');L('PV '+m(pv,0)+' %',405,162,11,'#0e7490','center',1);
rc(450,124,18,24,'#94a3b8','#475569',3);
rc(190,226,130,56,null,'#64748b',8);C.setLineDash([4,4]);C.strokeStyle='#64748b';C.lineWidth=1.2;C.stroke();C.setLineDash([]);L('PLC analog input',255,274,11,'#5b6576','center',1);
rc(222,242,66,16,'#ffffff');C.strokeStyle='#d9622b';C.lineWidth=2.5;C.beginPath();C.moveTo(222,250);for(var z=0;z<6;z++){C.lineTo(227+z*11,z%2?256:244);}C.lineTo(288,250);C.stroke();
L('R '+m(P.r,0)+' Ω',255,234,11,'#1a2333','center',1);L(m(vr,2)+' V',326,240,11,'#d9622b','left',1);
for(var k=0;k<dots.length;k++){var p=at(dots[k]);if(p[0]>360&&p[0]<450&&p[1]>90&&p[1]<170)continue;if(p[0]>40&&p[0]<120&&p[1]>110&&p[1]<190)continue;ci(p[0],p[1],4,'#16a34a');}
ar(240,60,262,60,'#16a34a',2);L(m(i,2)+' mA',250,46,13,'#16a34a','center',1);if(lim)L('Supply too low: current limited',250,84,12,'#b91c1c','center',1);
rc(490,40,140,240,'#f6f8fc','#dde3ee',8);L('Voltage budget',560,268,11,'#5b6576','center',1);var b0=250,s=6,bx=508;
rc(bx,b0-vt*s,30,vt*s,'#0e7490');rc(bx,b0-P.vs*s,30,vr*s,'#d9622b');ln(bx-4,b0-VM*s,bx+34,b0-VM*s,'#b91c1c',1.5,[4,3]);ln(bx,b0,bx+30,b0,'#1a2333',1.5);
var ym=b0-VM*s,yr=b0-(vt+vr/2)*s;if(Math.abs(yr-ym)<14)yr=ym-14;L('min '+m(VM,0)+' V',546,ym,11,'#b91c1c','left',1);L('R '+m(vr,1)+' V',546,yr,11,'#d9622b','left',1);L('Tx '+m(vt,1)+' V',546,b0-12,11,'#0e7490','left',1);
var x0=40,x1=470,X=function(a){return x0+a/24*(x1-x0);},sy=316;L('Loop current',x0,300,11,'#5b6576','left',1);
rc(x0,sy,x1-x0,12,'#e2e8f0');rc(x0,sy,X(3.6)-x0,12,'rgba(185,28,28,0.35)');rc(X(21),sy,x1-X(21),12,'rgba(185,28,28,0.35)');rc(X(4),sy,X(20)-X(4),12,'rgba(22,163,74,0.30)');
[0,4,8,12,16,20,24].forEach(function(v){ln(X(v),sy+12,X(v),sy+17,'#475569',1);L(String(v),X(v),sy+26,11,'#1a2333','center');});L('mA',x1+16,sy+26,11,'#1a2333','left');
L('fault',X(1.8),sy+6,11,'#7f1d1d','center',1);L('fault',X(22.5),sy+6,11,'#7f1d1d','center',1);
var px=X(i);C.fillStyle='#1a2333';C.beginPath();C.moveTo(px,sy);C.lineTo(px-7,sy-10);C.lineTo(px+7,sy-10);C.closePath();C.fill();L(m(i,1)+' mA = '+m((i-4)/16*100,0)+' %',Math.min(Math.max(px,175),x1-40),sy-20,11,'#1a2333','center',1);
mk(1,30,110);mk(2,462,90);mk(3,150,60);mk(4,180,226);mk(5,618,52);mk(6,x1+44,sy+6);}
"""
