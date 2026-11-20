PAGE = dict(
    slug="ratio-control", grp="DCS", name="Ratio Control", kw="How Ratio Control Works",
    title="How Ratio Control Works: Animated Diagram, Formula and Example",
    desc="How ratio control works, animated: a wild flow is measured, multiplied by the ratio and sent as setpoint to the flow controller on the second stream.",
    h1="How Ratio Control Works",
    hero="Set the required ratio, the average wild flow and the span of the controlled flow transmitter. Watch the ratio station follow the wild flow and the second flow loop track its moving setpoint.",
    quick="Ratio control keeps one flow in a fixed proportion to another. The uncontrolled or wild flow is measured, multiplied by the ratio R, and the result becomes the remote setpoint of a flow controller on the second stream.",
    intro=["Many processes need two streams in a fixed proportion: fuel and air in a burner, acid and water in dilution, or two reactants in a blend. The main stream is often set by an upstream unit, so the plant can only measure it.",
           "Ratio control measures this wild flow and calculates the setpoint for the controlled flow as R times the wild flow. When the wild flow rises, the controlled flow follows at once, before any quality analyser sees a change.",
           "In a DCS this is built with a ratio station or a multiplier block feeding a flow controller in cascade mode. The operator usually enters the ratio, and an outer quality loop can trim it."],
    sliders=[("r", "Required ratio R (flow B ÷ flow A)", 0.2, 2.0, 0.5, 0.05, 2, ""), ("fa", "Average wild flow A", 20, 100, 60, 1, 0, "m³/h"), ("sb", "Span of flow transmitter B", 50, 250, 50, 10, 0, "m³/h")],
    outs=[("sp", "Setpoint of flow B = R × flow A"), ("tot", "Blend flow and share of B"), ("k", "Ratio in percent of span, K (span A 100 m³/h)"), ("live", "Measured ratio B ÷ A now")],
    legend=["Wild flow transmitter FT A", "Ratio station: multiply by R", "Flow controller FIC B in cascade", "Control valve on stream B", "Flow transmitter FT B", "Blend header", "Trend: flow A, setpoint B and flow B"],
    steps=["The flow transmitter on stream A measures the wild flow, which is set by the upstream process.",
           "The ratio station multiplies this measurement by the ratio R entered by the operator or by an outer loop.",
           "The result is sent as a remote setpoint to the flow controller on stream B, which runs in cascade mode.",
           "The flow controller compares flow B with its setpoint and moves the control valve to remove the error.",
           "When flow A rises or falls, the setpoint for B moves with it, so the blend keeps the same proportion."],
    formula=["Setpoint of flow B = R × flow A",
             "Blend flow = flow A × (1 + R); share of B in the blend = R ÷ (1 + R)",
             "When both signals are in percent of span: K = R × span A ÷ span B",
             "For square root DP meters, linearise both signals before the multiplier",
             "Example: R 0.5, flow A 60 m³/h, span A 100 m³/h, span B 50 m³/h: setpoint B = 0.5 × 60 = 30 m³/h, blend = 90 m³/h, share of B = 0.5 ÷ 1.5 = 33.3 %, K = 0.5 × 100 ÷ 50 = 1.0"],
    parts=[("Wild flow transmitter", "Measures the stream that the loop cannot or should not control"),
           ("Ratio station or multiplier", "Multiplies the wild flow by R, often with a bias, and passes it on as a setpoint"),
           ("Flow controller", "PI controller on the second stream, in cascade mode so it accepts the remote setpoint"),
           ("Flow transmitter on stream B", "Measures the controlled flow for the flow controller"),
           ("Control valve", "Final element on the controlled stream")],
    uses=[("Combustion air and fuel", "Air flow follows fuel flow to keep the right excess air."),
          ("Chemical dosing", "Dosing pump or valve follows the main water flow."),
          ("Blending", "Components of a fuel or product blend stay in fixed proportions."),
          ("Reflux and distillate", "Reflux flow is held in ratio to the distillate or feed flow.")],
    pros=["Corrects for changes in the wild flow before the product quality moves", "Simple to build with standard DCS blocks", "Operator works with a meaningful number, the ratio, instead of a flow setpoint"],
    cons=["Accuracy depends on both flow measurements", "A failed wild flow transmitter drives the controlled flow to a wrong value", "Needs an outer trim loop when the true required ratio changes with the feed"],
    tips=["Check that both flow signals are linear in engineering units before the multiplier; mixing a square root signal with a linear one gives a wrong ratio.",
          "Scale the ratio when the DCS works in percent of span, using K = R × span A ÷ span B.",
          "Tune the flow controller on stream B in auto first, then switch it to cascade.",
          "Add a low and high clamp on the calculated setpoint so a transmitter fault cannot open the valve fully."],
    faq=[("What is a wild flow?", "It is the flow that the ratio loop measures but does not control. It is set by another unit, a level controller or the operator."),
         ("Is ratio control the same as cascade control?", "It uses the same remote setpoint idea, but the setpoint comes from a measured flow times R instead of from a master controller output."),
         ("Why divide the spans when the DCS works in percent?", "A percent of span value from each transmitter has a different meaning. Multiplying R by span A ÷ span B converts the ratio so the percentages give the right flow."),
         ("How is ratio control used in burners?", "Air flow is set in ratio to fuel flow, often with cross limits so air leads on load increase and fuel leads on load decrease.")],
    cal=[("control-valve/control-valve-opening-calculator", "Control Valve Opening Calculator"), ("flow/dp-flow-rerange-calculator", "DP Flow Rerange Calculator")],
    glo=[],
    cmp=[],
    tool=[("tools/pid-tuning/pid-simulator", "PID Simulator"), ("tools/practice-tests/control-valve-and-pid-quiz", "Control Valve and PID Quiz")],
    blog=("what-is-ratio-control-in-process-industries", "What is ratio control in process industries"))

