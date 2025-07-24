# 積位相のコンパクト性と Tychonoff の定理

## Tychonoff の定理の主張

> [!theorem] 定理1&emsp;Tychonoff の定理
> 空でない位相空間族 $\\{(X_\lambda,\mathcal{O}_\lambda)\\}\_{\lambda\in\Lambda}$ が全てコンパクトならば, その直積空間もまたコンパクトである.

### 証明したいこと

> [!info] 証明事項
> 1. $\operatorname{card}\Lambda < \aleph_0$ のとき, Tychonoff の定理は (選択公理を仮定しなくても) 成立する.
> 1. 選択公理を認めると Tychonoff の定理は ( $\Lambda$ の濃度に依らず) 成立する.
> 1. 選択公理と Tychonoff の定理は同値である.

---

## 復習

> [!definition] 定義2&emsp;直積位相
> 空でない位相空間族 $\\{(X_\lambda,\mathcal{O}\_\lambda)\\}\_{\lambda\in\Lambda}$ において, 任意の $\lambda\in\Lambda$ で射影 $\pi_\mu: \prod_{\lambda\in\Lambda} X_\lambda \to X_\mu$ が連続となるような $\prod_{\lambda\in\Lambda}$ の位相の中で最弱な位相 $\mathcal{O}$ を $\\{\mathcal{O}\_\lambda\\}\_{\lambda\in\Lambda}$ の **直積位相** (*product topology*) といい,   
> 位相空間 $(\prod_{\lambda\in\Lambda} X_\lambda, \mathcal{O})$ を $\\{(X_\lambda,\mathcal{O}\_\lambda)\\}_{\lambda\in\Lambda}$ の **直積空間** (*product space*) という.
>
> また, 各位相空間 $(X_\lambda, \mathcal{O}_\lambda)$ を **因子空間** (*factor space*) という.


> [!theorem] 定理3&emsp;直積位相の同値な定義
> 空でない位相空間族 $\\{(X_\lambda,\mathcal{O}\_\lambda)\\}\_{\lambda\in\Lambda}$ の各射影を $\pi_\mu: \prod_{\lambda\in\Lambda} X_\lambda \to X_\mu$ としたとき, 
>$$\mathscr{S} = \\{ \pi_\lambda^{-1}(V_\lambda) \mid V_\lambda \in \mathcal{O}\_\lambda, \lambda\in\Lambda \\}$$
>
> によって生成される位相は直積 $X = \prod_{\lambda\in\Lambda} X_\lambda$ の直積位相である.

> [!proof-without-details] 証明
> 各射影 $\pi_\lambda$ が位相空間 $(\prod_{\lambda\in\Lambda} X_\lambda,\mathcal{O})$ から位相空間 $(X_\lambda,\mathcal{O}_\lambda)$ への連続写像であるならば, $\mathscr{S} \subset\mathcal{O}$ である.

> [!definition] 定義4&emsp;被覆
> 集合 $X$ と $X$ の部分集合 $A$ に対して,
> $2^X$ の部分集合族 $\mathscr{G}$ が
> $A\subset\bigcup_{\mathscr{G}} G$
> を満たすとき, $\mathscr{G}$ は $A$ を **被覆する** (*cover*), あるいは **覆う** といい, $\mathscr{G}$ は $A$ の **被覆** (*covering*) であるともいう.
>
> $A$ の被覆 $\mathscr{G}$ の部分集合 $\mathscr{G}'$ に対しても
> $A\subset\bigcup_{G'\in\mathscr{G}'} G'$
> であるとき, $\mathscr{G}'$ を $\mathscr{G}$ の **部分被覆** (*subcover*) という.
>
> 特に, 位相空間 $(X, \mathcal{O})$ と $X$ の部分集合 $A$ に対して, 位相 $\mathcal{O}$ の部分集合族 $\mathscr{G}$ が $A$ を被覆するとき, $\mathscr{G}$ を $A$ の **開被覆** (*open cover*) という.

> [!definition] 定義5&emsp;コンパクト性
> 集合 $X$ と $X$ の部分集合 $A$ に対して, $A$ の開被覆が有限な部分被覆を持つとき, $A$ は **コンパクト集合** (*compact set*), あるいは **コンパクト** (*compact*) であるという.
>
> 特に, 位相空間 $(X, \mathcal{O})$ に対して, $X$ 自身がコンパクトであるとき, $(X, \mathcal{O})$ は **コンパクト空間** (*compact space*),　あるいは **コンパクト** (*compact*) であるという.

