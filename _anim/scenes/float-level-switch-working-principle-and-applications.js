var PER=4.8,ph=0;
var TX0=70,TX1=330,TY0=70,TY1=320,SX=195,YH=130,YL=262;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function lev(t){return YL-(YL-YH)*(1-Math.cos(2*Math.PI*t/PER))/2;}
function reed(y,on){rc(SX-4,y-11,8,22,'rgba(186,230,253,0.95)','#0284c7',4);C.strokeStyle='#b45309';C.lineWidth=2;C.beginPath();C.moveTo(SX,y-10);C.lineTo(SX+(on?0:-2),y-1);C.moveTo(SX,y+10);C.lineTo(SX+(on?0:2),y+1);C.stroke();if(on)ci(SX,y,3,'#facc15');}
function lamp(x,y,on,lab){ci(x,y,8,on?'#22c55e':'#e5e7eb','#475569',1.5);L(lab,x+16,y,12,'#1f2733','left',1);}
function draw(){
var lv=lev(ph),fy=lv-4,hiOn=lv<YH+3,loOn=lv>YL-3,pump=(ph<2.4&&!hiOn)||loOn;
L('Fill and drain shortened to one 4.8 s cycle',20,22,11,'#5b6576','left');
// liquid
C.fillStyle='#bfdbfe';C.beginPath();C.moveTo(TX0,TY1);for(var x=TX0;x<=TX1;x+=4)C.lineTo(x,lv+2*Math.sin(x/14+2*Math.PI*ph/1.2));C.lineTo(TX1,TY1);C.closePath();C.fill();
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();for(var x=TX0;x<=TX1;x+=4){var y=lv+2*Math.sin(x/14+2*Math.PI*ph/1.2);if(x==TX0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
// tank walls
C.strokeStyle='#475569';C.lineWidth=5;C.beginPath();C.moveTo(TX0,TY0);C.lineTo(TX0,TY1);C.lineTo(TX1,TY1);C.lineTo(TX1,TY0);C.lineTo(TX0,TY0);C.stroke();
// level marks
ln(TX0-8,YH,TX0,YH,'#dc2626',2);ln(TX0-8,YL,TX0,YL,'#ea580c',2);L('High',TX0-12,YH,11,'#dc2626','right',1);L('Low',TX0-12,YL,11,'#ea580c','right',1);
// inlet from pump
ln(290,100,370,100,'#64748b',8);ln(290,96,290,TY0+2,'#64748b',8);
if(pump){C.strokeStyle='#3b82f6';C.lineWidth=5;C.setLineDash([6,6]);C.lineDashOffset=-ph*50;C.beginPath();C.moveTo(290,TY0+4);C.lineTo(290,lv);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
// pump
ln(410,100,446,100,'#64748b',8);L('Supply',446,84,11,'#334155','right');
ci(390,100,20,pump?'#dbeafe':'#e5e7eb','#334155',2.5);var w0=0.2311,tOn=pump?(ph>=2.4?ph-(PER-w0):ph+w0):0,an=2*Math.PI*3*clamp(tOn,0,2.4)/2.4;for(var k=0;k<4;k++){var a=an+k*Math.PI/2;ln(390,100,390+14*Math.cos(a),100+14*Math.sin(a),'#1e3a8a',3);}ci(390,100,4,'#1e3a8a');
// outlet
ln(TX1,300,440,300,'#64748b',8);C.strokeStyle='#3b82f6';C.lineWidth=3;C.setLineDash([5,7]);C.lineDashOffset=-ph*30;C.beginPath();C.moveTo(TX1+4,300);C.lineTo(440,300);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L('Outlet to process',385,284,11,'#334155','center',1);
// stem and switch head
rc(SX-7,60,14,TY1-70,'#e2e8f0','#64748b');rc(SX-22,36,44,24,'#475569',null,4);L('Head',SX,48,11,'#fff','center',1);
reed(YH,hiOn);reed(YL,loOn);
// float with magnet ring
rc(SX-32,fy-14,64,28,'rgba(250,204,21,0.92)','#a16207',8);rc(SX-12,fy-5,8,10,'#dc2626');rc(SX+4,fy-5,8,10,'#2563eb');
ar(SX+44,fy+38,SX+44,fy+18,'#15803d',2.5);L('Buoyant force',SX+52,fy+30,11,'#15803d','left',1);
// wiring to controller
C.strokeStyle='#7c3aed';C.lineWidth=1.8;C.beginPath();C.moveTo(SX+22,48);C.lineTo(530,48);C.lineTo(530,156);C.stroke();
C.strokeStyle='#334155';C.beginPath();C.moveTo(462,236);C.lineTo(390,236);C.lineTo(390,120);C.stroke();
// controller
rc(462,156,158,120,'#f8fafc','#334155',8);L('Pump controller',541,174,12,'#1f2733','center',1);
lamp(480,200,hiOn,'HIGH reed '+(hiOn?'closed':'open'));lamp(480,224,loOn,'LOW reed '+(loOn?'closed':'open'));
L(pump?'Pump RUNNING':'Pump STOPPED',541,254,13,pump?'#16a34a':'#dc2626','center',1);
L('Starts at LOW level',462,300,11,'#334155','left');L('Stops at HIGH level',462,318,11,'#334155','left');
mk(1,SX-46,fy);mk(2,SX+40,YH);mk(3,SX+40,YL);mk(4,390,64);mk(5,606,164);mk(6,420,318);
}
