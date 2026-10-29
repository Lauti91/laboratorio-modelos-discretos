# =============== 8. Samuelson ===============
js8=MAPJS+r'''
var N=30,MF;
function prm(){return{ga:+$('ga').value,al:+$('al').value,G:+$('G').value,sh:+$('sh').value}}
function c2f(x){return 4*x/((1+x)*(1+x))}
function mf(x){return x<=1+1e-9?c2f(x):1/x}
function model(p){var pp=-p.ga*(1+p.al),qq=p.al*p.ga,Ys=p.G/(1-p.ga);
 return{pp:pp,qq:qq,Ys:Ys,y:sim2(pp,qq,p.G,Ys,Ys+p.sh,N),prod:p.al*p.ga,c2:c2f(p.al),cls:classify2(pp,qq)}}
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
 var f3=frame(340,300,40,10,12,28,0,5,0,1);MF=f3;var Z=function(){return 0};
 var r=clip('cC',f3)+axes(f3,{xt:[1,2,3,4,5],yt:[0,0.5,1],xl:'α',yl:'γ'});
 r+='<g clip-path="url(#cC)">';
 r+=band(f3,mf,Z,0,5,'fill:var(--okfill)',100);
 r+=band(f3,function(x){return x<=1+1e-9?1:c2f(x)},c2f,0,5,'fill:var(--okfill);opacity:.6',100);
 r+=band(f3,c2f,function(x){return x<=1+1e-9?c2f(x):1/x},0,5,'fill:var(--zone1)',100);
 r+=band(f3,function(x){return x<=1+1e-9?c2f(x):1},c2f,0,5,'fill:var(--zone2)',100);
 r+=curve(f3,c2f,0,5,'var(--demand)',2.2,null,120)+curve(f3,function(x){return 1/x},1,5,'var(--supply)',2.2,null,100)+'</g>';
 r+='<text x="'+f3.X(0.06)+'" y="'+f3.Y(0.95)+'" font-size="10.5" '+TX+'>monótona</text><text x="'+f3.X(1.45)+'" y="'+f3.Y(0.1)+'" font-size="10.5" '+TX+'>ciclo amortiguado</text><text x="'+f3.X(2.75)+'" y="'+f3.Y(0.52)+'" font-size="10.5" '+TX+'>ciclo explosivo</text><text x="'+f3.X(2.9)+'" y="'+f3.Y(0.92)+'" font-size="10.5" '+TX+'>monótona explosiva</text>';
 r+='<circle cx="'+f3.X(cl(p.al,0,5))+'" cy="'+f3.Y(cl(p.ga,0,1))+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 argand('c4',m.pp,m.qq);
 var tt=$('vT');tt.textContent=m.cls.txt;tt.style.color=m.cls.col;
 $('vag').textContent=F(m.prod,3);$('vY').textContent=F(m.Ys,2);$('vr').textContent=fmtRoots(m.cls.r);$('vm').textContent=F(m.cls.r.maxabs,3);
 $('vTc').textContent=m.cls.T?F(m.cls.T,1)+' períodos':'—';$('vD').textContent=F(m.pp*m.pp-4*m.qq,3);$('vc2').textContent=F(m.c2,3);
 $('vt').textContent=k+' · '+F(m.y[k],2)}
function pre(al,ga){setv('al',al);setv('ga',ga);setv('G',20);setv('sh',10);An.full()}
$('b1').onclick=function(){pre(0.2,0.8)};$('b2').onclick=function(){pre(1.5,0.6)};$('b3').onclick=function(){pre(2,0.5)};$('b4').onclick=function(){pre(3,0.5)};$('b5').onclick=function(){pre(4,0.9)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
drag($('c3'),function(xy){setv('al',Math.round(cl(MF.ix(xy[0]),0.05,5)*20)/20);setv('ga',Math.round(cl(MF.iy(xy[1]),0.05,0.99)*100)/100);An.fit();render()});
bindSliders(['ga','al','G','sh','sp'],function(){An.fit();render()});
An.full();
'''
bar8=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">Monótona convergente</button>
    <button type="button" id="b2">Ciclo amortiguado</button>
    <button type="button" id="b3">αγ = 1, amplitud constante</button>
    <button type="button" id="b4">Ciclo explosivo</button>
    <button type="button" id="b5">Monótona explosiva</button>
    <span class="sep"></span>''')
charts8=card('<p class="cap">Ingreso después de un shock: la economía estaba en Y* y en t = 1 el ingreso sube.</p><svg id="c1" viewBox="0 0 680 270" role="img" aria-label="Ingreso en el tiempo"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (α, γ): tocá o arrastrá para cambiar α y γ.</p><div class="leg"><span><i class="sq" style="background:var(--okfill)"></i>estable</span><span><i class="sq" style="background:var(--zone1)"></i>ciclo explosivo</span><span><i class="sq" style="background:var(--zone2)"></i>monótona explosiva</span></div><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Regiones dinámicas en el plano alfa y gamma"></svg>')+'\n'+card('<p class="cap">Raíces en el plano complejo: estables dentro del círculo unidad.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side8=card('<h2>Resultados</h2><div class="stats">'+stat('αγ','vag')+stat('Y* = G₀/(1−γ)','vY')+stat('Δ','vD')+stat('4α/(1+α)²','vc2')+stat('max |R|','vm')+stat('Período del ciclo','vTc')+stat('Raíces','vr',True)+stat('Régimen','vT',True,True)+stat('Período · Y<sub>t</sub>','vt',True)+'</div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('ga','γ (propensión al consumo)',0.05,0.99,0.01,0.6,2)+ctl('al','α (acelerador)',0.05,5,0.05,1.5,2)+ctl('G','G₀ (gasto público)',5,50,1,20,0)+ctl('sh','Shock Y₁ − Y*',2,30,1,10,0)+ctl('sp','Velocidad',0.5,6,0.5,3,1))
page('08_samuelson.html','Modelo de Samuelson','Multiplicador y acelerador: el modelo de Samuelson','Matemática Aplicada II · Modelos III',
 ['Y<sub>t+2</sub> − γ(1+α)·Y<sub>t+1</sub> + αγ·Y<sub>t</sub> = G₀','Y* = G₀/(1−γ)','estable ⇔ αγ &lt; 1','ciclos ⇔ γ &lt; 4α/(1+α)²'],bar8,charts8,side8,js8)

# =============== 9. Hicks ===============
js9=MAPJS+r'''
var N=30,MF;
function prm(){return{ga:+$('ga').value,al:+$('al').value,g:+$('g').value,I:+$('I').value,sh:+$('sh').value,ce:+$('ce').value/100,fl:+$('fl').value/100,ck:$('ck').checked}}
function hf(x){return 2*Math.sqrt(x)-x}
function model(p){var G=1+p.g,D=G*G-(p.ga+p.al)*G+p.al,warn=false;if(Math.abs(D)<1e-4){D=D<0?-1e-4:1e-4;warn=true}
 var A=p.I*G*G/D,pp=-(p.ga+p.al),qq=p.al,tr=[],lo=[],hi=[],y=[A,A*G*(1+p.sh/100)],clipOn=p.ck&&A>0;
 for(var t=0;t<=N;t++){var T=A*Math.pow(G,t);tr.push(T);lo.push(T*(1-p.fl));hi.push(T*(1+p.ce))}
 if(clipOn){y[0]=A;y[1]=cl(y[1],lo[1],hi[1])}
 for(var t=2;t<=N;t++){var v=-pp*y[t-1]-qq*y[t-2]+p.I*Math.pow(G,t);y.push(clipOn?cl(v,lo[t],hi[t]):v)}
 return{G:G,D:D,A:A,pp:pp,qq:qq,y:y,tr:tr,lo:lo,hi:hi,clipOn:clipOn,cls:classify2(pp,qq),warn:warn}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 var vis=[];for(var j=0;j<=k;j++)vis.push([j,m.y[j]]);var tv=m.y[k];if(k<N&&fr>1e-6){tv=m.y[k]+(m.y[k+1]-m.y[k])*cl(fr*2-1,0,1);vis.push([k+fr,tv])}
 var trv=m.tr.slice(0,k+2),all=vis.map(function(z){return z[1]}).concat(trv);if(m.clipOn)all=all.concat(m.lo.slice(0,k+2),m.hi.slice(0,k+2));
 var yr=yrange(all,0.1);
 var f=frame(680,280,56,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:sb('Y','t'),yf:function(v){return F(v,0)}});
 var tp=m.tr.map(function(v,i){return[i,v]});
 o+='<g clip-path="url(#cA)">';
 if(m.clipOn){o+=poly(f,m.hi.map(function(v,i){return[i,v]}),'var(--faint)',1.4,0,'3 4')+poly(f,m.lo.map(function(v,i){return[i,v]}),'var(--faint)',1.4,0,'3 4')}
 o+=poly(f,tp,'var(--supply)',1.8,0,'6 4')+poly(f,vis,'var(--demand)',2.4,3)+'</g>';
 if(k<N&&fr>1e-6)o+=tip(f,k+fr,tv,'var(--demand)');
 $('c1').innerHTML=o;
 var f3=frame(340,300,40,10,12,28,0,3,0,1);MF=f3;var Z=function(){return 0},ep=1+1e-9;
 var r=clip('cC',f3)+axes(f3,{xt:[1,2,3],yt:[0,0.5,1],xl:'α',yl:'γ'});
 r+='<g clip-path="url(#cC)">';
 r+=band(f3,function(x){return x<=ep?hf(x):0},Z,0,3,'fill:var(--okfill)',120);
 r+=band(f3,function(x){return x<=ep?1:0},function(x){return x<=ep?hf(x):0},0,3,'fill:var(--okfill);opacity:.6',120);
 r+=band(f3,function(x){return x>ep?hf(x):0},Z,0,3,'fill:var(--zone1)',120);
 r+=band(f3,function(x){return x>ep?1:0},function(x){return x>ep?hf(x):0},0,3,'fill:var(--zone2)',120);
 r+=curve(f3,hf,0,3,'var(--demand)',2.2,null,120)+'<line x1="'+f3.X(1)+'" x2="'+f3.X(1)+'" y1="'+f3.T+'" y2="'+(f3.T+f3.h)+'" style="stroke:var(--supply)" stroke-width="2.2"/></g>';
 r+='<text x="'+f3.X(0.05)+'" y="'+f3.Y(0.95)+'" font-size="10.5" '+TX+'>monótona</text><text x="'+f3.X(0.12)+'" y="'+f3.Y(0.1)+'" font-size="10.5" '+TX+'>ciclo amortiguado</text><text x="'+f3.X(1.55)+'" y="'+f3.Y(0.15)+'" font-size="10.5" '+TX+'>ciclo explosivo</text><text x="'+f3.X(1.5)+'" y="'+f3.Y(0.9)+'" font-size="10.5" '+TX+'>monótona explosiva</text>';
 r+='<circle cx="'+f3.X(cl(p.al,0,3))+'" cy="'+f3.Y(cl(p.ga,0,1))+'" r="6" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 argand('c4',m.pp,m.qq);
 var tt=$('vT');tt.textContent=m.cls.txt;tt.style.color=m.cls.col;
 $('vA').textContent=F(m.A,2);$('vD').textContent=F(m.D,3);$('vr').textContent=fmtRoots(m.cls.r);$('vm').textContent=F(m.cls.r.maxabs,3);
 $('vTc').textContent=m.cls.T?F(m.cls.T,1)+' períodos':'—';$('vD2').textContent=F(m.pp*m.pp-4*m.qq,3);$('vh').textContent=F(hf(p.al),3);
 $('vt').textContent=k+' · '+F(m.y[k],2);$('vcond').textContent=F(p.al,2)+(p.al<1?' < 1':' ≥ 1');
 $('msg').textContent=(p.ck&&m.A<=0)?'Sin tendencia de equilibrio positiva: el techo y el piso no se aplican.':(m.warn?'1+g es casi una raíz: la solución particular no está bien definida.':'')}
