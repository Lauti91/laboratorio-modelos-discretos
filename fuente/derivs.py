# Derivaciones milimétricas: fn -> (introducción, [(etapa, título, consigna, cuerpo HTML con TeX)])
# Cada paso es una sola operación algebraica, con su justificación.
DERIV={}

# ======================================================================= MD-01
DERIV['01_ecuacion_canonica.html']=(r'De \(y_{t+1}=A\,y_t+B\) a la solución explícita, sin saltear ninguna operación.',[
('Planteo',r'La ecuación y el objetivo',r'',
 r'''<p>Ecuación lineal de primer orden con coeficientes constantes \(A\) y \(B\), y un valor inicial \(y_0\) conocido:</p>
\[ y_{t+1}=A\,y_t+B,\qquad t=0,1,2,\dots \]
<p>Objetivo: una fórmula para \(y_t\) que dependa sólo de \(t\), \(A\), \(B\) e \(y_0\).</p>'''),
('Iteración',r'Primer período',r'Reemplazá \(t=0\) en la ecuación.',
 r'''\[ y_1=A\,y_0+B \]'''),
('Iteración',r'Segundo período',r'Escribí \(y_2\) y reemplazá \(y_1\) por lo que obtuviste.',
 r'''\[ y_2=A\,y_1+B=A\,(A\,y_0+B)+B \]
<p>Distribuimos \(A\):</p>
\[ y_2=A^2y_0+AB+B \]'''),
('Iteración',r'Tercer período',r'Repetí con \(y_3\).',
 r'''\[ y_3=A\,y_2+B=A\left(A^2y_0+AB+B\right)+B=A^3y_0+A^2B+AB+B \]'''),
('Iteración',r'El patrón general',r'¿Qué potencia acompaña a \(y_0\)? ¿Qué potencias de \(A\) multiplican a \(B\)?',
 r'''<p>\(y_0\) queda multiplicado por \(A^t\), y \(B\) por la suma de las potencias de \(A\) desde \(0\) hasta \(t-1\):</p>
\[ y_t=A^t\,y_0+B\left(1+A+A^2+\dots+A^{t-1}\right)=A^t\,y_0+B\sum_{k=0}^{t-1}A^k \]
<p>Se prueba por inducción: si vale para \(t\), entonces \(y_{t+1}=A\,y_t+B=A^{t+1}y_0+B\left(A+\dots+A^{t}\right)+B\), que es la misma fórmula para \(t+1\).</p>'''),
('Suma geométrica',r'Nombrar la suma',r'',
 r'''\[ S=1+A+A^2+\dots+A^{t-1} \]'''),
('Suma geométrica',r'Multiplicar por \(A\)',r'¿Qué queda si multiplicás toda la suma por \(A\)?',
 r'''\[ A\,S=A+A^2+\dots+A^{t-1}+A^t \]
<p>Cada término se corre una posición.</p>'''),
('Suma geométrica',r'Restar las dos sumas',r'Calculá \(S-A\,S\). ¿Qué términos se cancelan?',
 r'''<p>Se cancelan todos menos el primero de \(S\) y el último de \(A\,S\):</p>
\[ S-A\,S=1-A^t\quad\Longrightarrow\quad S\,(1-A)=1-A^t \]'''),
('Suma geométrica',r'Despejar \(S\)',r'¿Qué condición necesitás para dividir?',
 r'''<p>Si \(A\neq1\), podemos dividir por \(1-A\):</p>
\[ S=\frac{1-A^t}{1-A} \]'''),
('Suma geométrica',r'Volver a la solución',r'Reemplazá \(S\) en el patrón del paso 5.',
 r'''\[ y_t=A^t\,y_0+B\,\frac{1-A^t}{1-A} \]'''),
('Equilibrio',r'Definición de equilibrio',r'¿Qué significa que \(y\) esté en equilibrio?',
 r'''<p>Un equilibrio es un valor \(y^*\) que, una vez alcanzado, se repite: \(y_{t+1}=y_t=y^*\). Lo reemplazamos en la ecuación:</p>
\[ y^*=A\,y^*+B \]'''),
('Equilibrio',r'Despejar \(y^*\)',r'Pasá \(A\,y^*\) al otro miembro y sacá factor común.',
 r'''\[ y^*-A\,y^*=B\quad\Longrightarrow\quad y^*(1-A)=B\quad\Longrightarrow\quad y^*=\frac{B}{1-A}\qquad(A\neq1) \]'''),
('Solución general',r'Distribuir \(B\)',r'Volvé al paso 10 y separá la fracción en dos términos.',
 r'''\[ y_t=A^t\,y_0+\frac{B}{1-A}-A^t\,\frac{B}{1-A} \]'''),
('Solución general',r'Reconocer \(y^*\)',r'¿Dónde aparece \(\frac{B}{1-A}\)?',
 r'''<p>Reemplazamos \(\frac{B}{1-A}=y^*\) en los dos lugares:</p>
\[ y_t=A^t\,y_0+y^*-A^t\,y^* \]'''),
('Solución general',r'Factor común \(A^t\)',r'',
 r'''\[ \boxed{y_t=\left(y_0-y^*\right)A^t+y^*} \]
<p>Verificación: en \(t=0\), \(A^0=1\) y queda \(y_0\).</p>'''),
('Solución general',r'El desvío respecto del equilibrio',r'Definí \(z_t=y_t-y^*\). ¿Qué ecuación cumple?',
 r'''\[ z_{t+1}=y_{t+1}-y^*=(A\,y_t+B)-(A\,y^*+B)=A\,(y_t-y^*)=A\,z_t \]
<p>Entonces \(z_t=z_0\,A^t\): toda la dinámica la decide \(A\).</p>'''),
('Caso A = 1',r'Cuando \(A=1\)',r'Si \(A=1\), ¿cuánto vale la suma \(S\)?',
 r'''<p>Los \(t\) términos valen 1, así que \(S=t\) y</p>
\[ y_t=y_0+B\,t \]
<p>No hay equilibrio si \(B\neq0\): \(y^*(1-1)=B\) no tiene solución. La trayectoria es una recta.</p>'''),
('Estabilidad',r'Qué hay que pedir',r'¿Cuándo \(y_t\to y^*\)?',
 r'''\[ y_t-y^*=\left(y_0-y^*\right)A^t\;\to\;0\iff A^t\to0\qquad(\text{si }y_0\neq y^*) \]'''),
('Estabilidad',r'La condición',r'Usá que \(|A^t|=|A|^t\).',
 r'''\[ |A|^t\to0\iff|A|\lt 1 \]
<p>Si \(|A|\gt 1\), \(|A|^t\to\infty\) y el desvío crece sin límite. Si \(|A|=1\), el desvío no se achica.</p>'''),
('Forma de la trayectoria',r'El signo de \(A\)',r'¿Qué signo tiene \(A^t\) si \(A\lt 0\)?',
 r'''<p>Si \(A\gt 0\), \(A^t\gt 0\) siempre: el desvío conserva el signo y la trayectoria es monótona. Si \(A\lt 0\), \(A^t=(-1)^t|A|^t\) cambia de signo cada período: la trayectoria oscila alrededor de \(y^*\).</p>
<table class="dtab"><tr><td>\(A\gt 1\)</td><td>monótona explosiva</td></tr><tr><td>\(0\lt A\lt 1\)</td><td>monótona convergente</td></tr><tr><td>\(A=0\)</td><td>llega a \(y^*\) en un paso</td></tr><tr><td>\(-1\lt A\lt 0\)</td><td>oscilación amortiguada</td></tr><tr><td>\(A=-1\)</td><td>oscilación uniforme</td></tr><tr><td>\(A\lt -1\)</td><td>oscilación explosiva</td></tr></table>'''),
])

