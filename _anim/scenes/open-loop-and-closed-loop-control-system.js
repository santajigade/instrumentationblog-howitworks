var PER=4.8,ph=0,u=0,dist=0,To=60,Tc=60,Ho=50,Hc=50;
function upd(){}
function g(u){if(u<0.2)return 0;if(u<0.35)return sm((u-0.2)/0.15);if(u<0.62)return 1;if(u<0.8)return 1-sm((u-0.62)/0.18);return 0;}
function bump(x){return x>0?x*Math.exp(1-x):0;}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;dist=g(u);To=60-14*dist;
var e1=bump((u-0.2)/0.04),e2=bump((u-0.62)/0.04);Tc=60-4*e1+4*e2;Hc=50+30*dist+8*e1-8*e2;Hc=clamp(Hc,0,100);}
function box(x,y,w,h,t1,t2,f,s){rc(x,y,w,h,f,s,8);L(t1,x+w/2,y+(t2?h/2-8:h/2),12,'#1f2733','center',1);if(t2)L(t2,x+w/2,y+h/2+9,11,'#334155','center');}
function flow(pts,col,on){if(!on)return;C.strokeStyle=col;C.lineWidth=3;C.setLineDash([5,7]);C.lineDashOffset=-ph*25;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
function tank(x,y,T,H){rc(x,y,90,56,'#e0f2fe','#0284c7',6);var hot=clamp((T-40)/25,0,1);rc(x+4,y+18,82,34,'rgb('+Math.round(96+150*hot)+','+Math.round(165-30*hot)+','+Math.round(250-170*hot)+')',null,4);
C.globalAlpha=H/100;for(var k=0;k<4;k++){var hx=x+16+k*19;ln(hx,y+50,hx,y+44-6*Math.abs(Math.sin(2*Math.PI*(2*u)+k)),'#ef4444',3);}C.globalAlpha=1;L('Tank',x+45,y+10,11,'#0c4a6e','center',1);}
function gauge(x,y,T){rc(x,y,72,56,'#fff','#94a3b8',6);L(m(T,1)+' °C',x+36,y+22,14,Math.abs(T-60)>3?'#dc2626':'#16a34a','center',1);L('SP 60 °C',x+36,y+42,11,'#5b6576','center');}
function draw(){
L('Same heating process and same cold inflow disturbance in both loops; times slowed',20,22,11,'#5b6576','left');
// disturbance indicator
var dx=430;C.globalAlpha=0.25+0.75*dist;ar(dx,44,dx,60,'#2563eb',3);ar(dx,206,dx,222,'#2563eb',3);C.globalAlpha=1;
L(dist>0.05?'Cold inflow ON':'Cold inflow OFF',dx+50,46,11,dist>0.05?'#2563eb':'#5b6576','left',1);
// OPEN LOOP row
L('OPEN LOOP: no feedback',20,46,13,'#b45309','left',1);
var y=70;box(20,y,86,52,'Setpoint','60 °C','#f6f8fc','#94a3b8');box(140,y,96,52,'Controller','fixed output','#fef3c7','#d97706');box(270,y,90,52,'Heater',m(Ho,0)+' %','#fee2e2','#dc2626');
ar(106,y+26,138,y+26,'#334155',2);ar(236,y+26,268,y+26,'#334155',2);ar(360,y+26,383,y+26,'#334155',2);
tank(385,y-2,To,Ho);ar(475,y+26,500,y+26,'#334155',2);gauge(502,y-2,To);
flow([[106,y+26],[138,y+26]],'#f59e0b',1);flow([[236,y+26],[268,y+26]],'#f59e0b',1);
L('Output drifts away and is never corrected',300,y+72,12,'#b45309','center');
// CLOSED LOOP row
L('CLOSED LOOP: sensor feedback corrects the error',20,196,13,'#15803d','left',1);
var y2=230;box(20,y2,86,52,'Setpoint','60 °C','#f6f8fc','#94a3b8');box(140,y2,96,52,'Controller','PID','#dcfce7','#16a34a');box(270,y2,90,52,'Heater',m(Hc,0)+' %','#fee2e2','#dc2626');
ar(106,y2+26,138,y2+26,'#334155',2);ar(236,y2+26,268,y2+26,'#334155',2);ar(360,y2+26,383,y2+26,'#334155',2);
tank(385,y2-2,Tc,Hc);ar(475,y2+26,500,y2+26,'#334155',2);gauge(502,y2-2,Tc);
// sensor and feedback
rc(588,y2+6,36,40,'#ede9fe','#7c3aed',6);L('TT',606,y2+26,12,'#5b21b6','center',1);ln(574,y2+26,588,y2+26,'#7c3aed',2);
ln(606,y2+46,606,338,'#7c3aed',2);ln(606,338,188,338,'#7c3aed',2);ar(188,338,188,y2+54,'#7c3aed',2);
flow([[606,y2+46],[606,338],[188,338],[188,y2+54]],'#a78bfa',1);
L('Feedback: measured temperature',400,322,11,'#5b21b6','center',1);
flow([[106,y2+26],[138,y2+26]],'#f59e0b',1);flow([[236,y2+26],[268,y2+26]],'#f59e0b',1);
mk(1,20,y2-6);mk(2,236,y2-6);mk(3,360,y2-6);mk(4,475,y2-6);mk(5,606,214);mk(6,250,338);
}
