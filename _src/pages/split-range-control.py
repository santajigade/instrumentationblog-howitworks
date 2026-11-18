PAGE = dict(
    slug="split-range-control", grp="DCS", name="Split Range Control", kw="How Split Range Control Works",
    title="How Split Range Control Works: Animated Diagram and Formula",
    desc="How split range control works, animated: one controller output drives a cooling valve below the split point and a steam valve above it, with the mA ranges.",
    h1="How Split Range Control Works",
    hero="Move the controller output, the split point and the gap between the two ranges. Watch which valve opens on the jacketed vessel and read the valve positions and the 4 to 20 mA ranges each positioner must be calibrated for.",
    quick="In split range control one controller output is shared by two or more final control elements, each working over its own part of the 0 to 100 % range. A temperature controller can open a cooling valve over the lower half of its output and a steam valve over the upper half, so one loop handles both heating and cooling.",
    intro=["Some processes need two actuators to cover the whole operating range, such as heating and cooling on a reactor jacket, or a small and a large valve in parallel for wide flow turndown. Split range control lets one PID controller drive both, without two loops fighting each other.",
           "The controller output is divided at a split point, often 50 %. Each valve positioner is calibrated to stroke fully over its own part of the signal, for example 4 to 12 mA for the first valve and 12 to 20 mA for the second.",
           "The split can be done in the positioners, in the DCS with two output blocks, or with a splitter function block. Doing it in the DCS makes the ranges easy to see, adjust and document."],
    sliders=[("op", "Controller output OP", 0, 100, 70, 1, 0, "%"), ("s", "Split point S", 30, 70, 50, 1, 0, "%"),
             ("g", "Gap between the ranges", 0, 10, 0, 1, 0, "%")],
    outs=[("sv", "Steam valve opening"), ("cv", "Cooling water valve opening"), ("ma", "Loop signal = 4 + 0.16 × OP"), ("rg", "Positioner calibration ranges")],
    legend=["Temperature controller TIC with output OP", "One 4 to 20 mA signal to both positioners", "Cooling water valve, works below the split point", "Steam valve, works above the split point", "Jacketed vessel with temperature transmitter", "Split range graph of valve opening against OP"],
    steps=["The temperature transmitter sends the vessel temperature to the controller, which compares it with the setpoint and calculates its output OP.",
           "The same OP, as a 4 to 20 mA signal, goes to both valve positioners or to two output blocks in the DCS.",
           "Below the split point the cooling valve works: it is fully open at 0 % OP and closes as OP rises to the split point.",
           "Above the split point the steam valve works: it starts to open at the split point and is fully open at 100 % OP.",
           "Near the split point both valves are almost closed; a small gap there avoids heating and cooling at the same time, while an overlap avoids a dead zone."],
    formula=["Steam valve % = (OP − S2) ÷ (100 − S2) × 100 for OP above S2, where S2 = S + gap ÷ 2",
             "Cooling valve % = (S1 − OP) ÷ S1 × 100 for OP below S1, where S1 = S − gap ÷ 2",
             "Signal in mA = 4 + 0.16 × OP; each positioner is calibrated over its own mA band",
             "Example: OP 70 %, split 50 %, no gap: steam = (70 − 50) ÷ 50 × 100 = 40 %, cooling 0 %, signal 4 + 0.16 × 70 = 15.2 mA, steam positioner range 12 to 20 mA",
             "Process gain changes when the loop crosses from one valve to the other, so tuning must suit both halves"],
    parts=[("Temperature controller", "PID block in the DCS that calculates one output from the temperature error"),
           ("Splitter or two output blocks", "Divides the output into two ranges and scales each to 0 to 100 % for its valve"),
           ("Cooling water valve", "Opens on falling OP; usually chosen to fail open so cooling stays available on air or signal loss"),
           ("Steam valve", "Opens on rising OP; usually chosen to fail closed so heating stops on air or signal loss"),
           ("Valve positioners", "Calibrated to the mA band of their own range, or fed a rescaled signal from the DCS")],
    uses=[("Reactor heating and cooling", "One temperature loop moves smoothly from cooling water to steam on a jacketed reactor."),
          ("Tank pressure blanketing", "Below the split the vent valve opens, above it the nitrogen inlet valve opens to hold tank pressure."),
          ("Wide flow turndown", "A small valve handles low flows and a large valve in parallel takes over at high flows."),
          ("pH control", "Acid and alkali dosing valves are split around the neutral point of the controller output.")],
    pros=["One controller handles two actuators without loops fighting each other", "Extends the usable range beyond what one valve can give", "Simple to set up in the DCS and easy for operators to follow"],
    cons=["Process gain often differs on each side of the split, which makes tuning a compromise", "A gap gives a dead zone and an overlap wastes energy; both need care", "Valve stiction near the split point can cause a limit cycle"],
    tips=["Do the split in the DCS where possible, so each valve gets a full 4 to 20 mA signal and the positioners stay at standard calibration.",
          "Stroke test both valves at the split point and check that one is really closed before the other starts to open, or as designed.",
          "Check the fail positions of both valves against the process hazard, usually cooling fail open and steam fail closed.",
          "If the loop oscillates around the split point, look for valve stiction and different gains on the two sides before retuning."],
    faq=[("What is split range control?", "It is a control scheme where one controller output drives two or more valves, each over its own part of the output range. A common example is cooling below 50 % and heating above 50 %."),
         ("What is the difference between split range and sequence control?", "The terms are often used for the same idea. Some engineers say sequence when valves act in the same direction one after the other, and split range when they act in opposite directions such as heating and cooling."),
         ("Why use a gap at the split point?", "A small gap makes sure the heating and cooling valves are never open together, which saves energy. The cost is a small dead zone where neither valve acts."),
         ("How are the valve positioners calibrated in split range?", "Each positioner is set to give full stroke over its own mA band, for example 4 to 12 mA and 12 to 20 mA. Many plants now send each valve a full 4 to 20 mA signal from the DCS instead.")],
    cal=[("control-valve/split-range-calculator", "Split Range Calculator")],
    glo=[("split-range-control", "Split Range Control"), ("valve-positioner", "Valve Positioner"), ("fail-safe-position", "Fail Safe Position")],
    cmp=[("linear-vs-equal-percentage-valve", "Linear vs Equal Percentage Valve")],
    tool=[("tools/practice-tests/control-valve-and-pid-quiz", "Control Valve and PID Quiz")],
    blog=("split-range-control-working-principle", "Split range control working principle"))

