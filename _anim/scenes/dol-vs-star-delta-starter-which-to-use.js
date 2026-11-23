var PER=4.8,ph=0,NT=6,FT=[],FTOT=0;
function spd(t){
 if(t<0.3)return 0;
 if(t<2.6)return 0.85*(1-Math.exp(-(t-0.3)/0.6));
 var s1=0.85*(1-Math.exp(-2.3/0.6));
 if(t<2.8)return s1-0.15*(t-2.6);
 var s2=s1-0.03;
 if(t<4.1)return s2+(1-s2)*(1-Math.exp(-(t-2.8)/0.25));
 var s3=s2+(1-s2)*(1-Math.exp(-1.3/0.25));
 return s3*(1-sm((t-4.1)/0.7));}
function isd(t){
 if(t<0.3||(t>=2.6&&t<2.8)||t>=4.1)return 0;
 if(t<2.6)return 1.1+1.4*Math.exp(-(t-0.3)/0.6);
 return 1+1.6*Math.exp(-(t-2.8)/0.15);}
function idol(t){
 if(t<0.3||t>=4.1)return 0;var u=t-0.3;
 if(u<0.8)return 7-0.4*u;return 1+5.68*Math.exp(-(u-0.8)/0.12);}
(function(){var n=480,a=0;for(var i=0;i<=n;i++){FT.push(a);a+=spd(i*PER/n)*PER/n;}FTOT=a;})();
function ang(t){var i=Math.min(479,Math.floor(t/PER*480)),f=t/PER*480-i;return 2*Math.PI*NT*(FT[i]+(FT[i+1]-FT[i])*f)/FTOT;}
function upd(){}
function step(dt){ph=(ph+dt)%PER;}
function stage(t){if(t<0.3)return 0;if(t<2.6)return 1;if(t<2.8)return 2;if(t<4.1)return 3;return 4;}
function cont(y,name,sub,on,col){
 rc(20,y,180,38,on?'#ecfdf5':'#f8fafc',on?'#16a34a':'#94a3b8',8);
 L(name,32,y+13,13,'#1a2b4a','left',1);L(sub,32,y+28,11,'#5b6576','left');
 rc(128,y+9,62,20,on?'#16a34a':'#cbd5e1',null,10);L(on?'CLOSED':'OPEN',159,y+19,11,on?'#fff':'#334155','center',1);}
function coil(x1,y1,x2,y2,c){var mx=(x1+x2)/2,my=(y1+y2)/2,a=Math.atan2(y2-y1,x2-x1);
 ln(x1,y1,x2,y2,c,2.5);C.save();C.translate(mx,my);C.rotate(a);rc(-14,-6,28,12,'#fff',c,3);C.restore();}
