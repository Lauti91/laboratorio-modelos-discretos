# Derivaciones paso a paso: fn -> (introducción, [(título, consigna, cuerpo HTML con TeX)])
DERIV={}

DERIV['01_ecuacion_canonica.html']=(r'De la ecuación \(y_{t+1}=A\,y_t+B\) a su solución explícita y a la condición de estabilidad.',[
(r'Planteo',r'',
 r'''<p>Tenemos una ecuación lineal de primer orden con coeficientes constantes y un valor inicial \(y_0\) dado:</p>
\[ y_{t+1}=A\,y_t+B \]
<p>Queremos escribir \(y_t\) como función de \(t\), sin depender del valor anterior.</p>'''),
(r'Iterar desde \(y_0\)',r'Calculá \(y_1\), \(y_2\) e \(y_3\) a mano. ¿Qué patrón aparece?',
 r'''\[ y_1=A\,y_0+B,\qquad y_2=A^2y_0+AB+B,\qquad y_3=A^3y_0+A^2B+AB+B \]
<p>En general, cada período multiplica lo anterior por \(A\) y suma \(B\):</p>
\[ y_t=A^t\,y_0+B\left(1+A+A^2+\dots+A^{t-1}\right) \]'''),
(r'Sumar la progresión geométrica',r'¿Cuánto vale \(1+A+\dots+A^{t-1}\) si \(A\neq1\)?',
 r'''<p>Si \(A\neq1\), la suma geométrica es</p>
\[ 1+A+\dots+A^{t-1}=\frac{1-A^t}{1-A} \]
<p>y por lo tanto</p>
\[ y_t=A^t\,y_0+\frac{B}{1-A}\left(1-A^t\right) \]'''),
(r'El equilibrio \(y^*\)',r'Proponé una solución constante \(y_t=y^*\) para todo \(t\). ¿Qué valor tiene que tomar?',
 r'''<p>Si \(y_{t+1}=y_t=y^*\), la ecuación queda \(y^*=A\,y^*+B\). Despejando:</p>
\[ y^*=\frac{B}{1-A}\qquad (A\neq1) \]
<p>Es el término que apareció en el paso anterior.</p>'''),
(r'Solución general',r'Reescribí el resultado del paso 3 usando \(y^*\).',
 r'''<p>Agrupando los términos que multiplican a \(A^t\):</p>
\[ y_t=\left(y_0-y^*\right)A^t+y^* \]
<p>El desvío \(z_t=y_t-y^*\) cumple \(z_{t+1}=A\,z_t\), o sea \(z_t=z_0A^t\): toda la dinámica está en \(A\).</p>
<p>Si \(A=1\) no hay equilibrio (con \(B\neq0\)) y la suma del paso 2 da \(t\): \(y_t=y_0+B\,t\).</p>'''),
(r'Estabilidad',r'¿Para qué valores de \(A\) se cumple \(A^t\to0\)?',
 r'''\[ y_t\to y^*\iff A^t\to0\iff |A|\lt 1 \]
<p>Con \(|A|\gt 1\) el desvío crece sin límite. Con \(|A|=1\) no converge: \(A=1\) es lineal y \(A=-1\) oscila con amplitud constante.</p>'''),
(r'Forma de la trayectoria',r'¿Qué cambia si \(A\) es negativo?',
 r'''<p>El <b>signo</b> de \(A\) decide si hay oscilación: si \(A\lt 0\), \(A^t\) cambia de signo en cada período y la trayectoria salta de un lado al otro de \(y^*\).</p>
<table class="dtab"><tr><td>\(A\gt 1\)</td><td>monótona explosiva</td></tr><tr><td>\(0\lt A\lt 1\)</td><td>monótona convergente</td></tr><tr><td>\(-1\lt A\lt 0\)</td><td>oscilación amortiguada</td></tr><tr><td>\(A=-1\)</td><td>oscilación uniforme</td></tr><tr><td>\(A\lt -1\)</td><td>oscilación explosiva</td></tr></table>'''),
])

