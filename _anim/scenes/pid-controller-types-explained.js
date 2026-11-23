var PER=4.8,ph=0,Kp=1,ti=1,td=0.5,mode=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;if(ph<2.4){mode=0;Kp=1.5-0.5*Math.cos(2*Math.PI*ph/2.4);ti=1;}else{mode=1;Kp=1;ti=1.5-0.5*Math.cos(2*Math.PI*(ph-2.4)/2.4);}}
function flow(pts,on){C.strokeStyle='#334155';C.lineWidth=2;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();
C.setLineDash([5,7]);C.lineDashOffset=-ph*25;C.strokeStyle=on?'#f97316':'#93c5fd';C.lineWidth=2;C.beginPath();C.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)C.lineTo(pts[i][0],pts[i][1]);C.stroke();C.setLineDash([]);C.lineDashOffset=0;}
function blk(x,y,w,t,hot){rc(x,y-11,w,22,hot?'#ffedd5':'#eef4fb',hot?'#ea580c':'#64748b',5);L(t,x+w/2,y+1,12,'#1f2733','center',hot);}
function sum(x,y){ci(x,y,12,'#fff','#334155',2);L('Σ',x,y+1,13,'#1f2733','center',1);}
function out(y){ar(312,y,376,y,'#334155',2);L('Δm',382,y,13,'#1f2733','left',1);}
function three(cy,hp,hi,hd,t1){var ys=[cy-28,cy,cy+28],tx=[t1,'(1/τi) ∫e dt','τd de/dt'],h=[hp,hi,hd];
for(var k=0;k<3;k++){flow([[180,cy],[180,ys[k]],[192,ys[k]]]);blk(192,ys[k],90,tx[k],h[k]);}
flow([[282,ys[0]],[300,ys[0]],[300,cy-12]]);flow([[282,ys[2]],[300,ys[2]],[300,cy+12]]);flow([[282,cy],[288,cy]]);sum(300,cy);out(cy);}
function bars(cy,v,hot){var lab=['P','I','D'];for(var k=0;k<3;k++){var y=cy-22+k*22;L(lab[k],442,y,12,'#1f2733','center',1);rc(452,y-7,165,14,'#f1f5f9',null,4);rc(452,y-7,v[k]*55,14,hot[k]?'#f97316':'#3b82f6',null,4);}}
function draw(){
L('Same P, I and D ideas, three equation forms; parameters swept slowly',20,22,11,'#5b6576','left');
L('Now changing: '+(mode?'τi':'Kp'),22,46,14,'#ea580c','left',1);
L('Kp = '+m(Kp,2)+'    τi = '+m(ti,2)+' s    τd = '+m(td,2)+' s',618,46,13,'#1f2733','right',1);
L('Action strength',530,64,12,'#475569','center',1);
ln(20,152,620,152,'#e2e8f0',1.5);ln(20,247,620,247,'#e2e8f0',1.5);
var rows=[105,200,295],names=[['Parallel','independent'],['Ideal ISA','Kp on all'],['Series','interacting']];
for(var r=0;r<3;r++){L(names[r][0],22,rows[r]-8,13,'#1e3a8a','left',1);L(names[r][1],22,rows[r]+10,11,'#5b6576','left');L('e',112,rows[r],13,'#1f2733','center',1);}
// 1 parallel
var c=rows[0];flow([[120,c],[180,c]]);three(c,mode==0,mode==1,false,'Kp × e');
// 2 ideal
c=rows[1];flow([[120,c],[130,c]]);blk(130,c,38,'Kp',mode==0);flow([[168,c],[180,c]]);three(c,false,mode==1,false,'e');
// 3 series
c=rows[2];flow([[120,c],[130,c]]);blk(130,c,38,'Kp',mode==0);flow([[168,c],[180,c]]);blk(180,c,92,'1 + 1/(τi s)',mode==1);flow([[272,c],[284,c]]);blk(284,c,70,'1 + τd s',false);flow([[354,c],[364,c]]);ar(354,c,376,c,'#334155',2);L('Δm',382,c,13,'#1f2733','left',1);
// strengths
var a=mode==0,b=mode==1;
bars(rows[0],[Kp,1/ti,td],[a,b,false]);
bars(rows[1],[Kp,Kp/ti,Kp*td],[a,a||b,a]);
bars(rows[2],[Kp*(1+td/ti),Kp/ti,Kp*td],[a||b,a||b,a]);
mk(1,170,46);mk(2,340,77);mk(3,340,172);mk(4,318,267);mk(5,612,64);
}