> [!definition] 定義6&emsp;有限交差性
> 集合 $X$ の部分集合族 $\mathscr{A}$ が **有限交差性** (*finite intersection property*) を持つとは,  
> 任意の有限個の集合 $A_1, \dots,A_n\in\mathscr{A}$ に対して常に $\bigcap_{k=1}^n A_k \neq \emptyset$ を満たすことである.

> [!definition] 定理7&emsp;コンパクト性と有限交差性
> 位相空間 $(X, \mathcal{O})$ において, 次の2つの条件は同値である.
> 1. $(X, \mathcal{O})$ はコンパクト.
> 2. $(X, \mathcal{O})$ の閉集合族 $\mathcal{A}$ が有限交差性を持つならば $\bigcap{\mathscr{A}}\neq\emptyset$.

> [!proof-without-details] 証明
> $\Longrightarrow)$
> 
> $(X, \mathcal{O})$ の閉集合族 $\mathscr{A}$ に対して, 開集合族を $\mathscr{A}^c = \\{F^c\mid F\in\mathscr{A}\\}$ で定義する. 
> コンパクト性より, 適当に $F_1^c,\dots, F_n^c \in \mathscr{A}^c$ を選んで $X=\bigcup_{k=1}^n F_k^c$ とできるので, De Morgan の法則より $\bigcap_{k=1}^n F_k = \emptyset$.
> 
> $\Longleftarrow)$
>
> $(X, \mathcal{O})$ の開集合族 $\mathscr{G}$ に対して, 閉集合族を $\mathscr{G}^c = \\{O^c\mid O\in\mathscr{G}\\}$ で定義する.
> $\mathscr{G}$ が $X$ の開被覆であれば, De Morgan の法則より $\bigcap(\mathscr{G}^c) = \emptyset$.
> 条件2の対偶より, 適当に $O_1^c,\dots, O_n^c \in \mathscr{G}^c$ を選んで, $\bigcap_{k=1}^n O_k^c=\emptyset$ とできるので, 再び De Morgan の法則より $X=\bigcup_{k=1}^n O_k.$

---

## Tychonoff の定理の証明

### $\operatorname{card}\Lambda < \aleph_0$ のとき　(選択公理を必要としない証明) 

> [!proof-without-details] 証明
> 2つのコンパクト空間をそれぞれ $(X_1, \mathcal{O}_1), (X_2, \mathcal{O}_2)$ とし, 直積空間を $(X,\mathcal{O})$ とする.
>
> $X_1\times X_2$ の開被覆 $\mathscr{G}$ を任意に与えたとき, $\mathscr{G}_1,\mathscr{G}_2(x)$ をそれぞれ
>
> $$\mathscr{G}\_1 = \left\\{O\in\mathcal{O}\_1 \\;\middle|\\; {}^\exists n\in\mathbb{N}, {}^\exists U_1,\dots,U_n\in\mathscr{G} \\;\text{s.t.}\\;O\times X_2\subset \bigcup_{i=1}^{n}U_i\right\\},$$
> 
> $$\mathscr{G}_2(x) = \left\\{O\in\mathcal{O}\_2 \middle| x\in {}^\exists U\in\mathcal{O}\_1, {}^\exists G\in\mathscr{G} \\;\text{s.t.}\\; U\times O\subset G\right\\}$$
>
> と定義する.
>
> 積位相の定義および $\mathscr{G}$ が直積 $X_1\times X_2$ の開被覆であることから, $\mathscr{G}\_2(x)$ は $X_2$ の開被覆である.
> $(X_2,\mathcal{O}\_2)$ はコンパクト空間なので, $\mathscr{G}\_2(x)$ に属する有限個の開集合 $V_1,\dots,V_m$ を適当に選ぶことで,
> $X_2 = \bigcup_{i=1}^{m}V_i$ となるようにできる. $\mathscr{G}\_2(x)$ の定義より, 点 $x$ の $\mathcal{O}\_1$-開近傍 $U_1,\dots,U_m$ と $\mathscr{G}$ に属する開集合を適当に選び,
> $U_i\times V_i\subset G_i\\;(i=1,\dots,m)$ となるようにできる.
> そこで, $O=\bigcap_{i=1}^{m}U_i$ とすれば, $O$ は点 $x$ の開近傍で, 
> $$O\times X_2 = \bigcup_{j=1}^{m}(O\times V_j) = \bigcup_{i=1}^{m}\bigcap_{j=1}^{m}(U_i\times V_j) \subset \bigcup_{i=1}^{m}G_i$$
> より $O\times X_2$ は $G_1,\dots,G_m$ によって被覆できる.
>
> 従って, このように定義された点 $x$ の $\mathcal{O}\_1$-開近傍 $O$ は先に定義した $\mathscr{G}\_1$ に属することになり, $\mathscr{G}\_1$ は $X_1$ の開被覆となる.
> $(X_1,\mathcal{O}\_1)$ もコンパクト空間であるから, $\mathcal{O}\_1$ に属する有限個の開集合 $O_1,\dots,O_n$ を適当に選ぶことで,
> $X_1 = \bigcup_{i=1}^{n}O_i$ となるようにできる. 各番号 $i$ に対して, 直積 $O_i\times X_2$ は $\mathscr{G}$ に属する有限個の開集合によって被覆されるので
> その和集合
> $ X_1 \times X_2 = \bigcup_{i=1}^{n}\left(O_i\times X_2\right)$
> もまた $\mathscr{G}$ に属する有限個の開集合によって被覆される.
>
> 以上より, 2つのコンパクト空間の直積空間はコンパクトであることが示された.
> 3個以上の因子空間からなる直積空間は上記の議論を帰納的に繰り返すことで示せる.

