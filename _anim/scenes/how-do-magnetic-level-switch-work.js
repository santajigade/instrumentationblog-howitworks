var PER=4.8,ph=0,TX0=60,TX1=300,TY0=70,TY1=330,SX=180,YH=120,YL=280;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function lev(t){return YL+14-(YL-YH+16)*(1-Math.cos(2*Math.PI*t/PER))/2;}
function cap(x,y,s,on){rc(x-11*s,y-5*s,22*s,10*s,'rgba(186,230,253,0.9)','#0284c7',5*s);var g=on?0:2*s;C.strokeStyle='#b45309';C.lineWidth=1.6*s;C.beginPath();C.moveTo(x-10*s,y);C.lineTo(x+2*s,y-g);C.moveTo(x+10*s,y);C.lineTo(x-2*s,y+g);C.stroke();if(on)ci(x,y,1.6*s,'#facc15');}
function draw(){
var lv=lev(ph),fy=lv-6,hiOn=Math.abs(fy-YH)<14,loOn=Math.abs(fy-YL)<14;
L('Level change speeded up; reed gap enlarged for clarity',20,22,11,'#5b6576','left');
// liquid
C.fillStyle='#bfdbfe';C.beginPath();C.moveTo(TX0,TY1);for(var x=TX0;x<=TX1;x+=4)C.lineTo(x,lv+2*Math.sin(x/15+2*Math.PI*ph/1.2));C.lineTo(TX1,TY1);C.closePath();C.fill();
C.strokeStyle='#1e63b8';C.lineWidth=2;C.beginPath();for(var x=TX0;x<=TX1;x+=4){var y=lv+2*Math.sin(x/15+2*Math.PI*ph/1.2);if(x==TX0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();
C.strokeStyle='#475569';C.lineWidth=5;C.beginPath();C.moveTo(TX0,TY0);C.lineTo(TX0,TY1);C.lineTo(TX1,TY1);C.lineTo(TX1,TY0);C.closePath();C.stroke();
// stem, head
rc(SX-8,TY0-2,16,TY1-TY0-10,'#e2e8f0','#64748b');rc(SX-26,40,52,30,'#475569',null,4);L('Head',SX,55,11,'#fff','center',1);
// reed switches inside stem
cap(SX,YH,0.6,hiOn);cap(SX,YL,0.6,loOn);
L('High',TX0+5,YH,11,'#dc2626','left',1);L('Low',TX0+5,YL,11,'#ea580c','left',1);
// float
rc(SX-34,fy-15,68,30,'rgba(250,204,21,0.95)','#a16207',9);rc(SX-30,fy-5,14,10,'#dc2626');rc(SX+16,fy-5,14,10,'#2563eb');
// field lines from float magnet
C.globalAlpha=0.55;C.strokeStyle='#7c3aed';C.lineWidth=1.2;C.setLineDash([3,4]);C.lineDashOffset=-ph*25;for(var k=1;k<=2;k++){C.beginPath();C.ellipse(SX,fy,40+k*12,10+k*10,0,0,2*Math.PI);C.stroke();}C.setLineDash([]);C.lineDashOffset=0;C.globalAlpha=1;
// zoom of high switch
var on=hiOn,zx=470,zy=110;C.strokeStyle='#94a3b8';C.lineWidth=1.2;C.setLineDash([4,4]);C.beginPath();C.moveTo(SX+12,YH-6);C.lineTo(330,64);C.moveTo(SX+12,YH+6);C.lineTo(330,156);C.stroke();C.setLineDash([]);
rc(330,56,290,108,'#f8fafc','#94a3b8',8);L('Close up: HIGH reed switch',340,72,11,'#334155','left',1);
rc(380,90,180,40,'rgba(186,230,253,0.55)','#0284c7',20);
var g=on?0:7;C.strokeStyle='#b45309';C.lineWidth=5;C.lineCap='round';C.beginPath();C.moveTo(384,110);C.lineTo(440,110);C.quadraticCurveTo(462,110,478,110-g);C.moveTo(556,110);C.lineTo(500,110);C.quadraticCurveTo(478,110,462,110+g);C.stroke();C.lineCap='butt';
ln(346,110,384,110,'#64748b',3);ln(556,110,600,110,'#64748b',3);
if(on){ci(470,110,6,'rgba(250,204,21,0.9)');}
L(on?'Magnet near: reeds snap together, ON':'Magnet away: reeds apart, OFF',470,148,12,on?'#16a34a':'#dc2626','center',1);
// signal panel
rc(330,190,290,140,'#f8fafc','#334155',8);L('ON/OFF signals',475,208,12,'#1f2733','center',1);
ci(356,240,10,hiOn?'#ef4444':'#e5e7eb','#475569',1.5);L('High level alarm: '+(hiOn?'ON':'OFF'),374,240,12,'#1f2733','left',hiOn);
ci(356,272,10,loOn?'#f97316':'#e5e7eb','#475569',1.5);L('Low level alarm: '+(loOn?'ON':'OFF'),374,272,12,'#1f2733','left',loOn);
L('No power needed to switch, no contact with liquid',475,308,11,'#334155');
C.strokeStyle='#7c3aed';C.lineWidth=1.6;C.beginPath();C.moveTo(SX+26,50);C.lineTo(316,50);C.lineTo(316,260);C.lineTo(330,260);C.stroke();
ln(124,YH,SX-8,YH,'#d9622b',1.2,[3,3]);ln(124,YL,SX-8,YL,'#d9622b',1.2,[3,3]);mk(1,SX+48,fy+14);mk(2,SX-23,fy+26);mk(3,114,YH);mk(4,114,YL);mk(5,606,78);mk(6,606,206);
}
