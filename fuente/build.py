import os,re,html as _html
H=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(H,'site');os.makedirs(OUT,exist_ok=True)
CSS=open(os.path.join(H,'common.css'),encoding='utf-8').read()
LIB=open(os.path.join(H,'lib.js'),encoding='utf-8').read()
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@500;600;700&family=Share+Tech+Mono&family=STIX+Two+Text:ital@0;1&display=swap">')
MATHJAX=('<script>window.MathJax={tex:{inlineMath:[["\\\\(","\\\\)"]]},svg:{fontCache:"global"},options:{enableMenu:false}};</script>'
 '<script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-svg.min.js"></script>')
SITE='Laboratorio de modelos discretos'
ICON=('<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="1" y="1" width="30" height="30" rx="5" fill="#111c2d" stroke="#26364f"/>'
 '<rect x="5" y="6" width="22" height="16" rx="2" fill="#060b14"/><path d="M6 15 L9 9 L12 19 L15 11 L18 16 L21 13 L26 14" fill="none" stroke="#ff8a1f" stroke-width="1.6" stroke-linejoin="round"/>'
 '<circle cx="9" cy="26.5" r="1.6" fill="#5aa9ff"/><rect x="14" y="25.3" width="13" height="2.4" rx="1" fill="#26364f"/></svg>')
FAVICON='data:image/svg+xml,'+ICON.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ').replace('"',"'").replace('#','%23').replace('<','%3C').replace('>','%3E')
GROUPS={'I':('Modelos I','Primer orden'),'II':('Modelos II','Segundo orden'),'III':('Modelos III','Macroeconomía dinámica')}
# fn -> (slug, grupo, nombre corto)
REG=[('00_telarana.html','telarana-estandar','I','Telaraña estándar'),
 ('01_ecuacion_canonica.html','ecuacion-canonica','I','Ecuación canónica'),
 ('02_interes_y_rentas.html','interes-y-rentas','I','Interés y rentas'),
 ('03_expectativas_adaptativas.html','expectativas-adaptativas','I','Expectativas adaptativas'),
 ('04_mercado_con_inventarios.html','mercado-con-inventarios','I','Mercado con inventarios'),
 ('07_triangulo_de_estabilidad.html','triangulo-de-estabilidad','II','Triángulo de estabilidad'),
 ('05_telarana_extrapolacion.html','telarana-extrapolacion','II','Telaraña con extrapolación'),
 ('06_inventarios_de_metzler.html','metzler','II','Inventarios de Metzler'),
 ('08_samuelson.html','samuelson','III','Samuelson'),
 ('09_hicks.html','hicks','III','Hicks'),
 ('10_inflacion_desempleo.html','inflacion-desempleo','III','Inflación y desempleo')]
# orden de lectura del sitio
ORDER=['ecuacion-canonica','interes-y-rentas','telarana-estandar','expectativas-adaptativas','mercado-con-inventarios',
 'triangulo-de-estabilidad','telarana-extrapolacion','metzler','samuelson','hicks','inflacion-desempleo']
