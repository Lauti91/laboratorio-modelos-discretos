var $=function(i){return document.getElementById(i)};
function F(x,d){if(x==null||!isFinite(x))return '—';return x.toLocaleString('es-AR',{maximumFractionDigits:d==null?2:d})}
function cl(x,a,b){return Math.max(a,Math.min(b,x))}
function sb(b,k){return b+'<tspan dy="3" font-size="10">'+k+'</tspan>'}
var TX='style="fill:var(--muted)"',TXF='style="fill:var(--fg)"',AX='style="stroke:var(--line2)"';
function niceStep(span,n){var r=span/n,m=Math.pow(10,Math.floor(Math.log10(r))),f=r/m;return(f<1.5?1:f<3.5?2:f<7.5?5:10)*m}
function ticks(lo,hi,n){var s=niceStep(hi-lo,n),a=Math.ceil(lo/s-1e-9)*s,o=[];for(var v=a;v<=hi+1e-9;v+=s)o.push(Math.abs(v)<1e-12?0:+v.toFixed(10));return o}
function bindSliders(ids,cb){ids.forEach(function(i){var e=$(i),o=$('o_'+i);var u=function(){if(o)o.textContent=F(+e.value,+(e.dataset.d||2))};e.addEventListener('input',function(){u();cb(i)});u()})}
function setv(i,v){var e=$(i);e.value=v;var o=$('o_'+i);if(o)o.textContent=F(+e.value,+(e.dataset.d||2))}
function frame(W,H,L,R,T,B,x0,x1,y0,y1){var w=W-L-R,h=H-T-B;return{W:W,H:H,L:L,R:R,T:T,B:B,w:w,h:h,x0:x0,x1:x1,y0:y0,y1:y1,
 X:function(v){return L+(v-x0)/(x1-x0)*w},Y:function(v){return T+h-(v-y0)/(y1-y0)*h},
 ix:function(px){return x0+(px-L)/w*(x1-x0)},iy:function(py){return y0+(T+h-py)/h*(y1-y0)}}}
function clip(id,f){return'<defs><clipPath id="'+id+'"><rect x="'+f.L+'" y="'+(f.T-2)+'" width="'+f.w+'" height="'+(f.h+4)+'"/></clipPath></defs>'}
function axes(f,o){var s='';
 (o.yt||[]).forEach(function(v){s+='<line x1="'+f.L+'" x2="'+(f.L+f.w)+'" y1="'+f.Y(v)+'" y2="'+f.Y(v)+'" style="stroke:var(--line)"/><text x="'+(f.L-6)+'" y="'+(f.Y(v)+4)+'" font-size="11" text-anchor="end" '+TX+'>'+(o.yf?o.yf(v):F(v))+'</text>'});
 (o.xt||[]).forEach(function(v){s+='<line x1="'+f.X(v)+'" x2="'+f.X(v)+'" y1="'+f.T+'" y2="'+(f.T+f.h)+'" style="stroke:var(--line)"/><text x="'+f.X(v)+'" y="'+(f.T+f.h+16)+'" font-size="11" text-anchor="middle" '+TX+'>'+(o.xf?o.xf(v):F(v))+'</text>'});
 s+='<line x1="'+f.L+'" y1="'+(f.T+f.h)+'" x2="'+(f.L+f.w)+'" y2="'+(f.T+f.h)+'" '+AX+'/><line x1="'+f.L+'" y1="'+f.T+'" x2="'+f.L+'" y2="'+(f.T+f.h)+'" '+AX+'/>';
 if(o.xl)s+='<text x="'+(f.L+f.w-4)+'" y="'+(f.T+f.h-7)+'" class="mv" text-anchor="end" '+TX+'>'+o.xl+'</text>';
 if(o.yl)s+='<text x="'+(f.L+6)+'" y="'+(f.T+12)+'" class="mv" '+TX+'>'+o.yl+'</text>';
 return s}
function poly(f,pts,color,w,dots,dash){if(pts.length<1)return'';var s='';
 if(pts.length>1)s+='<polyline fill="none" stroke-linejoin="round" stroke-linecap="round" style="stroke:'+color+'" stroke-width="'+(w||2)+'"'+(dash?' stroke-dasharray="'+dash+'"':'')+' points="'+pts.map(function(p){return f.X(p[0]).toFixed(1)+','+f.Y(p[1]).toFixed(1)}).join(' ')+'"/>';
 if(dots)pts.forEach(function(p){s+='<circle cx="'+f.X(p[0]).toFixed(1)+'" cy="'+f.Y(p[1]).toFixed(1)+'" r="'+dots+'" style="fill:'+color+'"/>'});return s}
