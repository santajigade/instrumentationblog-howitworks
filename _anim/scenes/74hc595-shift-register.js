var PER=4.8,ph=0,B=[1,0,1,1,0,0,1,0];
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function X(i){return 220+i*48;}
function tx(t){return 110+t*490/4.8;}
function clk(){var c=0;for(var k=0;k<8;k++)c+=sm((ph-(k*0.4+0.2))/0.15);return c;}
function hi(s,t){if(s==0){var j=Math.floor(t/0.4);return t<3.2?B[j]:0;}if(s==1){var u=t%0.4;return t<3.2&&u>=0.2&&u<0.3?1:0;}if(s==2)return (t>=3.4&&t<3.5)||(t>=4.6&&t<4.7)?1:0;return t>=4.2&&t<4.5?0:1;}
function draw(){
L('Clock slowed down; first bit sent ends on QH, last bit on QA',20,22,11,'#5b6576','left');
var clr=ph>=4.2,lat=ph>=3.4&&ph<4.6,c=clk();
rc(140,40,470,156,'#f8fafc','#334155',10);
L('74HC595',146,182,12,'#1e3a8a','left',1);
var ne=0;for(var k=0;k<8;k++)if(ph>=k*0.4+0.2)ne++;var st=ph<3.2?(ph%0.4<0.2?'Bit '+(Math.floor(ph/0.4)+1)+' placed on SER':'SRCLK edge '+ne+' of 8: bits shift one stage'):ph<3.4?'Byte loaded, outputs not changed yet':ph<4.2?'RCLK: byte copied to outputs':ph<4.6?'SRCLR low: shift register cleared':'Next RCLK: zeros copied to outputs';
L(st,598,54,12,'#2563eb','right',1);
L('Shift register',196,68,11,'#5b6576','left');L('Output latch',196,124,11,'#5b6576','left');
// SER pin
L('SER',24,91,13,'#1f2733','left',1);ln(56,91,196,91,'#334155',2);
for(var i=0;i<8;i++){rc(X(i)-20,76,40,30,'#fff','#64748b',5);
var q=lat?B[7-i]:0;rc(X(i)-20,134,40,30,q?'#fef3c7':'#fff',q?'#d97706':'#64748b',5);L(String(q),X(i),150,14,'#1f2733','center',1);
L('Q'+'ABCDEFGH'[i],X(i),174,11,'#1f2733','center',1);
ln(X(i),196,X(i),210,'#334155',2);if(q){C.globalAlpha=.35;ci(X(i),221,15,'#fde047');C.globalAlpha=1;}ci(X(i),221,9,q?'#facc15':'#e5e7eb','#475569',1.5);
if(ph>=3.4&&ph<3.6)ar(X(i),108,X(i),132,'#ea580c',2);}
L('LEDs',196,221,11,'#5b6576','right');
// bit tokens
if(!(ph>=4.5)){C.globalAlpha=clr?clamp(1-(ph-4.2)/0.3,0,1):1;
for(var j=0;j<8;j++){if(ph<j*0.4)continue;var p=c-j-1,x=X(0)+p*48,v=B[j];ci(x,91,12,v?'#16a34a':'#cbd5e1','#334155',1.5);L(String(v),x,92,13,v?'#fff':'#1f2733','center',1);}
C.globalAlpha=1;}
// timing
var nm=['SER','SRCLK','RCLK','SRCLR'],ys=[258,282,306,330];
for(var s=0;s<4;s++){var y=ys[s];L(nm[s],24,y,12,'#1f2733','left',1);C.strokeStyle=s==2?'#ea580c':s==1?'#2563eb':'#334155';C.lineWidth=2;C.beginPath();
for(var t=0;t<=4.8001;t+=0.01){var yy=hi(s,Math.min(t,4.799))?y-7:y+7;if(t==0)C.moveTo(tx(t),yy);else C.lineTo(tx(t),yy);}C.stroke();}
ln(tx(ph),246,tx(ph),340,'#ef4444',1.5,[4,3]);
mk(1,80,72);mk(2,590,91);mk(3,590,149);mk(4,596,221);mk(5,88,282);mk(6,88,306);
}