BYFN={r[0]:r for r in REG};BYSLUG={r[1]:r for r in REG}
T=lambda s:'\\('+s+'\\)'
TEX={
 '00_telarana.html':[r'Q^d_t=\alpha-\beta P_t',r'Q^s_t=-\gamma+\delta P_{t-1}',r'P_{t+1}=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}P_t'],
 '01_ecuacion_canonica.html':[r'y_{t+1}=A\,y_t+B',r'y^*=\frac{B}{1-A}',r'y_t=(y_0-y^*)A^t+y^*'],
 '03_expectativas_adaptativas.html':[r'P^e_t=P^e_{t-1}+\eta\,(P_{t-1}-P^e_{t-1})',r'P_{t+1}=A\,P_t+\eta\,\frac{\alpha+\gamma}{\beta}',r'A=1-\eta\left(1+\frac{\delta}{\beta}\right)'],
 '04_mercado_con_inventarios.html':[r'P_{t+1}=P_t-\sigma\,(Q^s_t-Q^d_t)',r'A=1-\sigma(\beta+\delta)',r'\text{estable}\iff\sigma\lt\frac{2}{\beta+\delta}'],
 '05_telarana_extrapolacion.html':[r'P^e_t=P_{t-1}+\phi\,(P_{t-1}-P_{t-2})',r'P_{t+2}+\mu(1+\phi)P_{t+1}-\mu\phi P_t=\frac{\alpha+\gamma}{\beta}',r'\mu=\delta/\beta'],
 '06_inventarios_de_metzler.html':[r'Y_{t+2}-c(2+k)Y_{t+1}+c(1+k)Y_t=V_0',r'Y^*=\frac{V_0}{1-c}',r'\text{estable}\iff c(1+k)\lt 1'],
 '07_triangulo_de_estabilidad.html':[r'y_{t+2}+p\,y_{t+1}+q\,y_t=g',r'r^2+p\,r+q=0',r'y^*=\frac{g}{1+p+q}'],
 '08_samuelson.html':[r'Y_{t+2}-\gamma(1+\alpha)Y_{t+1}+\alpha\gamma\,Y_t=G_0',r'Y^*=\frac{G_0}{1-\gamma}',r'\text{estable}\iff\alpha\gamma\lt 1',r'\text{ciclos}\iff\gamma\lt\frac{4\alpha}{(1+\alpha)^2}'],
 '09_hicks.html':[r'Y_{t+2}-(\gamma+\alpha)Y_{t+1}+\alpha Y_t=I_0(1+g)^{t+2}',r'Y^p_t=A(1+g)^t',r'\text{estable}\iff\alpha\lt 1'],
 '10_inflacion_desempleo.html':[r'p_t=\alpha-T-\beta U_t+g\,\pi_t',r'\pi_{t+1}-\pi_t=j\,(p_t-\pi_t)',r'U_{t+1}-U_t=-k\,(m-p_{t+1})',r'\bar p=m'],
}
SUB={
 '00_telarana.html':'El productor decide con el precio de ayer. La oferta llega un período tarde y el precio rebota alrededor del equilibrio.',
 '01_ecuacion_canonica.html':'La ecuación de primer orden que está detrás de todos los modelos de la primera parte: el signo y el módulo de A deciden la trayectoria.',
 '02_interes_y_rentas.html':'Capitalización, valor final de una renta y saldo de un préstamo como ecuaciones de primer orden.',
 '03_expectativas_adaptativas.html':'Los productores corrigen su expectativa una fracción η del error. Si η es chico, un mercado que con la telaraña explota puede converger.',
 '04_mercado_con_inventarios.html':'El precio baja cuando se acumula stock y sube cuando falta. La velocidad de ajuste σ decide si converge, oscila o explota.',
 '05_telarana_extrapolacion.html':'Los productores proyectan la última variación del precio. La expectativa depende de dos rezagos y la ecuación pasa a ser de segundo orden.',
 '06_inventarios_de_metzler.html':'Las empresas reponen stock y además buscan una proporción k entre inventario y ventas. El acelerador puede desestabilizar el ingreso.',
 '07_triangulo_de_estabilidad.html':'Toda ecuación de segundo orden queda resumida en el punto (p, q). Adentro del triángulo, la trayectoria converge.',
 '08_samuelson.html':'Multiplicador y acelerador juntos generan ciclos sin necesidad de shocks externos.',
 '09_hicks.html':'Dinámica de Samuelson alrededor de una tendencia de crecimiento, con techo y piso que acotan el ciclo.',
 '10_inflacion_desempleo.html':'Curva de Phillips con expectativas adaptativas y política monetaria. La inflación converge a m y g decide si el trade-off es permanente.',
}
GREEK={'α':r'\alpha','β':r'\beta','γ':r'\gamma','δ':r'\delta','η':r'\eta','σ':r'\sigma','φ':r'\phi','μ':r'\mu','π':r'\pi','Δ':r'\Delta'}
LBL={
 'Cuota c':'Cuota '+T('c'),'Períodos n':'Períodos '+T('n'),'Tasa por período i (%)':'Tasa por período '+T('i')+' (%)','Capital inicial C':'Capital inicial '+T('C'),
 'Desvío inicial de Y₁ (% de la tendencia)':'Desvío inicial de '+T('Y_1')+' (% de la tendencia)',
 'P₀ − P* (con P₋₁ = P₀)':T('P_0-P^*')+' (con '+T('P_{-1}=P_0')+')','P₀ − P*':T('P_0-P^*'),
 'Shock Y₀ − Y*':'Shock '+T('Y_0-Y^*'),'Shock Y₁ − Y*':'Shock '+T('Y_1-Y^*'),
 'α − T (intercepto, %)':T(r'\alpha-T')+' (intercepto, %)','g (crecimiento de I″)':T('g')+' (crecimiento de '+T("I''")+')',
 'm nueva (%)':T('m')+' nueva (%)','m previa (%)':T('m')+' previa (%)','p':T('p'),'q':T('q'),
 'y₀ (valor inicial)':T('y_0')+' (valor inicial)','y₀':T('y_0'),'y₁':T('y_1'),
 'Piso: % bajo la tendencia':'Piso: % bajo la tendencia','Techo: % sobre la tendencia':'Techo: % sobre la tendencia',
 '(1+g)² − (γ+α)(1+g) + α':'Denominador de '+T('A'),
 '1 + p + q &gt; 0':T(r'1+p+q\gt 0'),'1 − p + q &gt; 0':T(r'1-p+q\gt 0'),'1 − q &gt; 0':T(r'1-q\gt 0'),
 '2√α − α':T(r'2\sqrt{\alpha}-\alpha'),'4α/(1+α)²':T(r'4\alpha/(1+\alpha)^2'),
 'A (solución particular)':T('A')+' (solución particular)','A = 1 − η(1+δ/β)':T(r'A=1-\eta(1+\delta/\beta)'),
 'A = 1 − σ(β+δ)':T(r'A=1-\sigma(\beta+\delta)'),'A telaraña = −δ/β':T('A')+' telaraña '+T(r'=-\delta/\beta'),'A':T('A'),
 'Cortes: (1−c)/c ; k̄':'Cortes: '+T('(1-c)/c')+' y '+T(r'\bar k'),'P*':T('P^*'),
 'Período · P<sub>t</sub>':'Período · '+T('P_t'),'Período · Y<sub>t</sub>':'Período · '+T('Y_t'),'Período · y<sub>t</sub>':'Período · '+T('y_t'),
 'Rango estable de φ':'Rango estable de '+T(r'\phi'),'Y* = G₀/(1−γ)':T(r'Y^*=G_0/(1-\gamma)'),'Y* = V₀/(1−c)':T(r'Y^*=V_0/(1-c)'),
 'G₀ (gasto público)':T('G_0')+' (gasto público)','V₀ (inversión autónoma)':T('V_0')+' (inversión autónoma)','I₀ (inversión autónoma)':T('I_0')+' (inversión autónoma)',
 'a₁':T('a_1'),'a₂':T('a_2'),'c(1+k)':T('c(1+k)'),'dŪ/dp̄':T(r'd\bar U/d\bar p'),'max |R|':T(r'\max|R|'),'max |r|':T(r'\max|r|'),
 'p = μ(1+φ)':T(r'p=\mu(1+\phi)'),'p̄ = m':T(r'\bar p=m'),'q = −μφ':T(r'q=-\mu\phi'),'y* = B/(1−A)':T('y^*=B/(1-A)'),'y*':T('y^*'),
 'Ū':T(r'\bar U'),'Δ = p² − 4q':T(r'\Delta=p^2-4q'),'Δ':T(r'\Delta'),'α (estable si &lt; 1)':T(r'\alpha')+' (estable si '+T(r'\lt 1')+')',
 'αγ':T(r'\alpha\gamma'),'δ/β vs (2−η)/η':T(r'\delta/\beta')+' vs '+T(r'(2-\eta)/\eta'),'σ(β+δ)':T(r'\sigma(\beta+\delta)'),
}
def lab(s):
    if s in LBL: return LBL[s]
    m=re.match(r'^([α-ωA-Za-z])(\s\(.*\))$',s)
    if m: return T(GREEK.get(m.group(1),m.group(1)))+m.group(2)
    return s
