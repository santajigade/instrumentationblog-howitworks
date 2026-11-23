var PER=4.8,ph=0,Tc=0,Rt=100;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;Tc=50*(1-Math.cos(2*Math.PI*u));Rt=100*(1+3.9083e-3*Tc-5.775e-7*Tc*Tc);}
function lc(a,b,f){return 'rgb('+Math.round(a[0]+(b[0]-a[0])*f)+','+Math.round(a[1]+(b[1]-a[1])*f)+','+Math.round(a[2]+(b[2]-a[2])*f)+')';}
function draw(){
L('PT100 per IEC 60751, heating and cooling slowed down, atoms and electrons not to scale',20,22,11,'#5b6576','left');
var f=Tc/100,liq=lc([191,219,254],[252,165,120],f);
// ---------- bath with PT100 probe ----------
rc(24,150,150,170,'#f1f5f9','#64748b',8);rc(28,180,142,136,liq,null,6);
L('Process',34,166,12,'#334155','left',1);
// heater glow at bottom when heating
var heat=Math.max(0,Math.sin(2*Math.PI*ph/PER));
for(var i=0;i<5;i++){ci(44+i*27,306,5,lc([203,213,225],[239,68,68],heat),null);}
// probe
rc(88,62,22,28,'#475569',null,4);rc(93,90,12,210,'#cbd5e1','#64748b',3);
rc(94,262,10,34,lc([226,232,240],[249,115,22],f),'#9a3412',2);
// lead wires to meter
ln(99,62,99,48,'#334155',2);ln(99,48,214,48,'#dc2626',2.5);ln(104,62,104,56,'#334155',2);ln(104,56,214,56,'#1d4ed8',2.5);
// ohmmeter / readout
rc(214,36,166,80,'#0f172a',null,8);
L('R = '+Rt.toFixed(2)+' Ω',297,62,17,'#4ade80','center',1);
L('T = '+Tc.toFixed(1)+' °C',297,92,15,'#fde68a','center',1);
// ---------- zoomed platinum wire ----------
var zx=290,zy=238,zr=74;
C.setLineDash([4,4]);ln(104,268,zx-zr,zy-20,'#94a3b8',1.2);ln(104,290,zx-zr+6,zy+30,'#94a3b8',1.2);C.setLineDash([]);
C.save();C.beginPath();C.arc(zx,zy,zr,0,Math.PI*2);C.clip();
rc(zx-zr,zy-zr,2*zr,2*zr,'#f8fafc');
var amp=1+5*f;
for(var r=0;r<4;r++)for(var c=0;c<5;c++){var ax=zx-56+c*28,ay=zy-42+r*28,k=r*5+c;
ci(ax+amp*Math.sin(2*Math.PI*ph*10/PER+k*1.7),ay+amp*Math.cos(2*Math.PI*ph*9/PER+k*2.3),8,'#94a3b8','#475569',1);}
for(var e=0;e<6;e++){var ex=zx-zr+((ph/PER*2+e/6)%1)*2*zr,ey=zy-28+(e%3)*28+14+2*Math.sin(ex/9+e);ci(ex,ey,3.5,'#2563eb');}
C.restore();ci(zx,zy,zr,null,'#334155',2);
L('Platinum wire, zoomed',zx,zy+zr+14,12,'#334155','center',1);
// ---------- R vs T graph ----------
var gx0=445,gx1=615,gy0=270,gy1=80;
ln(gx0,gy0,gx1+8,gy0,'#64748b',1.5);ln(gx0,gy0,gx0,gy1-10,'#64748b',1.5);
function GX(t){return gx0+(gx1-gx0)*t/100;}function GY(r){return gy0-(gy0-gy1)*(r-95)/(140-95);}
C.strokeStyle='#ea580c';C.lineWidth=2.5;C.beginPath();
for(var t=0;t<=100;t+=2){var rr=100*(1+3.9083e-3*t-5.775e-7*t*t);if(t==0)C.moveTo(GX(t),GY(rr));else C.lineTo(GX(t),GY(rr));}C.stroke();
ln(GX(Tc),gy0,GX(Tc),GY(Rt),'#94a3b8',1,[3,3]);ln(gx0,GY(Rt),GX(Tc),GY(Rt),'#94a3b8',1,[3,3]);
ci(GX(Tc),GY(Rt),6,'#dc2626','#fff',2);
L('0',gx0,gy0+14,11,'#334155');L('50',GX(50),gy0+14,11,'#334155');L('100 °C',GX(100),gy0+14,11,'#334155');
L('100 Ω',gx0-6,GY(100),11,'#334155','right');L('138.5 Ω',gx0-6,GY(138.51),11,'#334155','right');
ln(gx0-3,GY(138.51),gx0+3,GY(138.51),'#334155',1.5);
L('Resistance rises with temperature',525,62,13,'#1f2733','center',1);
// formula
rc(400,298,230,52,'#fff7ed','#fdba74',8);
L('R = R0 (1 + A·T + B·T²)',515,315,14,'#9a3412','center',1);
L('R0 = 100 Ω, linear α = 0.00385',515,336,12,'#334155','center');
// markers
mk(1,124,279);mk(2,72,76);mk(3,160,70);mk(4,394,50);mk(5,zx+zr-6,zy-zr+10);mk(6,GX(55),GY(128));
}
