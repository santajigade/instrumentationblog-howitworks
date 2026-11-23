PAGE = dict(
    slug="zener-barrier", grp="Safety", name="Zener Barrier", kw="How a Zener Barrier Works",
    title="How a Zener Barrier Works: Animated Diagram and Formula",
    desc="How a zener barrier works, animated: a fuse, resistor and zener diodes limit the voltage and current that can reach a transmitter in a hazardous area.",
    h1="How a Zener Barrier Works",
    hero="Change the barrier voltage Uo, the series resistor and the safe area supply. Watch the loop current flow normally, then raise the supply above Uo to see the zener diodes conduct to IS earth and the fuse blow.",
    quick="A zener barrier is a shunt diode safety barrier mounted in the safe area. A series resistor limits the current and zener diodes clamp the voltage, so even under a fault the energy sent into the hazardous area stays too low to ignite the gas.",
    intro=["Intrinsic safety protects hazardous areas by limiting energy rather than containing an explosion. The zener barrier is the classic and simplest way to do this for 4 to 20 mA loops, switches and solenoids.",
           "In normal operation the zener diodes do not conduct and the barrier simply adds a series resistance to the loop. If a fault puts a high voltage on the safe area terminals, the zeners conduct to the intrinsically safe earth and the fuse opens.",
           "Because the protection depends on a solid earth path, the barrier must be connected to a dedicated IS earth. IEC 60079 14 requires the resistance from the barrier earth bar to the main earth point to stay below 1 Ω."],
    sliders=[("uo", "Barrier voltage Uo (zener clamp)", 10, 30, 28, 0.5, 1, "V"), ("r", "Series resistor R", 100, 1000, 300, 10, 0, "Ω"), ("us", "Safe area supply Us", 12, 40, 24, 0.5, 1, "V")],
    outs=[("io", "Maximum current Io = Uo ÷ R"), ("po", "Maximum power Po = Uo × Io ÷ 4"), ("ut", "Voltage left for transmitter at 20 mA"), ("st", "Barrier state")],
    legend=["Safe area power supply Us", "Fuse", "Current limiting resistor R", "Redundant zener diodes", "IS earth (below 1 Ω)", "Receiver resistor 250 Ω", "Transmitter in the hazardous area"],
    steps=["The loop supply in the safe area feeds the barrier input terminals.",
           "Current passes through the fuse, past the zener diodes and through the series resistor; the fuse and resistor set the end to end resistance of the barrier.",
           "The zener diodes sit between the fuse and the resistor, connected to the IS earth, and stay off while the voltage is below their rating.",
           "If a fault raises the input voltage, the zeners conduct, clamp the output at Uo and divert the fault current to earth.",
           "The large zener current blows the fuse before the diodes overheat, and the resistor limits the short circuit current to Io."],
    formula=["Io = Uo ÷ R (short circuit current into the hazardous area)",
             "Po = Uo × Io ÷ 4 (maximum power into a matched load)",
             "Voltage at transmitter = Us − I × (R + receiver resistor)",
             "Zeners stay off while Us is below Uo; above Uo they conduct to IS earth and the fuse blows",
             "Example: Uo 28 V and R 300 Ω give Io 93.3 mA and Po 0.65 W; at 20 mA a 24 V supply leaves 24 − 0.02 × 550 = 13.0 V"],
    parts=[("Fuse", "Opens under fault current so the zener diodes are not destroyed; it is encapsulated and not replaceable"),
           ("Series resistor", "Limits the current that can flow into the hazardous area to Io"),
           ("Zener diodes", "Clamp the voltage at Uo; two for category ib and three for category ia so the barrier survives diode failures"),
           ("IS earth bar", "Low resistance path that carries the fault current away from the hazardous area wiring"),
           ("Encapsulation", "Potting compound that stops anyone from changing or bypassing the safety components")],
    uses=[("Transmitter loops", "Powering 4 to 20 mA pressure, level and temperature transmitters in Zone 0, 1 or 2."),
          ("Simple apparatus", "Switches, RTDs and thermocouples connected without their own certification."),
          ("Solenoid valves", "Driving IS rated solenoids and indicators from a PLC output."),
          ("Retrofits", "Low cost IS protection where a reliable IS earth already exists.")],
    pros=["Simple, compact and low cost", "Fast and passive, with no power supply of its own", "Easy to verify with the entity parameters Uo, Io and Po"],
    cons=["Needs a dedicated IS earth below 1 Ω, which must be tested", "The series resistance takes several volts from the loop", "Field circuit is earthed, so earth faults in the field can upset the signal"],
    tips=["Keep the supply voltage below the barrier working voltage, not just below Uo, or leakage through the zeners will spoil the signal.",
          "Add up supply volts, barrier drop at 20 mA, receiver drop and cable drop to confirm the transmitter still gets its minimum voltage.",
          "Test the IS earth resistance at commissioning and at each inspection, and keep two separate earth conductors where required.",
          "Check that the cable and field device parameters (Ui, Ii, Ci, Li) match the barrier Uo, Io, Co and Lo before connecting."],
    faq=[("What is the difference between a zener barrier and a galvanic isolator?", "A zener barrier limits energy with diodes and resistors and needs an IS earth. A galvanic isolator uses a transformer or optocoupler to separate the circuits, so it needs no IS earth but costs more and needs its own power."),
         ("Why does a zener barrier need an earth?", "The fault current from the zener diodes must go somewhere other than the hazardous area cable. A low resistance IS earth carries it away and keeps the field wiring at a safe voltage."),
         ("Can the fuse in a barrier be replaced?", "No. The fuse is encapsulated with the other safety parts, so a barrier with a blown fuse is replaced as a complete unit."),
         ("What do Uo, Io and Po mean?", "They are the maximum voltage, current and power the barrier can deliver into the hazardous area under fault conditions. The field device must be rated for at least these values.")],
    cal=[("safety/intrinsic-safety-calculator", "Intrinsic Safety Calculator"), ("electronics/zener-diode-resistor-calculator", "Zener Diode Resistor Calculator")],
    glo=[("intrinsic-safety", "Intrinsic Safety"), ("hazardous-area-zone", "Hazardous Area Zone"), ("equipment-protection-level", "Equipment Protection Level")],
    cmp=[("zener-barrier-vs-galvanic-isolator", "Zener Barrier vs Galvanic Isolator"), ("intrinsic-safety-vs-flameproof", "Intrinsic Safety vs Flameproof")],
    tool=[("tools/practice-tests/hazardous-area-and-ex-quiz", "Hazardous Area and Ex Quiz")],
    blog=("what-is-a-zener-diode", "What is a zener diode"))