function pre(al,ga,ck){setv('al',al);setv('ga',ga);setv('g',0.03);setv('I',10);setv('sh',10);$('ck').checked=!!ck;An.full()}
$('b1').onclick=function(){pre(0.5,0.6,0)};$('b2').onclick=function(){pre(0.2,0.8,0)};$('b3').onclick=function(){pre(1,0.5,0)};$('b4').onclick=function(){pre(1.5,0.6,0)};$('b5').onclick=function(){pre(1.5,0.6,1)};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
$('ck').addEventListener('change',function(){An.fit();render()});
drag($('c3'),function(xy){setv('al',Math.round(cl(MF.ix(xy[0]),0.05,3)*20)/20);setv('ga',Math.round(cl(MF.iy(xy[1]),0.05,0.95)*100)/100);An.fit();render()});
bindSliders(['ga','al','g','I','sh','ce','fl','sp'],function(){An.fit();render()});
An.full();
'''
bar9=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">Ciclo amortiguado</button>
    <button type="button" id="b2">Monótona convergente</button>
    <button type="button" id="b3">α = 1, amplitud constante</button>
    <button type="button" id="b4">α = 1,5 explosivo</button>
    <button type="button" id="b5">α = 1,5 con techo y piso</button>
    <span class="sep"></span>''')
