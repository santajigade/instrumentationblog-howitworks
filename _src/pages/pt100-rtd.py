PAGE = dict(
    slug="pt100-rtd", grp="Temperature", name="Pt100 RTD", kw="How a Pt100 RTD Works",
    title="How a Pt100 RTD Works: Animated Diagram and Formula",
    desc="How a Pt100 RTD works, animated: platinum resistance rises with temperature, the transmitter reads it with 2, 3 or 4 wires and lead errors appear.",
    h1="How a Pt100 RTD Works",
    hero="Change the process temperature, the resistance of each lead wire and the number of wires. Watch the platinum resistance follow the Callendar Van Dusen curve and see how much error the leads add in a two wire connection.",
    quick="A Pt100 RTD is a platinum resistor of 100 Ω at 0 °C whose resistance rises by about 0.385 Ω for every degree. The transmitter passes a small current through it, measures the voltage and converts the resistance to temperature with the IEC 60751 curve.",
    intro=["The Pt100 is the most common resistance temperature detector in process plants. It covers roughly −200 to 850 °C depending on construction and is accurate and stable enough for most control and custody duties.",
           "The sensing element is a fine platinum wire wound on a ceramic former or a thin platinum film on a ceramic chip. As the metal gets hotter its atoms vibrate more, the electrons scatter more and the resistance rises in a smooth and repeatable way.",
           "The element sits at the tip of a sheath inside a thermowell and is wired to a transmitter or a PLC RTD card. The lead wires also have resistance, so the way the sensor is connected decides how much of that resistance ends up in the reading."],
    sliders=[("t", "Process temperature", -50, 400, 100, 1, 0, "°C"), ("rl", "Resistance of each lead wire", 0, 5, 0.5, 0.1, 1, "Ω"), ("w", "Number of wires (2, 3 or 4)", 2, 4, 2, 1, 0, "")],
    outs=[("r", "Pt100 resistance R t (IEC 60751)"), ("rm", "Resistance seen by the transmitter"), ("e", "Temperature error from the leads"), ("v", "Voltage across the sensor at 1 mA")],
    legend=["Process liquid", "Thermowell and Pt100 element at the tip", "Connection head", "Lead wires: red and white per IEC 60751", "Transmitter with 1 mA excitation", "Close up: platinum lattice and electrons", "Callendar Van Dusen curve, R against t"],
    steps=["The transmitter drives a small constant current, typically about 1 mA, through the platinum element.",
           "Heat from the process passes through the thermowell and sheath and brings the element to the process temperature.",
           "The hotter platinum lattice scatters the electrons more, so the resistance rises along the Callendar Van Dusen curve.",
           "The transmitter measures the voltage across the element; in two wire hookup it also measures the drop in both leads, three wire cancels equal leads and four wire senses the element directly.",
           "The transmitter converts the resistance to temperature with the IEC 60751 equation and sends it as 4 to 20 mA or a digital value."],
    formula=["Callendar Van Dusen, 0 to 850 °C: R t = R0 × (1 + A × t + B × t²) with R0 = 100 Ω",
             "A = 3.9083 × 10⁻³ per °C and B = −5.775 × 10⁻⁷ per °C²; below 0 °C add R0 × C × (t − 100) × t³ with C = −4.183 × 10⁻¹² per °C⁴",
             "Two wire: R m = R t + 2 × R L; three wire cancels the leads when they are equal; four wire removes them fully",
             "Mean sensitivity from 0 to 100 °C: α = (R100 − R0) ÷ (100 × R0) = 0.00385 per °C",
             "Example: t = 100 °C: R = 100 × (1 + 0.39083 − 0.005775) = 138.51 Ω; two wire with 0.5 Ω per lead: R m = 139.51 Ω, which reads 102.64 °C, an error of 2.64 °C high"],
    parts=[("Platinum element", "Wire wound or thin film platinum resistor of 100 Ω at 0 °C"),
           ("Sheath and insulation", "Stainless steel tube packed with mineral insulation that protects the element and leads"),
           ("Thermowell", "Pressure retaining pocket that lets the sensor be removed without opening the process"),
           ("Connection head", "Terminal block where the sensor leads join the field cable"),
           ("Transmitter or RTD input card", "Supplies the excitation current, measures the resistance and linearises it to temperature")],
    uses=[("Process temperature control", "Reactor, column and heat exchanger temperatures where good accuracy is needed."),
          ("Bearing and winding temperature", "Monitoring of motors, pumps and turbines to trip on overheating."),
          ("Custody and energy metering", "Temperature compensation of liquid and gas flow measurement."),
          ("HVAC and utilities", "Chilled water, cooling water and steam header temperatures.")],
    pros=["High accuracy and good long term stability", "Nearly linear and covered by the IEC 60751 standard, so sensors are interchangeable", "Three and four wire hookups remove most of the lead error"],
    cons=["Lower maximum temperature than thermocouples", "Slower response and more fragile than a thin thermocouple", "Self heating from the excitation current and lead resistance can add error if ignored"],
    tips=["Use three or four wire connection for any run longer than a few metres; two wire adds about 2.6 °C per ohm of loop lead resistance.",
          "In three wire hookup the leads must be the same size and length, because the compensation assumes equal lead resistance.",
          "Check a suspect Pt100 by measuring its resistance and comparing it with the IEC 60751 table at the known temperature.",
          "Make sure the sheath reaches the bottom of the thermowell and is immersed at least ten sheath diameters, or heat conduction along the stem gives a low reading."],
    faq=[("Why is it called Pt100?", "Pt is the chemical symbol for platinum and 100 is its resistance in ohms at 0 °C. A Pt1000 uses the same curve with 1000 Ω at 0 °C."),
         ("What resistance should a Pt100 read at 100 °C?", "About 138.5 Ω by the IEC 60751 equation. At 0 °C it reads 100 Ω."),
         ("Which is better, three wire or four wire?", "Four wire removes the lead resistance completely, so it is used for laboratory and high accuracy work. Three wire is the usual choice in plants and is accurate when the leads are equal."),
         ("Can an RTD measure below zero?", "Yes. Below 0 °C the IEC 60751 equation adds a third term with the C coefficient, and the resistance falls below 100 Ω.")],
    cal=[("temperature/rtd-calculator", "RTD Calculator"), ("temperature/pt100-table", "Pt100 Table"), ("instrumentation-signal/rtd-lead-resistance-error-calculator", "RTD Lead Resistance Error Calculator")],
    glo=[("pt100", "Pt100"), ("rtd-wiring", "RTD Wiring"), ("alpha-coefficient", "Alpha Coefficient")],
    cmp=[("3-wire-vs-4-wire-rtd", "3 Wire vs 4 Wire RTD"), ("pt100-vs-pt1000", "Pt100 vs Pt1000"), ("rtd-vs-thermocouple", "RTD vs Thermocouple")],
    tool=[("tools/practice-tests/rtd-and-thermocouple-quiz", "RTD and Thermocouple Quiz")],
    blog=("what-is-rtd-and-how-it-works", "What is RTD and how it works"))

