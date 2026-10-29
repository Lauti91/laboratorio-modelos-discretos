# =============== 1. Ecuación canónica de primer orden ===============
js1=r'''
var N=16,MAXV=1e9;
function prm(){return{A:+$('A').value,B:+$('B').value,y0:+$('y0').value}}
function sim(p){var y=[p.y0];for(var t=0;t<N;t++)y.push(p.A*y[t]+p.B);return y}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var p=prm(),y=sim(p),A=p.A,B=p.B,u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 var eq=Math.abs(A-1)>1e-9?B/(1-A):null;
 $('vy').textContent=eq==null?'no existe':F(eq,3);
 var c=classify1(A,B);var tt=$('vT');tt.textContent=c[0];tt.style.color=c[1];
 $('vt').textContent=k+' · '+F(y[k],3);
 $('vA').textContent=F(A,2);
 /* fase */
 var cen=eq==null?p.y0:eq;var s=eq==null?Math.max(2,Math.abs(B)*7):1.5*Math.abs(p.y0-eq)+Math.max(1,Math.abs(eq)*0.2);
 var lo=cen-s,hi=cen+s;var f=frame(420,340,46,14,14,30,lo,hi,lo,hi);
 var o=clip('cA',f)+axes(f,{xt:ticks(lo,hi,5),yt:ticks(lo,hi,5),xl:sb('y','t'),yl:sb('y','t+1')});
 o+='<g clip-path="url(#cA)">';
 o+='<line x1="'+f.X(lo)+'" y1="'+f.Y(lo)+'" x2="'+f.X(hi)+'" y2="'+f.Y(hi)+'" style="stroke:var(--faint)" stroke-dasharray="5 4"/>';
 o+='<line x1="'+f.X(lo)+'" y1="'+f.Y(A*lo+B)+'" x2="'+f.X(hi)+'" y2="'+f.Y(A*hi+B)+'" style="stroke:var(--supply)" stroke-width="2.5"/>';
 var V=[[y[0],lo]];for(var j=0;j<N;j++){V.push([y[j],y[j+1]]);V.push([y[j+1],y[j+1]])}
 var segs=2*u,full=Math.floor(segs+1e-9),part=segs-full,pts=[V[0]];
 for(var j=1;j<=Math.min(full,V.length-1);j++)pts.push(V[j]);
 var tp=pts[pts.length-1];
 if(full<V.length-1&&part>1e-6){var a=V[full],b=V[full+1];tp=[a[0]+(b[0]-a[0])*part,a[1]+(b[1]-a[1])*part];pts.push(tp)}
 o+=poly(f,pts,'var(--demand)',2);
 o+='</g>';
 if(eq!=null&&eq>lo&&eq<hi)o+='<circle cx="'+f.X(eq)+'" cy="'+f.Y(eq)+'" r="4.5" style="fill:var(--fg)"/><text x="'+(f.X(eq)+8)+'" y="'+(f.Y(eq)+16)+'" font-size="12" '+TXF+'>y*</text>';
 if(tp[0]>=lo&&tp[0]<=hi&&tp[1]>=lo&&tp[1]<=hi)o+=tip(f,tp[0],tp[1],'var(--demand)');
 o+='<text x="'+(f.L+f.w-4)+'" y="'+(f.Y(A*hi+B)>f.T+16?f.Y(A*hi+B)-6:f.T+28)+'" font-size="12" text-anchor="end" style="fill:var(--supply)" font-weight="600">y<tspan dy="3" font-size="10">t+1</tspan><tspan dy="-3"> = A·y</tspan><tspan dy="3" font-size="10">t</tspan><tspan dy="-3"> + B</tspan></text>';
 $('c1').innerHTML=o;
 /* serie */
 var vis=y.slice(0,Math.min(k+2,y.length));var vals=vis.concat(eq==null?[]:[eq]);var yr=yrange(vals,0.12);
 var f2=frame(680,230,50,16,12,28,0,N,yr[0],yr[1]);
 var q=clip('cB',f2)+axes(f2,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('y','t')});
 q+='<g clip-path="url(#cB)">';
 if(eq!=null)q+=hl(f2,eq,'y* = '+F(eq,2));
 var pv=[];for(var j=0;j<=k;j++)pv.push([j,y[j]]);
 var tpy=y[k];if(k<N&&fr>1e-6){var fh=cl(fr*2-1,0,1);tpy=y[k]+(y[k+1]-y[k])*fh;pv.push([k+fr,tpy])}
 q+=poly(f2,pv,'var(--demand)',2,3.5)+'</g>';
 if(k<N&&fr>1e-6)q+=tip(f2,k+fr,tpy,'var(--demand)');
 $('c2').innerHTML=q;
 strip1('c3',A,-2,2)}
function pre(A,B,y0){setv('A',A);setv('B',B);setv('y0',y0);An.full()}
$('b1').onclick=function(){pre(0.5,4,14)};$('b2').onclick=function(){pre(-0.5,6,12)};
$('b3').onclick=function(){pre(-1,10,3)};$('b4').onclick=function(){pre(-1.25,9,5)};
$('b5').onclick=function(){pre(1.2,-2,6)};$('b6').onclick=function(){pre(1,2,3)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
bindSliders(['A','B','y0','sp'],function(){An.fit();render()});
An.full();
'''
bar1=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">A = 0,5</button>
    <button type="button" id="b2">A = −0,5</button>
    <button type="button" id="b3">A = −1</button>
    <button type="button" id="b4">A = −1,25</button>
    <button type="button" id="b5">A = 1,2</button>
    <button type="button" id="b6">A = 1</button>
    <span class="sep"></span>''')
charts1=card('<p class="cap">Diagrama de fases: cada escalón lleva y<sub>t</sub> a y<sub>t+1</sub> a través de la recta azul y vuelve a la diagonal.</p><svg id="c1" style="max-width:520px;margin:0 auto" viewBox="0 0 420 340" role="img" aria-label="Diagrama de fases de la ecuación en diferencias"></svg>')+'\n'+card('<div class="leg"><span><i style="background:var(--demand)"></i>Trayectoria y<sub>t</sub></span></div><svg id="c2" viewBox="0 0 680 230" role="img" aria-label="Trayectoria en el tiempo"></svg>')+'\n'+card('<p class="cap">Dónde cae A: la flecha marca el valor elegido.</p><svg id="c3" viewBox="0 0 680 74" role="img" aria-label="Escala del coeficiente A"></svg>')
side1=card('<h2>Resultados</h2><div class="stats">'+stat('A','vA')+stat('y* = B/(1−A)','vy')+stat('Trayectoria','vT',True,True)+stat('Período · y<sub>t</sub>','vt',True)+'</div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('A','A (coeficiente)',-2,2,0.05,0.5)+ctl('B','B (término constante)',-10,10,0.5,4,1)+ctl('y0','y₀ (valor inicial)',-10,20,0.5,14,1)+ctl('sp','Velocidad',0.3,3,0.1,0.9,1))
page('01_ecuacion_canonica.html','Ecuación canónica de primer orden','Ecuación canónica de primer orden','Matemática Aplicada II · Herramientas',
 ['y<sub>t+1</sub> = A·y<sub>t</sub> + B','y* = B/(1−A)','y<sub>t</sub> = (y₀−y*)·A<sup>t</sup> + y*'],bar1,charts1,side1,js1)

# =============== 2. Interés y rentas ===============
js2=r'''
var mode='ic',N=12;
function prm(){return{C0:+$('C0').value,i:+$('i').value/100,n:+$('n').value,c:+$('c').value}}
function cur(){return F(0,0)&&''}
function M(x){return'$ '+F(x,0)}
var An=makeAnim(render,function(){return +$('n').value},function(){return +$('sp').value},$('pl'));
function setMode(m){mode=m;['ic','ah','pr'].forEach(function(k){$('m_'+k).className=k===m?'on':''});
 $('g_C0').hidden=m!=='ic';$('g_c').hidden=m==='ic';
 var t={ic:'Interés simple e interés compuesto',ah:'Rentas ciertas vencidas: valor final',pr:'Rentas ciertas vencidas: valor actual (préstamo)'};$('ttl').textContent=t[m];
 var e={ic:['\\(y_{t+1}=(1+i)\\,y_t\\) <small>compuesto</small>','\\(y_t=C\\,(1+i\\,t)\\) <small>simple</small>'],
  ah:['\\(S_{t+1}=(1+i)\\,S_t+c\\)','\\(S_t=\\dfrac{c}{i}\\left[(1+i)^t-1\\right]\\)'],
  pr:['\\(V_{t+1}=(1+i)\\,V_t-c\\)','\\(V_0=c\\,\\dfrac{1-(1+i)^{-n}}{i}\\)']};
 $('e1').innerHTML=e[m][0];$('e2').innerHTML=e[m][1];
 if(window.MathJax&&MathJax.typesetPromise)MathJax.typesetPromise([$('e1'),$('e2')]).catch(function(){});An.full()}
