PAGE = dict(
    slug="historian-swinging-door", grp="SCADA", name="Historian Swinging Door Compression", kw="How Swinging Door Compression Works",
    title="How Swinging Door Compression Works: Animated Historian Demo",
    desc="How swinging door compression works, animated: two doors pivot on the last stored point and a sample is kept only when the doors open past parallel.",
    h1="How Swinging Door Compression Works",
    hero="Set the compression deviation and the noise on the signal. Watch the two doors close as samples arrive, see which points the historian keeps and compare the stored trend with the raw data.",
    quick="Swinging door compression stores a sample only when a straight line from the last stored point can no longer pass within a set deviation of every sample in between. Two imaginary doors, hinged above and below the last stored point, close as new samples arrive, and when they open past parallel the previous sample is archived.",
    intro=["A process historian collects thousands of tags every second, and storing every sample would fill disks and slow trend displays. Most historians therefore apply exception filtering first and then a compression algorithm before writing to the archive.",
           "The swinging door algorithm, published by E. H. Bristol in 1990, is the best known of these methods. It keeps only the points needed to redraw the trend with straight lines, while every discarded sample stays within the compression deviation of that line.",
           "The setting that matters is the compression deviation E. Too large and real process moves disappear from the trend, too small and the archive fills with noise."],
    sliders=[("E", "Compression deviation", 0.2, 5, 1.0, 0.1, 1, "%"), ("nz", "Noise on the signal", 0, 4, 1.0, 0.1, 1, "%")],
    outs=[("n", "Samples received in 10 minutes (1 s scan)"), ("a", "Points written to the archive"), ("cr", "Compression ratio"), ("err", "Largest error of the stored trend")],
    legend=["Raw samples from the field, one per second", "Archived points", "Upper door, pivoted at last stored value + E", "Lower door, pivoted at last stored value − E", "Held sample, the newest point not yet stored", "Archive counter and storage used"],
    steps=["The historian stores a point A and draws two pivots: A + E above it and A − E below it.",
           "For every new sample it calculates the slope from the upper pivot and the slope from the lower pivot to that sample.",
           "The upper door keeps the steepest slope seen so far and the lower door keeps the flattest, so the doors can only close, never open again.",
           "While the upper slope is below the lower slope, a straight line from A still fits every sample within ± E, so nothing is written.",
           "When the upper slope passes the lower slope the doors are open past parallel; the previous sample is archived, it becomes the new A and the doors restart."],
    formula=["Upper slope = max of (v − (vA + E)) ÷ (t − tA); lower slope = min of (v − (vA − E)) ÷ (t − tA)",
             "Archive the previous sample when upper slope > lower slope",
             "Every discarded sample lies within ± E of the straight line between stored points",
             "Compression ratio = samples received ÷ points archived",
             "Example with E = 1.0 %: A = 50.0 % at 0 s; sample 55.0 % at 10 s gives upper (55 − 51) ÷ 10 = 0.40 %/s and lower (55 − 49) ÷ 10 = 0.60 %/s, doors still open; sample 54.0 % at 15 s gives lower (54 − 49) ÷ 15 = 0.33 %/s, now 0.40 > 0.33 so the 10 s point is archived"],
    parts=[("Data collector", "Reads values from the PLC, DCS or RTU at the scan rate"),
           ("Exception filter", "Drops samples that changed less than the exception deviation before compression"),
           ("Compression engine", "Runs the swinging door test for each tag and decides which points to keep"),
           ("Archive", "Time series storage where only the kept points are written"),
           ("Trend client", "Redraws the trend by joining stored points with straight lines")],
    uses=[("Plant historians", "Long term storage of thousands of process tags at low disk cost."),
          ("SCADA archives", "Keeps pipeline and utility trends for years without huge databases."),
          ("Energy reporting", "Stores meter and power trends where slow changes dominate."),
          ("Data for analytics", "Reduces data volume before export, provided E is set below the needed accuracy.")],
    pros=["Keeps the shape of the trend with far fewer points", "Error of the stored trend is bounded by the compression deviation", "Works on each tag independently and needs very little memory"],
    cons=["Noise smaller than E is lost, so it hides small oscillations", "A deviation set too high flattens peaks and short upsets", "Stored points are not at regular time intervals, which some analysis tools expect"],
    tips=["Start with a compression deviation near the transmitter accuracy or about half the useful resolution of the tag.",
          "Set the exception deviation smaller than the compression deviation, usually about half of it.",
          "Turn compression off for tags used in custody transfer, reconciliation or event analysis where every sample matters.",
          "Check a trend of raw data against the archived trend after changing E, especially for fast tags such as compressor surge or vibration."],
    faq=[("What is the difference between exception and compression?", "Exception filtering runs first and drops samples that changed less than a small deadband. Compression then uses the swinging door test to decide which of the remaining samples must be stored."),
         ("Does compression lose data?", "It discards samples, but every discarded sample was within ± E of the straight line through the stored points. Detail smaller than E is lost."),
         ("Why is the stored point the previous sample and not the new one?", "The new sample is the one that broke the doors. The previous sample is the last point that still fits the line from A, so it is stored as the end of that line."),
         ("What compression ratio is normal?", "It depends on the tag. Slow, steady tags compress very well while noisy or fast tags compress poorly; the demo shows how noise and E change the ratio.")],
    cal=[("plc-signal/analog-scaling-calculator", "Analog Scaling Calculator")],
    glo=[],
    cmp=[],
    tool=[("tools/communication-protocols/modbus-rtu-timing-calculator", "Modbus RTU Timing Calculator")],
    blog=("historian-data-compression-swinging-door", "Historian data compression with the swinging door algorithm"))