SCENE = r"""
var A=3.9083e-3,B=-5.775e-7,CC=-4.183e-12,tt=100,at=[];for(var i=0;i<5;i++)for(var j=0;j<3;j++)at.push([250+i*40,154+j*24,Math.random()*6.28]);
function R(t){var r=100*(1+A*t+B*t*t);if(t<0)r+=100*CC*(t-100)*t*t*t;return r;}
function inv(r){var t=(r-100)/0.385;for(var k=0;k<30;k++){var d=100*(A+2*B*t)+(t<0?100*CC*(4*t*t*t-300*t*t):0);t-=(R(t)-r)/d;}return t;}
function NW(){return Math.round(P.w);}
function rm(){return R(P.t)+(NW()==2?2*P.rl:0);}
function upd(){var r=R(P.t),x=rm(),e=inv(x)-P.t;o('r',m(r,2)+' Ω');o('rm',m(x,2)+' Ω'+(NW()==3?' (equal leads cancel)':NW()==4?' (leads not in the reading)':''));o('e',(Math.abs(e)<0.005?'0.00':m(e,2))+' °C'+(e>0.005?' high':''));o('v',m(r,1)+' mV');}
function step(dt){tt+=(P.t-tt)*Math.min(1,dt/1.5);}
function col(t){var u=clamp((t+50)/450,0,1);return 'rgba('+Math.round(96+159*u)+','+Math.round(165-90*u)+','+Math.round(250-180*u)+',0.85)';}
function draw(){var n=NW(),u=clamp((tt+50)/450,0,1);
L('Lattice vibration and electron motion drawn for illustration',20,22,11,'#5b6576','left');
rc(24,132,170,206,'#e2e8f0','#64748b',6);wave(30,188,160,332,col(tt));L(m(tt,0)+' °C',60,316,12,'#fff','center',1);
rc(102,90,14,214,'#cbd5e1','#475569',4);rc(105,268,8,28,'#fde68a','#a8620a',2);for(var k=0;k<5;k++)ln(105,272+k*5,113,274+k*5,'#a8620a',1);
rc(86,58,46,34,'#94a3b8','#334155',6);L('Head',109,75,11,'#1a2333','center',1);
var cols=n==2?['#dc2626','#e2e8f0']:n==3?['#dc2626','#dc2626','#e2e8f0']:['#dc2626','#dc2626','#e2e8f0','#e2e8f0'];
var cur=n==2?[1,1]:n==3?[1,0,1]:[1,0,0,1];
L('Lead resistance R L = '+m(P.rl,1)+' Ω in each wire',214,44,11,'#5b6576','left',1);
for(var i=0;i<n;i++){var y=60+i*11;ln(132,y,460,y,'#334155',5);ln(132,y,460,y,cols[i],3);rc(276,y-4,26,8,'#fbbf24','#a8620a',1);
if(cur[i]){C.setLineDash([3,9]);C.lineDashOffset=(i==0?-1:1)*T*30;ln(132,y,460,y,'#1e63b8',2,[3,9]);C.setLineDash([]);C.lineDashOffset=0;}}
var ty=60+n*11+4;L(n==2?'Both leads carry the current and add to the reading':n==3?'Third wire lets the bridge cancel equal leads':'Outer pair carries current, inner pair senses only',300,ty+6,11,'#5b6576','center');
rc(460,40,170,146,'#1a2333',null,8);L('Transmitter',545,54,11,'#cbd5e1','center',1);L(n+' wire input, 1 mA',545,72,11,'#cbd5e1','center');
var x=R(tt)+(n==2?2*P.rl:0),sh=inv(x);L('R m '+m(x,2)+' Ω',545,98,14,'#fbbf24','center',1);L('Shows '+m(sh,1)+' °C',545,124,14,'#fff','center',1);
var e=sh-tt;L(Math.abs(e)<0.05?'Lead error removed':'Lead error '+m(e,1)+' °C',545,150,11,Math.abs(e)<0.05?'#86efac':'#fda4af','center',1);
var g=0.5+0.5*Math.sin(T*6);ci(482,170,5,'rgba(34,197,94,'+(0.4+0.6*g)+')');L('4 to 20 mA out',494,170,11,'#cbd5e1','left');
rc(220,118,220,122,'#f8fafc','#cbd5e1',8);L('Platinum close up',228,130,11,'#5b6576','left',1);
var amp=1+5*u;at.forEach(function(a){ci(a[0]+amp*Math.sin(T*11+a[2]),a[1]+amp*Math.cos(T*9+a[2]*1.3),7,'#94a3b8','#475569',1);});
var sp=70*(100/R(tt));for(var k=0;k<9;k++){var px=224+((T*sp+k*41)%212),py=166+24*(k%2)+6*Math.sin(T*6+k*2)*u;ci(px,py,3,'#1e63b8');}
L(u>0.6?'Hot: strong vibration, more scattering':u<0.25?'Cold: weak vibration, less scattering':'Electrons scatter off vibrating atoms',330,228,11,'#1a2333','center');
var gx0=270,gx1=620,gy0=258,gy1=336,lo=70,hi=260,TX=function(t){return gx0+(t+50)/450*(gx1-gx0);},TY=function(r){return gy1-(r-lo)/(hi-lo)*(gy1-gy0);};
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');C.strokeStyle='#b02a52';C.lineWidth=2;C.beginPath();for(var t=-50;t<=400;t+=10){var X=TX(t),Y=TY(R(t));if(t>-50)C.lineTo(X,Y);else C.moveTo(X,Y);}C.stroke();
L('R, Ω',gx0,gy0-10,11,'#b02a52','left',1);L('t from −50 to 400 °C',gx1,gy0-10,11,'#5b6576','right');L('260',gx0-4,gy0+4,11,'#5b6576','right');L('70',gx0-4,gy1,11,'#5b6576','right');
var px=TX(tt),py=TY(R(tt));ln(px,py,px,gy1,'#b02a52',1,[3,3]);ci(px,py,5+g,'#b02a52','#fff',2);if(n==2&&P.rl>0){var y2=TY(x);ci(TX(sh),y2,4,'#a8620a');}
mk(1,48,148);mk(2,130,284);mk(3,70,62);mk(4,190,44);mk(5,616,54);mk(6,428,130);mk(7,gx0+14,gy0+14);}
"""
