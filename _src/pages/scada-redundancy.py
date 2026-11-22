PAGE = dict(
    slug="scada-redundancy", grp="SCADA", name="SCADA Server Redundancy", kw="How SCADA Server Redundancy Works",
    title="How SCADA Server Redundancy Works: Animated Diagram",
    desc="How SCADA server redundancy works, animated: hot standby replication, missed heartbeats, failover to the standby and the data gap seen by operators.",
    h1="How SCADA Server Redundancy Works",
    hero="Set the heartbeat interval, the number of missed heartbeats before failover and the RTU poll cycle. Watch the primary server fail, the standby count the missed heartbeats, take over polling and the operator clients reconnect.",
    quick="A redundant SCADA system runs two servers: the primary polls the RTUs and serves the operator clients, while a hot standby receives a live copy of its database. When the standby stops seeing the heartbeat for the set number of intervals, it becomes primary and starts polling.",
    intro=["A SCADA server collects data from RTUs and PLCs across a pipeline, a water network or a substation and serves it to every operator screen. If that single server stops, operators lose their view of the whole system, so critical systems run a redundant pair.",
           "The primary server does all the polling and writes to the real time database, alarm list and event log. It replicates every change to the standby over a dedicated link and both servers exchange a heartbeat at a fixed interval.",
           "If the standby misses a set number of heartbeats in a row, it decides that the primary has failed and takes over. The settings for heartbeat interval and missed count are a balance between a fast failover and avoiding a false one on a busy network."],
    sliders=[("hb", "Heartbeat interval", 0.5, 5, 1, 0.5, 1, "s"), ("n", "Missed heartbeats before failover", 2, 10, 3, 1, 0, ""), ("pc", "RTU poll cycle", 1, 10, 2, 1, 0, "s")],
    outs=[("td", "Failure detection time, t d = N × t hb"), ("gp", "Worst case data gap, t d + t poll"), ("pm", "Poll cycles affected"), ("st", "Demo state")],
    legend=["Server A (primary at start)", "Server B (hot standby)", "Redundancy link: replication and heartbeat", "Operator clients", "Communication network to the field", "RTUs and PLCs at the remote sites", "Failover timeline"],
    steps=["Server A is primary: it polls every RTU in turn, updates the real time database and serves the operator clients.",
           "Every change in the database, alarm list and event log is replicated to Server B, and both servers send a heartbeat every interval.",
           "Server A fails; Server B stops receiving the heartbeat and counts the missed intervals.",
           "When the missed count reaches the set value, Server B becomes primary, starts polling the RTUs and the clients reconnect to it.",
           "After repair, Server A copies the database from Server B and returns as the hot standby; the roles are not switched back unless an engineer does it."],
    formula=["Failure detection time: t d = N × t hb, where N is the number of missed heartbeats and t hb the heartbeat interval",
             "Worst case data gap ≈ t d + t poll, because the new primary needs up to one poll cycle to refresh every RTU",
             "Poll cycles affected = gap ÷ t poll, rounded up",
             "The takeover time of the server software adds to this; take it from the supplier data or measure it in a failover test",
             "Example: t hb 1 s, N 3, t poll 2 s: t d = 3 × 1 = 3 s, gap ≈ 3 + 2 = 5 s, 5 ÷ 2 = 2.5, so up to 3 poll cycles are affected"],
    parts=[("Primary server", "Polls the field, owns the real time database and serves the clients"),
           ("Hot standby server", "Runs the same software and receives every database change, ready to take over"),
           ("Redundancy link", "Dedicated network path for replication and heartbeat, ideally doubled"),
           ("Operator clients", "Screens that connect to whichever server is primary and reconnect after a failover"),
           ("RTUs with event buffers", "Hold time stamped events during the gap so they can be collected by the new primary")],
    uses=[("Oil and gas pipelines", "Keeps the control room view of compressor and valve stations during a server fault."),
          ("Water and wastewater networks", "Monitors reservoirs, pumping stations and treatment plants without a blind period."),
          ("Electrical substations", "Keeps breaker status, alarms and sequence of events data flowing to the control centre."),
          ("Server maintenance", "Allows patching or replacing one server while the other keeps the system running.")],
    pros=["Operators keep their view of the field after a server failure", "Servers can be patched and maintained one at a time", "Event and alarm history is kept on both servers"],
    cons=["Doubles server hardware and licences", "Short timeouts can cause false failovers on a loaded network", "A failure of the shared network or the field communication is not covered by server redundancy"],
    tips=["Run the replication and heartbeat on their own link, not on the busy field or client network, so a traffic peak does not look like a failed server.",
          "Do a planned failover test after every software upgrade and record the real time from failure to the first fresh value on the screens.",
          "Enable time stamped event buffering in the RTUs so changes during the gap are collected and not lost.",
          "Place the two servers in different rooms or buildings with separate power so one local event does not stop both."],
    faq=[("What is the difference between hot and cold standby?", "A hot standby runs and receives live data all the time, so it can take over within seconds. A cold standby must be started and loaded first, so the outage is much longer."),
         ("Why not set the heartbeat timeout very short?", "On a busy or slow network a few heartbeats can be delayed without any failure. A very short timeout would then make the standby take over by mistake and the two servers could both act as primary."),
         ("Is data lost during a SCADA failover?", "Live values are not updated during the gap, but RTUs with event buffering keep time stamped changes and send them when the new primary polls. The historian may show a short gap in trends."),
         ("What is a split brain condition?", "It is when both servers believe they are primary, usually because the redundancy link failed while both servers kept running. Good designs use a second link or an arbiter to avoid it.")],
    cal=[("safety/availability-calculator", "Availability Calculator"), ("safety/mtbf-calculator", "MTBF Calculator")],
    glo=[("mtbf", "MTBF"), ("common-cause-failure", "Common Cause Failure")],
    cmp=[],
    tool=[("tools/communication-protocols/modbus-rtu-timing-calculator", "Modbus RTU Timing Calculator")],
    blog=("scada-redundancy-architecture", "SCADA redundancy architecture"))

