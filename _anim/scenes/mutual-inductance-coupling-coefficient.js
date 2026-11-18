var PER=4.8,ph=0,u=0,i1=0,di=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;i1=Math.sin(2*Math.PI*u);di=Math.cos(2*Math.PI*u);}
function coil(x,y0,y1,col,cur){
for(var y=y0;y<=y1;y+=12){C.strokeStyle=col;C.lineWidth=4;C.beginPath();C.ellipse(x,y,22,5,0,0,Math.PI);C.stroke();}
C.globalAlpha=.35;for(var y=y0;y<=y1;y+=12){C.strokeStyle=col;C.lineWidth=3;C.beginPath();C.ellipse(x,y,22,5,0,Math.PI,2*Math.PI);C.stroke();}C.globalAlpha=1;}
function draw(){
L('One cycle of current shown slowed down; leakage flux not drawn',20,22,11,'#5b6576','left');
// core
rc(140,50,240,160,'#94a3b8','#64748b',4);rc(166,76,188,108,'#fff',null,2);
// mutual flux path in core, direction follows i1
var a=Math.abs(i1);C.globalAlpha=0.2+0.8*a;C.strokeStyle='#7c3aed';C.lineWidth=3;C.setLineDash([8,8]);C.lineDashOffset=(i1>=0?-1:1)*ph*40;
C.beginPath();C.rect(153,63,214,134);C.stroke();C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
L('Mutual flux path in core',260,130,12,'#6d28d9','center',1);
// coils
coil(153,86,176,'#b45309');coil(367,86,176,'#0f766e');
L('Coil 1  L1',153,226,12,'#b45309','center',1);L('Coil 2  L2',367,226,12,'#0f766e','center',1);
// primary circuit with AC source
ln(131,86,80,86,'#334155',2);ln(131,176,80,176,'#334155',2);ln(80,86,80,108,'#334155',2);ln(80,154,80,176,'#334155',2);
ci(80,131,22,'#fff','#334155',2);C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();for(var k=0;k<=20;k++){var x=70+k,y=131-7*Math.sin(k/20*2*Math.PI);if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
// current arrow on primary wire
var al=clamp(a*1.3,0,1);C.globalAlpha=al;if(i1>=0)ar(92,80,122,80,'#b45309',2.5);else ar(122,80,92,80,'#b45309',2.5);C.globalAlpha=1;
L('i1',107,70,12,'#b45309','center',1);
// secondary circuit with voltmeter
ln(389,86,450,86,'#334155',2);ln(389,176,450,176,'#334155',2);ln(450,86,450,104,'#334155',2);ln(450,158,450,176,'#334155',2);
ci(450,131,27,'#fff','#334155',2);var na=-Math.PI/2+di*0.9;ln(450,140,450+20*Math.cos(na),140+20*Math.sin(na),'#dc2626',2.5);ci(450,140,3,'#1f2937');L('V',450,121,11,'#334155','center',1);
L('v2',476,92,12,'#0f766e','left',1);
// formulas
rc(492,60,138,104,'#f6f8fc','#dde3ee',8);
L('v2 = M di1/dt',561,82,13,'#1f2733','center',1);L('M = k √(L1 L2)',561,106,13,'#1f2733','center',1);L('0 ≤ k ≤ 1',561,130,12,'#334155','center');L('k = 1 means all flux links',561,150,11,'#5b6576','center');
// graph
var gx=60,gw=560,gy=295,ga=36;ln(gx,gy,gx+gw,gy,'#cbd5e1',1.5);ln(gx,gy-ga-6,gx,gy+ga+6,'#cbd5e1',1.5);
C.lineWidth=2.5;C.strokeStyle='#b45309';C.beginPath();for(var k=0;k<=112;k++){var x=gx+k*5,y=gy-ga*Math.sin(2*Math.PI*k/112);if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
C.strokeStyle='#0f766e';C.beginPath();for(var k=0;k<=112;k++){var x=gx+k*5,y=gy-ga*0.8*Math.cos(2*Math.PI*k/112);if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
var cx=gx+gw*u;ln(cx,gy-ga-6,cx,gy+ga+6,'#475569',1.5,[4,4]);ci(cx,gy-ga*i1,5,'#b45309');ci(cx,gy-ga*0.8*di,5,'#0f766e');
L('i1 in coil 1',gx+6,250,12,'#b45309','left',1);L('v2 in coil 2 (largest when i1 changes fastest)',gx+100,250,12,'#0f766e','left',1);
mk(1,128,104);mk(2,80,170);mk(3,260,206);mk(4,392,104);mk(5,478,166);mk(6,38,262);
}
