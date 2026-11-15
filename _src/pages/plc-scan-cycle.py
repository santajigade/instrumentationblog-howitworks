PAGE = dict(
    slug="plc-scan-cycle", grp="PLC", name="PLC Scan Cycle", kw="How a PLC Scan Cycle Works",
    title="How a PLC Scan Cycle Works: Animated Diagram and Timing",
    desc="How a PLC scan cycle works, animated: read inputs, run the program, update outputs. See why a pulse shorter than the scan time can be missed.",
    h1="How a PLC Scan Cycle Works",
    hero="Change the scan time and the length of the sensor pulse. Watch the PLC read its inputs once per scan and see when a short pulse slips through unseen.",
    quick="A PLC works in a repeating loop called the scan cycle. It copies all inputs into memory, runs the program from top to bottom using that copy, then writes the results to the outputs, and starts again.",
    intro=["Every PLC, from a small brick to a large rack system, runs its program in a continuous loop. One pass of that loop is called a scan, and the time it takes is the scan time, usually a few milliseconds to a few tens of milliseconds.",
           "Inside a scan the PLC does not look at the real input terminals while the program runs. It works from an input image taken at the start of the scan, and the outputs only change when the output image is written at the end.",
           "This simple idea explains many field problems: slow response, missed short pulses from sensors and outputs that seem to flicker. Understanding the scan cycle is the first step in troubleshooting PLC logic."],
    sliders=[("scan", "PLC scan time", 5, 100, 20, 1, 0, "ms"), ("pw", "Sensor pulse length", 2, 200, 12, 1, 0, "ms")],
    outs=[("sps", "Scans per second"), ("resp", "Worst case response (about 2 × scan)"), ("pw", "Will the pulse be seen?"), ("cnt", "Pulses seen and missed in the demo")],
    legend=["Field input: sensor wired to I0.1", "Input image table", "Program (ladder rung)", "Output image table", "Output Q0.0 driving a lamp", "Scan phases: read, execute, write, housekeeping"],
    steps=["Input scan: the PLC reads every input terminal and stores the states in the input image table.",
           "Program scan: it executes the program rung by rung, using only the input image, and writes results to the output image.",
           "Output scan: the output image is copied to the physical output terminals.",
           "Housekeeping: communication, diagnostics and the watchdog timer are serviced.",
           "The cycle repeats immediately, so a typical PLC completes hundreds of scans every second."],
    formula=["Scan time = input read + program execution + output write + housekeeping", "Scans per second = 1000 ÷ scan time (ms)",
             "Worst case response ≈ 2 × scan time + input filter + output delay", "A pulse is only guaranteed to be seen if it lasts longer than one scan",
             "Example: 20 ms scan gives 50 scans per second and up to about 40 ms response"],
    parts=[("Input module", "Converts field signals (24 V DC, 230 V AC) to logic levels, often with a filter delay"), ("Input image table", "Memory copy of all inputs taken at the start of each scan"),
           ("CPU and program", "Executes the user program using the image tables"), ("Output image table", "Memory where the program writes output results"),
           ("Watchdog timer", "Stops the PLC if one scan takes longer than the set limit")],
    uses=[("Troubleshooting slow response", "Explains delays between a sensor change and an output action."), ("Fast pulses", "Shows when to use high speed counters or interrupt inputs instead of normal inputs."),
          ("Program design", "Helps place logic in the right order so a result is used in the same scan."), ("System sizing", "Guides the choice of CPU when the program grows or loops get faster.")],
    pros=["Predictable, repeatable execution of logic", "Inputs stay stable during one scan, so logic is consistent", "Easy to measure and monitor scan time in the CPU diagnostics"],
    cons=["Short pulses can be missed if they fall between input reads", "Response time grows as the program grows", "Very long programs can trip the watchdog timer"],
    tips=["Check the scan time in the CPU diagnostics before blaming a sensor for slow response.", "Use a high speed counter or interrupt input for pulses shorter than the scan time.",
          "Do not use loops that wait for an input inside the program; the input image will not change during the scan.", "Remember the input filter time adds to the response; reduce it only if noise allows."],
    faq=[("What is a typical PLC scan time?", "Small programs often run in 1 to 10 ms and large programs in 20 to 100 ms. The CPU shows the actual, minimum and maximum scan time in its diagnostics."),
         ("Why can a PLC miss a short pulse?", "Inputs are read only once per scan. If a pulse starts and ends between two reads, the program never sees it."),
         ("What is the watchdog timer?", "It is a timer that stops the PLC and sets outputs to a safe state if a scan takes too long, for example because of an endless loop."),
         ("Does the order of rungs matter?", "Yes. A result calculated in a later rung is only used by earlier rungs in the next scan, which can add one scan of delay.")],
    cal=[("plc-signal/plc-response-time-calculator", "PLC Response Time Calculator"), ("plc-signal/plc-digital-filter-calculator", "PLC Digital Filter Calculator")],
    glo=[("plc-scan-time", "PLC Scan Time")],
    cmp=[],
    tool=[("tools/practice-tests/plc-and-signals-quiz", "PLC and Signals Quiz")],
    blog=("how-plc-scan-cycle-works", "How the PLC scan cycle works"))

