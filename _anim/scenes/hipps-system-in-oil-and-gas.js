var PER=4.8,ph=0;
function Pd(t){if(t<1.0)return 60;if(t<2.1)return 60+30*(t-1.0);if(t<2.4){var a=t-2.1;return 93+30*(a-a*a/0.6);}if(t<3.6)return 97.5;if(t<4.4)return 97.5-37.5*sm((t-3.6)/0.8);return 60;}
function Vf(t){if(t<2.1)return 1;if(t<2.4)return 1-(t-2.1)/0.3;if(t<3.9)return 0;if(t<4.3)return (t-3.9)/0.4;return 1;}
function Of(t){if(t<1.0)return 1;if(t<1.1)return 1-(t-1.0)/0.1;if(t<3.6)return 0;if(t<3.7)return (t-3.6)/0.1;return 1;}
function v1(t){return 70*Vf(t)*(Of(t)>0.5?1:0.35);}
function v2(t){return 70*Of(t)*Math.max(Vf(t),0.4);}
function lat(fn){var N=960,c=[0],s=0;for(var i=1;i<=N;i++){var t=(i-0.5)*PER/N;s+=fn(t)*PER/N;c.push(s);}var k=Math.max(1,Math.round(s/26));return{c:c,sp:s/k};}
function lv(o,t){var N=960,f=t/PER*N,i=Math.floor(f);if(i>=N)i=N-1;if(i<0)i=0;return o.c[i]+(o.c[i+1]-o.c[i])*(f-i);}
var LA=lat(v1),LB=lat(v2);
function tripped(t){return t>=2.013&&t<3.85;}
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function pcol(p){var u=clamp((p-60)/38,0,1);return 'rgb('+Math.round(191+(254-191)*u)+','+Math.round(219-(219-202)*u)+','+Math.round(254-(254-202)*u)+')';}
function dots(o,x0,x1,cy,gap){var sp=o.sp,off=lv(o,ph)%sp;C.fillStyle='#1e63b8';for(var r=0;r<2;r++){var sh=r?sp/2:0;for(var x=x0+((off+sh)%sp);x<x1;x+=sp){if(gap&&x>gap[0]&&x<gap[1])continue;C.fillRect(x-2,cy+(r?7:-7)-2,4,4);}}}
function valve(x,cy,f,lab){var h=16;C.fillStyle=f>0.5?'#e2e8f0':'#fecaca';C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(x-16,cy-h);C.lineTo(x+16,cy+h);C.lineTo(x+16,cy-h);C.lineTo(x-16,cy+h);C.closePath();C.fill();C.stroke();
ln(x,cy,x,cy-38,'#334155',3);rc(x-16,cy-58,32,20,'#475569',null,4);var g=(1-f)*28;rc(x-3,cy-15+0,6,g,'#991b1b');}
function draw(){
var t=ph,p=Pd(t),vf=Vf(t),of=Of(t),tr=tripped(t);
L('Trip and reset compressed into one 4.8 s cycle',20,22,11,'#5b6576','left');
var cy=200,R=14;
// source
rc(20,168,62,64,'#475569',null,8);L('HP',51,190,13,'#fff','center',1);L('source',51,208,11,'#fff','center');
// upstream pipe, heavier wall
var pu=vf<0.05?150:p;rc(82,cy-R-8,178,8,'#64748b');rc(82,cy+R,178,8,'#64748b');rc(82,cy-R,178,2*R,vf<0.05?'#fecaca':pcol(p));
// downstream low rated section
rc(260,cy-R-5,360,5,'#9aa5b8');rc(260,cy+R,360,5,'#9aa5b8');rc(260,cy-R,300,2*R,pcol(p));rc(560,cy-R,60,2*R,'#dbeafe');
dots(LA,84,560,cy,[132,238]);dots(LB,576,620,cy);
valve(150,cy,vf);valve(220,cy,vf);
// outlet valve
var ox=560;C.fillStyle=of>0.5?'#e2e8f0':'#fde68a';C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(ox-12,cy-12);C.lineTo(ox+12,cy+12);C.lineTo(ox+12,cy-12);C.lineTo(ox-12,cy+12);C.closePath();C.fill();C.stroke();
ln(ox,cy-12,ox,cy-30,'#334155',2);ln(ox-10,cy-30,ox+10,cy-30,'#334155',3);
L(of>0.5?'Outlet open':'Outlet blocked',618,cy-44,11,of>0.5?'#334155':'#b45309','right',1);
ar(588,cy,616,cy,'#334155',2);
L('Protected low rated section, 100 bar',410,cy+32,11,'#334155','center',1);
L('HIPPS valves',185,cy+32,11,'#334155','center',1);
// transmitters
var rd=[p,p-0.4,p-9],nm=['PT A','PT B','PT C'],px=[320,390,460],votes=0;
for(var k=0;k<3;k++){var v=rd[k]>=90;if(v)votes++;ln(px[k],cy-R-5,px[k],147,'#334155',2);ln(px[k],113,px[k],92,'#7c3aed',1.5,[4,3]);ci(px[k],130,17,v?'#fecaca':'#fff','#334155',2);L(nm[k],px[k],130,11,'#1f2733','center',1);L(m(rd[k],1),px[k]+21,148,11,v?'#dc2626':'#334155','left',1);}
L('drifted',481,163,11,'#5b6576','left');
// logic solver
rc(290,40,200,52,tr?'#fee2e2':'#f1f5f9',tr?'#dc2626':'#334155',8);L('Logic solver, 2oo3 voting',390,56,12,'#1f2733','center',1);
L(tr?'Votes '+votes+' of 3: TRIP':'Votes '+votes+' of 3: normal',390,76,12,tr?'#dc2626':'#16a34a','center',1);
// trip signal to valves
var sc=tr?'#dc2626':'#94a3b8';C.strokeStyle=sc;C.lineWidth=2;C.setLineDash([6,6]);C.lineDashOffset=tr?-ph*40:0;C.beginPath();C.moveTo(290,66);C.lineTo(150,66);C.lineTo(150,142);C.moveTo(220,66);C.lineTo(220,142);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L(vf>0.99?'Open':vf<0.01?'Closed':(t<3?'Closing':'Opening'),185,105,11,vf>0.99?'#16a34a':'#dc2626','center',1);
// trend chart
var gx0=70,gx1=600,gy0=345,gy1=250;function X(tt){return gx0+(gx1-gx0)*tt/PER;}function Y(pp){return gy0-(gy0-gy1)*(pp-50)/55;}
rc(gx0-6,gy1-6,gx1-gx0+12,gy0-gy1+12,'#f8fafc','#dde3ee',6);
ln(gx0,Y(100),gx1,Y(100),'#dc2626',1.5);ln(gx0,Y(90),gx1,Y(90),'#ea580c',1.5,[6,4]);
L('Rating 100 bar',gx0+4,Y(100)-8,11,'#dc2626','left',1);L('Trip 90 bar',gx0+4,Y(90)-8,11,'#ea580c','left',1);
L('Pressure',gx0-10,gy0-28,11,'#334155','right');L('bar',gx0-10,gy0-14,11,'#334155','right');
C.strokeStyle='#1e63b8';C.lineWidth=2.5;C.beginPath();for(var i=0;i<=240;i++){var tt=i*PER/240,yy=Y(Pd(tt));if(i)C.lineTo(X(tt),yy);else C.moveTo(X(tt),yy);}C.stroke();
ln(X(t),gy1,X(t),gy0,'#334155',1.5);ci(X(t),Y(p),5,'#1e63b8','#fff',2);
L(m(p,1)+' bar',X(t)+(t>4?-10:10),p>85?Y(90)+12:Y(p)+14,11,'#1e3a8a',t>4?'right':'left',1);
mk(1,296,116);mk(2,508,48);mk(3,185,150);mk(4,528,232);mk(5,592,176);mk(6,622,300);
}
