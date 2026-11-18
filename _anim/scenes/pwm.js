var PER=4.8,ph=0,D=0.5,sc=0,ang=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;D=0.5-0.4*Math.cos(2*Math.PI*u);sc+=dt;ang+=dt*D*13.963;}
function draw(){
L('Switching frequency shown slowed down',20,22,11,'#5b6576','left');
var x0=60,x1=420,y0=200,y1=80,per=72;
// axes
ln(x0,y0,x1,y0,'#94a3b8',1.5);ln(x0,y0+10,x0,y1-20,'#94a3b8',1.5);
L('12 V',x0-8,y1,12,'#334155','right');L('0 V',x0-8,y0,12,'#334155','right');
// waveform scrolling
var off=(sc*45)%per;C.strokeStyle='#2563eb';C.lineWidth=3;C.beginPath();
var first=true;
for(var s=-per;s<x1-x0+per;s+=per){var xa=x0+s-off,xb=xa+per*D,xc=xa+per;
var pts=[[xa,y0],[xa,y1],[xb,y1],[xb,y0],[xc,y0]];
for(var i=0;i<pts.length;i++){var px=clamp(pts[i][0],x0,x1);if(first){C.moveTo(px,pts[i][1]);first=false;}else C.lineTo(px,pts[i][1]);}}
C.stroke();
// average line
var ya=y0-(y0-y1)*D;ln(x0,ya,x1,ya,'#ea580c',2.5,[8,5]);rc(x0+6,ya-26,118,20,'rgba(255,255,255,0.9)',null,4);L('Average '+m(12*D,1)+' V',x0+10,ya-16,13,'#ea580c','left',1);
// ON time and period brackets on a fixed cycle
var bx=x0+150;ln(bx,y1-30,bx+per*D,y1-30,'#16a34a',2);ln(bx,y1-36,bx,y1-24,'#16a34a',2);ln(bx+per*D,y1-36,bx+per*D,y1-24,'#16a34a',2);L('Ton',bx+per*D+8,y1-30,12,'#16a34a','left',1);
ln(bx,y0+26,bx+per,y0+26,'#475569',2);ln(bx,y0+20,bx,y0+32,'#475569',2);ln(bx+per,y0+20,bx+per,y0+32,'#475569',2);L('Period T',bx+per/2,y0+42,12,'#475569','center',1);
// duty bar
rc(60,290,360,24,'#e2e8f0',null,12);rc(60,290,360*D,24,'#2563eb',null,12);
L('Duty cycle D = Ton / T = '+m(D*100,0)+' %',240,333,15,'#1f2733','center',1);
// LED
var br=D;C.globalAlpha=0.15+0.5*br;ci(530,110,26+10*br,'#fde047');C.globalAlpha=1;ci(530,110,22,'rgb('+Math.round(150+105*br)+','+Math.round(120+100*br)+',20)','#92400e',2);
L('LED brightness',530,160,12,'#334155');
// motor with fan
var cx=530,cy=260;ci(cx,cy,40,'#e2e8f0','#475569',2);
for(var k=0;k<3;k++){var a=ang+k*2*Math.PI/3;C.fillStyle='#64748b';C.beginPath();C.ellipse(cx+20*Math.cos(a),cy+20*Math.sin(a),17,7,a,0,2*Math.PI);C.fill();}
ci(cx,cy,6,'#1f2937');L('Motor speed '+m(D*100,0)+' %',cx,cy+56,12,'#334155');
mk(1,x0+300,y1-30);mk(2,bx-14,y1-30);mk(3,bx-14,y0+26);mk(4,x1-14,ya-14);mk(5,582,95);mk(6,585,230);
}
