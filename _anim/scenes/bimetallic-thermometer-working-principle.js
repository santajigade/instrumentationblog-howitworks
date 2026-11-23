var PER=4.8,ph=0,Tc=20;
function upd(){}
function step(dt){ph=(ph+dt)%PER;var u=ph/PER;Tc=20+40*(1-Math.cos(2*Math.PI*u));}
function lerpc(a,b,f){return 'rgb('+Math.round(a[0]+(b[0]-a[0])*f)+','+Math.round(a[1]+(b[1]-a[1])*f)+','+Math.round(a[2]+(b[2]-a[2])*f)+')';}
function draw(){
L('Schematic, bending exaggerated, heating and cooling slowed down',20,22,11,'#5b6576','left');
var f=(Tc-20)/80,hot=lerpc([191,219,254],[254,178,120],f);
// ---------- gauge: dial on top, stem below ----------
var dx=140,dy=118,R=70;
ci(dx,dy,R+9,'#cbd5e1','#64748b',2);ci(dx,dy,R,'#ffffff','#94a3b8',1.5);
for(var v=0;v<=120;v+=10){var a=(135+270*v/120)*Math.PI/180,big=v%40==0;
ln(dx+(R-(big?14:8))*Math.cos(a),dy+(R-(big?14:8))*Math.sin(a),dx+(R-3)*Math.cos(a),dy+(R-3)*Math.sin(a),'#334155',big?2:1.2);
if(big)L(String(v),dx+(R-28)*Math.cos(a),dy+(R-28)*Math.sin(a),12,'#334155','center',1);}
L('°C',dx,dy+34,12,'#334155','center',1);
var pa=(135+270*Tc/120)*Math.PI/180;
C.lineCap='round';ln(dx,dy,dx+(R-12)*Math.cos(pa),dy+(R-12)*Math.sin(pa),'#dc2626',3.5);C.lineCap='butt';
ci(dx,dy,6,'#1f2937');
// stem
var sx=dx,top=dy+R+9,sb=340;
rc(sx-16,top,32,sb-top,'#e5e7eb','#64748b',4);
// process connection (hex fitting)
rc(sx-26,214,52,20,'#94a3b8','#475569',3);for(var k=0;k<4;k++)ln(sx-20+k*13,216,sx-20+k*13,232,'#64748b',1);
// pipe with fluid
rc(20,250,250,14,'#9aa5b8');rc(20,264,250,76,hot);rc(20,340,250,8,'#9aa5b8');
rc(sx-16,264,32,76,'rgba(229,231,235,0.92)','#64748b',4);
// flow arrows in pipe (two whole cycles per loop)
for(var i=0;i<3;i++){var xx=30+((ph/PER*2+i/3)%1)*220;if(Math.abs(xx-sx)>34)ar(xx-14,322,xx+4,322,'#475569',1.8);}
L('Process fluid',60,290,11,'#334155','center',1);
// helix: bottom fixed, top end twists with temperature
var hy0=332,hy1=262,rot=f*Math.PI*1.4;
C.lineWidth=3;
for(var s=0;s<2;s++){C.strokeStyle=s?'#b45309':'#64748b';C.beginPath();
for(var y=hy0;y>=hy1;y-=1){var g=(hy0-y)/(hy0-hy1),x=sx+10*Math.sin(2*Math.PI*(hy0-y)/14+rot*g+(s?0.5:0));if(y==hy0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();}
rc(sx-12,hy0,24,5,'#334155');
// shaft up to pointer
ln(sx,hy1,sx,top,'#1f2937',2);
// rotation indicator on shaft top
var cw=10*Math.cos(rot);ln(sx-cw,240,sx+cw,240,'#dc2626',3);
// ---------- straight strip demonstration ----------
L('Bimetal strip',420,62,16,'#1f2733','center',1);
var x0=330,y0=200,Ls=200,kc=0.0012+0.0043*f,th=9;
rc(x0-26,y0-30,26,60,'#475569',null,3);L('Fixed',x0-13,y0+44,11,'#334155');
function lay(off,col){C.fillStyle=col;C.beginPath();var n=40,i,pts=[];
for(i=0;i<=n;i++){var sL=Ls*i/n,a=kc*sL,r=1/kc,x=x0+r*Math.sin(a),y=y0-(r-r*Math.cos(a));pts.push([x,y,a]);}
for(i=0;i<=n;i++){var p=pts[i];C.lineTo(p[0]-Math.sin(p[2])*off,p[1]-Math.cos(p[2])*off);}
for(i=n;i>=0;i--){var p=pts[i];C.lineTo(p[0]-Math.sin(p[2])*(off-th),p[1]-Math.cos(p[2])*(off-th));}
C.closePath();C.fill();return pts;}
var pts=lay(th,'#94a3b8');lay(0,'#d97706');
var tip=pts[pts.length-1];
// straight reference
ln(x0,y0+th/2,x0+Ls,y0+th/2,'#94a3b8',1.2,[5,5]);
ar(tip[0]+14,y0+4,tip[0]+14,tip[1]+2,'#16a34a',2);
L('Invar, low expansion',430,252,13,'#475569','left',1);
L('Brass, high expansion',430,274,13,'#b45309','left',1);
rc(416,246,8,8,'#94a3b8');rc(416,268,8,8,'#d97706');
L('Strip bends toward the low expansion side',470,306,12,'#1f2733','center');
// temperature readout
rc(530,48,100,46,'#fff7ed','#fdba74',8);
L('T = '+m(Tc,0)+' °C',580,71,16,'#c2410c','center',1);
L(Math.sin(2*Math.PI*ph/PER)>=0?'Heating':'Cooling',580,110,12,'#334155','center',1);
// markers
mk(1,sx+28,300);mk(2,sx+30,206);mk(3,sx+30,244);mk(4,dx+R+18,dy-48);mk(5,sx-40,224);mk(6,x0+50,y0+24);
}
