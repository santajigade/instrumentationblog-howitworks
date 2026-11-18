var PER=4.8,ph=0,u=0,p=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;p=5-5*Math.cos(2*Math.PI*u);}
function draw(){
L('Illustrative 0 to 10 bar sweep; diaphragm bending exaggerated',20,22,11,'#5b6576','left');
var s=p/10;
// gauge body cross section
rc(40,150,140,110,'#e2e8f0','#64748b',8);
// port and process fluid
rc(92,260,36,70,'#cbd5e1','#64748b',2);rc(98,260,24,70,'#bfdbfe',null,0);
for(var k=0;k<3;k++){var yy=322-((ph*25+k*20)%60);C.globalAlpha=0.3+0.7*s;ar(110,yy+12,110,yy,'#1d4ed8',2);C.globalAlpha=1;}
L('Process pressure',40,348,11,'#1e3a8a','left',1);
// oil chamber
rc(58,212,104,36,'#fef3c7','#d97706',4);L('Silicone oil',110,226,11,'#92400e','center');
// diaphragm (bends up with pressure)
var d=10*s;C.strokeStyle='#475569';C.lineWidth=4;C.beginPath();C.moveTo(58,252);C.quadraticCurveTo(110,252-2*d,162,252);C.stroke();
// silicon chip with 4 resistors
rc(80,176,60,22,'#a7f3d0','#047857',3);
for(var k=0;k<4;k++){var st=(k==0||k==3);var c=st?'rgba(220,38,38,'+(0.35+0.65*s)+')':'rgba(37,99,235,'+(0.35+0.65*s)+')';rc(85+k*13,181,9,12,c,null,1);}
L('Silicon chip',110,166,11,'#047857','center',1);
// wire to bridge
ln(140,187,212,187,'#334155',2);
// bridge diamond
var bx=262,by=187,r=50;var N=[bx,by-r],E=[bx+r,by],S=[bx,by+r],Wp=[bx-r,by];
function res(a,b,st){var col=st?'rgba(220,38,38,'+(0.35+0.65*s)+')':'rgba(37,99,235,'+(0.35+0.65*s)+')';ln(a[0],a[1],b[0],b[1],'#334155',2);var mx=(a[0]+b[0])/2,my=(a[1]+b[1])/2;C.save();C.translate(mx,my);C.rotate(Math.atan2(b[1]-a[1],b[0]-a[0]));rc(-11,-5,22,10,col,'#334155',2);C.restore();}
res(N,E,true);res(E,S,false);res(S,Wp,true);res(Wp,N,false);
ci(N[0],N[1],3,'#334155');ci(S[0],S[1],3,'#334155');ci(E[0],E[1],3,'#334155');ci(Wp[0],Wp[1],3,'#334155');
L('Excitation',bx,by-r-14,11,'#334155','center',1);L('Stretched',bx+8,by+r+16,11,'#dc2626','left',1);L('Compressed',bx-8,by+r+16,11,'#2563eb','right',1);
// bridge output
ln(E[0],E[1],340,by,'#334155',2);
// amplifier
C.fillStyle='#ede9fe';C.strokeStyle='#7c3aed';C.lineWidth=2;C.beginPath();C.moveTo(342,by-22);C.lineTo(342,by+22);C.lineTo(380,by);C.closePath();C.fill();C.stroke();L('Amp',356,by,11,'#5b21b6','center',1);
ar(380,by,402,by,'#334155',2);
// ADC
rc(402,by-26,96,52,'#fff','#334155',6);L('ADC',450,by-12,12,'#1f2733','center',1);
var cnt=Math.round(s*4095),bits='';for(var b=11;b>=0;b--)bits+=(cnt>>b)&1;L(bits,450,by+10,11,'#0f766e','center');
ar(498,by,515,by,'#334155',2);
// MCU
rc(515,by-26,100,52,'#fff','#334155',6);L('Microcontroller',565,by-8,11,'#1f2733','center',1);L('scales to bar',565,by+10,11,'#5b6576','center');
ar(565,by-26,565,110,'#334155',2);
// LCD
rc(470,46,150,64,'#1f2937',null,8);rc(478,54,134,48,'#a3e635',null,4);L(m(p,2)+' bar',545,78,22,'#1a2e05','center',1);
// pressure trend
var gx=200,gy=338,gw=420,gh=58;ln(gx,gy,gx+gw,gy,'#cbd5e1',1.5);ln(gx,gy,gx,gy-gh,'#cbd5e1',1.5);
C.strokeStyle='#2563eb';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=84;k++){var x=gx+gw*k/84,y=gy-gh*(0.5-0.5*Math.cos(2*Math.PI*k/84));if(k==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
ci(gx+gw*u,gy-gh*s,5,'#2563eb','#fff',2);L('Pressure',gx+6,gy-gh-8,11,'#1e3a8a','left',1);
mk(1,150,300);mk(2,60,274);mk(3,152,170);mk(4,214,140);mk(5,450,124);mk(6,456,52);
}