SCENE = r"""
var cy=3,TF=6,TR=15,TS=19,PER=24;
function vd(){return 1+0.25*P.n;}
function stA(t){if(t<TF)return'act';if(t<TR)return'fail';if(t<TS)return'sync';return'stby';}
function stB(t){if(t<TF)return'stby';if(t<TF+vd())return'wait';return'act';}
function miss(t){return Math.min(P.n,Math.ceil((t-TF)/vd()*P.n));}
function evt(t){if(t<TF)return'Normal: A primary and polling, B tracking';if(t<TF+vd())return'A failed, B counting missed heartbeats';if(t<TF+vd()+1.2)return'B primary, first poll cycle running';if(t<TR)return'B primary and polling';if(t<TS)return'A repaired, copying database from B';return'B primary, A hot standby';}
var lev='';function upd(){var td=P.n*P.hb,g=td+P.pc;o('td',m(td,1)+' s');o('gp',m(g,1)+' s');o('pm','up to '+m(Math.ceil(g/P.pc-1e-9),0)+' of '+m(P.pc,0)+' s each');o('st',evt(cy));}
function step(dt){cy+=dt;if(cy>=PER)cy-=PER;var e=evt(cy);if(e!==lev){lev=e;upd();}}
function pk(x1,y1,x2,y2,c,sp){C.setLineDash([5,9]);C.lineDashOffset=-T*sp;ln(x1,y1,x2,y2,c,3,[5,9]);C.setLineDash([]);C.lineDashOffset=0;}
function srv(x,y,name,s,extra){var col=s=='act'?'#16a34a':s=='fail'?'#b91c1c':s=='wait'?'#a8620a':s=='sync'?'#6b3fb0':'#1e63b8';
rc(x,y,160,96,s=='fail'?'#f1f5f9':'#ffffff',col,8);C.lineWidth=2.5;C.strokeStyle=col;C.stroke();L(name,x+80,y+16,13,'#1a2333','center',1);
for(var k=0;k<3;k++){rc(x+14,y+28+k*12,44,8,'#e2e8f0','#94a3b8',2);ci(x+52,y+32+k*12,2.5,s=='fail'?'#94a3b8':(Math.sin(T*7+k*2+x)>0?'#22c55e':'#bbf7d0'));}
var t=s=='act'?'PRIMARY':s=='fail'?'FAILED':s=='wait'?'CHECKING':s=='sync'?'SYNCING':'STANDBY';rc(x+66,y+28,86,22,col,null,4);L(t,x+109,y+39,11,'#fff','center',1);
if(extra)L(extra,x+109,y+62,11,col,'center',1);
if(s=='fail'){ln(x+20,y+80,x+140,y+80,'#b91c1c',2);L('Power supply fault',x+80,y+88,11,'#b91c1c','center',1);}else L('Real time database',x+80,y+84,11,'#5b6576','center');}
function draw(){var a=stA(cy),b=stB(cy),aA=a=='act',bA=b=='act',act=aA?170:bA?470:0;
L('Timeout and failover shown at a fixed speed',20,22,11,'#5b6576','left');
rc(250,34,140,28,'#1a2333',null,6);L('Operator clients',320,48,11,'#fff','center',1);
var ex=b=='wait'?'missed '+m(miss(cy),0)+' of '+m(P.n,0):'';
srv(90,92,'Server A',a,'');srv(390,92,'Server B',b,ex);
ln(300,62,170,92,aA?'#16a34a':'#cbd5e1',2);ln(340,62,470,92,bA?'#16a34a':'#cbd5e1',2);
if(aA)pk(300,62,170,92,'#16a34a',30);if(bA&&cy>TF+vd()+0.6)pk(340,62,470,92,'#16a34a',30);
L('Redundancy link',320,108,11,'#5b6576','center',1);ln(250,128,390,128,'#94a3b8',2);ln(250,158,390,158,'#94a3b8',2);
if(aA)pk(252,128,388,128,'#6b3fb0',40);else if(a=='sync')pk(388,128,252,128,'#6b3fb0',-40);L('replication',320,140,11,'#6b3fb0','center');
var ph=(T/P.hb*0.6)%1;if(a!='fail')ci(252+136*ph,158,4,'#d9622b');if(b!='fail')ci(388-136*ph,158,4,'#1e63b8');L('heartbeat',320,170,11,'#d9622b','center');
var ny=226;ln(60,ny,600,ny,'#0e7490',3);L('Communication network',184,ny-10,11,'#0e7490','left',1);
ln(170,188,170,ny,aA?'#16a34a':'#cbd5e1',3);ln(470,188,470,ny,bA?'#16a34a':'#cbd5e1',3);
var polling=aA||(bA&&cy>TF+vd());var rx=[130,320,510],cur=Math.floor(T/0.9)%3;
for(var i=0;i<3;i++){var on=polling&&i==cur;rc(rx[i]-50,262,100,40,'#f6f8fc',on?'#16a34a':'#64748b',6);if(on){C.lineWidth=2.5;C.strokeStyle='#16a34a';C.stroke();}L('RTU '+(i+1),rx[i],276,11,'#1a2333','center',1);L(on?'polled':(polling?'waiting':'buffering events'),rx[i],291,11,on?'#16a34a':(polling?'#5b6576':'#a8620a'),'center');ln(rx[i],ny,rx[i],262,'#475569',2);}
if(polling){var u=(T/0.9)%1,sx=act,tx=rx[cur],px,py;if(u<0.5){var k=u*2;px=sx+(tx-sx)*k;py=ny;}else{var k=(u-0.5)*2;px=tx+(sx-tx)*k;py=ny;}ci(px,py,5,u<0.5?'#16a34a':'#1e63b8','#fff',1.5);}
var tx0=60,tx1=600,ty=326;rc(tx0,ty-8,tx1-tx0,16,'#e2e8f0',null,4);function X(t){return tx0+(tx1-tx0)*t/PER;}
rc(X(0),ty-8,X(TF)-X(0),16,'#bbf7d0',null,4);rc(X(TF),ty-8,X(TF+vd())-X(TF),16,'#fde68a');rc(X(TF+vd()),ty-8,X(TR)-X(TF+vd()),16,'#bbf7d0');rc(X(TR),ty-8,X(TS)-X(TR),16,'#ddd6fe');rc(X(TS),ty-8,X(PER)-X(TS),16,'#bbf7d0',null,4);
L('A primary',(X(0)+X(TF))/2,ty,11,'#14532d','center',1);L('B primary',(X(TF+vd())+X(TR))/2,ty,11,'#14532d','center',1);L('A syncs',(X(TR)+X(TS))/2,ty,11,'#4c1d95','center',1);L('A standby',(X(TS)+X(PER))/2,ty,11,'#14532d','center',1);
L('gap',(X(TF)+X(TF+vd()))/2,ty+18,11,'#a8620a','center',1);
var cx=X(cy);C.fillStyle='#1a2333';C.beginPath();C.moveTo(cx,ty-9);C.lineTo(cx-6,ty-19);C.lineTo(cx+6,ty-19);C.closePath();C.fill();L('now',cx+9,ty-15,11,'#1a2333','left',1);
mk(1,96,98);mk(2,544,98);mk(3,250,112);mk(4,404,48);mk(5,600,212);mk(6,562,262);mk(7,44,326);}
"""