DERIV['02_interes_y_rentas.html']=(r'Las tres aplicaciones financieras son casos de \(y_{t+1}=A\,y_t+B\) con \(A=1+i\).',[
(r'Interés compuesto e interés simple',r'',
 r'''<p>Con interés compuesto, el capital de cada período genera interés sobre sí mismo:</p>
\[ C_{t+1}=(1+i)\,C_t\quad\Rightarrow\quad A=1+i,\;B=0\quad\Rightarrow\quad C_t=C_0(1+i)^t \]
<p>Con interés simple, el interés se calcula siempre sobre \(C_0\):</p>
\[ C_{t+1}=C_t+i\,C_0\quad\Rightarrow\quad A=1,\;B=iC_0\quad\Rightarrow\quad C_t=C_0(1+i\,t) \]'''),
(r'Valor final de una renta',r'Si depositás \(c\) al final de cada período, ¿cómo pasa el saldo de \(S_t\) a \(S_{t+1}\)?',
 r'''<p>El saldo genera intereses y se suma el nuevo depósito. Partimos de \(S_0=0\):</p>
\[ S_{t+1}=\underbrace{(1+i)\,S_t}_{\text{capital e intereses}}+\underbrace{c}_{\text{depósito}}\qquad A=1+i,\;B=c \]'''),
(r'Equilibrio y solución del ahorro',r'Usá \(y^*=B/(1-A)\) y la solución general de la ecuación canónica.',
 r'''\[ S^*=\frac{c}{1-(1+i)}=-\frac{c}{i} \]
\[ S_t=\left(S_0-S^*\right)(1+i)^t+S^*=\frac{c}{i}(1+i)^t-\frac{c}{i}=\boxed{\frac{c}{i}\Big[(1+i)^t-1\Big]} \]'''),
(r'Saldo de un préstamo',r'Ahora la cuota \(c\) reduce la deuda. ¿Qué cambia en la ecuación?',
 r'''<p>La deuda genera intereses y se descuenta la cuota:</p>
\[ V_{t+1}=(1+i)\,V_t-c\qquad A=1+i,\;B=-c,\qquad V^*=\frac{-c}{1-(1+i)}=\frac{c}{i} \]
\[ V_t=\left(V_0-\frac{c}{i}\right)(1+i)^t+\frac{c}{i} \]'''),
(r'Valor actual: la deuda se cancela en \(n\) cuotas',r'Imponé \(V_n=0\) y despejá \(V_0\).',
 r'''\[ 0=\left(V_0-\frac{c}{i}\right)(1+i)^n+\frac{c}{i}\quad\Rightarrow\quad V_0=\frac{c}{i}-\frac{c}{i}(1+i)^{-n} \]
\[ \boxed{V_0=c\,\frac{1-(1+i)^{-n}}{i}} \]
<p>El valor actual es la suma de las cuotas descontadas a la tasa \(i\).</p>'''),
(r'Estabilidad',r'¿Cómo es \(A=1+i\) comparado con 1?',
 r'''<p>Como \(A=1+i\gt 1\), el equilibrio es <b>inestable</b>: el saldo se aleja de \(y^*\) en forma monótona.</p>
<p>En el préstamo, si \(V_0\lt c/i\) la cuota cubre los intereses y algo de capital, y la deuda baja hasta cancelarse. Si \(V_0\gt c/i\) la cuota ni siquiera paga los intereses y la deuda crece.</p>'''),
])