# ======================================================================= MD-02
DERIV['02_interes_y_rentas.html']=(r'Las aplicaciones financieras como casos de \(y_{t+1}=A\,y_t+B\), con todas las cuentas.',[
('Interés compuesto',r'La ecuación del capital',r'¿Cuánto interés gana el capital \(C_t\) en un período?',
 r'''<p>El interés del período es \(i\,C_t\), y se suma al capital:</p>
\[ C_{t+1}=C_t+i\,C_t=(1+i)\,C_t \]'''),
('Interés compuesto',r'Forma canónica',r'Identificá \(A\) y \(B\).',
 r'''\[ A=1+i,\qquad B=0 \]'''),
('Interés compuesto',r'Equilibrio y solución',r'Aplicá \(y^*=B/(1-A)\) y \(y_t=(y_0-y^*)A^t+y^*\).',
 r'''\[ C^*=\frac{0}{1-(1+i)}=0\qquad\Longrightarrow\qquad C_t=(C_0-0)(1+i)^t=C_0(1+i)^t \]'''),
('Interés simple',r'La ecuación del capital',r'Con interés simple, ¿sobre qué capital se calcula el interés?',
 r'''<p>Siempre sobre el capital inicial \(C_0\):</p>
\[ C_{t+1}=C_t+i\,C_0\qquad A=1,\quad B=i\,C_0 \]'''),
('Interés simple',r'Solución con \(A=1\)',r'Usá el caso \(A=1\) de la ecuación canónica.',
 r'''\[ C_t=C_0+B\,t=C_0+i\,C_0\,t=C_0(1+i\,t) \]'''),
('Interés simple',r'Comparación',r'Desarrollá \((1+i)^t\) con el binomio.',
 r'''\[ (1+i)^t=1+t\,i+\frac{t(t-1)}{2}\,i^2+\dots\;\ge\;1+i\,t \]
<p>El compuesto supera al simple desde \(t=2\): la diferencia son los intereses sobre intereses.</p>'''),
('Valor final',r'La ecuación del ahorro',r'Depositás \(c\) al final de cada período. ¿Cómo pasa el saldo de \(S_t\) a \(S_{t+1}\)?',
 r'''<p>El saldo gana intereses y se suma el nuevo depósito. Partimos de \(S_0=0\):</p>
\[ S_{t+1}=S_t+i\,S_t+c=(1+i)\,S_t+c\qquad A=1+i,\quad B=c \]'''),
('Valor final',r'Equilibrio',r'',
 r'''\[ S^*=\frac{B}{1-A}=\frac{c}{1-(1+i)}=\frac{c}{-i}=-\frac{c}{i} \]
<p>Es un valor negativo: no tiene sentido económico, pero sirve para escribir la solución.</p>'''),
('Valor final',r'Solución general',r'Reemplazá \(S_0=0\) y \(S^*\).',
 r'''\[ S_t=\left(S_0-S^*\right)(1+i)^t+S^*=\left(0+\frac{c}{i}\right)(1+i)^t-\frac{c}{i} \]'''),
('Valor final',r'Factor común',r'',
 r'''\[ \boxed{S_t=\frac{c}{i}\Big[(1+i)^t-1\Big]} \]'''),
('Valor final',r'Verificación',r'Calculá \(S_1\) y \(S_2\) con la fórmula y con la recursión.',
 r'''\[ S_1=\frac{c}{i}\,i=c,\qquad S_2=\frac{c}{i}\left(2i+i^2\right)=c\,(2+i)=(1+i)\,c+c\;\checkmark \]'''),
('Préstamo',r'La ecuación de la deuda',r'Ahora la cuota \(c\) reduce la deuda \(V_t\). ¿Qué cambia?',
 r'''<p>La deuda genera intereses y se descuenta la cuota:</p>
\[ V_{t+1}=V_t+i\,V_t-c=(1+i)\,V_t-c\qquad A=1+i,\quad B=-c \]'''),
('Préstamo',r'Equilibrio',r'',
 r'''\[ V^*=\frac{-c}{1-(1+i)}=\frac{-c}{-i}=\frac{c}{i} \]
<p>Con una deuda de \(c/i\), la cuota paga exactamente los intereses y la deuda no cambia.</p>'''),
('Préstamo',r'Solución general',r'',
 r'''\[ V_t=\left(V_0-\frac{c}{i}\right)(1+i)^t+\frac{c}{i} \]'''),
('Valor actual',r'Condición de cancelación',r'La deuda se cancela con la cuota \(n\). ¿Qué ecuación plantea eso?',
 r'''\[ V_n=0\quad\Longrightarrow\quad 0=\left(V_0-\frac{c}{i}\right)(1+i)^n+\frac{c}{i} \]'''),
('Valor actual',r'Aislar el paréntesis',r'Pasá \(c/i\) al otro miembro y dividí por \((1+i)^n\).',
 r'''\[ \left(V_0-\frac{c}{i}\right)(1+i)^n=-\frac{c}{i}\quad\Longrightarrow\quad V_0-\frac{c}{i}=-\frac{c}{i}\,(1+i)^{-n} \]'''),
('Valor actual',r'Despejar \(V_0\)',r'',
 r'''\[ V_0=\frac{c}{i}-\frac{c}{i}(1+i)^{-n}=\boxed{c\,\frac{1-(1+i)^{-n}}{i}} \]'''),
('Valor actual',r'Interpretación como suma de cuotas descontadas',r'¿Cuánto vale hoy la cuota que se paga en \(t\)?',
 r'''<p>Cada cuota vale hoy \(c(1+i)^{-t}\). Sumando las \(n\) cuotas (suma geométrica de razón \((1+i)^{-1}\)):</p>
\[ \sum_{t=1}^{n}c\,(1+i)^{-t}=c\,(1+i)^{-1}\,\frac{1-(1+i)^{-n}}{1-(1+i)^{-1}}=c\,\frac{1-(1+i)^{-n}}{i}\;\checkmark \]'''),
('Estabilidad',r'Un equilibrio inestable',r'¿Cómo es \(A=1+i\) comparado con 1?',
 r'''<p>\(A=1+i\gt 1\): el equilibrio es inestable y la trayectoria es monótona.</p>
<p>En el préstamo: si \(V_0\lt c/i\), el paréntesis es negativo y la deuda baja hasta cancelarse. Si \(V_0\gt c/i\), la cuota no alcanza a pagar los intereses y la deuda crece.</p>'''),
])

# ======================================================================= MD-03 telaraña
DERIV['00_telarana.html']=(r'Del equilibrio de mercado con oferta retrasada a la trayectoria del precio, operación por operación.',[
('Planteo',r'Supuestos',r'',
 r'''\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P_{t-1},\qquad Q^d_t=Q^s_t \]
<p>con \(\alpha,\beta,\gamma,\delta\gt 0\). La oferta de hoy se decidió con el precio de ayer.</p>'''),
('Reducción',r'Igualar oferta y demanda',r'Reemplazá las dos funciones en la condición de equilibrio.',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P_{t-1} \]'''),
('Reducción',r'Agrupar',r'Sumá \(\beta P_t\) y \(\gamma\) a ambos miembros.',
 r'''\[ \alpha+\gamma=\beta P_t+\delta P_{t-1} \]'''),
('Reducción',r'Despejar \(P_t\)',r'Pasá \(\delta P_{t-1}\) restando y dividí por \(\beta\).',
 r'''\[ \beta P_t=\alpha+\gamma-\delta P_{t-1}\quad\Longrightarrow\quad P_t=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}P_{t-1} \]'''),
('Reducción',r'Adelantar un período',r'Reemplazá \(t\) por \(t+1\).',
 r'''\[ P_{t+1}=-\frac{\delta}{\beta}\,P_t+\frac{\alpha+\gamma}{\beta} \]'''),
('Reducción',r'Forma canónica',r'',
 r'''\[ A=-\frac{\delta}{\beta},\qquad B=\frac{\alpha+\gamma}{\beta} \]'''),
('Equilibrio',r'Aplicar la fórmula',r'',
 r'''\[ P^*=\frac{B}{1-A}=\frac{(\alpha+\gamma)/\beta}{1+\delta/\beta} \]'''),
('Equilibrio',r'Simplificar',r'Escribí \(1+\delta/\beta\) con denominador común.',
 r'''\[ 1+\frac{\delta}{\beta}=\frac{\beta+\delta}{\beta}\quad\Longrightarrow\quad P^*=\frac{\alpha+\gamma}{\beta}\cdot\frac{\beta}{\beta+\delta}=\frac{\alpha+\gamma}{\beta+\delta} \]'''),
('Equilibrio',r'Verificación',r'Evaluá oferta y demanda en \(P^*\).',
 r'''\[ Q^d=\alpha-\beta\,\frac{\alpha+\gamma}{\beta+\delta}=\frac{\alpha\delta-\beta\gamma}{\beta+\delta},\qquad Q^s=-\gamma+\delta\,\frac{\alpha+\gamma}{\beta+\delta}=\frac{\alpha\delta-\beta\gamma}{\beta+\delta}\;\checkmark \]
<p>Para que la cantidad de equilibrio sea positiva hace falta \(\alpha\delta\gt\beta\gamma\).</p>'''),
('Solución',r'Trayectoria del precio',r'Reemplazá en \(y_t=(y_0-y^*)A^t+y^*\).',
 r'''\[ P_t=\left(P_0-P^*\right)\left(-\frac{\delta}{\beta}\right)^t+P^* \]'''),
('Estabilidad',r'El signo de \(A\)',r'',
 r'''<p>\(A=-\delta/\beta\lt 0\) siempre, porque \(\beta,\delta\gt 0\). Entonces \(\left(-\delta/\beta\right)^t\) cambia de signo cada período: el precio <b>siempre oscila</b> alrededor de \(P^*\).</p>'''),
('Estabilidad',r'El módulo de \(A\)',r'Escribí \(|A|\lt 1\) en términos de \(\delta\) y \(\beta\).',
 r'''\[ |A|=\frac{\delta}{\beta}\lt 1\iff\delta\lt\beta \]'''),
('Estabilidad',r'Los tres casos',r'',
 r'''<table class="dtab"><tr><td>\(\delta\lt\beta\)</td><td>oscilación amortiguada</td></tr><tr><td>\(\delta=\beta\)</td><td>oscilación uniforme</td></tr><tr><td>\(\delta\gt\beta\)</td><td>oscilación explosiva</td></tr></table>
<p>Converge cuando la oferta reacciona al precio menos que la demanda.</p>'''),
])

# ======================================================================= MD-04 adaptativas
DERIV['03_expectativas_adaptativas.html']=(r'La oferta depende de un precio esperado que se corrige por una fracción \(\eta\) del error.',[
('Planteo',r'El sistema',r'',
 r'''\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P^e_t,\qquad Q^d_t=Q^s_t \]
