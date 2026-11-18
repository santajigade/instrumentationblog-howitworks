PAGE = dict(
    slug="scada-report-by-exception", grp="SCADA", name="SCADA Report by Exception", kw="How SCADA Report by Exception Works",
    title="How SCADA Report by Exception Works: Animated DNP3 Diagram",
    desc="How SCADA report by exception works, animated: an RTU checks each change against a deadband and sends unsolicited event messages only when the value moves.",
    h1="How SCADA Report by Exception Works",
    hero="Set the analog deadband, the size of the process swing and the poll interval you would otherwise use. Watch the RTU send a message only when the value moves past the deadband and compare the traffic with plain polling.",
    quick="In report by exception the outstation or RTU sends a value to the SCADA master only when it has changed by more than a set deadband, or when a digital point changes state. Quiet points send nothing, so the link carries far fewer messages than when the master polls every point on a fixed cycle.",
    intro=["Classic SCADA polling asks every outstation for every point on a fixed cycle, even when nothing has changed. On slow radio, satellite or leased line links that wastes most of the bandwidth and delays the messages that matter.",
           "Report by exception turns this around: the outstation watches its own points and creates an event only when a digital input changes or an analog value moves by more than its deadband. Protocols such as DNP3 and IEC 60870 5 101 and 104 support this, with events stored in a buffer and sent with a time stamp.",
           "The events reach the master either as unsolicited responses or when the master polls for event data. A slower integrity poll of all static values still runs in the background so the master database cannot drift out of step."],
    sliders=[("db", "Analog deadband", 0.5, 10, 2, 0.5, 1, "% of span"), ("amp", "Process swing, peak", 1, 20, 10, 1, 0, "% of span"),
             ("ps", "Poll interval for comparison", 1, 10, 2, 1, 0, "s")],
    outs=[("rpm", "Exception reports per minute ≈ 4 × A ÷ deadband"), ("poll", "Polled responses per minute = 60 ÷ poll interval"), ("save", "Messages saved against polling"), ("err", "Largest error at the master")],
    legend=["Field transmitter giving the process value", "RTU outstation comparing the change with the deadband", "Event buffer holding time stamped events", "Unsolicited event message on the link", "SCADA master database value", "Trend of the real value and the value at the master"],
    steps=["The RTU scans its inputs and keeps, for each analog point, the last value it reported to the master.",
           "On every scan it compares the new value with that last reported value.",
           "When the difference reaches the deadband, or a digital input changes state, the RTU creates an event with the value and a time stamp and puts it in the event buffer.",
           "The RTU sends the buffered events to the master as an unsolicited response, or the master collects them in its next event poll, and the master confirms receipt.",
           "The master updates its database and trends; a periodic integrity poll of all static values keeps the database aligned if any event was lost."],
    formula=["Report when |PV − last reported value| ≥ deadband",
             "The value at the master is never more than one deadband away from the real value",
             "For a sine swing of peak A: total travel per cycle = 4 × A, so reports per cycle ≈ 4 × A ÷ deadband",
             "Polling sends one response per point every poll interval, changed or not",
             "Example: A 10 %, deadband 2 %, one cycle per minute: 4 × 10 ÷ 2 = 20 reports per minute, against 60 ÷ 2 s = 30 polled responses, so about 33 % fewer messages"],
    parts=[("Field transmitter", "Measures the process and sends a 4 to 20 mA or digital value to the RTU"),
           ("RTU or outstation", "Scans the inputs, applies the deadband and creates time stamped events"),
           ("Event buffer", "Stores events in order until the master confirms them, so nothing is lost while the link is down"),
           ("Communication link", "Radio, cellular, fibre or leased line carrying unsolicited responses, polls and confirmations"),
           ("SCADA master", "Holds the real time database, confirms events and runs the integrity poll")],
    uses=[("Pipelines", "Pressure and flow stations along a pipeline report changes over narrow radio or satellite links."),
          ("Water networks", "Reservoir levels and pump status from many remote sites reach the control room without constant polling."),
          ("Electrical substations", "Breaker trips and alarms are sent at once with time stamps for the sequence of events record."),
          ("Oil and gas wellheads", "Solar powered RTUs save energy and airtime by staying quiet when nothing changes.")],
    pros=["Much less traffic when values are steady", "Changes and alarms arrive quickly instead of waiting for the next poll", "Events carry time stamps, which keeps the true order of fast changes"],
    cons=["A deadband set too wide hides real changes from operators", "A deadband set too narrow on a noisy signal floods the link", "Needs an integrity poll and event buffering to recover from lost messages"],
    tips=["Set analog deadbands per point from the process need, often around 1 to 2 % of span, and widen them on noisy signals.",
          "Keep an integrity poll running, for example every few minutes to an hour, so a lost event cannot leave a stale value on the screen.",
          "Check that the RTU clock is synchronised, otherwise event time stamps from different sites cannot be compared.",
          "Watch the event buffer size; if it overflows during a long link outage the oldest events are lost."],
    faq=[("What is the difference between polling and report by exception?", "With polling the master asks for every point on a fixed cycle. With report by exception the outstation sends a value only when it changes by more than the deadband."),
         ("What is an unsolicited response in DNP3?", "It is a message the outstation sends without being asked, carrying new event data. The master answers with a confirmation so the outstation can clear those events from its buffer."),
         ("Why is an integrity poll still needed?", "Events can be lost through a buffer overflow, a restart or a link fault. The integrity poll reads all current values so the master database is correct again."),
         ("How do I choose the analog deadband?", "Pick the smallest change the operator or historian really needs to see, then check the traffic. A noisy signal needs a wider deadband or some filtering in the RTU.")],
    cal=[("plc-signal/analog-scaling-calculator", "Analog Scaling Calculator")],
    glo=[],
    cmp=[],
    tool=[("tools/communication-protocols/modbus-rtu-timing-calculator", "Modbus RTU Timing Calculator")],
    blog=("report-by-exception-scada-dnp3", "Report by exception in SCADA and DNP3"))