function series(p){var n=p.n,i=p.i,a=[],b=[],tot=[];
 if(mode==='ic'){for(var t=0;t<=n;t++){a.push(p.C0*(1+i*t));b.push(p.C0*Math.pow(1+i,t))}}
 else if(mode==='ah'){var S=0;for(var t=0;t<=n;t++){a.push(p.c*t);b.push(S);S=(1+i)*S+p.c}}
 else{var V=p.c*(1-Math.pow(1+i,-n))/i;for(var t=0;t<=n;t++){b.push(V);V=(1+i)*V-p.c;if(Math.abs(V)<1e-6)V=0}}
 return{a:a,b:b}}
function render(){
 var p=prm(),n=p.n,s=series(p),u=Math.min(An.u,n),k=Math.min(Math.floor(u+1e-9),n),fr=u-k;
 $('o_sp')&&0;var i=p.i,A=1+i;
 var st=$('stats');
 var A_=F(A,3);
 var leg='',o='',q='';
 var f,yr;
 var vis=function(arr){var r=arr.slice(0,k+1);if(k<n&&fr>1e-6)r.push(arr[k]+(arr[k+1]-arr[k])*fr);return r};
 function pts(arr){var r=[];for(var j=0;j<=k;j++)r.push([j,arr[j]]);if(k<n&&fr>1e-6)r.push([k+fr,arr[k]+(arr[k+1]-arr[k])*fr]);return r}
 if(mode==='ic'){
  var big=s.b[n];yr=[0,Math.max(s.a[n],big)*1.08];f=frame(680,300,76,16,12,28,0,n,yr[0],yr[1]);
  o=clip('cA',f)+axes(f,{xt:ticks(0,n,10),yt:ticks(yr[0],yr[1],5),xl:'t (períodos)',yl:'Monto',yf:function(v){return F(v,0)}});
  o+='<g clip-path="url(#cA)">'+poly(f,pts(s.a),'var(--supply)',2.4,3)+poly(f,pts(s.b),'var(--demand)',2.4,3)+'</g>';
  if(k<n&&fr>1e-6){var fv=function(arr){return arr[k]+(arr[k+1]-arr[k])*fr};o+=tip(f,k+fr,fv(s.a),'var(--supply)')+tip(f,k+fr,fv(s.b),'var(--demand)')}
  leg='<span><i style="background:var(--demand)"></i>Compuesto C(1+i)<sup>t</sup></span><span><i style="background:var(--supply)"></i>Simple C(1+i·t)</span>';
  var dif=[];for(var j=0;j<=n;j++)dif.push(s.b[j]-s.a[j]);var dm=Math.max.apply(null,dif)*1.15+1e-9;
  var f2=frame(680,150,76,16,10,28,-0.5,n+0.5,0,dm);q=axes(f2,{xt:ticks(0,n,10),yt:ticks(0,dm,3),xl:'t',yl:'Compuesto − simple',yf:function(v){return F(v,0)}});
  var bw=f2.w/(n+1)*0.7;for(var j=0;j<=k;j++){q+='<rect x="'+(f2.X(j)-bw/2)+'" y="'+f2.Y(dif[j])+'" width="'+bw+'" height="'+Math.max(0,f2.Y(0)-f2.Y(dif[j]))+'" style="fill:var(--demand);opacity:.75"/>'}
  $('l2').textContent='Cuánto le saca el compuesto al simple en cada período.';
  var dbl=Math.log(2)/Math.log(1+i);
  st.innerHTML=stat0('A = 1 + i',A_)+stat0('B','0')+stat0('Compuesto en t = '+n,M(s.b[n]))+stat0('Simple en t = '+n,M(s.a[n]))+stat0('Diferencia',M(s.b[n]-s.a[n]))+stat0('Duplicación (compuesto)',F(dbl,1)+' períodos')+stat0('Duplicación (simple)',F(1/i,1)+' períodos');
 }else if(mode==='ah'){
  var tot=s.b[n];yr=[0,tot*1.08];f=frame(680,300,76,16,12,28,0,n,yr[0],yr[1]);
  o=clip('cA',f)+axes(f,{xt:ticks(0,n,10),yt:ticks(yr[0],yr[1],5),xl:'t (períodos)',yl:'Saldo acumulado',yf:function(v){return F(v,0)}});
  o+='<g clip-path="url(#cA)">'+poly(f,pts(s.a),'var(--supply)',2,0,'5 4')+poly(f,pts(s.b),'var(--demand)',2.6,3)+'</g>';
  if(k<n&&fr>1e-6)o+=tip(f,k+fr,s.b[k]+(s.b[k+1]-s.b[k])*fr,'var(--demand)');
  leg='<span><i style="background:var(--demand)"></i>Saldo S<sub>t</sub> con intereses</span><span><i style="background:var(--supply)"></i>Solo aportes c·t</span>';
  var f2=frame(680,150,76,16,10,28,-0.5,n+0.5,0,tot*1.08);q=axes(f2,{xt:ticks(0,n,10),yt:ticks(0,tot,3),xl:'t',yl:'Aportes e intereses',yf:function(v){return F(v,0)}});
  var bw=f2.w/(n+1)*0.7;for(var j=1;j<=k;j++){var ap=s.a[j],it=s.b[j]-s.a[j];
   q+='<rect x="'+(f2.X(j)-bw/2)+'" y="'+f2.Y(ap)+'" width="'+bw+'" height="'+(f2.Y(0)-f2.Y(ap))+'" style="fill:var(--supply);opacity:.7"/>';
   q+='<rect x="'+(f2.X(j)-bw/2)+'" y="'+f2.Y(ap+it)+'" width="'+bw+'" height="'+Math.max(0,f2.Y(ap)-f2.Y(ap+it))+'" style="fill:var(--demand);opacity:.85"/>'}
  $('l2').textContent='Azul: lo aportado. Naranja: lo que sumaron los intereses.';
  st.innerHTML=stat0('A = 1 + i',A_)+stat0('B = c',M(p.c))+stat0('Valor final S<sub>n</sub>',M(tot))+stat0('Aportes totales',M(p.c*n))+stat0('Intereses ganados',M(tot-p.c*n))+stat0('Equilibrio y* = −c/i','inestable: '+M(-p.c/i));
 }else{
  var V0=s.b[0];yr=[0,V0*1.08];f=frame(680,300,76,16,12,28,0,n,yr[0],yr[1]);
  o=clip('cA',f)+axes(f,{xt:ticks(0,n,10),yt:ticks(yr[0],yr[1],5),xl:'t (cuotas pagadas)',yl:'Saldo adeudado',yf:function(v){return F(v,0)}});
  o+='<g clip-path="url(#cA)">'+poly(f,pts(s.b),'var(--demand)',2.6,3)+'</g>';
  if(k<n&&fr>1e-6)o+=tip(f,k+fr,s.b[k]+(s.b[k+1]-s.b[k])*fr,'var(--demand)');
  leg='<span><i style="background:var(--demand)"></i>Saldo V<sub>t</sub></span>';
  var cmx=p.c*1.1;var f2=frame(680,150,76,16,10,28,0.5,n+0.5,0,cmx);q=axes(f2,{xt:ticks(1,n,10),yt:ticks(0,p.c,3),xl:'cuota número',yl:'Interés y amortización',yf:function(v){return F(v,0)}});
  var bw=f2.w/(n)*0.7;for(var j=1;j<=k;j++){var intr=i*s.b[j-1],am=p.c-intr;
   q+='<rect x="'+(f2.X(j)-bw/2)+'" y="'+f2.Y(intr)+'" width="'+bw+'" height="'+(f2.Y(0)-f2.Y(intr))+'" style="fill:var(--demand);opacity:.85"/>';
   q+='<rect x="'+(f2.X(j)-bw/2)+'" y="'+f2.Y(p.c)+'" width="'+bw+'" height="'+Math.max(0,f2.Y(intr)-f2.Y(p.c))+'" style="fill:var(--supply);opacity:.7"/>'}
  $('l2').textContent='Cada cuota c se reparte: naranja es interés, azul es amortización de capital.';
  st.innerHTML=stat0('A = 1 + i',A_)+stat0('B = −c',M(-p.c))+stat0('Valor actual V₀',M(V0))+stat0('Total pagado n·c',M(p.c*n))+stat0('Intereses pagados',M(p.c*n-V0))+stat0('Equilibrio y* = c/i','inestable: '+M(p.c/i));
 }
 $('c1').innerHTML=o;$('c2').innerHTML=q;$('leg1').innerHTML=leg;
 $('vt').textContent=k+' · '+M(mode==='ic'?s.b[k]:s.b[k])}