SCENE = r"""
var fa=60,fb=30,sp=30,pa=[],pb=[],pc=[],hist=[];for(var i=0;i<14;i++){pa.push(i/14);pb.push(i/14);pc.push(i/14);}
function wild(){return P.fa*(1+0.15*Math.sin(2*Math.PI*T/12)+0.05*Math.sin(2*Math.PI*T/3.1));}
var pre=0;function upd(){if(!pre){pre=1;for(var q=0;q<420;q++){T+=0.04;step(0.04);}}var s=P.r*P.fa;o('sp',m(s,1)+' m³/h');o('tot',m(P.fa*(1+P.r),1)+' m³/h, B is '+m(P.r/(1+P.r)*100,1)+' %');var k=P.r*100/P.sb;o('k',m(k,2)+(s>P.sb?' (setpoint above FT B span)':''));o('live',m(fb/Math.max(fa,1),3));}
var tk=0;function step(dt){fa=wild();sp=P.r*fa;fb+=(Math.min(sp,P.sb)-fb)*Math.min(1,dt/0.7);
for(var i=0;i<pa.length;i++){pa[i]=(pa[i]+dt*fa/180)%1;pb[i]=(pb[i]+dt*fb/180)%1;pc[i]=(pc[i]+dt*(fa+fb)/300)%1;}
hist.push([T,fa,sp,fb]);while(hist.length&&T-hist[0][0]>16)hist.shift();tk+=dt;if(tk>0.25){tk=0;o('live',m(fb/Math.max(fa,1),3));}}
function inst(x,y,t,c){ci(x,y,15,'#fff',c,2);L(t,x,y,11,c,'center',1);}
function draw(){var vo=clamp(fb/P.sb*100,0,100);
L('Swings exaggerated; dots move with flow',20,22,11,'#5b6576','left');
rc(20,72,470,16,'#dbeafe','#94a3b8');rc(20,192,470,16,'#ffedd5','#94a3b8');
L('Stream A (wild flow)',24,100,11,'#1e63b8','left',1);L('Stream B (controlled)',24,220,11,'#c2410c','left',1);
pa.forEach(function(u){ci(20+470*u,80,3,'#1e63b8');});pb.forEach(function(u){var x=20+470*u;if(x<404||x>436)ci(x,200,3,'#ea580c');});
rc(490,60,56,160,'#f1f5f9','#64748b',8);var ag=T*4;for(var j=0;j<3;j++){var yy=90+j*40;ln(518-12*Math.cos(ag+j),yy,518+12*Math.cos(ag+j),yy,'#475569',3);}ln(518,66,518,214,'#475569',2);
L('Blend',518,52,11,'#5b6576','center',1);rc(546,132,80,16,'#e9d5ff','#94a3b8');pc.forEach(function(u){ci(546+80*u,140,3,'#7c3aed');});L(m(fa+fb,1)+' m³/h',586,160,11,'#6b21a8','center',1);
ln(240,72,240,61,'#475569',2);inst(240,46,'FT A','#1e63b8');L(m(fa,1)+' m³/h',260,46,12,'#1e63b8','left',1);
ln(200,208,200,223,'#475569',2);inst(200,238,'FT B','#c2410c');L(m(fb,1)+' m³/h',220,238,12,'#c2410c','left',1);
rc(180,112,120,50,'#1a2333',null,8);L('Ratio station',240,124,11,'#cbd5e1','center',1);L('× '+m(P.r,2),240,146,14,'#fbbf24','center',1);
rc(340,112,120,50,'#ecfeff','#0e7490',8);L('FIC B  CAS',400,124,11,'#0e7490','center',1);L('SP '+m(sp,1),400,146,12,'#0f172a','center',1);
C.setLineDash([5,5]);C.lineDashOffset=-T*24;C.lineWidth=2;C.strokeStyle='#16a34a';C.beginPath();C.moveTo(240,61);C.lineTo(240,112);C.moveTo(300,137);C.lineTo(340,137);
C.moveTo(200,223);C.lineTo(200,176);C.lineTo(360,176);C.lineTo(360,162);C.moveTo(420,162);C.lineTo(420,171);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
var vx=420,vy=200;C.fillStyle='#c2410c';C.beginPath();C.moveTo(vx-14,vy-10);C.lineTo(vx+14,vy+10);C.lineTo(vx+14,vy-10);C.lineTo(vx-14,vy+10);C.closePath();C.fill();
ln(vx,vy,vx,vy-18,'#475569',2);C.fillStyle='#e2e8f0';C.beginPath();C.arc(vx,vy-18,11,Math.PI,0);C.fill();C.strokeStyle='#475569';C.lineWidth=1.5;C.stroke();
L(m(vo,0)+' % open',vx,vy+22,11,'#1a2333','center',1);
var gx0=60,gx1=620,gy0=262,gy1=340,mx=Math.max(120,P.fa*1.25,P.r*P.fa*1.25),TY=function(v){return gy1-v/mx*(gy1-gy0);},TX=function(t){return gx1-(T-t)/16*(gx1-gx0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');L('0',gx0-6,gy1,11,'#5b6576','right');L(m(mx,0),gx0-6,gy0,11,'#5b6576','right');
function tr(ix,c,d){C.strokeStyle=c;C.lineWidth=2;C.setLineDash(d||[]);C.beginPath();hist.forEach(function(h,i){var x=TX(h[0]),y=TY(h[ix]);if(i)C.lineTo(x,y);else C.moveTo(x,y);});C.stroke();C.setLineDash([]);}
tr(1,'#1e63b8');tr(2,'#d9622b',[6,4]);tr(3,'#16a34a');
L('Flow A',gx0+6,gy0+10,11,'#1e63b8','left',1);L('Setpoint B',gx0+56,gy0+10,11,'#d9622b','left',1);L('Flow B',gx0+130,gy0+10,11,'#16a34a','left',1);L('last 16 s, m³/h',gx1,gy0-8,11,'#5b6576','right');
mk(1,214,46);mk(2,180,112);mk(3,460,112);mk(4,vx+26,vy-22);mk(5,172,238);mk(6,546,72);mk(7,gx0-40,gy0+28);}
"""