DERIV['00_telarana.html']=(r'Del equilibrio de mercado con oferta retrasada a la trayectoria del precio.',[
(r'Planteo',r'',
 r'''<p>La producción tarda un período: se decide con el precio de ayer.</p>
\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P_{t-1},\qquad Q^d_t=Q^s_t \]
<p>con \(\alpha,\beta,\gamma,\delta\gt 0\).</p>'''),
(r'Igualar oferta y demanda',r'Reemplazá las dos funciones en \(Q^d_t=Q^s_t\).',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P_{t-1}\quad\Longrightarrow\quad \beta P_t+\delta P_{t-1}=\alpha+\gamma \]'''),
(r'Forma canónica',r'Adelantá un período y dividí por \(\beta\).',
 r'''\[ P_{t+1}=-\frac{\delta}{\beta}\,P_t+\frac{\alpha+\gamma}{\beta}\qquad A=-\frac{\delta}{\beta},\quad B=\frac{\alpha+\gamma}{\beta} \]'''),
(r'Precio de equilibrio',r'Aplicá \(P^*=B/(1-A)\).',
 r'''\[ P^*=\frac{(\alpha+\gamma)/\beta}{1+\delta/\beta}=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>Es el precio que iguala oferta y demanda cuando \(P_t=P_{t-1}\).</p>'''),
(r'Trayectoria del precio',r'',
 r'''\[ P_t=\left(P_0-P^*\right)\left(-\frac{\delta}{\beta}\right)^t+P^* \]'''),
(r'Estabilidad',r'¿Cuándo \(\left|-\delta/\beta\right|\lt 1\)?',
 r'''<p>Como \(A=-\delta/\beta\lt 0\), la trayectoria <b>siempre oscila</b>. Su amplitud depende del cociente de pendientes:</p>
<table class="dtab"><tr><td>\(\delta\lt\beta\)</td><td>oscilación amortiguada (converge)</td></tr><tr><td>\(\delta=\beta\)</td><td>oscilación uniforme</td></tr><tr><td>\(\delta\gt\beta\)</td><td>oscilación explosiva</td></tr></table>
<p>Converge si la oferta es menos sensible al precio que la demanda.</p>'''),
])

DERIV['03_expectativas_adaptativas.html']=(r'La oferta depende de un precio esperado que se corrige por una fracción del error.',[
(r'Planteo',r'',
 r'''\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P^e_t,\qquad Q^d_t=Q^s_t \]
\[ P^e_t=P^e_{t-1}+\eta\left(P_{t-1}-P^e_{t-1}\right),\qquad 0\lt\eta\le1 \]
<p>Con \(\eta=1\) queda \(P^e_t=P_{t-1}\): la telaraña estándar.</p>'''),
(r'Despejar la expectativa',r'Usá el equilibrio de mercado para escribir \(P^e_t\) en función de \(P_t\).',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P^e_t\quad\Longrightarrow\quad P^e_t=\frac{\alpha+\gamma-\beta P_t}{\delta} \]
<p>Lo mismo vale un período después: \(P^e_{t+1}=(\alpha+\gamma-\beta P_{t+1})/\delta\).</p>'''),
(r'Sustituir en la regla adaptativa',r'Escribí la regla para \(t+1\) y reemplazá las dos expectativas.',
 r'''<p>La regla adelantada es \(P^e_{t+1}=(1-\eta)P^e_t+\eta P_t\). Reemplazando y multiplicando por \(\delta\):</p>
\[ \alpha+\gamma-\beta P_{t+1}=(1-\eta)\left(\alpha+\gamma-\beta P_t\right)+\eta\,\delta P_t \]'''),
(r'Forma canónica',r'Despejá \(P_{t+1}\) y dividí por \(\beta\).',
 r'''\[ \beta P_{t+1}=\left[(1-\eta)\beta-\eta\delta\right]P_t+\eta(\alpha+\gamma) \]
\[ P_{t+1}=\underbrace{\left[1-\eta\left(1+\frac{\delta}{\beta}\right)\right]}_{A}P_t+\underbrace{\frac{\eta(\alpha+\gamma)}{\beta}}_{B} \]'''),
(r'Equilibrio y solución',r'¿Cambia el equilibrio respecto de la telaraña?',
 r'''\[ P^*=\frac{B}{1-A}=\frac{\eta(\alpha+\gamma)/\beta}{\eta\,(1+\delta/\beta)}=\frac{\alpha+\gamma}{\beta+\delta} \]
\[ P_t=\left(P_0-P^*\right)A^t+P^* \]
<p>El equilibrio es el mismo: \(\eta\) sólo cambia la dinámica.</p>'''),
(r'Estabilidad',r'Escribí \(-1\lt A\lt 1\) y fijate cuál de las dos desigualdades restringe.',
 r'''<p>La desigualdad \(A\lt 1\) vale siempre porque \(\eta(1+\delta/\beta)\gt 0\). La otra es la que restringe:</p>
\[ 1-\eta\left(1+\frac{\delta}{\beta}\right)\gt -1\iff\frac{\delta}{\beta}\lt\frac{2-\eta}{\eta} \]
<p>Con \(\eta=1\) se recupera \(\delta\lt\beta\). Con \(\eta\lt 1\) la cota es mayor que 1: el mercado puede converger aunque \(\delta\gt\beta\).</p>'''),
(r'Forma de la trayectoria',r'¿Cuándo \(A\) es positivo?',
 r'''<p>\(A\gt 0\iff\eta(1+\delta/\beta)\lt 1\): con un ajuste lento de las expectativas, la convergencia es <b>monótona</b>. Si \(A\lt 0\), el precio oscila como en la telaraña.</p>'''),
])

