# Canvas scenes (logical 640 x 360). Each defines upd(), step(dt), draw().
# Helpers available: C, W, H, T, P, m(x,d), o(id,txt), L(t,x,y,size,color,align,bold), ln, rc, ci, mk, ar, sm, clamp
K_TABLE = open(__import__('pathlib').Path(__file__).resolve().parent / 'k.js').read()

COMMON = r"""
(function(){
var cv=document.getElementById('hw-cv');if(!cv)return;
var C=cv.getContext('2d'),W=640,H=360,run=true,vis=true,last=0,T=0,P={},dirty=true;
function fit(){var w=cv.parentNode.clientWidth,d=window.devicePixelRatio||1,s=w/W;cv.width=Math.round(w*d);cv.height=Math.round(H*s*d);cv.style.height=Math.round(H*s)+'px';C.setTransform(s*d,0,0,s*d,0,0);dirty=true;}
function m(x,d){var s=Math.abs(x).toFixed(d);return(x<0&&Number(s)!==0?'−':'')+s;}
function o(id,v){var e=document.getElementById('hw-o-'+id);if(e&&e.textContent!==v)e.textContent=v;}
function L(t,x,y,sz,c,a,b){C.font=(b?'700 ':'')+(sz||13)+'px "Segoe UI",Arial,sans-serif';C.fillStyle=c||'#1f2733';C.textAlign=a||'center';C.textBaseline='middle';C.fillText(t,x,y);}
function ln(x1,y1,x2,y2,c,w,d){C.strokeStyle=c;C.lineWidth=w||1.5;C.setLineDash(d||[]);C.beginPath();C.moveTo(x1,y1);C.lineTo(x2,y2);C.stroke();C.setLineDash([]);}
function rc(x,y,w,h,f,s,r){C.beginPath();if(r&&C.roundRect)C.roundRect(x,y,w,h,r);else C.rect(x,y,w,h);if(f){C.fillStyle=f;C.fill();}if(s){C.strokeStyle=s;C.lineWidth=1.5;C.stroke();}}
function ci(x,y,r,f,s,w){C.beginPath();C.arc(x,y,r,0,Math.PI*2);if(f){C.fillStyle=f;C.fill();}if(s){C.strokeStyle=s;C.lineWidth=w||1.5;C.stroke();}}
function mk(n,x,y){ci(x,y,11,'#d9622b','#fff',2);L(String(n),x,y+1,13,'#fff','center',1);}
function ar(x1,y1,x2,y2,c,w){ln(x1,y1,x2,y2,c,w);var a=Math.atan2(y2-y1,x2-x1),h=8;C.fillStyle=c;C.beginPath();C.moveTo(x2,y2);C.lineTo(x2-h*Math.cos(a-.45),y2-h*Math.sin(a-.45));C.lineTo(x2-h*Math.cos(a+.45),y2-h*Math.sin(a+.45));C.closePath();C.fill();}
function sm(u){u=u<0?0:u>1?1:u;return u*u*(3-2*u);}
function clamp(x,a,b){return x<a?a:x>b?b:x;}
function rd(){[].forEach.call(document.querySelectorAll('#hw-ctl input'),function(i){P[i.dataset.k]=parseFloat(i.value);var e=document.getElementById(i.id+'-v');if(e)e.textContent=m(P[i.dataset.k],+i.dataset.d)+(i.dataset.u?' '+i.dataset.u:'');});upd();dirty=true;}
function pipe(x1,x2,cy,R,fl){rc(x1,cy-R-12,x2-x1,12,'#9aa5b8');rc(x1,cy+R,x2-x1,12,'#9aa5b8');rc(x1,cy-R,x2-x1,2*R,fl||'#e6f0fd');}
@@SCENE@@
function fr(t){var dt=Math.min(.05,((t-last)/1000)||0);last=t;if(run&&vis&&!document.hidden){T+=dt;step(dt);dirty=true;}if(dirty&&vis){C.clearRect(0,0,W,H);draw();dirty=false;}requestAnimationFrame(fr);}
[].forEach.call(document.querySelectorAll('#hw-ctl input'),function(i){i.addEventListener('input',rd);});
var dl=document.getElementById('hw-dl');if(dl&&cv.toBlob)dl.addEventListener('click',function(){cv.toBlob(function(b){var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=dl.dataset.name;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);},'image/png');});
var pp=document.getElementById('hw-pp');if(pp)pp.addEventListener('click',function(){run=!run;pp.textContent=run?'Pause animation':'Play animation';});
if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches){run=false;if(pp)pp.textContent='Play animation';}
if('IntersectionObserver' in window)new IntersectionObserver(function(e){vis=e[0].isIntersecting;dirty=true;}).observe(cv);
window.addEventListener('resize',function(){fit();C.clearRect(0,0,W,H);draw();});fit();rd();step(0.016);draw();requestAnimationFrame(fr);
})();
"""

S = {}