\[ P^e_t=P^e_{t-1}+\eta\left(P_{t-1}-P^e_{t-1}\right),\qquad 0\lt\eta\le1 \]'''),
('Planteo',r'Otra forma de la regla adaptativa',r'Distribuí \(\eta\) y agrupá \(P^e_{t-1}\).',
 r'''\[ P^e_t=P^e_{t-1}+\eta P_{t-1}-\eta P^e_{t-1}=\eta\,P_{t-1}+(1-\eta)\,P^e_{t-1} \]
<p>La expectativa es un promedio ponderado del último precio y de la expectativa anterior. Con \(\eta=1\) queda \(P^e_t=P_{t-1}\): la telaraña estándar.</p>'''),
('Reducción',r'Equilibrio de mercado',r'',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P^e_t \]'''),
('Reducción',r'Despejar la expectativa',r'Aislá \(\delta P^e_t\) y dividí por \(\delta\).',
 r'''\[ \delta P^e_t=\alpha+\gamma-\beta P_t\quad\Longrightarrow\quad P^e_t=\frac{\alpha+\gamma-\beta P_t}{\delta} \]'''),
('Reducción',r'La misma relación un período después',r'',
 r'''\[ P^e_{t+1}=\frac{\alpha+\gamma-\beta P_{t+1}}{\delta} \]'''),
('Reducción',r'Regla adaptativa adelantada',r'Escribí la regla del paso 2 para \(t+1\).',
 r'''\[ P^e_{t+1}=\eta\,P_t+(1-\eta)\,P^e_t \]'''),
('Reducción',r'Sustituir las dos expectativas',r'Reemplazá \(P^e_{t+1}\) y \(P^e_t\) por lo obtenido en los pasos 4 y 5.',
 r'''\[ \frac{\alpha+\gamma-\beta P_{t+1}}{\delta}=\eta\,P_t+(1-\eta)\,\frac{\alpha+\gamma-\beta P_t}{\delta} \]'''),
('Reducción',r'Multiplicar por \(\delta\)',r'',
 r'''\[ \alpha+\gamma-\beta P_{t+1}=\eta\,\delta\,P_t+(1-\eta)(\alpha+\gamma)-(1-\eta)\,\beta P_t \]'''),
('Reducción',r'Aislar \(\beta P_{t+1}\)',r'Pasá \(\beta P_{t+1}\) a un lado y todo lo demás al otro.',
 r'''\[ \beta P_{t+1}=(\alpha+\gamma)-(1-\eta)(\alpha+\gamma)+(1-\eta)\beta P_t-\eta\delta P_t \]
<p>Como \((\alpha+\gamma)-(1-\eta)(\alpha+\gamma)=\eta(\alpha+\gamma)\):</p>
\[ \beta P_{t+1}=\eta(\alpha+\gamma)+\left[(1-\eta)\beta-\eta\delta\right]P_t \]'''),
('Reducción',r'Dividir por \(\beta\)',r'',
 r'''\[ P_{t+1}=\left[1-\eta-\eta\,\frac{\delta}{\beta}\right]P_t+\frac{\eta(\alpha+\gamma)}{\beta} \]'''),
('Reducción',r'Forma canónica',r'Sacá \(\eta\) factor común en el corchete.',
 r'''\[ P_{t+1}=\underbrace{\left[1-\eta\left(1+\frac{\delta}{\beta}\right)\right]}_{A}P_t+\underbrace{\frac{\eta(\alpha+\gamma)}{\beta}}_{B} \]
<p>Control: con \(\eta=1\), \(A=-\delta/\beta\) y \(B=(\alpha+\gamma)/\beta\), como en la telaraña.</p>'''),
('Equilibrio',r'Calcular \(1-A\)',r'',
 r'''\[ 1-A=\eta\left(1+\frac{\delta}{\beta}\right)=\eta\,\frac{\beta+\delta}{\beta} \]'''),
('Equilibrio',r'Precio de equilibrio',r'',
 r'''\[ P^*=\frac{B}{1-A}=\frac{\eta(\alpha+\gamma)/\beta}{\eta(\beta+\delta)/\beta}=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>\(\eta\) se cancela: el equilibrio es el mismo que en la telaraña.</p>'''),
('Equilibrio',r'Solución general',r'',
 r'''\[ P_t=\left(P_0-P^*\right)A^t+P^* \]'''),
('Estabilidad',r'Las dos desigualdades',r'Escribí \(|A|\lt 1\) como doble desigualdad.',
 r'''\[ -1\lt 1-\eta\left(1+\frac{\delta}{\beta}\right)\lt 1 \]'''),
('Estabilidad',r'Desigualdad derecha',r'',
 r'''\[ 1-\eta\left(1+\frac{\delta}{\beta}\right)\lt 1\iff\eta\left(1+\frac{\delta}{\beta}\right)\gt 0 \]
<p>Se cumple siempre, porque \(\eta,\beta,\delta\gt 0\).</p>'''),
('Estabilidad',r'Desigualdad izquierda',r'Despejá \(\delta/\beta\).',
 r'''\[ 1-\eta\left(1+\frac{\delta}{\beta}\right)\gt -1\iff\eta\left(1+\frac{\delta}{\beta}\right)\lt 2\iff 1+\frac{\delta}{\beta}\lt\frac{2}{\eta}\iff\frac{\delta}{\beta}\lt\frac{2-\eta}{\eta} \]'''),
('Estabilidad',r'Comparación con la telaraña',r'¿Cuánto vale la cota con \(\eta=1\)? ¿Y con \(\eta\lt 1\)?',
 r'''<p>Con \(\eta=1\) la cota es 1: se recupera \(\delta\lt\beta\). Con \(\eta\lt 1\), \(\frac{2-\eta}{\eta}\gt 1\) (porque \(2-\eta\gt\eta\)): el rango estable es más amplio y el mercado puede converger aunque \(\delta\gt\beta\).</p>'''),
('Forma de la trayectoria',r'¿Monótona u oscilante?',r'¿Cuándo es \(A\gt 0\)?',
 r'''\[ A\gt 0\iff\eta\left(1+\frac{\delta}{\beta}\right)\lt 1 \]
<p>Con un ajuste lento de las expectativas, la convergencia es monótona. Si \(A\lt 0\), el precio oscila como en la telaraña.</p>'''),
])