DERIV['04_mercado_con_inventarios.html']=(r'El precio se ajusta según el exceso de oferta que se acumula como inventario.',[
(r'Planteo',r'',
 r'''\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P_t,\qquad P_{t+1}=P_t-\sigma\left(Q^s_t-Q^d_t\right) \]
<p>\(\sigma\gt 0\) es la velocidad de ajuste del precio.</p>'''),
(r'El exceso de oferta',r'Calculá \(Q^s_t-Q^d_t\) y escribilo en función de \(P_t-P^*\).',
 r'''\[ Q^s_t-Q^d_t=(\beta+\delta)P_t-(\alpha+\gamma)=(\beta+\delta)\left(P_t-P^*\right),\qquad P^*=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>Si \(P_t\gt P^*\) hay exceso de oferta y el precio baja; si \(P_t\lt P^*\), sube.</p>'''),
(r'Forma canónica',r'Reemplazá en la regla de ajuste y agrupá los términos en \(P_t\).',
 r'''\[ P_{t+1}=P_t-\sigma\Big[(-\gamma+\delta P_t)-(\alpha-\beta P_t)\Big]=\underbrace{\left[1-\sigma(\beta+\delta)\right]}_{A}P_t+\underbrace{\sigma(\alpha+\gamma)}_{B} \]'''),
(r'Equilibrio y solución',r'',
 r'''\[ P^*=\frac{B}{1-A}=\frac{\sigma(\alpha+\gamma)}{\sigma(\beta+\delta)}=\frac{\alpha+\gamma}{\beta+\delta},\qquad P_t=\left(P_0-P^*\right)A^t+P^* \]'''),
(r'Estabilidad',r'¿Cuál de las desigualdades de \(|A|\lt 1\) restringe a \(\sigma\)?',
 r'''<p>\(A\lt 1\) vale siempre. La restricción es</p>
\[ 1-\sigma(\beta+\delta)\gt -1\iff\sigma\lt\frac{2}{\beta+\delta} \]'''),
(r'Las tres zonas',r'Llamá \(x=\sigma(\beta+\delta)\). ¿Qué pasa con un desvío \(d\) en un período?',
 r'''<p>Un desvío \(d\) sobre \(P^*\) se corrige en \(x\,d\): queda \((1-x)\,d\).</p>
<table class="dtab"><tr><td>\(0\lt x\lt 1\)</td><td>corrige menos que \(d\): monótona convergente</td></tr><tr><td>\(x=1\)</td><td>llega a \(P^*\) en un paso</td></tr><tr><td>\(1\lt x\lt 2\)</td><td>se pasa, pero menos que \(d\): oscilación amortiguada</td></tr><tr><td>\(x=2\)</td><td>queda exactamente \(d\) del otro lado: oscilación uniforme</td></tr><tr><td>\(x\gt 2\)</td><td>sobreajuste mayor que \(d\): explosiva</td></tr></table>'''),
])

DERIV['07_triangulo_de_estabilidad.html']=(r'El método general para \(y_{t+2}+p\,y_{t+1}+q\,y_t=g\), que después se aplica a cada modelo de segundo orden.',[
(r'Planteo',r'',
 r'''\[ y_{t+2}+p\,y_{t+1}+q\,y_t=g \]
<p>con \(y_0\) e \(y_1\) dados. La solución es la suma de una solución particular y la solución de la homogénea.</p>'''),
(r'Solución particular',r'Proponé \(y_t=y^*\) constante.',
 r'''\[ y^*+p\,y^*+q\,y^*=g\quad\Longrightarrow\quad y^*=\frac{g}{1+p+q}\qquad(1+p+q\neq0) \]'''),
(r'La ecuación homogénea',r'¿Qué ecuación cumple el desvío \(z_t=y_t-y^*\)?',
 r'''<p>Restando la ecuación del equilibrio:</p>
\[ z_{t+2}+p\,z_{t+1}+q\,z_t=0 \]'''),
(r'Ecuación característica',r'Probá con \(z_t=r^t\). ¿Qué tiene que cumplir \(r\)?',
 r'''<p>Reemplazando y dividiendo por \(r^t\):</p>
\[ r^2+p\,r+q=0,\qquad r_{1,2}=\frac{-p\pm\sqrt{\Delta}}{2},\qquad \Delta=p^2-4q \]
<p>Además \(r_1+r_2=-p\) y \(r_1r_2=q\).</p>'''),
(r'Los tres casos',r'¿Cómo se escribe la solución según el signo de \(\Delta\)?',
 r'''<table class="dtab"><tr><td>\(\Delta\gt 0\)</td><td>\(z_t=C_1r_1^{\,t}+C_2r_2^{\,t}\)</td></tr><tr><td>\(\Delta=0\)</td><td>\(z_t=(C_1+C_2t)\,r^t,\;r=-p/2\)</td></tr><tr><td>\(\Delta\lt 0\)</td><td>\(z_t=\rho^t\left(C_1\cos\theta t+C_2\operatorname{sen}\theta t\right)\)</td></tr></table>
<p>En el caso complejo \(r=\rho(\cos\theta\pm i\operatorname{sen}\theta)\) con \(\rho=\sqrt q\) y \(\cos\theta=-\dfrac{p}{2\sqrt q}\).</p>'''),
(r'Constantes',r'Usá \(y_0\) e \(y_1\).',
 r'''<p>Con \(z_0=y_0-y^*\) y \(z_1=y_1-y^*\). Por ejemplo, si \(\Delta\gt 0\):</p>
\[ C_1+C_2=z_0,\qquad C_1r_1+C_2r_2=z_1 \]
<p>La solución general es \(y_t=y^*+z_t\).</p>'''),
(r'Condición de estabilidad',r'\(z_t\to0\) si y sólo si las dos raíces tienen módulo menor que 1. ¿Cómo se traduce en \(p\) y \(q\)?',
 r'''<p>Sea \(f(r)=r^2+p\,r+q\). Si las raíces son reales, están en \((-1,1)\) cuando \(f(1)\gt 0\), \(f(-1)\gt 0\) y \(r_1r_2=q\lt 1\). Si son complejas, \(|r|^2=q\lt 1\). En ambos casos:</p>
\[ 1-q\gt 0,\qquad 1+p+q\gt 0,\qquad 1-p+q\gt 0 \]
<p>Son los tres lados del triángulo en el plano \((p,q)\).</p>'''),
(r'Forma de la trayectoria',r'',
 r'''<table class="dtab"><tr><td>raíces complejas</td><td>ciclo, con período \(2\pi/\theta\)</td></tr><tr><td>raíz dominante real negativa</td><td>zigzag</td></tr><tr><td>raíz dominante real positiva</td><td>monótona</td></tr></table>
<p>La parábola \(q=p^2/4\) separa las raíces complejas (arriba) de las reales (abajo).</p>'''),
])