### $\Lambda$ が任意の濃度のとき　(選択公理を仮定する証明)

> [!proof-without-details] 証明
> 以降, $(X,\mathcal{O}) = \prod_{\lambda\in\Lambda}(X_\lambda, \mathcal{O}_\lambda)$ としよう.
>
> 有限交差性を持つ $X$ の部分集合族 $\mathscr{A}'$ で $\mathscr{A}\subset\mathscr{A}'$ となるような $\mathscr{A}$ 全体を $\mathscr{F}$ とする.
> 集合 $\mathscr{F}$ は包含関係による半順序に関して帰納的 (全ての全順序部分集合が上限を持つ) であるので,
> Zorn の補題より $\mathscr{F}$ の極大元 $\mathscr{M}$ が存在する. 有限交差性と極大性より, $\mathscr{M}$ は次の性質を持つ.
>
> - 任意の有限個の集合 $F_1,\dots,F_n\in\mathscr{M}$ に対して $\bigcap_{k=1}^n F_k\in\mathscr{M}$.
> - 部分集合 $A\subset X$ が $\mathscr{M}$ に属するすべての集合と交わるならば $A\in\mathscr{M}.$
>
> ($\star$) ここで, ${}^\forall F\in\mathscr{M}, {}^\forall\lambda\in\Lambda,{}^\exists x=(x_\lambda)\in X\\;\text{s.t.}\\;x_\lambda\in \overline{\pi_\lambda(F)}$ を示す.
>
> $\mathscr{M}\_\lambda = \left\\{\overline{\pi_\lambda(F)} \middle| F\in\mathscr{M}\right\\}$ とすれば,
> $\mathscr{M}\_\lambda$ はコンパクト空間 $(X_\lambda, \mathcal{O}\_\lambda)$ における有限交差性をもつ閉集合族であるから, $\bigcap\mathscr{M}\_\lambda\neq\emptyset.$
> よって, 選択公理より $x$ の存在性が示せた.
>
> ($\star\star$) 次に, 先ほど求めた点 $x$ は $\mathscr{M}$ に属するすべての集合の触点であることを示す.
>
> これは直積位相 $(X,\mathcal{O})$ における点 $x$ の近傍 $N$ が $\mathscr{M}$ に属するすべての集合と交わることを示せばよい.
>
> 直積位相の定義より, 有限個の添字 $\lambda_1,\dots,\lambda_n$ および $\mathcal{O}\_{\lambda_i}$-開集合$U_i\\;(i=1,\dots,n)$ が存在して,
> $$x\in\bigcap_{i=1}^{n}\pi_{\lambda_i}^{-1}(U_i)\subset N$$
> が成立する (ここで, $U_{i}$ は $x_{\lambda_i}=\pi_{\lambda_i}(x)$ の開近傍である). 
> もし $\pi_{\lambda_i}^{-1}(U_i)\in\mathscr{M}\;(i=1,\dots,n)$ ならば, 性質1より
> $${}^\forall F\in\mathscr{M}\left[F\cap\left(\bigcap_{i=1}^{n}\pi_{\lambda_i}^{-1}(U_i)\right)\neq\emptyset\right]$$
> が成立することから($\star\star$) が示される.
>
> ($\star\star\star$) 最後に, $(X, \mathcal{O})$ の点 $x_\lambda=\pi_\lambda(x)$ の開近傍 $U$ に対して $\pi_\lambda^{-1}(U)\in\mathscr{M}$ であることを示す.
> 
> ($\star$) より $U\cap\pi_\lambda(F)\neq\emptyset$ であり, $\pi_\lambda^{-1}(U)\cap F\neq\emptyset.$ 性質2より, $\pi_\lambda^{-1}(U)\in\mathscr{M}$.
> 
> 以上より, $\mathscr{M}$ に属するすべての集合の触点となる $Y$ の点 $y$ が存在する.
>  最初に与えた閉集合族 $\mathscr{A}$ は $\mathscr{M}$ の部分集合だから, $y$ は $\mathscr{A}$ に属するすべての閉集合に含まれることになり, $\cap\mathscr{A}\neq\emptyset$ が示された.

