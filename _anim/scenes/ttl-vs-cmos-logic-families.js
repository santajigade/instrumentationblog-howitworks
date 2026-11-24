var PER=4.8,ph=0,vin=0,vout=5,dv=0,pv=5;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;vin=2.5-2.5*Math.cos(2*Math.PI*u);var nv=vin<2?5:vin>3?0:5*(3-vin);dv=nv-vout;vout=nv;}
function VY(v){return 310-v*44;}
function fet(x,y,on,p){var part=vin>2&&vin<3,c=part?'#d97706':on?'#16a34a':'#94a3b8';
ln(x,y-28,x,y+28,c,5);ln(x-12,y-22,x-12,y+22,'#1f2937',3);ln(x-12,y,x-34,y,'#1f2937',2);if(p)ci(x-17,y,5,'#fff','#1f2937',2);
L(p?'PMOS':'NMOS',x+14,y-10,12,'#1f2733','left',1);L(part?'PARTLY ON':on?'ON':'OFF',x+14,y+8,12,c,'left',1);}
function ladder(x,lo,hi,name){var w=70;
rc(x,VY(5),w,VY(hi)-VY(5),'#dbeafe');rc(x,VY(hi),w,VY(lo)-VY(hi),'#fde68a');rc(x,VY(lo),w,VY(0)-VY(lo),'#e2e8f0');
C.strokeStyle='#475569';C.lineWidth=1.5;C.strokeRect(x,VY(5),w,VY(0)-VY(5));
L(name,x+w/2,VY(5)-14,13,'#1f2733','center',1);
L(m(hi,1)+' V',x+w+4,VY(hi),11,'#475569','left');L(m(lo,1)+' V',x+w+4,VY(lo),11,'#475569','left');
L('HIGH',x+w/2,(VY(5)+VY(hi))/2,11,'#1e3a8a','center',1);L('LOW',x+w/2,(VY(lo)+VY(0))/2,11,'#334155','center',1);L('Undefined',x+w/2,(VY(lo)+VY(hi))/2,11,'#92400e','center',1);
var z=vin>=hi?'HIGH':vin<=lo?'LOW':'Undefined',zc=vin>=hi?'#1e3a8a':vin<=lo?'#334155':'#b45309';
L('Reads '+z,x+w/2,VY(0)+18,12,zc,'center',1);}
function draw(){
L('CMOS inverter at 5 V; transfer curve simplified and slowed down',20,22,11,'#5b6576','left');
var x=180;
ln(120,62,240,62,'#dc2626',3);L('VDD +5 V',250,62,12,'#dc2626','left',1);
ln(x,62,x,92,'#1f2937',2);fet(x,120,vin<3,1);ln(x,148,x,212,'#1f2937',2);fet(x,240,vin>2,0);ln(x,268,x,300,'#1f2937',2);
ln(130,300,230,300,'#1f2937',3);ln(145,307,215,307,'#1f2937',2);ln(160,314,200,314,'#1f2937',2);
// input
ln(146,120,110,120,'#1f2937',2);ln(146,240,110,240,'#1f2937',2);ln(110,120,110,240,'#1f2937',2);ln(60,180,110,180,'#7c3aed',3);ci(110,180,4,'#1f2937');
L('Vin',60,165,13,'#7c3aed','left',1);L(m(vin,2)+' V',60,198,13,'#7c3aed','left',1);
// output and load capacitance
ci(x,180,4,'#1f2937');ln(x,180,310,180,'#ea580c',3);ln(290,180,290,205,'#1f2937',2);ln(276,205,304,205,'#1f2937',3);ln(276,213,304,213,'#1f2937',3);ln(290,213,290,300,'#1f2937',2);ln(230,300,290,300,'#1f2937',3);
L('CL',308,209,12,'#1f2933','left',1);L('Vout '+m(vout,1)+' V',192,166,13,'#ea580c','left',1);
// charge flow on switching
if(Math.abs(dv)>0.01){var up=dv>0;for(var k=0;k<4;k++){var f=((ph*2.5+k*0.25)%1);var yy=up?62+f*118:180+f*120;ci(x+8,yy,4,'#f59e0b');}
L(up?'Charging CL':'Discharging CL',x+20,up?92:285,11,'#b45309','left',1);}
// ladders
ladder(355,0.8,2.0,'TTL input');ladder(495,1.5,3.5,'74HC input');
ln(340,VY(vin),355,VY(vin),'#7c3aed',2.5);ln(425,VY(vin),495,VY(vin),'#7c3aed',2.5,[6,4]);ln(565,VY(vin),578,VY(vin),'#7c3aed',2.5);ar(600,VY(vin),578,VY(vin),'#7c3aed',2.5);L('Vin',604,VY(vin),12,'#7c3aed','left',1);
mk(1,140,96);mk(2,140,264);mk(3,60,138);mk(4,320,240);mk(5,390,VY(5)-40);mk(6,530,VY(5)-40);
}