DERIV['05_telarana_extrapolacion.html']=(r'Los productores proyectan la última variación del precio y la ecuación pasa a ser de segundo orden.',[
(r'El sistema',r'',
 r'''\[ \begin{cases} Q^d_t=\alpha-\beta P_t\\ Q^s_t=-\gamma+\delta P^e_t\\ Q^d_t=Q^s_t\\ P^e_t=P_{t-1}+\phi\,(P_{t-1}-P_{t-2}) \end{cases} \]
<p>Cuatro ecuaciones y cuatro incógnitas. Como \(P^e_t\) depende de \(P_{t-1}\) y \(P_{t-2}\), el resultado es de segundo orden.</p>'''),
(r'Paso 1: equilibrio de mercado',r'Despejá \(P_t\) de \(Q^d_t=Q^s_t\).',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P^e_t\quad\Rightarrow\quad P_t=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}P^e_t \]'''),
(r'Paso 2: sustituir la expectativa',r'Reemplazá \(P^e_t=(1+\phi)P_{t-1}-\phi P_{t-2}\) y distribuí.',
 r'''\[ P_t=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}\Big[(1+\phi)P_{t-1}-\phi P_{t-2}\Big] \]
\[ P_t=-\frac{\delta(1+\phi)}{\beta}P_{t-1}+\frac{\delta\phi}{\beta}P_{t-2}+\frac{\alpha+\gamma}{\beta} \]'''),
(r'Forma canónica',r'Adelantá dos períodos e identificá \(p\), \(q\) y \(g\).',
 r'''\[ \boxed{P_{t+2}+\frac{\delta(1+\phi)}{\beta}P_{t+1}-\frac{\delta\phi}{\beta}P_t=\frac{\alpha+\gamma}{\beta}} \]
\[ p=\mu(1+\phi),\qquad q=-\mu\phi,\qquad g=\frac{\alpha+\gamma}{\beta},\qquad \mu=\frac{\delta}{\beta} \]
<p>Con \(\phi=0\) queda \(q=0\): la telaraña estándar de primer orden.</p>'''),
(r'Punto de equilibrio',r'Proponé \(P_t=A\) constante.',
 r'''\[ A\left[1+\frac{\delta(1+\phi)-\delta\phi}{\beta}\right]=\frac{\alpha+\gamma}{\beta} \]
