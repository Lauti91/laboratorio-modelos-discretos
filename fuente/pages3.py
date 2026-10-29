# =============== 5. Telaraña con extrapolación (2º orden) ===============
js5=MAPJS+r'''
var N=24,MF;
function prm(){return{al:+$('al').value,ga:+$('ga').value,be:+$('be').value,de:+$('de').value,phi:+$('phi').value,d:+$('d').value}}
function model(p){var mu=p.de/p.be,g=(p.al+p.ga)/p.be,Ps=g/(1+mu),pp=mu*(1+p.phi),qq=-mu*p.phi,P0=Ps+p.d;
 return{mu:mu,g:g,Ps:Ps,pp:pp,qq:qq,y:sim2(pp,qq,g,P0,g-mu*P0,N),yn:sim2(mu,0,g,P0,g-mu*P0,N),cls:classify2(pp,qq)}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function phi1(m){var s=Math.sqrt(1+m);return-(s-1)/(s+1)}
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 function pts(arr){var r=[];for(var j=0;j<=k;j++)r.push([j,arr[j]]);var v=arr[k];if(k<N&&fr>1e-6){v=arr[k]+(arr[k+1]-arr[k])*cl(fr*2-1,0,1);r.push([k+fr,v])}return[r,v]}
 var a=pts(m.y),b=pts(m.yn);
 var yr=yrange(a[0].map(function(z){return z[1]}).concat([m.Ps]),0.12);
 var f=frame(680,260,50,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('P','t')});
 o+='<g clip-path="url(#cA)">'+hl(f,m.Ps,'P* = '+F(m.Ps,2))+poly(f,trunc(b[0],yr[0],yr[1]),'var(--supply)',1.8,0,'6 4')+poly(f,a[0],'var(--demand)',2.4,3)+'</g>';
 if(k<N&&fr>1e-6)o+=tip(f,k+fr,a[1],'var(--demand)');
 $('c1').innerHTML=o;
 /* mapa (mu, phi) */
 var f3=frame(340,300,40,10,12,28,0.25,4,-3.2,1.4);MF=f3;
 var r=clip('cC',f3)+axes(f3,{xt:[1,2,3,4],yt:[-3,-2,-1,0,1],xl:'μ = δ/β',yl:'φ'});
 r+='<g clip-path="url(#cC)">';
 var up=function(x){return(1/x-1)/2},lo=function(x){return-1/x};
 r+=band(f3,up,phi1,0.25,3,'fill:var(--zone1)',70);r+=band(f3,phi1,lo,0.25,3,'fill:var(--zone2)',70);
 r+=curve(f3,up,0.25,4,'var(--demand)',2.2);r+=curve(f3,lo,0.25,4,'var(--supply)',2.2);r+=curve(f3,phi1,0.25,4,'var(--faint)',1.4,'5 4');
 r+='<line x1="'+f3.L+'" x2="'+(f3.L+f3.w)+'" y1="'+f3.Y(0)+'" y2="'+f3.Y(0)+'" style="stroke:var(--faint)" stroke-dasharray="2 3"/>';
 r+='</g>';
 var mx=cl(m.mu,0.25,4),my=cl(p.phi,-3.2,1.4);
 r+='<circle cx="'+f3.X(mx)+'" cy="'+f3.Y(my)+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 r+='<text x="'+f3.X(2.55)+'" y="'+f3.Y(-0.82)+'" font-size="10.5" '+TX+'>estable</text><text x="'+f3.X(2.6)+'" y="'+f3.Y(0.7)+'" font-size="10.5" '+TX+'>inestable</text>';
 $('c3').innerHTML=r;
 argand('c4',m.pp,m.qq);
 var c=m.cls,tt=$('vT');tt.textContent=c.txt;tt.style.color=c.col;
 $('vp').textContent=F(m.pp,3);$('vq').textContent=F(m.qq,3);$('vP').textContent=F(m.Ps,3);
 $('vr').textContent=fmtRoots(c.r);$('vm').textContent=F(c.r.maxabs,3);$('vTc').textContent=c.T?F(c.T,1)+' períodos':'—';
 $('vb').textContent=F(-1/m.mu,2)+' < φ < '+F((1-m.mu)/(2*m.mu),2);
 var neg=m.y.slice(0,k+1).some(function(v){return v<0});$('msg').textContent=neg?'El precio resulta negativo: el modelo lineal deja de tener sentido.':''}
function pre(al,ga,be,de,phi,d){setv('al',al);setv('ga',ga);setv('be',be);setv('de',de);setv('phi',phi);setv('d',d);An.full()}
$('b1').onclick=function(){pre(10,2,2,1,0,1)};$('b2').onclick=function(){pre(10,2,2,1,0.4,1)};$('b3').onclick=function(){pre(10,2,2,1,1,1)};
$('b4').onclick=function(){pre(10,2,1,2,0,0.4)};$('b5').onclick=function(){pre(10,2,1,2,-0.4,0.4)};$('b6').onclick=function(){pre(10,2,1,2,-0.6,0.4)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
drag($('c3'),function(xy){var mu=cl(MF.ix(xy[0]),0.25,4),ph=cl(MF.iy(xy[1]),-4,2);setv('phi',Math.round(ph*20)/20);setv('de',Math.round(cl(mu*(+$('be').value),0.5,6)*10)/10);An.fit();render()});
bindSliders(['al','ga','be','de','phi','d','sp'],function(){An.fit();render()});
An.full();
'''
bar5=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">Estable, φ = 0</button>
    <button type="button" id="b2">φ = 0,4</button>
    <button type="button" id="b3">φ = 1</button>
    <button type="button" id="b4">Explosivo, φ = 0</button>
    <button type="button" id="b5">φ = −0,4</button>
    <button type="button" id="b6">φ = −0,6</button>
    <span class="sep"></span>''')
charts5=card('<div class="leg"><span><i style="background:var(--demand)"></i>Con extrapolación (φ elegido)</span><span><i style="background:var(--supply)"></i>Telaraña estándar (φ = 0); si explota, sale del gráfico</span></div><svg id="c1" viewBox="0 0 680 260" role="img" aria-label="Precio en el tiempo con extrapolación de tendencia"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (δ/β, φ): tocá o arrastrá para cambiar δ y φ.</p><div class="leg"><span><i class="sq" style="background:var(--zone1)"></i>estable, zigzag</span><span><i class="sq" style="background:var(--zone2)"></i>estable, ciclo</span></div><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Región de estabilidad en el plano mu y phi"></svg>')+'\n'+card('<p class="cap">Raíces en el plano complejo: estables si caen dentro del círculo unidad.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side5=card('<h2>Resultados</h2><div class="stats">'+stat('p = μ(1+φ)','vp')+stat('q = −μφ','vq')+stat('P*','vP')+stat('max |r|','vm')+stat('Raíces','vr',True)+stat('Rango estable de φ','vb',True)+stat('Período del ciclo','vTc',True)+stat('Trayectoria','vT',True,True)+'</div><div id="msg" role="status"></div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('al','α (demanda)',6,20,0.5,10,1)+ctl('ga','γ (oferta)',0,6,0.5,2,1)+ctl('be','β (pendiente de D)',0.5,4,0.1,1,1)+ctl('de','δ (pendiente de S)',0.5,6,0.1,2,1)+ctl('phi','φ (extrapolación)',-4,2,0.05,-0.4,2)+ctl('d','P₀ − P* (con P₋₁ = P₀)',-3,3,0.1,0.4,1)+ctl('sp','Velocidad',0.5,6,0.5,3,1))
page('05_telarana_extrapolacion.html','Telaraña con extrapolación','Telaraña con extrapolación de tendencia','Matemática Aplicada II · Ecuaciones de segundo orden',
 ['P<sup>e</sup><sub>t</sub> = P<sub>t−1</sub> + φ·(P<sub>t−1</sub> − P<sub>t−2</sub>)','P<sub>t+2</sub> + μ(1+φ)·P<sub>t+1</sub> − μφ·P<sub>t</sub> = (α+γ)/β','μ = δ/β'],bar5,charts5,side5,js5)

# =============== 6. Metzler ===============
js6=MAPJS+r'''
var N=24,MF;
function prm(){return{c:+$('c').value,k:+$('k').value,V:+$('V').value,sh:+$('sh').value}}
function model(p){var pp=-p.c*(2+p.k),qq=p.c*(1+p.k),Ys=p.V/(1-p.c);var y=sim2(pp,qq,p.V,Ys,Ys+p.sh,N+1).slice(1);
 var prod=p.c*(1+p.k),kb=2*((1-p.c)+Math.sqrt(1-p.c))/p.c,reg;
 if(prod<1-1e-9)reg=['Oscilante amortiguado (estable)','var(--good)'];else if(Math.abs(prod-1)<=1e-9)reg=['Oscilante de amplitud constante','var(--warn)'];
 else if(p.k<kb-1e-9)reg=['Oscilante explosivo','var(--bad)'];else reg=['Monótono explosivo','var(--bad)'];
 return{pp:pp,qq:qq,Ys:Ys,y:y,prod:prod,kb:kb,reg:reg,cls:classify2(pp,qq)}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 var vis=[];for(var j=0;j<=k;j++)vis.push([j,m.y[j]]);var tv=m.y[k];if(k<N&&fr>1e-6){tv=m.y[k]+(m.y[k+1]-m.y[k])*cl(fr*2-1,0,1);vis.push([k+fr,tv])}
 var yr=yrange(vis.map(function(z){return z[1]}).concat([m.Ys]),0.1);
 var f=frame(680,270,56,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('Y','t'),yf:function(v){return F(v,0)}});
 o+='<g clip-path="url(#cA)">'+hl(f,m.Ys,'Y* = '+F(m.Ys,1))+poly(f,vis,'var(--demand)',2.4,3)+'</g>';
 if(k<N&&fr>1e-6)o+=tip(f,k+fr,tv,'var(--demand)');
 $('c1').innerHTML=o;
 var f3=frame(340,300,40,10,12,28,0,4,0,1);MF=f3;
 var c1=function(x){return 1/(1+x)},c2=function(x){return 4*(1+x)/((2+x)*(2+x))};
 var r=clip('cC',f3)+axes(f3,{xt:[1,2,3,4],yt:[0,0.5,1],xl:'k',yl:'c'});
 r+='<g clip-path="url(#cC)">'+band(f3,c1,function(){return 0},0,4,'fill:var(--okfill)',60)+band(f3,c2,c1,0,4,'fill:var(--zone1)',60)+band(f3,function(){return 1},c2,0,4,'fill:var(--zone2)',60);
 r+=curve(f3,c1,0,4,'var(--supply)',2.2)+curve(f3,c2,0,4,'var(--demand)',2.2)+'</g>';
 r+='<text x="'+f3.X(2.3)+'" y="'+f3.Y(0.12)+'" font-size="10.5" text-anchor="middle" '+TX+'>estable</text><text x="'+f3.X(1.55)+'" y="'+f3.Y(0.65)+'" font-size="10.5" text-anchor="middle" '+TX+'>oscilante explosivo</text><text x="'+f3.X(3)+'" y="'+f3.Y(0.9)+'" font-size="10.5" text-anchor="middle" '+TX+'>monótono explosivo</text>';
 r+='<circle cx="'+f3.X(p.k)+'" cy="'+f3.Y(p.c)+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 argand('c4',m.pp,m.qq);
 var tt=$('vT');tt.textContent=m.reg[0];tt.style.color=m.reg[1];
 $('vcp').textContent=F(m.prod,3);$('vY').textContent=F(m.Ys,2);$('vr').textContent=fmtRoots(m.cls.r);$('vm').textContent=F(m.cls.r.maxabs,3);
 $('vTc').textContent=m.cls.T?F(m.cls.T,1)+' períodos':'—';$('vkb').textContent=F((1-p.c)/p.c,3)+' ; '+F(m.kb,3);
 $('vt').textContent=k+' · '+F(m.y[k],2)}
