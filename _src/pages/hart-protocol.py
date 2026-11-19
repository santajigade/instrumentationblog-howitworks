PAGE = dict(
    slug="hart-protocol", grp="Signals", name="HART Protocol", kw="How HART Protocol Works",
    title="How HART Protocol Works: Animated FSK Diagram and Formula",
    desc="How HART protocol works, animated: a 1200 and 2200 Hz FSK signal rides on the 4 to 20 mA loop while the average current still carries the analog value.",
    h1="How HART Protocol Works",
    hero="Change the process value and the loop resistor. Watch the digital HART signal ride on top of the analog current, see that its average leaves the 4 to 20 mA value untouched, and check whether the resistor is large enough for the modem.",
    quick="HART adds a small digital signal on top of the 4 to 20 mA current. It uses frequency shift keying: 1200 Hz means a 1 and 2200 Hz means a 0, with an amplitude of about 0.5 mA, so the average current and the analog reading are not disturbed.",
    intro=["HART stands for Highway Addressable Remote Transducer. It lets a host read and configure a smart transmitter over the same two wires that carry the 4 to 20 mA signal, without changing the analog value.",
           "The digital part is a Bell 202 style FSK signal at 1200 bit per second. Because a sine wave averages to zero, the analog input card and its filter still see only the DC current set by the transmitter.",
           "The signal appears as a voltage across the loop resistance, so HART needs a minimum resistance in the loop. Too little resistance or a large capacitor across the loop is the most common reason a handheld cannot talk to a device."],
    sliders=[("pv", "Process value", 0, 100, 50, 1, 0, "%"), ("r", "Loop resistor", 100, 600, 250, 10, 0, "Ω")],
    outs=[("i", "Loop current (analog value)"), ("vd", "DC voltage across the resistor"), ("vh", "HART signal across the resistor (1 mA peak to peak)"), ("ok", "Resistor check (HART needs 230 to 1100 Ω)")],
    legend=["Loop power supply", "Smart transmitter with HART modem", "Loop resistor (sense resistor)", "HART communicator across the resistor", "FSK signal on top of the DC current", "Average current = analog value"],
    steps=["The transmitter sets the DC loop current between 4 and 20 mA in proportion to the process value.",
           "When it replies to a request, its modem adds a sine current of about ±0.5 mA on top of that DC value.",
           "A 1 is sent as one cycle of 1200 Hz and a 0 as just under two cycles of 2200 Hz, giving 1200 bit per second.",
           "The communicator or host modem detects the voltage this current makes across the loop resistor and decodes the bytes.",
           "The analog card filters out the fast sine wave, so it still reads the true DC current and the control loop is not disturbed."],
    formula=["Loop current I = 4 + 16 × PV ÷ 100 (mA)",
             "HART voltage across the resistor = 1 mA peak to peak × R",
             "Bit time = 1 ÷ 1200 s ≈ 0.833 ms; logic 1 = 1200 Hz, logic 0 = 2200 Hz",
             "Loop resistance must be at least 230 Ω and normally not more than 1100 Ω",
             "Example: PV 50 %, R 250 Ω: I = 4 + 16 × 0.5 = 12 mA, DC voltage = 12 mA × 250 Ω = 3.0 V, HART signal = 1 mA × 250 Ω = 250 mV peak to peak"],
    parts=[("HART field device", "Smart transmitter or positioner with a modem that sends and receives FSK on the loop current"),
           ("Loop resistor", "Sense resistor, usually 250 Ω, that turns the current and the HART signal into a voltage"),
           ("HART master", "Handheld communicator, PC modem or HART enabled input card that starts each transaction"),
           ("Loop power supply", "DC supply that powers the two wire transmitter through the loop"),
           ("HART multiplexer or I/O card", "Lets a control or asset management system reach many HART devices")],
    uses=[("Configuration and range change", "Set tag, range, units and damping without opening the transmitter."),
          ("Diagnostics", "Read device status and alarms to find faults before they upset the process."),
          ("Loop checks", "Compare the digital PV with the analog reading during commissioning."),
          ("Multivariable devices", "Read secondary values such as sensor temperature from the same pair of wires.")],
    pros=["Uses the existing 4 to 20 mA wiring and keeps the analog signal", "Gives remote configuration and diagnostics on every device", "Open standard supported by most transmitters and handhelds"],
    cons=["Slow: 1200 bit per second, so only a few values per second", "Needs a minimum loop resistance and low loop capacitance", "Noisy or long cables and some isolators block the signal"],
    tips=["If the communicator finds no device, check that at least 230 Ω is in the loop between the handheld leads and the supply.",
          "Connect the handheld across the resistor or across the transmitter terminals, never in series with the loop.",
          "Check that any isolator or barrier in the loop is rated as HART transparent.",
          "Use the digital PV to cross check the analog reading on the control system during loop checks."],
    faq=[("Does HART change the 4 to 20 mA reading?", "No. The FSK sine wave averages to zero over each bit, and the analog card filters it out, so the DC current and the reading stay the same."),
         ("Why does HART need a 250 Ω resistor?", "The HART master detects a voltage. The signal current of about 1 mA peak to peak needs enough resistance to make a usable voltage, which is why the loop needs at least 230 Ω."),
         ("What frequencies does HART use?", "A logic 1 is 1200 Hz and a logic 0 is 2200 Hz. This is frequency shift keying based on the Bell 202 standard, at 1200 bit per second."),
         ("What is HART burst mode?", "In burst mode the field device sends a chosen reply repeatedly without being asked, which gives faster digital updates to a listening host.")],
    cal=[("instrumentation-signal/loop-power-supply-calculator", "Loop Power Supply Calculator"), ("instrumentation-signal/instrument-cable-loop-resistance-calculator", "Instrument Cable Loop Resistance Calculator")],
    glo=[("hart-protocol", "HART Protocol"), ("loop-resistance", "Loop Resistance")],
    cmp=[("hart-vs-foundation-fieldbus", "HART vs Foundation Fieldbus")],
    tool=[("tools/communication-protocols/hart-command-list", "HART Command List"), ("tools/practice-tests/hart-and-modbus-quiz", "HART and Modbus Quiz")],
    blog=("hart-protocol-how-it-works", "How HART protocol works"))