S['orifice-plate'] = r"""
var cy=170,R0=70,N=120,pt=[];for(var i=0;i<N;i++)pt.push({x:20+Math.random()*600,y:Math.random()*2-1});
function hh(x){var b=P.beta*R0,vc=b*0.8;if(x<230)return R0;if(x<300)return R0+(b-R0)*sm((x-230)/70);if(x<335)return b+(vc-b)*sm((x-300)/35);if(x<470)return vc+(R0-vc)*sm((x-335)/135);return R0;}
function lf(){return 1-Math.pow(P.beta,1.9);}
function upd(){var dp=Math.pow(P.flow/100,2)*100;o('dp',m(dp,1)+' %');o('loss',m(lf()*100,0)+' % of DP');o('vr',m(1/(P.beta*P.beta),2)+' x');o('dpr',m(P.flow,0)+' % flow');}
function step(dt){var v0=P.flow/100*110+4;for(var i=0;i<N;i++){var p=pt[i];p.x+=v0*R0/hh(p.x)*dt;if(p.x>620){p.x=20;p.y=Math.random()*2-1;}}}
function draw(){pipe(20,620,cy,R0);
C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i];var y=cy+p.y*hh(p.x)*0.9;if(p.x>294&&p.x<306&&Math.abs(y-cy)>P.beta*R0)continue;C.fillRect(p.x-1.5,y-1.5,3,3);}
var b=P.beta*R0;rc(296,cy-R0-12,8,R0-b+12,'#475569');rc(296,cy+b,8,R0-b+12,'#475569');rc(286,cy-R0-20,28,8,'#64748b');rc(286,cy+R0+12,28,8,'#64748b');
ln(284,cy-R0-20,284,64,'#b02a52',2.5);ln(316,cy-R0-20,316,64,'#1e63b8',2.5);
rc(250,22,100,42,'#1a2333',null,8);L('DP',272,43,13,'#fff','center',1);var dp=Math.pow(P.flow/100,2);rc(292,36,50,14,'#334155');rc(292,36,50*dp,14,'#f59e0b');
L('H',276,76,12,'#b02a52','right',1);L('L',324,76,12,'#1e63b8','left',1);
ar(40,cy,95,cy,'#1a2333',2);L('Flow',67,cy-14,12,'#1a2333','center',1);
var y0=278,sc=60*dp;ln(30,y0,620,y0,'#cbd5e1',1,[4,4]);C.strokeStyle='#d9622b';C.lineWidth=2.5;C.beginPath();for(var x=30;x<=620;x+=4){var g=0;if(x>=285&&x<335)g=sm((x-285)/50);else if(x>=335&&x<470)g=1-(1-lf())*sm((x-335)/135);else if(x>=470)g=lf();var y=y0+g*sc;if(x==30)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
L('Pressure along the pipe',30,y0-12,12,'#5b6576','left');if(dp>0.05){L('permanent loss',560,y0+lf()*sc+14,11,'#d9622b','center');}
mk(1,318,cy-R0+18);mk(2,262,98);mk(3,338,98);mk(4,345,cy+b*0.8+18);mk(5,368,30);}
"""

S['magnetic-flow-meter'] = r"""
var cy=180,R=60,N=70,pt=[],ch=[];for(var i=0;i<N;i++)pt.push({x:20+Math.random()*340,y:Math.random()*2-1});
for(var j=0;j<14;j++)ch.push({p:Math.random(),y:(Math.random()*1.6-0.8),q:j%2?1:-1});
function sg(){return Math.floor(T*1.2)%2?-1:1;}
function E(){return 0.002*(P.d/1000)*P.v*1000;}
function upd(){o('e',m(E(),3)+' mV');var q=P.v*Math.PI*Math.pow(P.d/1000,2)/4*3600;o('q',m(q,q<10?2:1)+' m³/h');o('vel',m(P.v,1)+' m/s');}
function step(dt){for(var i=0;i<N;i++){var p=pt[i];p.x+=(P.v*14+6)*dt;if(p.x>360){p.x=20;p.y=Math.random()*2-1;}}for(var j=0;j<ch.length;j++){ch[j].p+=dt*(0.15+P.v*0.06);if(ch[j].p>1){ch[j].p=0;ch[j].y=Math.random()*1.6-0.8;}}}
function draw(){L('Side view',190,22,13,'#5b6576','center',1);L('Cross section',500,22,13,'#5b6576','center',1);
pipe(20,360,cy,R);rc(20,cy-R,340,5,'#fde68a');rc(20,cy+R-5,340,5,'#fde68a');
rc(150,cy-R-40,80,26,'#b45309',null,4);rc(150,cy+R+14,80,26,'#b45309',null,4);
var s=sg();for(var x=162;x<=218;x+=14){ln(x,cy-R+6,x,cy+R-6,'#7c3aed',1.2,[5,4]);if(s>0)ar(x,cy-R+20,x,cy-R+34,'#7c3aed',1.2);else ar(x,cy+R-20,x,cy+R-34,'#7c3aed',1.2);}
C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i];C.fillRect(p.x-1.5,cy+p.y*R*0.85-1.5,3,3);}
ci(190,cy,8,'#f59e0b','#92400e',2);ar(40,cy,92,cy,'#1a2333',2);
var X=500,Y=180,r=82;ci(X,Y,r+10,'#9aa5b8');ci(X,Y,r+2,'#fde68a');ci(X,Y,r-3,'#e6f0fd');
rc(X-40,Y-r-38,80,22,'#b45309',null,4);rc(X-40,Y+r+16,80,22,'#b45309',null,4);
for(var k=-1;k<=1;k++){var xx=X+k*32;ln(xx,Y-r+8,xx,Y+r-8,'#7c3aed',1.2,[5,4]);if(s>0)ar(xx,Y-r+28,xx,Y-r+42,'#7c3aed',1.2);else ar(xx,Y+r-28,xx,Y+r-42,'#7c3aed',1.2);}
rc(X-r-6,Y-7,14,14,'#f59e0b','#92400e');rc(X+r-8,Y-7,14,14,'#f59e0b','#92400e');
for(var j=0;j<ch.length;j++){var c=ch[j],dir=c.q*s,xx=X+dir*c.p*(r-14),yy=Y+c.y*(r-20)*Math.sqrt(1-c.p*c.p*0.5);L(c.q>0?'+':'−',xx,yy,15,c.q>0?'#b02a52':'#1e63b8','center',1);}
var e=E()*s;L('E = '+m(e,3)+' mV',X,Y+r+52,14,'#1a2333','center',1);ln(X-r,Y+r+36,X+r,Y+r+36,'#94a3b8',1);
mk(1,244,cy-R-27);mk(2,240,cy-34);mk(3,604,Y-26);mk(4,X+50,Y-r+6);mk(5,70,cy+R-22);}
"""

