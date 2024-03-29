---
author: Артём Коржиманов
title: Квантовомеханическая теория водородоподобных атомов
date: 2020-10-25
keywords: [физика, атом, строение атома, квантовая механика]
lang: ru-RU
---
# Квантовомеханическая теория водородоподобных атомов
## Электрон в кулоновском потенциале
Теперь у нас имеется весь необходимый инструментарий для решения задачи о строении атома в рамках квантовой механики. С математической точки зрения, это задача о динамике взаимодействующих друг с другом электронов в кулоновском поле ядра. Для атома с произвольным количеством электронов на орбите эта задача, однако, аналитически не решается. Более того, сложности возникают и с численным решением уже для достаточно простых атомов с числом электронов больше двух–трёх. Однако фундаментальные результаты и общие закономерности можно получить и на примере задачи с одним электроном на орбите. Такая задача решается полностью аналитически.

Атомы, имеющие на орбите только один электрон, называются водородоподобными. Примерами таких атомов могут служить собственно изотопы водорода, а также ионы $\rm{He}^+$, $\rm{Li}^{2+}$ и т. д.

Если пренебречь движением тяжёлого ядра, то систему можно считать одночастичной и рассматривать движение только электрона. Оно описывается уравнением Шрёдингера вида
$$
i\hbar\frac{\partial \Psi}{\partial t} = \hat H\Psi
$$
где $\hat H$ — соответствующий оператор Гамильтона.

Нашей задачей будет поиск стационарных решений вида $\Psi(\vec r, t) = \psi(\vec r)\exp(i\frac{E}{\hbar} t)$, где $E$ — полная энергия электрона. Такие решения удовлетворяют стационарному уравнению Шрёдингера вида:
$$
\hat H\psi = E\psi
$$
Для удобства будем работать в сферической системе координат $(r, \vartheta,\varphi)$, в которой потенциальная энергия электрона имеет вид:
$$
U(\vec r) \equiv U(r) = - \frac{Ze^2}{r}
$$
где $Z$ — зарядовое число ядра.

В сферических координатах удобно представить оператор Гамильтона в следующем виде:
$$
\hat H = \hat T + \hat U = \frac{\hat p_r^2}{2m} + \frac{\hat {L^2}}{2mr^2} + U(r)
$$
где $\hat p_r$ — оператор радиальной составляющей импульса электрона, имеющий следующий вид:
$$
\hat p_r^2 = -\hbar^2\Delta_r = -\hbar^2\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right)
$$
Как мы показали в предыдущих лекциях, оператор $\hat {L^2}$ действует только на угловые координаты частицы, поэтому он коммутирует с операторами $\hat p_r$ и $U(r)$, и следовательно, коммутирует с оператором Гамильтона $\hat H$. Это означает, что можно выбрать собственные функции оператора Гамильтона так, чтобы они совпадали с собственными функциями оператора $\hat {L^2}$. В этом случае будет справедливо следующее равенство:
$$
\hat {L^2}\psi = \hbar^2l(l+1)\psi
$$
Это упрощает стационарное уравнение Шрёдингера до следующего вида:
$$
\frac{\partial^2\psi}{\partial r^2} + \frac{2}{r}\frac{\partial\psi}{\partial r} + \frac{2m}{\hbar^2}\left(E + \frac{Ze^2}{r} - \frac{\hbar^2l(l+1)}{2mr^2}\right)\psi = 0
$$
Будем решать его методом, аналогичным тому, который мы использовали для анализа квантового гармонического осциллятора. Введём безразмерные величины
$$
\beta^2 = -\frac{2mE}{\hbar^2} \\
$$
$$
q = \frac{2mZe^2}{\hbar^2}
$$
где мы учли, что интересуемся только связанными состояниями, для которых $E < 0$. Получаем уравнение следующего вида:
$$
\frac{\partial^2\psi}{\partial r^2} + \frac{2}{r}\frac{\partial\psi}{\partial r} + \left(\frac{q}{r} - \beta^2 - \frac{l(l+1)}{r^2}\right)\psi = 0
$$
Будем искать его решение в виде:
$$
\psi = \frac{u(r)}{r}e^{-\beta r}f(\vartheta, \varphi)
$$
После подстановки получаем:
$$
\frac{d^2 u}{d r^2} - 2\beta \frac{du}{d r} + \left(\frac{q}{r} - \frac{l(l+1)}{r^2}\right)u = 0
$$
Исследуем поведение этого решения на бесконечности, представив его в виде ряда:
$$
u = \sum\limits_{k=\gamma}^\infty a_k r^k
$$
Подставляем решение в таком виде в уравнение и приравниваем нулю коэффициенты при степенях $r$. Для степени $\gamma-2$ получаем:
$$
\gamma(\gamma-1) - l(l+1) = 0
$$
откуда $\gamma = l+1$ или $\gamma = -l$. Второе решение даёт нефизичный результат (функция $\psi$ обращается в бесконечность в точке $r=0$), поэтому оставляем только первое.

