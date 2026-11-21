PAGE = dict(
    slug="plc-shift-register", grp="PLC", name="PLC Shift Register", kw="How a PLC Shift Register Works",
    title="How a PLC Shift Register Works: Animated Diagram and Example",
    desc="How a PLC shift register works, animated: an inspection bit enters bit 0, shifts one place per part and fires the reject pusher at the right bit.",
    h1="How a PLC Shift Register Works",
    hero="Set where the reject pusher sits, counted in part positions from the inspection point, and the conveyor rate. Watch each bad part load a 1 into bit 0, ride along the register one bit per part and fire the pusher when it reaches the chosen bit.",
    quick="A PLC shift register moves every bit of a word or bit array one place on each clock pulse and loads a new bit at the first position. On a conveyor, one bit per part position lets the PLC remember which parts failed inspection until they reach the reject station.",
    intro=["Many machines inspect a product at one point and act on it further down the line. The PLC must remember the result for every part between the two points, even when several parts are on the way.",
           "A shift register does this with one bit per part position. A clock pulse from a part sensor or encoder shifts all bits one place, and the inspection result is loaded into the first bit at the same time.",
           "The bit at the reject position is then wired to the pusher output. In IEC 61131 3 this is done with the SHL or SHR function on a word, and many PLCs also have bit shift instructions such as BSL and BSR."],
    sliders=[("n", "Reject pusher position (bits after inspection)", 2, 15, 8, 1, 0, ""), ("ppm", "Conveyor rate", 10, 60, 30, 1, 0, "parts/min")],
    outs=[("pt", "Pitch time = 60 ÷ parts per minute"), ("dl", "Delay from inspection to reject = N × pitch time"), ("wd", "Register word now (decimal)"), ("rj", "Bad parts rejected so far")],
    legend=["Inspection sensor loads the data bit", "Clock pulse: one shift per part pitch", "Shift register, bit 0 on the left", "Reject pusher output driven by bit N", "Bad part tracked by a 1 bit", "Ladder logic for the shift and the output"],
    steps=["The inspection sensor checks the part that has just arrived at position 0 and gives a 1 for a bad part and a 0 for a good one.",
           "A clock pulse, made once per part pitch by a sensor or an encoder count, triggers the shift instruction.",
           "All bits move one place towards the reject station, the oldest bit drops out of the end and the new result is loaded into bit 0.",
           "Because the bits move exactly as the parts move, bit N always belongs to the part at position N.",
           "When bit N is 1, the PLC fires the reject pusher and that bad part is removed from the line."],
    formula=["Shift left of a 16 bit word with data input d: new word = (old word × 2 + d) AND 65535",
             "Pitch time = 60 ÷ parts per minute",
             "Delay from inspection to reject = N × pitch time",
             "Reject output = bit N of the register word",
             "Example: N 8, 30 parts/min: pitch time = 60 ÷ 30 = 2 s, delay = 8 × 2 = 16 s; word 37 (0000 0000 0010 0101) shifted with d = 1 gives 37 × 2 + 1 = 75 (0000 0000 0100 1011)"],
    parts=[("Data input", "Inspection sensor, camera or weigh check result for the part at position 0"),
           ("Clock input", "Part sensor or encoder count that gives one pulse per part pitch"),
           ("Shift register", "Word or bit array; SHL, SHR, BSL or BSR instruction in the PLC"),
           ("Reject output", "Bit N driving a solenoid valve for the pusher or air jet"),
           ("Reset", "Clears the register at start up or after a jam so old data does not fire the pusher")],
    uses=[("Reject tracking", "Removes failed bottles, cans or packs at a reject station downstream."),
          ("Bottling and filling lines", "Tracks empty positions so fill valves stay closed."),
          ("Indexing machines", "Follows parts through stations on a rotary table."),
          ("Sorting conveyors", "Holds the destination code of each part until it reaches its diverter.")],
    pros=["Simple and fast; one instruction per clock", "Tracks many parts at once with one word", "Easy to see on a programming terminal as a row of bits"],
    cons=["Only works if parts stay at a fixed pitch with no slip", "A missed or double clock pulse shifts all data out of step", "Needs a reset strategy after jams, manual removal or power loss"],
    tips=["Use a one shot on the clock input so the register shifts only once per pulse, however long the sensor stays on.",
          "Make the clock from an encoder count when possible; a part sensor can miss gaps in the product flow.",
          "Check the bit numbering in your PLC: on some platforms SHL moves bits towards the higher number, BSL works on a bit array.",
          "Add a reject confirm sensor after the pusher and alarm if a 1 bit passes without a confirmed reject."],
    faq=[("What is the difference between SHL and BSL?", "SHL in IEC 61131 3 shifts a whole word by a number of bits and fills with zeros. BSL type instructions shift a bit array by one and load the data bit you give it."),
         ("Why does the register need a clock?", "The bits must move exactly when the parts move one pitch. Shifting every PLC scan would push the data out of the register in milliseconds."),
         ("What happens if a part is removed by hand?", "Its bit keeps travelling, so the pusher may fire on an empty position or a good part. Many lines clear the register or use a tracking sensor before the reject station."),
         ("How long can a shift register be?", "As long as the PLC memory allows. Words can be chained, or a bit array of hundreds of bits can be used for a long conveyor.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator"), ("plc-signal/encoder-rpm-calculator", "Encoder RPM Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("plc-shift-register-shl-shr", "PLC shift register SHL and SHR"))

SCENE = r"""
var c=20,u=0,reg=0,rej={},cnt=0,lastQ=-9,clk=-9,pre=0;
function bad(k){return ((k*7+3)%10)<2;}
function pt(){return 60/P.ppm;}
function upd(){if(!pre){pre=1;reg=0;for(var k=c-15;k<=c;k++)reg=((reg<<1)|(bad(k)?1:0))&65535;}o('pt',m(pt(),2)+' s');o('dl',m(P.n*pt(),1)+' s');o('wd',String(reg));o('rj',String(cnt));}
function bit(i){return (reg>>i)&1;}
function step(dt){u+=dt/pt();if(u>=1){u-=1;c++;reg=((reg<<1)|(bad(c)?1:0))&65535;clk=T;if(bit(P.n)){rej[c-P.n]=T;lastQ=T;cnt++;}o('wd',String(reg));o('rj',String(cnt));}}
function X(p){return 48+p*36;}
function draw(){var mv=sm((u-0.6)/0.4),N=P.n,q=T-lastQ<0.6,bx=null;
L('Bit 0 is drawn on the left so bits move with the parts; demo marks 1 part in 5 as bad',20,22,11,'#5b6576','left');
rc(20,118,600,14,'#475569',null,4);C.setLineDash([10,10]);C.lineDashOffset=-(c+mv)*36;ln(24,125,616,125,'#94a3b8',2);C.setLineDash([]);C.lineDashOffset=0;
rc(X(N)-34,38,68,26,'#fee2e2','#b91c1c',4);L('Reject bin',X(N),51,11,'#b91c1c','center',1);
for(var k=c-16;k<=c+1;k++){var p=(c-k)+mv;if(p<-0.8||p>15.6)continue;var x=X(p),y=92,b=bad(k);
if(b&&rej[k]===undefined&&(c-k)>N)continue;if(rej[k]!==undefined){var e=T-rej[k];if(e>0.6)continue;y=92-60*sm(e/0.6);x=X(c-k);}
if(b&&rej[k]===undefined&&bx===null&&p>1.5&&Math.abs(p-N)>0.9)bx=x;rc(x-13,y,26,26,b?'#fca5a5':'#d6a86a',b?'#b91c1c':'#8a5a2b',3);if(b)L('✕',x,y+13,12,'#7f1d1d','center',1);}
var ext=q?16*Math.sin(Math.PI*clamp((T-lastQ)/0.6,0,1)):0;rc(X(N)-10,152-ext,20,10,'#334155');rc(X(N)-14,162,28,14,'#64748b',null,3);L('Pusher',X(N)+20,170,11,'#1a2333','left',1);
rc(X(0)-16,58,32,18,'#334155',null,4);L('I0.1',X(0),67,11,'#fff','center',1);C.globalAlpha=0.55+0.45*Math.sin(T*9);ln(X(0),76,X(0),90,'#ef4444',2,[3,3]);C.globalAlpha=1;L('Inspect',X(0)+20,67,11,'#5b6576','left',1);
var cf=T-clk<0.25;ci(X(0)-22,150,7,cf?'#f59e0b':'#475569');L('Clock I0.0',X(0)-12,150,11,'#1a2333','left',1);rc(X(1)+10,144,90,8,'#e2e8f0');rc(X(1)+10,144,90*u,8,'#f59e0b');L('next shift',X(1)+106,148,11,'#5b6576','left');
L('Register R, one bit per part position',20,190,11,'#1a2333','left',1);
for(var i=0;i<16;i++){var b=bit(i),x=X(i),hl=i==N;rc(x-15,198,30,26,b?'#fecaca':'#f1f5f9',hl?'#d9622b':'#94a3b8',3);if(hl){C.lineWidth=2.5;C.strokeStyle='#d9622b';C.stroke();}L(String(b),x,211,13,b?'#b91c1c':'#5b6576','center',1);L(String(i),x,232,11,'#5b6576','center');}
if(T-clk<0.4){var a=1-(T-clk)/0.4;C.globalAlpha=a;for(var i=0;i<15;i+=3)ar(X(i)+8,244,X(i+1)-8,244,'#16a34a',2);C.globalAlpha=1;}
ln(X(N),198,X(N),178,'#d9622b',1.5,[3,3]);
var R0=20,R1=620;ln(R0,262,R0,350,'#1a2333',3);ln(R1,262,R1,350,'#1a2333',3);
function ct(x,y,lab,on){var col=on?'#16a34a':'#475569';ln(x-6,y-10,x-6,y+10,col,2.5);ln(x+6,y-10,x+6,y+10,col,2.5);L(lab,x,y-18,11,'#1a2333','center',1);}
ln(R0,284,74,284,'#16a34a',2);ct(80,284,'I0.0  P',cf);ln(86,284,150,284,cf?'#16a34a':'#475569',2);
rc(150,268,170,32,'#fff','#c2410c',5);L('SHL  R,  data I0.1',235,284,12,'#1a2333','center',1);ln(320,284,R1,284,'#475569',2);
var bs='';for(var i=15;i>=0;i--){bs+=bit(i);if(i%4==0&&i)bs+=' ';}L(bs+'  = '+reg,R1-8,270,11,'#1e63b8','right',1);
ln(R0,332,74,332,'#16a34a',2);ct(80,332,'R bit '+N,bit(N)==1);ln(86,332,520,332,bit(N)==1?'#16a34a':'#475569',2);
C.strokeStyle=q?'#16a34a':'#475569';C.lineWidth=2.5;C.beginPath();C.arc(534,332,12,Math.PI*0.65,Math.PI*1.35);C.stroke();C.beginPath();C.arc(534,332,12,-Math.PI*0.35,Math.PI*0.35);C.stroke();L('Q0.0 pusher',534,312,11,'#1a2333','center',1);ln(548,332,R1,332,'#475569',2);
mk(1,X(0)-30,67);mk(2,X(1)+190,148);mk(3,X(15)+12,186);mk(4,X(N)-30,168);mk(5,bx!==null?bx:X(N)+34,bx!==null?80:51);mk(6,R0+20,306);}
"""
