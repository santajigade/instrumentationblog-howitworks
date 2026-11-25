var PER=4.8,ph=0,CX=150,CY=200,RR=110,RM=20;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function mode(){return ph<1.6?0:ph<3.2?1:2;}
function B(u){var re=1,im=0,tr=1,ti=0,q=u*u/2;for(var n=1;n<60;n++){var nr=-ti*q/(n*n),ni=tr*q/(n*n);tr=nr;ti=ni;re+=tr;im+=ti;}return Math.sqrt(re*re+im*im);}
function J(rmm,m){if(m==0)return 1;var d=m==1?9.3:2.1;return B(rmm/d)/B(RM/d);}
function draw(){
var m=mode(),lt=ph-1.6*m,s=m==0?1:Math.sin(2*Math.PI*lt/0.8),a=Math.abs(s);
L('Copper bar, 40 mm diameter. AC slowed down; density shown as colour',20,22,11,'#5b6576','left');
var tabs=['DC','AC 50 Hz','AC 1 kHz'];for(var i=0;i<3;i++){rc(30+i*82,40,76,26,i==m?'#1e63b8':'#e5e7eb',null,6);L(tabs[i],68+i*82,53,12,i==m?'#fff':'#334155','center',1);}
// cross section rings
for(var r=RR;r>0;r-=3){var rmm=r/RR*RM,v=J(rmm,m)*a,c=s>=0?'234,88,12':'37,99,235';C.fillStyle='rgba('+c+','+(0.08+0.85*v).toFixed(3)+')';C.beginPath();C.arc(CX,CY,r,0,2*Math.PI);C.arc(CX,CY,Math.max(r-3,0),0,2*Math.PI,true);C.fill();}
ci(CX,CY,RR,null,'#7c2d12',2.5);
// direction symbols
var pts=[[0,0],[0,-80],[80,0],[0,80],[-80,0]];for(var k=0;k<pts.length;k++){var x=CX+pts[k][0],y=CY+pts[k][1];ci(x,y,9,'#ffffff','#1f2733',1.5);if(a>0.15){if(s>=0)ci(x,y,3,'#1f2733');else{ln(x-5,y-5,x+5,y+5,'#1f2733',1.8);ln(x-5,y+5,x+5,y-5,'#1f2733',1.8);}}}
// skin depth ring
if(m>0){var d=m==1?9.3:2.1,rd=RR*(RM-d)/RM;C.setLineDash([5,4]);ci(CX,CY,rd,null,'#111827',1.5);C.setLineDash([]);L('δ = '+(m==1?'9.3 mm':'2.1 mm'),CX,CY+RR+20,12,'#111827','center',1);}
else L('Current spreads evenly',CX,CY+RR+20,12,'#111827','center',1);
L(m==0?'Steady current':(s>=0?'Current out of page':'Current into page'),CX,CY-RR-16,11,'#334155');
// graph
var gx=330,gy=80,gw=270,gh=170;rc(gx-10,gy-14,gw+30,gh+60,'#f8fafc','#94a3b8',8);
L('Current density across the radius',gx,gy,12,'#1f2733','left',1);
var x0=gx+20,y0=gy+gh-10,W2=gw-30,H2=gh-50;ln(x0,y0,x0+W2,y0,'#334155',1.5);ln(x0,y0,x0,y0-H2,'#334155',1.5);
L('centre',x0,y0+14,11,'#334155','center');L('surface',x0+W2,y0+14,11,'#334155','center');L('J',x0-10,y0-H2,11,'#334155','center',1);
for(var mm=0;mm<3;mm++){C.strokeStyle=mm==m?['#16a34a','#ea580c','#7c3aed'][mm]:'#cbd5e1';C.lineWidth=mm==m?3:1.5;C.beginPath();for(var i=0;i<=40;i++){var rmm=RM*i/40,x=x0+W2*i/40,y=y0-H2*J(rmm,mm)*(mm==0?0.6:1);if(i==0)C.moveTo(x,y);else C.lineTo(x,y);}C.stroke();}
var eff=m==0?'Whole area carries current':m==1?'Centre carries less, area shrinks':'Only a thin outer skin works';
L(eff,gx+gw/2,gy+gh+24,12,m==2?'#b91c1c':'#1f2733','center',1);
rc(320,296,300,48,'#fff7ed','#ea580c',8);L('δ = √(ρ ÷ (π × f × μ0 × μr))',470,312,12,'#7c2d12','center',1);L('Higher f, thinner skin, higher AC resistance',470,332,11,'#7c2d12');
mk(1,CX+RR-8,CY-RR+12);mk(2,CX+28,CY);mk(3,CX-RR-14,CY+40);mk(4,30+82*m+76,42);mk(5,gx+gw+8,gy+4);mk(6,608,300);
}