# ======================================================================= MD-05 inventarios
DERIV['04_mercado_con_inventarios.html']=(r'El precio se ajusta según el exceso de oferta que se acumula como inventario.',[
('Planteo',r'El sistema',r'',
 r'''\[ Q^d_t=\alpha-\beta P_t,\qquad Q^s_t=-\gamma+\delta P_t,\qquad P_{t+1}=P_t-\sigma\left(Q^s_t-Q^d_t\right),\quad\sigma\gt 0 \]'''),
('Exceso de oferta',r'Restar las funciones',r'Calculá \(Q^s_t-Q^d_t\).',
 r'''\[ Q^s_t-Q^d_t=(-\gamma+\delta P_t)-(\alpha-\beta P_t)=-\gamma-\alpha+\delta P_t+\beta P_t \]'''),
('Exceso de oferta',r'Agrupar',r'',
 r'''\[ Q^s_t-Q^d_t=(\beta+\delta)\,P_t-(\alpha+\gamma) \]'''),
('Exceso de oferta',r'Factorizar',r'Sacá \((\beta+\delta)\) factor común.',
 r'''\[ Q^s_t-Q^d_t=(\beta+\delta)\left(P_t-\frac{\alpha+\gamma}{\beta+\delta}\right)=(\beta+\delta)\left(P_t-P^*\right) \]
<p>Si \(P_t\gt P^*\) hay exceso de oferta (se acumula stock) y el precio baja. Si \(P_t\lt P^*\), el precio sube.</p>'''),
('Reducción',r'Sustituir en la regla de ajuste',r'',
 r'''\[ P_{t+1}=P_t-\sigma\left[(\beta+\delta)P_t-(\alpha+\gamma)\right] \]'''),
('Reducción',r'Distribuir \(\sigma\)',r'',
 r'''\[ P_{t+1}=P_t-\sigma(\beta+\delta)P_t+\sigma(\alpha+\gamma) \]'''),
('Reducción',r'Forma canónica',r'Sacá \(P_t\) factor común.',
 r'''\[ P_{t+1}=\underbrace{\left[1-\sigma(\beta+\delta)\right]}_{A}P_t+\underbrace{\sigma(\alpha+\gamma)}_{B} \]'''),
('Equilibrio',r'Precio de equilibrio',r'',
 r'''\[ 1-A=\sigma(\beta+\delta)\quad\Longrightarrow\quad P^*=\frac{\sigma(\alpha+\gamma)}{\sigma(\beta+\delta)}=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>Coincide con el precio que anula el exceso de oferta.</p>'''),
('Equilibrio',r'Solución y desvío',r'Llamá \(x=\sigma(\beta+\delta)\).',
 r'''\[ P_t=\left(P_0-P^*\right)(1-x)^t+P^*,\qquad z_{t+1}=(1-x)\,z_t \]'''),
('Estabilidad',r'Desigualdad derecha',r'',
 r'''\[ 1-x\lt 1\iff x\gt 0 \]
<p>Se cumple siempre.</p>'''),
('Estabilidad',r'Desigualdad izquierda',r'',
 r'''\[ 1-x\gt -1\iff x\lt 2\iff\sigma\lt\frac{2}{\beta+\delta} \]'''),
('Zonas',r'Qué pasa con un desvío en un período',r'Si el precio está \(d\) por encima de \(P^*\), ¿dónde queda después de un ajuste?',
 r'''<p>El ajuste baja el precio \(x\,d\), así que el nuevo desvío es \((1-x)\,d\):</p>
<table class="dtab"><tr><td>\(0\lt x\lt 1\)</td><td>corrige menos que \(d\): monótona convergente</td></tr><tr><td>\(x=1\)</td><td>llega a \(P^*\) en un paso</td></tr><tr><td>\(1\lt x\lt 2\)</td><td>se pasa menos que \(d\): oscilación amortiguada</td></tr><tr><td>\(x=2\)</td><td>queda \(d\) del otro lado: oscilación uniforme</td></tr><tr><td>\(x\gt 2\)</td><td>se pasa más que \(d\): explosiva</td></tr></table>'''),
])

# ======================================================================= MD-06 triángulo
DERIV['07_triangulo_de_estabilidad.html']=(r'El método general para \(y_{t+2}+p\,y_{t+1}+q\,y_t=g\), que después se aplica a cada modelo de segundo orden.',[
('Planteo',r'La ecuación',r'',
 r'''\[ y_{t+2}+p\,y_{t+1}+q\,y_t=g,\qquad y_0,\;y_1\text{ dados} \]
<p>Hacen falta dos condiciones iniciales porque cada valor depende de los dos anteriores.</p>'''),
('Planteo',r'Estrategia',r'',
 r'''<p>Como la ecuación es lineal, la solución es la suma de una solución particular \(y^*\) y la solución general de la homogénea \(z_t\):</p>
\[ y_t=y^*+z_t \]'''),
('Solución particular',r'Proponer una constante',r'Reemplazá \(y_t=y_{t+1}=y_{t+2}=y^*\).',
 r'''\[ y^*+p\,y^*+q\,y^*=g \]'''),
('Solución particular',r'Despejar',r'',
 r'''\[ y^*(1+p+q)=g\quad\Longrightarrow\quad y^*=\frac{g}{1+p+q}\qquad(1+p+q\neq0) \]'''),
('Homogénea',r'La ecuación del desvío',r'Restá la ecuación del paso 3 a la original.',
 r'''\[ (y_{t+2}-y^*)+p\,(y_{t+1}-y^*)+q\,(y_t-y^*)=0\quad\Longrightarrow\quad z_{t+2}+p\,z_{t+1}+q\,z_t=0 \]'''),
('Homogénea',r'Probar con una potencia',r'Reemplazá \(z_t=r^t\).',
 r'''\[ r^{t+2}+p\,r^{t+1}+q\,r^t=0\quad\Longrightarrow\quad r^t\left(r^2+p\,r+q\right)=0 \]'''),
('Homogénea',r'Ecuación característica',r'¿Qué tiene que valer cero?',
 r'''<p>Buscamos \(r\neq0\), así que tiene que anularse el paréntesis:</p>
\[ r^2+p\,r+q=0 \]'''),
('Homogénea',r'Raíces',r'',
 r'''\[ r_{1,2}=\frac{-p\pm\sqrt{\Delta}}{2},\qquad\Delta=p^2-4q \]
<p>Relaciones de Vieta: \(r_1+r_2=-p\) y \(r_1r_2=q\).</p>'''),
('Tres casos',r'\(\Delta\gt 0\): raíces reales distintas',r'',
 r'''<p>\(r_1^t\) y \(r_2^t\) son soluciones, y por linealidad también su combinación:</p>
\[ z_t=C_1\,r_1^{\,t}+C_2\,r_2^{\,t} \]'''),
('Tres casos',r'\(\Delta=0\): raíz doble',r'Probá que \(t\,r^t\) también es solución cuando \(r=-p/2\).',
 r'''<p>Reemplazando \(z_t=t\,r^t\):</p>
\[ (t+2)r^{t+2}+p(t+1)r^{t+1}+q\,t\,r^t=t\,r^t\left(r^2+pr+q\right)+r^{t+1}(2r+p)=0 \]
<p>porque \(r^2+pr+q=0\) y \(2r+p=0\). Entonces \(z_t=(C_1+C_2\,t)\,r^t\).</p>'''),
('Tres casos',r'\(\Delta\lt 0\): raíces complejas',r'Escribí las raíces como \(a\pm bi\) y calculá su módulo.',
 r'''\[ r=a\pm b\,i,\qquad a=-\frac{p}{2},\qquad b=\frac{\sqrt{4q-p^2}}{2} \]
\[ \rho=\sqrt{a^2+b^2}=\sqrt{\frac{p^2}{4}+\frac{4q-p^2}{4}}=\sqrt q,\qquad\cos\theta=\frac{a}{\rho}=-\frac{p}{2\sqrt q} \]'''),
('Tres casos',r'Forma trigonométrica',r'Usá De Moivre: \((\cos\theta+i\operatorname{sen}\theta)^t=\cos\theta t+i\operatorname{sen}\theta t\).',
 r'''\[ r^t=\rho^t\left(\cos\theta t\pm i\operatorname{sen}\theta t\right)\quad\Longrightarrow\quad z_t=\rho^t\left(C_1\cos\theta t+C_2\operatorname{sen}\theta t\right) \]
<p>Es un ciclo de período \(2\pi/\theta\) con amplitud que se multiplica por \(\rho\) cada período.</p>'''),
('Constantes',r'Usar las condiciones iniciales',r'Con \(\Delta\gt 0\), planteá el sistema para \(t=0\) y \(t=1\).',
 r'''\[ \begin{cases} C_1+C_2=z_0\\ C_1r_1+C_2r_2=z_1 \end{cases}\qquad z_0=y_0-y^*,\;z_1=y_1-y^* \]'''),
('Constantes',r'Resolver el sistema',r'',
 r'''\[ C_1=\frac{z_1-r_2\,z_0}{r_1-r_2},\qquad C_2=\frac{r_1\,z_0-z_1}{r_1-r_2} \]
<p>La solución completa es \(y_t=y^*+C_1r_1^{\,t}+C_2r_2^{\,t}\).</p>'''),
('Estabilidad',r'Qué hay que pedir',r'¿Cuándo \(z_t\to0\) para cualquier \(z_0,z_1\)?',
 r'''\[ z_t\to0\iff|r_1|\lt 1\;\text{ y }\;|r_2|\lt 1 \]'''),
('Estabilidad',r'Caso complejo',r'',
 r'''\[ |r|=\rho=\sqrt q\lt 1\iff q\lt 1 \]'''),
('Estabilidad',r'Caso real',r'Mirá la parábola \(f(r)=r^2+pr+q\) en \(r=1\) y \(r=-1\).',
 r'''<p>La parábola abre hacia arriba. Las dos raíces están en \((-1,1)\) cuando \(f(1)\gt 0\), \(f(-1)\gt 0\) y además no están las dos del mismo lado afuera del intervalo, lo que garantiza \(r_1r_2=q\lt 1\).</p>
\[ f(1)=1+p+q,\qquad f(-1)=1-p+q \]'''),
('Estabilidad',r'El triángulo',r'',
 r'''\[ \boxed{1-q\gt 0,\qquad 1+p+q\gt 0,\qquad 1-p+q\gt 0} \]
<p>Las tres rectas forman un triángulo en el plano \((p,q)\) con vértices \((-2,1)\), \((2,1)\) y \((0,-1)\).</p>'''),
('Forma de la trayectoria',r'Qué raíz domina',r'',
 r'''<table class="dtab"><tr><td>raíces complejas</td><td>ciclo</td></tr><tr><td>raíz real dominante negativa</td><td>zigzag</td></tr><tr><td>raíz real dominante positiva</td><td>monótona</td></tr></table>
<p>La parábola \(q=p^2/4\) (donde \(\Delta=0\)) separa las raíces complejas (arriba) de las reales (abajo).</p>'''),
])

