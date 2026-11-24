PAGE = dict(
    slug="rs485-network", grp="Signals", name="RS485 Network and Termination", kw="How RS485 Network Termination Works",
    title="How RS485 Network Termination Works: Animated Diagram",
    desc="How RS485 network termination works, animated: a data edge runs down the twisted pair, reflects from a wrong end resistor and bias sets the idle line.",
    h1="How RS485 Network Termination Works",
    hero="Change the end termination resistor, the bias resistors and the cable length. Watch the data edge travel along the trunk, see how big the reflection is and check whether the idle line stays above the 200 mV receiver threshold.",
    quick="An RS485 trunk is a twisted pair with a characteristic impedance of about 120 Ω, and a resistor equal to that impedance at each end absorbs the signal so nothing reflects. Bias resistors pull the two lines apart when no device is driving, so receivers see a defined idle state instead of noise.",
    intro=["RS485 is the physical layer under Modbus RTU and many other serial field protocols. It sends each bit as a voltage difference between two wires, which rejects common mode noise picked up along long cable runs.",
           "At higher baud rates or on long cables the line behaves as a transmission line. Any change in impedance, such as an open end or a wrong resistor, reflects part of every edge back along the cable and distorts the bits.",
           "When every driver is switched off between frames, the line floats. Fail safe bias resistors hold the difference above the receiver threshold so the idle line reads as a steady logic 1."],
    sliders=[("rt", "End termination resistor Rt (both ends)", 30, 480, 120, 10, 0, "Ω"), ("rb", "Bias resistors Rb (pull up and pull down)", 220, 2200, 560, 20, 0, "Ω"), ("len", "Trunk cable length", 100, 1200, 600, 50, 0, "m")],
    outs=[("g", "Reflection coefficient at the far end"), ("vb", "Idle bias voltage across the lines (needs 200 mV or more)"), ("dl", "One way cable delay at velocity factor 0.66"), ("ld", "Load of both terminators on the driver")],
    legend=["Master with RS485 driver", "Bias resistors: pull up and pull down", "Twisted pair trunk", "Termination resistor at each end", "Slave on a short stub", "Data edge and its reflection", "Received signal at the far slave", "Idle bias voltage against the 200 mV threshold"],
    steps=["The driver puts a voltage difference of a few volts on the two lines for every bit, positive for one logic state and negative for the other.",
           "Each edge travels along the twisted pair at about two thirds of the speed of light.",
           "At the far end the edge meets the termination resistor; if it equals the cable impedance all the energy is absorbed.",
           "If the resistor is missing or wrong, part of the edge reflects back and adds ringing to the bits seen by every receiver.",
           "Between frames no driver is active, and the bias resistors pull the lines apart so the receivers read a clean idle state."],
    formula=["Reflection coefficient Γ = (Rt − Z₀) ÷ (Rt + Z₀), with Z₀ ≈ 120 Ω for RS485 twisted pair",
             "Idle bias voltage Vb = Vs × (Rt ÷ 2) ÷ (Rt ÷ 2 + 2 × Rb), with both ends terminated and Vs = 5 V",
             "Receivers must see at least 200 mV, so Vb should stay above that with margin",
             "One way delay = length ÷ (0.66 × 299 792 458 m/s), about 5 ns per metre",
             "Example: Rt 120 Ω, Rb 560 Ω, 600 m: Γ = 0 ÷ 240 = 0.00, Vb = 5 × 60 ÷ (60 + 1120) = 254 mV, delay 3.03 µs one way and 6.06 µs round trip, driver load 60 Ω"],
    parts=[("RS485 transceiver", "Driver and receiver in each device, switched by the direction control"),
           ("Twisted pair cable", "Shielded pair with about 120 Ω impedance, run as one daisy chain trunk"),
           ("Termination resistors", "One at each physical end of the trunk, matched to the cable impedance"),
           ("Bias resistors", "One pull up and one pull down, fitted at one point only, usually the master"),
           ("Common or reference wire", "Keeps all transceivers within the allowed common mode voltage range")],
    uses=[("Modbus RTU networks", "Energy meters, drives and analysers on one serial trunk to a PLC or SCADA."),
          ("Building automation", "Controllers and sensors linked over long runs between floors."),
          ("Weighing and batching", "Weight indicators and dosing controllers reporting to a central panel."),
          ("Remote I/O and RTUs", "Serial links to outstations where Ethernet is not available.")],
    pros=["Differential signalling rejects noise over long cable runs", "Many devices on one pair, up to 32 unit loads per segment", "Low cost transceivers and simple wiring"],
    cons=["Needs correct termination and biasing or communication becomes unreliable", "Star wiring and long stubs cause reflections", "Half duplex, so only one device can transmit at a time"],
    tips=["Fit termination only at the two physical ends of the trunk; extra terminators in the middle load the driver and shrink the signal.",
          "Fit bias resistors at one point only, and recalculate them if you add or remove terminators.",
          "Wire the trunk as a daisy chain and keep stubs to each device as short as possible.",
          "Measure about 60 Ω across the two lines with power off; it confirms both terminators are in place and no third one is fitted."],
    faq=[("Why is a 120 Ω resistor used at the end of an RS485 line?", "It matches the characteristic impedance of typical RS485 twisted pair. A matched end absorbs each edge, so nothing reflects back to distort the bits."),
         ("Does a short RS485 cable need termination?", "When the round trip delay of the cable is short compared with the rise time of the edges, reflections settle before the bit is sampled. Long cables and high baud rates need termination."),
         ("What do bias resistors do on RS485?", "They pull one line up and the other down so the idle bus has a defined voltage difference. Without them the receivers may see noise between frames and report framing errors."),
         ("Why do I measure about 60 Ω across the bus?", "Two 120 Ω terminators at the two ends appear in parallel, which gives 60 Ω. A reading of 120 Ω means one is missing, and 40 Ω means a third one is fitted.")],
    cal=[("electrical/resistor-series-parallel-calculator", "Resistor Series Parallel Calculator")],
    glo=[("rs-485", "RS 485"), ("modbus-rtu", "Modbus RTU")],
    cmp=[],
    tool=[("tools/communication-protocols/rs485-cable-length-calculator", "RS485 Cable Length Calculator"), ("tools/troubleshooting/modbus-communication-fault-finder", "Modbus Communication Fault Finder")],
    blog=("rs485-termination-biasing-resistors", "RS485 termination and biasing resistors"))

