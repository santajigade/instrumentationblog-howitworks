PAGE = dict(
    slug="dcs-controller-redundancy", grp="DCS", name="DCS Controller Redundancy", kw="How DCS Controller Redundancy Works",
    title="How DCS Controller Redundancy Works: Animated Diagram",
    desc="How DCS controller redundancy works, animated: hot standby tracking, heartbeat loss, bumpless switchover and the availability gained from a redundant pair.",
    h1="How DCS Controller Redundancy Works",
    hero="Set the MTBF and repair time of one controller and the heartbeat timeout. Watch the standby controller track the primary, detect its failure and take over while the valve output holds steady.",
    quick="A redundant DCS controller is a pair: one primary runs the control strategy and a hot standby tracks its data every cycle. If the primary fails, the standby detects the lost heartbeat and takes over the I/O bus without a bump in the outputs.",
    intro=["A DCS controller may run hundreds of control loops, so losing it can trip a whole unit. For that reason controllers in critical service are almost always installed as a redundant pair in the same rack or in two linked racks.",
           "Both controllers hold the same configuration, but only the primary writes to the I/O. The standby receives a copy of every changed value over a dedicated redundancy link, so it is ready to continue from exactly the same point.",
           "Redundancy only helps if the failure is detected quickly and the switchover is bumpless. It also does not protect against faults that hit both controllers together, such as a shared power supply, a wrong download or a cabinet fire."],
    sliders=[("mtbf", "MTBF of one controller", 20000, 500000, 100000, 10000, 0, "h"), ("mttr", "Mean time to repair", 1, 72, 8, 1, 0, "h"),
             ("hb", "Heartbeat timeout", 50, 1000, 200, 50, 0, "ms")],
    outs=[("a1", "Single controller availability"), ("a2", "Redundant pair, ideal (no common cause)"), ("sw", "Failure detected and standby in control"), ("st", "Demo state")],
    legend=["Controller A (primary at start)", "Controller B (hot standby)", "Redundancy link: data tracking and heartbeat", "Redundant control network to operator stations", "I/O bus to the I/O modules", "Field devices: transmitter and control valve", "Switchover timeline and valve output"],
    steps=["Both controllers start with the same configuration; one is elected primary and the other becomes the hot standby.",
           "Every cycle the primary reads inputs, runs the control strategy and sends the changed data to the standby over the redundancy link.",
           "Both controllers exchange a heartbeat; the standby also checks the primary diagnostics and its own readiness.",
           "If the heartbeat stops for longer than the timeout, or the primary reports a hard fault, the standby takes over the I/O bus and continues from the tracked values.",
           "During the switchover the I/O modules hold their last output values, so the valves do not move; after repair the new unit loads the database and becomes the standby."],
    formula=["Availability A = MTBF ÷ (MTBF + MTTR)",
             "Unavailability U = 1 − A, downtime per year ≈ U × 8760 h",
             "Ideal redundant pair: U pair ≈ U × U (two independent units, each repaired before the other fails)",
             "Common cause faults, failed switchovers and an unready standby are not in this formula, so real figures are lower",
             "Example: MTBF 100 000 h, MTTR 8 h: A = 100 000 ÷ 100 008 = 99.992 % (about 42 min down per year); ideal pair U = 6.4 × 10⁻⁹, about 0.2 s per year"],
    parts=[("Primary controller", "Runs the control strategy and is the only unit that writes to the I/O"),
           ("Standby controller", "Tracks all data from the primary and is ready to take control at any moment"),
           ("Redundancy link", "Dedicated connection for data tracking, heartbeat and role negotiation"),
           ("Redundant networks and I/O bus", "Two paths to the operator stations and to the I/O so one cable fault does not stop the system"),
           ("Redundant power supplies", "Separate feeds for each controller so one supply fault does not take out the pair")],
    uses=[("Continuous process units", "Refinery, chemical and power plants where a controller trip would stop production."),
          ("Online maintenance", "Lets a controller module be replaced or a firmware upgrade done while the process keeps running."),
          ("Critical control loops", "Protects compressor, furnace and reactor controls that must never lose their output."),
          ("Remote unmanned sites", "Keeps pipelines and pumping stations running until a technician can reach the site.")],
    pros=["Very high availability of the control function", "Bumpless takeover without operator action", "Controllers can be repaired or replaced online"],
    cons=["Higher cost for hardware, cabinet space and power", "Does not cover common cause faults such as bad configuration or shared power", "A standby that is not synchronised gives false confidence"],
    tips=["Check the redundancy status on the system diagnostics every shift; a standby that shows not synchronised gives no protection.",
          "Test a manual switchover during planned maintenance to prove the standby really takes control.",
          "Feed the two controllers from separate power supplies and, where possible, separate circuits.",
          "After replacing a failed controller, wait until the database transfer is complete before treating the pair as redundant again."],
    faq=[("What is hot standby redundancy?", "The standby controller is powered, loaded with the same configuration and receives live data from the primary. It can take over within a short time without reloading anything."),
         ("Do the field outputs change during a switchover?", "They should not. The I/O modules hold their last values during the short gap, and the standby continues from the tracked data, so the takeover is bumpless."),
         ("How is a controller failure detected?", "By internal diagnostics in the primary and by the heartbeat on the redundancy link. If the standby stops receiving the heartbeat for longer than the timeout, it takes control."),
         ("Does controller redundancy make the DCS a safety system?", "No. Redundancy improves availability of control, but safety functions belong in a separate safety instrumented system designed to IEC 61511.")],
    cal=[("safety/availability-calculator", "Availability Calculator"), ("safety/mtbf-calculator", "MTBF Calculator")],
    glo=[("plc-redundancy", "PLC Redundancy"), ("mtbf", "MTBF"), ("common-cause-failure", "Common Cause Failure")],
    cmp=[],
    blog=("dcs-controller-redundancy-types", "DCS controller redundancy types"))