Для остальных степеней имеем уравнения вида:
$$
\left[k(k+1) - l(l+1)\right]a_{k+1} = (2\beta k - q)a_k,\ k = \gamma+1,\gamma+2,\dots
$$
Отсюда имеем рекуррентное соотношение между коэффициентами ряда:
$$
\frac{a_{k+1}}{a_k} = \frac{2\beta k - q}{k(k+1) - l(l+1)}
$$
Поведение функции $u(r)$ при больших $r$ определяется поведением коэффициентов при больших $k$. Асимптотически они ведут себя как:
$$
\frac{a_{k+1}}{a_k} \approx \frac{2\beta}{k+1}
$$
Но точно так же ведут себя и коэффициенты разложения в ряд функции $e^{2\beta r}$. Действительно:
$$
e^{2\beta r} = \sum\limits_k c_kr^k = \sum\limits_k \frac{1}{k!}(2\beta r)^k \\
$$
$$
\frac{c_{k+1}}{c_k} = \frac{2\beta}{k+1}
$$
Таким образом, функция $u(r)$ асимптотически ведёт себя на бесконечности, как функция $e^{2\beta r}$, следовательно, функция $\psi$ ведёт себя там же как $e^{\beta r}$, то есть расходится. Это означает, что такие решения нефизичны.

Мы, однако, рассмотрели только такие решения, для которых коэффициенты $a_k$ не обращаются в нуль. Если для некоторого $k=n$ коэффициент $a_{n+1}$ обратится в нуль, то будут равны нулю и все коэффициенты $a_k$ для $k>n+1$. Это означает, что функция $u(r)$ будет представлять собой полином степени $n$, и функция $\psi$ на бесконечности будет вести себя как $e^{-\beta r}$, то есть будет ограничена.

Условие существования таких решений можно получить, приравняв нулю $a_{n+1}$ в полученной ранее рекуррентной формуле:
$$
2\beta_n n - q = 0 \\
$$
$$
\beta_n = \frac{q}{2n}
$$
Это накладывает условие на энергию электрона:
$$
E_n = -\frac{\hbar^2\beta_n^2}{2m} = - \frac{mZ^2e^4}{2\hbar^2n^2}
$$
Таким образом, мы нашли условие квантования энергии электрона в водородоподобном атоме. Видно, что выражение для энергии стационарных состояний электрона, полученное нами, совпадает с выражением для энергии электрона в теории атома Бора, однако получено оно из более фундаментальных соображений.

Число $n$ называется __главным квантовым числом__.

## Вырожденность энергетических уровней атома
Одному и тому же $n$ в нашем выводе соответствует несколько различных состояний, отличающихся числами $l$ и $m$. В этом случае говорят о вырождении энергетического уровня. Число таких состояний называется _степенью или кратностью вырождения_.