SCENE = r"""
var st=[],cw=[],ag=0;for(var i=0;i<26;i++){st.push(Math.random());cw.push(Math.random());}
function s1(){return P.s-P.g/2;}function s2(){return P.s+P.g/2;}
function sv(op){return op>s2()?(op-s2())/(100-s2())*100:0;}
function cvo(op){return op<s1()?(s1()-op)/s1()*100:0;}
function ma(x){return 4+0.16*x;}
function upd(){o('sv',m(sv(P.op),1)+' %');o('cv',m(cvo(P.op),1)+' %');o('ma',m(ma(P.op),1)+' mA');o('rg','Cooling 4 to '+m(ma(s1()),1)+' mA reverse, steam '+m(ma(s2()),1)+' to 20 mA');}
function step(dt){var a=sv(P.op)/100,b=cvo(P.op)/100;for(var i=0;i<st.length;i++){st[i]+=dt*(0.05+0.9*a)*0.8;if(st[i]>1)st[i]-=1;cw[i]+=dt*(0.05+0.9*b)*0.8;if(cw[i]>1)cw[i]-=1;}ag+=dt*3;}
function valve(x,y,op,c,lab){C.fillStyle=op>0?c:'#94a3b8';C.beginPath();C.moveTo(x-14,y-10);C.lineTo(x+14,y+10);C.lineTo(x+14,y-10);C.lineTo(x-14,y+10);C.closePath();C.fill();
ln(x,y,x,y-20,'#475569',2);C.fillStyle='#e2e8f0';C.beginPath();C.arc(x,y-20,13,Math.PI,0);C.fill();C.strokeStyle='#475569';C.lineWidth=1.5;C.stroke();ln(x-13,y-20,x+13,y-20,'#475569',1.5);
L(lab+' '+m(op,0)+' %',x,y+22,11,'#1a2333','center',1);}
function flow(path,arr,col,on){if(!on)return;for(var i=0;i<arr.length;i++){var u=arr[i],L2=0,seg=[];for(var k=1;k<path.length;k++){var d=Math.hypot(path[k][0]-path[k-1][0],path[k][1]-path[k-1][1]);seg.push(d);L2+=d;}
var t=u*L2;for(var k=1;k<path.length;k++){if(t<=seg[k-1]){var f=t/seg[k-1];ci(path[k-1][0]+(path[k][0]-path[k-1][0])*f,path[k-1][1]+(path[k][1]-path[k-1][1])*f,2.6,col);break;}t-=seg[k-1];}}}
function draw(){var a=sv(P.op),b=cvo(P.op);
L('Flow dots drawn in proportion to valve opening',20,22,11,'#5b6576','left');
rc(20,40,120,70,'#1a2333',null,8);L('TIC 101',80,54,12,'#fff','center',1);rc(32,66,96,14,'#334155');rc(32,66,96*P.op/100,14,'#0e7490');L('OP '+m(P.op,0)+' %',80,94,12,'#fff','center',1);
C.setLineDash([5,5]);C.lineDashOffset=-T*25;C.strokeStyle='#16a34a';C.lineWidth=2.2;C.beginPath();C.moveTo(140,75);C.lineTo(170,75);C.lineTo(170,145);C.moveTo(170,145);C.lineTo(170,225);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
ln(140,75,170,75,'rgba(22,163,74,0.25)',6);L(m(ma(P.op),1)+' mA',176,90,11,'#16a34a','left',1);
rc(20,150,200,10,'#cbd5e1');rc(20,250,200,10,'#cbd5e1');L('Steam in',24,138,11,'#b91c1c','left',1);L('Water in',24,238,11,'#1e63b8','left',1);
valve(120,155,a,'#ef4444','Steam');valve(120,255,b,'#3b82f6','Cooling');ln(170,135,134,135,'#16a34a',1.5,[3,3]);ln(170,235,134,235,'#16a34a',1.5,[3,3]);
rc(220,110,130,190,'#e2e8f0','#64748b',14);rc(234,122,102,166,'#f1f5f9','#64748b',10);wave(236,334,170,286,'#bfdbfe');
ln(285,96,285,250,'#334155',3);var w=Math.cos(ag)*26;ln(285-w,250,285+w,250,'#334155',5);rc(275,86,20,12,'#475569');
ci(330,100,13,'#e0f2fe','#0e7490',2);L('TT',330,100,11,'#0e7490','center',1);ln(325,112,322,150,'#0e7490',2);
rc(350,146,26,8,'#cbd5e1');rc(350,266,26,8,'#cbd5e1');
flow([[20,155],[220,155],[228,155],[228,290]],st,'#ef4444',a>0);flow([[20,255],[220,255],[228,255],[228,120]],cw,'#3b82f6',b>0);
var gx=420,gy=56,gw=196,gh=180,X=function(p){return gx+gw*p/100;},Y=function(p){return gy+gh-gh*p/100;};
rc(gx,gy,gw,gh,'#f8fafc','#dde3ee');for(var p=0;p<=100;p+=50){ln(gx,Y(p),gx-5,Y(p),'#475569',1);L(p,gx-8,Y(p),11,'#5b6576','right');L(p,X(p),gy+gh+12,11,'#5b6576','center');}
L('Valve %',gx-8,gy-14,11,'#5b6576','left',1);L('Controller output OP %',gx+gw/2,gy+gh+28,11,'#5b6576','center',1);
ln(X(0),Y(100),X(s1()),Y(0),'#3b82f6',3);ln(X(s1()),Y(0),X(s2()),Y(0),'#94a3b8',3);ln(X(s2()),Y(0),X(100),Y(100),'#ef4444',3);
L('Cooling',X(4),Y(30),11,'#1e63b8','left',1);L('Steam',X(98),Y(30),11,'#b91c1c','right',1);
ln(X(P.s),gy,X(P.s),gy+gh,'#0e7490',1,[3,3]);
var px=X(P.op);ln(px,gy,px,gy+gh,'#1a2333',2);var pul=4+1.5*Math.sin(T*6);ci(px,Y(a>0?a:b),pul,'#1a2333');
L('Split '+m(P.s,0)+' %',gx+gw,gy-14,11,'#0e7490','right',1);
rc(380,300,240,46,'#ecfeff','#a5f3fc',6);L('Cooling band 4 to '+m(ma(s1()),1)+' mA',392,314,11,'#1e63b8','left',1);L('Steam band '+m(ma(s2()),1)+' to 20 mA',392,332,11,'#b91c1c','left',1);
mk(1,20,40);mk(2,196,60);mk(3,88,226);mk(4,88,128);mk(5,350,190);mk(6,gx+gw,gy);}
"""
