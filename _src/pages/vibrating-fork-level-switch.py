PAGE = dict(
    slug="vibrating-fork-level-switch", grp="Switches", name="Vibrating Fork Level Switch", kw="How a Vibrating Fork Level Switch Works",
    title="How a Vibrating Fork Level Switch Works: Animated Diagram",
    desc="How a vibrating fork level switch works, animated: liquid covers the tines, the resonant frequency drops and the electronics switch the output.",
    h1="How a Vibrating Fork Level Switch Works",
    hero="Change the liquid specific gravity and the switching threshold of the electronics. Watch the fork frequency fall as the liquid covers the tines and see when a light liquid no longer gives enough shift to switch.",
    quick="A vibrating fork level switch keeps a tuning fork vibrating at its resonant frequency with a piezo drive. When liquid covers the tines, the liquid moves with them and adds mass, so the frequency drops and the electronics change over the output.",
    intro=["A vibrating fork level switch is a point level device for liquids. It is used for high and low level alarms, overfill protection, pump dry run protection and pump start and stop in tanks and pipes.",
           "The fork has two tines that a piezo element drives at their natural frequency in air. A second piezo element or the same one picks up the vibration, and the electronics keep measuring the frequency.",
           "When the liquid covers the tines, it moves with them and the vibrating mass rises. The frequency falls by a few percent or more, and once the shift passes the threshold the output changes after a short delay."],
    sliders=[("sg", "Liquid specific gravity", 0.3, 1.6, 1.0, 0.05, 2, ""), ("th", "Switching threshold (frequency shift)", 2, 12, 5, 0.5, 1, "%")],
    outs=[("fc", "Frequency when covered, f = f air ÷ √(1 + β × SG)"), ("sh", "Frequency shift when covered"), ("mn", "Lowest SG that still switches"), ("st", "Output now (MAX fail safe mode)")],
    legend=["Fork tines vibrating at resonance", "Piezo drive and pickup in the housing", "Electronics measuring the frequency", "Liquid level", "Switch output to PLC or alarm", "Trend: fork frequency and threshold"],
    steps=["The piezo drive keeps the two tines vibrating at their resonant frequency while the fork is in air.",
           "The pickup feeds the vibration back to the electronics, which measure the frequency continuously.",
           "As the liquid rises over the tines, the liquid moves with them, the effective mass increases and the frequency falls.",
           "When the frequency shift passes the threshold for longer than the switching delay, the electronics change over the output.",
           "When the liquid drains, the frequency returns to the air value and the output changes back."],
    formula=["Frequency when covered: f = f air ÷ √(1 + β × SG), from f = (1 ÷ 2π) × √(k ÷ m)",
             "β is the ratio of the liquid mass that moves with the tines to the fork mass, per unit SG",
             "Frequency shift in percent = (1 − f ÷ f air) × 100",
             "Lowest SG that switches = (1 ÷ (1 − threshold)² − 1) ÷ β",
             "Example: f air 1200 Hz, β 0.25 (demo fork), SG 1.0: f = 1200 ÷ √1.25 = 1073.3 Hz, shift = 10.6 %, threshold 5 %: lowest SG = (1 ÷ 0.95² − 1) ÷ 0.25 = 0.43"],
    parts=[("Fork tines", "Two paddles shaped so the liquid drains off them and they vibrate in opposite directions"),
           ("Piezo drive", "Converts the drive voltage into mechanical vibration of the fork"),
           ("Piezo pickup", "Converts the vibration back into a signal for the frequency measurement"),
           ("Electronics", "Holds the fork at resonance, compares the frequency with the threshold and applies the delay"),
           ("Output stage", "Relay, transistor, NAMUR or two wire output to the PLC, pump starter or alarm")],
    uses=[("Overfill protection", "High level alarm or trip on storage and day tanks."),
          ("Pump dry run protection", "Detects a low level or an empty pipe and stops the pump."),
          ("Pump control", "Starts and stops a pump at two fixed levels with two switches."),
          ("Leak detection", "Senses liquid in a drip tray or bund.")],
    pros=["No moving float, so turbulence, flow and bubbles have little effect", "Not affected much by conductivity, dielectric constant or colour of the liquid", "Easy to test in place; many units have a test function"],
    cons=["Light liquids give a small frequency shift, so there is a minimum density", "Very viscous or crusting liquids can bridge the tines and hold the switch in the covered state", "Detects only one point; it gives no continuous level"],
    tips=["Check the minimum density on the datasheet against the lightest liquid the tank will hold, including at high temperature.",
          "Mount the fork so the tines are vertical when it enters through a side wall; liquid then drains between them.",
          "Use MAX fail safe mode for high level alarms so a broken wire or power loss gives an alarm, and MIN mode for dry run protection.",
          "Keep the fork away from the fill stream; a jet of liquid hitting dry tines can make the output chatter."],
    faq=[("Why does the frequency drop in liquid?", "The liquid around the tines moves with them, so the vibrating mass increases. A larger mass with the same stiffness gives a lower resonant frequency."),
         ("Does foam switch a vibrating fork?", "Light foam usually does not, because its density is too low to give enough shift. Dense foam can, so check the application with the supplier data."),
         ("What do MAX and MIN mode mean?", "In MAX mode the output is energised while the fork is uncovered and drops out when it is covered. In MIN mode it is energised while covered, so a low level or a failure drops it out."),
         ("Can a vibrating fork detect solids?", "Yes, there are fork designs for powders and granules, but they work on damping of the vibration and need a different fork and setting.")],
    cal=[("level/density-from-dp-calculator", "Density from DP Calculator")],
    glo=[("vibrating-fork-level-switch", "Vibrating Fork Level Switch"), ("point-level-measurement", "Point Level Measurement")],
    cmp=[("float-switch-vs-vibrating-fork", "Float Switch vs Vibrating Fork")],
    tool=[("tools/practice-tests/level-measurement-quiz", "Level Measurement Quiz")],
    blog=("vibrating-fork-level-switch-working", "Vibrating fork level switch working"))