function hl(f,v,label,color,dash){var y=f.Y(v);return'<line x1="'+f.L+'" x2="'+(f.L+f.w)+'" y1="'+y+'" y2="'+y+'" style="stroke:'+(color||'var(--line2)')+'" stroke-width="1.3" stroke-dasharray="'+(dash||'5 4')+'"/>'+(label?'<text x="'+(f.L+f.w-4)+'" y="'+(y-5)+'" font-size="12" text-anchor="end" '+TXF+'>'+label+'</text>':'')}
function tip(f,x,y,color){return'<circle cx="'+f.X(x)+'" cy="'+f.Y(y)+'" r="5.5" stroke-width="2" style="fill:'+color+';stroke:var(--surface)"/>'}
function yrange(vals,pad){var lo=Math.min.apply(null,vals),hi=Math.max.apply(null,vals);if(hi-lo<1e-9){hi+=0.5;lo-=0.5}var p=(hi-lo)*(pad==null?0.1:pad);return[lo-p,hi+p]}
function svgXY(e,el){var r=el.getBoundingClientRect(),vb=el.viewBox.baseVal;return[(e.clientX-r.left)/r.width*vb.width,(e.clientY-r.top)/r.height*vb.height]}
function drag(el,fn){var on=false;el.style.touchAction='none';el.style.cursor='crosshair';
 el.addEventListener('pointerdown',function(e){on=true;try{el.setPointerCapture(e.pointerId)}catch(x){}fn(svgXY(e,el))});
 el.addEventListener('pointermove',function(e){if(on)fn(svgXY(e,el))});
 el.addEventListener('pointerup',function(){on=false});el.addEventListener('pointercancel',function(){on=false})}
function makeAnim(render,maxFn,spFn,playBtn){var A={u:maxFn(),target:maxFn(),raf:null,last:0,play:false};
 function btn(){playBtn.textContent=A.play?'Pausar':'Reproducir'}
 function tick(ts){var dt=Math.min((ts-A.last)/1000,0.05);A.last=ts;var mx=maxFn();var tg=Math.min(A.target,mx);
  if(A.u<tg)A.u=Math.min(tg,A.u+dt*spFn());render();
  if(A.u<tg-1e-9){A.raf=requestAnimationFrame(tick)}else{A.raf=null;if(A.play&&A.u>=mx-1e-9)A.play=false;btn()}}
 function go(){if(!A.raf){A.last=performance.now();A.raf=requestAnimationFrame(tick)}}
 A.step=function(){A.play=false;var mx=maxFn();if(A.u>=mx-1e-9){A.u=0;A.target=0}var base=Math.floor(Math.max(A.target,A.u)+1e-9);if(A.target-A.u>1e-9)base=Math.floor(A.target+1e-9);A.target=Math.min(mx,base+1);btn();go()};
 A.toggle=function(){var mx=maxFn();if(A.play){A.play=false;A.target=Math.ceil(A.u-1e-9);btn();go();return}if(A.u>=mx-1e-9)A.u=0;A.play=true;A.target=mx;btn();go()};
 A.reset=function(){A.play=false;A.u=0;A.target=0;if(A.raf){cancelAnimationFrame(A.raf);A.raf=null}btn();render()};
 A.full=function(){A.play=false;if(A.raf){cancelAnimationFrame(A.raf);A.raf=null}A.u=maxFn();A.target=A.u;btn();render()};
 A.fit=function(){var mx=maxFn();A.u=Math.min(A.u,mx);A.target=Math.min(A.target,mx)};
 return A}
/* ---------- primer orden ---------- */
function classify1(A,B){if(Math.abs(A-1)<1e-9)return B===0?['Constante','var(--warn)']:['Crecimiento lineal (no hay equilibrio)','var(--bad)'];
 if(A>1)return['Monótona explosiva','var(--bad)'];if(A>0)return['Monótona convergente','var(--good)'];
 if(Math.abs(A)<1e-9)return['Converge en un paso','var(--good)'];
 if(A>-1+1e-9&&Math.abs(A+1)>=1e-9)return['Oscilación amortiguada','var(--good)'];
 if(Math.abs(A+1)<1e-9)return['Oscilación uniforme','var(--warn)'];return['Oscilación explosiva','var(--bad)']}
