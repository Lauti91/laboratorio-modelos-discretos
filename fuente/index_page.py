# =============== Portada ===============
GROUP_INFO=[
 ('I','Modelos I','Primer orden','Un coeficiente y una condición inicial. El equilibrio es \\(y^*=B/(1-A)\\) y todo depende de dónde cae \\(A\\).','\\(|A|\\lt 1\\)'),
 ('II','Modelos II','Segundo orden','Dos rezagos y dos raíces. La trayectoria puede ser monótona, en zigzag o cíclica, y el triángulo de Schur decide si converge.','\\(1-q\\gt 0,\\;1\\pm p+q\\gt 0\\)'),
 ('III','Modelos III','Macroeconomía dinámica','El mismo aparato aplicado al ingreso, al crecimiento y a la inflación: ciclos endógenos, techos y pisos, y la curva de Phillips.','\\(|R_1|,\\,|R_2|\\lt 1\\)'),
]
CARDS={
 'I':[('ecuacion-canonica','Herramienta','Ecuación canónica',r'y_{t+1}=A\,y_t+B','El punto de partida: diagrama de fases, trayectoria y los cuatro casos según \\(A\\).'),
      ('interes-y-rentas','Finanzas','Interés y rentas',r'S_{t+1}=(1+i)\,S_t+c','Capitalización, valor final de una renta y saldo de un préstamo.'),
      ('telarana-estandar','Mercado','Telaraña estándar',r'P_{t+1}=\tfrac{\alpha+\gamma}{\beta}-\tfrac{\delta}{\beta}P_t','El ciclo de la telaraña, escalón por escalón sobre la oferta y la demanda.'),
      ('expectativas-adaptativas','Mercado','Expectativas adaptativas',r'A=1-\eta\left(1+\tfrac{\delta}{\beta}\right)','Cómo una velocidad de ajuste \\(\\eta\\) chica estabiliza un mercado explosivo.'),
      ('mercado-con-inventarios','Mercado','Mercado con inventarios',r'A=1-\sigma(\beta+\delta)','El precio responde al stock: zonas monótona, oscilante y explosiva según \\(\\sigma\\).')],
 'II':[('triangulo-de-estabilidad','Herramienta','Triángulo de estabilidad',r'y_{t+2}+p\,y_{t+1}+q\,y_t=g','Arrastrá \\((p,q)\\) por el triángulo y mirá cómo cambian las raíces y la trayectoria.'),
       ('telarana-extrapolacion','Mercado','Telaraña con extrapolación',r'P_{t+2}+\mu(1+\phi)P_{t+1}-\mu\phi P_t=g','Proyectar la tendencia: ciclos, zigzag y la región estable en el plano \\((\\mu,\\phi)\\).'),
       ('metzler','Macro','Inventarios de Metzler',r'Y_{t+2}-c(2+k)Y_{t+1}+c(1+k)Y_t=V_0','Stock deseado y acelerador: los cuatro regímenes del ingreso según \\(c\\) y \\(k\\).')],
 'III':[('samuelson','Macro','Samuelson',r'Y_{t+2}-\gamma(1+\alpha)Y_{t+1}+\alpha\gamma Y_t=G_0','Multiplicador más acelerador: ciclos sin shocks externos. Estable si \\(\\alpha\\gamma\\lt 1\\).'),
        ('hicks','Macro','Hicks',r'Y_{t+2}-(\gamma+\alpha)Y_{t+1}+\alpha Y_t=I_0(1+g)^{t+2}','Ciclo alrededor de una tendencia creciente, con techo y piso opcionales.'),
        ('inflacion-desempleo','Macro','Inflación y desempleo',r'p_{t+2}-a_1p_{t+1}+a_2p_t=\tfrac{j\beta km}{1+\beta k}','Phillips con expectativas: un cambio de \\(m\\) y la curva de largo plazo según \\(g\\).')],
}
def _card(c,first=False,n=3):
    slug,tag,name,eq,desc=c
    cls=(' w5' if n==5 else ' w3') if first else ''
    vb='0 0 420 190' if first else '0 0 320 92'
    return (f'<a class="mcard{cls}" href="{slug}.html"><svg class="spark" data-s="{slug}" viewBox="{vb}" role="img" aria-label="Trayectoria típica de {name}"></svg>'
            f'<div class="mc-body"><span class="mc-tag">{tag}</span><h3>{name}</h3><span class="mc-eq">\\({eq}\\)</span><p>{desc}</p><span class="mc-go">Abrir simulador <span aria-hidden="true">→</span></span></div></a>')
