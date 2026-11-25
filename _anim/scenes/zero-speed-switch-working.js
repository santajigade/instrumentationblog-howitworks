var PER=4.8,ph=0,Q=Math.PI/2,K=14*Q/3.4,CX=150,CY=205,R=62;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function wv(t){t=((t%PER)+PER)%PER;if(t<2.4)return 1;if(t<3.4)return 1-sm(t-2.4);if(t<3.8)return 0;return sm(t-3.8);}
function I(u){return u*u*u-u*u*u*u/2;}
function th(t){var n=Math.floor(t/PER),u=t-n*PER,a=0;if(u<2.4)a=u;else{a=2.4;if(u<3.4)a+=(u-2.4)-I(u-2.4)+0;else{a+=0.5;if(u>=3.8)a+=I(u-3.8);}}return K*(a+n*3.4);}
function state(t){var w=wv(t);if(t<2.4)return 0;if(t<3.8)return w<0.8?2:1;return 3;}
function draw(){
L('Shaft slowed for viewing; belt slip, trip and restart shown in one 4.8 s cycle',20,22,11,'#5b6576','left');
var w=wv(ph),a=th(ph),st=state(ph);
// belt
var trav=K*3.4*R,p=trav/150;C.strokeStyle='#334155';C.lineWidth=7;C.setLineDash([p*0.62,p*0.38]);C.lineDashOffset=a*R;
C.beginPath();C.moveTo(330,CY-R-4);C.lineTo(CX,CY-R-4);C.arc(CX,CY,R+4,-Q,Q,true);C.lineTo(330,CY+R+4);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L('Belt',300,CY-R-20,12,'#334155','center',1);L('to drive pulley',300,CY+R+22,11,'#5b6576');
// pulley
ci(CX,CY,R,'#cbd5e1','#475569',2.5);ci(CX,CY,14,'#64748b');
for(var k=0;k<4;k++){var b=a+k*Q;ln(CX+14*Math.cos(b),CY+14*Math.sin(b),CX+(R-4)*Math.cos(b),CY+(R-4)*Math.sin(b),'#94a3b8',5);
var bx=CX+(R-16)*Math.cos(b),by=CY+(R-16)*Math.sin(b);C.save();C.translate(bx,by);C.rotate(b);rc(-7,-7,14,14,'#f59e0b','#92400e',2);C.restore();}
L('Tail pulley',CX,CY+R+38,12,'#1f2733','center',1);
// sensor facing the bolt circle on the face (left)
var sx=CX-(R-16),near=false;for(var k=0;k<4;k++){var b=((a+k*Q)%(2*Math.PI)+2*Math.PI)%(2*Math.PI);if(Math.abs(b-Math.PI)<0.16)near=true;}
rc(22,CY-9,sx-34,18,'#0f766e','#134e4a',3);ci(sx-12,CY,5,near?'#facc15':'#99f6e4');L('Sensor',40,CY-22,11,'#0f766e','left',1);
// pulse train panel
var px=360,py=52,pw=260,ph2=86;rc(px,py,pw,ph2,'#f8fafc','#94a3b8',6);L('Sensor pulses, last 2 s',px+8,py+12,11,'#334155','left',1);
C.strokeStyle='#0f766e';C.lineWidth=2;C.beginPath();
for(var i=0;i<=240;i++){var tt=ph-2+2*i/240,b=th(tt+PER)%Q,on=(b<0.16||b>Q-0.16);var x=px+10+i,y=on?py+34:py+74;if(i==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
// speed logic
var f=4*w;rc(360,152,260,92,'#f8fafc','#94a3b8',6);L('Speed logic',370,166,12,'#1f2733','left',1);
L('f = RPM × N ÷ 60 = '+(60*w).toFixed(0)+' × 4 ÷ 60 = '+f.toFixed(2)+' Hz',370,188,11,'#1f2733','left');
rc(370,204,240,14,'#e5e7eb');rc(370,204,240*f/4,14,f<3.2?'#dc2626':'#16a34a');ln(370+240*0.8,198,370+240*0.8,224,'#1f2733',2);
L("Trip setpoint 80 % = 3.20 Hz",612,234,11,"#1f2733","right");
// relay
var en=(st==0||st==1||st==3),tx=['RUNNING, relay energised','Belt slip: speed falling','UNDERSPEED TRIP, drive stopped','Restart: start delay blocks trip'][st];
rc(360,258,260,74,en?'#dcfce7':'#fee2e2',en?'#16a34a':'#dc2626',6);L(tx,490,280,12,en?'#166534':'#991b1b','center',1);
L('Fail safe relay to MCC or PLC',490,304,11,'#334155');ci(380,318,7,en?'#22c55e':'#e5e7eb','#475569');L(en?'contact closed':'contact open',394,318,11,'#334155','left');
mk(1,CX+R+12,CY+48);mk(2,CX+(R-16)*Math.cos(a+Q),CY+(R-16)*Math.sin(a+Q));mk(3,22,CY+26);mk(4,606,py+16);mk(5,606,166);mk(6,606,272);
}