---

## 選択公理と Tychonoff の定理の同値性

> [!lemma] 補題8&emsp;有限集合を含む集合族の有限交差性
> $\mathscr{A}$ をある集合の部分集合族とし, その中に有限集合 $A$ が含まれているとする.
> このとき, $\mathscr{A}$ が有限交差性を持てば $\bigcap\mathscr{A}\neq\emptyset$ である.

> [!proof-without-details] 証明
> $A=\\{a_1, \dots, a_n\\}$ とする.
> もし $\bigcap\mathscr{A}=\emptyset$ ならば $a_i\notin A_i$ であるような集合 $A_1, \dots A_n\in\mathscr{A}$ が存在するので, $$A\cap\left(\bigcap_{i=1}^n A_i\right) = \emptyset$$
> となるが, これは $\mathscr{A}$ が有限交差性を持つことに矛盾する.
>
> よって, $\mathscr{A}$ が有限交差性を持てば, $\bigcap\mathscr{A}\neq\emptyset$.

> [!theorem] 定理9&emsp;Tychonoff の定理と選択公理の同値性
> Tychonoff の定理と選択公理は同値である.
>
> すなわち, 台の直積が空集合でないことが既知である直積空間に対して Tychonoff の定理が成立するならば, 選択公理が成立する.

> [!proof-without-details] 証明
> 集合族 $\\{A_\lambda\\}\_{\lambda\in\Lambda}$ において,
> ${}^\forall\lambda\in\Lambda[A_\lambda\neq\emptyset]\\;\Longrightarrow\\;\prod_{\lambda\in\Lambda}A_\lambda\neq\emptyset$ を示せばよい.
>
> まず, 和集合 $\omega\notin\bigcup_{\lambda\in\Lambda} A_\lambda$ を選び, 
> $$X_\lambda = A_\lambda\cup\\{\omega\\}\quad(\lambda\in\Lambda)$$
> とする. ${}^\forall\lambda\in\Lambda[\omega\in X_\lambda]$ であるから, $X\neq\emptyset$ (選択関数が具体的に決定するため, この主張に選択公理は必要ない).
> 次に, 各 $\mathcal{O}\_\lambda=\\{\emptyset, \\{\omega\\}\\} \cup \\{O \subset X_\lambda \mid O^c\\;\text{is finite}\\}$ とすれば,
> $\mathcal{O}\_\lambda$ は $X_\lambda$ の位相である.
>
> 補題8より, 位相空間 $(X_\lambda, \mathcal{O}\_\lambda)$ において閉集合族 $\mathscr{A}\_\lambda$ は有限交差性を持ち $\bigcap\mathscr{A}\_\lambda\neq\emptyset$ であるから, $(X_\lambda, \mathcal{O}\_\lambda)$ はコンパクト空間である.
> よって, 条件付きの Tychonoff の定理より, 積空間 $\prod_{\lambda\in\Lambda}(X_\lambda, \mathcal{O}_\lambda)$ もコンパクト空間である.
>
> $F_\lambda:=\pi_\lambda^{-1}(A_\lambda)$ は直積空間における閉集合であり, さらにこの閉集合族は直積$X$ の元 $x=(x_\lambda)$ に対して
> $x_{\lambda_i}\in A_{\lambda_i}\\;(i=1,\dots,n),\\;x_\lambda=\omega\\;(\lambda\neq\lambda_1,\dots,\lambda_n)$ となるものが存在するから,
> $\\{F_\lambda\\}_{\lambda\in\Lambda}$ は有限交差性を持つ.
>
> 従って, 定理7 より $\bigcap_{\lambda\in\Lambda} F_\lambda\neq\emptyset$.
> 一方, $F_\lambda=\pi_\lambda^{-1}(A_\lambda)$ であったから, $\bigcap_{\lambda\in\Lambda} F_\lambda=\prod_{\lambda\in\Lambda} A_\lambda\neq\emptyset.$


---

## 参考文献

- 内田伏一「集合と位相」(裳華房 数学シリーズ, 増補新装版, 2020)
- 松坂和夫「集合・位相入門」 (岩波書店 数学入門シリーズ，新装版，2018)
- 数学の景色, [https://mathlandscape.com/](https://mathlandscape.com/)