PAGE = dict(
    slug="modbus-rtu", grp="Signals", name="Modbus RTU Communication", kw="How Modbus RTU Communication Works",
    title="How Modbus RTU Communication Works: Frame, CRC and Timing",
    desc="How Modbus RTU communication works, animated: the master sends a function 03 request, the slave replies, with live CRC bytes and frame timing.",
    h1="How Modbus RTU Communication Works",
    hero="Change the baud rate, the slave address and the number of holding registers read. Watch the request and reply frames travel on the RS 485 line, the CRC bytes recalculate and the frame times change.",
    quick="Modbus RTU is a master and slave protocol on a serial line, usually RS 485. The master sends a frame with the slave address, a function code, data and a CRC; only the addressed slave answers, and frames are separated by a silent gap of at least 3.5 character times.",
    intro=["Modbus RTU is one of the most common field protocols for energy meters, VFDs, flow computers, analysers and small PLCs. It runs on a two wire RS 485 line that can carry up to 32 unit loads per segment.",
           "Only the master starts a transaction. Each slave has an address from 1 to 247, listens to every frame on the line and replies only when the address matches.",
           "A frame has no start or end character. The receiver finds the frame boundaries from silent gaps on the line and checks every frame with a 16 bit CRC."],
    sliders=[("baud", "Baud rate", 2400, 38400, 9600, 2400, 0, "bit/s"), ("addr", "Slave address", 1, 247, 17, 1, 0, ""), ("n", "Holding registers read (function 03)", 1, 7, 3, 1, 0, "")],
    outs=[("ch", "Character time = 11 bits ÷ baud rate"), ("req", "Request frame (8 bytes) and its CRC"), ("rep", "Reply frame (5 + 2 × N bytes)"), ("tt", "Silent gap t3.5 and total transaction time")],
    legend=["Modbus master (PLC, SCADA or HMI)", "RS 485 two wire line", "Line termination resistors", "Addressed slave", "Request frame bytes", "Reply frame bytes", "Frame timing to scale"],
    steps=["The master waits for a silent line of at least 3.5 character times, then sends the slave address, function code, start register, quantity and CRC.",
           "Every slave receives the frame and checks the CRC; a frame with a wrong CRC is ignored.",
           "Only the slave whose address matches executes the request and reads the holding registers.",
           "After a silent gap, the slave replies with its address, the function code, a byte count, the register data and a new CRC.",
           "The master checks the CRC of the reply, stores the values and moves on to the next request after another silent gap."],
    formula=["Character time = 11 bits ÷ baud rate (1 start, 8 data, 1 parity, 1 stop, or 2 stop bits without parity)",
             "Function 03 request = 8 bytes; reply = 5 + 2 × N bytes for N registers",
             "Silent gap t3.5 = 3.5 × character time; above 19200 bit/s it is fixed at 1.75 ms",
             "Transaction time = (8 + 5 + 2 × N) × character time + 2 × t3.5, not counting slave processing time",
             "Example: 9600 bit/s, slave 17, N 3, start register 006B hex: character 1.146 ms, request 11 03 00 6B 00 03 76 87 = 9.17 ms, reply 11 bytes = 12.60 ms, t3.5 = 4.01 ms, total = 19 × 1.146 + 2 × 4.01 = 29.79 ms"],
    parts=[("Master", "Starts every transaction and handles timeouts and retries"),
           ("Slave devices", "Answer only frames with their own address; address 0 is a broadcast with no reply"),
           ("RS 485 transceivers", "Drive the differential A and B lines and switch between send and receive"),
           ("Termination resistors", "About 120 Ω at each end of the trunk to stop reflections"),
           ("CRC 16", "Two check bytes, low byte first, calculated over the whole frame")],
    uses=[("Energy meters", "A PLC or SCADA reads voltage, current and energy registers."),
          ("Drives", "Speed reference, run command and fault codes over one cable."),
          ("Package units", "Compressor, chiller and analyser panels report data to the DCS."),
          ("Remote I/O and RTUs", "Low cost serial links to small outstations.")],
    pros=["Simple, open and supported by almost every controller", "Needs only a twisted pair over long distances", "Easy to diagnose with a serial sniffer"],
    cons=["Slow compared with Ethernet; one master asks one slave at a time", "No built in data types, so word order and scaling must be agreed", "A single bad device or wrong termination can upset the whole line"],
    tips=["Set the same baud rate, parity and stop bits on the master and every slave; one mismatch gives CRC errors or silence.",
          "Use shielded twisted pair, a daisy chain topology and termination only at the two ends of the trunk.",
          "Check the register map for the offset: register 40108 in a manual is often address 006B hex in the frame.",
          "Set the master timeout longer than the slave response time, and keep retries low so one dead slave does not slow the whole poll cycle."],
    faq=[("Why is the CRC sent low byte first?", "The Modbus serial specification sends the CRC low order byte first. In the example the CRC is 8776 hex and the frame ends with 76 87."),
         ("What is the 3.5 character gap for?", "RTU frames have no start or end marker. A silent time of at least 3.5 characters tells every device that one frame has ended and the next can start."),
         ("How many devices can be on one Modbus RTU line?", "Addresses run from 1 to 247, but one RS 485 segment carries 32 unit loads. More devices need repeaters or low load transceivers."),
         ("What is the difference between Modbus RTU and Modbus TCP?", "RTU uses binary frames with a CRC on a serial line. TCP wraps the same function codes in an Ethernet packet with an MBAP header and no CRC.")],
    cal=[],
    glo=[("modbus-rtu", "Modbus RTU"), ("rs-485", "RS 485"), ("modbus-tcp", "Modbus TCP")],
    cmp=[],
    tool=[("tools/communication-protocols/modbus-crc-calculator", "Modbus CRC Calculator"), ("tools/communication-protocols/modbus-rtu-timing-calculator", "Modbus RTU Timing Calculator"), ("tools/communication-protocols/modbus-frame-decoder", "Modbus Frame Decoder")],
    blog=("modbus-protocol-explained", "Modbus protocol explained"))

