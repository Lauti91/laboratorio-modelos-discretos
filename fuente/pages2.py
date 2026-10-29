# =============== helpers de mapas ===============
MAPJS=r'''
function band(f,top,bot,m0,m1,style,n){var s=[],i,m,st=(m1-m0)/(n||60);
 var cy=function(v){return cl(v,f.y0,f.y1)};
 for(i=0;i<=(n||60);i++){m=m0+i*st;s.push([f.X(m),f.Y(cy(top(m)))])}
 for(i=(n||60);i>=0;i--){m=m0+i*st;s.push([f.X(m),f.Y(cy(bot(m)))])}
 return'<polygon points="'+s.map(function(a){return a[0].toFixed(1)+','+a[1].toFixed(1)}).join(' ')+'" style="'+style+'"/>'}
function curve(f,fn,m0,m1,color,w,dash,n){var s=[],i,m,st=(m1-m0)/(n||80);for(i=0;i<=(n||80);i++){m=m0+i*st;var v=fn(m);if(v>=f.y0-1e-9&&v<=f.y1+1e-9)s.push([m,v])}
 return poly(f,s,color,w||2,0,dash)}
'''

# =============== 3. Expectativas adaptativas ===============
js3=MAPJS+r'''
var N=14;
function prm(){return{al:+$('al').value,ga:+$('ga').value,be:+$('be').value,de:+$('de').value,eta:+$('eta').value,d:+$('d').value}}
function model(p){var mu=p.de/p.be,g=(p.al+p.ga)/p.be,Ps=g/(1+mu),Aa=1-p.eta*(1+mu),Ao=-mu;
 var P=[Ps+p.d],Q=[Ps+p.d],E=[];for(var t=0;t<N;t++){P.push(Aa*P[t]+p.eta*g);Q.push(Ao*Q[t]+g)}
 for(var t=0;t<=N;t++)E.push((g-P[t])/mu);return{mu:mu,g:g,Ps:Ps,Aa:Aa,Ao:Ao,P:P,Q:Q,E:E,thr:(2-p.eta)/p.eta}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
var MF;
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 function pts(arr){var r=[];for(var j=0;j<=k;j++)r.push([j,arr[j]]);var v=arr[k];if(k<N&&fr>1e-6){v=arr[k]+(arr[k+1]-arr[k])*cl(fr*2-1,0,1);r.push([k+fr,v])}return[r,v]}
 var a=pts(m.P),b=pts(m.Q),e=pts(m.E);
 var all=a[0].map(function(z){return z[1]}).concat([m.Ps]);var yr=yrange(all,0.12);
 var f=frame(680,250,50,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('P','t')});
 o+='<g clip-path="url(#cA)">'+hl(f,m.Ps,'P* = '+F(m.Ps,2))+poly(f,trunc(b[0],yr[0],yr[1]),'var(--supply)',2,2.5,'6 4')+poly(f,a[0],'var(--demand)',2.4,3.5)+'</g>';
 if(k<N&&fr>1e-6)o+=tip(f,k+fr,a[1],'var(--demand)');
 $('c1').innerHTML=o;
 var all2=a[0].map(function(z){return z[1]}).concat(e[0].map(function(z){return z[1]}),[m.Ps]);var y2=yrange(all2,0.12);
 var g2=frame(340,230,44,10,12,28,0,N,y2[0],y2[1]);
 var q=clip('cB',g2)+axes(g2,{xt:ticks(0,N,5),yt:ticks(y2[0],y2[1],4),xl:'t'});
 q+='<g clip-path="url(#cB)">'+hl(g2,m.Ps,null)+poly(g2,e[0],'var(--c3)',2,2.5)+poly(g2,a[0],'var(--demand)',2.2,2.5)+'</g>';
 $('c2').innerHTML=q;
 /* mapa mu-eta */
 var f3=frame(340,230,40,10,12,28,0,4.5,0,1.05);MF=f3;
 var r=clip('cC',f3)+axes(f3,{xt:ticks(0,4.5,5),yt:[0,0.5,1],xl:'δ/β',yl:'η'});
 r+='<g clip-path="url(#cC)">';
 r+=band(f3,function(x){return x<1?1.05:Math.min(1.05,2/(1+x))},function(){return 0},0,4.5,'fill:var(--okfill)',90);
 r+=band(f3,function(x){return Math.min(1.05,1/(1+x))},function(){return 0},0,4.5,'fill:var(--okfill);opacity:.0',2);
 r+=curve(f3,function(x){return 2/(1+x)},0.9,4.5,'var(--bad)',2.2);
 r+=curve(f3,function(x){return 1/(1+x)},0,4.5,'var(--good)',1.6,'5 4');
 r+='<line x1="'+f3.L+'" x2="'+(f3.L+f3.w)+'" y1="'+f3.Y(1)+'" y2="'+f3.Y(1)+'" style="stroke:var(--supply)" stroke-dasharray="3 3"/>';
 r+='</g>';
 r+='<text x="'+f3.X(3.3)+'" y="'+f3.Y(0.13)+'" font-size="11" text-anchor="middle" '+TX+'>estable</text><text x="'+f3.X(3.3)+'" y="'+f3.Y(0.75)+'" font-size="11" text-anchor="middle" '+TX+'>explosiva</text>';
 r+='<text x="'+(f3.L+f3.w-3)+'" y="'+(f3.Y(1)-4)+'" font-size="10" text-anchor="end" style="fill:var(--supply)">η = 1 (telaraña)</text>';
 var mx=cl(m.mu,0,4.5),my=cl(p.eta,0,1.05);
 r+='<circle cx="'+f3.X(mx)+'" cy="'+f3.Y(my)+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 var c=classify1(m.Aa,1);var tt=$('vT');tt.textContent=c[0];tt.style.color=c[1];
 $('vA').textContent=F(m.Aa,3);$('vAo').textContent=F(m.Ao,3);$('vP').textContent=F(m.Ps,3);$('vthr').textContent=F(m.mu,2)+' vs '+F(m.thr,2);
 $('vt').textContent=k+' · '+F(m.P[k],3);
 var neg=m.P.slice(0,k+1).some(function(v){return v<0});$('msg').textContent=neg?'El precio resulta negativo: el modelo lineal deja de tener sentido.':'';
 var cmp=m.Ao<=-1&&Math.abs(m.Aa)<1?'Con η = '+F(p.eta,2)+' el mercado converge aunque la telaraña estándar explota.':(Math.abs(m.Ao)<1&&Math.abs(m.Aa)>=1?'Atención: la telaraña estándar converge, pero con este η no.':'');
 $('note').textContent=cmp}
function pre(al,ga,be,de,eta,d){setv('al',al);setv('ga',ga);setv('be',be);setv('de',de);setv('eta',eta);setv('d',d);An.full()}
$('b1').onclick=function(){pre(10,2,1,2,0.5,0.4)};$('b2').onclick=function(){pre(10,2,1,2,1,0.4)};
$('b3').onclick=function(){pre(10,2,2,1,0.3,1)};$('b4').onclick=function(){pre(10,2,1,2,0.85,0.4)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
drag($('c3'),function(xy){var mu=cl(MF.ix(xy[0]),0.1,4.5),eta=cl(MF.iy(xy[1]),0.05,1);setv('eta',Math.round(eta*20)/20);setv('de',Math.round(cl(mu*(+$('be').value),0.5,6)*10)/10);An.fit();render()});
bindSliders(['al','ga','be','de','eta','d','sp'],function(){An.fit();render()});
An.full();
'''
bar3=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">η = 0,5 (estabiliza)</button>
    <button type="button" id="b2">η = 1 (telaraña)</button>
    <button type="button" id="b3">Mercado estable, η bajo</button>
    <button type="button" id="b4">η = 0,85</button>
    <span class="sep"></span>''')
charts3=card('<div class="leg"><span><i style="background:var(--demand)"></i>Precio P<sub>t</sub> (adaptativas)</span><span><i style="background:var(--supply)"></i>Telaraña estándar (η = 1); si explota, sale del gráfico</span></div><svg id="c1" viewBox="0 0 680 250" role="img" aria-label="Precio en el tiempo con expectativas adaptativas y con telaraña estándar"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Precio P<sub>t</sub> y precio esperado P<sup>e</sup><sub>t</sub> (violeta).</p><svg id="c2" viewBox="0 0 340 230" role="img" aria-label="Precio y precio esperado"></svg>')+'\n'+card('<p class="cap">Mapa de estabilidad: tocá o arrastrá para cambiar δ/β y η.</p><svg id="c3" viewBox="0 0 340 230" role="img" aria-label="Región de estabilidad en el plano δ sobre β y η"></svg><p class="hint">Verde: A = 0. Rojo: A = −1. Estable debajo del rojo.</p>')+'\n      </div>'
side3=card('<h2>Resultados</h2><div class="stats">'+stat('A = 1 − η(1+δ/β)','vA')+stat('A telaraña = −δ/β','vAo')+stat('P*','vP')+stat('δ/β vs (2−η)/η','vthr')+stat('Trayectoria','vT',True,True)+stat('Período · P<sub>t</sub>','vt',True)+'</div><div id="msg" role="status"></div><p class="hint" id="note"></p>')+'\n'+card('<h2>Parámetros</h2>'+ctl('al','α (demanda)',6,20,0.5,10,1)+ctl('ga','γ (oferta)',0,6,0.5,2,1)+ctl('be','β (pendiente de D)',0.5,4,0.1,1,1)+ctl('de','δ (pendiente de S)',0.5,6,0.1,2,1)+ctl('eta','η (velocidad de ajuste)',0.05,1,0.05,0.5,2)+ctl('d','P₀ − P*',-2,3,0.1,0.4,1)+ctl('sp','Velocidad',0.3,3,0.1,1,1))
page('03_expectativas_adaptativas.html','Expectativas adaptativas','Expectativas adaptativas','Matemática Aplicada II · Telaraña con expectativas adaptativas',
 ['P<sup>e</sup><sub>t</sub> = P<sup>e</sup><sub>t−1</sub> + η·(P<sub>t−1</sub> − P<sup>e</sup><sub>t−1</sub>)','P<sub>t+1</sub> = A·P<sub>t</sub> + η(α+γ)/β','A = 1 − η(1 + δ/β)'],bar3,charts3,side3,js3)

# =============== 4. Mercado con inventarios ===============
js4=r'''
var N=14;
function prm(){return{al:+$('al').value,ga:+$('ga').value,be:+$('be').value,de:+$('de').value,sg:+$('sg').value,d:+$('d').value}}
function updSigma(keep){var s=prm(),mx=3/(s.be+s.de);var e=$('sg');var t=+e.value/(+e.max||mx);e.max=mx;e.step=mx/150;if(!keep)e.value=cl(t*mx,mx/150,mx);setv('sg',+e.value)}
function model(p){var b=p.be+p.de,Ps=(p.al+p.ga)/b,A=1-p.sg*b,B=p.sg*(p.al+p.ga);var P=[Ps+p.d];for(var t=0;t<N;t++)P.push(A*P[t]+B);
 var dI=P.map(function(v){return b*v-(p.al+p.ga)});return{b:b,Ps:Ps,A:A,P:P,dI:dI,s:p.sg*b}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 var Pk=m.P[k]+(k<N?(m.P[k+1]-m.P[k])*cl(fr*2-1,0,1):0);
 /* mercado */
 var Pmax=p.al/p.be*1.08,Qmax=p.al*1.05;var f=frame(420,300,46,14,12,30,0,Qmax,0,Pmax);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,Qmax,5),yt:ticks(0,Pmax,5),xl:'Q',yl:'P'});
 o+='<g clip-path="url(#cA)">';
 o+='<line x1="'+f.X(0)+'" y1="'+f.Y(p.al/p.be)+'" x2="'+f.X(p.al)+'" y2="'+f.Y(0)+'" style="stroke:var(--demand)" stroke-width="2.5"/>';
 o+='<line x1="'+f.X(0)+'" y1="'+f.Y(p.ga/p.de)+'" x2="'+f.X(Qmax)+'" y2="'+f.Y((Qmax+p.ga)/p.de)+'" style="stroke:var(--supply)" stroke-width="2.5"/>';
 var qd=p.al-p.be*Pk,qs=-p.ga+p.de*Pk;
 o+='<rect x="'+f.X(Math.min(qd,qs))+'" y="'+(f.Y(Pk)-4)+'" width="'+Math.abs(f.X(qs)-f.X(qd))+'" height="8" style="fill:'+(qs>qd?'var(--demand)':'var(--supply)')+';opacity:.35"/>';
 o+='<line x1="'+f.L+'" x2="'+(f.L+f.w)+'" y1="'+f.Y(Pk)+'" y2="'+f.Y(Pk)+'" style="stroke:var(--faint)" stroke-dasharray="3 3"/>';
 for(var j=0;j<=k;j++)o+='<circle cx="'+f.L+'" cy="'+f.Y(m.P[j])+'" r="3" style="fill:var(--fg)"/>';
 o+='<circle cx="'+f.X(qd)+'" cy="'+f.Y(Pk)+'" r="5" style="fill:var(--demand);stroke:var(--surface)" stroke-width="2"/><circle cx="'+f.X(qs)+'" cy="'+f.Y(Pk)+'" r="5" style="fill:var(--supply);stroke:var(--surface)" stroke-width="2"/>';
 o+='<circle cx="'+f.X(p.al-p.be*m.Ps)+'" cy="'+f.Y(m.Ps)+'" r="4.5" style="fill:var(--fg)"/>';
 o+='</g><text x="'+(f.X(p.al)-6)+'" y="'+(f.Y(0)-8)+'" font-size="13" font-weight="600" text-anchor="end" style="fill:var(--demand)">D</text>';
 o+='<text x="'+(f.L+f.w-18)+'" y="'+(f.T+14)+'" font-size="13" font-weight="600" style="fill:var(--supply)">S</text>';
 $('c1').innerHTML=o;
 $('gap').textContent=(qs>qd+1e-6?'Exceso de oferta: ':qs<qd-1e-6?'Exceso de demanda: ':'Mercado en equilibrio: ')+F(Math.abs(qs-qd),2)+' unidades';
 /* precio */
 var vis=[];for(var j=0;j<=k;j++)vis.push([j,m.P[j]]);var tp=m.P[k];if(k<N&&fr>1e-6){tp=Pk;vis.push([k+fr,Pk])}
 var yr=yrange(vis.map(function(z){return z[1]}).concat([m.Ps]),0.12);var f2=frame(680,210,50,16,12,28,0,N,yr[0],yr[1]);
 var q=clip('cB',f2)+axes(f2,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('P','t')});
 q+='<g clip-path="url(#cB)">'+hl(f2,m.Ps,'P* = '+F(m.Ps,2))+poly(f2,vis,'var(--demand)',2.4,3.5)+'</g>';if(k<N&&fr>1e-6)q+=tip(f2,k+fr,Pk,'var(--demand)');
 $('c2').innerHTML=q;
 /* inventario */
 var dv=m.dI.slice(0,k+1);var mxv=Math.max(1,Math.max.apply(null,dv.map(Math.abs)))*1.15;
 var f3=frame(680,170,50,16,10,28,-0.5,N+0.5,-mxv,mxv);var r=axes(f3,{xt:ticks(0,N,8),yt:[-mxv/1.15,0,mxv/1.15],xl:'t',yf:function(v){return F(v,1)}});
 r+='<line x1="'+f3.L+'" x2="'+(f3.L+f3.w)+'" y1="'+f3.Y(0)+'" y2="'+f3.Y(0)+'" '+AX+'/>';
 var bw=f3.w/(N+1)*0.65;dv.forEach(function(v,j){var y0=f3.Y(Math.max(v,0)),h=Math.abs(f3.Y(v)-f3.Y(0));r+='<rect x="'+(f3.X(j)-bw/2)+'" y="'+y0+'" width="'+bw+'" height="'+h+'" style="fill:'+(v>0?'var(--demand)':'var(--supply)')+';opacity:.8"/>'});
 $('c3').innerHTML=r;
 strip1('c4',m.s,0,3,[[0,1,'monótona amortiguada','var(--good)'],[1,2,'oscilación amortiguada','var(--good)'],[2,3,'oscilación explosiva','var(--bad)']]);
 var c=classify1(m.A,1);var tt=$('vT');tt.textContent=c[0];tt.style.color=c[1];
 $('vA').textContent=F(m.A,3);$('vP').textContent=F(m.Ps,3);$('vs').textContent=F(m.s,2)+' (σ = '+F(p.sg,3)+')';$('vt').textContent=k+' · '+F(m.P[k],3);
 var neg=m.P.slice(0,k+1).some(function(v){return v<0});$('msg').textContent=neg?'El precio resulta negativo: el modelo lineal deja de tener sentido.':''}