function draw(){
 var t=ph,sg=stage(t);
 L('Currents in multiples of full load current (FLC); timing slowed down',20,22,11,'#5b6576','left');
 var kmOn=(sg==1||sg==2||sg==3),kyOn=(sg==1),kdOn=(sg==3);
 cont(42,'KM','Main contactor',kmOn);cont(90,'KY','Star contactor',kyOn);cont(138,'KD','Delta contactor',kdOn);
 // timer
 var tp=sg==1?(t-0.3)/2.3:(sg==2||sg==3?1:0);
 L('KT timer',32,198,11,'#1a2b4a','left',1);rc(90,191,110,14,'#e2e8f0',null,7);if(tp>0)rc(90,191,110*tp,14,'#f59e0b',null,7);
 mk(1,214,61);mk(2,214,109);mk(3,214,157);mk(4,214,198);
 // motor
 var cx=315,cy=112,s=spd(t),a=ang(t);
 ci(cx,cy,60,'#cbd5e1','#475569',2);ci(cx,cy,46,'#fff','#94a3b8',1.5);
 C.save();C.translate(cx,cy);C.rotate(a);ci(0,0,40,'#9ca3af','#4b5563',1.5);
 for(var k=0;k<8;k++){C.save();C.rotate(k*Math.PI/4);rc(-4,-38,8,16,'#b45309',null,2);C.restore();}
 ci(0,0,9,'#334155');ln(0,0,0,-30,'#facc15',3);C.restore();
 mk(5,372,58);
 var st=['Stopped','Star start','Open transition','Delta run','Stop pressed'][sg];
 L(st,cx,188,14,sg==1?'#2563eb':sg==3?'#16a34a':sg==2?'#d97706':'#475569','center',1);
 L('Speed '+Math.round(s*100)+'%',cx,206,12,'#334155');
 // winding diagram
 var wx=535,wy=118,R=50,c=sg==1?'#2563eb':sg==3?'#16a34a':'#94a3b8';
 var P3=[];for(var k=0;k<3;k++){var q=-Math.PI/2+k*2*Math.PI/3;P3.push([wx+R*Math.cos(q),wy+R*Math.sin(q)]);}
 if(sg==3){coil(P3[0][0],P3[0][1],P3[1][0],P3[1][1],c);coil(P3[1][0],P3[1][1],P3[2][0],P3[2][1],c);coil(P3[2][0],P3[2][1],P3[0][0],P3[0][1],c);}
 else{for(var k=0;k<3;k++)coil(wx,wy,P3[k][0],P3[k][1],c);ci(wx,wy,4,c);}
 for(var k=0;k<3;k++)ci(P3[k][0],P3[k][1],5,'#1a2b4a');
 L(sg==3?'Delta connection':(sg==1?'Star connection':'Windings off'),wx,50,13,c,'center',1);
 L(sg==1?'58% voltage per winding':(sg==3?'Full line voltage per winding':(sg==2?'Short break, no current':'No supply')),wx,188,12,'#334155');
 L(sg==1?'Torque about 33%':(sg==3?'Full torque':''),wx,206,12,'#334155');
 // graph
 var gx0=70,gx1=610,gy0=332,gk=11.5;function X(u){return gx0+u/PER*(gx1-gx0);}function Y(v){return gy0-v*gk;}
 ln(gx0,gy0,gx1,gy0,'#334155',1.5);ln(gx0,gy0,gx0,Y(8.3),'#334155',1.5);
 for(var v=0;v<=8;v+=2){L(String(v),gx0-8,Y(v),11,'#5b6576','right');if(v)ln(gx0,Y(v),gx1,Y(v),'#eef2f7',1);}
 L('× FLC',gx0-8,Y(8)-14,11,'#5b6576','right',1);
 L('Time, one start and stop cycle',(gx0+gx1)/2,346,11,'#5b6576');
 C.strokeStyle='#dc2626';C.lineWidth=2;C.setLineDash([6,4]);C.beginPath();for(var i=0;i<=480;i++){var u=i*PER/480;var yy=Y(idol(u));if(i)C.lineTo(X(u),yy);else C.moveTo(X(u),yy);}C.stroke();C.setLineDash([]);
 C.globalAlpha=0.25;C.strokeStyle='#2563eb';C.lineWidth=2.5;C.beginPath();for(var i=0;i<=480;i++){var u=i*PER/480;if(i)C.lineTo(X(u),Y(isd(u)));else C.moveTo(X(u),Y(isd(u)));}C.stroke();C.globalAlpha=1;
 C.strokeStyle='#2563eb';C.lineWidth=3;C.beginPath();var nn=Math.floor(t/PER*480);for(var i=0;i<=nn;i++){var u=i*PER/480;if(i)C.lineTo(X(u),Y(isd(u)));else C.moveTo(X(u),Y(isd(u)));}C.lineTo(X(t),Y(isd(t)));C.stroke();
 ln(X(t),Y(8.3),X(t),gy0,'#94a3b8',1,[3,3]);ci(X(t),Y(isd(t)),5,'#2563eb','#fff',1.5);
 L('DOL start 6 to 8 × FLC',212,Y(6.4),11,'#dc2626','left',1);
 L('Star delta start 2 to 3 × FLC',222,Y(4.2),11,'#2563eb','left',1);
 L('Star to delta switch spike',398,Y(3.3),11,'#2563eb','left');
 rc(470,Y(7.6),130,34,'#fff','#dde3ee',6);ln(478,Y(7.6)+11,500,Y(7.6)+11,'#2563eb',3);L('Star delta',506,Y(7.6)+11,11,'#1a2b4a','left');
 ln(478,Y(7.6)+24,500,Y(7.6)+24,'#dc2626',2,[6,4]);L('DOL',506,Y(7.6)+24,11,'#1a2b4a','left');
 mk(6,X(0.3)-14,Y(5.2));
}
