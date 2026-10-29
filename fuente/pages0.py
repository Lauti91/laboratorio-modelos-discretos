# =============== 0. Telaraña estándar (página original, integrada al sistema) ===============
_src=open(os.path.join(H,'cobweb_src.html'),encoding='utf-8').read()
def _cut(s,a,b):
    i=s.index(a);j=s.index(b,i);return s[i:j]
_bar=_cut(_src,'<div class="bar">','<div class="layout">').rstrip()
_bar=_bar[:_bar.rfind('</div>')+6]
import re as _re
_bar=_re.sub(r'<button type="button" class="go" id="step">.*?id="rs">Reiniciar</button>',lambda m:'<span class="ctrls">'+_re.sub(r'>\s+<','><',m.group(0))+'</span>',_bar,flags=_re.S)
_charts=_cut(_src,'<div class="charts">','<aside class="side">')
_charts=_charts[len('<div class="charts">'):_charts.rfind('</div>')]
_side=_cut(_src,'<aside class="side">','</aside>')[len('<aside class="side">'):]
_js=_cut(_src,'<script>','</script>')[len('<script>'):]
# etiquetas en LaTeX
for a,b in [('α (demanda) <output','<span class="lt">\\(\\alpha\\) (demanda)</span><output'),('γ (oferta) <output','<span class="lt">\\(\\gamma\\) (oferta)</span><output'),
            ('β (pendiente de D) <output','<span class="lt">\\(\\beta\\) (pendiente de D)</span><output'),('δ (pendiente de S) <output','<span class="lt">\\(\\delta\\) (pendiente de S)</span><output'),
            ('P₀ − P* <output','<span class="lt">\\(P_0-P^*\\)</span><output'),('Velocidad <output','<span class="lt">Velocidad</span><output'),
            ('<div class="l">A = −δ/β</div>','<div class="l">\\(A=-\\delta/\\beta\\)</div>'),('<div class="l">P* = (α+γ)/(β+δ)</div>','<div class="l">\\(P^*\\) de equilibrio</div>'),
            ('<div class="l">Período t · precio P<sub>t</sub></div>','<div class="l">Período \\(t\\) · precio \\(P_t\\)</div>'),
            (' style="font-family:var(--sans);font-size:16px;font-weight:600"',''),('<div class="v" id="vT">','<div class="v t" id="vT">')]:
    assert a in _side,a; _side=_side.replace(a,b)
_side=_side.replace('<div class="ctl" style="margin-bottom:0">','<div class="ctl">')
for a,b in [("font-size=\"13\" text-anchor=\"end\" '+TX+'>P</text>","class=\"mv\" text-anchor=\"end\" '+TX+'>P</text>"),
            ("font-size=\"13\" '+TX+'>Q</text>","class=\"mv\" '+TX+'>Q</text>"),
            ("font-size=\"12\" text-anchor=\"end\" '+TX+'>t</text>","class=\"mv\" text-anchor=\"end\" '+TX+'>t</text>")]:
    assert a in _js,a; _js=_js.replace(a,b)
page('00_telarana.html','Telaraña estándar','Modelo de la telaraña','',[],'  '+_bar,_charts,_side,'(function(){'+_js+'})();')
