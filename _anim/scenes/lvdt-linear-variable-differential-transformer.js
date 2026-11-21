var PER=4.8,ph=0,DM=50,CP=0.24;
var CY=140;
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function dsp(t){return DM*Math.sin(2*Math.PI*t/PER);} // + = core toward S2 (right)
function v1(t){return 0.5-0.4*dsp(t)/DM;}
function v2(t){return 0.5+0.4*dsp(t)/DM;}
function coil(x0,x1,col,lab){var cl=['#b45309','#d97706'];for(var h=0;h<2;h++){var y=h?CY+12:CY-44;rc(x0,y,x1-x0,32,col,'#92400e',3);C.strokeStyle='rgba(255,255,255,0.35)';C.lineWidth=1;for(var x=x0+5;x<x1;x+=8){C.beginPath();C.moveTo(x,y+2);C.lineTo(x+2,y+30);C.stroke();}}
var w=C.measureText?0:0;C.font='700 12px "Segoe UI",Arial,sans-serif';var tw=C.measureText(lab).width+12;rc((x0+x1)/2-tw/2,CY-37,tw,18,'rgba(255,255,255,0.92)',null,9);L(lab,(x0+x1)/2,CY-28,12,'#1f2733','center',1);}
function draw(){
var d=dsp(ph),xc=320+d,a1=v1(ph),a2=v2(ph),vo=a1-a2,car=Math.sin(2*Math.PI*ph/CP);
L('AC excitation slowed down; core travel exaggerated',20,22,11,'#5b6576','left');
// former tube
rc(140,CY-12,360,24,'#f1f5f9','#94a3b8',2);
// rod and moving part
rc(xc-80-150,CY-3,150,6,'#64748b');rc(xc-80-150-34,CY-22,34,44,'#475569',null,5);L('Object',xc-80-167,CY+36,11,'#334155','center',1);
// flux arcs (strength follows coupling)
var sides=[[200,a1],[440,a2]];C.setLineDash([5,5]);C.lineDashOffset=0;
for(var s=0;s<2;s++){var cx=(320+sides[s][0])/2;C.strokeStyle='rgba(124,58,237,'+(0.15+0.9*sides[s][1])+')';C.lineWidth=1+2.5*sides[s][1];C.beginPath();C.ellipse(cx,CY,78,58,0,Math.PI,2*Math.PI);C.stroke();C.beginPath();C.ellipse(cx,CY,78,58,0,0,Math.PI);C.stroke();}
C.setLineDash([]);C.lineDashOffset=0;
// core
rc(xc-80,CY-10,160,20,'#6b7280','#374151',4);
coil(150,250,'#d97706','S1');coil(260,380,'#b45309','Primary');coil(390,490,'#d97706','S2');
// AC source on primary
ln(290,CY-44,290,58,'#334155',2);ln(350,CY-44,350,58,'#334155',2);ln(290,58,306,58,'#334155',2);ln(334,58,350,58,'#334155',2);
ci(320,58,14,'#fff','#334155',2);C.strokeStyle='#334155';C.lineWidth=1.8;C.beginPath();for(var i=0;i<=16;i++){var x=311+i*18/16,y=58-5*Math.sin(i/16*2*Math.PI+2*Math.PI*ph/CP);if(i)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
L('AC excitation',362,58,12,'#1f2733','left',1);
// secondary wiring: series opposition
ln(160,CY+44,160,236,'#334155',2);ln(240,CY+44,240,206,'#334155',2);ln(240,206,400,206,'#334155',2);ln(400,206,400,CY+44,'#334155',2);ln(480,CY+44,480,236,'#334155',2);
L('Series opposition',320,218,11,'#334155','center');
ci(160,236,4,'#fff','#334155',2);ci(480,236,4,'#fff','#334155',2);L('A',150,236,12,'#1f2733','right',1);L('B',490,236,12,'#1f2733','left',1);
// meters
var bx=40,bw=200;L('VS1',bx,262,12,'#1f2733','left',1);rc(bx+36,255,bw,14,'#e2e8f0',null,7);rc(bx+36,255,bw*a1/0.9,14,'#d97706',null,7);
L('VS2',bx,284,12,'#1f2733','left',1);rc(bx+36,277,bw,14,'#e2e8f0',null,7);rc(bx+36,277,bw*a2/0.9,14,'#b45309',null,7);
L('Vout = VS1 − VS2 = '+m(vo*10,2)+' V',bx,310,12,'#1e3a8a','left',1);
L(Math.abs(d)<3?'Core at null position':'Core '+(Math.abs(d)/10).toFixed(1)+' mm toward '+(d<0?'S1':'S2'),bx,332,12,'#334155','left',1);
// scope
var x0=300,x1=616,y0=252,y1=346,ym=(y0+y1)/2+6;rc(x0-4,y0-8,x1-x0+8,y1-y0+12,'#f8fafc','#dde3ee',6);
var st=Math.abs(d)<3?'Null: output near zero':(vo>0?'Toward S1: in phase':'Toward S2: phase reversed');L(st,x0+6,y0+4,11,'#334155','left',1);
ln(x0,ym,x1,ym,'#cbd5e1',1);
C.lineWidth=1.2;C.strokeStyle='#94a3b8';C.beginPath();for(var x=x0;x<=x1;x+=2){var tt=ph-(x1-x)/(x1-x0)*1.2,y=ym-12*Math.sin(2*Math.PI*tt/CP);if(x>x0)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
C.lineWidth=2.5;C.strokeStyle='#1d4ed8';C.beginPath();for(var x=x0;x<=x1;x+=2){var tt=ph-(x1-x)/(x1-x0)*1.2,dd=dsp(tt),y=ym-36*(-0.8*dd/DM)*Math.sin(2*Math.PI*tt/CP);if(x>x0)C.lineTo(x,y);else C.moveTo(x,y);}C.stroke();
L('excitation',x1-4,y1-2,11,'#94a3b8','right');L('Vout',x1-66,y1-2,11,'#1d4ed8','right',1);
mk(1,272,CY-28);mk(2,166,CY-28);mk(3,474,CY-28);mk(4,xc+58,CY);mk(5,296,40);mk(6,602,y0+6);
}