charts9=card('<div class="leg"><span><i style="background:var(--demand)"></i>Ingreso Y<sub>t</sub></span><span><i style="background:var(--supply)"></i>Tendencia Y<sup>p</sup><sub>t</sub> = A(1+g)<sup>t</sup></span></div><svg id="c1" viewBox="0 0 680 280" role="img" aria-label="Ingreso y tendencia de crecimiento en el tiempo"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (α, γ): sólo α &lt; 1 es estable. Tocá o arrastrá el punto.</p><div class="leg"><span><i class="sq" style="background:var(--okfill)"></i>estable</span><span><i class="sq" style="background:var(--zone1)"></i>ciclo explosivo</span><span><i class="sq" style="background:var(--zone2)"></i>monótona explosiva</span></div><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Regiones dinámicas en el plano alfa y gamma"></svg>')+'\n'+card('<p class="cap">Raíces en el plano complejo: estables dentro del círculo unidad.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side9=card('<h2>Resultados</h2><div class="stats">'+stat('A (solución particular)','vA')+stat('(1+g)² − (γ+α)(1+g) + α','vD')+stat('α (estable si &lt; 1)','vcond')+stat('Δ','vD2')+stat('2√α − α','vh')+stat('max |R|','vm')+stat('Raíces','vr',True)+stat('Período del ciclo','vTc',True)+stat('Régimen','vT',True,True)+stat('Período · Y<sub>t</sub>','vt',True)+'</div><div id="msg" role="status"></div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('ga','γ (propensión al consumo)',0.05,0.95,0.01,0.6,2)+ctl('al','α (acelerador)',0.05,3,0.05,0.5,2)+ctl('g','g (crecimiento de I″)',0,0.08,0.005,0.03,3)+ctl('I','I₀ (inversión autónoma)',5,50,1,10,0)+ctl('sh','Desvío inicial de Y₁ (% de la tendencia)',-20,30,1,10,0)+'<div class="ctl"><label for="ck"><span>Techo y piso (ilustración)</span></label><input type="checkbox" id="ck" style="width:18px;height:18px;accent-color:var(--supply)"></div>'+ctl('ce','Techo: % sobre la tendencia',5,40,1,15,0)+ctl('fl','Piso: % bajo la tendencia',5,40,1,15,0)+ctl('sp','Velocidad',0.5,6,0.5,3,1)+'<p class="hint">Con el techo y el piso, Y<sub>t</sub> se recorta a esa franja en cada período. Es una simplificación para ver cómo el caso α ≥ 1 deja de explotar.</p>')
page('09_hicks.html','Modelo de Hicks','Ciclo y crecimiento: el modelo de Hicks','Matemática Aplicada II · Modelos III',
 ['Y<sub>t+2</sub> − (γ+α)·Y<sub>t+1</sub> + α·Y<sub>t</sub> = I₀(1+g)<sup>t+2</sup>','A = I₀(1+g)² / [(1+g)² − (γ+α)(1+g) + α]','estable ⇔ α &lt; 1'],bar9,charts9,side9,js9)

