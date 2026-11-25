PAGE = dict(
    slug="2oo3-voting", grp="Safety", name="2oo3 Voting Logic", kw="How 2oo3 Voting Logic Works",
    title="How 2oo3 Voting Logic Works: Animated Diagram and PFD Formula",
    desc="How 2oo3 voting logic works, animated: three transmitters vote, any two above the trip point close the valve, and one failed transmitter cannot trip it alone.",
    h1="How 2oo3 Voting Logic Works",
    hero="Watch the fault demo: one transmitter fails high, then another sticks, and see when the shutdown valve really closes. Change the failure rate, proof test interval and common cause factor to see the average probability of failure on demand.",
    quick="In 2oo3 voting, three sensors measure the same variable and the safety system trips only when at least two of them are beyond the trip point. One failed sensor can neither cause a spurious trip nor stop a real one.",
    intro=["A safety instrumented function has to act when the process goes wrong, but it should not shut the plant down for no reason. A single transmitter cannot give both, because its one failure either blocks the trip or causes a false trip.",
           "2oo3 voting uses three transmitters and asks for agreement from any two. This gives a hardware fault tolerance of 1 for dangerous failures and also tolerates one failure in the safe direction without a spurious trip.",
           "That balance of safety and availability is why 2oo3 is common on high pressure, high level and overspeed trips on large continuous units. The price is three sensors, three input channels and careful handling of common cause failures."],
    sliders=[("lam", "Dangerous undetected failure rate λDU of one transmitter", 0.1, 5, 1, 0.1, 1, "per 10⁶ h"), ("ti", "Proof test interval TI", 0.5, 4, 1, 0.5, 1, "years"), ("beta", "Common cause factor β", 0, 10, 5, 1, 0, "%")],
    outs=[("p1", "PFDavg of one transmitter (1oo1)"), ("p3", "PFDavg of the 2oo3 sensor group"), ("cc", "Share of the 2oo3 PFDavg from common cause"), ("v", "Demo vote now")],
    legend=["Process vessel, pressure in bar", "Three pressure transmitters A, B, C on separate taps", "Trip comparators: each channel votes 1 at 8.0 bar or above", "2oo3 voting logic: trip when any two vote", "Shutdown valve on the feed, closes when its solenoid loses power", "Fault demo: what has failed right now"],
    steps=["Three independent pressure transmitters measure the same vessel pressure through separate tapping points.",
           "The logic solver compares each signal with the trip set point, and every channel at or above it casts one trip vote.",
           "The voting logic counts the votes and calls for a trip only when at least two of the three channels agree.",
           "On a trip the logic solver removes power from the solenoid, and the shutdown valve moves to its fail safe position.",
           "A single failed channel is flagged by a deviation alarm, so it can be repaired while the other two keep protecting the process."],
    formula=["PFDavg 2oo3 ≈ ((1 − β) × λDU × TI)² + β × λDU × TI ÷ 2",
             "PFDavg 1oo1 ≈ λDU × TI ÷ 2 (simplified IEC 61508 equations: no diagnostics, repair time ignored)",
             "Trip = (A AND B) OR (B AND C) OR (A AND C)",
             "Risk reduction factor RRF = 1 ÷ PFDavg",
             "Example: λDU 1.0 per 10⁶ h and TI 1 year give λDU × TI = 0.00876; with β 5 % the 2oo3 PFDavg is 0.0000693 + 0.000219 = 0.000288 (RRF about 3470), against 0.00438 for one transmitter"],
    parts=[("Three transmitters", "Measure the same variable; ideally on separate taps and impulse lines so one blockage cannot affect all three"),
           ("Input channels", "Bring each signal into the logic solver, preferably on different input cards"),
           ("Trip comparators", "Turn each analog value into a trip vote when it crosses the set point"),
           ("2oo3 voting block", "Counts the votes, trips on two out of three and raises a deviation alarm when one channel disagrees"),
           ("Final element", "Solenoid and shutdown valve that go to the safe position when power is removed")],
    uses=[("High pressure trips", "Reactor, separator and column overpressure protection."),
          ("Level trips", "High level in knock out drums and low level in boiler drums."),
          ("Machine protection", "Turbine overspeed and compressor high vibration trips with three probes."),
          ("Furnaces and heaters", "High temperature and low fuel pressure trips where spurious trips are costly.")],
    pros=["Tolerates one dangerous failure, a hardware fault tolerance of 1", "Tolerates one failure in the safe direction without a spurious trip", "One channel can be taken out for repair while the other two still protect"],
    cons=["Three transmitters, taps and input channels cost more than 1oo2 or 1oo1", "Common cause failures, such as a shared tapping point or the same calibration error, dominate the result", "More logic to configure: deviation alarms, bypass handling and degraded voting"],
    tips=["Use separate tapping points and impulse lines; three transmitters on one blocked tap are really a 1oo1 system.",
          "Configure a deviation alarm between the three channels so a stuck transmitter is found long before the proof test.",
          "Write down in the safety requirements specification how the vote degrades when one channel is bypassed or faulty, for example to 2oo2 or 1oo2.",
          "Proof test each channel through the logic solver to the final element and record the as found values."],
    faq=[("Why choose 2oo3 instead of 1oo2?", "1oo2 trips when either sensor votes, so it is very safe but trips on any single spurious signal. 2oo3 keeps the protection of a fault tolerant system while one false signal is not enough to shut down."),
         ("What happens when one transmitter fails?", "If it is stuck or reads low, the remaining two must both vote, so the group behaves as 2oo2. If it fails high, one more vote trips the plant, so it behaves as 1oo2 until the fault is repaired."),
         ("What is the common cause factor β?", "It is the fraction of failures that hit all channels at once, for example from a shared process tap, the same wrong range or a common environment. Even a few percent usually outweighs the independent failure term."),
         ("Is 2oo3 voting the same as median selection?", "Not exactly. Median selection passes the middle value to one comparator, while 2oo3 voting compares each signal with the set point and counts the votes; both trip on the same event when all channels are healthy, but diagnostics and degraded modes differ.")],
    cal=[("safety/pfdavg-calculator", "PFDavg Calculator"), ("safety/spurious-trip-rate-calculator", "Spurious Trip Rate Calculator")],
    glo=[("voting-architecture", "Voting Architecture"), ("hardware-fault-tolerance", "Hardware Fault Tolerance"), ("common-cause-failure", "Common Cause Failure")],
    cmp=[("1oo2-vs-2oo3-voting", "1oo2 vs 2oo3 Voting")],
    tool=[("tools/practice-tests/sil-and-functional-safety-quiz", "SIL and Functional Safety Quiz")],
    blog=("safety-instrumented-function-sif-design", "Safety instrumented function SIF design"))