\[ A\cdot\frac{\beta+\delta}{\beta}=\frac{\alpha+\gamma}{\beta}\quad\Rightarrow\quad P^*=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>La extrapolación no cambia el equilibrio, sólo la dinámica.</p>'''),
(r'Ecuación característica',r'',
 r'''\[ r^2+\mu(1+\phi)\,r-\mu\phi=0,\qquad \Delta=\mu^2(1+\phi)^2+4\mu\phi \]
<p>Si \(\phi\ge0\), \(\Delta\gt 0\): raíces reales. Sólo con \(\phi\lt 0\) puede haber raíces complejas.</p>'''),
(r'¿Cuándo hay ciclos?',r'Escribí \(\Delta\lt 0\) como una desigualdad cuadrática en \(\phi\).',
 r'''\[ \Delta\lt 0\iff\mu\phi^2+2(\mu+2)\phi+\mu\lt 0\iff\phi_2\lt\phi\lt\phi_1,\qquad \phi_{1,2}=\frac{-(\mu+2)\pm2\sqrt{1+\mu}}{\mu} \]
<p>Además \(\phi_1\phi_2=1\) y \(\phi_2\lt -1\lt\phi_1\lt 0\).</p>'''),
(r'Condiciones de estabilidad',r'Aplicá \(1-q\gt 0\), \(1+p+q\gt 0\) y \(1-p+q\gt 0\).',
 r'''\[ \begin{cases} 1+\mu\phi\gt 0\\ 1+\mu\gt 0\quad\checkmark\\ 1-\mu(1+2\phi)\gt 0 \end{cases}\quad\Longrightarrow\quad -\frac{\beta}{\delta}\lt\phi\lt\frac{\beta-\delta}{2\delta} \]
<p>La cota superior es positiva sólo si \(\beta\gt\delta\). El intervalo no es vacío si y sólo si \(\mu\lt 3\).</p>'''),
(r'Interpretación',r'',
 r'''<p>\(\phi\gt 0\): los productores extrapolan, sobreproducen y amplifican las oscilaciones. \(\phi\lt 0\): anticipan una corrección y las amortiguan, pero si \(\phi\lt-\beta/\delta\) sobrecorrigen y el ciclo vuelve a crecer.</p>'''),
])

DERIV['06_inventarios_de_metzler.html']=(r'Ingreso, ventas e inversión en inventarios: el acelerador produce una ecuación de segundo orden.',[
(r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=U_t+S_t+V_0\\ U_t=c\,Y_{t-1}\\ S_t=c(1+k)(Y_{t-1}-Y_{t-2}) \end{cases} \]
<p>\(0\lt c\lt 1\) es la propensión al consumo y \(k\gt 0\) la proporción deseada de inventario sobre ventas.</p>'''),
(r'De dónde sale \(S_t\)',r'Si las ventas suben, ¿qué tienen que hacer las empresas con su stock?',
 r'''<p>Tienen que reponer lo vendido de más (factor 1) y ampliar el stock para mantener la proporción \(k\) (factor \(k\)):</p>
\[ S_t=(1+k)(U_t-U_{t-1})=(1+k)\,c\,(Y_{t-1}-Y_{t-2}) \]'''),
(r'Reducción',r'Sustituí \(U_t\) y \(S_t\) en la primera ecuación y agrupá.',
 r'''\[ Y_t=c\,Y_{t-1}+c(1+k)(Y_{t-1}-Y_{t-2})+V_0=c(2+k)\,Y_{t-1}-c(1+k)\,Y_{t-2}+V_0 \]
\[ \boxed{Y_{t+2}-c(2+k)\,Y_{t+1}+c(1+k)\,Y_t=V_0} \]'''),
(r'Ingreso de equilibrio',r'Proponé \(Y_t=A\) constante.',
 r'''\[ A\left[1-2c-ck+c+ck\right]=V_0\quad\Rightarrow\quad A(1-c)=V_0\quad\Rightarrow\quad Y^*=\frac{V_0}{1-c} \]
<p>\(k\) desaparece: es el multiplicador keynesiano.</p>'''),
(r'Ecuación característica y discriminante',r'',
 r'''\[ r^2-c(2+k)\,r+c(1+k)=0,\qquad\Delta=c\left[c(2+k)^2-4(1+k)\right] \]
\[ \Delta\lt 0\iff c\lt\frac{4(1+k)}{(2+k)^2} \]
<p>Si las raíces son reales, son positivas (suma y producto positivos): nunca hay zigzag.</p>'''),
(r'Condición de estabilidad',r'Con \(p=-c(2+k)\) y \(q=c(1+k)\), ¿cuál de las tres condiciones puede fallar?',
 r'''\[ \begin{cases} 1-c(1+k)\gt 0\\ 1-c(2+k)+c(1+k)=1-c\gt 0\quad\checkmark\\ 1+c(2+k)+c(1+k)\gt 0\quad\checkmark \end{cases}\quad\Longrightarrow\quad c(1+k)\lt 1 \]'''),
(r'Las cuatro regiones',r'',
 r'''<table class="dtab"><tr><td>\(c\lt\frac{1}{1+k}\)</td><td>oscilante y convergente</td></tr><tr><td>\(c=\frac{1}{1+k}\)</td><td>oscilante de amplitud constante</td></tr><tr><td>\(\frac{1}{1+k}\lt c\lt\frac{4(1+k)}{(2+k)^2}\)</td><td>oscilante y divergente</td></tr><tr><td>\(c\ge\frac{4(1+k)}{(2+k)^2}\)</td><td>monótono y divergente</td></tr></table>
<p>Como \(\frac{1}{1+k}\lt\frac{4(1+k)}{(2+k)^2}\) para todo \(k\gt 0\), la estabilidad sólo puede tomar forma de oscilaciones amortiguadas.</p>'''),
])