function pre(s){updSigma(true);var b=(+$('be').value)+(+$('de').value);setv('sg',s/b);An.full()}
$('b1').onclick=function(){pre(0.5)};$('b2').onclick=function(){pre(1.5)};$('b3').onclick=function(){pre(2)};$('b4').onclick=function(){pre(2.5)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
bindSliders(['al','ga','be','de','sg','d','sp'],function(id){if(id==='be'||id==='de')updSigma(false);An.fit();render()});
updSigma(true);setv('sg',1.5/3);An.full();
'''
bar4=anim_bar('''<span class="lbl">Ajuste σ(β+δ)</span>
    <button type="button" id="b1">0,5 monótona</button>
    <button type="button" id="b2">1,5 amortiguada</button>
    <button type="button" id="b3">2 uniforme</button>
    <button type="button" id="b4">2,5 explosiva</button>
    <span class="sep"></span>''')
charts4=card('<p class="cap">Mercado: el precio P<sub>t</sub> fija cuánto se ofrece (punto azul) y cuánto se demanda (punto naranja). La diferencia se acumula como inventario.</p><svg id="c1" style="max-width:520px;margin:0 auto" viewBox="0 0 420 300" role="img" aria-label="Oferta, demanda y precio vigente"></svg><p class="cap" id="gap" style="margin-top:6px"></p>')+'\n'+card('<svg id="c2" viewBox="0 0 680 210" role="img" aria-label="Precio en el tiempo"></svg>')+'\n'+card('<p class="cap">Cambio de inventario en cada período: Q<sup>s</sup> − Q<sup>d</sup>. Naranja se acumula stock; azul se vacía.</p><svg id="c3" viewBox="0 0 680 170" role="img" aria-label="Variación de inventarios"></svg>')+'\n'+card('<p class="cap">Velocidad de ajuste σ(β+δ) = 1 − A.</p><svg id="c4" viewBox="0 0 680 74" role="img" aria-label="Zonas de estabilidad según el ajuste"></svg>')
side4=card('<h2>Resultados</h2><div class="stats">'+stat('A = 1 − σ(β+δ)','vA')+stat('P*','vP')+stat('σ(β+δ)','vs',True)+stat('Trayectoria','vT',True,True)+stat('Período · P<sub>t</sub>','vt',True)+'</div><div id="msg" role="status"></div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('al','α (demanda)',6,20,0.5,10,1)+ctl('ga','γ (oferta)',0,6,0.5,2,1)+ctl('be','β (pendiente de D)',0.5,4,0.1,1,1)+ctl('de','δ (pendiente de S)',0.5,4,0.1,2,1)+ctl('sg','σ (ajuste del precio)',0.01,1,0.01,0.5,3)+ctl('d','P₀ − P*',-2,3,0.1,0.4,1)+ctl('sp','Velocidad',0.3,3,0.1,1,1))
page('04_mercado_con_inventarios.html','Mercado con inventarios','Mercado con inventarios','Matemática Aplicada II · Ajuste de precios según el inventario',
 ['P<sub>t+1</sub> = P<sub>t</sub> − σ·(Q<sup>s</sup><sub>t</sub> − Q<sup>d</sup><sub>t</sub>)','A = 1 − σ(β+δ)','estable ⇔ σ &lt; 2/(β+δ)'],bar4,charts4,side4,js4)
