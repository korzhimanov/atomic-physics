---
author: Артём Коржиманов
title: Спин-орбитальное взаимодействие и тонкая структура спектральных линий
date: 2020-11-10
keywords: [физика, атом, спин]
lang: ru-RU
---
# Спин-орбитальное взаимодействие

## Понятие о спин-орбитальном взаимодействии
Наличие у электрона в атоме как момента импульса и соответствующего магнитного момента, связанного с его орбитальным движением, так и собственного момента импульса и соответствующего магнитного момента, называемых спиновыми, приводит к существованию специфического взаимодействия, называемого спин-орбитальным. Это взаимодействие на качественном уровне может быть понято как взаимодействие между собственным магнитным моментом электрона и магнитным полем, создаваемым его орбитальным магнитным моментом.

Оценим по порядку величины поправку к энергии электрона, обусловленную спин-орбитальным взаимодействием. Из курса электродинамики известно, что энергия магнитного момента во внешнем поле равна:
$$
E = -\left(\vec \mu \vec H\right)
$$
Для электрона спиновый магнитный момент равен $\mu \equiv \mu_s = \mu_B = e\hbar/(2m_ec)$. Величину магнитного поля, создаваемого движением электрона по орбите, можно оценить как $H = ev_e/(cr_B^2) = m_e^2e^5v_e/(c\hbar^4)$. Оценить величину скорости электрона можно из равенства по модулю его кинетической и полной энергии: $m_ev_e^2/2 = m_e e^4/2\hbar^2$. Объединяя эти выражения, получаем:
$$
E_{s-o} \approx \frac{e\hbar}{2m_ec}\frac{m_e^2e^5v_e}{c\hbar^4} = \frac{m_ee^6}{2c^2\hbar^3}\frac{e^2}{\hbar} = \left(\frac{e^2}{c\hbar}\right)^2 \frac{m_e e^4}{2\hbar^2} \equiv \alpha^2 E_1
$$
Величина $\alpha = e^2/c\hbar \approx 1/137$ называется __постоянной тонкой структуры__, и в силу её малости спин-орбитальная добавка к энергии значительно меньше величины энергии электрона на основном уровне в атоме водорода.

Тем не менее, спин-орбитальное взаимодействие приводит к наблюдаемому эффекту, называемому __тонкой структурой__ спектральных линий. Дело в том, что знак спин-орбитальной добавки зависит от величины и знака проекции магнитного момента на направление магнитного поля, то есть от взаимной ориентации орбитального и спинового моментов импульса. Таким образом, состояния электрона, отличающиеся только этой ориентацией, будут иметь несколько различную энергию, а переход в эти состояния из других состояний будет происходить с испусканием или поглощением фотонов немного различной частоты. В спектре это будет наблюдаться как несколько близко расположенных линий, сливающихся при плохом разрешении спектрометра в одну. Тонкая структура была впервые измерена в атоме водорода Майкельсоном и Морли в 1887 году.

Спин-орбитальное взаимодействие в общем случае снимает вырождение уровней энергии атомов по квантовым числам $j$ и $l$. Образовавшуюся в результате систему подуровней называют __мультиплетом__.

Для атома водорода, однако, не происходит снятие вырождения по квантовому числу $l$, что связано с особой симметричностью чисто кулоновского потенциала. Точное выражение для энергии электрона в атоме водорода с учётом спин-орбитального взаимодействия и релятивистских эффектов, которые оказываются того же порядка по величине, были получены только после вывода Дираком релятивистского обобщения уравнения Шрёдингера — уравнения Дирака. Это выражение представляет собой бесконечный ряд, первые члены которого выглядят следующим образом:
$$
E_{n,j} = \frac{R}{n^2} - \frac{\alpha^2 R}{n^3}\left(\frac{1}{j+1/2} - \frac{3}{4n}\right)
$$

## Многоэлектронные атомы

### Приближение L-S связи

В более сложных случаях, когда атом содержит более одного электрона, ситуация значительно усложняется, поскольку магнитное поле теперь создаётся магнитными моментами всех электронов, а в энергию дают вклад его взаимодействие со всеми спиновыми магнитными моментами. То есть в общем случае энергия состояния зависит от значения квантовых чисел $j_i$ и $l_i$ каждого электрона. Во многих случаях, однако, удаётся получить удовлетворительные результаты в приближении так называемой __L-S-связи__, известного также как приближение нормальной связи или приближение Рассела — Саундерса.

