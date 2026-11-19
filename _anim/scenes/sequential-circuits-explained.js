var PER=4.8,ph=0,TP=1.2,E0=0.3;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function clk(t){var u=((t-E0)%TP+TP)%TP;return u<0.6?1:0;}
function xin(t){return (t<0.8||(t>=1.7&&t<1.9)||(t>=2.0&&t<3.2)||t>=4.5)?1:0;}
function qv(t){return (t>=0.3&&t<2.7)?1:0;}
function col(v){return v?'#16a34a':'#94a3b8';}
function wire(pts,v){C.strokeStyle=col(v);C.lineWidth=v?3.5:2.5;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();
if(v){C.setLineDash([5,7]);C.lineDashOffset=-ph*62.5;C.strokeStyle='#bbf7d0';C.lineWidth=2;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}}
function xorG(x,y){C.fillStyle='#fff';C.strokeStyle='#1e3a8a';C.lineWidth=2.5;C.beginPath();C.moveTo(x,y-28);C.quadraticCurveTo(x+40,y-28,x+62,y);C.quadraticCurveTo(x+40,y+28,x,y+28);C.quadraticCurveTo(x+14,y,x,y-28);C.closePath();C.fill();C.stroke();
C.beginPath();C.moveTo(x-9,y-28);C.quadraticCurveTo(x+5,y,x-9,y+28);C.stroke();L('XOR',x+30,y,12,'#1e3a8a','center',1);}
function trace(f,cy,x0,s,c){C.strokeStyle=c;C.lineWidth=2.5;C.beginPath();var prev=f(0);C.moveTo(x0,cy+(prev?-11:11));
for(var t=0.01;t<=PER+0.001;t+=0.01){var v=f(Math.min(t,PER-0.0001));var x=x0+t*s;if(v!=prev){C.lineTo(x,cy+(prev?-11:11));C.lineTo(x,cy+(v?-11:11));prev=v;}else C.lineTo(x,cy+(v?-11:11));}C.stroke();}
function draw(){
var X=xin(ph),Q=qv(ph),D=X^Q,K=clk(ph);
var u=((ph-E0)%TP+TP)%TP,fl=u<0.3?1-u/0.3:0;
L('Slowed down. Q changes only on a rising clock edge',20,22,11,'#5b6576','left');
// external input X
rc(32,70,40,36,X?'#16a34a':'#e2e8f0','#475569',8);L(String(X),52,89,18,X?'#fff':'#334155','center',1);L('X',20,88,16,'#1f2733','center',1);
wire([[72,88],[134,88]],X);
// feedback Q to XOR
wire([[430,85],[430,180],[110,180],[110,112],[134,112]],Q);ci(430,85,4,col(Q));
xorG(140,100);
wire([[202,100],[250,100],[250,85],[290,85]],D);L('D = '+D,208,84,12,'#1f2733','left',1);
// clock source
rc(205,120,50,30,'#eff6ff','#2563eb',6);C.strokeStyle='#2563eb';C.lineWidth=2;C.beginPath();C.moveTo(211,142);C.lineTo(219,142);C.lineTo(219,128);C.lineTo(230,128);C.lineTo(230,142);C.lineTo(241,142);C.lineTo(241,128);C.lineTo(249,128);C.stroke();
wire([[255,135],[290,135]],K);
// flip flop
if(fl>0){C.globalAlpha=0.35*fl;rc(282,52,116,116,'#fde047',null,12);C.globalAlpha=1;}
rc(290,60,100,100,'#fff','#1e3a8a',8);C.lineWidth=2.5;C.strokeStyle='#1e3a8a';C.stroke();
L('D FLIP FLOP',340,112,12,'#1e3a8a','center',1);L('D',300,85,13,'#1f2733','left',1);L('Q',380,85,13,'#1f2733','right',1);
C.strokeStyle='#1e3a8a';C.lineWidth=2;C.beginPath();C.moveTo(290,126);C.lineTo(302,135);C.lineTo(290,144);C.stroke();L('CLK',306,135,11,'#1f2733','left');
L('stored Q = '+Q,340,150,12,'#334155','center',1);
wire([[390,85],[469,85]],Q);
ci(485,85,16,Q?'#facc15':'#e5e7eb','#475569',2);if(Q){C.globalAlpha=.3;ci(485,85,25,'#fde047');C.globalAlpha=1;}L(String(Q),485,86,14,'#1f2733','center',1);
L('Q',514,85,15,'#1f2733','left',1);
L('feedback: Q returns as secondary input',270,191,11,'#475569','center');
// rule panel
L('D = X ⊕ Q',540,118,13,'#1e3a8a','left',1);L('X = 1: Q toggles',540,138,12,'#334155','left');L('X = 0: Q holds',540,156,12,'#334155','left');
if(fl>0){rc(536,40,96,22,'rgba(253,224,71,'+(0.4+0.6*fl)+')',null,6);L('Edge: Q takes D',584,51,11,'#1f2733','center',1);}
// timing diagram
var x0=70,s=114.5,rows=[['CLK',clk,218,'#2563eb'],['X',xin,252,'#16a34a'],['D',function(t){return xin(t)^qv(t);},286,'#7c3aed'],['Q',qv,320,'#ea580c']];
rc(14,198,618,146,'#f8fafc','#cbd5e1',8);
for(var k=0;k<4;k++){var ex=x0+(E0+k*TP)*s;ln(ex,204,ex,338,'#cbd5e1',1,[4,4]);}
for(var r=0;r<4;r++){L(rows[r][0],28,rows[r][2],13,'#1f2733','left',1);trace(rows[r][1],rows[r][2],x0,s,rows[r][3]);}
var cx=x0+ph*s;ln(cx,202,cx,340,'#dc2626',2);
for(var r=0;r<4;r++){var v=rows[r][1](ph);ci(cx,rows[r][2]+(v?-11:11),4,'#dc2626');}
mk(1,52,56);mk(2,171,58);mk(3,340,44);mk(4,268,154);mk(5,110,146);mk(6,485,54);
}