# ======================================================================= MD-07 extrapolación
DERIV['05_telarana_extrapolacion.html']=(r'Los productores proyectan la última variación del precio y la ecuación pasa a ser de segundo orden.',[
('Planteo',r'El sistema',r'',
 r'''\[ \begin{cases} Q^d_t=\alpha-\beta P_t\\ Q^s_t=-\gamma+\delta P^e_t\\ Q^d_t=Q^s_t\\ P^e_t=P_{t-1}+\phi\,(P_{t-1}-P_{t-2}) \end{cases} \]
<p>Cuatro ecuaciones y cuatro incógnitas: \(Q^d_t\), \(Q^s_t\), \(P_t\), \(P^e_t\).</p>'''),
('Reducción',r'Equilibrio de mercado',r'',
 r'''\[ \alpha-\beta P_t=-\gamma+\delta P^e_t \]'''),
('Reducción',r'Despejar \(P_t\)',r'Aislá \(\beta P_t\) y dividí por \(\beta\).',
 r'''\[ \beta P_t=\alpha+\gamma-\delta P^e_t\quad\Longrightarrow\quad P_t=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}P^e_t \]'''),
('Reducción',r'Reordenar la expectativa',r'Distribuí \(\phi\) y agrupá \(P_{t-1}\).',
 r'''\[ P^e_t=P_{t-1}+\phi P_{t-1}-\phi P_{t-2}=(1+\phi)P_{t-1}-\phi P_{t-2} \]'''),
('Reducción',r'Sustituir',r'',
 r'''\[ P_t=\frac{\alpha+\gamma}{\beta}-\frac{\delta}{\beta}\Big[(1+\phi)P_{t-1}-\phi P_{t-2}\Big] \]'''),
('Reducción',r'Distribuir \(-\delta/\beta\)',r'',
 r'''\[ P_t=-\frac{\delta(1+\phi)}{\beta}P_{t-1}+\frac{\delta\phi}{\beta}P_{t-2}+\frac{\alpha+\gamma}{\beta} \]'''),
('Reducción',r'Pasar todo a la izquierda',r'',
 r'''\[ P_t+\frac{\delta(1+\phi)}{\beta}P_{t-1}-\frac{\delta\phi}{\beta}P_{t-2}=\frac{\alpha+\gamma}{\beta} \]'''),
('Reducción',r'Adelantar dos períodos',r'Reemplazá \(t\) por \(t+2\).',
 r'''\[ \boxed{P_{t+2}+\frac{\delta(1+\phi)}{\beta}P_{t+1}-\frac{\delta\phi}{\beta}P_t=\frac{\alpha+\gamma}{\beta}} \]'''),
('Reducción',r'Identificar coeficientes',r'Compará con \(y_{t+2}+p\,y_{t+1}+q\,y_t=g\).',
 r'''\[ p=\mu(1+\phi),\qquad q=-\mu\phi,\qquad g=\frac{\alpha+\gamma}{\beta},\qquad\mu=\frac{\delta}{\beta}\gt 0 \]
<p>El signo de \(q\) depende de \(\phi\). Con \(\phi=0\), \(q=0\) y la ecuación es de primer orden: la telaraña estándar.</p>'''),
('Equilibrio',r'Proponer una constante',r'Reemplazá \(P_t=P_{t+1}=P_{t+2}=A\).',
 r'''\[ A+\frac{\delta(1+\phi)}{\beta}A-\frac{\delta\phi}{\beta}A=\frac{\alpha+\gamma}{\beta} \]'''),
('Equilibrio',r'Factor común \(A\)',r'',
 r'''\[ A\left[1+\frac{\delta(1+\phi)-\delta\phi}{\beta}\right]=\frac{\alpha+\gamma}{\beta} \]'''),
('Equilibrio',r'Simplificar el corchete',r'',
 r'''\[ \delta(1+\phi)-\delta\phi=\delta\quad\Longrightarrow\quad A\cdot\frac{\beta+\delta}{\beta}=\frac{\alpha+\gamma}{\beta}\quad\Longrightarrow\quad P^*=\frac{\alpha+\gamma}{\beta+\delta} \]
<p>\(\phi\) no aparece: la extrapolación cambia la dinámica, no el equilibrio.</p>'''),
('Raíces',r'Ecuación característica',r'',
 r'''\[ r^2+\mu(1+\phi)\,r-\mu\phi=0 \]'''),
('Raíces',r'Discriminante',r'',
 r'''\[ \Delta=p^2-4q=\mu^2(1+\phi)^2+4\mu\phi \]'''),
('Raíces',r'Si \(\phi\ge0\)',r'¿Puede ser negativo \(\Delta\)?',
 r'''<p>Los dos términos son no negativos y el primero es positivo, así que \(\Delta\gt 0\): raíces reales. Las raíces complejas sólo pueden aparecer con \(\phi\lt 0\).</p>'''),
('Raíces',r'\(\Delta\lt 0\) como desigualdad en \(\phi\)',r'Dividí por \(\mu\gt 0\) y desarrollá el cuadrado.',
 r'''\[ \mu(1+\phi)^2+4\phi\lt 0\iff\mu+2\mu\phi+\mu\phi^2+4\phi\lt 0\iff\mu\phi^2+2(\mu+2)\phi+\mu\lt 0 \]'''),
('Raíces',r'Raíces de la cuadrática en \(\phi\)',r'',
 r'''\[ \phi_{1,2}=\frac{-2(\mu+2)\pm\sqrt{4(\mu+2)^2-4\mu^2}}{2\mu}=\frac{-(\mu+2)\pm2\sqrt{1+\mu}}{\mu} \]
<p>porque \((\mu+2)^2-\mu^2=4\mu+4\). La parábola abre hacia arriba, así que \(\Delta\lt 0\iff\phi_2\lt\phi\lt\phi_1\). Además \(\phi_1\phi_2=\mu/\mu=1\).</p>'''),
('Estabilidad',r'Las tres condiciones',r'Reemplazá \(p\) y \(q\) en \(1-q\), \(1+p+q\) y \(1-p+q\).',
 r'''\[ 1-q=1+\mu\phi,\qquad 1+p+q=1+\mu+\mu\phi-\mu\phi=1+\mu,\qquad 1-p+q=1-\mu-\mu\phi-\mu\phi=1-\mu(1+2\phi) \]'''),
('Estabilidad',r'Condición 2',r'',
 r'''<p>\(1+\mu\gt 0\) se cumple siempre.</p>'''),
('Estabilidad',r'Condición 1',r'',
 r'''\[ 1+\mu\phi\gt 0\iff\phi\gt-\frac{1}{\mu}=-\frac{\beta}{\delta} \]'''),
('Estabilidad',r'Condición 3',r'',
 r'''\[ \mu(1+2\phi)\lt 1\iff 1+2\phi\lt\frac{\beta}{\delta}\iff\phi\lt\frac12\left(\frac{\beta}{\delta}-1\right)=\frac{\beta-\delta}{2\delta} \]'''),
('Estabilidad',r'Reunir las condiciones',r'',
 r'''\[ \boxed{-\frac{\beta}{\delta}\lt\phi\lt\frac{\beta-\delta}{2\delta}} \]
<p>El intervalo no es vacío si \(-\frac1\mu\lt\frac{1-\mu}{2\mu}\iff-2\lt 1-\mu\iff\mu\lt 3\). La cota superior es positiva sólo si \(\beta\gt\delta\).</p>'''),
('Interpretación',r'Comparación con la telaraña estándar',r'',
 r'''<p>Con \(\phi=0\) la condición queda \(0\lt\frac{\beta-\delta}{2\delta}\iff\delta\lt\beta\). Extrapolar (\(\phi\gt 0\)) achica el rango estable; corregir (\(\phi\lt 0\)) lo amplía, hasta el límite \(\phi\gt-\beta/\delta\): más allá, los productores sobrecorrigen y el ciclo vuelve a crecer.</p>'''),
])

