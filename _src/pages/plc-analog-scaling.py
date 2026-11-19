PAGE = dict(
    slug="plc-analog-scaling", grp="PLC", name="PLC Analog Input Scaling", kw="How PLC Analog Input Scaling Works",
    title="How PLC Analog Input Scaling Works: Raw Count Formula, Example",
    desc="How PLC analog input scaling works, animated: a 4 to 20 mA signal becomes a raw ADC count and the scaling block turns it into pressure on the HMI.",
    h1="How PLC Analog Input Scaling Works",
    hero="Move the input current, the transmitter range and the raw count the card gives at 20 mA. Watch the card convert the current to a raw count, the scaling block turn it into bar and the status change when the signal leaves the normal range.",
    quick="A PLC analog input card converts the 4 to 20 mA current into an integer called the raw count. The program then scales that count with a straight line equation into engineering units such as bar, °C or m³/h.",
    intro=["A PLC cannot use milliamps directly. The analog input card measures the current across a small resistor, converts it with an analog to digital converter and stores the result as a whole number in a word of memory.",
           "Each card maps its signal range to a fixed count range set by the manufacturer and the card settings. The program must know both ends of that count range and both ends of the transmitter range to calculate the real value.",
           "Most analog problems on commissioning are scaling errors: the wrong count range, the wrong transmitter range or a missing check for wire break. A clear picture of the straight line behind scaling makes them quick to find."],
    sliders=[("i", "Input current", 3, 22, 12, 0.05, 2, "mA"), ("eu", "Transmitter range high (low = 0)", 1, 100, 10, 1, 0, "bar"),
             ("rh", "Raw count at 20 mA (4 mA = 0)", 4000, 32000, 32000, 1000, 0, "")],
    outs=[("raw", "Raw count"), ("eu", "Scaled value"), ("res", "Resolution (value per count)"), ("st", "Signal status (NAMUR NE 43)")],
    legend=["Transmitter sending 4 to 20 mA", "Input shunt resistor on the card", "ADC sampling the voltage", "Raw count stored in an input word", "Scaling block (straight line equation)", "Engineering value on the HMI", "Scaling line from raw count to bar"],
    steps=["The transmitter sends a current between 4 and 20 mA that is proportional to the process value.",
           "The card passes the current through a shunt resistor, producing a small voltage.",
           "The ADC samples that voltage and the card stores it as a raw count, with 4 mA at the low count and 20 mA at the high count.",
           "The scaling block in the program uses the straight line equation to convert the raw count into engineering units.",
           "The program checks the current or count against limits to flag under range, over range and wire break before using the value."],
    formula=["Value = EU low + (raw − raw low) × (EU high − EU low) ÷ (raw high − raw low)",
             "Raw count = raw low + (I − 4) ÷ 16 × (raw high − raw low)",
             "Resolution = (EU high − EU low) ÷ (raw high − raw low)",
             "NAMUR NE 43: 3.8 to 20.5 mA is the measuring range; 3.6 mA or less and 21 mA or more signal a failure",
             "Example: 12 mA, range 0 to 10 bar, raw 0 to 32000: raw = (12 − 4) ÷ 16 × 32000 = 16000; value = 16000 × 10 ÷ 32000 = 5.000 bar; resolution about 0.00031 bar per count"],
    parts=[("Shunt resistor", "Converts the loop current into a voltage the card can measure"),
           ("ADC", "Converts the voltage into a binary number, usually with 12 to 16 bits of resolution"),
           ("Input filter", "Smooths noise by averaging samples, adding a small delay"),
           ("Input word", "Memory location where the raw count is stored for the program"),
           ("Scaling block", "Program instruction or function that turns the count into engineering units and checks limits")],
    uses=[("Pressure and level transmitters", "Turn 4 to 20 mA from field transmitters into bar, metres or percent."),
          ("Temperature transmitters", "Scale a head mounted transmitter signal into °C."),
          ("Flow measurement", "Convert flow transmitter signals into m³/h for control and totalising."),
          ("Wire break alarms", "Use the raw count below the 4 mA value to detect an open loop.")],
    pros=["Simple straight line math, easy to check by hand", "Raw count range and engineering range are set independently", "Allows under range and wire break detection from the same signal"],
    cons=["Wrong count range or transmitter range gives a wrong value with no alarm", "Card resolution and filtering limit the finest change you can see", "Non linear signals such as square root flow need an extra step"],
    tips=["Check the card manual for the raw count at 4 mA and 20 mA for the range you selected; it differs between cards and settings.",
          "Make sure the engineering range in the PLC matches the range configured in the transmitter.",
          "Inject 4, 12 and 20 mA with a loop calibrator and confirm 0, 50 and 100 % on the HMI during loop checks.",
          "Alarm on current below 3.6 mA or above 21 mA so a broken wire or failed transmitter is not read as a real value."],
    faq=[("What is a raw count in a PLC?", "It is the integer the analog card writes to memory after converting the signal. Its range, such as 0 to 32000, depends on the card and its settings."),
         ("Why does my PLC show a negative value?", "The current is below 4 mA, so the raw count is below the 4 mA count. Check for a wire break, a failed transmitter or a wrong card range."),
         ("How do I scale a 4 to 20 mA signal?", "Use the straight line equation from the raw count at 4 mA and 20 mA to the transmitter range low and high. The formula and example on this page show the steps."),
         ("What is the resolution of an analog input?", "It is the smallest change in value that one count represents, equal to the engineering span divided by the number of counts.")],
    cal=[("plc-signal/analog-scaling-calculator", "Analog Scaling Calculator"), ("plc-signal/adc-resolution-calculator", "ADC Resolution Calculator")],
    glo=[("analog-scaling", "Analog Scaling"), ("adc-resolution", "ADC Resolution"), ("namur-ne43", "NAMUR NE 43")],
    cmp=[("4-20-ma-vs-0-10-v", "4 to 20 mA vs 0 to 10 V")],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("plc-analog-scaling-raw-count", "PLC analog scaling and raw count"))

