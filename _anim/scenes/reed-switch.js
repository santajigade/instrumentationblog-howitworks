var PER=4.8,ph=0,mx=0,closed=false;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;mx=320+190*Math.cos(2*Math.PI*u);var d=Math.abs(mx-320);closed=d<70;}
function draw(){
L('Magnet moves along the switch; field shown simplified',20,22,11,'#5b6576','left');
var gy=150;
// field lines around magnet
var near=clamp(1-Math.abs(mx-320)/190,0,1);
C.globalAlpha=0.25+0.5*near;
for(var k=1;k<=3;k++){C.strokeStyle='#7c3aed';C.lineWidth=1.3;C.setLineDash([4,5]);C.lineDashOffset=-T*20;C.beginPath();C.ellipse(mx,gy+70,60+k*26,22+k*20,0,Math.PI,2*Math.PI);C.stroke();}
C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
// glass tube
rc(170,gy-28,300,56,'rgba(186,230,253,0.45)','#7dd3fc',28);
// lead wires
ln(70,gy,175,gy,'#64748b',4);ln(465,gy,570,gy,'#64748b',4);
// reeds
var bend=closed?7:0;
C.strokeStyle='#b45309';C.lineWidth=6;C.lineCap='round';
C.beginPath();C.moveTo(175,gy);C.lineTo(260,gy);C.quadraticCurveTo(300,gy,330,gy-9+bend);C.stroke();
C.beginPath();C.moveTo(465,gy);C.lineTo(380,gy);C.quadraticCurveTo(340,gy,312,gy+9-bend);C.stroke();
C.lineCap='butt';
if(closed){ci(321,gy,6,'rgba(250,204,21,0.9)');}
// magnet
var my=gy+70;rc(mx-55,my-16,55,32,'#dc2626','#991b1b');rc(mx,my-16,55,32,'#2563eb','#1e3a8a');
L('N',mx-27,my,15,'#fff','center',1);L('S',mx+27,my,15,'#fff','center',1);
ar(mx-75,my+32,mx-25,my+32,'#334155',2);ar(mx+75,my+32,mx+25,my+32,'#334155',2);
// circuit
var by=315;ln(70,gy,70,by,'#334155',2.5);ln(570,gy,570,by,'#334155',2.5);ln(70,by,250,by,'#334155',2.5);ln(390,by,570,by,'#334155',2.5);
if(closed){C.setLineDash([6,6]);C.lineDashOffset=-T*40;ln(70,by,250,by,'#16a34a',3,[6,6]);ln(390,by,570,by,'#16a34a',3,[6,6]);C.setLineDash([]);C.lineDashOffset=0;}
// battery
rc(250,by-22,40,44,'#1f2937',null,6);L('+',270,by-8,13,'#fff','center',1);L('24 V',270,by+9,11,'#fff');
// lamp
ci(360,by,22,closed?'#facc15':'#e5e7eb','#475569',2);if(closed){C.globalAlpha=.35;ci(360,by,36,'#fde047');C.globalAlpha=1;}
L(closed?'CLOSED':'OPEN',600,60,18,closed?'#16a34a':'#dc2626','right',1);
L(closed?'Lamp ON':'Lamp OFF',600,84,13,'#334155','right');
mk(1,190,gy-44);mk(2,240,gy-18);mk(3,321,gy-30);mk(4,mx,my-34);mk(5,360,by-38);mk(6,226,by);
}
