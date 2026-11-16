PAGE = dict(
    slug="scada-polling", grp="SCADA", name="SCADA Polling System", kw="How SCADA Polling Works",
    title="How SCADA Polling Works: RTU Poll Cycle Animated Diagram",
    desc="How SCADA polling works, animated: the master sends a request to each RTU in turn and waits for the reply. See how baud rate and registers set the poll cycle.",
    h1="How SCADA Polling Works",
    hero="Change the number of RTUs, the baud rate and the registers read in each poll. Watch the master question each RTU in turn and see how long one full poll cycle takes.",
    quick="In a polled SCADA system the master station sends a request to one RTU, waits for its reply, then moves to the next RTU. The time for one full round of all RTUs is the poll cycle, and it sets how fresh the data on the operator screen can be.",
    intro=["Most serial SCADA networks work on a master and slave basis. Field RTUs never talk on their own; they answer only when the master asks, so only one device uses the line at any time.",
           "Each poll costs time on the wire: the request frame, the RTU processing delay and the reply frame. On a slow serial link these add up quickly as RTUs and registers are added.",
           "Knowing how to estimate the poll cycle helps when you size a telemetry network, choose a baud rate or explain to operations why a value on the screen is a few seconds old."],
    sliders=[("n", "Number of RTUs on the line", 1, 20, 8, 1, 0, ""), ("baud", "Baud rate", 1200, 19200, 9600, 1200, 0, "bit/s"),
             ("reg", "Registers read per poll", 1, 60, 20, 1, 0, "")],
    outs=[("tp", "Time to poll one RTU"), ("cyc", "Full poll cycle (data refresh time)"), ("util", "Share of time spent sending frames"), ("bt", "Bytes on the line per poll")],
    legend=["SCADA master station", "Request frame from the master", "RS485 communication line", "RTU being polled", "Reply frame with register data", "Poll cycle timeline"],
    steps=["The master builds a request for one RTU with its address, the function code, the first register and the number of registers.",
           "The request travels over the shared line; every RTU hears it, but only the addressed RTU acts on it.",
           "The RTU reads its data, waits its turnaround time and sends a reply frame with the register values and a CRC.",
           "The master checks the CRC, updates its database and moves on to the next RTU, or retries after a timeout if no reply came.",
           "When the last RTU is done the cycle starts again; the time for one round is the poll cycle seen as data refresh on the screens."],
    formula=["Poll time per RTU = (request bytes + reply bytes + 7 gap characters) × 11 bits ÷ baud rate + RTU reply delay",
             "Modbus RTU style frames: request 8 bytes; reply 5 + 2 × registers bytes; each character is 11 bits on the line",
             "Full poll cycle = number of RTUs × poll time per RTU",
             "This demo assumes a fixed RTU reply delay of 20 ms and no retries",
             "Example: 20 registers at 9600 baud: (8 + 45 + 7) × 11 ÷ 9600 = 68.8 ms, plus 20 ms = 88.8 ms; 8 RTUs need about 0.71 s"],
    parts=[("SCADA master or front end processor", "Runs the poll schedule, sends requests and stores replies in its database"),
           ("Communication line", "Serial RS485, radio or leased line shared by all RTUs on the channel"),
           ("RTU", "Field unit that reads local I/O and answers only when it is addressed"),
           ("Request and reply frames", "Carry the address, function code, register data and a CRC check"),
           ("Timeout and retry settings", "Decide how long the master waits for a silent RTU before moving on")],
    uses=[("Pipeline and water networks", "Polls pumping stations, valve stations and tanks spread over long distances."),
          ("Power distribution", "Reads breaker status and feeder measurements from substation RTUs."),
          ("Oil and gas wellheads", "Collects flow, pressure and alarm data from remote well sites."),
          ("Network sizing", "Estimates whether a baud rate and number of RTUs give the refresh time operations need.")],
    pros=["Simple, deterministic access: only one device talks at a time", "Easy to detect a failed RTU from missing replies", "Works on low bandwidth serial and radio links"],
    cons=["Poll cycle grows with every RTU and register added", "A silent RTU wastes a full timeout on every cycle", "Events between polls are only seen at the next poll unless the RTU time stamps them"],
    tips=["Read registers in one block per RTU instead of many small requests; frame overhead is paid per request.",
          "Set the timeout just above the real reply time; a long timeout on a dead RTU slows the whole channel.",
          "Poll alarm and status data more often than slow values such as totals or diagnostics.",
          "Check baud rate, parity and stop bits on both ends first when an RTU gives CRC errors or no reply."],
    faq=[("What is a poll cycle in SCADA?", "It is the time the master takes to request and receive data from every RTU on a channel once. A value on the screen can be up to one poll cycle old."),
         ("Why is each character 11 bits?", "A Modbus RTU character has 1 start bit, 8 data bits, 1 parity bit and 1 stop bit, or 2 stop bits when parity is not used."),
         ("How can I make SCADA polling faster?", "Raise the baud rate if the line allows, read data in larger blocks, remove unused registers, split RTUs over more channels and shorten timeouts."),
         ("What is the difference between polling and report by exception?", "In polling the master asks every RTU every cycle. In report by exception an RTU sends data only when a value changes beyond a deadband, which saves bandwidth.")],
    cal=[],
    glo=[("modbus-rtu", "Modbus RTU"), ("rs-485", "RS 485")],
    cmp=[],
    tool=[("tools/communication-protocols/modbus-rtu-timing-calculator", "Modbus RTU Timing Calculator"), ("tools/communication-protocols/modbus-frame-decoder", "Modbus Frame Decoder")],
    blog=("scada-polling-rate-optimization", "SCADA polling rate optimization"))