# ======================================================================= MD-08 Metzler
DERIV['06_inventarios_de_metzler.html']=(r'Ingreso, ventas e inversión en inventarios: el acelerador produce una ecuación de segundo orden.',[
('Planteo',r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=U_t+S_t+V_0\\ U_t=c\,Y_{t-1}\\ S_t=(1+k)(U_t-U_{t-1}) \end{cases}\qquad 0\lt c\lt 1,\;k\gt 0 \]'''),
('Planteo',r'De dónde sale \(S_t\)',r'Si las ventas suben \(U_t-U_{t-1}\), ¿qué tienen que hacer las empresas?',
 r'''<p>Reponer lo que se vendió de más (factor 1) y ampliar el stock para mantener la proporción deseada \(k\) entre inventario y ventas (factor \(k\)):</p>
\[ S_t=1\cdot(U_t-U_{t-1})+k\,(U_t-U_{t-1})=(1+k)(U_t-U_{t-1}) \]'''),
('Reducción',r'Ventas en función del ingreso',r'Usá \(U_t=c\,Y_{t-1}\) y \(U_{t-1}=c\,Y_{t-2}\).',
 r'''\[ U_t-U_{t-1}=c\,Y_{t-1}-c\,Y_{t-2}=c\,(Y_{t-1}-Y_{t-2})\quad\Longrightarrow\quad S_t=c(1+k)(Y_{t-1}-Y_{t-2}) \]'''),
('Reducción',r'Sustituir en el ingreso',r'',
 r'''\[ Y_t=c\,Y_{t-1}+c(1+k)(Y_{t-1}-Y_{t-2})+V_0 \]'''),
('Reducción',r'Distribuir',r'',
 r'''\[ Y_t=c\,Y_{t-1}+c(1+k)\,Y_{t-1}-c(1+k)\,Y_{t-2}+V_0 \]'''),
('Reducción',r'Agrupar \(Y_{t-1}\)',r'',
 r'''\[ c+c(1+k)=c\,(2+k)\quad\Longrightarrow\quad Y_t=c(2+k)\,Y_{t-1}-c(1+k)\,Y_{t-2}+V_0 \]'''),
('Reducción',r'Pasar a la izquierda',r'Pasá los términos en \(Y_{t-1}\) e \(Y_{t-2}\) al primer miembro.',
 r'''\[ Y_t-c(2+k)Y_{t-1}+c(1+k)Y_{t-2}=V_0 \]'''),
('Reducción',r'Adelantar dos períodos',r'Reemplazá \(t\) por \(t+2\).',
 r'''\[ \boxed{Y_{t+2}-c(2+k)\,Y_{t+1}+c(1+k)\,Y_t=V_0} \]
<p>\(p=-c(2+k)\), \(q=c(1+k)\), \(g=V_0\).</p>'''),
('Equilibrio',r'Proponer \(Y_t=A\)',r'',
 r'''\[ A-c(2+k)A+c(1+k)A=V_0 \]'''),
('Equilibrio',r'Simplificar',r'Desarrollá los productos dentro del corchete.',
 r'''\[ A\left[1-2c-ck+c+ck\right]=V_0\quad\Longrightarrow\quad A(1-c)=V_0\quad\Longrightarrow\quad Y^*=\frac{V_0}{1-c} \]
<p>\(k\) se cancela: es el multiplicador keynesiano.</p>'''),
('Raíces',r'Ecuación característica',r'',
 r'''\[ r^2-c(2+k)\,r+c(1+k)=0 \]'''),
('Raíces',r'Discriminante',r'Sacá \(c\) factor común.',
 r'''\[ \Delta=c^2(2+k)^2-4c(1+k)=c\left[c(2+k)^2-4(1+k)\right] \]'''),
('Raíces',r'Condición para ciclos',r'',
 r'''\[ \Delta\lt 0\iff c(2+k)^2\lt 4(1+k)\iff c\lt\frac{4(1+k)}{(2+k)^2} \]
<p>Esta cota es menor que 1 porque \((2+k)^2-4(1+k)=k^2\gt 0\).</p>'''),
('Raíces',r'Signo de las raíces reales',r'Mirá la suma y el producto.',
 r'''\[ r_1+r_2=c(2+k)\gt 0,\qquad r_1r_2=c(1+k)\gt 0 \]
<p>Si son reales, son las dos positivas: nunca hay zigzag. Si son complejas, \(|r|=\sqrt{c(1+k)}\).</p>'''),
('Estabilidad',r'Condición 1',r'',
 r'''\[ 1-q=1-c(1+k)\gt 0 \]'''),
('Estabilidad',r'Condición 2',r'',
 r'''\[ 1+p+q=1-c(2+k)+c(1+k)=1-c\gt 0\quad\checkmark \]'''),
('Estabilidad',r'Condición 3',r'',
 r'''\[ 1-p+q=1+c(2+k)+c(1+k)\gt 0\quad\checkmark \]'''),
('Estabilidad',r'La condición clave',r'',
 r'''\[ \boxed{c(1+k)\lt 1}\iff k\lt\frac{1-c}{c} \]'''),
('Regiones',r'Las cuatro regiones',r'',
 r'''<table class="dtab"><tr><td>\(c\lt\frac{1}{1+k}\)</td><td>oscilante y convergente</td></tr><tr><td>\(c=\frac{1}{1+k}\)</td><td>oscilante de amplitud constante</td></tr><tr><td>\(\frac{1}{1+k}\lt c\lt\frac{4(1+k)}{(2+k)^2}\)</td><td>oscilante y divergente</td></tr><tr><td>\(c\ge\frac{4(1+k)}{(2+k)^2}\)</td><td>monótono y divergente</td></tr></table>'''),
('Regiones',r'Corolario',r'Compará las dos cotas.',
 r'''\[ \frac{1}{1+k}\lt\frac{4(1+k)}{(2+k)^2}\iff(2+k)^2\lt 4(1+k)^2\iff 2+k\lt 2+2k\iff k\gt 0 \]
<p>La región estable queda adentro de la de oscilación: no existe un movimiento monótono estable.</p>'''),
])

# ======================================================================= MD-09 Samuelson
DERIV['08_samuelson.html']=(r'Multiplicador y acelerador juntos dan una ecuación de segundo orden con ciclos endógenos.',[
('Planteo',r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=C_t+I_t+G_0\\ C_t=\gamma\,Y_{t-1}\\ I_t=\alpha\,(C_t-C_{t-1}) \end{cases}\qquad 0\lt\gamma\lt 1,\;\alpha\gt 0 \]'''),
('Reducción',r'Consumo del período anterior',r'',
 r'''\[ C_{t-1}=\gamma\,Y_{t-2} \]'''),
('Reducción',r'Inversión en función del ingreso',r'Reemplazá \(C_t\) y \(C_{t-1}\) en \(I_t\).',
 r'''\[ I_t=\alpha\left(\gamma Y_{t-1}-\gamma Y_{t-2}\right)=\alpha\gamma\,(Y_{t-1}-Y_{t-2}) \]'''),
('Reducción',r'Sustituir en el ingreso',r'',
 r'''\[ Y_t=\gamma Y_{t-1}+\alpha\gamma(Y_{t-1}-Y_{t-2})+G_0 \]'''),
('Reducción',r'Distribuir \(\alpha\gamma\)',r'',
 r'''\[ Y_t=\gamma Y_{t-1}+\alpha\gamma Y_{t-1}-\alpha\gamma Y_{t-2}+G_0 \]'''),
('Reducción',r'Agrupar \(Y_{t-1}\)',r'Sacá \(\gamma\) factor común entre los términos en \(Y_{t-1}\).',
 r'''\[ \gamma+\alpha\gamma=\gamma(1+\alpha)\quad\Longrightarrow\quad Y_t=\gamma(1+\alpha)\,Y_{t-1}-\alpha\gamma\,Y_{t-2}+G_0 \]'''),
('Reducción',r'Pasar a la izquierda',r'',
 r'''\[ Y_t-\gamma(1+\alpha)Y_{t-1}+\alpha\gamma\,Y_{t-2}=G_0 \]'''),
('Reducción',r'Adelantar dos períodos',r'Reemplazá \(t\) por \(t+2\).',
 r'''\[ \boxed{Y_{t+2}-\gamma(1+\alpha)\,Y_{t+1}+\alpha\gamma\,Y_t=G_0} \]
<p>\(p=-\gamma(1+\alpha)\lt 0\), \(q=\alpha\gamma\gt 0\), \(g=G_0\).</p>'''),
('Equilibrio',r'Proponer \(Y_t=A\)',r'',
 r'''\[ A-\gamma(1+\alpha)A+\alpha\gamma A=G_0 \]'''),
('Equilibrio',r'Simplificar',r'',
 r'''\[ A\left[1-\gamma-\alpha\gamma+\alpha\gamma\right]=G_0\quad\Longrightarrow\quad A(1-\gamma)=G_0\quad\Longrightarrow\quad Y^*=\frac{G_0}{1-\gamma} \]
<p>Es el multiplicador keynesiano: la inversión inducida no cambia el nivel de equilibrio.</p>'''),
('Raíces',r'Ecuación característica',r'',
 r'''\[ r^2-\gamma(1+\alpha)\,r+\alpha\gamma=0,\qquad r_{1,2}=\frac{\gamma(1+\alpha)\pm\sqrt\Delta}{2} \]'''),
('Raíces',r'Discriminante',r'',
 r'''\[ \Delta=\gamma^2(1+\alpha)^2-4\alpha\gamma \]'''),
('Raíces',r'Condición para ciclos',r'Dividí por \(\gamma\gt 0\).',
 r'''\[ \Delta\lt 0\iff\gamma(1+\alpha)^2\lt 4\alpha\iff\gamma\lt\frac{4\alpha}{(1+\alpha)^2} \]'''),
('Raíces',r'Signo y módulo',r'',
 r'''<p>Suma \(\gamma(1+\alpha)\gt 0\) y producto \(\alpha\gamma\gt 0\): si son reales, las dos raíces son positivas y no hay zigzag. Si son complejas, \(|r|=\sqrt{\alpha\gamma}\).</p>'''),
('Estabilidad',r'Condición 1',r'',
 r'''\[ 1-q=1-\alpha\gamma\gt 0 \]'''),
('Estabilidad',r'Condición 2',r'',
 r'''\[ 1+p+q=1-\gamma-\alpha\gamma+\alpha\gamma=1-\gamma\gt 0\quad\checkmark \]'''),
('Estabilidad',r'Condición 3',r'',
 r'''\[ 1-p+q=1+\gamma+\alpha\gamma+\alpha\gamma=1+\gamma+2\alpha\gamma\gt 0\quad\checkmark \]'''),
('Estabilidad',r'La condición activa',r'',
 r'''\[ \boxed{\alpha\gamma\lt 1} \]'''),
('Interpretación',r'Cuándo hay ciclos endógenos',r'',
 r'''<p>Hay ciclo si \(\gamma\lt 4\alpha/(1+\alpha)^2\), es decir, con un acelerador alto respecto de la propensión al consumo. El ciclo se amortigua si \(\alpha\gamma\lt 1\) y explota si \(\alpha\gamma\gt 1\). La economía puede oscilar por su propia estructura, sin shocks externos.</p>'''),
])

