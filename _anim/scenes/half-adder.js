var PER=4.8,ph=0,A=0,B=0,row=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;row=Math.floor(ph/1.2)%4;A=row>>1;B=row&1;}
function col(v){return v?'#16a34a':'#94a3b8';}
function wire(pts,v){C.strokeStyle=col(v);C.lineWidth=v?3.5:2.5;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();
if(v){C.setLineDash([5,7]);C.lineDashOffset=-T*30;C.strokeStyle='#bbf7d0';C.lineWidth=2;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}}
function andG(x,y){C.fillStyle='#fff';C.strokeStyle='#1e3a8a';C.lineWidth=2.5;C.beginPath();C.moveTo(x,y-28);C.lineTo(x+32,y-28);C.arc(x+32,y,28,-Math.PI/2,Math.PI/2);C.lineTo(x,y+28);C.closePath();C.fill();C.stroke();L('AND',x+28,y,12,'#1e3a8a','center',1);}
function xorG(x,y){C.fillStyle='#fff';C.strokeStyle='#1e3a8a';C.lineWidth=2.5;C.beginPath();C.moveTo(x,y-28);C.quadraticCurveTo(x+40,y-28,x+62,y);C.quadraticCurveTo(x+40,y+28,x,y+28);C.quadraticCurveTo(x+14,y,x,y-28);C.closePath();C.fill();C.stroke();
C.beginPath();C.moveTo(x-9,y-28);C.quadraticCurveTo(x+5,y,x-9,y+28);C.stroke();L('XOR',x+30,y,12,'#1e3a8a','center',1);}
function inp(x,y,lab,v){rc(x-20,y-18,40,36,v?'#16a34a':'#e2e8f0','#475569',8);L(String(v),x,y+1,18,v?'#fff':'#334155','center',1);L(lab,x-34,y,16,'#1f2733','center',1);}
function outL(x,y,lab,v){ci(x,y,18,v?'#facc15':'#e5e7eb','#475569',2);if(v){C.globalAlpha=.3;ci(x,y,28,'#fde047');C.globalAlpha=1;}L(String(v),x,y+1,15,'#1f2733','center',1);L(lab,x+28,y,15,'#1f2733','left',1);}
function draw(){
var S=A^B,Cy=A&B;
L('Inputs step through 00, 01, 10, 11',20,22,11,'#5b6576','left');
inp(70,110,'A',A);inp(70,230,'B',B);
// wires A
wire([[90,110],[150,110],[150,98],[230,98]],A);wire([[150,110],[150,222],[230,222]],A);ci(150,110,4,col(A));
// wires B
wire([[90,230],[120,230],[120,122],[230,122]],B);wire([[120,230],[120,246],[230,246]],B);ci(120,230,4,col(B));
xorG(232,110);andG(232,234);
wire([[294,110],[372,110]],S);wire([[292,234],[372,234]],Cy);
outL(392,110,'Sum',S);outL(392,234,'Carry',Cy);
L('S = A ⊕ B',300,300,15,'#1e3a8a','left',1);L('C = A · B',300,326,15,'#1e3a8a','left',1);
// truth table
var tx=490,ty=70,cw=34,rh=34,hd=['A','B','S','C'];
rc(tx-6,ty-22,cw*4+12,rh*5+10,'#f8fafc','#cbd5e1',8);
for(var j=0;j<4;j++)L(hd[j],tx+cw*j+cw/2,ty,14,'#1f2733','center',1);
for(var r=0;r<4;r++){var a=r>>1,b=r&1,yy=ty+rh*(r+1);if(r==row)rc(tx-2,yy-15,cw*4+4,30,'#dcfce7','#16a34a',6);
var v=[a,b,a^b,a&b];for(var j=0;j<4;j++)L(String(v[j]),tx+cw*j+cw/2,yy,15,'#1f2733','center',r==row);}
mk(1,70,70);mk(2,262,72);mk(3,262,196);mk(4,392,76);mk(5,392,200);mk(6,tx+cw*2,ty+rh*5+20);
}