SCENE = r"""
var t0=14.5,p=7.8,cl=false,lk='',gas=[];for(var i=0;i<36;i++)gas.push([Math.random(),Math.random(),Math.random()*6.28]);
var SP=8,TY=[120,170,220];
function sup(n){var s=String(n),q='',d='⁰¹²³⁴⁵⁶⁷⁸⁹';for(var i=0;i<s.length;i++){q+=s[i]=='-'?'⁻':d[+s[i]];}return q;}
function sc(x){var e=Math.floor(Math.log10(x)),mm=x/Math.pow(10,e);if(mm>=9.995){mm/=10;e++;}return mm.toFixed(2)+' × 10'+sup(e);}
function pf(){var lt=P.lam*1e-6*8760*P.ti,b=P.beta/100;return {one:lt/2,ind:Math.pow((1-b)*lt,2),cc:b*lt/2};}
function wr(v){return ((v%1)+1)%1;}
function tc(){return (T+t0)%24;}
function rdg(){var c=tc();return [c>=12&&c<22?6.0:p+0.04*Math.sin(T*3.1),c>=6&&c<12?10.0:p+0.04*Math.sin(T*2.3+1),p+0.04*Math.sin(T*2.7+2)];}
function votes(r){return (r[0]>=SP?1:0)+(r[1]>=SP?1:0)+(r[2]>=SP?1:0);}
function upd(){var f=pf(),t=f.ind+f.cc;o('p1',sc(f.one));o('p3',sc(t)+' (RRF '+m(1/t,0)+')');o('cc',m(f.cc/t*100,0)+' %');var v=votes(rdg());o('v',v+' of 3 votes: '+(cl?'TRIP, feed valve closed':(v==1?'alarm only, no trip':'normal')));}
function step(dt){var c=tc(),up=c>=12&&c<20,tg=cl?4.5:(up?9.6:6);p+=(tg-p)*Math.min(1,dt*(cl?0.35:0.7));var v=votes(rdg());if(v>=2)cl=true;if(cl&&c>=22&&v<2)cl=false;var k=v+'|'+cl;if(k!==lk){lk=k;upd();}}
function draw(){var c=tc(),r=rdg(),v=votes(r),st=['','',''];if(c>=12&&c<22)st[0]='stuck';if(c>=6&&c<12)st[1]='failed high';
L('Fault demo on a 24 s loop; pressure changes sped up',20,22,11,'#5b6576','left');
pipe(170,630,290,8);if(!cl){for(var k=0;k<20;k++){var x=630-((T*70+k*23)%460);if(x>512&&x<548)continue;ci(x,290,3,'#1e63b8');}}
rc(40,80,130,230,'#e2e8f0','#475569',22);
for(var i=0;i<gas.length;i++){var g=gas[i],sp=0.02+0.006*p,x=52+106*wr(g[0]+sp*Math.sin(T*3+g[2])),y=144+150*wr(g[1]+sp*Math.cos(T*2.6+g[2]));ci(x,y,2.4,'#1e63b8');}
rc(56,96,98,40,'rgba(255,255,255,0.92)','#94a3b8',6);L('Vessel',105,108,11,'#1a2333','center',1);L(m(p,2)+' bar',105,125,12,'#1e63b8','center',1);
rc(310,70,150,180,'#1a2333',null,10);L('Logic solver',385,84,12,'#cbd5e1','center',1);
for(var i=0;i<3;i++){var y=TY[i],vt=r[i]>=SP,bad=st[i]!=='';
ln(170,y,188,y,'#64748b',4);ci(205,y,17,bad?'#fee2e2':'#e0f2fe',bad?'#dc2626':'#0369a1',2);L('PT '+'ABC'[i],205,y,11,bad?'#b91c1c':'#0369a1','center',1);
C.setLineDash([5,6]);C.lineDashOffset=-T*30;ln(222,y,320,y,vt?'#dc2626':'#22c55e',2,[5,6]);C.setLineDash([]);C.lineDashOffset=0;
L(m(r[i],1)+' bar',268,y-10,11,'#1a2333','center',1);L(bad?st[i]:'healthy',268,y+11,11,bad?'#dc2626':'#16a34a','center',1);
rc(320,y-12,58,24,vt?'#dc2626':'#334155',null,5);L('ABC'[i]+' vote '+(vt?1:0),349,y,11,'#fff','center',1);ln(378,y,392,y,vt?'#f87171':'#64748b',2);}
rc(392,108,58,124,'#0f172a','#94a3b8',6);L('2oo3',421,134,13,'#fff','center',1);L(v+' of 3',421,160,12,'#cbd5e1','center',1);
var bl=cl?0.6+0.4*Math.sin(T*9):1;L(cl?'TRIP':'OK',421,190,13,cl?'rgba(248,113,113,'+bl+')':'#4ade80','center',1);if(cl&&v<2)L('latched',421,212,11,'#fca5a5','center',1);
L('Trip at '+m(SP,1)+' bar',385,242,11,'#fde68a','center',1);
var oc=cl?'#dc2626':'#22c55e';ln(460,170,530,170,oc,2.5,cl?[6,5]:null);ln(530,170,530,232,oc,2.5,cl?[6,5]:null);
rc(512,232,36,22,cl?'#fee2e2':'#dcfce7','#475569',4);L('S',530,243,11,'#1a2333','center',1);ln(530,254,530,282,'#475569',3);
C.fillStyle=cl?'#dc2626':'#ffffff';C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(512,278);C.lineTo(548,302);C.lineTo(548,278);C.lineTo(512,302);C.closePath();C.fill();C.stroke();
L('SDV '+(cl?'closed':'open'),556,243,11,cl?'#b91c1c':'#16a34a','left',1);L('Feed in',626,320,11,'#1e63b8','right',1);
L(cl?'Solenoid power off':'Solenoid powered',538,150,11,oc,'center',1);
var ph=c<6?'Normal: all three healthy, no votes':c<12?'PT B failed high: 1 vote only, alarm, no spurious trip':c<22?(cl?'PT A stuck at 6 bar: B and C still voted, valve closed':'PT A stuck at 6 bar while the pressure rises'):'Trip latched until reset; operator reset, PT A repaired';
L(ph,46,340,12,'#1a2333','left',1);
mk(1,50,90);mk(2,186,100);mk(3,322,98);mk(4,452,110);mk(5,496,243);mk(6,30,340);}
"""
