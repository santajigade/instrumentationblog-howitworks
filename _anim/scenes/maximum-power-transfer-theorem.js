var PER=4.8,ph=0,RL=4,VTH=12,RTH=4;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;RL=RTH*Math.pow(2,2.5*Math.sin(2*Math.PI*u));}
function pw(r){return VTH*VTH*r/((RTH+r)*(RTH+r));}
function gx(r){return 350+(Math.log(r)/Math.LN2+1)/6*260;}
function gy(p){return 290-p/12*210;}
function zz(x1,y1,x2,y2,c){var n=6,dx=(x2-x1)/n,dy=(y2-y1)/n,len=Math.hypot(x2-x1,y2-y1),nx=-(y2-y1)/len*9,ny=(x2-x1)/len*9;C.strokeStyle=c;C.lineWidth=2.5;C.beginPath();C.moveTo(x1,y1);for(var i=0;i<n;i++){var s=(i%2?-1:1);C.lineTo(x1+dx*(i+.5)+nx*s,y1+dy*(i+.5)+ny*s);}C.lineTo(x2,y2);C.stroke();}
function draw(){
var I=VTH/(RTH+RL),VL=I*RL,P=VL*I,eta=RL/(RL+RTH)*100,at=Math.abs(Math.log(RL/RTH))<0.12;
L('Load resistance sweeps from about 0.7 Ω to 22 Ω; current dots move at a fixed speed',20,22,11,'#5b6576','left');
// circuit wires
var wc='#334155';
ln(80,164,80,80,wc,2.5);ln(80,80,130,80,wc,2.5);zz(130,80,220,80,'#b45309');ln(220,80,280,80,wc,2.5);
ln(280,80,280,130,wc,2.5);zz(280,130,280,230,'#2563eb');ln(280,230,280,300,wc,2.5);ln(280,300,80,300,wc,2.5);ln(80,300,80,216,wc,2.5);
// current flow, width shows size of current
C.globalAlpha=0.35+0.65*I/3;C.setLineDash([5,10]);C.lineDashOffset=-ph/PER*150;C.strokeStyle='#16a34a';C.lineWidth=1.5+I*1.2;
C.beginPath();C.moveTo(80,150);C.lineTo(80,92);C.lineTo(268,92);C.lineTo(268,288);C.lineTo(92,288);C.lineTo(92,230);C.stroke();C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
// variable arrow on RL
ar(250,230,312,140,'#1e3a8a',2);
// source
ci(80,190,26,'#fff','#334155',2.5);L('+',80,176,15,'#dc2626','center',1);L('12 V',80,200,12,'#1f2733','center',1);
L('Rth = 4 Ω',175,58,13,'#b45309','center',1);L('RL',296,206,14,'#2563eb','left',1);
// readouts
var rx=118,ry=128;
L('RL = '+m(RL,2)+' Ω',rx,ry,13,'#2563eb','left',1);
L('I = '+m(I,2)+' A',rx,ry+24,13,'#1f2733','left');
L('VL = '+m(VL,2)+' V',rx,ry+48,13,'#1f2733','left');
L('P = '+m(P,2)+' W',rx,ry+72,13,at?'#16a34a':'#1f2733','left',1);
L('η = '+m(eta,0)+' %',rx,ry+96,13,'#1f2733','left');
L('P = VL × I',rx,ry+124,12,'#5b6576','left');
// graph
rc(338,52,290,272,'#f8fafc','#cbd5e1',8);
ln(350,290,610,290,'#475569',1.5);ln(350,290,350,78,'#475569',1.5);
var tk=[0.5,1,2,4,8,16,32];for(var i=0;i<tk.length;i++){var x=gx(tk[i]);ln(x,290,x,295,'#475569',1.2);L(String(tk[i]),x,304,11,'#5b6576');}
for(var p=0;p<=10;p+=5){ln(345,gy(p),350,gy(p),'#475569',1.2);L(String(p),340,gy(p),11,'#5b6576','right');}
L('Load RL in Ω (log scale)',480,318,11,'#5b6576');L('P (W)',356,68,11,'#5b6576','left');
ln(gx(4),gy(9),gx(4),290,'#16a34a',1.2,[4,4]);L('RL = Rth',gx(4)+6,276,12,'#16a34a','left',1);
C.strokeStyle='#d9622b';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=120;k++){var r=0.5*Math.pow(2,6*k/120),x=gx(r),y=gy(pw(r));if(k)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
L('Pmax = 9 W',gx(4),gy(9)-26,12,'#d9622b','center',1);
var dx=gx(RL),dy=gy(P);ln(dx,dy,dx,290,'#2563eb',1,[3,3]);ci(dx,dy,7,'#2563eb','#fff',2);
L(at?'Matched: maximum power, 50 % efficiency':(RL<RTH?'RL < Rth: high current, low voltage':'RL > Rth: high voltage, low current'),20,342,12,at?'#16a34a':'#334155','left',1);
mk(1,40,190);mk(2,175,108);mk(3,308,250);mk(4,gx(4),238);mk(5,dx>560?dx-24:dx+20,dy+18);
}
