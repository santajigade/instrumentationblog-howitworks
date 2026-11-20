var PER=4.8,ph=0,SX=112,PXM=140,V=450;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function cx(ns){return 172+ns/25*420;}
function draw(){
var half=ph<2.4?0:1,u=ph%2.4,D=[1.5,3.0],d=D[half],dn=D[1-half];
var xt=SX+d*PXM;if(u>2.05){xt=SX+(d+(dn-d)*sm((u-2.05)/0.35))*PXM;}
var path=2*(xt-SX),el=u-0.1,s=el*V,fly=el>0&&s<path&&u<2.05,arr=el>0&&s>=path&&u<=2.05,tr=2*d/0.3;
var tns=fly?tr*s/path:(arr?tr:0);
L('Light speed slowed billions of times for viewing',20,22,11,'#5b6576','left');
// sensor module
rc(30,108,82,112,'#065f46','#064e3b',8);L('ToF',62,198,12,'#d1fae5','center',1);
rc(96,130,16,20,'#dc2626','#7f1d1d',3);rc(96,170,16,20,'#334155','#0f172a',3);
// paths
ln(SX,140,xt,140,'#fecaca',1.5,[3,5]);ln(xt,180,SX,180,'#fecaca',1.5,[3,5]);
// target
rc(xt,104,24,124,'#94a3b8','#475569',4);for(var k=0;k<5;k++)ln(xt+24,112+k*24,xt+32,104+k*24,'#64748b',1.5);
// pulse
if(fly){var px,py;if(s<path/2){px=SX+s;py=140;}else{px=xt-(s-path/2);py=180;}
C.globalAlpha=.35;rc(px-14,py-7,28,14,'#f87171',null,7);C.globalAlpha=1;rc(px-8,py-4,16,8,'#dc2626',null,4);
ar(px+(py==140?10:-10),py,px+(py==140?22:-22),py,'#dc2626',2);}
if(arr){var f=clamp(1-(el-path/V)/1.0,0,1);C.globalAlpha=0.2+0.6*f;ci(104,180,16,'#fca5a5');C.globalAlpha=1;}
// ruler
ln(SX,246,SX+3*PXM,246,'#475569',1.5);for(var r=0;r<=3;r++){var rx=SX+r*PXM;ln(rx,241,rx,251,'#475569',1.5);L(r+' m',rx,259,11,'#5b6576');}
ar(SX+4,234,xt-4,234,'#2563eb',1.5);ar(xt-4,234,SX+4,234,'#2563eb',1.5);
// readout
rc(330,30,296,54,'#f8fafc','#cbd5e1',8);
L('Round trip time t = '+m(tns,1)+' ns',342,47,13,'#1f2733','left',1);
L(arr?'d = c × t ÷ 2 = '+m(d,2)+' m':'d = c × t ÷ 2, c = 3 × 10⁸ m/s',342,68,13,arr?'#16a34a':'#334155','left',arr);
// timing chart
rc(126,272,500,72,'#f8fafc','#e2e8f0',8);L('Tx',150,288,12,'#dc2626','center',1);L('Rx',150,318,12,'#334155','center',1);
ln(170,296,616,296,'#94a3b8',1.5);ln(170,326,616,326,'#94a3b8',1.5);
rc(cx(0),282,7,14,'#dc2626');
if(arr)rc(cx(tr),312,7,14,'#334155');
for(var n=0;n<=25;n+=5)L(n+' ns',cx(n),337,11,'#5b6576');
if(fly||arr){var cc=cx(tns);ln(cc,278,cc,330,'#d9622b',2);}
mk(1,82,132);mk(2,82,172);mk(3,210,124);mk(4,xt+12,98);mk(5,612,57);mk(6,138,346);
}