function pre(k){setv('c',0.8);setv('k',k);setv('V',20);setv('sh',10);An.full()}
$('b1').onclick=function(){pre(0.1)};$('b2').onclick=function(){pre(0.25)};$('b3').onclick=function(){pre(0.5)};$('b4').onclick=function(){pre(2)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
drag($('c3'),function(xy){setv('k',Math.round(cl(MF.ix(xy[0]),0,3)*100)/100);setv('c',Math.round(cl(MF.iy(xy[1]),0.1,0.99)*100)/100);An.fit();render()});
bindSliders(['c','k','V','sh','sp'],function(){An.fit();render()});
An.full();
'''
bar6=anim_bar('''<span class="lbl">Casos (c = 0,8)</span>
    <button type="button" id="b1">k = 0,1 amortiguado</button>
    <button type="button" id="b2">k = 0,25 amplitud constante</button>
    <button type="button" id="b3">k = 0,5 explosivo</button>
    <button type="button" id="b4">k = 2 monótono</button>
    <span class="sep"></span>''')
charts6=card('<p class="cap">Ingreso después de un shock: la economía estaba en Y* y en t = 0 el ingreso sube.</p><svg id="c1" viewBox="0 0 680 270" role="img" aria-label="Ingreso en el tiempo"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (k, c): tocá o arrastrá para cambiar k y c.</p><div class="leg"><span><i class="sq" style="background:var(--okfill)"></i>estable</span><span><i class="sq" style="background:var(--zone1)"></i>oscilante explosivo</span><span><i class="sq" style="background:var(--zone2)"></i>monótono explosivo</span></div><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Regiones dinámicas en el plano k y c"></svg>')+'\n'+card('<p class="cap">Raíces en el plano complejo: estables dentro del círculo unidad.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side6=card('<h2>Resultados</h2><div class="stats">'+stat('c(1+k)','vcp')+stat('Y* = V₀/(1−c)','vY')+stat('max |r|','vm')+stat('Período del ciclo','vTc')+stat('Raíces','vr',True)+stat('Cortes: (1−c)/c ; k̄','vkb',True)+stat('Régimen','vT',True,True)+stat('Período · Y<sub>t</sub>','vt',True)+'</div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('c','c (propensión al consumo)',0.1,0.99,0.01,0.8,2)+ctl('k','k (stock deseado / ventas)',0,3,0.01,0.1,2)+ctl('V','V₀ (inversión autónoma)',5,50,1,20,0)+ctl('sh','Shock Y₀ − Y*',2,30,1,10,0)+ctl('sp','Velocidad',0.5,6,0.5,3,1))
page('06_inventarios_de_metzler.html','Inventarios de Metzler','Modelo de inventarios de Metzler','Matemática Aplicada II · Ecuaciones de segundo orden',
 ['Y<sub>t+2</sub> − c(2+k)·Y<sub>t+1</sub> + c(1+k)·Y<sub>t</sub> = V₀','Y* = V₀/(1−c)','estable ⇔ c(1+k) &lt; 1'],bar6,charts6,side6,js6)

# =============== 7. Triángulo de estabilidad ===============
js7=MAPJS+r'''
var N=24,MF;
function prm(){return{p:+$('p').value,q:+$('q').value,g:+$('g').value,y0:+$('y0').value,y1:+$('y1').value}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var s=prm(),cls=classify2(s.p,s.q),y=sim2(s.p,s.q,s.g,s.y0,s.y1,N),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 var den=1+s.p+s.q,eq=Math.abs(den)>1e-9?s.g/den:null;
 var vis=[];for(var j=0;j<=k;j++)vis.push([j,y[j]]);var tv=y[k];if(k<N&&fr>1e-6){tv=y[k]+(y[k+1]-y[k])*cl(fr*2-1,0,1);vis.push([k+fr,tv])}
 var yr=yrange(vis.map(function(z){return z[1]}).concat(eq==null?[]:[eq]),0.1);
 var f=frame(680,270,56,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('y','t'),yf:function(v){return F(v,0)}});
 o+='<g clip-path="url(#cA)">'+(eq==null?'':hl(f,eq,'y* = '+F(eq,2)))+poly(f,vis,'var(--demand)',2.4,3)+'</g>';
 if(k<N&&fr>1e-6)o+=tip(f,k+fr,tv,'var(--demand)');
 $('c1').innerHTML=o;
 var f3=frame(340,300,40,10,12,28,-3,3,-1.5,2.4);MF=f3;
 var r=clip('cC',f3)+axes(f3,{xt:[-2,-1,0,1,2],yt:[-1,0,1,2],xl:'p',yl:'q'});
 r+='<polygon points="'+f3.X(-2)+','+f3.Y(1)+' '+f3.X(2)+','+f3.Y(1)+' '+f3.X(0)+','+f3.Y(-1)+'" style="fill:var(--okfill);stroke:var(--good)" stroke-width="2"/>';
 r+='<g clip-path="url(#cC)">'+curve(f3,function(x){return x*x/4},-3,3,'var(--faint)',1.6,'5 4',100)+'</g>';
 r+='<text x="'+f3.X(0)+'" y="'+f3.Y(0.55)+'" font-size="11" text-anchor="middle" '+TX+'>complejas</text><text x="'+f3.X(0)+'" y="'+f3.Y(-0.5)+'" font-size="11" text-anchor="middle" '+TX+'>reales</text>';
 r+='<text x="'+f3.X(0)+'" y="'+(f3.Y(1)-5)+'" font-size="10.5" text-anchor="middle" '+TX+'>q = 1</text><text x="'+(f3.X(-1)-6)+'" y="'+f3.Y(-0.1)+'" font-size="10.5" text-anchor="end" '+TX+'>1+p+q = 0</text><text x="'+(f3.X(1)+6)+'" y="'+f3.Y(-0.1)+'" font-size="10.5" '+TX+'>1−p+q = 0</text>';
 r+='<circle cx="'+f3.X(cl(s.p,-3,3))+'" cy="'+f3.Y(cl(s.q,-1.5,2.4))+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 argand('c4',s.p,s.q);
 var tt=$('vT');tt.textContent=cls.txt;tt.style.color=cls.col;
 $('vD').textContent=F(s.p*s.p-4*s.q,3);$('vr').textContent=fmtRoots(cls.r);$('vm').textContent=F(cls.r.maxabs,3);
 $('vTc').textContent=cls.T?F(cls.T,1)+' períodos':'—';$('vy').textContent=eq==null?'no existe':F(eq,3);
 $('c1c').textContent=F(1-s.q,3);$('c2c').textContent=F(1+s.p+s.q,3);$('c3c').textContent=F(1-s.p+s.q,3);
 ['c1c','c2c','c3c'].forEach(function(i){var v=parseFloat($(i).textContent.replace(',','.'));$(i).style.color=v>1e-9?'var(--good)':'var(--bad)'})}
