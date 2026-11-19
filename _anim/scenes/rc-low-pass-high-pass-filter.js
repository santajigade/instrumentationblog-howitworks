var PER=4.8,ph=0;
var GL=0.995,PL=0.0997,GH=0.0995,PH=1.4711;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function res(x1,y,x2,c){var n=6,w=(x2-x1)/n;C.strokeStyle=c;C.lineWidth=2.5;C.beginPath();C.moveTo(x1,y);for(var i=0;i<n;i++){C.lineTo(x1+w*(i+0.25),y-8);C.lineTo(x1+w*(i+0.75),y+8);}C.lineTo(x2,y);C.stroke();}
function resV(x,y1,y2,c){var n=6,h=(y2-y1)/n;C.strokeStyle=c;C.lineWidth=2.5;C.beginPath();C.moveTo(x,y1);for(var i=0;i<n;i++){C.lineTo(x-8,y1+h*(i+0.25));C.lineTo(x+8,y1+h*(i+0.75));}C.lineTo(x,y2);C.stroke();}
function gnd(x,y){ln(x-12,y,x+12,y,'#334155',2.5);ln(x-8,y+5,x+8,y+5,'#334155',2);ln(x-4,y+10,x+4,y+10,'#334155',1.5);}
function src(x,y){ci(x,y,13,'#fff','#334155',2);C.strokeStyle='#2563eb';C.lineWidth=2;C.beginPath();for(var i=0;i<=16;i++){var u=i/16;var xx=x-8+16*u,yy=y-5*Math.sin(2*Math.PI*u+2*Math.PI*ph/PER*10);if(!i)C.moveTo(xx,yy);else C.lineTo(xx,yy);}C.stroke();}
// a slow tone at 0.1 fc and a fast tone at 10 fc; slow = 1 cycle per 4.8 s, fast = 10 cycles per 4.8 s
function trace(y0,a1,p1,a2,p2,col,lab,sub){
var x0=290,x1=620,w=x1-x0;
rc(x0,y0-30,w,60,'#f8fafc','#e2e8f0',6);ln(x0,y0,x1,y0,'#cbd5e1',1,[4,4]);
C.strokeStyle=col;C.lineWidth=2.5;C.beginPath();
for(var x=x0;x<=x1;x+=1.5){var tt=2*Math.PI*(ph/PER-(x-x0)/w);var v=a1*Math.sin(tt+p1)+a2*Math.sin(10*tt+p2);if(x==x0)C.moveTo(x,y0-v);else C.lineTo(x,y0-v);}
C.stroke();
L(lab,x0+2,y0-40,12,col,'left',1);
L(sub,x1-28,y0-40,11,'#475569','right');
}
function draw(){
L('Signals slowed down; slow tone at 0.1 fc and fast tone at 10 fc',20,22,11,'#5b6576','left');
// LPF schematic
var y=82;L('RC low pass filter',20,48,13,'#1f2733','left',1);
src(34,y+22);ln(34,y+9,34,y,'#334155',2.5);ln(34,y,70,y,'#334155',2.5);res(70,y,130,'#b45309');ln(130,y,240,y,'#334155',2.5);
ci(170,y,3.5,'#334155');ln(170,y,170,y+20,'#334155',2.5);ln(156,y+20,184,y+20,'#2563eb',3);ln(156,y+28,184,y+28,'#2563eb',3);ln(170,y+28,170,y+48,'#334155',2.5);gnd(170,y+48);
ln(34,y+35,34,y+48,'#334155',2.5);gnd(34,y+48);
ci(240,y,4,'#fff','#16a34a',2);L('Vout',240,y+16,12,'#16a34a','center',1);
L('R',100,y-18,12,'#b45309','center',1);L('C',196,y+24,12,'#2563eb','center',1);
// HPF schematic
y=212;L('RC high pass filter',20,178,13,'#1f2733','left',1);
src(34,y+22);ln(34,y+9,34,y,'#334155',2.5);ln(34,y,88,y,'#334155',2.5);ln(88,y-14,88,y+14,'#2563eb',3);ln(96,y-14,96,y+14,'#2563eb',3);ln(96,y,240,y,'#334155',2.5);
ci(170,y,3.5,'#334155');resV(170,y+4,y+44,'#b45309');gnd(170,y+48);
ln(34,y+35,34,y+48,'#334155',2.5);gnd(34,y+48);
ci(240,y,4,'#fff','#9333ea',2);L('Vout',240,y+16,12,'#9333ea','center',1);
L('C',110,y-16,12,'#2563eb','center',1);L('R',190,y+24,12,'#b45309','center',1);
// moving charge dots in series element paths
C.fillStyle='#f59e0b';for(var k=0;k<3;k++){var u=((ph/PER*10)+k/3)%1;var s=Math.sin(2*Math.PI*u);ci(150+12*s,82,3,'#f59e0b');ci(130+12*s,212,3,'#f59e0b');}
// traces
trace(84,14,0,10,0,'#2563eb','Input: slow + fast tone','both tones 100 %');
trace(180,14*GL,-PL,10*GH,-PH,'#16a34a','Low pass output','slow 99.5 %, fast 10 %');
trace(276,14*GH,PH,10*GL,PL,'#9333ea','High pass output','slow 10 %, fast 99.5 %');
// formula strip
rc(20,318,600,34,'#eef4fb',null,8);
L('Cutoff fc = 1 ÷ (2πRC); at fc both outputs are 70.7 % (3 dB) with 45° phase shift',320,335,13,'#1a2b4a','center',1);
mk(1,100,106);mk(2,216,126);mk(3,92,240);mk(4,146,236);mk(5,610,140);mk(6,610,236);
}