SCENE = r"""
var cy=4.6,TF=5.5,TR=12,TS=15,PER=20;
function tv(){return 0.3+P.hb/1000*2;}
function dt_(h){if(h>=1)return m(h,1)+' h';if(h*60>=1)return m(h*60,0)+' min';var s=h*3600;return s>=0.01?m(s,2)+' s':'below 0.01 s';}
function stA(t){if(t<TF)return'act';if(t<TR)return'fail';if(t<TS)return'sync';return'stby';}
function stB(t){if(t<TF)return'stby';if(t<TF+tv())return'wait';return'act';}
function evt(t){if(t<TF)return'Normal: A in control, B tracking';if(t<TF+tv())return'A failed, B waiting for heartbeat timeout';if(t<TR)return'B in control, outputs unchanged';if(t<TS)return'A replaced, loading database from B';return'B primary, A hot standby';}
function upd(){var A=P.mtbf/(P.mtbf+P.mttr),U=1-A;o('a1',m(A*100,4)+' % (about '+dt_(U*8760)+' down per year)');
o('a2',m((1-U*U)*100,6)+' % (about '+dt_(U*U*8760)+' per year)');o('sw','about '+m(P.hb,0)+' ms; I/O holds last values');o('st',evt(cy));}
function step(dt){cy+=dt;if(cy>=PER)cy-=PER;upd();}
function ctl(x,y,name,s){if(s=='fail'){C.globalAlpha=0.3;ln(x+12,y+8,x+138,y+72,'#b91c1c',3);ln(x+138,y+8,x+12,y+72,'#b91c1c',3);C.globalAlpha=1;}var col=s=='act'?'#16a34a':s=='fail'?'#b91c1c':s=='wait'?'#a8620a':'#1e63b8';rc(x,y,150,80,s=='fail'?'rgba(255,255,255,0.6)':'#ffffff',col,8);C.lineWidth=2.5;C.strokeStyle=col;C.stroke();
L(name,x+75,y+18,13,'#1a2333','center',1);var t=s=='act'?'ACTIVE':s=='fail'?'FAILED':s=='wait'?'STANDBY, checking':s=='sync'?'LOADING DATABASE':'HOT STANDBY';rc(x+14,y+34,122,22,col,null,4);L(t,x+75,y+45,11,'#fff','center',1);
for(var k=0;k<4;k++){ci(x+30+k*30,y+68,4,s=='fail'?'#475569':(k==0||(Math.sin(T*6+k*1.7)>0)?col:'#cbd5e1'));}
}
function pk(x1,x2,y,c,sp){C.setLineDash([5,9]);C.lineDashOffset=-T*sp;ln(x1,y,x2,y,c,3,[5,9]);C.setLineDash([]);C.lineDashOffset=0;}
function draw(){var a=stA(cy),b=stB(cy),aAct=a=='act',bAct=b=='act';
L('Timeout and switchover slowed down',20,22,11,'#5b6576','left');
rc(440,10,150,26,'#1a2333',null,6);L('Operator station',515,23,11,'#fff','center',1);ln(515,36,515,50,'#475569',2);
ln(100,47,560,47,'#0e7490',2.5);ln(100,53,560,53,'#0e7490',2.5);L('Control network A and B',330,40,11,'#0e7490','center',1);
ln(185,53,185,70,'#475569',2);ln(455,53,455,70,'#475569',2);
ctl(110,70,'Controller A',a);ctl(380,70,'Controller B',b);
L('Redundancy link',320,82,11,'#5b6576','center',1);ln(260,98,380,98,'#94a3b8',2);ln(260,122,380,122,'#94a3b8',2);
if(aAct)pk(262,378,98,'#6b3fb0',40);else if(bAct&&a!='fail')pk(378,262,98,'#6b3fb0',-40);
L('data',320,108,11,'#6b3fb0','center');
var hbA=a!='fail',hbB=true;var ph=(T*1.5)%1;if(hbA){ci(262+116*ph,122,4,'#d9622b');}if(hbB){ci(378-116*ph,122,4,'#1e63b8');}L('heartbeat',320,134,11,'#d9622b','center');
var by=184;ln(100,by,560,by,'#475569',3);L('I/O bus',100,by+12,11,'#475569','left',1);
ln(185,150,185,by,aAct?'#16a34a':'#cbd5e1',3);ln(455,150,455,by,bAct?'#16a34a':'#cbd5e1',3);
if(aAct){C.setLineDash([4,6]);C.lineDashOffset=-T*30;ln(185,150,185,by,'#16a34a',3,[4,6]);}if(bAct){C.setLineDash([4,6]);C.lineDashOffset=-T*30;ln(455,150,455,by,'#16a34a',3,[4,6]);}C.setLineDash([]);C.lineDashOffset=0;
var ioOn=aAct||bAct;if(ioOn)pk(102,558,by,'#16a34a',aAct?40:-40);
rc(200,198,90,32,'#f6f8fc','#64748b',4);L('AI module',245,214,11,'#1a2333','center',1);rc(350,198,90,32,'#f6f8fc','#64748b',4);L('AO module',395,214,11,'#1a2333','center',1);
ln(245,by,245,198,'#475569',2);ln(395,by,395,198,'#475569',2);ln(245,230,245,244,'#475569',2);ln(395,230,395,244,'#475569',2);
ci(245,256,12,'#e0f2fe','#0e7490',2);L('PT',245,256,11,'#0e7490','center',1);L('Transmitter',245,280,11,'#5b6576','center');
C.fillStyle='#cbd5e1';C.beginPath();C.moveTo(381,248);C.lineTo(409,264);C.lineTo(409,248);C.lineTo(381,264);C.closePath();C.fill();C.strokeStyle='#475569';C.lineWidth=1.5;C.stroke();ln(395,256,395,244,'#475569',2);
L('Valve 62 %'+(ioOn?'':' held'),395,280,11,ioOn?'#5b6576':'#a8620a','center',1);
var x0=170,x1=620,X=function(t){return x0+t/PER*(x1-x0);};L('Valve output',x0-8,300,11,'#5b6576','right',1);L('In control',x0-8,322,11,'#5b6576','right',1);
ln(x0,300,x1,300,'#1e63b8',2.5);rc(X(TF),294,X(TF+tv())-X(TF),12,'rgba(245,158,11,0.35)');
rc(x0,316,X(TF)-x0,12,'#16a34a');L('A',(x0+X(TF))/2,322,11,'#fff','center',1);rc(X(TF),316,X(TF+tv())-X(TF),12,'#f59e0b');rc(X(TF+tv()),316,x1-X(TF+tv()),12,'#0e7490');L('B',(X(TF+tv())+x1)/2,322,11,'#fff','center',1);
L('hold',X(TF+tv()/2),340,11,'#a8620a','center',1);ln(X(cy),290,X(cy),332,'#1a2333',2);
mk(1,110,70);mk(2,530,70);mk(3,320,152);mk(4,88,50);mk(5,572,184);mk(6,320,256);mk(7,40,311);}
"""
