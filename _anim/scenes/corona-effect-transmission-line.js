var PER=4.8,ph=0,CX=165,CY=205,RC=34,TH=0.78;
var BEADS=[0.3,1.25,2.1,2.9,3.7,4.6,5.5];
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function rnd(i){var x=Math.sin(i*127.1+11.7)*43758.5;return x-Math.floor(x);}
function draw(){
var u=(ph%2.4)/2.4,v=Math.sin(2*Math.PI*u),av=Math.abs(v),on=av>TH,pos=v>0;
L('One AC cycle slowed to 2.4 s; line shown above its critical voltage, as in foul weather',20,22,11,'#5b6576','left');
// field lines
for(var k=0;k<16;k++){var a=k*Math.PI/8;C.globalAlpha=0.15+0.6*av;var r1=pos?RC+6:RC+70,r2=pos?RC+70:RC+8;ar(CX+r1*Math.cos(a),CY+r1*Math.sin(a),CX+r2*Math.cos(a),CY+r2*Math.sin(a),pos?'#2563eb':'#9333ea',1.5);}C.globalAlpha=1;
// glow
if(on){var g=(av-TH)/(1-TH);if(pos){var gr=C.createRadialGradient(CX,CY,RC,CX,CY,RC+22+16*g);gr.addColorStop(0,'rgba(139,92,246,'+(0.35+0.5*g)+')');gr.addColorStop(1,'rgba(139,92,246,0)');C.fillStyle=gr;C.beginPath();C.arc(CX,CY,RC+40,0,2*Math.PI);C.fill();}
else{for(var b=0;b<BEADS.length;b++){var a=BEADS[b],bx=CX+(RC+4)*Math.cos(a),by=CY+(RC+4)*Math.sin(a);var gr=C.createRadialGradient(bx,by,0,bx,by,10+8*g);gr.addColorStop(0,'rgba(244,63,94,0.95)');gr.addColorStop(1,'rgba(244,63,94,0)');C.fillStyle=gr;C.beginPath();C.arc(bx,by,18+8*g,0,2*Math.PI);C.fill();}}
// electron avalanche particles
var g2=(av-TH)/(1-TH);for(var i=0;i<26;i++){var a=rnd(i)*2*Math.PI,s=((u*6+rnd(i+40))%1),rr=RC+4+s*26*(0.5+g2);C.globalAlpha=1-s;ci(CX+rr*Math.cos(a),CY+rr*Math.sin(a),2.2,'#f59e0b');}C.globalAlpha=1;}
// conductor (stranded look)
ci(CX,CY,RC,'#9ca3af','#374151',2);for(var k=0;k<6;k++){var a=k*Math.PI/3;ci(CX+18*Math.cos(a),CY+18*Math.sin(a),11,'#d1d5db','#6b7280',1);}ci(CX,CY,11,'#d1d5db','#6b7280',1);
L(on?(pos?'Positive half: uniform violet glow':'Negative half: reddish beads at rough spots'):'Field below breakdown: air insulates',CX,CY+RC+92,12,on?'#7c2d12':'#334155','center',1);
// waveform panel
var px=340,py=48,pw=280,phh=160,mid=py+80,A=48;rc(px,py,pw,phh,'#f8fafc','#94a3b8',8);
L('Conductor surface gradient',px+10,py+14,12,'#1f2733','left',1);
ln(px+10,mid,px+pw-10,mid,'#94a3b8',1);
C.fillStyle='rgba(139,92,246,0.16)';C.fillRect(px+10,mid-A,pw-20,A*(1-TH));C.fillStyle='rgba(244,63,94,0.14)';C.fillRect(px+10,mid+A*TH,pw-20,A*(1-TH));
ln(px+10,mid-A*TH,px+pw-10,mid-A*TH,'#dc2626',1.5,[5,4]);ln(px+10,mid+A*TH,px+pw-10,mid+A*TH,'#dc2626',1.5,[5,4]);
C.strokeStyle='#1e63b8';C.lineWidth=2.5;C.beginPath();for(var i=0;i<=120;i++){var x=px+10+(pw-20)*i/120,y=mid-A*Math.sin(2*Math.PI*i/120);if(i==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
var cx2=px+10+(pw-20)*u;ln(cx2,mid-A-6,cx2,mid+A+6,'#111827',1.5);ci(cx2,mid-A*v,5,on?'#dc2626':'#1e63b8');
L('Dashed: air breaks down, about 30 kV per cm peak',px+pw/2,py+phh-10,11,'#b91c1c','center');
// effects panel
var ey=218;rc(340,ey,280,130,'#f8fafc','#94a3b8',8);L('Effects while corona is active',350,ey+16,12,'#1f2733','left',1);
var eff=[['Hissing sound',0],['Visible glow',1],['Ozone smell',2],['Power loss',3],['Radio interference',4]];
for(var i=0;i<5;i++){var x=354+(i%2)*134,y=ey+42+Math.floor(i/2)*28;ci(x+6,y,7,on?'#f97316':'#e5e7eb','#475569',1.2);L(eff[i][0],x+18,y,12,on?'#7c2d12':'#64748b','left',on);}
L('Vc = m0 × δ × g0 × r × ln(d ÷ r)',480,ey+118,11,'#334155');
mk(1,CX,CY);mk(2,CX+RC+82,CY-30);mk(3,CX+RC+22,CY+RC+30);mk(4,px+24,mid-A*TH);mk(5,px+pw-14,py+14);mk(6,606,ey+16);
}