function stat0(l,v){return'<div class="stat"><div class="l">'+l+'</div><div class="v">'+v+'</div></div>'}
$('m_ic').onclick=function(){setMode('ic')};$('m_ah').onclick=function(){setMode('ah')};$('m_pr').onclick=function(){setMode('pr')};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
bindSliders(['C0','i','n','c','sp'],function(id){An.fit();if(id==='n')An.full();render()});
setMode('ic');
'''
bar2=anim_bar('''<span class="lbl">Modelo</span>
    <button type="button" id="m_ic" class="on">Simple vs. compuesto</button>
    <button type="button" id="m_ah">Ahorro con cuotas</button>
    <button type="button" id="m_pr">Préstamo en cuotas</button>
    <span class="sep"></span>''')
charts2=card('<h2 id="ttl"></h2><div class="leg" id="leg1"></div><svg id="c1" viewBox="0 0 680 300" role="img" aria-label="Evolución del monto en el tiempo"></svg>')+'\n'+card('<p class="cap" id="l2"></p><svg id="c2" viewBox="0 0 680 150" role="img" aria-label="Descomposición por período"></svg>')
side2=card('<h2>Resultados</h2><div class="stats" id="stats"></div><div class="stat w" style="margin-top:10px"><div class="l">Período · valor</div><div class="v" id="vt"></div></div>')+'\n'+card('<h2>Parámetros</h2><div id="g_C0">'+ctl('C0','Capital inicial C',100,10000,100,1000,0)+'</div>'+ctl('i','Tasa por período i (%)',0.5,20,0.5,5,1)+ctl('n','Períodos n',1,30,1,12,0)+'<div id="g_c" hidden>'+ctl('c','Cuota c',10,1000,10,100,0)+'</div>'+ctl('sp','Velocidad',0.5,6,0.5,2,1))
page('02_interes_y_rentas.html','Interés y rentas ciertas','Interés y rentas ciertas','Matemática Aplicada II · Aplicaciones financieras',
 ['<span id="e1"></span>','<span id="e2"></span>'],bar2,charts2,side2,js2)
