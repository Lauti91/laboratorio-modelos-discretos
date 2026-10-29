# =============== Portada: frente del instrumento + rack de módulos ===============
BANKS=[
 ('I','Primer orden','Un coeficiente y una condición inicial. El equilibrio es \\(y^*=B/(1-A)\\) y todo depende de dónde cae \\(A\\).','\\(|A|\\lt 1\\)'),
 ('II','Segundo orden','Dos rezagos y dos raíces: trayectorias monótonas, en zigzag o cíclicas. El triángulo de Schur decide si convergen.','\\(1-q\\gt 0,\\;1\\pm p+q\\gt 0\\)'),
 ('III','Macroeconomía dinámica','El mismo aparato aplicado al ingreso, al crecimiento y a la inflación.','\\(|R_1|,\\,|R_2|\\lt 1\\)'),
]
UNITS={
 'I':[('ecuacion-canonica','Herramienta','Ecuación canónica',r'y_{t+1}=A\,y_t+B','Diagrama de fases, trayectoria y los cuatro casos según \\(A\\).'),
      ('interes-y-rentas','Finanzas','Interés y rentas',r'S_{t+1}=(1+i)\,S_t+c','Capitalización, valor final de una renta y saldo de un préstamo.'),
      ('telarana-estandar','Mercado','Telaraña estándar',r'P_{t+1}=\tfrac{\alpha+\gamma}{\beta}-\tfrac{\delta}{\beta}P_t','El ciclo de la telaraña sobre la oferta y la demanda.'),
      ('expectativas-adaptativas','Mercado','Expectativas adaptativas',r'A=1-\eta\left(1+\tfrac{\delta}{\beta}\right)','Una velocidad de ajuste \\(\\eta\\) chica estabiliza un mercado explosivo.'),
      ('mercado-con-inventarios','Mercado','Mercado con inventarios',r'A=1-\sigma(\beta+\delta)','El precio responde al stock. Zonas según \\(\\sigma\\).')],
 'II':[('triangulo-de-estabilidad','Herramienta','Triángulo de estabilidad',r'y_{t+2}+p\,y_{t+1}+q\,y_t=g','Arrastrá \\((p,q)\\) y mirá las raíces y la trayectoria.'),
       ('telarana-extrapolacion','Mercado','Telaraña con extrapolación',r'P_{t+2}+\mu(1+\phi)P_{t+1}-\mu\phi P_t=g','Proyectar la tendencia: ciclos, zigzag y la región estable.'),
       ('metzler','Macro','Inventarios de Metzler',r'Y_{t+2}-c(2+k)Y_{t+1}+c(1+k)Y_t=V_0','Los cuatro regímenes del ingreso según \\(c\\) y \\(k\\).')],
 'III':[('samuelson','Macro','Samuelson',r'Y_{t+2}-\gamma(1+\alpha)Y_{t+1}+\alpha\gamma Y_t=G_0','Multiplicador y acelerador: ciclos sin shocks externos.'),
        ('hicks','Macro','Hicks',r'Y_{t+2}-(\gamma+\alpha)Y_{t+1}+\alpha Y_t=I_0(1+g)^{t+2}','Ciclo alrededor de una tendencia, con techo y piso.'),
        ('inflacion-desempleo','Macro','Inflación y desempleo',r'p_{t+2}-a_1p_{t+1}+a_2p_t=\tfrac{j\beta km}{1+\beta k}','Phillips con expectativas y la curva de largo plazo.')],
}
def _unit(u):
    slug,tag,name,eq,desc=u
    return (f'<a class="unit" href="{slug}.html"><span class="ear" aria-hidden="true"></span>'
            f'<span class="u-id"><span class="mno">{mno(slug)}</span><span class="u-tag">{tag}</span></span>'
            f'<span class="u-name"><b>{name}</b><small>{desc}</small></span>'
            f'<span class="u-eq">\\({eq}\\)</span>'
            f'<svg class="spark" data-s="{slug}" viewBox="0 0 240 70" role="img" aria-label="Trayectoria típica de {name}"></svg>'
            f'<span class="u-key">Abrir</span><span class="ear" aria-hidden="true"></span></a>')
banks=''
for bid,t,d,crit in BANKS:
    banks+=(f'<section class="bank" id="modelos-{bid.lower()}"><header class="bhead"><span class="bno">Banco {bid}</span>'
            f'<div class="btxt"><h2 class="bt">{t}</h2><p>{d}</p></div>'
            f'<div class="crit"><span class="cl">Estable si</span><span class="cv">{crit}</span></div></header>'
            f'<div class="units">{"".join(_unit(u) for u in UNITS[bid])}</div></section>\n')
