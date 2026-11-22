var PER=4.8,ph=0,u=0,p=0;
function upd(){}
function step(dt){ph=(ph+dt)%PER;u=ph/PER;p=5-5*Math.cos(2*Math.PI*u);}
function draw(){
L('Illustrative 0 to 10 bar cycle; diaphragm movement exaggerated',20,22,11,'#5b6576','left');
var s=p/10;
// process pipe
pipe(20,620,318,22,'#d9f99d');
for(var k=0;k<8;k++){var xx=20+((ph*75+k*75)%600);ci(xx,312+(k%3)*6,3,'#65a30d');}
L('Process media (corrosive or viscous)',440,270,12,'#3f6212','center',1);
// branch nozzle and seal
rc(150,262,100,34,'#d9f99d',null,0);ln(150,262,150,296,'#9aa5b8',4);ln(250,262,250,296,'#9aa5b8',4);
for(var k=0;k<3;k++){var yy=290-((ph*20+k*9)%27);C.globalAlpha=0.3+0.7*s;ar(200,yy+8,200,yy,'#3f6212',2);C.globalAlpha=1;}
rc(130,250,140,12,'#64748b',null,2);rc(130,206,140,12,'#64748b',null,2);
rc(140,218,120,32,'#fde68a',null,0);ln(140,218,140,250,'#64748b',3);ln(260,218,260,250,'#64748b',3);
// corrugated diaphragm
var d=9*s;C.strokeStyle='#334155';C.lineWidth=3;C.beginPath();
for(var k=0;k<=60;k++){var xx=140+120*k/60,t=k/60;var bow=Math.sin(Math.PI*t)*d;var cor=2.2*Math.sin(t*Math.PI*10);var yy=250-bow+cor*Math.sin(Math.PI*t);if(k==0)C.moveTo(xx,yy);else C.lineTo(xx,yy);}C.stroke();
L('Fill fluid',200,232,11,'#92400e','center',1);
// capillary
var cp=[[200,206],[200,150],[360,150],[360,190],[470,190]];
C.strokeStyle='#94a3b8';C.lineWidth=8;C.beginPath();C.moveTo(cp[0][0],cp[0][1]);for(var k=1;k<cp.length;k++)C.lineTo(cp[k][0],cp[k][1]);C.stroke();
C.strokeStyle='#fbbf24';C.lineWidth=4;C.stroke();
// fluid displacement ticks (small shift with pressure)
C.setLineDash([3,9]);C.lineDashOffset=-s*12;C.strokeStyle='#b45309';C.lineWidth=4;C.stroke();C.setLineDash([]);C.lineDashOffset=0;
L('Capillary',280,138,11,'#475569','center',1);
// gauge
var gx=520,gy=150,R=62;ci(gx,gy,R+8,'#e2e8f0','#475569',2);ci(gx,gy,R,'#fff','#94a3b8',1.5);
for(var i=0;i<=10;i++){var a=Math.PI*0.75+Math.PI*1.5*i/10;var c=Math.cos(a),sn=Math.sin(a);ln(gx+c*(R-10),gy+sn*(R-10),gx+c*(R-2),gy+sn*(R-2),'#334155',i%5==0?2.5:1.5);if(i%2==0)L(String(i),gx+c*(R-22),gy+sn*(R-22),11,'#334155','center',1);}
var an=Math.PI*0.75+Math.PI*1.5*s;ln(gx,gy,gx+Math.cos(an)*(R-14),gy+Math.sin(an)*(R-14),'#dc2626',3);ci(gx,gy,5,'#1f2937');
L('bar',gx,gy+46,11,'#5b6576','center');rc(gx-38,gy+R+14,76,22,'#1f2937',null,5);L(m(p,1)+' bar',gx,gy+R+25,12,'#a3e635','center',1);
// steps
var st=['Pressure acts on diaphragm','Diaphragm flexes','Fill fluid transfers pressure','Gauge shows the value'];
var act=Math.floor(ph/1.2)%4;
for(var k=0;k<4;k++){var y=52+k*24;rc(20,y,196,20,k==act?'#0e7490':'#ecfeff',null,10);L((k+1)+'  '+st[k],30,y+10,11,k==act?'#fff':'#155e75','left',1);}
mk(1,90,318);mk(2,282,250);mk(3,282,226);mk(4,380,170);mk(5,600,90);
}