SCENE = r"""
var F0=1200,B=0.25,lvl=52,f=1200,wet=false,tmr=0,hist=[],pre=0;
function Y(l){return 330-l*2.8;}
function fcov(){return F0/Math.sqrt(1+B*P.sg);}
function sh(){return (1-fcov()/F0)*100;}
function upd(){if(!pre){pre=1;for(var q=0;q<500;q++){T+=0.04;step(0.04);}}var fc=fcov(),s=sh(),t=P.th/100;o('fc',m(fc,1)+' Hz');o('sh',m(s,1)+' %'+(s<P.th?' (below threshold, no switching)':''));o('mn','SG '+m((1/((1-t)*(1-t))-1)/B,2));o('st',wet?'Covered: relay off, alarm':'Free: relay on, normal');}
function cover(){var s=Y(lvl);return clamp((196-s)/22,0,1);}
function step(dt){lvl=52+30*Math.sin(2*Math.PI*T/18);var ft=F0-(F0-fcov())*cover();f+=(ft-f)*Math.min(1,dt/0.3);
var w=(1-f/F0)*100>=P.th;if(w!==wet){tmr+=dt;if(tmr>1){wet=w;tmr=0;upd();}}else tmr=0;
hist.push([T,f]);while(hist.length&&T-hist[0][0]>20)hist.shift();}
function draw(){var s=Y(lvl),c=cover(),vb=Math.sin(T*40);
L('Level cycle sped up; tine movement exaggerated',20,22,11,'#5b6576','left');
rc(24,40,206,296,'#e2e8f0','#64748b',6);rc(30,46,194,284,'#f8fafc');
wave(30,224,s,330,'rgba(147,197,253,0.85)');
if(Math.cos(2*Math.PI*T/18)>0){stream(60,46,s);L('Filling',60,58,11,'#1e63b8','left',1);}else L('Draining',60,58,11,'#1e63b8','left',1);
rc(224,170,8,30,'#475569');rc(232,166,60,38,'#cbd5e1','#334155',6);L('Fork',262,185,11,'#1a2333','center',1);
rc(198,181,26,8,'#94a3b8','#334155',2);var a=1.6*vb*(1-0.4*c);rc(160,173+a,40,6,'#64748b','#1e293b',2);rc(160,191-a,40,6,'#64748b','#1e293b',2);
ln(292,185,312,185,'#475569',2);ln(312,185,312,110,'#475569',2);ln(312,110,330,110,'#475569',2);
rc(330,42,150,136,'#f8fafc','#cbd5e1',8);L('Tines close up',405,54,11,'#5b6576','center',1);if(c>0.5)rc(332,66,146,110,'rgba(147,197,253,0.55)');
var A=10*(1-0.35*c),ph=Math.sin(2*Math.PI*(f/400)*T);rc(420,84,52,74,'#cbd5e1','#334155',4);L('Piezo',446,121,11,'#1a2333','center',1);
rc(350,96+A*ph,70,12,'#64748b','#1e293b',3);rc(350,134-A*ph,70,12,'#64748b','#1e293b',3);
ar(344,102,344,92+A,'#d9622b',1.5);ar(344,140,344,150-A,'#d9622b',1.5);L(c>0.5?'In liquid':'In air',385,170,11,c>0.5?'#1e63b8':'#5b6576','center',1);
rc(492,42,130,136,'#1a2333',null,8);L('Electronics',557,56,11,'#cbd5e1','center',1);L(m(f,0)+' Hz',557,82,16,'#fbbf24','center',1);
L('shift '+m((1-f/F0)*100,1)+' %',557,104,11,'#cbd5e1','center');var on=!wet;ci(516,140,12,on?'#22c55e':'#334155','#94a3b8',2);if(wet){var g=0.5+0.5*Math.sin(T*8);ci(516,140,17+3*g,null,'rgba(251,113,133,0.7)',2);}
L(on?'Relay on':'Relay off',536,134,11,'#fff','left',1);L(wet?'HIGH ALARM':'Normal',536,150,11,wet?'#fda4af':'#cbd5e1','left',1);
var gx0=330,gx1=620,gy0=212,gy1=322,lo=980,hi=1230,TY=function(v){return gy1-(v-lo)/(hi-lo)*(gy1-gy0);},TX=function(t){return gx1-(T-t)/20*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');var thf=F0*(1-P.th/100);ln(gx0,TY(thf),gx1,TY(thf),'#d9622b',1,[4,4]);L('threshold '+m(thf,0)+' Hz',gx0+6,TY(thf)-9,11,'#d9622b','left');
L(m(hi,0),gx0-4,gy0,11,'#5b6576','right');L(m(lo,0),gx0-4,gy1,11,'#5b6576','right');
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();hist.forEach(function(p,i){var x=TX(p[0]),y=TY(clamp(p[1],lo,hi));if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
L('Fork frequency, Hz',gx0,gy0-10,11,'#1e63b8','left',1);L('last 20 s',gx1,gy0-10,11,'#5b6576','right');L('Fork at '+m(51.8,0)+' % of tank height',127,346,11,'#5b6576','center');
mk(1,150,166);mk(2,262,150);mk(3,610,52);mk(4,206,s-16);mk(5,604,174);mk(6,gx0+12,gy1-14);}
"""