function strip1(id,A,lo,hi,labels){var el=$(id);var W=680,H=74,L=14,R=14;var X=function(v){return L+(v-lo)/(hi-lo)*(W-L-R)};
 var o='';var zs=labels||[[lo,-1,'oscilación explosiva','var(--bad)'],[-1,0,'oscilación amortiguada','var(--good)'],[0,1,'monótona amortiguada','var(--good)'],[1,hi,'monótona explosiva','var(--bad)']];
 zs.forEach(function(z,i){o+='<rect x="'+X(z[0])+'" y="26" width="'+(X(z[1])-X(z[0]))+'" height="14" style="fill:'+z[3]+';opacity:'+(z[3]==='var(--good)'?0.35:0.22)+'"/>';
  o+='<text x="'+((X(z[0])+X(z[1]))/2)+'" y="58" font-size="11" text-anchor="middle" '+TX+'>'+z[2]+'</text>'});
 for(var v=Math.ceil(lo);v<=hi;v++)o+='<text x="'+X(v)+'" y="20" font-size="11" text-anchor="middle" '+TX+'>'+v+'</text><line x1="'+X(v)+'" x2="'+X(v)+'" y1="40" y2="44" '+AX+'/>';
 var a=cl(A,lo,hi);o+='<path d="M'+X(a)+' 40 l-6 -14 h12 z" style="fill:var(--fg)"/>';el.innerHTML=o}
/* ---------- segundo orden ---------- */
function sim2(p,q,g,y0,y1,N){var y=[y0,y1];for(var t=2;t<=N;t++)y.push(g-p*y[t-1]-q*y[t-2]);return y}
function roots2(p,q){var d=p*p-4*q;if(d>=0){var s=Math.sqrt(d);return{cx:false,r1:(-p+s)/2,r2:(-p-s)/2,re:-p/2,im:0,d:d,maxabs:Math.max(Math.abs((-p+s)/2),Math.abs((-p-s)/2))}}
 var im=Math.sqrt(-d)/2;return{cx:true,re:-p/2,im:im,d:d,maxabs:Math.sqrt(q)}}
function classify2(p,q){var r=roots2(p,q),e=1e-9;
 var st=(1-q>e&&1+p+q>e&&1-p+q>e)?'estable':((1-q<-e||1+p+q<-e||1-p+q<-e)?'inestable':'borde');
 var tipo,col;
 if(r.cx){tipo='ciclo'}else{var big=Math.abs(r.r1)>=Math.abs(r.r2)?r.r1:r.r2;tipo=big<0?'zigzag':'monótona'}
 var th=r.cx?Math.atan2(r.im,r.re):null;
 var txt=tipo==='ciclo'?'Ciclo':tipo==='zigzag'?'Zigzag':'Trayectoria monótona';
 if(st==='estable'){txt+=' amortiguado';col='var(--good)'}else if(st==='borde'){txt+=' en el borde';col='var(--warn)'}else{txt+=' explosivo';col='var(--bad)'}
 if(tipo==='monótona'){txt=st==='estable'?'Monótona convergente':st==='borde'?'Monótona en el borde':'Monótona explosiva'}
 return{r:r,st:st,tipo:tipo,th:th,T:th?2*Math.PI/th:null,txt:txt,col:col}}
function fmtRoots(r){if(r.cx)return F(r.re,3)+' ± '+F(r.im,3)+' i';return F(r.r1,3)+' ; '+F(r.r2,3)}
function argand(id,p,q){var r=roots2(p,q);var m=Math.max(1.5,r.maxabs*1.18);var f=frame(300,300,22,22,16,22,-m,m,-m,m);var o='';
 var cx=f.X(0),cy=f.Y(0),rad=f.X(1)-f.X(0);
 o+='<circle cx="'+cx+'" cy="'+cy+'" r="'+rad+'" style="fill:var(--okfill);stroke:var(--line2)" stroke-width="1.5"/>';
 o+='<line x1="'+f.L+'" x2="'+(f.L+f.w)+'" y1="'+cy+'" y2="'+cy+'" '+AX+'/><line x1="'+cx+'" x2="'+cx+'" y1="'+f.T+'" y2="'+(f.T+f.h)+'" '+AX+'/>';
 [-1,1].forEach(function(v){o+='<text x="'+f.X(v)+'" y="'+(cy+14)+'" font-size="11" text-anchor="middle" '+TX+'>'+v+'</text>'});
 o+='<text x="'+(f.L+f.w)+'" y="'+(cy-5)+'" font-size="11" text-anchor="end" '+TX+'>Re</text><text x="'+(cx+5)+'" y="'+(f.T+10)+'" font-size="11" '+TX+'>Im</text>';
 var pts=r.cx?[[r.re,r.im],[r.re,-r.im]]:[[r.r1,0],[r.r2,0]];
 pts.forEach(function(pt){var mod=Math.hypot(pt[0],pt[1]);var c=mod<1-1e-9?'var(--good)':mod>1+1e-9?'var(--bad)':'var(--warn)';
  o+='<circle cx="'+f.X(pt[0])+'" cy="'+f.Y(pt[1])+'" r="6" stroke-width="2" style="fill:'+c+';stroke:var(--surface)"/>'});
 $(id).innerHTML=o}

function trunc(pts,lo,hi){var s=hi-lo,o=[];for(var i=0;i<pts.length;i++){o.push(pts[i]);if(pts[i][1]<lo-s||pts[i][1]>hi+s)break}return o}
