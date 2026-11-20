var PER=4.8,ph=0,SW=1.2,TR=1.05;
var GX=402,GY=50,DW=27,DH=26;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function sig(fr){return Math.sin(2*Math.PI*2*fr);}
function draw(){
var u=ph%SW,tracing=u<TR,fr=tracing?u/TR:1-(u-TR)/(SW-TR),vy=sig(fr),sx=GX+fr*8*DW,sy=GY+3*DH-vy*2*DH;
L('Side view shows vertical deflection only; sweep slowed for viewing',20,22,11,'#5b6576','left');
// tube outline
C.fillStyle='#f1f5f9';C.strokeStyle='#64748b';C.lineWidth=2;C.beginPath();C.moveTo(28,112);C.lineTo(215,112);C.lineTo(352,52);C.lineTo(352,228);C.lineTo(215,168);C.lineTo(28,168);C.closePath();C.fill();C.stroke();
rc(348,52,10,176,'#bbf7d0','#16a34a',3);
// gun: heater cathode, grid, anodes
rc(36,128,18,24,'#f59e0b','#92400e',3);rc(62,124,8,32,'#94a3b8','#475569',2);rc(78,122,10,36,'#64748b','#334155',2);rc(96,122,10,36,'#64748b','#334155',2);
// Y plates
rc(150,118,46,6,'#2563eb');rc(150,156,46,6,'#2563eb');L('+',202,118,11,'#2563eb','left',1);
// X plates (seen edge on)
C.globalAlpha=.35;rc(222,116,30,48,'#d9622b','#9a3412',2);C.globalAlpha=1;
// beam
var by2=140-vy*44;if(tracing){C.setLineDash([5,6]);C.lineDashOffset=-ph/PER*220;C.strokeStyle='#16a34a';C.lineWidth=2;C.beginPath();C.moveTo(106,140);C.lineTo(150,140);C.quadraticCurveTo(196,140,250,140-vy*12);C.lineTo(348,by2);C.stroke();C.setLineDash([]);C.lineDashOffset=0;ci(350,by2,4,'#22c55e');}
L('Electron gun',70,186,11,'#334155','center',1);L('Y plates',173,104,11,'#2563eb','center',1);L('X plates (front and back)',255,242,11,'#d9622b','center',1);
// front screen
rc(GX-10,GY-10,8*DW+20,6*DH+20,'#0f172a',null,12);rc(GX,GY,8*DW,6*DH,'#052e16');
for(var i=0;i<=8;i++)ln(GX+i*DW,GY,GX+i*DW,GY+6*DH,'#14532d',1);for(var j=0;j<=6;j++)ln(GX,GY+j*DH,GX+8*DW,GY+j*DH,'#14532d',1);
C.strokeStyle='rgba(74,222,128,0.35)';C.lineWidth=2;C.beginPath();for(var k=0;k<=216;k++){var f=k/216,y=GY+3*DH-sig(f)*2*DH;if(k)C.lineTo(GX+k,y);else C.moveTo(GX,y);}C.stroke();
if(tracing){C.strokeStyle='#4ade80';C.lineWidth=2.5;C.beginPath();for(var k=0;k<=fr*216;k++){var f=k/216,y=GY+3*DH-sig(f)*2*DH;if(k)C.lineTo(GX+k,y);else C.moveTo(GX,y);}C.stroke();
C.globalAlpha=.35;ci(sx,sy,9,'#86efac');C.globalAlpha=1;ci(sx,sy,4,'#f0fdf4');}
L('2 V/div   1 ms/div',GX+108,GY+6*DH+22,12,'#334155','center',1);
L('8 Vpp, T = 4 ms, f = 1/T = 250 Hz',GX+108,GY+6*DH+40,12,'#16a34a','center',1);
// bottom plots
rc(24,262,300,78,'#f8fafc','#e2e8f0',8);L('Y input signal',34,276,11,'#2563eb','left',1);
C.strokeStyle='#2563eb';C.lineWidth=2;C.beginPath();for(var k=0;k<=260;k++){var y=310-sig(k/260)*20;if(k)C.lineTo(44+k,y);else C.moveTo(44,y);}C.stroke();
if(tracing)ln(44+fr*260,284,44+fr*260,334,'#d9622b',1.5);
rc(340,262,284,78,'#f8fafc','#e2e8f0',8);L('Time base sawtooth to X plates',350,276,11,'#d9622b','left',1);
C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();var x0=360,w=244/4;for(var n=0;n<4;n++){var a=x0+n*w;C.moveTo(a,330);C.lineTo(a+w*TR/SW,290);C.lineTo(a+w,330);}C.stroke();
var cyc=Math.floor(ph/SW),cxp=x0+cyc*w+u/SW*w;ci(cxp,tracing?330-40*u/TR:290+40*(u-TR)/(SW-TR),4,'#1f2733');
mk(1,70,206);mk(2,173,84);mk(3,166,242);mk(4,GX+8*DW+2,GY-14);mk(5,612,276);mk(6,312,276);
}
