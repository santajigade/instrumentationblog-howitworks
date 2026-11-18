var PER=4.8,ph=0,u=0,vr=1,Wd=40;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;vr=5-4*Math.cos(2*Math.PI*u);Wd=26*Math.sqrt((vr+0.7)/1.7);}
function draw(){
L('Illustrative reverse voltage sweep; carriers shown fixed for clarity',20,22,11,'#5b6576','left');
var x0=80,x1=420,y0=70,y1=170,cx=250;
rc(x0,y0,cx-x0,y1-y0,'#fde2e4','#e11d48');rc(cx,y0,x1-cx,y1-y0,'#dbeafe','#2563eb');
// depletion region
rc(cx-Wd,y0,2*Wd,y1-y0,'#f8fafc','#64748b');C.setLineDash([4,4]);ln(cx-Wd,y0,cx-Wd,y1,'#64748b',1.5);ln(cx+Wd,y0,cx+Wd,y1,'#64748b',1.5);C.setLineDash([]);
// fixed ions inside depletion
for(var r=0;r<4;r++){for(var c=0;c<12;c++){var xl=cx-Wd+6+c*12,xr=cx+Wd-6-c*12,yy=y0+16+r*23;if(xl<cx-4){rc(xl-4,yy-4,8,8,'#e11d48');L('−',xl,yy-1,10,'#fff','center',1);}if(xr>cx+4){rc(xr-4,yy-4,8,8,'#2563eb');L('+',xr,yy,10,'#fff','center',1);}}}
// mobile carriers, jiggle each frame
for(var r=0;r<4;r++){for(var c=0;c<8;c++){var j=0;
var hx=x0+12+c*20+j,hy=y0+14+r*24+j*0.6;if(hx<cx-Wd-6){ci(hx,hy,6,'#fff','#e11d48',1.5);L('+',hx,hy,10,'#e11d48','center',1);}
var ex=x1-12-c*20-j,ey=y0+14+r*24-j*0.6;if(ex>cx+Wd+6){ci(ex,ey,5,'#1d4ed8');}}}
L('P',x0+14,y1+16,14,'#e11d48','center',1);L('N',x1-14,y1+16,14,'#2563eb','center',1);
ar(cx-Wd,y1+16,cx+Wd,y1+16,'#334155',1.5);ar(cx+Wd,y1+16,cx-Wd,y1+16,'#334155',1.5);L('W',cx,y1+30,12,'#334155','center',1);
// reverse bias source
var by=240;ln(x0,120,50,120,'#334155',2);ln(50,120,50,by,'#334155',2);ln(x1,120,450,120,'#334155',2);ln(450,120,450,by,'#334155',2);
ln(50,by,225,by,'#334155',2);ln(275,by,450,by,'#334155',2);
rc(225,by-18,50,36,'#1f2937',null,6);L('−',236,by,14,'#fff','center',1);L('+',264,by,14,'#fff','center',1);
L('Reverse voltage Vr = '+m(vr,1)+' V',250,by+32,13,'#1f2733','center',1);
// C vs Vr curve
var gx=480,gy=170,gw=140,gh=100;ln(gx,gy,gx+gw,gy,'#94a3b8',1.5);ln(gx,gy,gx,gy-gh,'#94a3b8',1.5);
C.strokeStyle='#7c3aed';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=28;k++){var v=1+8*k/28,cc=Math.sqrt(1.7/(v+0.7));var x=gx+gw*k/28,y=gy-gh*cc;if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
var cvl=Math.sqrt(1.7/(vr+0.7));ci(gx+gw*(vr-1)/8,gy-gh*cvl,6,'#7c3aed','#fff',2);
L('C',gx-10,gy-gh,12,'#334155','center',1);L('Vr',gx+gw,gy+14,12,'#334155','center',1);
L('Capacitance vs reverse voltage',gx+gw/2,gy+32,11,'#334155','center');
// capacitance bar
rc(480,232,140,16,'#e2e8f0',null,8);rc(480,232,140*cvl,16,'#7c3aed',null,8);L('Junction capacitance',550,262,12,'#334155','center');
// formula box
rc(60,292,520,56,'#f6f8fc','#dde3ee',8);
L('C = ε A / W : higher Vr widens W, so C falls',320,311,12,'#1f2733','center',1);L('In an LC tank, smaller C gives a higher f = 1 / (2π√(LC))',320,331,12,'#334155','center');
mk(1,x0+18,y0-12);mk(2,cx,y0-12);mk(3,x1-18,y0-12);mk(4,205,by);mk(5,600,62);
}