S['vortex-flow-meter'] = r"""
var cy=150,R=70,N=110,pt=[],vx=[],acc=0,side=1;for(var i=0;i<N;i++)pt.push({x:20+Math.random()*600,y:Math.random()*2-1});
function f(){return 0.2*P.v/(P.d/1000);}
function fv(){return clamp(f()*0.08,0.5,3.5);}
function bh(){return P.d*0.9;}
function upd(){o('f',m(f(),1)+' Hz');o('per',m(1000/f(),1)+' ms');o('vel',m(P.v,1)+' m/s');}
function step(dt){var v=P.v*16+10;for(var i=0;i<N;i++){var p=pt[i];p.x+=v*dt;if(p.x>620){p.x=20;p.y=Math.random()*2-1;}}
acc+=dt*fv();if(acc>=1){acc=0;side=-side;vx.push({x:232,y:cy+side*(bh()/2+4),s:side,r:5});}
for(var k=vx.length-1;k>=0;k--){var q=vx[k];q.x+=v*0.8*dt;q.r=Math.min(16,q.r+dt*12);q.y+=(cy+q.s*R*0.35-q.y)*dt*0.6;if(q.x>630)vx.splice(k,1);}}
function draw(){pipe(20,620,cy,R);var h=bh()/2;
C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i],y=cy+p.y*R*0.9;if(p.x>186&&p.x<236&&Math.abs(y-cy)<h+5)y=cy+(p.y<0?-1:1)*(h+5+Math.abs(p.y)*(R*0.9-h-5));C.fillRect(p.x-1.5,y-1.5,3,3);}
for(var k=0;k<vx.length;k++){var q=vx[k],a=Math.max(0,1-(q.x-232)/400);C.strokeStyle='rgba(217,98,43,'+a+')';C.lineWidth=2;for(var n=0;n<2;n++){C.beginPath();var st=T*6*q.s+n*Math.PI;C.arc(q.x,q.y,q.r*(n?0.55:1),st,st+Math.PI*1.3);C.stroke();}}
C.fillStyle='#475569';C.beginPath();C.moveTo(200,cy-h-6);C.lineTo(226,cy-h);C.lineTo(226,cy+h);C.lineTo(200,cy+h+6);C.closePath();C.fill();
rc(228,cy-5,10,10,'#f59e0b','#92400e');ar(40,cy,92,cy,'#1a2333',2);
var x0=330,x1=620,y0=300;rc(x0,y0-36,x1-x0,72,'#f6f8fc','#dde3ee',8);L('Sensor signal',x0+8,y0-26,11,'#5b6576','left');C.strokeStyle='#1d7a46';C.lineWidth=2;C.beginPath();for(var x=x0+4;x<=x1-4;x+=2){var tt=T-(x1-x)/145,y=y0+4+20*Math.sin(2*Math.PI*fv()/2*tt*2);if(x==x0+4)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
L('Vortex frequency f = St × v ÷ d',30,y0,13,'#1a2333','left',1);L('Animation slowed for viewing',30,y0+22,11,'#5b6576','left');
mk(1,190,cy-h-20);mk(2,330,cy-R+22);mk(3,252,cy+20);mk(4,x1-14,y0-26);}
"""

S['coriolis-flow-meter'] = r"""
var path=[],N=40,fp=[];for(var i=0;i<N;i++)fp.push(i/N);
function phi(){return P.flow/100*0.55;}
function freq(){return 100*Math.sqrt(3000/(2000+P.rho));}
function upd(){o('f',m(freq(),1)+' Hz');o('dt',m(P.flow*0.4,1)+' µs');o('rho',m(P.rho,0)+' kg/m³');o('mf',m(P.flow,0)+' %');}
function step(dt){for(var i=0;i<N;i++){fp[i]+=dt*P.flow/100*0.12;if(fp[i]>1)fp[i]-=1;}}
function dx(y,side){var h=(305-y)/215,w=2*Math.PI*1.1*T;return 16*h*Math.sin(w+side*phi());}
function build(){path=[];var y,x;for(y=305;y>=90;y-=5)path.push([190+dx(y,1),y]);var a=dx(90,1),b=dx(90,-1);for(x=195;x<=445;x+=5){var u=(x-190)/260;path.push([x+a+(b-a)*u,90]);}for(y=90;y<=305;y+=5)path.push([450+dx(y,-1),y]);}
function draw(){build();rc(20,308,140,22,'#9aa5b8');rc(480,308,140,22,'#9aa5b8');rc(150,300,340,38,'#64748b',null,6);
L('Inlet',60,346,12,'#5b6576');L('Outlet',580,346,12,'#5b6576');
C.lineJoin='round';C.lineCap='round';C.strokeStyle='#94a3b8';C.lineWidth=16;C.beginPath();path.forEach(function(p,i){if(i)C.lineTo(p[0],p[1]);else C.moveTo(p[0],p[1]);});C.stroke();
C.strokeStyle='#dbeafe';C.lineWidth=9;C.stroke();
C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=path[Math.floor(fp[i]*(path.length-1))];C.fillRect(p[0]-2,p[1]-2,4,4);}
var pl=path[Math.round((305-200)/5)],pr=path[path.length-1-Math.round((305-200)/5)];
rc(pl[0]-26,pl[1]-9,16,18,'#1d7a46');rc(pr[0]+10,pr[1]-9,16,18,'#d9622b');var tp=path[Math.round(path.length/2)];rc(tp[0]-12,tp[1]-30,24,16,'#7c3aed');
var x0=478,x1=632,y0=40,y1=170;rc(x0,y0,x1-x0,y1-y0,'#f6f8fc','#dde3ee',8);L('Pickoff signals',x0+8,y0+12,11,'#5b6576','left');
var w=2*Math.PI*1.1;[[1,'#1d7a46',80],[-1,'#d9622b',130]].forEach(function(s){C.strokeStyle=s[1];C.lineWidth=2;C.beginPath();for(var x=x0+6;x<=x1-6;x+=2){var tt=T-(x1-x)/120,y=s[2]+18*Math.sin(w*tt+s[0]*phi());if(x==x0+6)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();});
L('Inlet',x0+8,y0+26,10,'#1d7a46','left',1);L('Outlet',x0+8,y0+108,10,'#d9622b','left',1);
L('Twist and phase shift exaggerated',30,22,11,'#5b6576','left');
mk(1,320,112);mk(2,tp[0]+24,tp[1]-26);mk(3,pl[0]-38,pl[1]);mk(4,pr[0]+40,pr[1]);mk(5,x1-14,y1-14);}
"""