groups=''
for gid,k,t,d,crit in GROUP_INFO:
    groups+=(f'<section class="group" id="modelos-{gid.lower()}"><header class="ghead"><div class="gnum" aria-hidden="true">{gid}</div>'
             f'<div class="gtxt"><span class="kicker">{k}</span><h2 class="gt">{t}</h2><p>{d}</p></div>'
             f'<div class="crit"><span class="cl">Estable si</span><span class="cv">{crit}</span></div></header>'
             f'<div class="cards">{"".join(_card(c,i==0,len(CARDS[gid])) for i,c in enumerate(CARDS[gid]))}</div></section>\n')
IDX_CSS=r'''
.home{max-width:1180px;margin:0 auto}
.hero{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:40px;align-items:center;padding:56px 0 40px}
.display{font-family:var(--display);font-weight:600;font-size:clamp(42px,6.4vw,78px);line-height:.98;letter-spacing:-.025em;margin:14px 0 18px;text-wrap:balance}
.display em{font-style:italic;font-weight:500;color:var(--accent)}
.lead{font-size:17.5px;line-height:1.6;color:var(--muted);max-width:52ch;margin:0}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.btn{display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;font-size:14.5px;border-radius:10px;padding:11px 18px;border:1px solid var(--line2);background:var(--surface);transition:transform .15s,border-color .15s,filter .15s}
.btn:hover{border-color:var(--fg);transform:translateY(-1px)}
.btn.pri{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.btn.pri:hover{filter:brightness(1.08)}
.hero-fig{margin:0;padding:18px 18px 14px;display:flex;flex-direction:column;gap:10px}
.hf-top{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.hf-eq{font-size:18px}
.hf-state{font-size:13.5px;font-weight:600;padding:3px 10px;border-radius:999px;background:var(--chip)}
.hf-ctl{display:flex;align-items:center;gap:12px}
.hf-ctl label{font-size:14px;color:var(--muted);white-space:nowrap}
.hf-ctl output{font-family:var(--mono);font-size:14px;background:var(--chip);border-radius:6px;padding:1px 8px;min-width:62px;text-align:center}
.hf-chips{display:flex;flex-wrap:wrap;gap:6px}
.hero-fig figcaption{font-size:13px;color:var(--faint)}
.how{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:6px 0 26px;padding:0;list-style:none;counter-reset:s}
.how li{counter-increment:s;display:flex;gap:12px;align-items:flex-start;padding:14px 16px;border-top:2px solid var(--fg)}
.how li::before{content:counter(s);font-family:var(--display);font-size:30px;line-height:1;color:var(--accent);font-weight:600}
.how b{display:block;font-size:15px}
.how span{font-size:13.5px;color:var(--muted)}
.group{padding:34px 0 8px;scroll-margin-top:12px}
.ghead{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:20px;align-items:end;padding-bottom:16px;margin-bottom:18px;border-bottom:1px solid var(--line)}
.gnum{font-family:var(--display);font-size:clamp(56px,7vw,88px);line-height:.8;font-weight:500;color:var(--accent);font-style:italic;min-width:1.1em}
.gt{font-family:var(--display);font-size:clamp(26px,3.2vw,34px);font-weight:600;margin:4px 0 6px;text-transform:none;letter-spacing:-.01em;color:var(--fg)}
.gtxt p{margin:0;color:var(--muted);max-width:64ch}
.crit{display:flex;flex-direction:column;align-items:flex-end;gap:4px;padding:8px 12px;border:1px dashed var(--line2);border-radius:10px;background:var(--surface)}
.crit .cl{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.crit .cv{font-size:15.5px}
.cards{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}
@media (min-width:640px){.cards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:980px){.cards{grid-template-columns:repeat(3,minmax(0,1fr))}}
.mcard{display:flex;flex-direction:column;text-decoration:none;background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:var(--shadow);transition:transform .18s,border-color .18s,box-shadow .18s}
.mcard:hover{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 10px 30px rgba(21,32,43,.08)}
.spark{background:var(--surface2);border-bottom:1px solid var(--line);
  background-image:linear-gradient(var(--grid2) 1px,transparent 1px),linear-gradient(90deg,var(--grid2) 1px,transparent 1px);background-size:16px 16px}
.mc-body{display:flex;flex-direction:column;gap:7px;padding:14px 16px 16px;flex:1}
.mc-tag{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600}
.mcard h3{font-family:var(--display);font-size:22px;font-weight:600;margin:0;line-height:1.15}
.mc-eq{font-size:14px;max-width:100%;overflow-x:auto;overflow-y:hidden;padding:2px 0;color:var(--fg)}
.mcard p{margin:0;font-size:14px;color:var(--muted);flex:1}
.mc-go{font-size:13.5px;font-weight:600;color:var(--accent);margin-top:4px}
.mcard:hover .mc-go span{display:inline-block;transform:translateX(3px);transition:transform .18s}
@media (min-width:640px){.mcard.w5{grid-column:span 2;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr)}.mcard.w5 .spark{height:100%;border-bottom:0;border-right:1px solid var(--line)}.mcard.w5 .mc-body{justify-content:center;padding:22px 24px}.mcard.w5 h3{font-size:27px}.mcard.w5 .mc-eq{font-size:17px}}
@media (min-width:640px) and (max-width:979px){.mcard.w3{grid-column:span 2;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr)}.mcard.w3 .spark{height:100%;border-bottom:0;border-right:1px solid var(--line)}.mcard.w3 .mc-body{justify-content:center;padding:22px 24px}.mcard.w3 h3{font-size:27px}.mcard.w3 .mc-eq{font-size:17px}}
@media (max-width:560px){.ghead{grid-template-columns:minmax(0,1fr);gap:8px}.gnum{font-size:52px}.crit{grid-column:1}}
@media (max-width:900px){.hero{grid-template-columns:minmax(0,1fr);padding-top:36px;gap:28px}.how{grid-template-columns:minmax(0,1fr)}.ghead{grid-template-columns:auto minmax(0,1fr)}.crit{grid-column:1/-1;align-items:flex-start;flex-direction:row;gap:10px;align-self:start}}
@media (max-width:420px){.cards{grid-template-columns:minmax(0,1fr)}.display{font-size:40px}}
'''
IDX_JS=r'''
var $=function(i){return document.getElementById(i)};
function F(x,d){return x.toLocaleString('es-AR',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d})}
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
/* ---------- figura del hero ---------- */
var HW=560,HH=290,HL=40,HR=46,HT=16,HB=32,N=16,YS=10,Y0=18,LO=0,HI=20;
function hX(t){return HL+t/N*(HW-HL-HR)}function hY(v){return HT+(HH-HT-HB)*(1-(v-LO)/(HI-LO))}
function regime(A){if(Math.abs(A-1)<1e-9)return['Constante','var(--warn)'];if(A>1)return['Monótona explosiva','var(--bad)'];
 if(A>0)return['Monótona convergente','var(--good)'];if(Math.abs(A)<1e-9)return['Converge en un paso','var(--good)'];
 if(Math.abs(A+1)<1e-9)return['Oscilación uniforme','var(--warn)'];if(A>-1)return['Oscilación amortiguada','var(--good)'];return['Oscilación explosiva','var(--bad)']}
var prog=RM?1:0;
function hero(){var A=+$('hA').value,y=[Y0];for(var t=0;t<N;t++)y.push(A*y[t]+YS*(1-A));
 var o='<defs><clipPath id="hc"><rect x="'+HL+'" y="'+(HT-4)+'" width="'+(HW-HL-HR+6)+'" height="'+(HH-HT-HB+8)+'"/></clipPath></defs>';
 [0,5,10,15,20].forEach(function(v){o+='<line x1="'+HL+'" x2="'+(HW-HR)+'" y1="'+hY(v)+'" y2="'+hY(v)+'" style="stroke:var(--line)"/><text x="'+(HL-8)+'" y="'+(hY(v)+4)+'" font-size="13" text-anchor="end" style="fill:var(--faint)">'+v+'</text>'});
 for(var t=0;t<=N;t+=4)o+='<text x="'+hX(t)+'" y="'+(HH-10)+'" font-size="13" text-anchor="middle" style="fill:var(--faint)">'+t+'</text>';
 o+='<text x="'+(HW-HR+30)+'" y="'+(HH-10)+'" class="mv" text-anchor="start" style="fill:var(--muted)">t</text>';
 o+='<line x1="'+HL+'" x2="'+(HW-HR)+'" y1="'+hY(YS)+'" y2="'+hY(YS)+'" style="stroke:var(--supply)" stroke-width="1.6" stroke-dasharray="6 5"/>';
 o+='<text x="'+(HW-HR+14)+'" y="'+(hY(YS)+5)+'" class="mv" style="fill:var(--supply)">y*</text>';
 var n=Math.max(1,Math.round(prog*N)),pts=[];for(var t=0;t<=n;t++)pts.push(hX(t).toFixed(1)+','+hY(y[t]).toFixed(1));
 o+='<g clip-path="url(#hc)"><polyline fill="none" style="stroke:var(--accent)" stroke-width="2.6" stroke-linejoin="round" points="'+pts.join(' ')+'"/>';
 for(var t=0;t<=n;t++)o+='<circle cx="'+hX(t).toFixed(1)+'" cy="'+hY(y[t]).toFixed(1)+'" r="'+(t===n?5.5:3.2)+'" style="fill:'+(t===n?'var(--accent)':'var(--surface)')+';stroke:var(--accent)" stroke-width="2"/>';
 o+='</g>';$('hplot').innerHTML=o;
 $('o_hA').textContent=F(A);var r=regime(A),s=$('hstate');s.textContent=r[0];s.style.color=r[1]}
function intro(ts0){var t0=null;function f(ts){if(t0==null)t0=ts;prog=Math.min(1,(ts-t0)/1500);hero();if(prog<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
$('hA').addEventListener('input',function(){prog=1;hero()});
Array.prototype.forEach.call(document.querySelectorAll('[data-a]'),function(b){b.addEventListener('click',function(){$('hA').value=b.dataset.a;prog=RM?1:0;if(RM)hero();else intro()})});
hero();if(!RM)intro();
/* ---------- miniaturas ---------- */
function lin(A,B,y0,n){var y=[y0];for(var t=0;t<n;t++)y.push(A*y[t]+B);return y}
function sec(p,q,g,y0,y1,n){var y=[y0,y1];for(var t=2;t<=n;t++)y.push(g-p*y[t-1]-q*y[t-2]);return y}
var SP={
 'ecuacion-canonica':function(){return{y:lin(-0.7,17,18,16),s:10}},
 'interes-y-rentas':function(){return{y:lin(1.08,10,0,16),s:null}},
 'telarana-estandar':function(){return{y:lin(-0.8,7.2,5.2,16),s:4}},
 'expectativas-adaptativas':function(){return{y:lin(-0.5,6,5.2,12),s:4}},
 'mercado-con-inventarios':function(){return{y:lin(0.55,1.8,6.4,14),s:4}},
 'triangulo-de-estabilidad':function(){return{y:sec(-1,0.5,5,16,14,22),s:10}},
 'telarana-extrapolacion':function(){return{y:sec(1.2,0.8,12,4.6,12-2*4.6,24),s:4}},
 'metzler':function(){return{y:sec(-1.68,0.88,20,100,110,30),s:100}},
 'samuelson':function(){return{y:sec(-1.5,0.9,20,50,60,30),s:50}},
 'hicks':function(){var ga=.6,al=.5,g=.03,I=10,G=1+g,D=G*G-(ga+al)*G+al,A=I*G*G/D,y=[A,A*G*1.12],tr=[];
   for(var t=0;t<=30;t++)tr.push(A*Math.pow(G,t));for(var t=2;t<=30;t++)y.push((ga+al)*y[t-1]-al*y[t-2]+I*Math.pow(G,t));return{y:y,s:null,tr:tr}},
 'inflacion-desempleo':function(){var a=8,be=1,g=.8,j=.5,k=.4,mo=4,mn=8,pi=mo,U=(a-(1-g)*mo)/be,P=[];
   for(var t=0;t<=30;t++){var pt=a-be*U+g*pi;P.push(pt);var pin=pi+j*(pt-pi);U=(U-k*mn+k*(a+g*pin))/(1+be*k);pi=pin}return{y:P,s:mn}}
};
Array.prototype.forEach.call(document.querySelectorAll('.spark'),function(el){var d=SP[el.dataset.s]();if(!d)return;
 var vb=el.viewBox.baseVal,W=vb.width,Hh=vb.height,L=14,R=14,T=14,B=14,y=d.y,n=y.length-1,vals=y.concat(d.s==null?[]:[d.s]).concat(d.tr||[]);
 var lo=Math.min.apply(null,vals),hi=Math.max.apply(null,vals),pd=(hi-lo)*0.08;lo-=pd;hi+=pd;
 var X=function(t){return L+t/n*(W-L-R)},Y=function(v){return T+(Hh-T-B)*(1-(v-lo)/(hi-lo))};
 var o='';if(d.s!=null)o+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(d.s)+'" y2="'+Y(d.s)+'" style="stroke:var(--supply)" stroke-width="1.3" stroke-dasharray="5 4" opacity=".8"/>';
 if(d.tr)o+='<polyline fill="none" style="stroke:var(--supply)" stroke-width="1.3" stroke-dasharray="5 4" opacity=".8" points="'+d.tr.map(function(v,t){return X(t).toFixed(1)+','+Y(v).toFixed(1)}).join(' ')+'"/>';
 o+='<polyline fill="none" style="stroke:var(--accent)" stroke-width="2.2" stroke-linejoin="round" points="'+y.map(function(v,t){return X(t).toFixed(1)+','+Y(v).toFixed(1)}).join(' ')+'"/>';
 y.forEach(function(v,t){if(n<=16||t%2===0)o+='<circle cx="'+X(t).toFixed(1)+'" cy="'+Y(v).toFixed(1)+'" r="2" style="fill:var(--accent)"/>'});
 o+='<circle cx="'+X(n).toFixed(1)+'" cy="'+Y(y[n]).toFixed(1)+'" r="4" style="fill:var(--accent);stroke:var(--surface)" stroke-width="2"/>';
 el.innerHTML=o});
'''
HERO=r'''
<section class="hero">
  <div class="hero-text">
    <span class="kicker">Ecuaciones en diferencias</span>
    <h1 class="display">Laboratorio de modelos <em>discretos</em></h1>
    <p class="lead">Once simuladores para ver cómo se mueve una economía período a período. Cada uno resuelve un modelo de la cursada y deja cambiar los parámetros mientras la trayectoria se dibuja.</p>
    <div class="cta"><a class="btn pri" href="ecuacion-canonica.html">Empezar por la ecuación canónica <span aria-hidden="true">→</span></a><a class="btn" href="#modelos-i">Ver los once modelos</a></div>
  </div>
  <figure class="hero-fig card">
    <div class="hf-top"><span class="hf-eq">\(y_{t+1}=A\,y_t+B\)</span><span class="hf-state" id="hstate" role="status"></span></div>
    <svg id="hplot" viewBox="0 0 560 290" role="img" aria-label="Trayectoria de y en el tiempo para el valor elegido de A"></svg>
    <div class="hf-ctl"><label for="hA">Mové \(A\)</label><input type="range" id="hA" min="-1.2" max="1.2" step="0.05" value="-0.7"><output id="o_hA"></output></div>
    <div class="hf-chips"><button type="button" data-a="0.6">\(A=0{,}6\)</button><button type="button" data-a="-0.7">\(A=-0{,}7\)</button><button type="button" data-a="-1">\(A=-1\)</button><button type="button" data-a="1.1">\(A=1{,}1\)</button></div>
    <figcaption>Con \(|A|\lt 1\) la trayectoria vuelve a \(y^*\); con \(A\lt 0\) lo hace oscilando.</figcaption>
  </figure>
</section>
<ol class="how">
  <li><div><b>Elegí un caso</b><span>Cada simulador trae casos precargados: estable, en el borde y explosivo.</span></div></li>
  <li><div><b>Reproducí la dinámica</b><span>Avanzá período a período o dejá correr la animación.</span></div></li>
  <li><div><b>Mové los parámetros</b><span>Las raíces, el equilibrio y el régimen se recalculan al instante.</span></div></li>
</ol>
'''
doc=head(SITE,'Simuladores interactivos de ecuaciones en diferencias para Matemática Aplicada II: primer orden, segundo orden y macroeconomía dinámica.')+IDX_CSS+'</style>\n'+MATHJAX+'\n</head>\n<body>\n'+topbar()+'\n<main class="home">'+HERO+groups+'</main>\n'+foot()+'\n<script>'+IDX_JS+'</script>\n</body>\n</html>\n'
open(os.path.join(OUT,'index.html'),'w',encoding='utf-8').write(doc)