DERIV['08_samuelson.html']=(r'Multiplicador y acelerador juntos dan una ecuación de segundo orden con ciclos endógenos.',[
(r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=C_t+I_t+G_0\\ C_t=\gamma\,Y_{t-1}\\ I_t=\alpha\,(C_t-C_{t-1}) \end{cases}\qquad 0\lt\gamma\lt 1,\;\alpha\gt 0 \]'''),
(r'La inversión en función del ingreso',r'Reemplazá \(C_t\) y \(C_{t-1}\) en \(I_t\).',
 r'''\[ I_t=\alpha(\gamma Y_{t-1}-\gamma Y_{t-2})=\alpha\gamma\,(Y_{t-1}-Y_{t-2}) \]'''),
(r'Reducción',r'Sustituí \(C_t\) e \(I_t\) en la primera ecuación.',
 r'''\[ Y_t=\gamma Y_{t-1}+\alpha\gamma(Y_{t-1}-Y_{t-2})+G_0\quad\Rightarrow\quad Y_t-\gamma(1+\alpha)Y_{t-1}+\alpha\gamma Y_{t-2}=G_0 \]
\[ \boxed{Y_{t+2}-\gamma(1+\alpha)Y_{t+1}+\alpha\gamma\,Y_t=G_0} \]
<p>\(p=-\gamma(1+\alpha)\), \(q=\alpha\gamma\), \(g=G_0\).</p>'''),
(r'Ingreso de equilibrio',r'Proponé \(Y_t=A\).',
 r'''\[ A\left[1-\gamma(1+\alpha)+\alpha\gamma\right]=G_0\quad\Rightarrow\quad A(1-\gamma)=G_0\quad\Rightarrow\quad Y^*=\frac{G_0}{1-\gamma} \]
<p>Es el multiplicador keynesiano: la inversión inducida no cambia el nivel de equilibrio.</p>'''),
(r'Raíces y discriminante',r'',
 r'''\[ r^2-\gamma(1+\alpha)\,r+\alpha\gamma=0,\qquad\Delta=\gamma^2(1+\alpha)^2-4\alpha\gamma \]
\[ \Delta\lt 0\iff\gamma\lt\frac{4\alpha}{(1+\alpha)^2} \]
<p>Si son reales, las raíces son positivas (suma y producto positivos): no hay zigzag.</p>'''),
(r'Condición de estabilidad',r'¿Qué condición de Schur queda activa?',
 r'''\[ \begin{cases} 1-\alpha\gamma\gt 0\\ 1-\gamma(1+\alpha)+\alpha\gamma=1-\gamma\gt 0\quad\checkmark\\ 1+\gamma(1+\alpha)+\alpha\gamma=1+\gamma+2\alpha\gamma\gt 0\quad\checkmark \end{cases}\quad\Longrightarrow\quad\alpha\gamma\lt 1 \]'''),
(r'Interpretación',r'',
 r'''<p>Con raíces complejas, \(|r|=\sqrt{\alpha\gamma}\): el ciclo se amortigua si \(\alpha\gamma\lt 1\) y explota si \(\alpha\gamma\gt 1\). Un acelerador alto respecto de la propensión al consumo genera ciclos sin necesidad de shocks externos.</p>'''),
])

DERIV['09_hicks.html']=(r'Samuelson con inversión autónoma creciente: la solución particular deja de ser constante.',[
(r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=C_t+I'_t+I''_t\\ C_t=\gamma\,Y_{t-1}\\ I'_t=\alpha\,(Y_{t-1}-Y_{t-2})\\ I''_t=I_0(1+g)^t \end{cases} \]'''),
(r'Reducción',r'Sustituí todo en la primera ecuación.',
 r'''\[ Y_t=\gamma Y_{t-1}+\alpha(Y_{t-1}-Y_{t-2})+I_0(1+g)^t \]
\[ \boxed{Y_{t+2}-(\gamma+\alpha)Y_{t+1}+\alpha\,Y_t=I_0(1+g)^{t+2}} \]
<p>\(p=-(\gamma+\alpha)\), \(q=\alpha\). El término independiente ya no es constante.</p>'''),
(r'Solución particular',r'Como el término independiente es \((1+g)^t\), proponé \(Y^p_t=A(1+g)^t\).',
 r'''\[ A(1+g)^{t+2}-(\gamma+\alpha)A(1+g)^{t+1}+\alpha A(1+g)^t=I_0(1+g)^{t+2} \]
<p>Dividiendo por \((1+g)^t\):</p>
\[ \boxed{A=\frac{I_0(1+g)^2}{(1+g)^2-(\gamma+\alpha)(1+g)+\alpha}} \]
<p>El ingreso de equilibrio crece a la tasa \(g\).</p>'''),
(r'Ecuación característica',r'',
 r'''\[ r^2-(\gamma+\alpha)\,r+\alpha=0,\qquad\Delta=(\gamma+\alpha)^2-4\alpha \]
\[ \Delta\lt 0\iff\gamma\lt 2\sqrt\alpha-\alpha \]'''),
(r'Condición de estabilidad',r'',
 r'''\[ \begin{cases} 1-\alpha\gt 0\\ 1-(\gamma+\alpha)+\alpha=1-\gamma\gt 0\quad\checkmark\\ 1+(\gamma+\alpha)+\alpha=1+\gamma+2\alpha\gt 0\quad\checkmark \end{cases}\quad\Longrightarrow\quad\alpha\lt 1 \]'''),
(r'Solución general',r'',
 r'''\[ Y_t=A(1+g)^t+z_t \]
<p>donde \(z_t\) es la solución de la homogénea. Si \(\alpha\lt 1\), \(z_t\to0\) y el ingreso converge a la tendencia. Si \(\alpha\ge1\), las oscilaciones no se amortiguan: Hicks las acota con un techo (pleno empleo) y un piso (inversión autónoma).</p>'''),
])