S['ultrasonic-flow-meter'] = r"""
var cy=165,R=75,N=90,pt=[],ph=0;for(var i=0;i<N;i++)pt.push({x:20+Math.random()*600,y:Math.random()*2-1});
var ax=200,ay=cy-R,bx=200+2*R,by=cy+R;
function tt(){var Dm=P.d/1000,Lp=Dm/Math.sin(Math.PI/4),c=P.c,vc=P.v*Math.cos(Math.PI/4);return{L:Lp,dn:Lp/(c+vc),up:Lp/(c-vc)};}
function upd(){var t=tt();o('dn',m(t.dn*1e6,3)+' µs');o('up',m(t.up*1e6,3)+' µs');o('dt',m((t.up-t.dn)*1e9,1)+' ns');var q=P.v*Math.PI*Math.pow(P.d/1000,2)/4*3600;o('q',m(q,q<100?1:0)+' m³/h');}
function step(dt){var v=P.v*14+5;for(var i=0;i<N;i++){var p=pt[i];p.x+=v*dt;if(p.x>620){p.x=20;p.y=Math.random()*2-1;}}ph=(ph+dt/2.6)%1;}
function draw(){pipe(20,620,cy,R);C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i];C.fillRect(p.x-1.5,cy+p.y*R*0.9-1.5,3,3);}
ln(ax,ay,bx,by,'#94a3b8',1.5,[6,5]);rc(ax-16,ay-30,32,18,'#7c3aed',null,4);rc(bx-16,by+12,32,18,'#7c3aed',null,4);L('A',ax,ay-21,12,'#fff','center',1);L('B',bx,by+21,12,'#fff','center',1);
var e=clamp(P.v/10,0,1)*0.3,u,col;if(ph<0.45){u=clamp(ph/(0.45*(1-e)),0,1);col='#1d7a46';px=ax+(bx-ax)*u;py=ay+(by-ay)*u;}else if(ph>0.5&&ph<0.95){u=clamp((ph-0.5)/(0.45*(1+e)),0,1);col='#d9622b';px=bx+(ax-bx)*u;py=by+(ay-by)*u;}else{u=-1;}
if(u>=0&&u<1){for(var k=3;k>0;k--)ci(px,py,4+k*4,null,col,1.2);ci(px,py,4,col);}
ar(40,cy,92,cy,'#1a2333',2);
var t=tt(),x0=200,y0=282,base=240,dx=clamp((t.up-t.dn)/t.dn*1500,0,90);
L('A to B (with flow)',30,y0,12,'#1d7a46','left',1);rc(x0,y0-7,base-dx/2,14,'#1d7a46',null,3);
L('B to A (against flow)',30,y0+30,12,'#d9622b','left',1);rc(x0,y0+23,base+dx/2,14,'#d9622b',null,3);
L('Time difference exaggerated',x0,y0+58,11,'#5b6576','left');
var px,py;mk(1,ax+30,ay-21);mk(2,bx+30,by+21);mk(3,(ax+bx)/2+16,cy-10);mk(4,66,cy+R-20);}
"""