SCENE = r"""
var zt=0,I=12,hot=0;
function ut(i){return Math.min(P.us-i/1000*250,P.uo)-i/1000*P.r;}
function flt(){return P.us>P.uo;}
function upd(){o('io',m(P.uo/P.r*1000,1)+' mA');o('po',m(P.uo*P.uo/(4*P.r),2)+' W');var u=ut(20);o('ut',u>0?m(u,1)+' V':'Not enough voltage');o('st',flt()?(zt>=1.2?'Fuse blown: replace barrier':'Zeners conducting to IS earth'):'Normal: zeners off');}
function step(dt){I=12+8*Math.sin(2*Math.PI*T/6);if(flt()){var z=zt;zt+=dt;if(z<1.2&&zt>=1.2)upd();if(z==0)upd();}else if(zt>0){zt=0;upd();}}
function dots(pts,off,col){var acc=0;C.fillStyle=col;for(var i=0;i<pts.length-1;i++){var a=pts[i],b=pts[i+1],l=Math.hypot(b[0]-a[0],b[1]-a[1]);for(var s=((off-acc)%24+24)%24;s<l;s+=24){ci(a[0]+(b[0]-a[0])*s/l,a[1]+(b[1]-a[1])*s/l,3,col);}acc+=l;}}
function zd(x,on){ln(x,110,x,245,on?'#dc2626':'#334155',2);C.fillStyle=on?'#dc2626':'#334155';C.beginPath();C.moveTo(x-9,190);C.lineTo(x+9,190);C.lineTo(x,174);C.closePath();C.fill();ln(x-9,174,x+9,174,on?'#dc2626':'#334155',2.5);ln(x-9,174,x-12,169,on?'#dc2626':'#334155',2);ln(x+9,174,x+12,179,on?'#dc2626':'#334155',2);}
function draw(){var f=flt(),bl=f&&zt>=1.2,cond=f&&!bl,i=bl?0:I;
L('Fault demo: a barrier with a blown fuse is replaced, not repaired',20,22,11,'#5b6576','left');
L('SAFE AREA',120,52,12,'#1d7a46','center',1);L('HAZARDOUS AREA',540,52,12,'#b45309','center',1);ln(430,44,430,340,'#b45309',2,[8,6]);
rc(225,80,190,195,'#eef2f7','#475569',10);L('Zener barrier',320,94,11,'#5b6576','center',1);
ln(65,140,65,110,'#334155',2);ln(65,110,540,110,'#334155',2);ln(540,110,540,140,'#334155',2);ln(540,230,540,245,'#334155',2);ln(540,245,65,245,'#334155',2);ln(65,245,65,230,'#334155',2);
rc(30,140,70,90,'#1a2333',null,8);L('Supply',65,165,11,'#cbd5e1','center',1);L(m(P.us,1)+' V',65,186,13,'#fff','center',1);L('Us',65,208,11,'#cbd5e1','center');
rc(240,103,36,14,bl?'#ffffff':(cond?'rgba(220,38,38,'+(0.5+0.5*Math.sin(T*20))+')':'#fde68a'),'#334155',3);if(bl){C.clearRect(251,100,14,20);rc(251,100,14,20,'#eef2f7');ln(251,104,255,116,'#334155',1.5);ln(265,104,261,116,'#334155',1.5);}L('Fuse',258,128,11,'#1a2333','center',1);
C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(342,110);for(var k=0;k<6;k++)C.lineTo(347+k*7.5,k%2?103:117);C.lineTo(392,110);C.stroke();L('R '+m(P.r,0)+' Ω',368,128,11,'#1a2333','center',1);
zd(296,cond);zd(322,cond);L('Uo',309,208,11,'#1a2333','center',1);
rc(232,241,176,8,'#1d7a46');ln(360,249,360,300,'#1d7a46',3);ln(344,300,376,300,'#1d7a46',3);ln(349,306,371,306,'#1d7a46',3);ln(354,312,366,312,'#1d7a46',3);L('IS earth < 1 Ω',360,328,11,'#1d7a46','center',1);
C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(140,245);for(var k=0;k<6;k++)C.lineTo(145+k*7.5,k%2?238:252);C.lineTo(190,245);C.stroke();L('250 Ω receiver',165,266,11,'#1a2333','center',1);L(m(i*0.25,2)+' V',165,228,11,'#1e63b8','center',1);
rc(480,140,120,90,'#ffffff','#475569',8);ci(540,172,16,'#e0f2fe','#0369a1',2);L('PT',540,172,11,'#0369a1','center',1);L('Transmitter',540,202,11,'#1a2333','center',1);L('4 to 20 mA',540,218,11,'#5b6576','center');
var u=bl?0:Math.max(0,ut(i));L('I '+m(i,1)+' mA',545,276,12,'#1e63b8','center',1);L('U at transmitter '+m(u,1)+' V',545,296,12,'#1e63b8','center',1);
var off=T*(4+i*2.2);if(!bl&&ut(I)>0){dots([[65,140],[65,110],[540,110],[540,140]],off,'#1e63b8');dots([[540,230],[540,245],[65,245],[65,230]],off,'#1e63b8');}
if(cond){var o2=T*90;dots([[65,140],[65,110],[296,110],[296,245],[360,245],[360,300]],o2,'#dc2626');dots([[322,110],[322,245]],o2,'#dc2626');L('Fault current to earth',352,288,11,'#dc2626','right',1);}
mk(1,100,140);mk(2,258,148);mk(3,368,148);mk(4,344,196);mk(5,390,306);mk(6,212,245);mk(7,600,140);}
"""