SCENE = r"""
var tc=0,XL=132,XR=600,YA=120,YB=136,bits=[1,0,0,1,0,1,1,0,1,0,9,9],SX=[250,380,510];
function gm(){return (P.rt-120)/(P.rt+120);}
function vb(){var h=P.rt/2;return 5*h/(h+2*P.rb);}
function upd(){var g=gm();o('g',m(g,2)+(Math.abs(g)<0.005?', no reflection':(g>0?', reflection in phase':', reflection inverted')));var v=vb()*1000;o('vb',m(v,0)+' mV, '+(v>=200?'idle state defined':'too low, idle may read noise'));
var d=P.len/(0.66*299792458)*1e6;o('dl',m(d,2)+' µs, round trip '+m(2*d,2)+' µs');o('ld',m(P.rt/2,0)+' Ω (driver test load 54 Ω)');}
function step(dt){tc=(tc+dt)%(1.4+(Math.abs(gm())>0.01?1.4:0.4));}
function res(x,y1,y2,lab){ln(x,y1,x,y1+4,'#475569',2);rc(x-5,y1+4,10,y2-y1-8,'#fef3c7','#92400e',2);ln(x,y2-4,x,y2,'#475569',2);}
function edge(x,col,a){C.globalAlpha=a;rc(x-10,YA-6,20,YB-YA+12,col,null,4);C.globalAlpha=1;}
function draw(){var g=gm();
L('Edge travel slowed down; ringing on the trace drawn to show the size of the reflection',20,22,11,'#5b6576','left');
rc(20,88,94,80,'#1a2333',null,8);L('Master',67,104,12,'#fff','center',1);L('driver',67,120,11,'#cbd5e1','center');
L('+5 V',42,52,11,'#b91c1c','center',1);ln(42,58,42,64,'#b91c1c',2);rc(37,64,10,18,'#fde68a','#92400e',2);ln(42,82,42,88,'#475569',1);
ln(42,86,118,86,'#475569',1);ln(118,86,118,YA,'#475569',1);
ln(98,168,98,186,'#475569',1);rc(93,186,10,18,'#fde68a','#92400e',2);ln(98,204,98,212,'#1a2333',2);L('0 V',112,210,11,'#1a2333','left',1);ln(98,168,122,168,'#475569',1);ln(122,168,122,YB,'#475569',1);
L('Rb '+m(P.rb,0)+' Ω',56,74,11,'#92400e','left',1);
ln(114,YA,XR+6,YA,'#1e63b8',3);ln(114,YB,XR+6,YB,'#c2410c',3);
res(XL,YA,YB);res(XR,YA,YB);L('Rt '+m(P.rt,0)+' Ω',XL+10,YA-14,11,'#92400e','left',1);L('Rt '+m(P.rt,0)+' Ω',XR-4,YA-14,11,'#92400e','right',1);
for(var i=0;i<3;i++){var x=SX[i];ln(x-4,YA,x-4,170,'#1e63b8',1.5);ln(x+4,YB,x+4,170,'#c2410c',1.5);rc(x-30,170,60,30,'#f8fafc','#94a3b8',6);L('Slave '+(i+1),x,185,11,'#1a2333','center',1);}
var tf=1.4,tr=1.4,t=tc;if(t<tf){edge(XL+(XR-XL)*t/tf,'rgba(124,58,237,0.75)',1);}else if(t<tf+tr&&Math.abs(g)>0.01){var a=Math.min(1,0.2+Math.abs(g));edge(XR-(XR-XL)*(t-tf)/tr,g>0?'rgba(217,98,43,0.8)':'rgba(14,116,144,0.8)',a);L(g>0?'reflection':'inverted reflection',XR-(XR-XL)*(t-tf)/tr,YA-24,11,g>0?'#c2410c':'#0e7490','center',1);}
else if(t>=tf&&t<tf+0.6&&Math.abs(g)<=0.01)L('absorbed',XR-36,YB+18,11,'#16a34a','right',1);
var bx0=470,bx1=620,by=56,vmax=0.5,v=vb(),Xb=function(q){return bx0+q/vmax*(bx1-bx0);};rc(bx0,by,bx1-bx0,14,'#e2e8f0',null,3);rc(bx0,by,Xb(Math.min(v,vmax))-bx0,14,v>=0.2?'#16a34a':'#dc2626',null,3);ln(Xb(0.2),by-6,Xb(0.2),by+20,'#1a2333',1.5,[3,2]);
L('Idle bias '+m(v*1000,0)+' mV',bx0,by-10,11,'#1a2333','left',1);L('200 mV',Xb(0.2),by+28,11,'#1a2333','center');
var x0=40,x1=620,ym=284,AMP=34,Y=function(q){return ym-q/2.5*AMP*1.2;},bw=48,n=bits.length,off=(T*40)%(n*bw);
rc(x0,226,x1-x0,116,'#f6f8fc','#dde3ee',6);L('Received signal at slave 3, A minus B (illustrative)',x0+6,238,11,'#5b6576','left',1);
ln(x0,Y(0.2),x1,Y(0.2),'#94a3b8',1,[3,3]);ln(x0,Y(-0.2),x1,Y(-0.2),'#94a3b8',1,[3,3]);
C.save();C.beginPath();C.rect(x0+1,227,x1-x0-2,114);C.clip();C.strokeStyle='#7c3aed';C.lineWidth=2;C.beginPath();
for(var x=x0;x<=x1;x+=1){var q=(x-x0+off)%(n*bw),k=Math.floor(q/bw),u=q-k*bw,b=bits[k],pb=bits[(k+n-1)%n];var lv=function(z){return z==9?v:(z?2:-2);};
var cur=lv(b),pre=lv(pb),s=cur+(cur-pre)*g*Math.exp(-u/9)*Math.cos(u*0.9);var y=Y(s);if(x==x0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();C.restore();
rc(x1-64,Y(0.2)-17,60,14,'rgba(246,248,252,0.9)');L('±200 mV',x1-6,Y(0.2)-10,11,'#5b6576','right');
mk(1,20,88);mk(2,26,66);mk(3,320,YB+14);mk(4,XR+20,YA+8);mk(5,SX[0]-44,185);mk(6,XL+24,YB+18);mk(7,330,238);mk(8,bx0-16,by+7);}
"""