IDX_CSS=r'''
.home{max-width:1200px;margin:0 auto;display:flex;flex-direction:column;gap:22px}
.front{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:28px;align-items:stretch;background:var(--panel);border:1px solid var(--edge);border-radius:10px;padding:26px;
  box-shadow:inset 0 1px 0 var(--edge-hi),0 18px 40px rgba(0,0,0,.35);position:relative}
.front::before,.front::after{content:"";position:absolute;top:12px;width:10px;height:10px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#5d6d85,#1a2638 70%);box-shadow:inset 0 0 0 1px rgba(0,0,0,.5)}
.front::before{left:12px}.front::after{right:12px}
.fr-l{display:flex;flex-direction:column;justify-content:space-between;gap:26px;padding:10px 4px 4px}
.fr-l .keys{margin-top:26px}
.dir{display:flex;flex-direction:column;border-top:1px solid var(--edge)}
.dir a{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:12px;align-items:center;padding:10px 2px;border-bottom:1px solid var(--edge);text-decoration:none}
.dir a:hover b{color:var(--ch1)}
.dir .bno{font-size:13px;padding:4px 0 3px;text-align:center}
.dir b{font-family:var(--cond);font-weight:600;font-size:18px;letter-spacing:.06em;text-transform:uppercase}
.dir .rng{font-family:var(--mono);font-size:13px;color:var(--muted)}
.serial{font-family:var(--mono);font-size:13px;color:var(--muted);display:flex;gap:8px;flex-wrap:wrap}
.serial span{border:1px solid var(--edge);padding:3px 8px;border-radius:3px;background:var(--panel2)}
.big{font-family:var(--cond);font-weight:700;text-transform:uppercase;font-size:clamp(44px,6.4vw,84px);line-height:.9;letter-spacing:.005em;margin:16px 0 0}
.big span{display:block;color:var(--ch1);text-shadow:0 0 22px rgba(255,138,31,.25)}
.keys{display:flex;flex-wrap:wrap;gap:10px}
.key{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--cond);font-weight:600;font-size:16px;letter-spacing:.1em;text-transform:uppercase;
  background:linear-gradient(#22324a,#1a273b);border:1px solid #050a12;border-radius:4px;padding:10px 16px 9px;box-shadow:inset 0 1px 0 rgba(255,255,255,.09),0 3px 0 #050a12}
.key:hover{background:linear-gradient(#2a3c58,#1f2f47)}
.key:active{transform:translateY(3px);box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}
.key .led{width:9px;height:9px;border-radius:50%;background:var(--good);box-shadow:0 0 8px var(--good)}
.key.dim .led{background:#2a3850;box-shadow:none}
.scope{display:flex;flex-direction:column;background:var(--panel2);border:1px solid var(--edge);border-radius:8px;padding:12px;gap:10px;box-shadow:inset 0 1px 0 var(--edge-hi)}
.screen{background:var(--surface);border:1px solid #03070e;border-radius:6px;box-shadow:inset 0 0 0 1px var(--edge),inset 0 3px 18px rgba(0,0,0,.7);padding:10px 12px 6px;
  background-image:radial-gradient(ellipse at 50% 40%,rgba(90,169,255,.05),transparent 70%)}
.sc-top{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap;font-family:var(--mono);font-size:13px;color:var(--muted)}
.ch{display:inline-flex;align-items:center;gap:6px;margin-right:12px}
.ch i{width:12px;height:3px;border-radius:2px;display:inline-block}
.sc-eq{color:var(--fg);font-size:15px}
.lcd{display:grid;grid-template-columns:auto auto minmax(0,1fr);gap:8px}
.lcd div{background:var(--surface);border:1px solid #03070e;border-radius:4px;padding:5px 10px;box-shadow:inset 0 2px 6px rgba(0,0,0,.55);min-width:0}
.lcd small{display:block;font-family:var(--cond);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.lcd b{font-family:var(--mono);font-weight:400;font-size:19px;color:var(--ch2)}
.lcd b#hstate{font-family:var(--cond);font-weight:600;letter-spacing:.06em;text-transform:uppercase;font-size:17px;text-shadow:0 0 10px currentColor;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:block}
.fader{display:flex;align-items:center;gap:12px}
.fader label{font-family:var(--cond);font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--legend);white-space:nowrap}
.fader input{flex:1}
.presets{display:flex;flex-wrap:wrap;gap:6px}
.bank{display:flex;flex-direction:column;gap:8px;scroll-margin-top:12px}
.bhead{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:18px;align-items:center;padding:4px 2px 8px}
.bno{font-family:var(--cond);font-weight:700;font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:#0a111c;background:var(--legend);padding:6px 10px 5px;border-radius:3px;white-space:nowrap}
.bt{font-family:var(--cond);font-weight:700;font-size:clamp(24px,3vw,32px);letter-spacing:.04em;text-transform:uppercase;margin:0;color:var(--fg);display:block}
.bt::after{display:none}
.btxt p{margin:2px 0 0;color:var(--muted);max-width:70ch}
.crit{background:var(--surface);border:1px solid #03070e;border-radius:4px;padding:6px 12px;box-shadow:inset 0 2px 6px rgba(0,0,0,.55);text-align:right}
.crit .cl{display:block;font-family:var(--cond);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.crit .cv{color:var(--ch2);font-size:15px}
.units{display:flex;flex-direction:column;gap:6px}
.unit{display:grid;grid-template-columns:18px 118px minmax(0,1.15fr) minmax(0,1.25fr) 210px 82px 18px;align-items:center;gap:16px;text-decoration:none;
  background:linear-gradient(#142135,#101a2b);border:1px solid var(--edge);border-radius:4px;padding:10px 6px;box-shadow:inset 0 1px 0 var(--edge-hi),0 2px 0 #050a12;transition:border-color .12s}
.unit:hover{border-color:var(--ch1)}
.unit:hover .u-key{color:var(--ch1)}
.unit:hover .u-key::before{background:var(--ch1);box-shadow:0 0 8px var(--ch1)}
.ear{align-self:stretch;display:flex;flex-direction:column;justify-content:space-between;padding:2px 0}
.ear::before,.ear::after{content:"";width:9px;height:9px;margin:0 auto;border-radius:50%;background:radial-gradient(circle at 35% 35%,#5d6d85,#172235 70%);box-shadow:inset 0 0 0 1px rgba(0,0,0,.5)}
.u-id{display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.u-id .mno{margin-top:0;grid-row:auto}
.u-tag{font-family:var(--cond);font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.u-name b{display:block;font-family:var(--cond);font-weight:600;font-size:21px;letter-spacing:.04em;text-transform:uppercase;line-height:1.1}
.u-name small{display:block;color:var(--muted);font-size:14px;margin-top:3px}
.u-eq{background:var(--surface);border:1px solid #03070e;border-radius:4px;padding:8px 10px;box-shadow:inset 0 2px 6px rgba(0,0,0,.55);font-size:14px;overflow-x:auto;overflow-y:hidden;color:var(--fg);min-height:46px;display:flex;align-items:center}
.unit .spark{background:var(--surface);border:1px solid #03070e;border-radius:4px;box-shadow:inset 0 0 0 1px var(--edge);
  background-image:linear-gradient(rgba(140,170,210,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(140,170,210,.09) 1px,transparent 1px);background-size:24px 14px}
.u-key{position:relative;font-family:var(--cond);font-weight:600;font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--legend);
  background:linear-gradient(#22324a,#1a273b);border:1px solid #050a12;border-radius:4px;padding:8px 10px 7px 24px;box-shadow:inset 0 1px 0 rgba(255,255,255,.09),0 2px 0 #050a12;text-align:center}
.u-key::before{content:"";position:absolute;left:9px;top:50%;width:8px;height:8px;margin-top:-4px;border-radius:50%;background:#2a3850}
@media (max-width:1060px){.unit{grid-template-columns:18px 104px minmax(0,1fr) 190px 18px;grid-template-areas:"e1 id nm sp e2" "e1 id eq sp e2" "e1 id eq ky e2"}
  .unit>.ear:first-child{grid-area:e1}.unit>.ear:last-child{grid-area:e2}.u-id{grid-area:id}.u-name{grid-area:nm}.u-eq{grid-area:eq}.unit .spark{grid-area:sp}.u-key{grid-area:ky}}
@media (max-width:900px){.front{grid-template-columns:minmax(0,1fr);padding:20px}.bhead{grid-template-columns:auto minmax(0,1fr)}.crit{grid-column:1/-1;text-align:left;justify-self:start}}
@media (max-width:620px){.unit{grid-template-columns:minmax(0,1fr);grid-template-areas:"id" "nm" "sp" "eq" "ky";padding:12px;gap:10px}.unit>.ear{display:none}
  .u-id{flex-direction:row;align-items:center;gap:10px}.u-key{justify-self:start}.lcd{grid-template-columns:1fr 1fr}.lcd div:last-child{grid-column:1/-1}.bhead{grid-template-columns:minmax(0,1fr)}.bhead>.bno{justify-self:start}.front{padding:16px}#hplot text{font-size:21px!important}#hplot text.mv{font-size:24px!important}}
'''
IDX_JS=r'''
var $=function(i){return document.getElementById(i)};
function F(x,d){return x.toLocaleString('es-AR',{minimumFractionDigits:d==null?2:d,maximumFractionDigits:d==null?2:d})}
var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var HW=560,HH=280,HL=36,HR=40,HT=14,HB=28,N=16,YS=10,Y0=18,LO=0,HI=20;
function hX(t){return HL+t/N*(HW-HL-HR)}function hY(v){return HT+(HH-HT-HB)*(1-(v-LO)/(HI-LO))}
function regime(A){if(Math.abs(A-1)<1e-9)return['Constante','var(--warn)'];if(A>1)return['Monótona explosiva','var(--bad)'];
 if(A>0)return['Monótona convergente','var(--good)'];if(Math.abs(A)<1e-9)return['Converge en un paso','var(--good)'];
 if(Math.abs(A+1)<1e-9)return['Oscilación uniforme','var(--warn)'];if(A>-1)return['Oscilación amortiguada','var(--good)'];return['Oscilación explosiva','var(--bad)']}
var prog=RM?1:0;
function hero(){var A=+$('hA').value,y=[Y0];for(var t=0;t<N;t++)y.push(A*y[t]+YS*(1-A));
 var o='<defs><clipPath id="hc"><rect x="'+HL+'" y="'+(HT-4)+'" width="'+(HW-HL-HR+6)+'" height="'+(HH-HT-HB+8)+'"/></clipPath></defs>';
 for(var v=0;v<=20;v+=2.5){var maj=v%5===0;o+='<line x1="'+HL+'" x2="'+(HW-HR)+'" y1="'+hY(v)+'" y2="'+hY(v)+'" style="stroke:var(--line)"'+(maj?'':' stroke-dasharray="1 5"')+'/>';if(maj)o+='<text x="'+(HL-8)+'" y="'+(hY(v)+4)+'" font-size="12" text-anchor="end" style="fill:var(--faint);font-family:var(--mono)">'+v+'</text>'}
 for(var t=0;t<=N;t+=2){o+='<line x1="'+hX(t)+'" x2="'+hX(t)+'" y1="'+HT+'" y2="'+(HH-HB)+'" style="stroke:var(--line)"'+(t%4?' stroke-dasharray="1 5"':'')+'/>';if(t%4===0)o+='<text x="'+hX(t)+'" y="'+(HH-8)+'" font-size="12" text-anchor="middle" style="fill:var(--faint);font-family:var(--mono)">'+t+'</text>'}
 o+='<line x1="'+HL+'" x2="'+(HW-HR)+'" y1="'+hY(YS)+'" y2="'+hY(YS)+'" style="stroke:var(--ch2)" stroke-width="1.6" stroke-dasharray="7 5"/>';
 o+='<text x="'+(HW-HR+8)+'" y="'+(hY(YS)+5)+'" class="mv" style="fill:var(--ch2)">y*</text>';
 var n=Math.max(1,Math.round(prog*N)),pts=[];for(var t=0;t<=n;t++)pts.push(hX(t).toFixed(1)+','+hY(y[t]).toFixed(1));
 o+='<g clip-path="url(#hc)" style="filter:drop-shadow(0 0 4px rgba(255,138,31,.55))"><polyline fill="none" style="stroke:var(--ch1)" stroke-width="2.4" stroke-linejoin="round" points="'+pts.join(' ')+'"/>';
 for(var t=0;t<=n;t++)o+='<circle cx="'+hX(t).toFixed(1)+'" cy="'+hY(y[t]).toFixed(1)+'" r="'+(t===n?5:2.6)+'" style="fill:var(--ch1)"/>';
 o+='</g>';$('hplot').innerHTML=o;
 $('o_hA').textContent=F(A);$('hmod').textContent=F(Math.abs(A));var r=regime(A),s=$('hstate');s.textContent=r[0];s.style.color=r[1]}
function intro(){var t0=null;function f(ts){if(t0==null)t0=ts;prog=Math.min(1,(ts-t0)/1400);hero();if(prog<1)requestAnimationFrame(f)}requestAnimationFrame(f)}
$('hA').addEventListener('input',function(){prog=1;hero()});
Array.prototype.forEach.call(document.querySelectorAll('[data-a]'),function(b){b.addEventListener('click',function(){$('hA').value=b.dataset.a;prog=RM?1:0;if(RM)hero();else intro()})});
hero();if(!RM)intro();
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
 var vb=el.viewBox.baseVal,W=vb.width,Hh=vb.height,L=10,R=10,T=10,B=10,y=d.y,n=y.length-1,vals=y.concat(d.s==null?[]:[d.s]).concat(d.tr||[]);
 var lo=Math.min.apply(null,vals),hi=Math.max.apply(null,vals),pd=(hi-lo)*0.08;lo-=pd;hi+=pd;
 var X=function(t){return L+t/n*(W-L-R)},Y=function(v){return T+(Hh-T-B)*(1-(v-lo)/(hi-lo))};
 var o='';if(d.s!=null)o+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+Y(d.s)+'" y2="'+Y(d.s)+'" style="stroke:var(--ch2)" stroke-width="1.2" stroke-dasharray="5 4"/>';
 if(d.tr)o+='<polyline fill="none" style="stroke:var(--ch2)" stroke-width="1.2" stroke-dasharray="5 4" points="'+d.tr.map(function(v,t){return X(t).toFixed(1)+','+Y(v).toFixed(1)}).join(' ')+'"/>';
 o+='<g style="filter:drop-shadow(0 0 3px rgba(255,138,31,.6))"><polyline fill="none" style="stroke:var(--ch1)" stroke-width="1.8" stroke-linejoin="round" points="'+y.map(function(v,t){return X(t).toFixed(1)+','+Y(v).toFixed(1)}).join(' ')+'"/>';
 o+='<circle cx="'+X(n).toFixed(1)+'" cy="'+Y(y[n]).toFixed(1)+'" r="3.2" style="fill:var(--ch1)"/></g>';
 el.innerHTML=o});
'''
FRONT=r'''
<section class="front">
  <div class="fr-l">
    <div>
      <div class="serial"><span>Matemática Aplicada II</span><span>FCE-UBA</span><span>11 módulos</span></div>
      <h1 class="big">Laboratorio de modelos <span>discretos</span></h1>
      <div class="keys"><a class="key" href="ecuacion-canonica.html"><i class="led"></i>Encender MD-01</a><a class="key dim" href="#modelos-i"><i class="led"></i>Ver el rack</a></div>
    </div>
    <nav class="dir" aria-label="Bancos">
      <a href="#modelos-i"><span class="bno">I</span><b>Primer orden</b><span class="rng">MD-01 … MD-05</span></a>
      <a href="#modelos-ii"><span class="bno">II</span><b>Segundo orden</b><span class="rng">MD-06 … MD-08</span></a>
      <a href="#modelos-iii"><span class="bno">III</span><b>Macroeconomía dinámica</b><span class="rng">MD-09 … MD-11</span></a>
    </nav>
  </div>
  <div class="scope">
    <div class="screen">
      <div class="sc-top"><span><span class="ch"><i style="background:var(--ch1)"></i>CH1 y(t)</span><span class="ch"><i style="background:var(--ch2)"></i>CH2 y*</span></span><span class="sc-eq">\(y_{t+1}=A\,y_t+B\)</span></div>
      <svg id="hplot" viewBox="0 0 560 280" role="img" aria-label="Trayectoria de y en el tiempo para el valor elegido de A"></svg>
    </div>
    <div class="lcd"><div><small>A</small><b id="o_hA"></b></div><div><small>|A|</small><b id="hmod"></b></div><div><small>Modo</small><b id="hstate" role="status"></b></div></div>
    <div class="fader"><label for="hA">Coeficiente A</label><input type="range" id="hA" min="-1.2" max="1.2" step="0.05" value="-0.7"></div>
    <div class="presets"><button type="button" data-a="0.6">A = 0,6</button><button type="button" data-a="-0.7">A = −0,7</button><button type="button" data-a="-1">A = −1</button><button type="button" data-a="1.1">A = 1,1</button></div>
  </div>
</section>
'''
doc=head(SITE,'Simuladores interactivos de ecuaciones en diferencias para Matemática Aplicada II: primer orden, segundo orden y macroeconomía dinámica.')+IDX_CSS+'</style>\n'+MATHJAX+'\n</head>\n<body>\n'+topbar()+'\n<main class="home">'+FRONT+banks+'</main>\n'+foot()+'\n<script>'+IDX_JS+'</script>\n</body>\n</html>\n'
open(os.path.join(OUT,'index.html'),'w',encoding='utf-8').write(doc)