Найдём кратность вырождения для уровня с квантовым числом $n$. Воспользуемся найденным нами условием $\gamma = l+1$. Тогда функция $u_n(r)$ представляет собой сумму:
$$
u = \sum\limits_{k=l+1}^n a_k r^k = r^{l+1} \sum\limits_{\alpha=0}^{n-l-1} a_{\alpha+l+1}r^\alpha
$$
Эта сумма существует для значений $l=0,1,\dots,n-1$. Для каждого $l$ число $m$ может принимать $2l+1$ значений, поэтому полная кратность вырождения равна:
$$
\sum\limits_{l=0}^{n-1} (2l+1) = n^2
$$
Необходимо также учесть, что электроны могут иметь внутренние степени свободы. Позднее мы узнаем, что каждый электрон обладает характеристикой, называемой спином, которая может принимать два значения. Таким образом, полная кратность вырождения равна $2n^2$.

## Квантовые числа
Напомним, что числа $n$, $l$, $m$ носят название главного, орбитального и магнитного квантового числа соответственно. Помимо них иногда вводят также _радиальное квантовое число_ $n_r = n-l-1$, равное числу членов в разложении функции $u(r)$ по степеням, то есть это число определяет число нулей этой функции.

Отметим также, что исторически состояния с различными $l$ принято обозначать буквами:
$$
l=0 \rightarrow s \\
$$
$$
l=1 \rightarrow p \\
$$
$$
l=2 \rightarrow d \\
$$
$$
l=3 \rightarrow f \\
$$
$$
l=4 \rightarrow g \\
$$
$$
\cdots
$$

## Примеры радиальных распределений некоторых состояний
Рассмотрим внешний вид радиальных зависимостей функции $\psi(r,\vartheta,\varphi)$ для простейших случаев.

### 1s
В состоянии $1s$ квантовые числа равны $n=1$, $l=0$, $m=0$. Следовательно,
$$
u = a_1r \\
$$
$$
\psi = a_1e^{-\beta r}f(\vartheta,\varphi)
$$
Физический смысл, однако, имеет вероятность $dP = |\psi|^2dV$ обнаружения электрона в объёме $dV$. В случае исследования радиальной зависимости в качестве объёма $dV$ выступает тонкий шаровой слой радиусом $r$ и толщиной $dr$, его объём: $dV = 4\pi r^2dr$, следовательно, вероятность равна:
$$
dP = 4\pi|\psi|^2r^2dr
$$
Откуда плотность вероятности:
$$
\rho(r) = 4\pi r^2|\psi|^2 \sim r^2e^{-2\beta r} = r^2e^{-qr}
$$
Эта функция имеет максимум в точке $r=\frac{2}{q}=\frac{\hbar^2}{me^2}$, что совпадает с выражением для боровского радиуса $r_B$.

### 2s
В состоянии $2s$ квантовые числа равны $n=2$, $l=0$, $m=0$. Следовательно,
$$
u = a_1r+a_2r^2 \\
$$
$$
\frac{a_2}{a_1} = -\frac{q}{4} \\
$$
$$
\rho(r) \sim r^2 \left(1-\frac{qr}{4}\right)^2 e^{-qr/2}
$$
Эта функция имеет нуль в точке $r=\frac{4}{q}=2r_B$

### 3s
В состоянии $3s$ квантовые числа равны $n=3$, $l=0$, $m=0$. Следовательно,
$$
u = a_1r+a_2r^2+a_3r^3 \\
$$
$$
\frac{a_2}{a_1} = -\frac{q}{3} \\
$$
$$
\frac{a_3}{a_2} = -\frac{q}{18} \\
$$
$$
\rho(r) \sim r^2 \left(1-\frac{qr}{3} + \frac{(qr)^2}{54}\right)^2 e^{-qr/3}
$$

### 2p
Состояние $1p$ не существует, поскольку $l$ не может быть больше, чем $n-1$, а в состоянии $2p$ квантовые числа имеют значения $n=2$, $l=1$ и число $m$ может принимать три значения $-1, 0, 1$, что даёт нам три различных состояния. Найдём радиальную плотность вероятности:
$$
u = a_2r^2 \\
$$
$$
\rho(r)\sim r^4 e^{-qr/2}
$$
Эта функция имеет один максимум в точке $r=\frac{8}{q}=4r_B$.

![Радиальные плотности вероятности обнаружения электрона в атоме водорода для состояний 1s, 2s, 3s и 2p.](img/hydrogen-radial-functions.svg){width=100%}