DERIV['10_inflacion_desempleo.html']=(r'Curva de Phillips con expectativas, expectativas adaptativas y política monetaria (Chiang, §18.3).',[
(r'El sistema',r'',
 r'''\[ \begin{cases} p_t=\alpha-T-\beta U_t+g\,\pi_t & (18.18)\\ \pi_{t+1}-\pi_t=j\,(p_t-\pi_t) & (18.19)\\ U_{t+1}-U_t=-k\,(m-p_{t+1}) & (18.20) \end{cases} \]
<p>Tres variables endógenas: \(p_t\), \(\pi_t\) y \(U_t\). El parámetro de política es \(m\).</p>'''),
(r'Diferenciar la curva de Phillips',r'Adelantá (18.18) un período y restá. Después usá (18.19) y (18.20).',
 r'''\[ \begin{aligned} p_{t+1}-p_t&=-\beta(U_{t+1}-U_t)+g(\pi_{t+1}-\pi_t)\\ &=\beta k(m-p_{t+1})+gj(p_t-\pi_t)\qquad(18.21) \end{aligned} \]'''),
(r'Eliminar \(\pi_t\)',r'De (18.18), \(g\pi_t=p_t-(\alpha-T)+\beta U_t\).',
 r'''\[ \begin{aligned} (1+\beta k)\,p_{t+1}-\left[1-j(1-g)\right]p_t+j\beta U_t\\ =\beta k m+j(\alpha-T)\qquad(18.23) \end{aligned} \]'''),
(r'Eliminar \(U_t\)',r'Adelantá (18.23), restale (18.23) y usá (18.20) para \(U_{t+1}-U_t\).',
 r'''\[ \begin{aligned} (1+\beta k)(p_{t+2}-p_{t+1})-\left[1-j(1-g)\right](p_{t+1}-p_t)\\ +\,j\beta k(p_{t+1}-m)=0 \end{aligned} \]
<p>Agrupando y dividiendo por \(1+\beta k\):</p>
\[ \boxed{p_{t+2}-a_1\,p_{t+1}+a_2\,p_t=\frac{j\beta k\,m}{1+\beta k}} \]
\[ a_1=\frac{1+gj+(1-j)(1+\beta k)}{1+\beta k},\quad a_2=\frac{1-j(1-g)}{1+\beta k} \]'''),
(r'Inflación de equilibrio',r'Proponé \(p_t=\bar p\) constante.',
 r'''\[ \bar p=\frac{j\beta k m/(1+\beta k)}{1-a_1+a_2} \]
\[ 1-a_1+a_2=\frac{\beta jk}{1+\beta k}\quad\Longrightarrow\quad\bar p=m \]
<p>En el largo plazo la inflación iguala la tasa de expansión monetaria.</p>'''),
(r'La convergencia está garantizada',r'Mirá la suma, el producto y \((1-r_1)(1-r_2)\).',
 r'''\[ r_1+r_2=a_1\gt 0,\qquad r_1r_2=a_2\in(0,1) \]
\[ (1-r_1)(1-r_2)=1-a_1+a_2=\frac{\beta jk}{1+\beta k}\gt 0 \]
<p>Si las raíces son reales, sólo es posible \(0\lt r_2\lt r_1\lt 1\). Si son complejas, \(\rho=\sqrt{a_2}\lt 1\). En los dos casos \(p_t\to m\).</p>'''),
(r'Curva de Phillips de largo plazo',r'Con \(\pi=p=\bar p\) en (18.18), despejá \(\bar U\).',
 r'''\[ \bar U=\frac{1}{\beta}\Big[\alpha-T-(1-g)\,\bar p\Big] \]
<p>Si \(g\lt 1\), la curva tiene pendiente \(-(1-g)/\beta\lt 0\): hay un trade-off permanente. Si \(g=1\), \(\bar U=(\alpha-T)/\beta\) no depende de \(\bar p\): la curva es vertical (tasa natural de desempleo).</p>'''),
])