# ======================================================================= MD-10 Hicks
DERIV['09_hicks.html']=(r'Samuelson con inversión autónoma creciente: la solución particular deja de ser constante.',[
('Planteo',r'El sistema',r'',
 r'''\[ \begin{cases} Y_t=C_t+I'_t+I''_t\\ C_t=\gamma\,Y_{t-1}\\ I'_t=\alpha\,(Y_{t-1}-Y_{t-2})\\ I''_t=I_0(1+g)^t \end{cases} \]'''),
('Reducción',r'Sustituir',r'',
 r'''\[ Y_t=\gamma Y_{t-1}+\alpha(Y_{t-1}-Y_{t-2})+I_0(1+g)^t \]'''),
('Reducción',r'Distribuir y agrupar',r'',
 r'''\[ Y_t=(\gamma+\alpha)\,Y_{t-1}-\alpha\,Y_{t-2}+I_0(1+g)^t \]'''),
('Reducción',r'Pasar a la izquierda',r'',
 r'''\[ Y_t-(\gamma+\alpha)Y_{t-1}+\alpha Y_{t-2}=I_0(1+g)^t \]'''),
('Reducción',r'Adelantar dos períodos',r'Ojo: también cambia el exponente del término independiente.',
 r'''\[ \boxed{Y_{t+2}-(\gamma+\alpha)Y_{t+1}+\alpha\,Y_t=I_0(1+g)^{t+2}} \]
<p>\(p=-(\gamma+\alpha)\), \(q=\alpha\). El término independiente no es constante.</p>'''),
('Solución particular',r'Proponer la forma',r'Si el término independiente es \((1+g)^t\), ¿qué forma tiene sentido probar?',
 r'''\[ Y^p_t=A(1+g)^t,\qquad Y^p_{t+1}=A(1+g)^{t+1},\qquad Y^p_{t+2}=A(1+g)^{t+2} \]'''),
('Solución particular',r'Sustituir',r'',
 r'''\[ A(1+g)^{t+2}-(\gamma+\alpha)A(1+g)^{t+1}+\alpha A(1+g)^t=I_0(1+g)^{t+2} \]'''),
('Solución particular',r'Dividir por \((1+g)^t\)',r'',
 r'''\[ A(1+g)^2-(\gamma+\alpha)A(1+g)+\alpha A=I_0(1+g)^2 \]'''),
('Solución particular',r'Despejar \(A\)',r'',
 r'''\[ A\left[(1+g)^2-(\gamma+\alpha)(1+g)+\alpha\right]=I_0(1+g)^2\quad\Longrightarrow\quad\boxed{A=\frac{I_0(1+g)^2}{(1+g)^2-(\gamma+\alpha)(1+g)+\alpha}} \]
<p>El ingreso de equilibrio \(A(1+g)^t\) crece a la tasa \(g\).</p>'''),
('Raíces',r'Ecuación característica',r'',
 r'''\[ r^2-(\gamma+\alpha)\,r+\alpha=0,\qquad\Delta=(\gamma+\alpha)^2-4\alpha \]'''),
('Raíces',r'Condición para ciclos',r'Tomá raíz cuadrada (los dos lados son positivos).',
 r'''\[ \Delta\lt 0\iff(\gamma+\alpha)^2\lt 4\alpha\iff\gamma+\alpha\lt 2\sqrt\alpha\iff\gamma\lt 2\sqrt\alpha-\alpha \]'''),
('Estabilidad',r'Condición 1',r'',
 r'''\[ 1-q=1-\alpha\gt 0 \]'''),
('Estabilidad',r'Condición 2',r'',
 r'''\[ 1+p+q=1-(\gamma+\alpha)+\alpha=1-\gamma\gt 0\quad\checkmark \]'''),
('Estabilidad',r'Condición 3',r'',
 r'''\[ 1-p+q=1+(\gamma+\alpha)+\alpha=1+\gamma+2\alpha\gt 0\quad\checkmark \]'''),
('Estabilidad',r'La condición activa',r'',
 r'''\[ \boxed{\alpha\lt 1} \]'''),
('Solución general',r'Tendencia más desvío',r'',
 r'''\[ Y_t=A(1+g)^t+z_t \]
<p>donde \(z_t\) es la solución de la homogénea (paso 10). Si \(\alpha\lt 1\), \(z_t\to0\) y el ingreso converge a la tendencia. Si \(\alpha\ge1\), las oscilaciones no se amortiguan: Hicks las acota con un techo (pleno empleo) y un piso (inversión autónoma).</p>'''),
])