S['turbine-flow-meter'] = r"""
var cy=165,R=70,N=100,pt=[],rot=0,ev=[],tot=0,lastTop=false;for(var i=0;i<N;i++)pt.push({x:20+Math.random()*600,y:Math.random()*2-1});
function fq(){return P.k*P.q/3.6;}
function upd(){o('f',m(fq(),1)+' Hz');o('ppm',m(fq()*60,0));o('q',m(P.q,1)+' m³/h');}
function step(dt){var v=P.q*1.6+6;for(var i=0;i<N;i++){var p=pt[i];p.x+=v*dt;if(p.x>620){p.x=20;p.y=Math.random()*2-1;}}
var w=P.q/100*9;rot+=w*dt;tot+=P.q/3.6*dt;o('tot',m(tot,1)+' L');
var top=false;for(var k=0;k<6;k++){var a=rot+k*Math.PI/3;if(Math.cos(a)>0.97&&Math.sin(a)>0)top=true;}if(top&&!lastTop)ev.push(T);lastTop=top;while(ev.length&&T-ev[0]>3)ev.shift();}
function draw(){pipe(20,620,cy,R);C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i],y=cy+p.y*R*0.9;if(p.x>262&&p.x<380&&Math.abs(y-cy)<17)continue;C.fillRect(p.x-1.5,y-1.5,3,3);}
for(var s=0;s<2;s++){var xs=s?470:120;for(var k=-2;k<=2;k++)ln(xs,cy+k*26,xs+60,cy+k*26,'#64748b',2.5);}
ln(250,cy-R,262,cy,'#64748b',3);ln(250,cy+R,262,cy,'#64748b',3);ln(392,cy-R,380,cy,'#64748b',3);ln(392,cy+R,380,cy,'#64748b',3);
for(var k=0;k<6;k++){var a=rot+k*Math.PI/3;if(Math.sin(a)<=0){var yt=cy+(R-6)*Math.cos(a),yh=cy+15*Math.cos(a);C.fillStyle='#cbd5e1';C.beginPath();C.moveTo(312,yh);C.lineTo(330,yh);C.lineTo(336,yt);C.lineTo(318,yt);C.closePath();C.fill();}}
C.fillStyle='#475569';C.beginPath();C.moveTo(262,cy);C.quadraticCurveTo(280,cy-17,300,cy-17);C.lineTo(340,cy-17);C.quadraticCurveTo(362,cy-17,380,cy);C.quadraticCurveTo(362,cy+17,340,cy+17);C.lineTo(300,cy+17);C.quadraticCurveTo(280,cy+17,262,cy);C.fill();
for(var k=0;k<6;k++){var a=rot+k*Math.PI/3;if(Math.sin(a)>0){var yt=cy+(R-6)*Math.cos(a),yh=cy+15*Math.cos(a);C.fillStyle='#1e63b8';C.beginPath();C.moveTo(312,yh);C.lineTo(330,yh);C.lineTo(336,yt);C.lineTo(318,yt);C.closePath();C.fill();}}
rc(306,cy-R-40,34,30,'#1a2333',null,4);L('N S',323,cy-R-25,10,'#fff','center',1);ar(40,cy,92,cy,'#1a2333',2);
var x0=120,x1=620,y0=300;rc(x0,y0-34,x1-x0,68,'#f6f8fc','#dde3ee',8);L('Pickup pulses (last 3 s)',x0+8,y0-24,11,'#5b6576','left');
C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();C.moveTo(x0+6,y0+20);var sc=(x1-x0-12)/3;ev.forEach(function(t){var x=x1-6-(T-t)*sc;C.lineTo(x,y0+20);C.lineTo(x,y0-6);C.lineTo(x+3,y0-6);C.lineTo(x+3,y0+20);});C.lineTo(x1-6,y0+20);C.stroke();
L('Rotor speed slowed for viewing',30,22,11,'#5b6576','left');
mk(1,350,cy+R-18);mk(2,356,cy-R-25);mk(3,150,cy-R+14);mk(4,232,cy+R-22);mk(5,x1-14,y0-24);}
"""

S['dp-level-measurement'] = r"""
var px=260/5.5,yb=312;
function pr(){return P.sg*1000*9.80665*P.h/1000;}
function span(){return 1000*9.80665*5/1000;}
function ma(){return clamp(4+16*pr()/span(),3.8,20.5);}
function upd(){o('p',m(pr(),2)+' kPa ('+m(pr()*10,1)+' mbar)');o('ma',m(ma(),2)+' mA');var ind=(ma()-4)/16*5;o('ind',m(ind,2)+' m');o('err',m(ind-P.h,2)+' m');}
function step(dt){}
function draw(){rc(110,40,200,290,null,'#475569');var top=yb-P.h*px,sg=clamp((P.sg-0.6)/0.8,0,1);var col='rgb('+Math.round(150-110*sg)+','+Math.round(200-110*sg)+','+Math.round(250-70*sg)+')';
rc(112,top,196,328-top,col);for(var k=0;k<4;k++){var yy=top+4+3*Math.sin(T*2+k);}
ln(112,top,308,top,'#1e3a8a',2);for(var mm=0;mm<=5;mm++){var y=yb-mm*px;ln(110,y,122,y,'#475569',1);L(mm+' m',104,y,11,'#5b6576','right');}
ar(200,top+6,200,yb-4,'#ffffff',2);ar(200,yb-4,200,top+6,'#ffffff',2);L('h = '+m(P.h,2)+' m',214,(top+yb)/2,13,top<yb-30?'#fff':'#1a2333','left',1);
ln(310,yb,420,yb,'#b02a52',4);rc(420,282,84,60,'#1a2333',null,8);L('DP',438,296,12,'#fff','center',1);rc(452,300,46,22,'#bbf7d0',null,3);L(m(ma(),1),475,311,12,'#14532d','center',1);L('H',414,yb-10,11,'#b02a52','right',1);
ln(490,282,490,236,'#1e63b8',3);ln(480,236,500,236,'#1e63b8',3);L('L vented',474,236,11,'#1e63b8','right',1);
var bx=540,by=330,bh=5*px;rc(bx,by-bh,26,bh,'#f1f5f9','#cbd5e1');rc(bx,by-P.h*px,26,P.h*px,'#1e63b8');var ind=(ma()-4)/16*5;rc(bx+34,by-bh,26,bh,'#f1f5f9','#cbd5e1');rc(bx+34,by-clamp(ind,0,5.5)*px,26,clamp(ind,0,5.5)*px,'#d9622b');
L('Actual',bx+13,by+14,10,'#1e63b8','center',1);L('Shown',bx+47,by+14,10,'#d9622b','center',1);
L('Calibrated: 0 to 5 m at SG 1.0',30,22,11,'#5b6576','left');
mk(1,128,58);mk(2,340,yb+18);mk(3,512,258);mk(4,520,296);mk(5,250,(top+yb)/2+20);}
"""

