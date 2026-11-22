var PER=4.8,ph=0,u=0,Rx=250,vo=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;var sn=Math.sin(2*Math.PI*u);Rx=250+5*(sn>0?1:-1)*Math.max(0,Math.abs(sn)-0.15)/0.85;vo=10*(Rx/(250+Rx)-0.5)*1000;}
function rz(a,b,lab,col){ln(a[0],a[1],b[0],b[1],'#334155',2.5);var mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2;C.save();C.translate(mx,my);C.rotate(Math.atan2(b[1]-a[1],b[0]-a[0]));rc(-22,-9,44,18,'#fff',null,4);rc(-22,-9,44,18,col,'#334155',4);C.restore();}
function draw(){
L('Illustrative 10 V excitation; strain gauge change exaggerated',20,22,11,'#5b6576','left');
var cx=215,cy=190,r=105;var N=[cx,cy-r],E=[cx+r,cy],S=[cx,cy+r],Wp=[cx-r,cy];
var imb=clamp(Math.abs(vo)/50,0,1);
rz(N,Wp,'R1','#dbeafe');rz(Wp,S,'R2','#dbeafe');rz(N,E,'R3','#fef3c7');
var hot='rgba(220,38,38,'+(0.25+0.6*imb)+')';rz(E,S,'Rx',hot);
L('R1 100 Ω',cx-110,cy-72,12,'#1e3a8a','right',1);L('R2 100 Ω',cx-110,cy+72,12,'#1e3a8a','right',1);
L('R3 250 Ω',cx+110,cy-72,12,'#92400e','left',1);L('Rx '+m(Rx,1)+' Ω',cx+110,cy+72,12,'#b91c1c','left',1);
[N,E,S,Wp].forEach(function(p){ci(p[0],p[1],4,'#334155');});
// excitation battery
ln(N[0],N[1],N[0],50,'#334155',2.5);ln(S[0],S[1],S[0],330,'#334155',2.5);
ln(N[0],50,40,50,'#334155',2.5);ln(40,50,40,170,'#334155',2.5);ln(40,210,40,330,'#334155',2.5);ln(40,330,S[0],330,'#334155',2.5);
ln(28,170,52,170,'#334155',3);ln(33,180,47,180,'#334155',3);ln(28,190,52,190,'#334155',3);ln(33,200,47,200,'#334155',3);ln(40,200,40,210,'#334155',2.5);
L('+',22,170,13,'#334155','center',1);L('VIN',62,152,12,'#334155','left',1);L('10 V',62,166,11,'#5b6576','left');
// galvanometer branch
var gx=cx,gy=cy;ln(Wp[0],Wp[1],gx-30,gy,'#334155',2);ln(gx+30,gy,E[0],E[1],'#334155',2);
ci(gx,gy,28,'#fff','#334155',2.5);L('G',gx,gy+14,11,'#334155','center',1);
var ang=clamp(vo/50,-1,1)*1.0;C.strokeStyle='#dc2626';C.lineWidth=2.5;C.beginPath();C.moveTo(gx,gy+8);C.lineTo(gx+20*Math.sin(ang),gy+8-20*Math.cos(ang));C.stroke();ci(gx,gy+8,3,'#dc2626');
// current dots in galvanometer branch
if(imb>0.08){var dir=vo>0?-1:1;for(var k=0;k<4;k++){var f=((ph*1.25+k/4)%1);var x0=dir>0?Wp[0]:E[0],x1=dir>0?E[0]:Wp[0];var x=x0+(x1-x0)*f;if(Math.abs(x-gx)>32){C.globalAlpha=imb;ci(x,gy,3.5,'#16a34a');C.globalAlpha=1;}}}
// readout panel
rc(410,60,210,118,'#f8fafc','#cbd5e1',8);
L('Output between midpoints',515,78,12,'#334155','center',1);
var bal=Math.abs(vo)<0.05;
L(m(vo,1)+' mV',515,110,26,bal?'#16a34a':'#b91c1c','center',1);
L(bal?'BALANCED: no current in G':'UNBALANCED: current flows',515,142,12,bal?'#16a34a':'#b91c1c','center',1);
L('Balance: R1 / R2 = R3 / Rx',515,162,11,'#5b6576','center');
// trend
var gx2=420,gy2=320,gw=200,gh=110;rc(410,195,210,140,'#fff','#e2e8f0',8);
ln(gx2,gy2-gh/2,gx2+gw-10,gy2-gh/2,'#cbd5e1',1,[4,4]);L('0 mV',gx2+gw-12,gy2-gh/2-9,11,'#5b6576','right');
C.strokeStyle='#b91c1c';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=80;k++){var x=gx2+(gw-10)*k/80;var sk=Math.sin(2*Math.PI*k/80);var rr=250+5*(sk>0?1:-1)*Math.max(0,Math.abs(sk)-0.15)/0.85;var v=10*(rr/(250+rr)-0.5)*1000;var y=gy2-gh/2-v/50*(gh/2-8);if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
var yy=gy2-gh/2-vo/50*(gh/2-8);ci(gx2+(gw-10)*u,yy,5,'#b91c1c','#fff',2);
L('Rx changes, output follows',gx2,207,11,'#334155','left',1);
mk(1,cx-62,cy-82);mk(2,cx+62,cy+82);mk(3,gx,gy-44);mk(4,22,140);mk(5,600,96);
}
