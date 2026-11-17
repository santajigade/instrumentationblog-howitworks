PAGE = dict(
    slug="plc-timer", grp="PLC", name="PLC On Delay Timer (TON)", kw="How a PLC On Delay Timer Works",
    title="How a PLC On Delay Timer Works: Animated TON Diagram",
    desc="How a PLC on delay timer works, animated: the TON block, elapsed time counting up to the preset and the output Q, with a live timing diagram of IN, ET and Q.",
    h1="How a PLC On Delay Timer Works",
    hero="Set the preset time PT and how long the input stays on. Watch the elapsed time count up in the TON block and see when the output turns on, or why it never does when the input drops too early.",
    quick="An on delay timer (TON) starts timing when its input turns on and turns its output on only after the input has stayed on for the preset time. If the input turns off before that, the elapsed time resets to zero and the output never comes on.",
    intro=["The on delay timer is the most used timer in PLC programs. It is defined in the IEC 61131 standard as the TON function block, and almost every PLC offers the same behaviour under a similar name.",
           "A TON has an input IN, a preset time PT, an output Q and an elapsed time ET. ET counts up while IN is on, and Q turns on when ET reaches PT.",
           "Typical uses are delays before a motor starts, filters that ignore short sensor flickers and alarms that must persist for some seconds before they are raised. Understanding the reset behaviour avoids most timer bugs in the field."],
    sliders=[("pt", "Preset time PT", 1, 10, 3, 0.5, 1, "s"), ("pw", "Input on time", 1, 12, 5, 0.5, 1, "s")],
    outs=[("q", "Output Q turns on"), ("on", "Q stays on for"), ("et", "Elapsed time ET now"), ("acc", "Preset in counts (10 ms time base)")],
    legend=["Input contact I0.0 from a switch or sensor", "TON instruction block", "Preset time PT", "Elapsed time ET counting up", "Timer output Q driving coil Q0.0", "Timing diagram of IN, ET and Q"],
    steps=["While the input IN is off, the elapsed time ET is held at zero and the output Q is off.",
           "When IN turns on, the timer starts and ET counts up in real time on every scan.",
           "When ET reaches the preset PT, ET stops at PT and Q turns on.",
           "Q stays on as long as IN stays on; when IN turns off, Q turns off at once and ET resets to zero.",
           "If IN turns off before ET reaches PT, ET resets and Q never turns on, so short pulses are ignored."],
    formula=["Q = IN AND (ET ≥ PT)",
             "ET counts up while IN is on, stops at PT and resets to 0 when IN turns off",
             "Q on time = input on time − PT (zero if the input is shorter than PT)",
             "Preset in counts = PT ÷ time base; the timing error is up to about one scan time",
             "Example: PT 3 s, input on for 5 s: Q turns on 3 s after the input and stays on for 2 s; with a 10 ms time base the preset is 300 counts"],
    parts=[("IN input", "Rung condition that starts the timer; usually a contact from a sensor or switch"),
           ("PT preset", "The delay to wait, entered as a time value or as counts of the time base"),
           ("ET elapsed time", "Current timed value; it can be shown on an HMI or used in compare instructions"),
           ("Q output", "Timer done bit that turns on when ET reaches PT"),
           ("Time base", "Resolution of the timer, such as 1 ms, 10 ms or 100 ms, on PLCs that count in units")],
    uses=[("Start delay", "Waits a few seconds after a start command, for example to sound a warning horn before a conveyor moves."),
          ("Signal debounce", "Ignores short flickers from level switches or proximity sensors before acting."),
          ("Alarm delay", "Raises an alarm only if a low pressure or high temperature condition lasts longer than the preset."),
          ("Sequence steps", "Holds each step of a batch or machine sequence for a fixed time before moving on.")],
    pros=["Simple and the same behaviour on almost every PLC", "Filters out short unwanted pulses", "ET can be shown on an HMI so operators see the countdown"],
    cons=["Resets fully if the input drops for even one scan", "Accuracy is limited to about one scan time", "Many timers with long presets make logic harder to follow"],
    tips=["If a timer never finishes, watch IN online; a contact that flickers for one scan resets the TON every time.",
          "Use a retentive timer (RTO or TONR) when the time must add up across interruptions, not a TON.",
          "Check the time base and units of the preset; entering 30 in a 100 ms timer gives 3 s, not 30 s.",
          "Avoid using the same timer address twice in a program; the last call in the scan decides its state."],
    faq=[("What is the difference between TON and TOF?", "TON delays turning the output on after the input turns on. TOF turns the output on at once and delays turning it off after the input turns off."),
         ("What happens if the input turns off before the preset time?", "The elapsed time resets to zero and the output never turns on. The next time the input turns on, timing starts again from zero."),
         ("What is the difference between TON and RTO?", "An RTO, or retentive timer, keeps its elapsed time when the input turns off and continues from there. It needs a separate reset instruction."),
         ("How accurate is a PLC timer?", "The timer is updated in the scan, so the output can turn on up to about one scan time late. For short presets the scan time and input filter matter.")],
    cal=[("plc-signal/plc-timer-preset-calculator", "PLC Timer Preset Calculator"), ("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("plc-timer-instructions-ton-tof-rto", "PLC timer instructions TON, TOF and RTO"))

SCENE = r"""
var cy=0,PER=14,T0=1;
function inOn(t){return t>=T0&&t<T0+P.pw;}
function etAt(t){return inOn(t)?Math.min(P.pt,t-T0):0;}
function qAt(t){return inOn(t)&&t-T0>=P.pt;}
function upd(){var ok=P.pw>P.pt;o('q',ok?m(P.pt,1)+' s after the input turns on':'Never: input drops before PT');o('on',ok?m(P.pw-P.pt,1)+' s':'0 s');
o('et',m(etAt(cy),1)+' s of '+m(P.pt,1)+' s');o('acc',m(P.pt*100,0)+' counts');}
function step(dt){cy+=dt;if(cy>=PER)cy-=PER;upd();}
function pw(x1,y1,x2,y2,on){if(on){C.setLineDash([6,5]);C.lineDashOffset=-T*30;ln(x1,y1,x2,y2,'#16a34a',3.5,[6,5]);C.setLineDash([]);C.lineDashOffset=0;}else ln(x1,y1,x2,y2,'#475569',2);}
function draw(){var I=inOn(cy),E=etAt(cy),Q=qAt(cy);
L('Real time; the demo repeats every 14 s',20,22,11,'#5b6576','left');
var R0=40,R1=600,y=80;ln(R0,40,R0,150,'#1a2333',3);ln(R1,40,R1,150,'#1a2333',3);
pw(R0,y,94,y,true);var c=I?'#16a34a':'#475569';ln(94,y-12,94,y+12,c,2.5);ln(106,y-12,106,y+12,c,2.5);L('I0.0',100,y-22,11,'#1a2333','center',1);L('Start',100,y+24,11,'#5b6576','center');
pw(106,y,220,y,I);
rc(220,48,160,96,'#ffffff','#c2410c',8);C.lineWidth=2.5;C.strokeStyle='#c2410c';C.stroke();L('TON   T1',300,60,12,'#1a2333','center',1);
L('IN',228,y,11,'#1a2333','left',1);L('Q',372,y,11,'#1a2333','right',1);L('PT',228,112,11,'#1a2333','left',1);L('ET',372,112,11,'#1a2333','right',1);
ln(200,112,220,112,'#475569',2);rc(130,103,70,18,'#fff7ed','#c2410c',3);L(m(P.pt,1)+' s',165,112,11,'#c2410c','center',1);
ln(380,112,400,112,'#475569',2);rc(400,103,70,18,'#eff6ff','#1e63b8',3);L(m(E,1)+' s',435,112,11,'#1e63b8','center',1);
rc(236,126,128,10,'#e2e8f0');rc(236,126,128*E/P.pt,10,Q?'#16a34a':'#1e63b8');
pw(380,y,520,y,Q);C.strokeStyle=Q?'#16a34a':'#475569';C.lineWidth=2.5;C.beginPath();C.arc(536,y,12,Math.PI*0.65,Math.PI*1.35);C.stroke();C.beginPath();C.arc(536,y,12,-Math.PI*0.35,Math.PI*0.35);C.stroke();
L('Q0.0',536,y-22,11,'#1a2333','center',1);pw(552,y,R1,y,Q);
ci(536,y+40,9,Q?'#fde047':'#e2e8f0','#475569',1.5);if(Q){for(var k=0;k<6;k++){var a=k*Math.PI/3+T*2;ln(536+12*Math.cos(a),y+40+12*Math.sin(a),536+17*Math.cos(a),y+40+17*Math.sin(a),'#f59e0b',2);}}L('Lamp',566,y+40,11,'#5b6576','left');
var x0=110,x1=620,X=function(t){return x0+t/PER*(x1-x0);};
var rows=[['IN',190],['ET',250],['Q',300]];rows.forEach(function(r){L(r[0],x0-12,r[1],12,'#1a2333','right',1);});
C.lineWidth=2.5;C.strokeStyle='#16a34a';C.beginPath();C.moveTo(X(0),200);C.lineTo(X(T0),200);C.lineTo(X(T0),180);C.lineTo(X(T0+P.pw),180);C.lineTo(X(T0+P.pw),200);C.lineTo(X(PER),200);C.stroke();
ln(x0,222,x1,222,'#c2410c',1,[4,3]);L('PT',x1,214,11,'#c2410c','right',1);ln(x0,272,x1,272,'#cbd5e1',1);
C.strokeStyle='#1e63b8';C.beginPath();C.moveTo(X(0),272);C.lineTo(X(T0),272);var te=Math.min(P.pt,P.pw);C.lineTo(X(T0+te),272-te/P.pt*50);C.lineTo(X(T0+P.pw),272-te/P.pt*50);C.lineTo(X(T0+P.pw),272);C.lineTo(X(PER),272);C.stroke();
C.strokeStyle='#c2410c';C.beginPath();C.moveTo(X(0),310);if(P.pw>P.pt){C.lineTo(X(T0+P.pt),310);C.lineTo(X(T0+P.pt),290);C.lineTo(X(T0+P.pw),290);C.lineTo(X(T0+P.pw),310);}C.lineTo(X(PER),310);C.stroke();
if(P.pw>P.pt){ln(X(T0),283,X(T0+P.pt),283,'#5b6576',1);ln(X(T0),279,X(T0),287,'#5b6576',1);ln(X(T0+P.pt),279,X(T0+P.pt),287,'#5b6576',1);L('delay PT',X(T0+P.pt/2),297,11,'#5b6576','center',1);}
for(var s=0;s<=PER;s+=2){ln(X(s),318,X(s),323,'#475569',1);L(s+' s',X(s),333,11,'#5b6576','center');}
ln(X(cy),172,X(cy),316,'#1a2333',2);ci(X(cy),272-E/P.pt*50,4,'#1e63b8');
mk(1,74,y-26);mk(2,206,58);mk(3,148,136);mk(4,480,112);mk(5,510,y+40);mk(6,x0-40,250);}
"""
