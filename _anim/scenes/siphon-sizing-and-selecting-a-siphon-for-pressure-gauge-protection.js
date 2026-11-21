var PER=4.8,ph=0;
var RX=150,DX=230,UX=310,TY=110,BY=230,RB=40,GY=82,MY=320;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function tcol(u){u=clamp(u,0,1);return 'rgb('+Math.round(220-(220-59)*u)+','+Math.round(38+(130-38)*u)+','+Math.round(38+(246-38)*u)+')';}
function tube(path,col,w){C.strokeStyle=col;C.lineWidth=w;C.lineCap='round';C.lineJoin='round';C.beginPath();path();C.stroke();C.lineCap='butt';}
function draw(){
var u=ph/PER,yi=170+5*Math.sin(2*Math.PI*u*2),pg=10+0.25*Math.sin(2*Math.PI*u*2);
L('Steam motion and condensation slowed down; pulsation exaggerated',20,22,11,'#5b6576','left');
// steam main
rc(20,MY-24,600,8,'#9aa5b8');rc(20,MY+16,600,8,'#9aa5b8');rc(20,MY-16,600,32,'#fde2e2');
for(var k=0;k<14;k++){var x=20+((k*48+ph*140)%672);if(x>616)continue;C.globalAlpha=0.55;ci(x,MY+(k%2?6:-5),7+(k%3)*2,'#fff');C.globalAlpha=1;}
ar(470,MY,530,MY,'#991b1b',2);L('Steam main',560,MY,11,'#991b1b','left',1);
L('Hot steam 250 °C',30,MY-36,12,'#b91c1c','left',1);
// siphon wall (temperature coloured)
var segs=[[function(){C.moveTo(RX,MY-24);C.lineTo(RX,TY);},0.05],[function(){C.arc((RX+DX)/2,TY,RB,Math.PI,2*Math.PI);},0.25],[function(){C.moveTo(DX,TY);C.lineTo(DX,BY);},0.45],[function(){C.arc((DX+UX)/2,BY,RB,Math.PI,0,true);},0.65],[function(){C.moveTo(UX,BY);C.lineTo(UX,GY+38);},0.85]];
for(var i=0;i<segs.length;i++)tube(segs[i][0],tcol(segs[i][1]),20);
// inside: steam part
var st='#fecaca',wa='#93c5fd';
tube(function(){C.moveTo(RX,MY-16);C.lineTo(RX,TY);C.arc((RX+DX)/2,TY,RB,Math.PI,2*Math.PI);C.lineTo(DX,yi);},st,11);
// water part
tube(function(){C.moveTo(DX,yi);C.lineTo(DX,BY);C.arc((DX+UX)/2,BY,RB,Math.PI,0,true);C.lineTo(UX,GY+36);},wa,11);
// water surface line
ln(DX-6,yi,DX+6,yi,'#1d4ed8',2);
// steam puffs rising along riser and over the bend
var Lr=(MY-16-TY),La=Math.PI*RB,Ld=yi-TY,Ltot=Lr+La+Ld;
for(var k=0;k<6;k++){var s=((ph/1.6+k/6)%1)*Ltot,x,y;if(s<Lr){x=RX;y=MY-16-s;}else if(s<Lr+La){var a=Math.PI+(s-Lr)/RB;x=(RX+DX)/2+RB*Math.cos(a);y=TY+RB*Math.sin(a);}else{x=DX;y=TY+(s-Lr-La);}
C.globalAlpha=1-0.7*s/Ltot;ci(x,y,3.5,'#fff','#ef4444',1);C.globalAlpha=1;}
// condensate droplets running down to the surface
for(var k=0;k<3;k++){var f=(ph/1.2+k/3)%1,y=TY+4+f*(yi-TY-8);ci(DX+3,y,2.6,'#1d4ed8');}
// heat leaving the wall
for(var k=0;k<4;k++){var f=(ph/1.2+k/4)%1,c='rgba(234,88,12,'+(0.8*(1-f))+')';
var y0=255-k*45;C.strokeStyle=c;C.lineWidth=1.5;C.beginPath();for(var j=0;j<=10;j++){var xx=RX-16-f*30-j*2.2,yy=y0+3*Math.sin(j*1.3+f*6);if(j)C.lineTo(xx,yy);else C.moveTo(xx,yy);}C.stroke();}
for(var k=0;k<2;k++){var f=(ph/1.2+k/2+0.25)%1,c='rgba(234,88,12,'+(0.6*(1-f))+')';var y0=58-k*0;var x0=150+k*80;C.strokeStyle=c;C.lineWidth=1.5;C.beginPath();for(var j=0;j<=8;j++){var yy=TY-RB-14-f*14-j*0,xx=x0+20+j*2.5;yy+=3*Math.sin(j*1.4+f*6);if(j)C.lineTo(xx,yy);else C.moveTo(xx,yy);}C.stroke();}
L('Heat lost to air',110,187,11,'#c2410c','right',1);
L('Steam condenses',135,62,11,'#1f2733','right',1);L('on cool wall',135,78,11,'#1f2733','right',1);
L('Condensate',UX+18,BY-22,12,'#1d4ed8','left',1);L('seal fills the',UX+18,BY-6,11,'#1d4ed8','left');L('gauge side',UX+18,BY+8,11,'#1d4ed8','left');
// pressure pulses through water (chevrons pulse, water does not flow)
for(var k=0;k<3;k++){var a=0.25+0.6*Math.max(0,Math.sin(2*Math.PI*(u*2)-k*0.8));C.globalAlpha=a;C.strokeStyle='#1e3a8a';C.lineWidth=2;var yy=BY-40-k*24;C.beginPath();C.moveTo(UX-5,yy+4);C.lineTo(UX,yy-1);C.lineTo(UX+5,yy+4);C.stroke();}C.globalAlpha=1;
// gauge
ci(UX,GY,40,'#fff','#334155',3);for(var i=0;i<=8;i++){var a=Math.PI*0.75+i*Math.PI*1.5/8,r1=33,r2=i%2?29:26;ln(UX+r1*Math.cos(a),GY+r1*Math.sin(a),UX+r2*Math.cos(a),GY+r2*Math.sin(a),'#334155',1.5);}

var na=Math.PI*0.75+pg/16*Math.PI*1.5;ln(UX,GY,UX+28*Math.cos(na),GY+28*Math.sin(na),'#dc2626',2.5);ci(UX,GY,4,'#334155');
L(m(pg,1),UX,GY+15,11,'#1f2733','center',1);
L('Gauge stays cool',UX+52,GY-6,12,'#1f2733','left',1);L('reads about 10 bar',UX+52,GY+10,11,'#334155','left');
// temperature profile
var cx0=450,cx1=615,cy0=270,cy1=150;rc(cx0-10,cy1-30,cx1-cx0+20,cy0-cy1+56,'#f8fafc','#dde3ee',6);
L('Temperature along siphon',cx0,cy1-16,11,'#334155','left',1);
ln(cx0,cy0,cx1,cy0,'#94a3b8',1.5);ln(cx0,cy0,cx0,cy1,'#94a3b8',1.5);
C.strokeStyle='#ea580c';C.lineWidth=2.5;C.beginPath();for(var i=0;i<=40;i++){var q=i/40,T2=40+210*Math.exp(-3.2*q),x=cx0+q*(cx1-cx0),y=cy0-(T2/250)*(cy0-cy1);if(i)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
var q=(u*2)%1,T2=40+210*Math.exp(-3.2*q);ci(cx0+q*(cx1-cx0),cy0-(T2/250)*(cy0-cy1),4,'#ea580c','#fff',1.5);
L('250 °C',cx0+6,cy1+4,11,'#b91c1c','left',1);L('Process',cx0,cy0+12,11,'#334155','left');L('Gauge',cx1,cy0+12,11,'#334155','right');
mk(1,250,MY);mk(2,(RX+DX)/2,TY-RB-26);mk(3,270,yi);mk(4,(DX+UX)/2,BY+2);mk(5,UX-50,GY-30);
}