function pre(p,q){setv('p',p);setv('q',q);An.full()}
$('b1').onclick=function(){pre(-1,0.5)};$('b2').onclick=function(){pre(1.2,0.3)};$('b3').onclick=function(){pre(-1.2,0.3)};
$('b4').onclick=function(){pre(0,1)};$('b5').onclick=function(){pre(-1,1.5)};$('b6').onclick=function(){pre(2.5,1)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
drag($('c3'),function(xy){setv('p',Math.round(cl(MF.ix(xy[0]),-3,3)*20)/20);setv('q',Math.round(cl(MF.iy(xy[1]),-1.5,2.4)*20)/20);An.fit();render()});
bindSliders(['p','q','g','y0','y1','sp'],function(){An.fit();render()});
An.full();
'''
bar7=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">Ciclo amortiguado</button>
    <button type="button" id="b2">Zigzag amortiguado</button>
    <button type="button" id="b3">Monótona</button>
    <button type="button" id="b4">Ciclo uniforme</button>
    <button type="button" id="b5">Ciclo explosivo</button>
    <button type="button" id="b6">Zigzag explosivo</button>
    <span class="sep"></span>''')
charts7=card('<svg id="c1" viewBox="0 0 680 270" role="img" aria-label="Trayectoria de la ecuación de segundo orden"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (p, q): el triángulo verde es la zona estable. Tocá o arrastrá el punto.</p><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Triángulo de estabilidad en el plano p y q"></svg>')+'\n'+card('<p class="cap">Raíces de r² + p·r + q: estables dentro del círculo unidad.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side7=card('<h2>Resultados</h2><div class="stats">'+stat('Δ = p² − 4q','vD')+stat('max |r|','vm')+stat('Raíces','vr',True)+stat('y*','vy')+stat('Período del ciclo','vTc')+stat('Trayectoria','vT',True,True)+'</div>')+'\n'+card('<h2>Las tres condiciones</h2><div class="stats">'+stat('1 − q &gt; 0','c1c')+stat('1 + p + q &gt; 0','c2c')+stat('1 − p + q &gt; 0','c3c')+'</div><p class="hint">Verde: se cumple. Rojo: no se cumple.</p>')+'\n'+card('<h2>Parámetros</h2>'+ctl('p','p',-3,3,0.05,-1,2)+ctl('q','q',-1.5,2.4,0.05,0.5,2)+ctl('g','g (término constante)',0,30,1,10,0)+ctl('y0','y₀',-10,50,1,30,0)+ctl('y1','y₁',-10,50,1,26,0)+ctl('sp','Velocidad',0.5,6,0.5,3,1))
page('07_triangulo_de_estabilidad.html','Triángulo de estabilidad','Ecuaciones de segundo orden: el triángulo de estabilidad','Matemática Aplicada II · Herramientas',
 ['y<sub>t+2</sub> + p·y<sub>t+1</sub> + q·y<sub>t</sub> = g','r² + p·r + q = 0','y* = g/(1+p+q)'],bar7,charts7,side7,js7)