SCENE = r"""
var ts=0,SP=6,lv=50,cnt=0,pk=[],hist=[],buf=0;
function pv(t){return 50+P.amp*Math.sin(2*Math.PI*t/60);}
function rpm(){return Math.floor(4*P.amp/P.db+1e-9);}
var pre=0;function upd(){if(!pre){pre=1;for(var k=0;k<520;k++){T+=0.02;step(0.02);}}var r=rpm(),p=60/P.ps;o('rpm',r+' reports');o('poll',m(p,0)+' responses');o('save',r<p?'About '+m((1-r/p)*100,0)+' % fewer messages':'None: more traffic than polling');o('err','Less than '+m(P.db,1)+' % of span');}
function step(dt){ts+=dt*SP;var v=pv(ts);if(Math.abs(v-lv)>=P.db-1e-9){lv=v;cnt++;buf++;pk.push({p:0,v:v,a:0});}
for(var i=pk.length-1;i>=0;i--){var q=pk[i];q.p+=dt*1.2;if(q.p>=1&&!q.a){q.a=1;buf=Math.max(0,buf-1);q.db=q.v;}if(q.p>=2)pk.splice(i,1);}
hist.push([ts,v,lv]);while(hist.length&&ts-hist[0][0]>60)hist.shift();}
var mval=50;
function draw(){var v=pv(ts);for(var j=0;j<pk.length;j++)if(pk[j].a)mval=pk[j].db;
L('Time sped up 6 times; one process cycle lasts 60 s',20,22,11,'#5b6576','left');
ci(52,82,20,'#e0f2fe','#0369a1',2);L('PT',52,82,12,'#0369a1','center',1);ln(52,102,52,128,'#475569',3);rc(36,128,32,10,'#94a3b8');
C.setLineDash([5,5]);C.lineDashOffset=-T*25;ln(72,82,120,82,'#16a34a',2.5,[5,5]);C.setLineDash([]);C.lineDashOffset=0;
rc(120,40,170,120,'#1a2333',null,8);L('RTU outstation',205,54,12,'#fff','center',1);
L('PV now',132,76,11,'#cbd5e1','left');L(m(v,1)+' %',278,76,12,'#fff','right',1);L('Last sent',132,94,11,'#cbd5e1','left');L(m(lv,1)+' %',278,94,12,'#fbbf24','right',1);
var df=Math.abs(v-lv);L('Change',132,112,11,'#cbd5e1','left');rc(184,106,94,12,'#334155');rc(184,106,94*clamp(df/P.db,0,1),12,df/P.db>0.85?'#f59e0b':'#38bdf8');L('of deadband',278,124,11,'#94a3b8','right');
L('Events',132,146,11,'#cbd5e1','left');for(var k=0;k<Math.min(buf,8);k++)rc(176+k*11,140,8,12,'#fbbf24');
var x0=290,x1=430,ly=100;ln(x0,ly,x1,ly,'#94a3b8',3);L('Link',360,ly-16,11,'#5b6576','center',1);
for(var i=0;i<pk.length;i++){var q=pk[i];if(q.p<1){var x=x0+16+(x1-x0-32)*q.p;rc(x-14,ly-9,28,18,'#f59e0b',null,3);L('EV',x,ly,11,'#1a2333','center',1);}else{var x=x1-17-(x1-x0-34)*(q.p-1);rc(x-15,ly+12,30,16,'#a7f3d0',null,3);L('CON',x,ly+20,11,'#065f46','center',1);}}
rc(430,40,190,120,'#f5f3ff','#7c3aed',8);L('SCADA master',525,54,12,'#2e1065','center',1);L('Database value',444,80,11,'#5b6576','left');L(m(mval,1)+' %',606,80,13,'#7c3aed','right',1);
L('Events received',444,104,11,'#5b6576','left');L(String(cnt),606,104,12,'#1a2333','right',1);L('Error now',444,128,11,'#5b6576','left');L(m(Math.abs(v-mval),1)+' %',606,128,12,'#1a2333','right',1);
var gx0=70,gx1=620,gy0=190,gy1=320,Y=function(p){return gy1-(p-25)/50*(gy1-gy0);},X=function(t){return gx1-(ts-t)/60*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');[30,50,70].forEach(function(p){ln(gx0,Y(p),gx1,Y(p),'#e2e8f0',1);L(p+' %',gx0-6,Y(p),11,'#5b6576','right');});
C.fillStyle='rgba(245,158,11,0.15)';C.fillRect(gx0,Y(lv+P.db),gx1-gx0,Y(lv-P.db)-Y(lv+P.db));
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(h,i){var x=X(h[0]),y=Y(h[1]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();hist.forEach(function(h,i){var x=X(h[0]),y=Y(h[2]);if(i){C.lineTo(x,Y(hist[i-1][2]));C.lineTo(x,y);}else C.moveTo(x,y);});C.stroke();
L('Real value',gx0+8,gy0+12,11,'#1e63b8','left',1);L('Reported value',gx0+90,gy0+12,11,'#d9622b','left',1);L('Deadband band',gx0+200,gy0+12,11,'#b45309','left',1);
L('last 60 s',gx1,gy1+14,11,'#5b6576','right');L('now',gx1,gy0-8,11,'#5b6576','right');
mk(1,52,46);mk(2,120,40);mk(3,284,146);var pq=null;for(var i=0;i<pk.length;i++)if(pk[i].p<1){pq=pk[i];break;}mk(4,pq?clamp(x0+16+(x1-x0-32)*pq.p,312,408):330,ly+44);mk(5,430,40);mk(6,34,230);}
"""
