# #1 位相空間と諸概念の定義

> **お知らせ**  
> このページは未完成です！（現在執筆中）

> [!claim] 位相空間のモチベーション
> Euclid空間 $\mathbb{R}^n$ などの空間は連続や収束・発散、開集合・閉集合・閉包などの概念があるが、
> これらの定義は実数に依存したものになっているので, そのままでは他の空間に適用することができない.  
> 
> そこで, より一般的な空間に対しても同様の概念を扱えるように抽象化した空間が位相空間である.
> 
> まずは位相空間の性質を学ぶ前に基本的な定義を覚えておこう.

---

## 位相空間・開集合

> [!definition] 定義1.1&emsp;開集合による位相空間の定義
> $X$ を空でない集合とする.
> 集合族 $\mathcal{O}\subset 2^X$ が次の3条件を満たすとき, $\mathcal{O}$ は集合 $X$ 上の **位相** (*topology*) であるという.
>
> 1. $\emptyset\in\mathcal{O},\\;X\in\mathcal{O}.$
> 1. $O_1,O_2\in\mathcal{O}\\;\Longrightarrow\\;O_1\cap O_2\in\mathcal{O}.$
> 1. $\displaystyle\forall\lambda\in\Lambda[O_\lambda\in\mathcal{O}]\\;\Longrightarrow\\;\bigcup_{\lambda\in\Lambda}O_\lambda\in\mathcal{O}.$
>
> 位相 $\mathcal{O}$ を与えられた集合 $X$  を **位相空間** (*topology space*) といい, $(X, \mathcal{O})$ で表す.
>
> $\mathcal{O}$ に属する $X$ の部分集合 $O$ を **開集合** (*open set*), あるいは厳密に **$\mathcal{O}$-開集合** (*$\mathcal{O}$-open set*) といい,  
> 集合 $X$ を **台集合** (*underlying set*), あるいは単に **台** という.  
>
> また, 集合 $X$ の元を **点** (*point*) という.

> [!remark] 注意
> 条件2はあるいは次のように置き換えることができる.
> $$O_1,O_2,\dots,O_n\in\mathcal{O}\\;\Longrightarrow\\;\bigcap_{k=1}^{n} O_k\in\mathcal{O}.$$
> ただし, 条件3は開集合が無限個でも構わないのに対して, 条件2の開集合の共通集合は **有限個** でなければならない.

> [!remark] 注意
> 文脈から位相の集合族 $\mathcal{O}$ が明らかな場合は, 位相空間 $(X,\mathcal{O})$ を単に $X$ と略記する場合がある.


> [!example] 例1.2&emsp;密着位相
> $\mathcal{O}=\\{\emptyset,X\\}$ は位相の定義から明らかに集合 $X$ 上の一つの位相になる.  
> この位相を **密着位相** (*indiscrete space*) という.

> [!example] 例1.3&emsp;離散位相
> $\mathcal{O}=2^X$ は位相の定義から明らかに集合 $X$ 上の一つの位相になる.  
> この位相を **離散位相** (*discrete space*) という.

> [!example] 例1.4&emsp;通常の位相 (自然な位相)
> $n$次元Euclid空間 $\mathbb{R}^n$ の開集合系 $\\mathcal{O}$ は $\mathbb{R}^n$ 上の一つの位相である.  
> この位相を $\mathbb{R}^n$ の**通常の位相** (*standard topology*, または **自然な位相**, *natural topology*) という.

> [!example] 例1.5&emsp;距離位相
> 距離空間 $(X, d)$ の開集合系 $\\mathcal{O}$ は $X$ 上の一つの位相である.  
> この位相を $X$ の $d$ によって定まる **距離位相** (*metric topology*) という.
>
> 集合 $X$ 上の位相 $\mathcal{O}$ と一致するような距離位相が存在するとき, 位相 $\mathcal{O}$ は **距離化可能** (*metrizable*) であるという

> [!example] 例1.6&emsp;相対位相
> $(X,\mathcal{O})$ を位相空間, $A\subset X$ を空でない部分集合としたとき, 
> $$\mathcal{O}_A = \{A\capU \mid U\in\mathcal{O}\}$$
> は $A$ 上の一つの位相であり, この位相 $\mathcal{O}_A$ を集合 $A$ の上の $\mathcal{O}$ に関する **相対位相** (*subspace topology*, *relative topology*, or *induced topology*) という.
> 
> 位相空間 $(A, \mathcal{O}_A)$ を位相空間 $(X, \mathcal{O})$ の **部分空間** (*subspace*) という.

---

## 閉集合

> [!definition] 定義1.7&emsp;閉集合
> 位相空間 $(X, \mathcal{O})$ において, 部分集合 $F\in X$ の補集合 $F^c:=X-F$ が $\mathcal{O}$ に属するとき, 
> $F$ を **閉集合** (*closed set*), あるいは厳密に **$\mathcal{O}$-閉集合**, (*$\mathcal{O}$-closed set*) という.

> [!remark] 注意
> 部分集合 $A\in X$&emsp;が開集合に属さないからといって, 閉集合に属する**とは限らない** (逆も然りである).
> 
> 例えば, 位相空間 $(X, \mathcal{O})$ において, 空集合 $\emptyset$ と $X$ は各定義から開集合であり, また閉集合でもある (**開かつ閉集合**, *clopen set*).


---

##  内部(開核)・内点, 閉包・触点, 外部・外点, 境界・境界点

以降, 位相空間 $(X,\mathcal{O})$ について考える.

> [!definition] 定義1.8&emsp;内点, 内部 (開核)
> $A\subset X$ に包まれる最大の $\mathcal{O}$-開集合を $A$ の **内部** (*interior*, あるいは **開核**) といい,
> $A^i,\\;\operatorname{int}(A),\\;\operatorname{Int}(A),$  あるいは $A^\circ$で表す.  
> 
> $A^i$ の点を $A$ の **内点** (*interior point*) という.

> [!definition] 定義1.9&emsp;閉包, 触点
> $A\subset X$ を包む 最小の $\mathcal{O}$-閉集合を $A$ の **閉包** (*closure*) といい,  
> $A^a,\\;\operatorname{cl}(A),\\;\operatorname{Cl}(A),$ あるいは $\overline{A} $で表す.
>   
> $A^i$ の点を $A$ の **触点** (*closure point*) という.

> [!definition] 定義1.10&emsp;外部, 外点
> $A\subset X$ の補集合 $A^c$ の内部 $(A^c)^i$ を $A$ の **外部** (*exterior*) といい,   
> $A^f,\\;\operatorname{ext}(A),$ または $\operatorname{Ext}(A)$ で表す.
>  
> $A^f$ の点を $A$ の **外点** (*exterior point*) という.

> [!definition] 定義1.11&emsp;境界, 境界点
> $A\subset X$ で $A$ の内部でも外部でもない点全体の集合 $A-(A^i\cup A^e)^c$ を $A$ の **境界** (*boundary*, *frontior*) といい,  
> $A^f,\\;\operatorname{bd}(A),\\;\operatorname{fr}(A),$ または $\partial A$ で表す.
>  
> $A^f$ の点を $A$ の **境界点** (*exterior point*) という.