SCENE = r"""
var ph=0,vt=1.6,sens=false,inB=false,outB=false,qPhys=false,caught=false,seen=0,miss=0,pt=0.9,pon=-1,hist=[],reads=[];
function pulseVis(){return P.pw/P.scan*vt;}
function upd(){o('sps',m(1000/P.scan,1));o('resp','about '+m(2*P.scan,0)+' ms');o('pw',P.pw>P.scan?'Always seen':'Can be missed');o('cnt',seen+' seen, '+miss+' missed');}
function step(dt){var p0=ph;ph+=dt/vt;if(ph>=1){ph-=1;inB=sens;if(sens)caught=true;reads.push(T);}
if(p0<0.8&&ph>=0.8)outB=inB;if(p0<0.95&&ph>=0.95)qPhys=outB;
pt-=dt;if(pt<=0&&pon<0){pon=0;sens=true;caught=false;}if(pon>=0){pon+=dt;if(pon>=pulseVis()){sens=false;pon=-1;pt=3.1+Math.random()*1.4;if(caught)seen++;else miss++;upd();}}
hist.push([T,sens]);while(hist.length&&T-hist[0][0]>4.2)hist.shift();while(reads.length&&T-reads[0]>4.2)reads.shift();}
function blk(x,y,w,h,t,on){rc(x,y,w,h,on?'#fff1e9':'#f8fafc',on?'#d9622b':'#cbd5e1',8);if(on){C.lineWidth=2.5;C.strokeStyle='#d9622b';C.stroke();}L(t,x+w/2,y+14,12,'#1a2333','center',1);}
function draw(){var rp=ph<0.15,ex=ph>=0.15&&ph<0.8,wr=ph>=0.8&&ph<0.95,hk=ph>=0.95;
L('Field input',75,56,12,'#5b6576','center',1);rc(30,70,90,60,'#1a2333',null,8);L('Sensor',75,88,11,'#fff','center',1);ci(75,112,9,sens?'#22c55e':'#334155','#94a3b8');L('I0.1',75,145,12,'#1a2333','center',1);ln(120,100,190,100,sens?'#22c55e':'#94a3b8',3);
rc(180,40,300,230,'#ffffff','#475569',12);L('PLC CPU',330,56,12,'#5b6576','center',1);
blk(192,72,80,90,'Input image',rp);rc(212,100,40,26,inB?'#bbf7d0':'#e2e8f0','#94a3b8',4);L('I0.1 = '+(inB?1:0),232,113,11,'#1a2333','center',1);
blk(284,72,112,90,'Program',ex);ln(292,128,312,128,'#334155',2);rc(312,116,20,24,null,'#334155');L('I0.1',322,108,10,'#334155','center',1);ln(332,128,352,128,'#334155',2);ci(366,128,11,null,'#334155',2);L('Q0.0',366,108,10,'#334155','center',1);ln(377,128,390,128,'#334155',2);if(ex&&inB){ln(292,128,390,128,'#22c55e',3);}
blk(408,72,64,90,'Output',wr);rc(418,100,44,26,outB?'#bbf7d0':'#e2e8f0','#94a3b8',4);L('Q0.0 = '+(outB?1:0),440,113,10,'#1a2333','center',1);
var bx=192,bw=280,by=190;var seg=[[0,0.15,'Read','#1e63b8'],[0.15,0.8,'Execute','#6b3fb0'],[0.8,0.95,'Write','#1d7a46'],[0.95,1,'','#a8620a']];seg.forEach(function(s){rc(bx+bw*s[0],by,bw*(s[1]-s[0]),26,s[3]);if(s[2])L(s[2],bx+bw*(s[0]+s[1])/2,by+13,11,'#fff','center',1);});
ar(bx+bw*ph,by+46,bx+bw*ph,by+30,'#1a2333',2);L('one scan',bx+bw/2,by+58,11,'#5b6576','center');
ln(472,128,520,128,qPhys?'#f59e0b':'#94a3b8',3);ci(560,128,26,qPhys?'#fde047':'#e2e8f0','#475569',2);if(qPhys){for(var k=0;k<8;k++){var a=k*Math.PI/4+T;ln(560+32*Math.cos(a),128+32*Math.sin(a),560+40*Math.cos(a),128+40*Math.sin(a),'#f59e0b',2);}}L('Lamp',560,170,12,'#1a2333','center',1);
var x0=30,x1=620,y0=300;L('Sensor signal and PLC input reads (last 4 s)',x0,y0-12,11,'#5b6576','left');C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();hist.forEach(function(h,i){var x=x1-(T-h[0])/4.2*(x1-x0),y=h[1]?y0+8:y0+40;if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();
reads.forEach(function(t){var x=x1-(T-t)/4.2*(x1-x0);ln(x,y0+2,x,y0+46,'#1e63b8',1.2,[3,3]);});
L('Scan time and pulse shown slowed down',30,22,11,'#5b6576','left');
mk(1,135,86);mk(2,262,150);mk(3,384,150);mk(4,462,150);mk(5,600,104);mk(6,bx-14,by+13);}
"""