# =============== 10. Inflación y desempleo ===============
js10=MAPJS+r'''
var N=40,MF;
function prm(){return{a:+$('a').value,be:+$('be').value,g:+$('g').value,j:+$('j').value,k:+$('k').value,mo:+$('mo').value,mn:+$('mn').value}}
function model(p){var pi=p.mo,U=(p.a-(1-p.g)*p.mo)/p.be,P=[],PI=[],UU=[];
 for(var t=0;t<=N;t++){PI.push(pi);UU.push(U);var pt=p.a-p.be*U+p.g*pi;P.push(pt);
  var pin=pi+p.j*(pt-pi);U=(U-p.k*p.mn+p.k*(p.a+p.g*pin))/(1+p.be*p.k);pi=pin}
 var d=1+p.be*p.k,a1=(1+p.g*p.j+(1-p.j)*d)/d,a2=(1-p.j*(1-p.g))/d,Ub=(p.a-(1-p.g)*p.mn)/p.be,U0=(p.a-(1-p.g)*p.mo)/p.be;
 return{P:P,PI:PI,U:UU,a1:a1,a2:a2,Ub:Ub,U0:U0,cls:classify2(-a1,a2),pp:-a1}}
var An=makeAnim(render,function(){return N},function(){return +$('sp').value},$('pl'));
function render(){
 var p=prm(),m=model(p),u=An.u,k=Math.min(Math.floor(u+1e-9),N),fr=u-k;
 function seg(arr){var r=[];for(var j=0;j<=k;j++)r.push([j,arr[j]]);var v=arr[k];if(k<N&&fr>1e-6){v=arr[k]+(arr[k+1]-arr[k])*cl(fr*2-1,0,1);r.push([k+fr,v])}return r}
 var sp=seg(m.P),spi=seg(m.PI),su=seg(m.U);
 var all=[].concat(sp,spi,su).map(function(z){return z[1]}).concat([p.mn,m.Ub,p.mo,m.U0]);
 var yr=yrange(all,0.1);
 var f=frame(680,280,50,16,12,28,0,N,yr[0],yr[1]);
 var o=clip('cA',f)+axes(f,{xt:ticks(0,N,8),yt:ticks(yr[0],yr[1],4),xl:'t',yl:'%',yf:function(v){return F(v,1)}});
 o+='<g clip-path="url(#cA)">'+hl(f,p.mn,'m = '+F(p.mn,1)+'%')+hl(f,m.Ub,'',null,'2 4')+poly(f,su,'var(--supply)',2.2,2.5)+poly(f,spi,'var(--c3)',2,0,'6 4')+poly(f,sp,'var(--demand)',2.4,2.5)+'</g>';
 $('c1').innerHTML=o;
 var xs=m.U.concat([m.Ub,m.U0]),ys=m.P.concat([p.mn,p.mo]);
 var xr=yrange(xs,0.15),yr2=yrange(ys,0.15);
 var f3=frame(340,300,44,10,12,30,xr[0],xr[1],yr2[0],yr2[1]);MF=f3;
 var r=clip('cC',f3)+axes(f3,{xt:ticks(xr[0],xr[1],4),yt:ticks(yr2[0],yr2[1],4),xl:'U (%)',yl:'p (%)',yf:function(v){return F(v,1)},xf:function(v){return F(v,1)}});
 var lr=[],q;for(var i=0;i<=40;i++){q=yr2[0]+(yr2[1]-yr2[0])*i/40;lr.push([(p.a-(1-p.g)*q)/p.be,q])}
 var sr=[];for(var i=0;i<=40;i++){var uu=xr[0]+(xr[1]-xr[0])*i/40;sr.push([uu,p.a-p.be*uu+p.g*p.mo])}
 r+='<g clip-path="url(#cC)">'+poly(f3,lr,'var(--supply)',2.2)+poly(f3,sr,'var(--faint)',1.4,0,'5 4');
 var tr=[];for(var j=0;j<=k;j++)tr.push([m.U[j],m.P[j]]);r+=poly(f3,tr,'var(--demand)',2,2.5)+'</g>';
 r+='<circle cx="'+f3.X(m.U0)+'" cy="'+f3.Y(p.mo)+'" r="5.5" stroke-width="2" style="fill:var(--surface);stroke:var(--fg)"/><circle cx="'+f3.X(m.Ub)+'" cy="'+f3.Y(p.mn)+'" r="5.5" stroke-width="2" style="fill:var(--fg);stroke:var(--surface)"/>';
 $('c3').innerHTML=r;
 argand('c4',m.pp,m.a2);
 var c=m.cls,tt=$('vT');tt.textContent=c.txt;tt.style.color=c.col;
 $('va1').textContent=F(m.a1,3);$('va2').textContent=F(m.a2,3);$('vr').textContent=fmtRoots(c.r);$('vm').textContent=F(c.r.maxabs,3);
 $('vTc').textContent=c.T?F(c.T,1)+' períodos':'—';$('vp').textContent=F(p.mn,2)+' %';$('vU').textContent=F(m.Ub,2)+' %';
 $('vs').textContent=F(-(1-p.g)/p.be,3);$('vt').textContent=k+' · p = '+F(m.P[k],2)+' ; U = '+F(m.U[k],2);
 var neg=m.U.slice(0,k+1).some(function(v){return v<0});$('msg').textContent=neg?'El desempleo resulta negativo: bajá m o subí el intercepto α − T.':''}
function pre(o){var d={a:8,be:1,g:0.8,j:0.5,k:0.4,mo:4,mn:8};for(var x in o)d[x]=o[x];for(var x in d)setv(x,d[x]);An.full()}
$('b1').onclick=function(){pre({})};$('b2').onclick=function(){pre({g:1})};$('b3').onclick=function(){pre({g:0.4})};
$('b4').onclick=function(){pre({j:0.1})};$('b5').onclick=function(){pre({k:1.5,j:1})};$('b6').onclick=function(){pre({mo:8,mn:3})};
$('step').onclick=An.step;$('pl').onclick=An.toggle;$('rs').onclick=An.reset;
bindSliders(['a','be','g','j','k','mo','mn','sp'],function(){An.fit();render()});
An.full();
'''
bar10=anim_bar('''<span class="lbl">Casos</span>
    <button type="button" id="b1">Base (g = 0,8)</button>
    <button type="button" id="b2">g = 1, vertical</button>
    <button type="button" id="b3">g = 0,4</button>
    <button type="button" id="b4">Expectativas lentas</button>
    <button type="button" id="b5">Con ciclos</button>
    <button type="button" id="b6">Desinflación</button>
    <span class="sep"></span>''')
