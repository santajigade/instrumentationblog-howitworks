var PER=4.8,ph=0,u=0,t=0,R=100,V=100;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;t=50-50*Math.cos(2*Math.PI*u);R=100*(1+0.00385*t);V=R*1.0;}
function hot(a){var r=Math.round(59+(220-59)*a),g=Math.round(130+(38-130)*a),b=Math.round(246+(38-246)*a);return 'rgb('+r+','+g+','+b+')';}
function draw(){
L('Pt100, linear form R = R0(1 + αT); motion slowed for clarity',20,22,11,'#5b6576','left');
var a=t/100;
// process pipe
var cy=118,R0=30;
rc(20,cy-R0-10,240,10,'#9aa5b8');rc(20,cy+R0,240,10,'#9aa5b8');
C.globalAlpha=0.35+0.4*a;rc(20,cy-R0,240,2*R0,hot(a));C.globalAlpha=1;
for(var k=0;k<4;k++){var x=24+((u*220+k*55)%220);ar(x,cy+16,x+20,cy+16,'#1e3a8a',2);}
L('Process fluid',30,cy-R0-20,11,'#1e3a8a','left',1);
// thermowell and element
rc(124,48,32,22,'#475569',null,4);L('Head',140,59,11,'#fff','center',1);
rc(132,70,16,72,'#cbd5e1','#64748b',6);
C.strokeStyle=hot(a);C.lineWidth=2.5;C.beginPath();for(var k=0;k<=40;k++){var yy=96+k*1.0,xx=140+5*Math.sin(k*1.2);if(k==0)C.moveTo(xx,yy);else C.lineTo(xx,yy);}C.stroke();
// wires to instruments
ln(156,54,330,54,'#334155',2);ln(156,64,275,64,'#334155',2);ln(275,64,275,150,'#334155',2);ln(330,54,330,80,'#334155',2);
// current flow dots on wire (whole cycles)
C.setLineDash([5,7]);C.lineDashOffset=-u*48;C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();C.moveTo(330,54);C.lineTo(156,54);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
// constant current source
rc(290,80,110,44,'#ecfdf5','#16a34a',6);L('Constant current',345,94,11,'#166534','center',1);L('I = 1 mA',345,111,12,'#166534','center',1);
// voltmeter
rc(265,150,140,54,'#fff','#334155',6);L('Voltage V = I × R',335,164,11,'#334155','center',1);
rc(287,174,96,24,'#1f2937',null,4);L(m(V,1)+' mV',335,186,13,'#a3e635','center',1);
// lattice zoom
rc(20,182,240,150,'#f8fafc','#94a3b8',8);L('Inside the platinum wire',30,198,11,'#334155','left',1);
var amp=0.5+4.5*a;
for(var i=0;i<6;i++)for(var j=0;j<3;j++){var bx=50+i*36,by=232+j*36;var dx=amp*Math.sin(2*Math.PI*(u*7+i*0.37+j*0.61)),dy=amp*Math.cos(2*Math.PI*(u*9+i*0.53+j*0.29));ci(bx+dx,by+dy,8,'#94a3b8','#475569',1.5);}
for(var k=0;k<7;k++){var ex=30+((u*2*220+k*32)%220),ey=250+((k*23)%60)+3*a*Math.sin(2*Math.PI*(u*6+k*0.3));ci(ex,ey,3.5,'#2563eb');}
L('Hotter: atoms vibrate harder',140,322,11,'#5b21b6','center');
// readout
rc(430,40,190,96,'#1f2937',null,8);
L('T = '+m(t,1)+' °C',525,64,16,hot(a),'center',1);L('R = '+m(R,2)+' Ω',525,90,16,'#fff','center',1);L('V = '+m(V,1)+' mV',525,116,14,'#a3e635','center',1);
// graph R vs T
var gx=450,gy=320,gw=160,gh=140;
ln(gx,gy,gx+gw,gy,'#64748b',1.5);ln(gx,gy,gx,gy-gh,'#64748b',1.5);
function py(r){return gy-(r-95)/(145-95)*gh;}
ln(gx,py(100),gx+gw,py(138.5),'#dc2626',2.5);
var px=gx+gw*t/100;ln(px,gy,px,py(R),'#94a3b8',1,[3,3]);ci(px,py(R),5,'#dc2626','#fff',2);
L('0',gx,gy+12,11,'#334155','center');L('100 °C',gx+gw,gy+12,11,'#334155','center');
L('100 Ω',gx-4,py(100),11,'#334155','right');L('138.5 Ω',gx+gw-4,py(138.5)-12,11,'#334155','right');
L('Resistance vs temperature',gx+16,gy-gh-14,11,'#1e3a8a','left',1);
mk(1,168,118);mk(2,236,96);mk(3,240,214);mk(4,416,102);mk(5,418,177);mk(6,446,166);
}