S['radar-level-transmitter'] = r"""
var ph=0,yr=90,sc=24;
function d(){return 10-P.l;}
function rf(){var s=Math.sqrt(P.er);return Math.pow((s-1)/(s+1),2);}
function upd(){o('d',m(d(),2)+' m');o('tof',m(2*d()/299792458*1e9,2)+' ns');o('l',m(P.l,2)+' m');o('rf',m(rf()*100,1)+' %');}
function step(dt){ph=(ph+dt/1.8)%1;}
function draw(){var ys=330-P.l*sc;rc(160,yr,280,240,null,'#475569');rc(162,ys,276,330-ys-2,'#bfdbfe');ln(162,ys,438,ys,'#1e3a8a',2);
rc(286,yr-14,28,14,'#64748b');rc(268,28,64,34,'#1a2333',null,6);L('Radar',300,45,11,'#fff','center',1);C.fillStyle='#94a3b8';C.beginPath();C.moveTo(290,yr);C.lineTo(310,yr);C.lineTo(322,yr+30);C.lineTo(278,yr+30);C.closePath();C.fill();
var y0=yr+30,dist=ys-y0;if(ph<0.5){var u=ph/0.5,y=y0+dist*u;for(var k=0;k<3;k++){var yy=y-k*10;if(yy<y0)continue;C.strokeStyle='rgba(124,58,237,'+(0.9-k*0.25)+')';C.lineWidth=2.5;C.beginPath();C.arc(300,yy-30,40+((yy-y0)*0.25),Math.PI*0.3,Math.PI*0.7);C.stroke();}}
else{var u=(ph-0.5)/0.5,y=ys-dist*u,a=0.25+rf()*0.75;for(var k=0;k<3;k++){var yy=y+k*10;if(yy>ys)continue;C.strokeStyle='rgba(217,98,43,'+(a-k*0.2)+')';C.lineWidth=2.5;C.beginPath();C.arc(300,yy+30,40+((ys-yy)*0.2),Math.PI*1.3,Math.PI*1.7);C.stroke();}}
ln(450,yr,450,ys,'#1a2333',1,[4,3]);ar(450,yr+4,450,ys-2,'#1a2333',1.2);L('d',458,(yr+ys)/2,13,'#1a2333','left',1);
var x0=500,x1=630;rc(x0,yr,x1-x0,240,'#f6f8fc','#dde3ee',8);L('Echo curve',x0+6,yr-12,11,'#5b6576','left',1);C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();for(var y=yr+4;y<=326;y+=2){var dd=(y-yr)/sc,amp=0.05+0.35*Math.exp(-Math.pow(dd/0.4,2))+(0.15+0.75*rf())*Math.exp(-Math.pow((dd-d())/0.25,2));var x=x0+6+amp*(x1-x0-12);if(y==yr+4)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
L('Tank height 10 m, reference at flange',30,22,11,'#5b6576','left');
mk(1,340,yr+14);mk(2,360,y0+40);mk(3,x1-14,ys);mk(4,180,ys-14);mk(5,346,40);}
"""

S['displacer-level-transmitter'] = r"""
var Dd=0.0762,Ld=0.356,Wn=2.2*9.80665,top=120,bot=300;
function sub(){return P.lvl/100*Ld;}
function Fb(){return P.sg*1000*9.80665*Math.PI/4*Dd*Dd*sub();}
function Fmax(){return 1000*9.80665*Math.PI/4*Dd*Dd*Ld;}
function upd(){o('sub',m(sub()*1000,0)+' mm');o('fb',m(Fb(),2)+' N');o('aw',m(Wn-Fb(),2)+' N');var ma=clamp(4+16*Fb()/Fmax(),3.8,20.5);o('ma',m(ma,2)+' mA');}
function step(dt){}
function draw(){var ys=bot-P.lvl/100*(bot-top),lift=Fb()/Fmax()*6;
rc(30,60,170,270,null,'#475569');rc(32,ys,166,328-ys,'#bfdbfe');rc(200,96,60,12,'#9aa5b8');rc(200,296,60,12,'#9aa5b8');rc(260,70,80,260,null,'#475569');rc(262,ys,76,328-ys,'#bfdbfe');rc(262,98,76,ys-98>0?0:0,'#bfdbfe');ln(32,ys,198,ys,'#1e3a8a',2);ln(262,ys,338,ys,'#1e3a8a',2);
var yt=top-lift,yb=bot-lift;ln(300,74,300,yt,'#334155',2);rc(285,yt,30,yb-yt,'#cbd5e1','#475569',4);
var fb=Fb()/Fmax();if(fb>0.02){ar(300,yb-6,300,yb-6-50*fb,'#1d7a46',3);}ar(318,(yt+yb)/2,318,(yt+yb)/2+40,'#b02a52',2.5);
rc(290,40,140,30,'#64748b',null,4);ci(300,55,7,'#334155');var ang=-0.08*fb;ln(300,55,300+40*Math.cos(Math.PI/2+ang),55+40*Math.sin(Math.PI/2+ang)-40,'#334155',2);
rc(430,22,100,66,'#1a2333',null,8);L('Transmitter',480,38,11,'#fff','center',1);rc(446,50,68,24,'#bbf7d0',null,3);L(m(clamp(4+16*fb*P.sg/P.sg,3.8,20.5),2)+' mA',480,62,12,'#14532d','center',1);
L('Buoyancy',335,yb-30,11,'#1d7a46','left',1);L('Weight',335,(yt+yb)/2+30,11,'#b02a52','left',1);
L('Example: 76 mm × 356 mm displacer, 2.2 kg',30,22,11,'#5b6576','left');
mk(1,270,(yt+yb)/2);mk(2,350,300);mk(3,410,55);mk(4,60,ys-14);mk(5,545,40);}
"""