SCENE = r"""
var nz=0,nt=0,dots=[],fl=0;for(var k=0;k<14;k++)dots.push(k/14);
function raw(i){return Math.round((i-4)/16*P.rh);}
function val(r){return r*P.eu/P.rh;}
function stat(i){return i<=3.6?'Failure: 3.6 mA or less':i<3.8?'Under range':i<=20.5?'Normal measuring range':i<21?'Over range':'Failure: 21 mA or more';}
function upd(){var r=raw(P.i),rs=P.eu/P.rh;o('raw',m(r,0));o('eu',m(val(r),3)+' bar');o('res',m(rs,rs<0.001?5:4)+' bar');o('st',stat(P.i));}
function step(dt){nt-=dt;if(nt<=0){nt=0.3;nz=(Math.random()-0.5)*0.008;fl=1;}fl=Math.max(0,fl-dt*4);for(var k=0;k<dots.length;k++){dots[k]+=dt*0.25*P.i/20;if(dots[k]>=1)dots[k]-=1;}}
function draw(){var i=P.i+nz,r=raw(i),v=val(r),bad=i<3.8||i>20.5;
L('A small input noise is added so the last digits flicker as on a real card',20,22,11,'#5b6576','left');
rc(20,60,90,80,'#ffffff','#c2410c',8);C.lineWidth=2.5;C.strokeStyle='#c2410c';C.stroke();L('Pressure',65,76,11,'#1a2333','center',1);L('transmitter',65,92,11,'#1a2333','center',1);L(m(P.i,2)+' mA',65,118,12,'#c2410c','center',1);
ln(110,84,170,84,'#475569',2.5);ln(110,116,170,116,'#475569',2.5);for(var k=0;k<dots.length;k++){ci(110+dots[k]*60,84,3,'#16a34a');ci(170-dots[k]*60,116,3,'#16a34a');}
rc(160,44,190,112,null,'#64748b',8);C.setLineDash([4,4]);C.strokeStyle='#64748b';C.lineWidth=1.2;C.stroke();C.setLineDash([]);L('Analog input card',255,146,11,'#5b6576','center',1);
ln(184,84,184,92,'#475569',2);ln(184,108,184,116,'#475569',2);ln(170,84,184,84,'#475569',2);ln(170,116,184,116,'#475569',2);
C.strokeStyle='#d9622b';C.lineWidth=2.5;C.beginPath();C.moveTo(184,92);for(var z=0;z<4;z++)C.lineTo(z%2?178:190,94+z*4);C.lineTo(184,108);C.stroke();L('250 Ω',196,100,11,'#1a2333','left',1);
ar(238,100,258,100,'#1a2333',1.5);rc(258,66,80,66,'#1a2333',null,6);L('ADC',298,80,11,'#cbd5e1','center',1);
for(var b=0;b<8;b++){var on=(Math.max(0,r)>>(b+8))&1;rc(266+b*8.5,96,6,14,on?'#fde047':'#475569');}ci(330,74,3,fl>0.2?'#22c55e':'#334155');L('sample',298,122,11,'#cbd5e1','center');
ar(338,100,358,100,'#1a2333',1.5);rc(358,70,96,60,'#f8fafc','#1e63b8',6);L('Input word',406,84,11,'#5b6576','center',1);L(m(r,0),406,108,14,'#1e63b8','center',1);
ar(454,100,474,100,'#1a2333',1.5);rc(474,52,152,96,'#1a2333',null,8);L('Scaling block',550,66,11,'#cbd5e1','center',1);L('value = raw × '+m(P.eu,0)+' ÷ '+m(P.rh,0),550,90,11,'#fff','center');
L('= '+m(r,0)+' × '+m(P.eu/P.rh,6),550,108,11,'#e2e8f0','center');L('= '+m(v,3)+' bar',550,128,12,'#bbf7d0','center',1);
rc(20,190,200,140,'#1a2333',null,10);L('HMI',40,206,11,'#cbd5e1','left',1);L('PT 101',200,206,11,'#cbd5e1','right',1);L(m(v,3)+' bar',120,238,20,bad?'#fca5a5':'#bbf7d0','center',1);
var pc=clamp(v/P.eu,0,1.15);rc(36,262,168,14,'#334155');rc(36,262,168*Math.min(pc,1),14,bad?'#ef4444':'#22c55e');ln(36+168*(16000/32000),258,36+168*0.5,280,'#94a3b8',1);
L('0',36,290,11,'#cbd5e1','left');L(m(P.eu,0)+' bar',204,290,11,'#cbd5e1','right');L(stat(i),120,314,11,bad?'#fca5a5':'#cbd5e1','center',1);
var gx0=310,gx1=610,gy0=196,gy1=320,rmin=-P.rh/16,rmax=P.rh*18/16,GX=function(q){return gx0+(q-rmin)/(rmax-rmin)*(gx1-gx0);},GY=function(q){return gy1-(q-(-P.eu/16))/(P.eu*18/16)*(gy1-gy0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');rc(GX(rmin),gy0,GX(-0.0125*P.rh)-GX(rmin),gy1-gy0,'rgba(185,28,28,0.10)');rc(GX(1.03125*P.rh),gy0,gx1-GX(1.03125*P.rh),gy1-gy0,'rgba(185,28,28,0.10)');
ln(GX(rmin),GY(val(rmin)),GX(rmax),GY(val(rmax)),'#1e63b8',2.5);ln(GX(0),gy1,GX(0),gy0,'#cbd5e1',1);ln(gx0,GY(0),gx1,GY(0),'#cbd5e1',1);
var px=GX(r),py=GY(v);ln(px,gy1,px,py,'#d9622b',1.2,[4,3]);ln(gx0,py,px,py,'#d9622b',1.2,[4,3]);ci(px,py,6,'#d9622b','#fff',2);
L('4 mA',GX(0),gy1+12,11,'#5b6576','center');L('20 mA',GX(P.rh),gy1+12,11,'#5b6576','center');L('raw '+m(P.rh,0),GX(P.rh),gy1+26,11,'#5b6576','center');L('raw 0',GX(0),gy1+26,11,'#5b6576','center');
L(m(P.eu,0)+' bar',gx0-4,GY(P.eu),11,'#5b6576','right');L('0',gx0-4,GY(0),11,'#5b6576','right');L('Raw count to bar',gx0+8,gy0+12,11,'#1a2333','left',1);
mk(1,20,56);mk(2,204,74);mk(3,258,62);mk(4,452,66);mk(5,622,50);mk(6,226,194);mk(7,GX(P.rh*0.75)+14,GY(P.eu*0.75)+14);}
"""
