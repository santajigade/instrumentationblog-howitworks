var PER=4.8,ph=0,dg=0;
var SEG=['1111110','0110000','1101101','1111001','0110011','1011011','1011111','1110000','1111111','1111011'];
function upd(){}
function step(dt){ph=(ph+dt)%PER;dg=Math.floor(ph/0.48)%10;}
function bits(n){return [(n>>3)&1,(n>>2)&1,(n>>1)&1,n&1];}
function bar(x,y,w,h,on){rc(x,y,w,h,on?'#ef4444':'#f1e4e4',on?'#b91c1c':'#e5d0d0',4);if(on){C.globalAlpha=.25;rc(x-3,y-3,w+6,h+6,'#fca5a5',null,6);C.globalAlpha=1;}}
function draw(){
var b=bits(dg),s=SEG[dg],lab=['D (8)','C (4)','B (2)','A (1)'],sl='abcdefg';
L('Common cathode display, BCD input counts 0 to 9',20,22,11,'#5b6576','left');
// inputs
for(var i=0;i<4;i++){var y=100+i*48;rc(54,y-16,36,32,b[i]?'#16a34a':'#e2e8f0','#475569',7);L(String(b[i]),72,y+1,16,b[i]?'#fff':'#334155','center',1);L(lab[i],48,y,12,'#1f2733','right',1);
ln(90,y,130,y,b[i]?'#16a34a':'#94a3b8',b[i]?3:2);}
// decoder
rc(130,64,96,206,'#eef4fb','#1e3a8a',8);L('BCD to',178,150,13,'#1e3a8a','center',1);L('7 segment',178,168,13,'#1e3a8a','center',1);L('decoder',178,186,13,'#1e3a8a','center',1);
// outputs with resistors
for(var j=0;j<7;j++){var y=80+j*28,on=s[j]=='1',c=on?'#16a34a':'#94a3b8';L(sl[j],232,y-9,11,'#475569','left');
ln(226,y,256,y,c,on?3:2);rc(256,y-6,28,12,'#fde68a','#92400e',2);ln(284,y,318,y,c,on?3:2);
if(on){C.setLineDash([4,6]);C.lineDashOffset=-ph/PER*100;ln(226,y,256,y,'#bbf7d0',1.5,[4,6]);ln(284,y,318,y,'#bbf7d0',1.5,[4,6]);C.setLineDash([]);C.lineDashOffset=0;}}
L('220 Ω each',270,290,11,'#92400e','center');
// display package
rc(318,60,150,238,'#1f2937','#0f172a',10);
var ox=360,oy=96,w=58,h=72,t=11;
bar(ox+t,oy,w,t,s[0]=='1');bar(ox+w+t,oy+t,t,h,s[1]=='1');bar(ox+w+t,oy+2*t+h,t,h,s[2]=='1');bar(ox+t,oy+2*t+2*h,w,t,s[3]=='1');
bar(ox,oy+2*t+h,t,h,s[4]=='1');bar(ox,oy+t,t,h,s[5]=='1');bar(ox+t,oy+t+h,w,t,s[6]=='1');
L('a',ox+t+w/2,oy-10,11,'#cbd5e1');L('g',ox+t+w/2,oy+t+h+22,11,'#cbd5e1');
// common cathode
ln(393,298,393,318,'#334155',2.5);ln(378,318,408,318,'#334155',2.5);ln(384,324,402,324,'#334155',2);ln(389,330,397,330,'#334155',1.5);
L('COM to 0 V',414,318,11,'#334155','left');
// truth table
var tx=490,ty=50,rh=24;rc(tx-6,ty-14,150,rh*11+6,'#f8fafc','#cbd5e1',8);
L('N',tx+10,ty,12,'#1f2733','center',1);L('DCBA',tx+50,ty,12,'#1f2733','center',1);L('abcdefg',tx+108,ty,12,'#1f2733','center',1);
for(var r=0;r<10;r++){var yy=ty+rh*(r+1),q=bits(r),cur=r==dg;if(cur)rc(tx-3,yy-11,144,22,'#dcfce7','#16a34a',5);
L(String(r),tx+10,yy,12,'#1f2733','center',cur);L(q.join(''),tx+50,yy,12,'#1f2733','center',cur);L(SEG[r],tx+108,yy,12,'#1f2733','center',cur);}
mk(1,72,62);mk(2,178,96);mk(3,270,60);mk(4,444,80);mk(5,355,320);mk(6,560,326);
}
