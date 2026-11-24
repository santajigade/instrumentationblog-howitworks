var PER=4.8,ph=0,hb=1,lb=1,eq=0,pH=100,pL=40,msg='';
function upd(){}
function rp(t,a,b){return sm((t-a)/(b-a));}
function step(dt){ph=(ph+dt)%PER;var t=ph;
hb=1-rp(t,0.4,0.8)+rp(t,3.2,3.6);lb=1-rp(t,0.8,1.2)+rp(t,3.6,4.0);eq=rp(t,1.2,1.6)-rp(t,2.8,3.2);
if(t<1.2){pH=100;pL=40;}else if(t<3.2){var e=rp(t,1.2,1.6);pH=100-30*e;pL=40+30*e;}else if(t<3.6){pH=70+30*rp(t,3.2,3.6);pL=70;}else{pH=100;pL=70-30*rp(t,3.6,4.0);}
msg=t<0.4?'Normal: blocks open, equalizer closed':t<0.8?'Close the high block valve':t<1.2?'Close the low block valve':t<1.6?'Open the equalizing valve':t<2.8?'Zero check: both sides equal':t<3.2?'Close the equalizing valve':t<3.6?'Open the high block valve':t<4.0?'Open the low block valve':'Back to normal measurement';}
function col(p){var u=clamp((p-40)/60,0,1);return 'rgb('+Math.round(147-110*u)+','+Math.round(197-138*u)+','+Math.round(253-75*u)+')';}
function valve(x,y,open,vert){var c=open>0.5?'#16a34a':'#dc2626';C.save();C.translate(x,y);if(vert)C.rotate(Math.PI/2);
C.fillStyle=c;C.strokeStyle='#1f2937';C.lineWidth=1.5;C.beginPath();C.moveTo(-14,-10);C.lineTo(14,10);C.lineTo(14,-10);C.lineTo(-14,10);C.closePath();C.fill();C.stroke();C.restore();
}
function draw(){
L('5 valve manifold zero check sequence; pressures in relative units',20,22,11,'#5b6576','left');
// process pipe with orifice
pipe(40,470,62,14,'#e0f2fe');rc(253,44,4,36,'#475569');
C.setLineDash([10,10]);C.lineDashOffset=-ph*25;C.strokeStyle='#38bdf8';C.lineWidth=3;C.beginPath();C.moveTo(40,62);C.lineTo(470,62);C.stroke();C.setLineDash([]);C.lineDashOffset=0;rc(52,54,40,16,'#e0f2fe');L('Flow',72,62,11,'#0369a1','center',1);
// impulse lines
var cH=col(pH*hb+100*(1-hb)>0?100:100),cL=col(40);
ln(200,76,200,170,col(100),6);ln(310,76,310,110,col(40),6);ln(310,110,420,110,col(40),6);ln(420,110,420,170,col(40),6);
// manifold block
rc(160,150,300,122,'#f1f5f9','#475569',10);L('Manifold block',310,166,11,'#475569','center',1);
// internal channels downstream of blocks
ln(200,200,200,290,col(pH),6);ln(420,200,420,290,col(pL),6);
var ce=eq>0.05?col((pH+pL)/2):'#e2e8f0';ln(200,215,420,215,ce,5);
ln(200,245,262,245,'#cbd5e1',4);ln(420,245,358,245,'#cbd5e1',4);
valve(200,185,hb,true);valve(420,185,lb,true);valve(310,215,eq,false);
valve(240,245,0,false);valve(380,245,0,false);L('Vent',272,246,11,'#475569','left',1);L('Vent',348,246,11,'#475569','right',1);
L('H',188,128,13,'#1e3a8a','center',1);L('L',432,128,13,'#0369a1','center',1);
// transmitter
rc(170,290,280,50,'#fff7ed','#c2410c',10);ci(200,315,14,col(pH),'#1f2937');ci(420,315,14,col(pL),'#1f2937');
L('DP transmitter',310,308,13,'#9a3412','center',1);
var dp=pH-pL;L('DP '+m(dp,0)+' %',310,326,13,'#1f2733','center',1);
// panel
rc(480,110,150,150,'#0f172a',null,10);L('Reading',555,130,12,'#94a3b8','center',1);L(m(dp,0)+' %',555,162,26,'#4ade80','center',1);
rc(495,190,120,12,'#334155',null,6);rc(495,190,120*dp/60,12,'#4ade80',null,6);
var w=msg.split(' '),l1='',l2='';for(var i=0;i<w.length;i++){if((l1+' '+w[i]).length<20&&!l2)l1+=(l1?' ':'')+w[i];else l2+=(l2?' ':'')+w[i];}
L(l1,555,222,11,'#e2e8f0','center',1);L(l2,555,240,11,'#e2e8f0','center',1);
L('Never open the equalizer while',555,286,11,'#b91c1c','center',1);L('both block valves are open',555,302,11,'#b91c1c','center',1);
mk(1,232,185);mk(2,388,185);mk(3,310,190);mk(4,240,267);mk(5,140,315);mk(6,255,100);
}