# ======================================================================= MD-11 Phillips
DERIV['10_inflacion_desempleo.html']=(r'Curva de Phillips con expectativas, expectativas adaptativas y política monetaria (Chiang, §18.3), sin saltear cuentas.',[
('Planteo',r'El sistema',r'',
 r'''\[ \begin{cases} p_t=\alpha-T-\beta U_t+g\,\pi_t & (18.18)\\ \pi_{t+1}-\pi_t=j\,(p_t-\pi_t) & (18.19)\\ U_{t+1}-U_t=-k\,(m-p_{t+1}) & (18.20) \end{cases} \]
<p>Variables: \(p_t\) (inflación), \(\pi_t\) (inflación esperada), \(U_t\) (desempleo). Política: \(m\). Objetivo: una ecuación sólo en \(p\).</p>'''),
('Primera diferencia',r'Adelantar (18.18)',r'',
 r'''\[ p_{t+1}=\alpha-T-\beta U_{t+1}+g\,\pi_{t+1} \]'''),
('Primera diferencia',r'Restar (18.18)',r'¿Qué pasa con \(\alpha-T\)?',
 r'''<p>La constante \(\alpha-T\) se cancela:</p>
\[ p_{t+1}-p_t=-\beta\,(U_{t+1}-U_t)+g\,(\pi_{t+1}-\pi_t) \]'''),
('Primera diferencia',r'Usar (18.20)',r'',
 r'''\[ -\beta\,(U_{t+1}-U_t)=-\beta\left[-k(m-p_{t+1})\right]=\beta k\,(m-p_{t+1}) \]'''),
('Primera diferencia',r'Usar (18.19)',r'',
 r'''\[ g\,(\pi_{t+1}-\pi_t)=g\,j\,(p_t-\pi_t) \]'''),
('Primera diferencia',r'Resultado',r'',
 r'''\[ p_{t+1}-p_t=\beta k\,(m-p_{t+1})+g\,j\,(p_t-\pi_t)\qquad(18.21) \]'''),
('Eliminar π',r'Despejar \(g\pi_t\) de (18.18)',r'',
 r'''\[ g\,\pi_t=p_t-(\alpha-T)+\beta U_t \]'''),
('Eliminar π',r'Calcular \(g\,j\,(p_t-\pi_t)\)',r'Distribuí y reemplazá \(g\pi_t\).',
 r'''\[ g\,j\,(p_t-\pi_t)=g\,j\,p_t-j\,(g\pi_t)=g\,j\,p_t-j\left[p_t-(\alpha-T)+\beta U_t\right] \]
\[ =-j(1-g)\,p_t+j(\alpha-T)-j\beta\,U_t \]'''),
('Eliminar π',r'Reemplazar en (18.21)',r'',
 r'''\[ p_{t+1}-p_t=\beta k\,m-\beta k\,p_{t+1}-j(1-g)\,p_t+j(\alpha-T)-j\beta\,U_t \]'''),
('Eliminar π',r'Ordenar',r'Pasá los términos en \(p\) y \(U\) a la izquierda.',
 r'''\[ \begin{aligned} (1+\beta k)\,p_{t+1}-\left[1-j(1-g)\right]p_t+j\beta\,U_t\\ =\beta k\,m+j(\alpha-T)\qquad(18.23) \end{aligned} \]'''),
('Eliminar U',r'Adelantar (18.23)',r'',
 r'''\[ \begin{aligned} (1+\beta k)\,p_{t+2}-\left[1-j(1-g)\right]p_{t+1}+j\beta\,U_{t+1}\\ =\beta k\,m+j(\alpha-T) \end{aligned} \]'''),
('Eliminar U',r'Restar (18.23)',r'El miembro derecho es el mismo: se cancela.',
 r'''\[ \begin{aligned} (1+\beta k)(p_{t+2}-p_{t+1})-\left[1-j(1-g)\right](p_{t+1}-p_t)\\ +\,j\beta\,(U_{t+1}-U_t)=0 \end{aligned} \]'''),
('Eliminar U',r'Usar (18.20) otra vez',r'',
 r'''\[ j\beta\,(U_{t+1}-U_t)=j\beta\left[-k(m-p_{t+1})\right]=j\beta k\,p_{t+1}-j\beta k\,m \]'''),
('Eliminar U',r'Coeficiente de \(p_{t+1}\)',r'Juntá todos los términos que multiplican a \(p_{t+1}\).',
 r'''\[ -(1+\beta k)-\left[1-j(1-g)\right]+j\beta k=-\left[2+\beta k-j+gj-j\beta k\right] \]
<p>Como \((1-j)(1+\beta k)=1+\beta k-j-j\beta k\), el corchete es \((1+gj)+(1-j)(1+\beta k)\).</p>'''),
('Eliminar U',r'Ecuación ordenada',r'',
 r'''\[ \begin{aligned} (1+\beta k)\,p_{t+2}-\left[(1+gj)+(1-j)(1+\beta k)\right]p_{t+1}\\ +\left[1-j(1-g)\right]p_t=j\beta k\,m \end{aligned} \]'''),
('Eliminar U',r'Dividir por \(1+\beta k\)',r'',
 r'''\[ \boxed{p_{t+2}-a_1\,p_{t+1}+a_2\,p_t=c}\qquad(18.24) \]
\[ a_1=\frac{1+gj+(1-j)(1+\beta k)}{1+\beta k},\qquad a_2=\frac{1-j(1-g)}{1+\beta k},\qquad c=\frac{j\beta k\,m}{1+\beta k} \]'''),
('Equilibrio',r'Inflación de equilibrio',r'Proponé \(p_t=\bar p\).',
 r'''\[ \bar p\,(1-a_1+a_2)=c\quad\Longrightarrow\quad\bar p=\frac{c}{1-a_1+a_2} \]'''),
('Equilibrio',r'Calcular \(1-a_1+a_2\)',r'',
 r'''\[ 1-a_1+a_2=\frac{(1+\beta k)-(1+gj)-(1-j)(1+\beta k)+1-j+gj}{1+\beta k}=\frac{j(1+\beta k)-j}{1+\beta k}=\frac{\beta jk}{1+\beta k} \]'''),
('Equilibrio',r'Resultado',r'',
 r'''\[ \bar p=\frac{j\beta k\,m/(1+\beta k)}{\beta jk/(1+\beta k)}=m \]
<p>En el largo plazo la inflación iguala la tasa de expansión monetaria.</p>'''),
('Convergencia',r'Suma de las raíces',r'',
 r'''\[ r_1+r_2=a_1=\frac{1+gj}{1+\beta k}+1-j\gt 0 \]'''),
('Convergencia',r'Producto de las raíces',r'',
 r'''\[ r_1r_2=a_2=\frac{1-j(1-g)}{1+\beta k}\in(0,1) \]
<p>porque \(0\lt 1-j(1-g)\le 1\) y \(1+\beta k\gt 1\).</p>'''),
('Convergencia',r'El tercer dato',r'',
 r'''\[ (1-r_1)(1-r_2)=1-(r_1+r_2)+r_1r_2=1-a_1+a_2=\frac{\beta jk}{1+\beta k}\gt 0 \]'''),
('Convergencia',r'Caso real',r'Combiná los tres datos.',
 r'''<p>Producto positivo: mismo signo. Suma positiva: las dos positivas. \((1-r_1)(1-r_2)\gt 0\): las dos menores que 1 o las dos mayores. Producto menor que 1: no pueden ser las dos mayores. Queda \(0\lt r_2\lt r_1\lt 1\).</p>'''),
('Convergencia',r'Caso complejo',r'',
 r'''\[ \rho=\sqrt{a_2}\lt 1 \]
<p>En los dos casos \(p_t\to m\): la convergencia está garantizada por las hipótesis del modelo.</p>'''),
('Largo plazo',r'Desempleo de equilibrio',r'En el estado estacionario \(\pi=p=m\). Reemplazá en (18.18).',
 r'''\[ m=\alpha-T-\beta\bar U+g\,m\quad\Longrightarrow\quad\beta\bar U=\alpha-T-(1-g)\,m\quad\Longrightarrow\quad\bar U=\frac{1}{\beta}\Big[\alpha-T-(1-g)\,m\Big] \]'''),
('Largo plazo',r'Curva de Phillips de largo plazo',r'Reemplazá \(m=\bar p\).',
 r'''\[ \bar U=\frac{1}{\beta}\Big[\alpha-T-(1-g)\,\bar p\Big],\qquad\frac{d\bar U}{d\bar p}=-\frac{1-g}{\beta} \]
<p>Si \(g\lt 1\), la pendiente es negativa: hay un trade-off permanente. Si \(g=1\), \(\bar U=(\alpha-T)/\beta\) no depende de \(\bar p\): la curva es vertical en la tasa natural de desempleo.</p>'''),
])
