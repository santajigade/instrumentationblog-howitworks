var PER=4.8,ph=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function dev(x,y,lab,on,ip,col){rc(x-28,y,56,40,on?'#fff':'#e5e7eb',on?col:'#9ca3af',6);rc(x-20,y+6,40,18,on?'#dbeafe':'#d1d5db',null,3);L(lab,x,y+15,12,on?'#1e3a8a':'#6b7280','center',1);L(on?(ip||'no IP'):'OFF',x,y+33,11,on?(ip?'#15803d':'#b91c1c'):'#6b7280','center',1);}
function pkt(x1,y1,x2,y2,f,col,lab){var x=x1+(x2-x1)*f,y=y1+(y2-y1)*f;rc(x-36,y-9,72,18,col,null,9);L(lab,x,y,11,'#fff','center',1);}
function panel(ox,dh){
var col=dh?'#0f766e':'#7c3aed';
rc(ox,40,290,305,'#f8fafc','#e2e8f0',10);
L(dh?'DHCP: dynamic lease':'BOOTP: fixed MAC to IP table',ox+145,56,13,col,'center',1);
rc(ox+22,70,246,92,'#fff',col,8);L(dh?'DHCP server pool':'BOOTP server table',ox+145,84,12,'#334155','center',1);
var t=ph,cOff=t>1.2,expired=dh&&t>2.0,dReq=t>2.2&&t<3.0,dGet=dh&&t>=3.4,deny=!dh&&t>=3.0;
var rows=[['.11','A'],['.12','B'],['.13','C']];
for(var i=0;i<3;i++){var y=106+i*20,txt,c='#334155';
 if(i<2){txt='→ '+rows[i][1];}
 else if(!dh){txt=cOff?'→ C (still reserved)':'→ C';c=cOff?'#b91c1c':'#334155';}
 else{txt=dGet?'→ D (new lease)':(expired?'free, back in pool':'→ C');c=dGet?'#0f766e':(expired?'#ca8a04':'#334155');}
 L('192.168.1'+rows[i][0],ox+36,y,11,'#1f2733','left',1);L(txt,ox+128,y,11,c,'left',dh&&i==2&&expired?1:0);}
// devices
var dy=262,xs=[ox+40,ox+110,ox+180,ox+250];
dev(xs[0],dy,'A',true,'.11',col);dev(xs[1],dy,'B',true,'.12',col);dev(xs[2],dy,'C',!cOff,'.13',col);
var dOn=t>2.0;if(dOn)dev(xs[3],dy,'D',true,dGet?'.13':null,col);else{rc(xs[3]-28,dy,56,40,null,'#cbd5e1',6);C.setLineDash([]);L('joins',xs[3],dy+20,11,'#94a3b8','center');}
// lease bars (DHCP)
if(dh){for(var k=0;k<3;k++){var bx=xs[k]-24,by=dy+46,lv;
  if(k<2){lv=1-((t+k*0.8)%1.6)/1.6;}else{lv=cOff?clamp(1-(t-1.2)/0.8,0,1):1-(t%1.6)/1.6;}
  if(k==2&&cOff&&lv<=0)continue;
  rc(bx,by,48,7,'#e2e8f0',null,3);rc(bx,by,48*lv,7,k==2&&cOff?'#ca8a04':'#14b8a6',null,3);}
 if(dGet){var lv2=1-((t-3.4)%1.6)/1.6;rc(xs[3]-24,dy+46,48,7,'#e2e8f0',null,3);rc(xs[3]-24,dy+46,48*lv2,7,'#14b8a6',null,3);}
 L('Bars show lease time left',ox+145,dy+68,11,'#5b6576','center');}
// D request
if(dReq){pkt(xs[3],dy-4,ox+215,164,(t-2.2)/0.8,'#2563eb','request');}
if(t>=3.0&&t<3.4){var f=(t-3.0)/0.4;if(dh)pkt(ox+215,164,xs[3],dy-4,f,'#0f766e','offer .13');else pkt(ox+215,164,xs[3],dy-4,f,'#b91c1c','none free');}
if(deny){L('No address for D, although C is off',ox+145,190,12,'#b91c1c','center',1);}
if(dGet){L('Expired address reused by D',ox+145,190,12,'#0f766e','center',1);}
if(cOff&&t<2.2){L(dh?'C off: its lease runs out':'C off: address stays reserved',ox+145,190,12,dh?'#ca8a04':'#b91c1c','center',1);}
if(t<1.2)L('3 addresses, 3 devices online',ox+145,190,12,'#334155','center',1);
}
function draw(){
L('Same 3 address network as in the article; lease time shortened for illustration',20,22,11,'#5b6576','left');
var a=ph>4.5?clamp(1-(ph-4.5)/0.3,0,1):(ph<0.15?ph/0.15:1);
C.globalAlpha=0.25+0.75*a;panel(20,false);panel(330,true);C.globalAlpha=1;
mk(1,34,62);mk(2,200,322);mk(3,580,330);mk(4,390,330);mk(5,344,62);
}
