var PER=4.8,ph=0,TX=82,TY=88,RY=134,WX=575,D=WX-TX-18,V=2*(WX-TX-18)/3.2,TS0=0.3,TB1=0.6,TE1=3.8;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function tx(t){return 110+t*500/PER;}
function sig(t0,t1,y,col){ln(tx(t0),y,tx(t1),y,col,2.5);}
function rowTrig(col){var y=238;C.strokeStyle=col;C.lineWidth=2.5;C.beginPath();C.moveTo(tx(0),y);C.lineTo(tx(0),y-18);C.lineTo(tx(TS0),y-18);C.lineTo(tx(TS0),y);C.lineTo(tx(PER),y);C.stroke();}
function rowBurst(col){var y=278;C.strokeStyle=col;C.lineWidth=2;C.beginPath();C.moveTo(tx(0),y);var w=(TB1-TS0)/8;for(var k=0;k<8;k++){var a=TS0+k*w;C.lineTo(tx(a),y);C.lineTo(tx(a),y-18);C.lineTo(tx(a+w/2),y-18);C.lineTo(tx(a+w/2),y);}C.lineTo(tx(PER),y);C.stroke();}
function rowEcho(col){var y=318;C.strokeStyle=col;C.lineWidth=2.5;C.beginPath();C.moveTo(tx(0),y);C.lineTo(tx(TB1),y);C.lineTo(tx(TB1),y-18);C.lineTo(tx(TE1),y-18);C.lineTo(tx(TE1),y);C.lineTo(tx(PER),y);C.stroke();}
function draw(){
L('Time slowed down: real TRIG is 10 µs and echo time is 1000 µs',20,22,11,'#5b6576','left');
// module board
rc(30,52,34,120,'#1e3a8a','#0f1f4d',6);L('SR04',47,182,12,'#1e3a8a','center',1);
ci(TX,TY,18,'#cbd5e1','#475569',2);ci(TX,TY,9,'#64748b');L('T',TX,TY,11,'#fff','center',1);
ci(TX,RY,18,'#cbd5e1','#475569',2);ci(TX,RY,9,'#64748b');L('R',TX,RY,11,'#fff','center',1);
// target wall
rc(WX,52,22,120,'#94a3b8','#475569');for(var y=58;y<170;y+=14)ln(WX+2,y+10,WX+20,y,'#64748b',1.2);
L('Target',WX+11,42,12,'#334155','center',1);
ar(TX+24,TY,WX-6,TY,'#dbe3ee',1.5);ar(WX-6,RY,TX+24,RY,'#dbe3ee',1.5);L('Outgoing burst',200,56,11,'#2563eb','center');L('Echo from target',200,162,11,'#16a34a','center');
// sound arcs
var w=(TB1-TS0)/8;C.lineCap='round';
for(var k=0;k<8;k++){var d=V*(ph-(TS0+k*w));if(d<=0||d>=2*D)continue;
 if(d<D){var a=Math.min(0.6,Math.asin(Math.min(1,18/Math.max(d,30))));C.strokeStyle='#2563eb';C.lineWidth=3;C.beginPath();C.arc(TX+18,TY,d,-a,a);C.stroke();}
 else{var cx=2*(WX)-TX-18,cy=RY,a=Math.min(0.6,Math.asin(Math.min(1,18/Math.max(d,30))));C.strokeStyle='#16a34a';C.lineWidth=3;C.beginPath();C.arc(cx,cy,d,Math.PI-a,Math.PI+a);C.stroke();}}
C.lineCap='butt';
// distance dimension
ar(330,176,TX+22,176,'#475569',1.5);ar(330,176,WX-4,176,'#475569',1.5);rc(300,167,60,18,'#fff',null,4);L('17.2 cm',330,176,12,'#334155','center',1);
L('Distance = 343.4 m/s × 1000 µs ÷ 2 = 17.2 cm at 20 °C',360,202,13,'#1f2733','center',1);
// timing diagram
L('TRIG',96,229,12,'#334155','right',1);L('Burst',96,269,12,'#334155','right',1);L('ECHO',96,309,12,'#334155','right',1);
rowTrig('#cbd5e1');rowBurst('#cbd5e1');rowEcho('#cbd5e1');
C.save();C.beginPath();C.rect(tx(0)-2,205,tx(ph)-tx(0)+2,125);C.clip();rowTrig('#dc2626');rowBurst('#2563eb');rowEcho('#16a34a');C.restore();
L('10 µs pulse',tx(TS0)+10,222,11,'#dc2626','left');
L('8 cycles at 40 kHz',tx(TB1)+10,262,11,'#2563eb','left');
var tm=ph<TB1?0:ph<TE1?(ph-TB1)/(TE1-TB1)*1000:1000;
L('Echo width = round trip time: '+m(tm,0)+' µs',(tx(TB1)+tx(TE1))/2,340,12,'#16a34a','center',1);
var cx=tx(ph);ln(cx,213,cx,326,'#f97316',2,[4,4]);
mk(1,TX+26,TY-24);mk(2,TX+26,RY+24);mk(3,300,56);mk(4,WX-16,66);mk(5,tx(0)+16,206);mk(6,tx(TE1)+18,296);
}