charts10=card('<div class="leg"><span><i style="background:var(--demand)"></i>Inflación p<sub>t</sub></span><span><i style="background:var(--c3)"></i>Inflación esperada π<sub>t</sub></span><span><i style="background:var(--supply)"></i>Desempleo U<sub>t</sub></span></div><p class="cap">La economía parte de su equilibrio con la expansión monetaria m previa. En t = 0 la autoridad pasa a la m nueva.</p><svg id="c1" viewBox="0 0 680 280" role="img" aria-label="Inflación, inflación esperada y desempleo en el tiempo"></svg>')+'\n      <div class="row2">\n'+card('<p class="cap">Plano (U, p): trayectoria entre los dos equilibrios.</p><div class="leg"><span><i style="background:var(--supply)"></i>Phillips de largo plazo</span><span><i style="background:var(--faint)"></i>Phillips de corto plazo (π = m previa)</span></div><div class="leg"><span>○ equilibrio previo</span><span>● equilibrio nuevo</span></div><svg id="c3" viewBox="0 0 340 300" role="img" aria-label="Plano desempleo e inflación con la curva de Phillips de largo plazo"></svg>')+'\n'+card('<p class="cap">Raíces en el plano complejo: la convergencia está garantizada por las hipótesis.</p><svg id="c4" viewBox="0 0 300 300" role="img" aria-label="Raíces características y círculo unidad"></svg>')+'\n      </div>'
side10=card('<h2>Resultados</h2><div class="stats">'+stat('a₁','va1')+stat('a₂','va2')+stat('p̄ = m','vp')+stat('Ū','vU')+stat('dŪ/dp̄','vs')+stat('max |R|','vm')+stat('Raíces','vr',True)+stat('Período del ciclo','vTc',True)+stat('Trayectoria','vT',True,True)+stat('Período · valores','vt',True)+'</div><div id="msg" role="status"></div>')+'\n'+card('<h2>Parámetros</h2>'+ctl('a','α − T (intercepto, %)',4,12,0.5,8,1)+ctl('be','β (efecto del desempleo)',0.5,3,0.1,1,1)+ctl('g','g (traslado de expectativas)',0.05,1,0.05,0.8,2)+ctl('j','j (aprendizaje)',0.05,1,0.05,0.5,2)+ctl('k','k (sensibilidad al dinero real)',0.05,2,0.05,0.4,2)+ctl('mo','m previa (%)',0,12,0.5,4,1)+ctl('mn','m nueva (%)',0,12,0.5,8,1)+ctl('sp','Velocidad',0.5,8,0.5,4,1))
page('10_inflacion_desempleo.html','Inflación y desempleo','Inflación y desempleo en tiempo discreto','Matemática Aplicada II · Modelos III',
 ['p<sub>t</sub> = α − T − βU<sub>t</sub> + gπ<sub>t</sub>','π<sub>t+1</sub> − π<sub>t</sub> = j(p<sub>t</sub> − π<sub>t</sub>)','U<sub>t+1</sub> − U<sub>t</sub> = −k(m − p<sub>t+1</sub>)','p̄ = m'],bar10,charts10,side10,js10)