SCENE = r"""
var cur=0,u=0,flash=[];for(var i=0;i<20;i++)flash.push(-9);
function rb(){return 5+2*P.reg;}
function ftm(){var cb=(8+rb()+7)*11/P.baud;return cb;}
function tp(){return ftm()+0.02;}
function upd(){var f=ftm(),t=tp();o('tp',m(t*1000,1)+' ms ('+m(f*1000,1)+' ms frames + 20 ms delay)');o('cyc',m(P.n*t,2)+' s for '+P.n+' RTU'+(P.n>1?'s':''));o('util',m(f/t*100,0)+' %');o('bt',(8+rb())+' bytes + 7 gap characters');}
function dv(){return clamp(tp()*8,0.8,3.2);}
function step(dt){u+=dt/dv();if(u>=1){u-=1;flash[cur]=T;cur++;if(cur>=P.n)cur=0;}if(cur>=P.n)cur=0;}
function px(i){return 186+(i%10)*46;}
function path(i){var x=px(i);if(i<10)return[[124,100],[x,100],[x,114]];return[[124,100],[614,100],[614,176],[x,176],[x,190]];}
function at(pts,f){var Lt=0,s=[];for(var k=1;k<pts.length;k++){var d=Math.abs(pts[k][0]-pts[k-1][0])+Math.abs(pts[k][1]-pts[k-1][1]);s.push(d);Lt+=d;}var g=f*Lt;for(var k=1;k<pts.length;k++){if(g<=s[k-1]||k==pts.length-1){var r=s[k-1]?g/s[k-1]:0;r=clamp(r,0,1);return[pts[k-1][0]+(pts[k][0]-pts[k-1][0])*r,pts[k-1][1]+(pts[k][1]-pts[k-1][1])*r];}g-=s[k-1];}return pts[0];}
function draw(){var n=P.n,c=11/P.baud,rq=(8+3.5)*c,rp=(rb()+3.5)*c,t=tp(),fa=rq/t,fb=(rq+0.02)/t;
L('Timing slowed down for viewing; bar widths are to scale',20,22,11,'#5b6576','left');
rc(20,56,104,88,'#1a2333',null,8);L('SCADA',72,72,12,'#fff','center',1);L('master',72,88,11,'#cbd5e1','center');rc(36,98,72,34,'#0f172a','#334155',4);
for(var k=0;k<3;k++)ln(42,106+k*9,42+20+30*Math.abs(Math.sin(T*2+k)),106+k*9,'#38bdf8',2);
ln(124,100,614,100,'#475569',3);if(n>10){ln(614,100,614,176,'#475569',3);ln(186,176,614,176,'#475569',3);}
for(var i=0;i<n;i++){var x=px(i),y=i<10?114:190,a=i==cur;ln(x,y-14,x,y,'#475569',2);rc(x-19,y,38,34,a?'#fff1e9':'#f8fafc',a?'#d9622b':'#94a3b8',5);if(a){C.lineWidth=2.5;C.strokeStyle='#d9622b';C.stroke();}
L('RTU',x,y+11,11,'#1a2333','center',1);L(String(i+1),x,y+25,11,'#5b6576','center');var fl=T-flash[i];ci(x+13,y+26,3.5,fl<0.8?'#22c55e':'#cbd5e1');}
var pts=path(cur),pk;if(u<fa){pk=at(pts,u/fa);rc(pk[0]-9,pk[1]-6,18,12,'#1e63b8',null,3);}else if(u>=fb){pk=at(pts,1-(u-fb)/(1-fb));rc(pk[0]-11,pk[1]-6,22,12,'#16a34a',null,3);}else{var x=px(cur),y=cur<10?114:190;L('RTU busy',x+16,y+48,11,'#d9622b','left',1);}
if(n<=10)L('Every RTU hears the request; only RTU '+(cur+1)+' is addressed and replies',400,214,11,'#5b6576','center');
var x0=150,x1=620,w=(x1-x0)/n;L('Poll cycle',20,272,12,'#1a2333','left',1);L(m(n*t,2)+' s for one round',x1,252,11,'#5b6576','right');
for(var i=0;i<n;i++){rc(x0+i*w+1,262,w-2,20,i==cur?'#d9622b':i<cur?'#93c5fd':'#e2e8f0');if(w>=22)L(String(i+1),x0+i*w+w/2,272,11,i==cur?'#fff':'#1a2333','center',1);}
ar(x0+(cur+u)*w,302,x0+(cur+u)*w,286,'#1a2333',2);
L('One RTU poll',20,327,12,'#1a2333','left',1);var bw=x1-x0;rc(x0,316,bw*fa,22,'#1e63b8');rc(x0+bw*fa,316,bw*(fb-fa),22,'#cbd5e1');rc(x0+bw*fb,316,bw*(1-fb),22,'#16a34a');
ln(x0+bw*u,312,x0+bw*u,342,'#1a2333',2);
L('request '+m(rq*1000,1)+' ms, RTU delay 20 ms, reply '+m(rp*1000,1)+' ms',x1,352,11,'#5b6576','right');
mk(1,30,56);mk(2,x0+Math.max(bw*fa/2,10),306);mk(3,560,88);mk(4,px(cur),cur<10?162:238);mk(5,x0+bw*fb+Math.max(bw*(1-fb)/2,10),306);mk(6,138,262);}
"""