S['bourdon-tube-pressure-gauge'] = r"""
var X=420,Y=168,RD=130,pm=10,sp=0;
function pf(){return clamp(sp,0,10.6)/pm;}
function upd(){var p=P.p;o('p',m(p,1)+' bar');o('pc',m(p/pm*100,0)+' %');o('st',p>pm?'Over range':(p>=pm*0.25&&p<=pm*0.75?'Good working band':(p<pm*0.25?'Low in range':'High in range')));}
function step(dt){sp+=(P.p-sp)*(1-Math.exp(-dt/0.25));}
function tip(f){var sw=250-16*f,a=(100+sw)*Math.PI/180,r=78+9*f;return[X+r*Math.cos(a),Y+10+r*Math.sin(a)];}
function draw(){var f=pf();rc(20,326,385,18,'#9aa5b8');rc(404,300,32,44,'#64748b');ar(60,335,120,335,'#1a2333',2);L('Pressure in',90,316,11,'#1a2333','center',1);
ci(X,Y,RD+10,'#1a2333');ci(X,Y,RD,'rgba(248,250,252,0.94)');
for(var i=0;i<=50;i++){var a=(135+270*i/50)*Math.PI/180,r1=RD-6,r2=i%5?RD-13:RD-20;ln(X+r1*Math.cos(a),Y+r1*Math.sin(a),X+r2*Math.cos(a),Y+r2*Math.sin(a),'#1a2333',i%5?1:2);if(i%5==0)L(String(i/5),X+(RD-32)*Math.cos(a),Y+(RD-32)*Math.sin(a),12,'#1a2333','center',1);}
C.strokeStyle='rgba(29,125,70,.35)';C.lineWidth=8;C.beginPath();C.arc(X,Y,RD-3,(135+67.5)*Math.PI/180,(135+202.5)*Math.PI/180);C.stroke();
L('bar',X,Y+52,12,'#5b6576','center',1);
var b0=[X+78*Math.cos(100*Math.PI/180),Y+10+78*Math.sin(100*Math.PI/180)];C.lineCap='round';C.strokeStyle='#b45309';C.lineWidth=9;C.beginPath();C.moveTo(X,300);C.lineTo(b0[0],b0[1]);C.stroke();C.strokeStyle='#fde68a';C.lineWidth=4;C.stroke();C.strokeStyle='#b45309';C.lineWidth=9;C.beginPath();var sw=250-16*f;for(var u=0;u<=1.001;u+=0.02){var a=(100+sw*u)*Math.PI/180,r=78+9*f*u;var x=X+r*Math.cos(a),y=Y+10+r*Math.sin(a);if(u==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();C.strokeStyle='#fde68a';C.lineWidth=4;C.stroke();
var t=tip(f);ci(t[0],t[1],5,'#92400e');var sx=X+34,sy=Y+44;ln(t[0],t[1],sx,sy,'#334155',2.5);ci(sx,sy,4,'#334155');ln(sx,sy,X+6,Y+6,'#64748b',3);ci(X,Y,10,'#94a3b8','#334155');
var pa=(135+270*f)*Math.PI/180;ln(X-14*Math.cos(pa),Y-14*Math.sin(pa),X+(RD-18)*Math.cos(pa),Y+(RD-18)*Math.sin(pa),'#b02a52',3.5);ci(X,Y,6,'#b02a52');
L('Cutaway view: tube movement exaggerated',30,22,11,'#5b6576','left');
mk(1,X-58,Y+58);mk(2,450,322);mk(3,(t[0]+sx)/2+12,(t[1]+sy)/2+14);mk(4,X+28,Y-22);mk(5,X+(RD-50)*Math.cos(pa)+14,Y+(RD-50)*Math.sin(pa));mk(6,X+RD-10,Y-RD+20);}
"""

