var PER=4.8,ph=0,a=0,atm=14.7,pa=48.7,pg=34;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;a=0.5-0.5*Math.cos(2*Math.PI*u);atm=14.7-2.2*a;pg=pa-atm;}
function Y(p){return 320-p*4.5;}
function dial(cx,cy,v,c,lab,unit){ci(cx,cy,58,'#fff','#475569',3);
for(var k=0;k<=6;k++){if(k==0||k==6){var an=(225-k*45)*Math.PI/180;ln(cx+48*Math.cos(an),cy-48*Math.sin(an),cx+56*Math.cos(an),cy-56*Math.sin(an),'#475569',2);continue;}var an=(225-k*45)*Math.PI/180;ln(cx+48*Math.cos(an),cy-48*Math.sin(an),cx+56*Math.cos(an),cy-56*Math.sin(an),'#475569',2);L(String(k*10),cx+37*Math.cos(an),cy-37*Math.sin(an),11,'#475569');}
var an=(225-v/60*270)*Math.PI/180;ar(cx,cy,cx+30*Math.cos(an),cy-30*Math.sin(an),c,4);ci(cx,cy,6,'#1f2937');
rc(cx-50,cy+66,100,22,'#f6f8fc',c,6);L(m(v,1)+' '+unit,cx,cy+77,14,c,'center',1);L(lab,cx,cy+102,13,'#1f2733','center',1);}
function draw(){
L('Same tyre, same absolute pressure; only the atmosphere changes with altitude',20,22,11,'#5b6576','left');
// scale
ln(70,Y(0),70,Y(55),'#94a3b8',1.5);
for(var p=0;p<=50;p+=10){ln(64,Y(p),70,Y(p),'#94a3b8',1.5);L(String(p),58,Y(p),11,'#475569','right');}
L('psi',58,Y(55),11,'#475569','right');
// vacuum line
ln(70,Y(0),330,Y(0),'#1f2937',2.5);L('Perfect vacuum, 0 psia',200,Y(0)+16,12,'#1f2937','center',1);
// atmosphere band
C.fillStyle='rgba(56,189,248,0.18)';C.fillRect(71,Y(atm),259,Y(0)-Y(atm));
// absolute bar
rc(95,Y(pa),55,Y(0)-Y(pa),'#2563eb',null,4);L('Absolute',122,Y(pa)-28,12,'#1e3a8a','center',1);L(m(pa,1)+' psia',122,Y(pa)-13,12,'#1e3a8a','center',1);
// gauge bar
rc(195,Y(pa),55,Y(atm)-Y(pa),'#ea580c',null,4);L('Gauge',222,Y(pa)-28,12,'#9a3412','center',1);L(m(pg,1)+' psig',222,Y(pa)-13,12,'#9a3412','center',1);
// atm line
ln(70,Y(atm),330,Y(atm),'#0284c7',2.5,[8,5]);L('Atmosphere '+m(atm,1)+' psia',265,Y(atm)+16,12,'#0369a1','center',1);
// equation
rc(355,50,270,34,'#f6f8fc','#dde3ee',8);L('Absolute = Gauge + Atmospheric',490,67,14,'#1f2733','center',1);
// altitude panel
var bx=360,by=150;C.fillStyle='#e2e8f0';C.beginPath();C.moveTo(bx,by);C.lineTo(bx+130,by-52);C.lineTo(bx+260,by);C.closePath();C.fill();
C.fillStyle='#f8fafc';C.beginPath();C.moveTo(bx+108,by-43);C.lineTo(bx+130,by-52);C.lineTo(bx+152,by-43);C.closePath();C.fill();
ln(bx,by,bx+260,by,'#64748b',2);
var px=bx+20+110*a,py=by-6-44*a;ci(px,py,7,'#ea580c','#fff',2);
L('Sea level 14.7 psia',bx+4,by+14,12,'#334155','left');L('Denver 12.5 psia',bx+152,by-56,12,'#334155','left');
// dials
dial(420,238,pa,'#1e3a8a','Absolute gauge','psia');
dial(565,238,pg,'#c2410c','Gauge reading','psig');
mk(1,40,Y(0));mk(2,315,Y(atm)-14);mk(3,262,Y(pa)+40);mk(4,165,Y(pa)+40);mk(5,px-22,py+4);mk(6,617,186);
}
