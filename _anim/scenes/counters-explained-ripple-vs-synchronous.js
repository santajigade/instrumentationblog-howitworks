var PER=4.8,ph=0,TP=0.08;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function cnt(t){t=((t%PER)+PER)%PER;var n=0;for(var k=0;k<8;k++)if(0.3+0.6*k<=t)n++;return n%8;}
function clk(t){t=((t%PER)+PER)%PER;return (t%0.6)<0.3?1:0;}
function q(i,t){return (cnt(t-(i+1)*TP)>>i)&1;}
function tx(t){return 90+t/PER*530;}
function ff(x,n){rc(x,60,80,70,'#eef4fb','#1e3a8a',8);L('T FF'+n,x+40,95,13,'#1e3a8a','center',1);
L('T',x+10,78,11,'#334155','left');L('Q',x+70,78,11,'#334155','right');
C.strokeStyle='#334155';C.lineWidth=1.5;C.beginPath();C.moveTo(x,104);C.lineTo(x+9,112);C.lineTo(x,120);C.stroke();ci(x-5,112,4,'#fff','#334155',1.5);
ln(x-22,78,x,78,'#16a34a',2);L('1',x-26,78,11,'#16a34a','right',1);}
function led(x,y,v,lab){ci(x,y,10,v?'#facc15':'#e5e7eb','#475569',1.5);if(v){C.globalAlpha=.3;ci(x,y,16,'#fde047');C.globalAlpha=1;}L(lab+' = '+v,x+16,y,12,'#1f2733','left',1);}
function sig(v){return v?'#16a34a':'#94a3b8';}
function draw(){
var c=clk(ph),Q=[q(0,ph),q(1,ph),q(2,ph)],n=Q[0]+2*Q[1]+4*Q[2];
L('Falling edge triggered T flip flops; propagation delay greatly exaggerated',20,22,11,'#5b6576','left');
// clock source
rc(18,98,50,28,'#fff','#475569',6);C.strokeStyle=c?'#16a34a':'#475569';C.lineWidth=2;C.beginPath();C.moveTo(24,118);C.lineTo(32,118);C.lineTo(32,106);C.lineTo(44,106);C.lineTo(44,118);C.lineTo(56,118);C.lineTo(56,106);C.lineTo(62,106);C.stroke();
L('CLK',43,140,11,'#334155','center',1);
ln(68,112,105,112,sig(c),c?3:2);
ff(110,0);ff(270,1);ff(430,2);
// Q0 to FF1 clock, Q1 to FF2 clock
ln(190,78,230,78,sig(Q[0]),Q[0]?3:2);ln(230,78,230,112,sig(Q[0]),Q[0]?3:2);ln(230,112,265,112,sig(Q[0]),Q[0]?3:2);
ln(350,78,390,78,sig(Q[1]),Q[1]?3:2);ln(390,78,390,112,sig(Q[1]),Q[1]?3:2);ln(390,112,425,112,sig(Q[1]),Q[1]?3:2);
ln(510,78,540,78,sig(Q[2]),Q[2]?3:2);
ln(230,78,230,58,sig(Q[0]),2);ln(390,78,390,58,sig(Q[1]),2);ln(540,78,540,58,sig(Q[2]),2);
led(230,48,Q[0],'Q0');led(390,48,Q[1],'Q1');led(540,48,Q[2],'Q2');
// count readout
L('Count',598,92,12,'#334155','center',1);rc(572,102,52,40,'#1f2937',null,8);L(String(n),598,123,24,'#facc15','center',1);
L(Q[2]+''+Q[1]+''+Q[0],598,156,12,'#334155','center',1);
// timing diagram
var rows=['CLK','Q0','Q1','Q2'],by=[192,228,264,300];
rc(78,172,552,150,'#f8fafc','#e2e8f0',8);
for(var r=0;r<4;r++){L(rows[r],66,by[r],12,'#1f2733','right',1);C.strokeStyle=r?'#2563eb':'#334155';C.lineWidth=2;C.beginPath();
for(var k=0;k<=530;k++){var t=k/530*PER,v=r?q(r-1,t):clk(t),y=by[r]+(v?-11:11);if(k)C.lineTo(90+k,y);else C.moveTo(90+k,y);}C.stroke();}
for(var e=0;e<8;e++){var xe=tx(0.3+0.6*e);ln(xe,176,xe,318,'#cbd5e1',1,[2,4]);}
var cx=tx(ph);ln(cx,176,cx,318,'#d9622b',2);
mk(1,43,166);mk(2,150,148);mk(3,250,132);mk(4,tx(2.1+3*TP)+16,by[3]+3);mk(5,550,123);
}