Основная идея этого приближения заключается в том, что если энергия электростатического взаимодействия между электронами значительно превышает энергию спин-орбитального взаимодействия, то за счёт электростатических сил быстро устанавливается некое равновесие отдельно между орбитальными моментами отдельных электронов и отдельно между их спиновыми моментами, а взаимодействие между суммарным орбитальным моментом и суммарным спиновым моментом осуществляется значительно медленнее. В этом случае квазистационарные состояния электронов можно описывать всего тремя моментами импульса: суммарным орбитальным моментом импульса $\vec L = \sum \vec l_i$, суммарным спиновым моментом импульса $\vec S = \sum \vec s_i$ и суммарным общим моментом импульса $\vec J = \vec L + \vec S$.

Такое описание оказывается аналогичным описанию одного электрона в квантовыми числами $J$, $L$, $S$. Отличие от случая атома водорода, однако, заключается в том, что число $S$ может принимать не только значение 1/2, но и другие целые (в случае чётного числа электронов в атоме) и полуцелые (в случае нечётного числа электронов в атоме) значения. Отмечу, что при этом число $J$ тоже будет или целым, или полуцелым, и по правилу сложения моментов импульса может принимать только следующие значения: $J = |L-S|,...,L+S$.

На практике описание состояния многоэлектронного атома определяется только состоянием его внешних (валентных) электронов, поскольку моменты импульса электронов полностью заполненных оболочек, как правило, взаимно скомпенсированы.

В силу того, что система электронов находится в центрально-симметричном поле, то полный момент импульса $\vec J$ сохраняется. В силу малости спин-орбитального взаимодействия обычно также сохраняются модули моментов импульса $\vec L$ и $\vec S$, однако их проекции на вектор $\vec J$ могут меняться. Визуально это можно представлять как прецессию этих векторов вокруг вектора $\vec J$.

Состояние многоэлектронного атома обозначается аналогично состоянию электрона в атоме водорода, однако для обозначения велчины квантового числа $L$ используются прописные буквы латинского алфавита $S$, $P$, $D$, $F$ и т. д. Приобретает также смысл указание мультиплетности уровня, которая в атоме водорода всегда равнялась 2:
$$
^{2S+1}L_{J}
$$
Величина $2S+1$, как правило, совпадает с количеством подуровней в образовавшемся в результате спин-орбитального взаимодействия мультиплете, и поэтому носит название мультиплетности. Это, однако, справедливо только в случае $S \le L$, поскольку только в этом случае количество различных значений числа $J$ равно $2S+1$. В случае, если $S \ge L$, мультиплет содержит $2L+1$ подуровней.

#### Пример

Рассмотрим атом с двумя валентными электронами. Его полный спиновый момент может принимать два значения: $S = 0$ (если спиновые моменты электронов противоположно направлены) или $S = 1$ (если они сонаправлены).

В случае $S=0$: $J=L$, и мультиплетность равна 1, то есть такие уровни являются синглетами. Например, $^1S_0$, $^1P_1$, $^1D_2$ и т. д.

В случае $S=1$: $J$ может принимать три значения $L-1$, $L$, $L+1$, и соответствующий уровень представляет собой триплет. Исключение представляет собой случай $L=0$, в котором $J$ принимает только два значения $J = 0$ и $J = 1$. Соответствующие примеры: дублет $^3S_0$ и $^3S_1$, триплет $^3P_0$, $^3P_1$ и $^3P_2$, триплет $^3D_1$, $^3D_2$ и $^3D_3$ и т. д.

### Приближение j-j связи
Приближение L-S связи хорошо работает для относительно небольших атомов. С ростом числа электронов растёт размер атома, что приводит к снижению силы электростатического взаимодействия, обсуловленной также и экранировкой заряда электронами внутренних оболочек. Для тяжёлых атомов энергия электростатического взаимодействия становится меньше энергии спин-орбитального взаимодействия, и может быть применено обратное приближение, в котором полный момент импульса $\vec j_i$ отдельного электрона считается слабо зависящим от моментов импульса других электронов. Такое приближение называют приближением j-j связи.

## Правила отбора

Расщепление энергетического уровня на подуровни в результате спин-орбитального взаимодействия приводит к соответствуюшему расщеплению спектральных линий --- так называемой тонкой структуре спектра. Однако знание структуры энергетических подуровней (то есть спектральных термов) в общем случае оказывается недостаточным для определения спектра. Дело в том, что часть из возможных переходов оказываются запрещёнными законами сохранения и, в частности, законом сохранения момента импульса. Правила, которые определяют, какие переходы разрешены, а какие запрещены, называют правилами отбора.

Это связано с тем, что момент импульса излучаемого или поглощаемого фотона ограничен. Фотон в этих процессах, как правило, не приобретает орбитального момента импульса, однако, аналогично электрону обладает спиновым моментом импульса. Но в отличии от электрона спин фотона равен $\hbar$.

Запишем закон сохранения момента импульса для процесса излучения:
$$
\vec J = \vec J^{\prime} + \vec s_{\textrm ф}
$$
где $\vec J$, $\vec J^{\prime}$ --- полные моменты импульса атома соответственно до и после акта излучения, $\vec s_{\textrm ф}$ --- спиновый момент импульса фотона.