S['thermocouple'] = r"""
var KT=[@@K@@],K0=-20,N=26,el=[];for(var i=0;i<N;i++)el.push(Math.random());
function emf(t){t=clamp(t,-20,1300);var i=Math.floor(t-K0),f=t-K0-i;if(i>=KT.length-1)return KT[KT.length-1];return KT[i]+(KT[i+1]-KT[i])*f;}
function tmp(e){for(var i=0;i<KT.length-1;i++){if(e>=KT[i]&&e<=KT[i+1])return K0+i+(e-KT[i])/(KT[i+1]-KT[i]);}return e<KT[0]?-20:1300;}
function upd(){var eh=emf(P.th),ec=emf(P.tc),em=eh-ec;o('eh',m(eh,3)+' mV');o('ec',m(ec,3)+' mV');o('em',m(em,3)+' mV');o('no',m(tmp(em),1)+' °C');o('yes',m(tmp(em+ec),1)+' °C');}
function step(dt){var s=(emf(P.th)-emf(P.tc))/50;for(var i=0;i<N;i++){el[i]+=dt*s*0.6;if(el[i]>1)el[i]-=1;if(el[i]<0)el[i]+=1;}}
function draw(){var h=clamp(P.th/1200,0,1);var g='rgb('+Math.round(90+165*h)+','+Math.round(30+150*h*h)+','+Math.round(20+40*h*h*h)+')';
rc(20,80,160,200,'#1f2937',null,10);rc(32,92,136,176,g,null,8);L('Hot zone',100,104,12,'#fff','center',1);L(m(P.th,0)+' °C',100,250,15,'#fff','center',1);
ci(120,180,8,'#fbbf24','#1a2333',2);
var xa=120,xb=380;C.lineCap='round';ln(xa,180,150,170,'#16a34a',5);ln(150,170,xb,170,'#16a34a',5);ln(xa,180,150,190,'#475569',7);ln(150,190,xb,190,'#f8fafc',5);
rc(360,122,80,118,'#e2e8f0','#475569',8);L('Terminals',400,136,11,'#1a2333','center',1);L(m(P.tc,0)+' °C',400,224,13,'#1a2333','center',1);rc(376,162,48,36,'#cbd5e1','#64748b',4);ci(392,206,0);rc(426,200,10,14,'#7c3aed');
ln(424,170,500,150,'#b45309',3);ln(424,190,500,210,'#b45309',3);
rc(500,110,128,140,'#1a2333',null,10);L('Without CJC',564,132,11,'#fca5a5','center',1);var em=emf(P.th)-emf(P.tc);L(m(tmp(em),1)+' °C',564,154,16,'#fff','center',1);L('With CJC',564,190,11,'#86efac','center',1);L(m(tmp(em+emf(P.tc)),1)+' °C',564,212,16,'#fff','center',1);L(m(em,3)+' mV',564,238,11,'#94a3b8','center');
C.fillStyle='#fde047';for(var i=0;i<N;i++){var u=el[i],x=150+(xb-150)*u;C.fillRect(x-2,i%2?168:188,4,4);}
L('Type K (IEC green and white)',150,150,11,'#5b6576','left');
mk(1,120,206);mk(2,300,210);mk(3,400,184);mk(4,448,207);mk(5,616,122);}
"""

S['valve-positioner'] = r"""
var pos=0.5,N=70,pt=[];for(var i=0;i<N;i++)pt.push({x:20+Math.random()*600,y:Math.random()*2-1});
function spt(){return clamp((P.ma-4)/16,0,1);}
function upd(){o('sp',m(spt()*100,1)+' %');o('ma',m(P.ma,1)+' mA');}
function step(dt){pos+=(spt()-pos)*(1-Math.exp(-dt/0.6));var v=pos*90+2;for(var i=0;i<N;i++){var p=pt[i];p.x+=v*dt;if(p.x>620){p.x=20;p.y=Math.random()*2-1;}}o('pos',m(pos*100,1)+' %');o('pa',m(0.2+0.8*pos,2)+' bar');}
function draw(){var cy=300,R=26,lift=pos*36,mv=Math.abs(spt()-pos)>0.004;pipe(20,620,cy,R);
C.fillStyle='#1e63b8';for(var i=0;i<N;i++){var p=pt[i];if(pos<0.02&&p.x>300&&p.x<340)continue;C.fillRect(p.x-1.5,cy+p.y*R*0.8-1.5,3,3);}
ci(320,cy,46,'#64748b');ci(320,cy,38,'#e6f0fd');rc(296,cy+2,48,6,'#334155');rc(306,cy-12-lift,28,14,'#1a2333',null,4);
ln(320,cy-12-lift,320,120-lift,'#475569',4);rc(300,248,40,12,'#64748b');ln(292,140,292,248,'#64748b',5);ln(348,140,348,248,'#64748b',5);
C.fillStyle='#94a3b8';C.beginPath();C.ellipse(320,108,82,34,0,Math.PI,0);C.fill();rc(238,108,164,30,'#94a3b8',null,4);ln(242,124-lift*0.3,398,124-lift*0.3,'#1a2333',3);
for(var k=0;k<5;k++){var y1=84+k*7-lift*0.2;ln(300,y1,340,y1+4,'#334155',1.5);}L('Spring',320,62,10,'#1a2333','center',1);
rc(430,170,96,70,'#1a2333',null,8);L('Positioner',478,186,11,'#fff','center',1);rc(444,198,68,24,'#bbf7d0',null,3);L(m(pos*100,0)+' %',478,210,12,'#14532d','center',1);
ln(320,206-lift,430,205,'#d9622b',3);ci(320,206-lift,4,'#d9622b');
var pa=0.2+0.8*pos;C.setLineDash(mv?[8,6]:[]);C.lineDashOffset=-T*30;C.strokeStyle='rgba(30,99,184,'+(0.35+0.6*pos)+')';C.lineWidth=4;C.beginPath();C.moveTo(430,180);C.lineTo(410,180);C.lineTo(410,134);C.lineTo(402,134);C.stroke();C.setLineDash([]);C.lineDashOffset=0;
ln(526,226,600,226,'#1e63b8',3);L('Supply air',604,212,11,'#1e63b8','right',1);
rc(480,24,140,48,'#f6f8fc','#dde3ee',8);L('Control signal',550,38,11,'#5b6576','center');L(m(P.ma,1)+' mA',550,58,15,'#1a2333','center',1);ln(500,72,470,170,'#16a34a',2.5);
L('Air to open, spring to close',30,22,11,'#5b6576','left');
mk(1,540,180);mk(2,226,92);mk(3,372,206-lift);mk(4,350,cy+30);mk(5,580,244);mk(6,456,100);}
"""