def ctl(i,label,mn,mx,st,val,d=2):
    return f'<div class="ctl"><label for="{i}"><span class="lt">{lab(label)}</span><output id="o_{i}"></output></label><input type="range" id="{i}" min="{mn}" max="{mx}" step="{st}" value="{val}" data-d="{d}"></div>'
def stat(l,i,w=False,t=False):
    return f'<div class="stat{" w" if w else ""}"><div class="l">{lab(l)}</div><div class="v{" t" if t else ""}" id="{i}"></div></div>'
def anim_bar(extra=''):
    return f'''  <div class="bar">
    <span class="pre">{extra}</span>
    <span class="ctrls"><button type="button" class="go" id="step">Siguiente paso</button><button type="button" class="go" id="pl">Reproducir</button><button type="button" id="rs">Reiniciar</button></span>
  </div>'''
def card(inner,cls=''):
    return f'      <div class="card {cls}">{inner}</div>'
def head(title,desc):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{_html.escape(desc)}">
<link rel="icon" href="{FAVICON}">
{FONTS}
<style>
{CSS}
'''
def mno(slug): return 'MD-%02d'%(ORDER.index(slug)+1)
def topbar(slug=None):
    right=(f'<span class="meta"><a href="index.html">◀ Índice</a>&nbsp; {mno(slug)} / {len(ORDER):02d}</span>' if slug else '<span class="meta">Matemática Aplicada II · FCE-UBA</span>')
    return f'<div class="topbar"><a class="brand" href="index.html">{ICON}<span><b>Lab</b> · Modelos discretos</span></a>{right}</div>'
def foot():
    return '<footer class="foot"><span>Matemática Aplicada II · FCE-UBA</span><span>Chiang y Wainwright, cap. 17–18 · Bernardello et al., cap. 3</span></footer>'
def pager(slug):
    i=ORDER.index(slug);o='<nav class="pager" aria-label="Otros módulos">'
    if i>0:
        r=BYSLUG[ORDER[i-1]];o+=f'<a class="pv" href="{r[1]}.html"><span class="d">◀ {mno(r[1])}</span><span class="n">{r[3]}</span></a>'
    if i<len(ORDER)-1:
        r=BYSLUG[ORDER[i+1]];o+=f'<a class="nx" href="{r[1]}.html"><span class="n">{r[3]}</span><span class="d">{mno(r[1])} ▶</span></a>'
    else:
        o+='<a class="nx" href="index.html"><span class="n">Volver al índice</span><span class="d">▶</span></a>'
    return o+'</nav>'
exec(open(os.path.join(H,'derivs.py'),encoding='utf-8').read())
def deriv_html(fn):
    if fn not in DERIV: return ''
    intro,steps=DERIV[fn];n=len(steps);li='';ph=None;pk=0
    for i,(fase,t,q,body) in enumerate(steps):
        if fase!=ph:
            ph=fase;pk+=1;li+=f'<li class="dphase" aria-hidden="true"><span>Etapa {pk}</span>{fase}</li>'
        qh=f'<p class="dq"><span>Antes de abrirlo:</span> {q}</p>' if q else '<p class="dq"><span>Siguiente:</span> seguí con la derivación.</p>'
        li+=(f'<li class="dstep{" open" if i==0 else (" next" if i==1 else " locked")}" id="paso-{i+1}">'
             f'<div class="dn" aria-hidden="true">{i+1}</div><div class="dw"><h3>{t}</h3>{qh}'
             f'<button type="button" class="dunl">Desbloquear paso {i+1}</button><div class="dbody">{body}</div></div></li>')
    return (f'<section class="deriv" id="derivacion" aria-labelledby="dtit"><header class="dhead"><div><h2 class="dtitle" id="dtit">Derivación paso a paso</h2>'
            f'<p class="dsub">{intro}</p></div><div class="dctl"><span class="dprog" role="status">Paso <b id="dk">1</b> de {n}</span>'
            f'<div class="dbar"><i id="dfill" style="width:{100/n:.1f}%"></i></div>'
            f'<button type="button" id="dnext" class="dbtn">Desbloquear siguiente</button><button type="button" id="dall" class="dbtn pri">Mostrar derivación completa</button>'
            f'<button type="button" id="dreset" class="dbtn ghost">Volver a empezar</button></div></header><ol class="dsteps">{li}</ol></section>')
DJS=r"""
(function(){var S=[].slice.call(document.querySelectorAll('.dstep'));if(!S.length)return;var k=1,n=S.length,RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
 function upd(go){S.forEach(function(e,i){e.classList.toggle('open',i<k);e.classList.toggle('next',i===k);e.classList.toggle('locked',i>k)});
  document.getElementById('dk').textContent=Math.min(k,n);document.getElementById('dfill').style.width=(100*Math.min(k,n)/n)+'%';
  document.getElementById('dnext').disabled=k>=n;document.getElementById('dall').disabled=k>=n;
  if(go&&S[go-1])S[go-1].scrollIntoView({behavior:RM?'auto':'smooth',block:'nearest'})}
 S.forEach(function(e,i){e.querySelector('.dunl').addEventListener('click',function(){k=i+1;upd(k)})});
 document.getElementById('dnext').addEventListener('click',function(){if(k<n){k++;upd(k)}});
 document.getElementById('dall').addEventListener('click',function(){k=n;upd()});
 document.getElementById('dreset').addEventListener('click',function(){k=1;upd(1)});
 upd()})();
"""
def page(fn,title,h1,sub,eqs,bar,charts,side,js,extra_css=''):
    r=BYFN[fn];slug,grp,short=r[1],r[2],r[3];g=GROUPS[grp]
    if fn in TEX: eqs=[T(e) for e in TEX[fn]]
    eqh=''.join(e if e.startswith('<span') else '<span>%s</span>'%e for e in eqs)
    sub=SUB.get(fn,sub)
    doc=head(f'{title} · {SITE}',sub)+extra_css+f'''