SCENE = r"""
var SR=0.5,acc=0,k=60,raw=[],arc=[],lv={},WN=40;
function rn(i){var x=Math.sin(i*12.9898+4.1)*43758.5453;return(x-Math.floor(x))*2-1;}
function sig(i){return 50+15*Math.sin(2*Math.PI*i/40)+6*Math.sin(2*Math.PI*i/13)+P.nz*rn(i);}
function SD(s,t,v,E,out){if(!s.A){s.A=[t,v];out.push([t,v]);s.H=null;s.sU=-1e9;s.sL=1e9;return 1;}
var dt=t-s.A[0],u=(v-s.A[1]-E)/dt,l=(v-s.A[1]+E)/dt,nu=Math.max(s.sU,u),nl=Math.min(s.sL,l),r=0;
if(nu>nl&&s.H){out.push(s.H);s.A=s.H;dt=t-s.A[0];s.sU=(v-s.A[1]-E)/dt;s.sL=(v-s.A[1]+E)/dt;r=1;}else{s.sU=nu;s.sL=nl;}s.H=[t,v];return r;}
function upd(){var s={},out=[],N=600;for(var i=0;i<N;i++)SD(s,i,sig(i),P.E,out);if(s.H&&s.H[0]!==out[out.length-1][0])out.push(s.H);
var e=0,j=0;for(var i=0;i<N;i++){while(j<out.length-2&&out[j+1][0]<i)j++;var a=out[j],b=out[j+1],y=a[1]+(b[1]-a[1])*(i-a[0])/(b[0]-a[0]);e=Math.max(e,Math.abs(sig(i)-y));}
o('n',String(N));o('a',String(out.length));o('cr',m(N/out.length,1)+' : 1');o('err',m(e,2)+' % (limit '+m(P.E,1)+' %)');raw=[];for(var q=k-WN-1;q<=k;q++)raw.push([q,sig(q)]);lv={};arc=[];raw.forEach(function(r){SD(lv,r[0],r[1],P.E,arc);});}
function step(dt){acc+=dt;while(acc>=SR){acc-=SR;k++;var v=sig(k);raw.push([k,v]);SD(lv,k,v,P.E,arc);}
while(raw.length&&raw[0][0]<k-WN-2)raw.shift();while(arc.length>2&&arc[1][0]<k-WN-2)arc.shift();}
function draw(){var fr=acc/SR,gx0=60,gx1=620,gy0=118,gy1=330,X=function(t){return gx1-(k+fr-t)/WN*(gx1-gx0);},Y=function(v){return gy1-(v-22)/56*(gy1-gy0);};
L('One sample per second, shown 2 times faster; E band drawn to scale',20,22,11,'#5b6576','left');
var cur=raw.length?raw[raw.length-1][1]:50;
rc(20,38,170,62,'#1a2333',null,8);L('Collector',105,52,12,'#fff','center',1);L('New sample',32,74,11,'#cbd5e1','left');L(m(cur,1)+' %',178,74,13,'#93c5fd','right',1);
var pu=(k%2)?'#38bdf8':'#0ea5e9';ci(32,90,4,pu);L('scan 1 s',42,90,11,'#94a3b8','left');
ar(192,69,232,69,'#64748b',2);
rc(236,38,170,62,'#f5f3ff','#7c3aed',8);L('Swinging door test',321,52,12,'#2e1065','center',1);L('E = ± '+m(P.E,1)+' %',321,72,12,'#7c3aed','center',1);
var op=lv.H?(lv.sU<lv.sL?'Doors open: hold':'Doors closed: store'):'Start';L(op,321,90,11,'#5b6576','center');
ar(408,69,448,69,'#64748b',2);
var inw=raw.filter(function(r){return r[0]>k-WN;}).length,st=arc.filter(function(a){return a[0]>k-WN;}).length;
rc(452,38,168,62,'#fff7ed','#d9622b',8);L('Archive',536,52,12,'#7c2d12','center',1);
L('Raw',462,72,11,'#5b6576','left');rc(492,66,118,10,'#dbeafe');rc(492,66,118*inw/WN,10,'#1e63b8');
L('Kept',462,90,11,'#5b6576','left');rc(492,84,118,10,'#ffedd5');rc(492,84,118*st/WN,10,'#d9622b');L(st+' of '+inw,606,90,11,'#7c2d12','right',1);
rc(gx0,gy0,gx1-gx0,gy1-gy0,'#f8fafc','#e2e8f0');[30,50,70].forEach(function(p){ln(gx0,Y(p),gx1,Y(p),'#e2e8f0',1);L(p+' %',gx0-6,Y(p),11,'#5b6576','right');});
C.save();C.beginPath();C.rect(gx0,gy0,gx1-gx0,gy1-gy0);C.clip();
if(lv.A&&lv.H){var A=lv.A,te=k+fr+1,ux=te-A[0];var u1=A[1]+P.E,l1=A[1]-P.E,u2=u1+lv.sU*ux,l2=l1+lv.sL*ux;
C.fillStyle='rgba(124,58,237,0.08)';C.beginPath();C.moveTo(X(A[0]),Y(u1));C.lineTo(X(te),Y(u2));C.lineTo(X(te),Y(l2));C.lineTo(X(A[0]),Y(l1));C.closePath();C.fill();
ln(X(A[0]),Y(u1),X(te),Y(u2),'#7c3aed',2.2);ln(X(A[0]),Y(l1),X(te),Y(l2),'#0f766e',2.2);ci(X(A[0]),Y(u1),4,'#7c3aed');ci(X(A[0]),Y(l1),4,'#0f766e');ln(X(A[0]),Y(u1),X(A[0]),Y(l1),'#94a3b8',1,[3,3]);}
var pts=arc.slice();if(lv.H)pts.push(lv.H);C.strokeStyle='#d9622b';C.lineWidth=2;C.beginPath();pts.forEach(function(p,i){if(i)C.lineTo(X(p[0]),Y(p[1]));else C.moveTo(X(p[0]),Y(p[1]));});C.stroke();
raw.forEach(function(r){ci(X(r[0]),Y(r[1]),2.6,'#1e63b8');});
arc.forEach(function(a){rc(X(a[0])-5,Y(a[1])-5,10,10,'#d9622b','#fff');});
if(lv.H){var g=5+2*Math.sin(T*8);ci(X(lv.H[0]),Y(lv.H[1]),g,null,'#16a34a',2);}
C.restore();
L('Raw samples',gx0+8,gy0+12,11,'#1e63b8','left',1);L('Stored trend',gx0+96,gy0+12,11,'#d9622b','left',1);L('Upper door',gx0+186,gy0+12,11,'#7c3aed','left',1);L('Lower door',gx0+266,gy0+12,11,'#0f766e','left',1);L('last 40 s',gx1,gy1+14,11,'#5b6576','right');
var a2=null;for(var i=arc.length-1;i>=0;i--){if(X(arc[i][0])>gx0+20&&X(arc[i][0])<gx1-100){a2=arc[i];break;}}
var rr=null;for(var i=raw.length-1;i>=0;i--){if(X(raw[i][0])<gx0+150&&X(raw[i][0])>gx0+20){rr=raw[i];break;}}
mk(1,rr?X(rr[0]):gx0+40,rr?clamp(Y(rr[1])-18,gy0+26,gy1-12):gy0+40);mk(2,a2?X(a2[0]):gx0+200,a2?clamp(Y(a2[1])+20,gy0+26,gy1-12):gy1-20);
if(lv.A&&lv.H){var mx=Math.min(gx1-20,X(lv.A[0])+60),ux2=k+fr-lv.A[0]+1;var tt=(mx-X(lv.A[0]))/(gx1-gx0)*WN;mk(3,X(lv.A[0])-16,clamp(Y(lv.A[1]+P.E)-16,gy0+26,gy1-12));mk(4,X(lv.A[0])-16,clamp(Y(lv.A[1]-P.E)+16,gy0+26,gy1-12));mk(5,Math.min(X(lv.H[0])+6,gx1-12),clamp(Y(lv.H[1])-24,gy0+26,gy1-12));}
else{mk(3,gx1-40,gy0+30);mk(4,gx1-40,gy1-20);mk(5,gx1-16,gy0+50);}
mk(6,620,38);}
"""