Отметим сразу, что из этого закона сохранения следует невозможность так называемых 0-0 переходов между состояниями с $J=0$ и $J^{\prime}=0$, поскольку в этом случае требовалось бы равенству нулю и спина фотона, что невозможно.

Для остальных случаев найдём правила отбора на основе нестрогого, но наглядного метода векторных диаграмм.

Пусть для определённости $|\vec J^{\prime}| \ge |\vec J|$. Тогда из неравенства треугольника имеем:
$$
|\vec J^{\prime}| \le |\vec J| + |\vec s_{\textrm ф}|
$$
Применяя правила квантования для моментов импульса, получаем:
$$
\sqrt{J^{\prime}(J^{\prime}+1)} \le \sqrt{J(J+1)} + \sqrt{s_{\textrm ф}(s_{\textrm ф}+1)}
$$
где $J$, $J^{\prime}$ --- квантовые числа, характеризующие момент импульса атома соответственно до и после акта излучения, $s_{\textrm ф}=1$ --- спиновое квантовое число фотона.

Введём величину $\Delta J = J^{\prime} - J$, подставим $J^{\prime} = \Delta J + J$ в неравенство выше, после чего возведём его в квадрат. После несложных преобразований получаем:
$$
\Delta J^2 + (2J + 1)\Delta J - 2 \le 2\sqrt{2J(J + 1)}
$$
Отметим, что в случае чётного числа электронов в атоме оба числа $J$ и $J^{\prime}$ являются целыми, а в случае нечётного числа электронов, они оба полуцелые. В обоих случаях, однако, число $\Delta J$ будет целым и в силу первоначального условия $|\vec J^{\prime}| \ge |\vec J|$ неотрицательным.

Несложно видеть, что последнее неравенство выполняется для $\Delta J = 0$ и $\Delta J = 1$ и не выполняется для $\Delta J = 2$. Кроме того, можно показать, что выражение слева в области $\Delta J > 0$ является растущей функцией величины $\Delta J$, таким образом, неравенство не будет выполняться и для всех $\Delta J \ge 2$.

Аналогично можно рассмотреть случай $|\vec J^{\prime}| \le |\vec J|$ и показать, что неравенство треугольника в этом случае выполняется только для $\Delta J = 0$ и $\Delta J = -1$. Таким образом окончательно получаем следующее правило отбора, связанное с законом сохранения момента импульса:
$$
\Delta J = 0, \pm 1
$$

Аналогичное правило отбора справедливо и для магнитного квантового числа, характеризующего проекцию момента импульса на произвольную ось. Поскольку проекция момента импульса фотона может принимать лишь значения $s_{\textrm фz} = \pm \hbar$ (значение $s_{\textrm фz} = 0$ оказывается невозможным в силу нулевой массы фотона), то и проекция момента импульса атома в процессе излучения или поглощения фотона может измениться не более чем на $\hbar$, или другими словами:
$$
\Delta m_J = 0, \pm 1
$$
Отметим, что в случае $\Delta m_J = 0$ испущенный фотон будет находиться в состоянии суперпозиции состояний с проекциями момента импульса $s_{\textrm фz} = \hbar$ и $s_{\textrm фz} = - \hbar$, так что его средняя проекция момента импульса будет равна нулю. Состояния с $s_{\textrm фz} = \hbar$ и $s_{\textrm фz} = - \hbar$ отвечают лево- и право- циркулярнополяризованным волнам, а их суперпозиция с нулевой проекцией --- линейнополяризованной волне.

Рассмотренные выше правила отбора называют строгими, однако в большинстве случаев их можно заменить более слабыми условиями, называемыми нестрогими правилами отбора. Дело в том, что спин является релятивистским эффектом, но энергия фотонов оптического диапазона (порядка 1 эВ) значительно ниже энергии покоя электрона (около 511 кэВ), поэтому изменение модуля спина в таких процессах маловероятно. Поэтому изменение полного момента импульса практически всегда связано с изменением орбитального момента импульса. Таким образом, можно сформулировать правила отбора в следующем виде:
$$
\Delta S = 0
$$
$$
\Delta L = 0, \pm 1
$$

### Замечания
1. Правила отбора справедливы только для однофотонных процессов. При одновременном излучении или поглощении двух или более фотонов ограничения, связанные с законом сохранения момента импульса, изменяются.
2. Правила отбора не распротраняются на неэлектромагнитные процессы. То есть запрещённые правилами отбора переходы могут происходить в результате электронного удара или взаимодействия с тепловыми колебаниями.
3. Интенсивность запрещённых правилами отбора линий не равна в точности нулю, однако имеет чрезвычайно малую интенсивность.