</style>
{MATHJAX}
</head>
<body>
{topbar(slug)}
<div class="wrap">
  <header class="plate">
    <span class="mno">{mno(slug)}</span>
    <span class="grp">{g[0]} · {g[1]}</span>
    <h1>{h1}</h1>
    <p class="sub">{sub}{' <a class="dlink" href="#derivacion">Ver la derivación paso a paso ↓</a>' if fn in DERIV else ''}</p>
    <div class="eq">{eqh}</div>
  </header>
{bar}
  <div class="layout">
    <div class="charts">
{charts}
    </div>
    <aside class="side">
{side}
    </aside>
  </div>
  {deriv_html(fn)}
  {pager(slug)}
</div>
{foot()}
<script>
{LIB}
{js}
{DJS}
(function(){{var b=document.getElementById('pl');if(!b)return;var f=function(){{b.classList.toggle('run',/paus/i.test(b.textContent))}};new MutationObserver(f).observe(b,{{childList:true,characterData:true,subtree:true}});f()}})();
</script>
</body>
</html>
'''
    open(os.path.join(OUT,slug+'.html'),'w',encoding='utf-8').write(doc)
for f in ['pages0.py','pages1.py','pages2.py','pages3.py','pages4.py']:
    exec(open(os.path.join(H,f),encoding='utf-8').read())
exec(open(os.path.join(H,'index_page.py'),encoding='utf-8').read())
