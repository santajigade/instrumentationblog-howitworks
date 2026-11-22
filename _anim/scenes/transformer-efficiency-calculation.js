var PER=4.8,ph=0,u=0,x=0.5;
var PI0=0.5,PCU=2;
function eta(v){return 100*100*v/(100*v+PI0+PCU*v*v);}
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;x=0.6-0.4*Math.cos(2*Math.PI*u);}
function draw(){
L('Illustrative losses: iron loss = one quarter of full load copper loss',20,22,11,'#5b6576','left');
var cu=x*x;
// core
var cg='rgba(220,38,38,0.35)';
rc(50,60,170,170,'#94a3b8','#475569',4);rc(80,90,110,110,'#fff',null,0);
C.globalAlpha=0.5;rc(50,60,170,170,null,'#dc2626',4);C.globalAlpha=1;
// flux path dashes (constant)
C.setLineDash([10,10]);C.lineDashOffset=-ph*50;C.strokeStyle='#7c3aed';C.lineWidth=2.5;C.strokeRect(65,75,140,140);C.setLineDash([]);C.lineDashOffset=0;
L('Flux',135,82,11,'#5b21b6','center',1);
// windings
var hc='rgba(234,88,12,'+(0.15+0.85*cu)+')';
for(var k=0;k<7;k++){var y=98+k*14;rc(40,y,50,10,'#b45309',null,4);rc(180,y,50,10,'#b45309',null,4);}
C.globalAlpha=0.2+0.6*cu;rc(34,92,62,104,'#f97316',null,10);rc(174,92,62,104,'#f97316',null,10);C.globalAlpha=1;
L('Primary',65,244,11,'#334155','center',1);L('Secondary',205,244,11,'#334155','center',1);
// supply wires
ln(10,100,40,100,'#334155',2);ln(10,190,40,190,'#334155',2);L('Supply',8,90,11,'#334155','left',1);
// load circuit
ln(230,100,300,100,'#334155',2);ln(230,190,300,190,'#334155',2);ln(300,100,300,108,'#334155',2);
var nl=Math.round(x*5);
for(var k=0;k<5;k++){var ly=112+k*16;var on=k<nl;ci(312,ly,6,on?'#facc15':'#e5e7eb','#475569',1.5);if(on){C.globalAlpha=0.3;ci(312,ly,11,'#fde047');C.globalAlpha=1;}}
ln(300,190,300,184,'#334155',2);
// current dots speed ~ x
var dn=Math.round(2+x*4);for(var k=0;k<6;k++){var f=((ph*1.25+k/6)%1);var xx=232+66*f;C.globalAlpha=k<dn?1:0.15;ci(xx,100,3,'#16a34a');ci(298-66*f,190,3,'#16a34a');C.globalAlpha=1;}
L('Load',312,206,11,'#334155','center',1);
L('Load x = '+Math.round(x*100)+' %',310,252,15,'#1e63b8','center',1);
// loss bars
var bx=380,sc=100;rc(bx-10,50,250,180,'#f8fafc','#e2e8f0',8);
L('Losses at this load',bx+115,66,12,'#334155','center',1);
L('Iron loss (constant)',bx,88,12,'#b91c1c','left',1);rc(bx,98,PI0*sc,16,'#ef4444',null,4);
L('Copper loss = x² × full load copper loss',bx,132,11,'#c2410c','left',1);rc(bx,140,PCU*sc*0.98,16,'#fde7d6',null,4);rc(bx,140,PCU*cu*sc*0.98,16,'#f97316',null,4);
L('x² = '+(cu).toFixed(2),bx+228,148,11,'#c2410c','right',1);
var eq=Math.abs(cu*PCU-PI0)<0.06;
ln(bx+PI0*sc,137,bx+PI0*sc,160,'#b91c1c',1.5,[3,3]);
L(eq?'Copper loss = iron loss: maximum efficiency':(cu*PCU<PI0?'Light load: iron loss dominates':'Heavy load: copper loss dominates'),bx+115,186,12,eq?'#16a34a':'#334155','center',1);
L('Max η at x = √(Piron ÷ Pcu,FL) = 50 % here',bx+115,210,11,'#5b6576','center');
// efficiency curve
var gx=380,gy=326,gw=230,gh=56;rc(gx-10,244,250,108,'#fff','#e2e8f0',8);
L('Efficiency η versus load',gx,258,12,'#334155','left',1);
var lo=97.0,hi=98.2;function Y(e){return gy-gh*(e-lo)/(hi-lo);}
ln(gx,gy,gx+gw,gy,'#cbd5e1',1.5);
C.strokeStyle='#1e63b8';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=60;k++){var v=0.2+0.8*k/60;var xx=gx+gw*(v-0.2)/0.8;if(k==0)C.moveTo(xx,Y(eta(v)));else C.lineTo(xx,Y(eta(v)));}C.stroke();
var px=gx+gw*(0.5-0.2)/0.8;ln(px,Y(eta(0.5)),px,gy,'#16a34a',1.5,[3,3]);L('peak',px,gy+10,11,'#16a34a','center',1);
L('20 %',gx+8,gy+10,11,'#5b6576','center');L('100 %',gx+gw-12,gy+10,11,'#5b6576','center');
ci(gx+gw*(x-0.2)/0.8,Y(eta(x)),5,'#1e63b8','#fff',2);
// formula
rc(20,270,330,74,'#eef4fb',null,8);
L('η = Pout ÷ (Pout + Piron + x² Pcu,FL) × 100',185,292,13,'#1a2b4a','center',1);
L('Pout = x × kVA × power factor × 1000',185,316,12,'#334155','center');
L('Piron is the same at every load',185,334,11,'#5b6576','center');
mk(1,135,46);mk(2,24,214);mk(3,336,96);mk(4,624,96);mk(5,px-22,Y(eta(0.5))+22);
}
