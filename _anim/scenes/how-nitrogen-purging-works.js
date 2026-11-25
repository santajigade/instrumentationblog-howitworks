var PER=4.8,ph=0,SEG=[[150,150,470,150],[470,150,470,285],[470,285,560,285],[560,285,560,120]];
var LEN=[],TOT=0;for(var i=0;i<SEG.length;i++){var s=SEG[i],l=Math.hypot(s[2]-s[0],s[3]-s[1]);LEN.push(l);TOT+=l;}
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function pos(s){var d=s*TOT;for(var i=0;i<SEG.length;i++){if(d<=LEN[i]||i==SEG.length-1){var q=SEG[i],f=d/LEN[i];return[q[0]+(q[2]-q[0])*f,q[1]+(q[3]-q[1])*f];}d-=LEN[i];}}
function rnd(i){var x=Math.sin(i*91.7+3.3)*43758.5;return x-Math.floor(x);}
function draw(){
var front=Math.min(ph/3.0,1.05),reset=ph>4.3?sm((ph-4.3)/0.5):0,o2;
if(ph<2.9)o2=20.9;else o2=0.5+20.4*Math.exp(-(ph-2.9)/0.25);if(reset>0)o2=o2+(20.9-o2)*reset;
L('Displacement purge of a pipeline, time compressed; cycle restarts with air',20,22,11,'#5b6576','left');
// pipe body
C.lineCap='round';C.lineJoin='round';C.strokeStyle='#94a3b8';C.lineWidth=34;C.beginPath();C.moveTo(150,150);C.lineTo(470,150);C.lineTo(470,285);C.lineTo(560,285);C.lineTo(560,120);C.stroke();
C.strokeStyle='#f1f5f9';C.lineWidth=26;C.stroke();C.lineCap='butt';C.lineJoin='miter';
// particles: plug flow, front at s = front
var v=1/3.0;for(var i=0;i<90;i++){var s0=i/90,s=(s0+v*ph)%1,p=pos(s),j=rnd(i),off=(j-0.5)*16;
var isN=s<front-0.06*rnd(i+7);if(reset>0&&rnd(i+3)<reset)isN=false;
var px=p[0],py=p[1];if(s*TOT<LEN[0]||(s*TOT>LEN[0]+LEN[1]&&s*TOT<LEN[0]+LEN[1]+LEN[2]))py+=off;else px+=off;
if(isN)ci(px,py,4,'#16a34a');else{var w=rnd(i+20);ci(px,py,4,w<0.21?'#dc2626':(w<0.27?'#0ea5e9':'#94a3b8'));}}
// cylinder, regulator, valve
rc(40,110,56,200,'#16a34a','#14532d',14);rc(56,92,24,20,'#475569',null,3);L('N2',68,210,18,'#fff','center',1);
ln(68,92,68,74,'#475569',5);ln(68,74,118,74,'#475569',5);ln(118,74,118,150,'#475569',5);ln(118,150,134,150,'#475569',5);
ci(98,74,12,'#fff','#334155',2);var na=-2.4+1.6;ln(98,74,98+8*Math.cos(na),74+8*Math.sin(na),'#dc2626',2);
C.fillStyle='#1f2733';C.beginPath();C.moveTo(108,140);C.lineTo(128,150);C.lineTo(108,160);C.closePath();C.fill();C.beginPath();C.moveTo(128,140);C.lineTo(108,150);C.lineTo(128,160);C.closePath();C.fill();
L('Inlet valve open',104,186,11,'#334155','left');
// vent and arrow out
for(var k=0;k<3;k++){var yy=110-((ph*40+k*14)%42);C.globalAlpha=0.5;ar(560,112,560+(k-1)*14,yy-10,'#64748b',1.6);}C.globalAlpha=1;
L('Vent',528,110,12,'#334155','right',1);
// O2 analyzer
var ax=330,ay=38;rc(ax,ay,180,58,'#0f172a',null,8);L('O2 at vent',ax+10,ay+16,11,'#cbd5e1','left',1);L(o2.toFixed(1)+' %',ax+170,ay+38,20,o2<5?'#4ade80':'#fbbf24','right',1);
rc(ax+10,ay+30,70,10,'#334155');rc(ax+10,ay+30,70*o2/20.9,10,o2<5?'#4ade80':'#fbbf24');
ln(560,124,600,124,'#0f172a',1.5,[3,3]);ln(600,124,600,67,'#0f172a',1.5,[3,3]);ln(600,67,ax+180,67,'#0f172a',1.5,[3,3]);
// legend + status
var ly=318;ci(160,ly,5,'#16a34a');L('Nitrogen',170,ly,12,'#1f2733','left');ci(250,ly,5,'#dc2626');L('Oxygen',260,ly,12,'#1f2733','left');ci(330,ly,5,'#0ea5e9');L('Moisture',340,ly,12,'#1f2733','left');ci(420,ly,5,'#94a3b8');L('Other air gases',430,ly,12,'#1f2733','left');
var st=ph<2.9?'Nitrogen front pushes air toward the vent':(reset>0?'Loop restarts with air in the line':'Oxygen low: line is inert and dry');
L(st,300,210,13,ph<2.9?'#1e3a8a':'#166534','center',1);
var fp=pos(Math.min(front,1));if(ph<2.9)ln(fp[0],fp[1]-18,fp[0],fp[1]+18,'#14532d',2,[3,3]);
mk(1,30,100);mk(2,98,52);mk(3,118,124);mk(4,300,124);mk(5,540,140);mk(6,ax+180,44);
}
