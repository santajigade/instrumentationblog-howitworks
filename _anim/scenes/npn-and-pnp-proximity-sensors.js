var PER=4.8,ph=0,u=0,tx=0,on=false;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;tx=28*(0.5-0.5*Math.cos(2*Math.PI*u));on=tx>17;}
function flow(pts,col){C.strokeStyle=col;C.lineWidth=3;C.setLineDash([5,7]);C.lineDashOffset=-ph*25;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
function half(ox,pnp){
var BN='#8b5a2b',BK='#111827',BU='#2563eb';
L(pnp?'PNP (sourcing)':'NPN (sinking)',ox+20,46,14,pnp?'#b45309':'#0f766e','left',1);
// target
var x=ox+12+tx;rc(x,125,10,50,'#94a3b8','#475569',2);L('Metal',ox+28,190,11,'#334155','center');
// sensor body
rc(ox+50,135,90,30,'#cbd5e1','#64748b',4);rc(ox+50,135,9,30,'#f97316','#c2410c',2);
for(var k=0;k<6;k++)ln(ox+66+k*12,135,ox+66+k*12,165,'#94a3b8',1);
L(pnp?'PNP':'NPN',ox+100,150,12,'#1f2733','center',1);
ci(ox+128,129,5,on?'#facc15':'#e5e7eb','#a16207',1.5);
// field at face
C.globalAlpha=on?0.55:0.25;C.strokeStyle='#7c3aed';C.lineWidth=1.5;for(var k=1;k<=2;k++){C.beginPath();C.arc(ox+50,150,6+k*7,Math.PI/2,Math.PI*1.5);C.stroke();}C.globalAlpha=1;
// rails and supply
ln(ox+160,70,ox+300,70,'#dc2626',2.5);ln(ox+150,300,ox+300,300,'#1e3a8a',2.5);
L('+24 V',ox+262,60,12,'#dc2626','center',1);L('0 V',ox+262,314,12,'#1e3a8a','center',1);
ln(ox+300,70,ox+300,168,'#334155',2);ln(ox+300,208,ox+300,300,'#334155',2);
ln(ox+286,168,ox+314,168,'#334155',3);ln(ox+292,176,ox+308,176,'#334155',3);ln(ox+286,184,ox+314,184,'#334155',3);ln(ox+292,192,ox+308,192,'#334155',3);ln(ox+300,192,ox+300,208,'#334155',2);
// wires
ln(ox+140,143,ox+160,143,BN,3);ln(ox+160,143,ox+160,70,BN,3);
ln(ox+140,157,ox+150,157,BU,3);ln(ox+150,157,ox+150,300,BU,3);
ln(ox+140,150,ox+240,150,BK,3);
L('BN',ox+172,110,11,BN,'left',1);L('BU',ox+138,230,11,BU,'right',1);L('BK',ox+200,140,11,BK,'center',1);
// load
var ly=pnp?200:88,lh=pnp?50:44;
if(pnp){ln(ox+240,150,ox+240,ly,BK,3);ln(ox+240,ly+lh,ox+240,300,'#334155',2);}
else{ln(ox+240,70,ox+240,ly,'#334155',2);ln(ox+240,ly+lh,ox+240,150,BK,3);}
rc(ox+222,ly,36,lh,on?'#fef08a':'#f1f5f9','#475569',6);L('Load',ox+240,ly+lh/2,11,'#1f2733','center',1);
// current path when ON
if(on){
if(pnp)flow([[ox+300,70],[ox+160,70],[ox+160,143],[ox+140,143],[ox+140,150],[ox+240,150],[ox+240,300],[ox+300,300]],'#22c55e');
else flow([[ox+300,70],[ox+240,70],[ox+240,150],[ox+140,150],[ox+140,157],[ox+150,157],[ox+150,300],[ox+300,300]],'#22c55e');}
L(on?'Target detected: output ON':'No target: output OFF',ox+160,338,12,on?'#15803d':'#64748b','center',1);
}
function draw(){
L('Same inductive sensor, two output types; green dashes show conventional current',20,22,11,'#5b6576','left');
half(0,true);ln(320,40,320,345,'#e2e8f0',1.5);half(320,false);
mk(1,26,110);mk(2,66,116);mk(3,276,225);mk(4,596,111);mk(5,484,262);mk(6,594,188);
}