SCENE = r"""
var CH=0.16,u=0,ph=0,dat=[555,0,100,0,0,0,0];
function crc(b){var c=0xFFFF;for(var i=0;i<b.length;i++){c^=b[i];for(var j=0;j<8;j++)c=(c&1)?((c>>1)^0xA001):(c>>1);}return c;}
function hx(b){return ('0'+b.toString(16).toUpperCase()).slice(-2);}
function rq(){var b=[P.addr,3,0,0x6B,0,P.n],c=crc(b);b.push(c&255,c>>8);return b;}
function rp(){var b=[P.addr,3,2*P.n];for(var i=0;i<P.n;i++){b.push(dat[i]>>8,dat[i]&255);}var c=crc(b);b.push(c&255,c>>8);return b;}
function ct(){return 11/P.baud;}
function t35(){return P.baud>19200?0.00175:3.5*ct();}
function upd(){var c=ct(),r=rq(),nr=5+2*P.n;o('ch',m(c*1000,3)+' ms');o('req',m(8*c*1000,2)+' ms, CRC '+hx(r[6])+' '+hx(r[7]));o('rep',nr+' bytes, '+m(nr*c*1000,2)+' ms');o('tt','t3.5 '+m(t35()*1000,2)+' ms, total '+m(((13+2*P.n)*c+2*t35())*1000,2)+' ms');}
function seg(){var a=8*CH,g=3.5*CH,b=(5+2*P.n)*CH;return [a,g,b,g];}
function step(dt){var s=seg(),tot=s[0]+s[1]+s[2]+s[3];u+=dt;if(u>=tot){u-=tot;dat[0]=555+Math.round(12*Math.sin(T/2));dat[1]=Math.round(40+30*Math.sin(T/3));dat[2]=100+Math.round(5*Math.cos(T));}}
function others(){return [P.addr==1?2:1,P.addr==247?246:247];}
function row(b,y,k,lab,col){var w=26,x0=40;L(lab,x0,y-21,11,'#1a2333','left',1);for(var i=0;i<b.length;i++){var x=x0+i*(w+2),f=i==0?'#dbeafe':i==1?'#ede9fe':i>=b.length-2?'#ffedd5':'#f1f5f9';
if(k>=0&&i==Math.floor(k))f=col;else if(k>=0&&i>k)f='#ffffff';rc(x,y-11,w,22,f,'#94a3b8',3);L(hx(b[i]),x+w/2,y,11,(k>=0&&i==Math.floor(k))?'#fff':'#1a2333','center',1);}}
function draw(){var s=seg(),a=s[0],g=s[1],b=s[2],r=rq(),p=rp(),sx=[230,380,530],ad=[others()[0],P.addr,others()[1]],sl=1;
L('Slowed down: one byte per 0.16 s; timing bar is to scale',20,22,11,'#5b6576','left');
rc(20,46,104,70,'#1a2333',null,8);L('Master',72,62,12,'#fff','center',1);L('function 03',72,80,11,'#cbd5e1','center');L(m(P.baud,0)+' bit/s',72,98,11,'#fbbf24','center',1);
ln(124,76,612,76,'#1e63b8',2.5);ln(124,86,612,86,'#c2410c',2.5);L('A',614,76,11,'#1e63b8','left',1);L('B',614,86,11,'#c2410c','left',1);
rc(140,70,10,22,'#fef3c7','#92400e',2);rc(596,70,10,22,'#fef3c7','#92400e',2);L('120 Ω',145,104,11,'#92400e','center',1);L('120 Ω',601,104,11,'#92400e','center',1);
for(var i=0;i<3;i++){var x=sx[i],act=i==sl;ln(x,86,x,118,'#475569',2);rc(x-36,118,72,42,act?'#fff1e9':'#f8fafc',act?'#d9622b':'#94a3b8',6);L('Slave',x,131,11,'#1a2333','center',1);L('address '+ad[i],x,147,11,act?'#d9622b':'#5b6576','center',1);}
var t=u,px=null,lab='',col='#1e63b8';if(t<a){var f=t/a;px=124+f*(612-124);lab='Request';col='#1e63b8';}else if(t<a+g){lab='Silent t3.5';}else if(t<a+g+b){var f=(t-a-g)/b;px=sx[sl]-f*(sx[sl]-124);lab='Reply';col='#16a34a';}else lab='Silent t3.5';
if(px!==null){rc(px-24,64,48,32,col,null,5);L(lab,px,80,11,'#fff','center',1);}else{L(lab,370,58,11,'#5b6576','center',1);}
if(t<a){for(var i=0;i<3;i++){var x=sx[i];if(px>x){var ok=i==sl;L(ok?'Address match':'Ignore',x,172,11,ok?'#16a34a':'#5b6576','center',1);}}}
if(t>=a&&t<a+g)L('Checking CRC',sx[sl],172,11,'#d9622b','center',1);
var kq=t<a?t/CH:-1,kp=(t>=a+g&&t<a+g+b)?(t-a-g)/CH:-1;
row(r,212,t<a?kq:-1,'Request: address, function, start register, quantity, CRC','#1e63b8');
row(p,268,kp,'Reply: address, function, byte count, data, CRC','#16a34a');
var c=ct(),T35=t35(),ta=8*c,tb=(5+2*P.n)*c,tot=ta+tb+2*T35,x0=40,x1=620,W=x1-x0,X=function(v){return x0+v/tot*W;};
L('One transaction, real time '+m(tot*1000,2)+' ms',x0,304,11,'#1a2333','left',1);
rc(X(0),314,X(ta)-X(0),20,'#1e63b8');rc(X(ta),314,X(ta+T35)-X(ta),20,'#e2e8f0');rc(X(ta+T35),314,X(ta+T35+tb)-X(ta+T35),20,'#16a34a');rc(X(ta+T35+tb),314,X(tot)-X(ta+T35+tb),20,'#e2e8f0');
var tr=[0,a,a+g,a+g+b,a+g+b+g],rr=[0,ta,ta+T35,ta+T35+tb,tot],q=0;for(var i=0;i<4;i++)if(t>=tr[i]&&t<tr[i+1])q=rr[i]+(t-tr[i])/(tr[i+1]-tr[i])*(rr[i+1]-rr[i]);ln(X(q),310,X(q),338,'#1a2333',2);
L('request '+m(ta*1000,2)+' ms, gap '+m(T35*1000,2)+' ms, reply '+m(tb*1000,2)+' ms',x1,348,11,'#5b6576','right');
mk(1,30,46);mk(2,470,96);mk(3,182,104);mk(4,sx[sl]+44,118);mk(5,600,212);mk(6,600,268);mk(7,26,324);}
"""
