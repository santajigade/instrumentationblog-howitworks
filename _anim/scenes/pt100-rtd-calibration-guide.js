var PER=4.8,ph=0,seg=0,tau=0,temp=0;
var TS=[0,50,100],RS=[100.00,119.40,138.50],DV=[0.03,-0.02,0.05];
function rOf(t){return t<=50?100+(19.40)*t/50:119.40+19.10*(t-50)/50;}
function upd(){}
function step(dt){ph=(ph+dt)%PER;seg=Math.floor(ph/1.6)%3;tau=ph-seg*1.6;var pv=TS[(seg+2)%3];temp=pv+(TS[seg]-pv)*sm(tau/0.95);}
function draw(){
L('Example readings; ramp time shortened for illustration',20,22,11,'#5b6576','left');
var stable=tau>1.0,h=temp/100;
// dry block
var gc='rgb('+Math.round(120+135*h)+','+Math.round(160-60*h)+','+Math.round(220-170*h)+')';
rc(30,150,170,170,'#e2e8f0','#64748b',10);rc(45,165,140,110,gc,'#475569',6);
// heat shimmer
for(var k=0;k<4;k++){var yy=275-((ph*50+k*27.5)%110);C.globalAlpha=0.15+0.5*h;ln(55+k*35,yy,55+k*35,yy-14,'#fff',2);C.globalAlpha=1;}
rc(45,285,140,26,'#1f2937',null,5);L('Block '+m(temp,1)+' °C',115,298,12,'#a3e635','center',1);
// probes
rc(78,95,14,150,'#cbd5e1','#475569',4);rc(138,95,14,150,'#cbd5e1','#475569',4);
rc(78,215,14,30,'#b45309',null,3);rc(138,215,14,30,'#2563eb',null,3);
L('PT100',85,260,11,'#fff','center',1);L('Ref',145,260,11,'#fff','center',1);
// cables 4 wire PT100
for(var w=0;w<4;w++){C.strokeStyle=['#dc2626','#dc2626','#f8fafc','#f8fafc'][w];C.lineWidth=2;C.beginPath();C.moveTo(82+w*2,95);C.bezierCurveTo(82+w*2,55,240,55+w*3,250,118+w*4);C.stroke();C.strokeStyle='#475569';C.lineWidth=0.6;C.stroke();}
C.strokeStyle='#2563eb';C.lineWidth=2.5;C.beginPath();C.moveTo(145,95);C.bezierCurveTo(145,72,230,150,250,190);C.stroke();
// calibrator
rc(250,100,140,170,'#fff','#334155',10);L('RTD calibrator',320,116,12,'#334155','center',1);
rc(262,130,116,44,'#0f172a',null,6);L('PT100 (4 wire)',320,141,11,'#94a3b8','center');L(m(rOf(temp)+(stable?DV[seg]:0),2)+' Ω',320,160,17,'#fbbf24','center',1);
rc(262,182,116,44,'#0f172a',null,6);L('Reference',320,193,11,'#94a3b8','center');L(m(temp,2)+' °C',320,212,17,'#60a5fa','center',1);
var bl=stable?'#16a34a':'#ca8a04';rc(262,234,116,24,bl,null,12);L(stable?'Stable: read':'Stabilizing, wait',320,246,11,'#fff','center',1);
// table
var tx=410;rc(tx,90,220,180,'#f8fafc','#cbd5e1',8);
L('Compare with IEC 60751',tx+107,106,12,'#334155','center',1);
L('Temp',tx+30,128,11,'#5b6576','center',1);L('Standard',tx+85,128,11,'#5b6576','center',1);L('Measured',tx+145,128,11,'#5b6576','center',1);L('Dev',tx+187,128,11,'#5b6576','center',1);
for(var j=0;j<3;j++){var y=152+j*36;if(j==seg)rc(tx+6,y-15,203,30,'#fef9c3',null,6);
 L(TS[j]+' °C',tx+30,y,12,'#1f2733','center',1);L(RS[j].toFixed(2),tx+85,y,12,'#1f2733','center');
 var done=j<seg||(j==seg&&tau>=1.4);
 L(done?(RS[j]+DV[j]).toFixed(2):'...',tx+145,y,12,done?'#b45309':'#94a3b8','center',done?1:0);
 L(done?(DV[j]>0?'+':'−')+Math.abs(DV[j]).toFixed(2):'',tx+187,y,12,'#16a34a','center',1);}
L('Ω values; deviation within tolerance',tx+107,258,11,'#16a34a','center');
// steps strip
var st=['1 Stabilize','2 Measure Ω','3 Compare','4 Record'];var act=tau<1.0?0:(tau<1.2?1:(tau<1.4?2:3));
for(var k=0;k<4;k++){var x=30+k*150;rc(x,300+28,140,24,k==act?'#1e63b8':'#e2e8f0',null,12);L(st[k],x+70,340,12,k==act?'#fff':'#334155','center',1);}
mk(1,212,165);mk(2,62,120);mk(3,168,120);mk(4,395,96);mk(5,622,84);
}