SCENE = r"""
var BR=1.5,BW=56,bits=[],nm=[],cum=[0],dots=[],pv=50;for(var k=0;k<26;k++)dots.push(k/26);
var PTH=[[75,90],[75,55],[445,55],[445,85],[445,165],[445,190],[75,190],[75,160]];
var LEN=[],TOT=0;for(var k=1;k<PTH.length;k++){var d=Math.hypot(PTH[k][0]-PTH[k-1][0],PTH[k][1]-PTH[k-1][1]);LEN.push(d);TOT+=d;}
function at(u){var s=u*TOT;for(var k=0;k<LEN.length;k++){if(s<=LEN[k]){var f=s/LEN[k];return[PTH[k][0]+(PTH[k+1][0]-PTH[k][0])*f,PTH[k][1]+(PTH[k+1][1]-PTH[k][1])*f];}s-=LEN[k];}return PTH[0];}
function hx(b){return '0x'+(b<16?'0':'')+b.toString(16).toUpperCase();}
function build(){var dv=new DataView(new ArrayBuffer(4));dv.setFloat32(0,P.pv);var by=[],lb=[];for(var k=0;k<5;k++){by.push(255);lb.push('Preamble');}
var msg=[6,128,1,7,0,0,57,dv.getUint8(0),dv.getUint8(1),dv.getUint8(2),dv.getUint8(3)],ml=['Delimiter','Address','Command 1','Byte count','Response code','Device status','Units code','PV float byte 1','PV float byte 2','PV float byte 3','PV float byte 4'],cs=0;
msg.forEach(function(b,i){cs^=b;by.push(b);lb.push(ml[i]);});by.push(cs);lb.push('Checksum');bits=[];nm=[];
by.forEach(function(b,i){var p=1,ch=[0];for(var j=0;j<8;j++){var v=(b>>j)&1;ch.push(v);p^=v;}ch.push(p);ch.push(1);ch.forEach(function(v){bits.push(v);nm.push(lb[i]+' '+hx(b));});});
for(var k=0;k<6;k++){bits.push(2);nm.push('No carrier between messages');}cum=[0];for(var k=0;k<bits.length;k++)cum.push(cum[k]+(bits[k]==1?1:bits[k]==0?11/6:0));}
function bitAt(b){var N=bits.length,K=Math.floor(b),i=((K%N)+N)%N;return i;}
function phase(b){var N=bits.length,K=Math.floor(b),i=((K%N)+N)%N,f=b-K,c=bits[i]==1?1:bits[i]==0?11/6:0;return 2*Math.PI*(Math.floor(K/N)*cum[N]+cum[i]+f*c);}
function upd(){build();var i=4+16*P.pv/100;o('i',m(i,2)+' mA');o('vd',m(i*P.r/1000,2)+' V');o('vh',m(P.r,0)+' mV peak to peak');o('ok',P.r<230?'Too low: HART signal too weak':P.r>1100?'Too high':'OK for HART');}
function step(dt){pv+=(P.pv-pv)*Math.min(1,dt*3);var v=(4+16*pv/100)/20*0.08;for(var k=0;k<dots.length;k++){dots[k]+=v*dt;if(dots[k]>=1)dots[k]-=1;}}
function draw(){var i=4+16*pv/100,pos=T*BR+12,ib=bitAt(pos),act=bits[ib]!=2;
L('Bits slowed about 800 times; DC current dots not to scale',20,22,11,'#5b6576','left');
C.strokeStyle='#475569';C.lineWidth=3;C.beginPath();C.moveTo(PTH[0][0],PTH[0][1]);for(var k=1;k<PTH.length;k++)C.lineTo(PTH[k][0],PTH[k][1]);C.stroke();
rc(35,90,80,70,'#1a2333',null,8);L('Supply',75,108,11,'#cbd5e1','center',1);L('24 V DC',75,128,12,'#fff','center',1);L('+',100,98,12,'#f87171','center',1);L('−',100,152,12,'#93c5fd','center',1);
rc(395,85,100,80,'#ffffff','#3b4bb0',8);C.lineWidth=2.5;C.strokeStyle='#3b4bb0';C.stroke();L('Transmitter',445,99,11,'#1a2333','center',1);L('HART modem',445,117,11,'#3b4bb0','center',1);
ci(445,145,9,act?'#fde047':'#e2e8f0','#475569');if(act){for(var k=0;k<3;k++){var rr=11+((T*12+k*3.3)%10);C.globalAlpha=1-(rr-11)/10;ci(445,145,rr,null,'#3b4bb0',1.5);C.globalAlpha=1;}}
rc(205,182,70,16,'#ffffff');C.strokeStyle='#d9622b';C.lineWidth=2.5;C.beginPath();C.moveTo(205,190);for(var z=0;z<6;z++){C.lineTo(211+z*11,z%2?196:184);}C.lineTo(275,190);C.stroke();L('R '+m(P.r,0)+' Ω',240,210,11,'#1a2333','center',1);
ln(212,190,212,160,'#16a34a',2);ln(268,190,268,160,'#b91c1c',2);rc(180,80,120,80,'#1a2333',null,10);rc(192,90,96,40,P.r>=230?'#d9f99d':'#fecaca');
if(P.r>=230){L('Cmd 1 reply',240,101,11,'#1a2333','center',1);L('PV '+m(P.pv,1)+' %',240,119,12,'#1a2333','center',1);}else{L('No device',240,101,11,'#7f1d1d','center',1);L('signal too weak',240,119,11,'#7f1d1d','center',1);}L('HART master',240,146,11,'#cbd5e1','center',1);
for(var k=0;k<dots.length;k++){var p=at(dots[k]);if(p[0]>395&&p[0]<495&&p[1]>85&&p[1]<165)continue;if(p[0]>35&&p[0]<115&&p[1]>90&&p[1]<160)continue;ci(p[0],p[1],3.5,'#16a34a');}
L(m(i,2)+' mA DC',330,42,12,'#16a34a','center',1);
rc(520,40,110,150,'#f6f8fc','#dde3ee',8);L('Now sending',575,56,11,'#5b6576','center',1);var w=nm[ib].split(' ');var hxs=w.pop();L(w.join(' '),575,82,11,'#1a2333','center',1);L(hxs,575,102,13,'#3b4bb0','center',1);
L(act?'bit '+bits[ib]:'idle',575,130,13,act?'#d9622b':'#5b6576','center',1);L(act?(bits[ib]?'1200 Hz':'2200 Hz'):'no carrier',575,150,11,'#5b6576','center');L('1200 bit/s',575,174,11,'#5b6576','center');
var x0=70,x1=620,cy=282,A=26;rc(x0,228,x1-x0,104,'#f8fafc','#e2e8f0',6);
ln(x0,cy,x1,cy,'#1a2333',1.5,[6,4]);L('average '+m(i,2)+' mA',x0+6,240,11,'#1a2333','left',1);L('+0.5 mA',x0-4,cy-26,11,'#5b6576','right');L('−0.5 mA',x0-4,cy+26,11,'#5b6576','right');L(m(i,1),x0-4,cy,11,'#5b6576','right',1);
var b0=Math.floor(pos-(x1-x0)/BW);for(var b=b0;b<=pos;b++){var x=x1-(pos-b)*BW;if(x>x0&&x<x1)ln(x,252,x,328,'#cbd5e1',1);var xm=x1-(pos-b-0.5)*BW,ii=bitAt(b);if(xm>x0+8&&xm<x1-8&&bits[ii]!=2)L(String(bits[ii]),xm,320,11,'#d9622b','center',1);}
C.strokeStyle='#3b4bb0';C.lineWidth=2;C.beginPath();for(var x=x0;x<=x1;x+=2){var b=pos-(x1-x)/BW,ii=bitAt(b),y=cy-(bits[ii]==2?0:A*Math.sin(phase(b)));if(x==x0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
L('Loop current, newest at the right',x1-6,240,11,'#5b6576','right');
mk(1,30,84);mk(2,500,86);mk(3,290,206);mk(4,176,82);mk(5,x1+10,cy-30);mk(6,x0+136,240);}
"""
