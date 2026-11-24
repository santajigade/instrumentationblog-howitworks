var PER=4.8,ph=0,TS=0.2;
function upd(){}
function sig(t){var w=2*Math.PI/PER;return 50+28*Math.sin(w*t)+9*Math.sin(3*w*t+0.6);}
function step(dt){ph=(ph+dt)%PER;}
function draw(){
L('Signal and sampling rate slowed down to show the idea',20,22,11,'#5b6576','left');
var v=sig(ph);
// transducer and conditioning
rc(20,165,90,50,'#e0f2fe','#0369a1',8);L('Transducer',65,190,12,'#0c4a6e','center',1);
ar(110,190,132,190,'#334155',2);
rc(134,160,90,60,'#ede9fe','#6d28d9',8);L('Signal',179,181,12,'#4c1d95','center',1);L('conditioning',179,198,12,'#4c1d95','center',1);
ln(224,190,236,190,'#334155',2);ln(236,105,236,275,'#334155',2);ar(236,105,252,105,'#334155',2);ar(236,275,252,275,'#334155',2);
L('Temperature',65,150,11,'#475569');
// analog path
L('Analog system: continuous',350,52,13,'#0f766e','center',1);
rc(254,65,200,80,'#f0fdfa','#99f6e4',6);
C.strokeStyle='#0f766e';C.lineWidth=2.5;C.beginPath();
for(var x=0;x<=200;x+=2){var t=ph-(200-x)*0.012,y=145-sig(t)*0.8;if(x==0)C.moveTo(254+x,y);else C.lineTo(254+x,y);}C.stroke();
// meter
var cx=550,cy=125;C.fillStyle='#fff';C.strokeStyle='#475569';C.lineWidth=2.5;C.beginPath();C.arc(cx,cy,62,Math.PI,2*Math.PI);C.closePath();C.fill();C.stroke();
for(var k=0;k<=10;k++){var an=Math.PI+k*Math.PI/10;ln(cx+52*Math.cos(an),cy+52*Math.sin(an),cx+60*Math.cos(an),cy+60*Math.sin(an),'#475569',k%5?1:2);}
L('0',cx-46,cy-8,11,'#475569');L('100',cx+44,cy-8,11,'#475569');
var an=Math.PI+v/100*Math.PI;ln(cx,cy,cx+50*Math.cos(an),cy+50*Math.sin(an),'#dc2626',3);ci(cx,cy,5,'#1f2937');
L('Pointer and scale',cx,cy+16,12,'#1f2733','center',1);
// digital path
L('Digital system: discrete',350,222,13,'#1d4ed8','center',1);
rc(254,245,60,60,'#dbeafe','#1d4ed8',8);L('A/D',284,267,13,'#1e3a8a','center',1);L('converter',284,284,10,'#1e3a8a','center');
ar(314,275,330,275,'#334155',2);
rc(332,235,150,80,'#eff6ff','#bfdbfe',6);
C.strokeStyle='#1d4ed8';C.lineWidth=2.5;C.beginPath();var first=true;
for(var x=0;x<=150;x+=1){var t=ph-(150-x)*0.016,ts=Math.floor(t/TS)*TS,y=315-sig(ts)*0.8;if(first){C.moveTo(332+x,y);first=false;}else C.lineTo(332+x,y);}C.stroke();
for(var j=0;j<13;j++){var ts=Math.floor(ph/TS)*TS-j*TS,x=332+150-(ph-ts)/0.016;if(x>=332)ci(x,315-sig(ts)*0.8,3,'#1d4ed8');}
var vs=sig(Math.floor(ph/TS)*TS),code=Math.round(vs*2.55);
rc(500,240,125,70,'#0f172a',null,8);L(m(vs,1)+' %',562,265,20,'#4ade80','center',1);
var b=code.toString(2);while(b.length<8)b='0'+b;L(b,562,292,13,'#93c5fd','center',1);
L('8 bit code',562,326,11,'#475569');
mk(1,65,236);mk(2,179,140);mk(3,cx+72,cy-50);mk(4,284,325);mk(5,470,228);mk(6,615,342);
}
