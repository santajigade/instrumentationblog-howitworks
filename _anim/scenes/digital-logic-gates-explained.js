var PER=4.8,ph=0,A=0,B=0,row=0,GH=20;
function upd(){}
function step(dt){ph=(ph+dt)%PER;row=Math.floor(ph/1.2)%4;A=row>>1;B=row&1;}
function col(v){return v?'#16a34a':'#94a3b8';}
function wire(pts,v){C.strokeStyle=col(v);C.lineWidth=v?3.5:2.5;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();
if(v){C.setLineDash([5,7]);C.lineDashOffset=-T*30;C.strokeStyle='#bbf7d0';C.lineWidth=2;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}}
function sty(){C.fillStyle='#fff';C.strokeStyle='#1e3a8a';C.lineWidth=2.5;}
function andB(x,y){sty();C.beginPath();C.moveTo(x,y-GH);C.lineTo(x+24,y-GH);C.arc(x+24,y,GH,-Math.PI/2,Math.PI/2);C.lineTo(x,y+GH);C.closePath();C.fill();C.stroke();return x+44;}
function orB(x,y){sty();C.beginPath();C.moveTo(x,y-GH);C.quadraticCurveTo(x+38,y-GH,x+58,y);C.quadraticCurveTo(x+38,y+GH,x,y+GH);C.quadraticCurveTo(x+11,y,x,y-GH);C.closePath();C.fill();C.stroke();return x+58;}
function xorB(x,y){var o=orB(x,y);C.beginPath();C.moveTo(x-8,y-GH);C.quadraticCurveTo(x+3,y,x-8,y+GH);C.stroke();return o;}
function notB(x,y){sty();C.beginPath();C.moveTo(x,y-GH);C.lineTo(x+48,y);C.lineTo(x,y+GH);C.closePath();C.fill();C.stroke();return x+48;}

function gate(kind,x,y,v){
 var two=kind!='NOT';
 if(two){wire([[x-30,y-10],[x+8,y-10]],A);wire([[x-30,y+10],[x+8,y+10]],B);L('A',x-38,y-10,12,'#334155','center',1);L('B',x-38,y+10,12,'#334155','center',1);}
 else{wire([[x-30,y],[x+4,y]],A);L('A',x-38,y,12,'#334155','center',1);}
 var o,inv=(kind=='NAND'||kind=='NOR'||kind=='XNOR'||kind=='NOT');
 if(kind=='AND'||kind=='NAND')o=andB(x,y);else if(kind=='OR'||kind=='NOR')o=orB(x,y);else if(kind=='XOR'||kind=='XNOR')o=xorB(x,y);else o=notB(x,y);
 if(inv){ci(o+5,y,5,'#fff','#1e3a8a',2.5);o+=10;}
 wire([[o,y],[x+108,y]],v);
 var lx=x+122;ci(lx,y,13,v?'#facc15':'#e5e7eb','#475569',2);if(v){C.globalAlpha=.3;ci(lx,y,21,'#fde047');C.globalAlpha=1;}
 L(String(v),lx,y+1,13,'#1f2733','center',1);
 var lx2=kind=='NOT'?x+16:(kind=='AND'||kind=='NAND')?x+21:x+31;L(kind,lx2,y,11,'#1e3a8a','center',1);
}
function inp(x,y,lab,v){rc(x-20,y-18,40,36,v?'#16a34a':'#e2e8f0','#475569',8);L(String(v),x,y+1,18,v?'#fff':'#334155','center',1);L(lab,x-34,y,16,'#1f2733','center',1);}
function draw(){
L('Inputs A and B step through 00, 01, 10, 11 (1.2 s per row)',20,22,11,'#5b6576','left');
rc(14,48,112,292,'#f8fafc','#cbd5e1',8);
L('Inputs',70,66,13,'#1f2733','center',1);
inp(78,112,'A',A);inp(78,192,'B',B);
var rs=['00','01','10','11'];
L('Row AB',70,246,12,'#334155','center',1);
for(var r=0;r<4;r++){var cx=34+r*24;rc(cx-11,260,22,22,r==row?'#dcfce7':'#fff',r==row?'#16a34a':'#cbd5e1',5);L(rs[r],cx,272,11,'#1f2733','center',r==row);}
var u=(ph%1.2)/1.2;rc(24,300,92,8,'#e2e8f0',null,4);rc(24,300,92*u,8,'#16a34a',null,4);
L('next row',70,322,11,'#5b6576','center');
var nA=1-A,a=A,b=B;
var ys=[75,145,215,285];
gate('AND',205,ys[0],a&b);gate('OR',205,ys[1],a|b);gate('XOR',205,ys[2],a^b);gate('NOT',205,ys[3],nA);
gate('NAND',445,ys[0],1-(a&b));gate('NOR',445,ys[1],1-(a|b));gate('XNOR',445,ys[2],1-(a^b));
ci(430,285,9,'#facc15','#475569',2);L('Lamp lit = output 1',446,285,12,'#334155','left');
mk(1,78,82);mk(2,78,162);mk(3,229,42);mk(4,495,48);mk(5,190,184);mk(6,350,52);
}
