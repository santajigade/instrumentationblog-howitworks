var PER=4.8,ph=0,NE=72,TR=1.6;
var X0=80,XB0=250,XB1=310,X1=540,Y0=100,Y1=200;
function hsh(a,b){var s=Math.sin(a*127.1+b*311.7)*43758.5453;return s-Math.floor(s);}
function vbe(t){return 0.7+0.01*Math.sin(2*Math.PI*t/PER);}
function ie(t){return 10*Math.exp((vbe(t)-0.7)/0.026);}
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function bat(x,y,lab,sub){ln(x+6,y-16,x+6,y+16,'#1f2733',3);ln(x-6,y-9,x-6,y+9,'#1f2733',5);}
function draw(){
var IE=ie(ph),IC=0.98*IE,IB=IE-IC,v=vbe(ph);
L('Electrons (blue) slowed down; arrows show conventional current; recombination exaggerated',20,22,11,'#5b6576','left');
// regions
rc(X0,Y0,XB0-X0,Y1-Y0,'#bfdbfe');rc(XB0,Y0,XB1-XB0,Y1-Y0,'#fbcfe8');rc(XB1,Y0,X1-XB1,Y1-Y0,'#dbeafe');
// depletion layers: EB narrow (forward), CB wide (reverse)
rc(XB0-3,Y0,7,Y1-Y0,'rgba(100,116,139,0.45)');rc(XB1-14,Y0,34,Y1-Y0,'rgba(100,116,139,0.35)');
C.strokeStyle='#475569';C.lineWidth=1.5;C.strokeRect(X0,Y0,X1-X0,Y1-Y0);
L('Emitter',165,70,13,'#1e3a8a','center',1);L('N+, heavily doped',165,86,11,'#1e3a8a','center');
L('Base',280,70,13,'#9d174d','center',1);L('P, thin, light',280,86,11,'#9d174d','center');
L('Collector',425,70,13,'#1e3a8a','center',1);L('N, moderately doped',425,86,11,'#1e3a8a','center');
// holes in base
for(var k=0;k<5;k++){var hx=258+k*8+3*Math.sin(2*Math.PI*ph/PER*(k+1)+k),hy=118+k*16+4*Math.cos(2*Math.PI*ph/PER*2+k);L('+',hx,hy,13,'#be185d','center',1);}
// electrons
for(var i=0;i<NE;i++){var w=ph/TR+i/NE,u=w%1,pass=Math.floor(w)%3,te=((ph-u*TR)%PER+PER)%PER;
if(hsh(i,pass)>ie(te)/14.7)continue;
var lane=Y0+18+hsh(i,7)*(Y1-Y0-30),rec=(i%12==5),x=X0+u*(X1-X0),y=lane,a=1;
if(rec){var xr=275;if(x>xr){var q=(x-xr)/60;if(q>1)continue;x=xr+6*q;y=lane+(Y1-6-lane)*q;a=1-q*0.8;}}
C.globalAlpha=a;ci(x,y,3.4,'#1d4ed8');L('−',x,y-0.5,9,'#fff','center',1);C.globalAlpha=1;}
// wires
ln(X0,150,50,150,'#334155',2.5);ln(50,150,50,300,'#334155',2.5);ln(280,Y1,280,300,'#334155',2.5);ln(X1,150,590,150,'#334155',2.5);ln(590,150,590,300,'#334155',2.5);
ln(50,300,159,300,'#334155',2.5);ln(171,300,280,300,'#334155',2.5);ln(280,300,429,300,'#334155',2.5);ln(441,300,590,300,'#334155',2.5);
bat(165,300);bat(435,300);
L('−',150,282,13,'#1f2733','center',1);L('+',182,282,13,'#dc2626','center',1);L('−',420,282,13,'#1f2733','center',1);L('+',452,282,13,'#dc2626','center',1);
L('VBE = '+v.toFixed(3)+' V',165,324,12,'#1f2733','center',1);L('VCB = 10 V',435,324,12,'#1f2733','center',1);
// junction labels
L('Forward biased',236,216,11,'#15803d','right',1);L('narrow depletion',236,230,11,'#15803d','right');
L('Reverse biased',336,216,11,'#b91c1c','left',1);L('wide depletion',336,230,11,'#b91c1c','left');
// currents (conventional)
ar(50,240,50,256,'#ea580c',2);L('IE = '+m(IE,1)+' mA',60,262,12,'#ea580c','left',1);
ar(280,256,280,240,'#ea580c',2);L('IB = '+m(IB,2)+' mA',290,262,12,'#ea580c','left',1);
ar(590,256,590,240,'#ea580c',2);L('IC = '+m(IC,1)+' mA',580,262,12,'#ea580c','right',1);
L('About 98 % of injected electrons reach the collector:  IE = IB + IC',320,348,12,'#334155','center',1);
mk(1,96,80);mk(2,280,48);mk(3,522,80);mk(4,250,194);mk(5,313,194);mk(6,268,286);
}
