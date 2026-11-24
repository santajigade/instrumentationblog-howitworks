var PER=4.8,ph=0,rot=0;
function upd(){}
function Vt(t){if(t<1)return 100;if(t<3.4)return 100-12*Math.exp(-(t-1)/0.45);return 100+6*Math.exp(-(t-3.4)/0.3);}
function If(t){if(t<1)return 1;if(t<3.4){var a=(t-1)/0.4;return 1.6+0.9*a*Math.exp(1-a)-0.6*Math.exp(-(t-1)/0.15);}var b=(t-3.4)/0.3;return 1+0.6*Math.exp(-b)-0.4*b*Math.exp(1-b);}
function step(dt){ph=(ph+dt)%PER;rot=2*Math.PI*4*ph/PER;}
function draw(){
L('Simplified response; times and values illustrative, slowed down',20,22,11,'#5b6576','left');
var v=Vt(ph),fi=If(ph),on=ph>=1&&ph<3.4;
// generator
var gx=110,gy=135;ci(gx,gy,62,'#e2e8f0','#475569',3);ci(gx,gy,44,'#fff','#94a3b8',1.5);
C.save();C.translate(gx,gy);C.rotate(rot);rc(-38,-14,76,28,'#cbd5e1','#475569',6);
var g=clamp((fi-0.6)/1.8,0,1);C.fillStyle='rgba(234,88,12,'+(0.25+0.7*g)+')';C.fillRect(-30,-9,60,18);
L('N',-24,0,11,'#1f2937','center',1);L('S',24,0,11,'#1f2937','center',1);C.restore();
L('Generator',gx,gy+76,12,'#1f2733','center',1);
// bus
ln(gx+62,gy,300,gy,'#1f2937',3);L('Terminal '+m(v*4.15,0)+' V',240,gy-14,12,'#1f2733','center',1);
// load lamp
ln(205,gy,205,gy+30,'#1f2937',2);var br=clamp((v-80)/20,0,1.1);C.globalAlpha=0.2+0.6*br;ci(205,gy+44,20,'#fde047');C.globalAlpha=1;ci(205,gy+44,12,'rgb(250,'+Math.round(150+80*br)+',40)','#92400e',2);
// motor with switch
ln(285,gy,285,gy+18,'#1f2937',2);
if(on)ln(285,gy+18,285,gy+40,'#16a34a',3);else ln(285,gy+18,300,gy+36,'#dc2626',3);
ci(285,gy+68,22,'#e0f2fe','#0369a1',2);L('M',285,gy+68,14,'#0c4a6e','center',1);
L(on?'Motor started':'Motor off',285,gy+104,11,on?'#16a34a':'#475569','center',1);
// PT and AVR
ln(180,gy,180,250,'#7c3aed',2,[5,4]);rc(30,250,160,58,'#ede9fe','#6d28d9',8);L('AVR',110,268,14,'#4c1d95','center',1);L('set point 415 V',110,290,11,'#4c1d95','center');
L('PT sense',186,226,11,'#6d28d9','left',1);
ar(40,250,62,gy+48,'#ea580c',2.5);L('Field current',60,236,11,'#c2410c','left',1);
L('If '+m(fi,2)+' pu',110,325,12,'#c2410c','center',1);
// chart
var x0=362,x1=626;
rc(x0,55,x1-x0,120,'#f8fafc','#e2e8f0',6);rc(x0,190,x1-x0,120,'#fff7ed','#fed7aa',6);
L('Terminal voltage %',x0,45,12,'#1e3a8a','left',1);L('Field current pu',x0,182,12,'#9a3412','left',1);
function VY(x){return 110-(x-100)*3.5;}function IY(x){return 300-(x-0.6)*54;}
ln(x0,VY(100),x1,VY(100),'#94a3b8',1,[4,4]);L('100',x0-4,VY(100),11,'#475569','right');L('88',x0-4,VY(88),11,'#475569','right');
L('1.0',x0-4,IY(1),11,'#475569','right');L('2.0',x0-4,IY(2),11,'#475569','right');
C.lineWidth=2.5;C.strokeStyle='#1d4ed8';C.beginPath();for(var i=0;i<=264;i++){var t=i/264*PER,y=VY(Vt(t));if(i==0)C.moveTo(x0+i,y);else C.lineTo(x0+i,y);}C.stroke();
C.strokeStyle='#ea580c';C.beginPath();for(var i=0;i<=264;i++){var t=i/264*PER,y=IY(If(t));if(i==0)C.moveTo(x0+i,y);else C.lineTo(x0+i,y);}C.stroke();
var cx=x0+ph/PER*264;ln(cx,56,cx,174,'#334155',1.5);ln(cx,191,cx,309,'#334155',1.5);ci(cx,VY(v),5,'#1d4ed8');ci(cx,IY(fi),5,'#ea580c');
L('Motor starts',x0+55,322,11,'#475569','center');L('Motor stops',x0+187,322,11,'#475569','center');
mk(1,gx,gy-30);mk(2,166,228);mk(3,205,280);mk(4,318,gy+68);mk(5,x0+80,150);mk(6,x0+110,205);
}
