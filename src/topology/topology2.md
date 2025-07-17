# #2 閉集合・開核作用素・閉包作用素・近傍系

## 閉集合

> [!theorem] 定理2.1&emsp;閉集合
> 位相空間 $(X,\mathcal{O})$ の閉集合族 $\mathcal{A}$ において, 以下が成立する.
>
> 1. $\emptyset,X\in\mathcal{A}.$
> 1. $F_1,F_2\in\mathcal{A}\\;\Longrightarrow\\;F_1\cup F_2\in\mathcal{A}.$
> 1. $\displaystyle\forall\lambda\in\Lambda[F_\lambda\in\mathcal{A}]\\;\Longrightarrow\\;\bigcap_{\lambda\in\Lambda}F_\lambda\in\mathcal{A}.$

> [!proof]
> **1.**
>
> $\emptyset,X$ の補集合はそれぞれ $X,\emptyset$ であり, 開集合の定義より $\emptyset,X\in\mathcal{O}$ であるから
> $\emptyset,X\in\mathcal{A}.$
>
> **2.**
>
> $F_1^c,F_2^c\in\mathcal{O}\\;\Longrightarrow\\;F_1^c\cap F_2^c = (F_1\cap F_2)^c\in\mathcal{O}\\;F_1\cup F_2\in\mathcal{A}.$  
>
> **3.**
> 
> $\displaystyle\forall\lambda\in\Lambda[F_\lambda\in\mathcal{A}]
> \\;\Longrightarrow\\;\forall\lambda\in\Lambda[F_\lambda^c\in\mathcal{O}]
> \\;\Longrightarrow\\;\left(\bigcup_{\lambda\in\Lambda}F_\lambda^c\right)\in\mathcal{O}
> \\;\Longrightarrow\\;\left(\bigcap_{\lambda\in\Lambda}F_\lambda\right)^c\in\mathcal{O}
> \\;\Longrightarrow\\;\bigcap_{\lambda\in\Lambda}F_\lambda\in\mathcal{A}.$ 



## 開核作用素

> [!definition] 定義2.2&emsp;開核作用素
> 位相空間 $(X,\mathcal{O})$ において, $A$ から $A^\circ$ へ移す写像 ${}^\circ: 2^X\to2^X$ を **開核作用素** (*interior operator*)という.

> [!theorem] 定理2.3&emsp;開核作用素の性質
> 位相空間 $(X,\mathcal{O})$ の開核作用素は次の性質をもつ.
>
> 1. $X^\circ = X.$
> 1. $A^\circ \subset A.$
> 1. $(A\cap B)^\circ = A^\circ\cap B^\circ.$
> 1. $(A^\circ)^\circ = A^\circ.$

> [!proof]
> **1.**
>
> $X\in\mathcal{O}$ より, $X$ に包まれる最大の開集合 $X^\circ$ は $X$ 自身.
>
> **2.**
>
> $A^\circ$ の定義より明らか.
>
> **3.**
> 
> $A^\circ, B^\circ$ はそれぞれ $A, B$ に包まれる開集合であるから, $A^\circ \cap B^\circ$ は $A\cap B$ に包まれる開集合である.
> また, 内部の定義より $(A \cap B)^\circ$ は $A\cap B$ に包まれる最大の開集合である.
> よって, $A^\circ \cap B^\circ\subset(A \cap B)^\circ.$
>
> さらに $(A \cap B)^\circ\subset A\cap B$ であるから $(A \cap B)^\circ$ は $A$ に包まれる開集合であり,
> また $A^\circ$ は $A$ に包まれる最大の開集合であるから $A^\circ \cap B^\circ\subset A^\circ.$
> 
> 同様に $A^\circ \cap B^\circ\subset B^\circ$ が成立する. 従って $(A\cap B)^\circ = A^\circ\cap B^\circ.$
>
> **4.**
> 
> $A^\circ$ は $A$ に包まれる開集合であり、かつ $A^\circ$ に包まれる最大の開集合は $A^\circ$ であるから, $(A^\circ)^\circ = A^\circ.$

## 閉包作用素

> [!definition] 定義2.4&emsp;開核作用素
> 位相空間 $(X,\mathcal{O})$ において, $A$ から $\overline{A}$ へ移す写像 $\overline{\\;\cdot\\;}: 2^X\to2^X$ を **閉包作用素** (*closure operator*)という.

> [!theorem] 定義2.5&emsp;閉包作用素の性質
> 位相空間 $(X,\mathcal{O})$ の開核作用素は次の性質をもつ.
>
> 1. $\overline{\emptyset} = \emptyset.$
> 1. $A\subset \overline{A}.$
> 1. $\overline{A\cap B}= \overline{A}\cap \overline{B}.$
> 1. $\overline{\overline{A}} = \overline{A}.$

> [!proof]
> **1.**
>
> $\emptyset$ は閉集合より, $\emptyset$ を包む最小の開集合 $\overline{\emptyset}$ は $\emptyset$ 自身.
>
> **2.**
>
> $\overline{A}$ の定義より明らか.
>
> **3.**
> 
> $\overline{A}, \overline{B}$ はそれぞれ $A, B$ を包む閉集合であるから, $\overline{A}\cup\overline{B}$ は $A\cup B$ を包む閉集合である.
> また, 閉包の定義より $\overline{A \cup B}$ は $A\cup B$ を包む最小の閉集合である.
> よって, $\overline{A \cup B} \subset\overline{A}\cup \overline{B}.$
>
> さらに $A\cup B\subset\overline{A \cup B}$ であるから $\overline{A \cup B}$ は $A$ を包む閉集合であり,
> また $`\overline{A}$ は $A$ に包む最小の閉集合であるから $\overline{A}\subset \overline{A \cup B}.$
> 
> 同様に $\overline{B}\subset \overline{A \cup B}$ が成立する. 従って $\overline{A}\cup\overline{B}\subset \overline{A \cup B}.$
>
> **4.**
> 
> $\overline{A}$ は $A$ を包む閉集合であり、かつ $\overline{A}$ を包む最小の閉集合は $\overline{A}$ であるから, $\overline{\overline{A}} = \overline{A}.$


## 近傍系

> [!theorem] 定理2.6&emsp;近傍系の性質
> 位相空間 $(X,\mathcal{O})$ の近傍系は次の性質をもつ.
>
> 1. ${}^\forall a\in X[X\in\mathcal{N}(a) \land (N\in\mathcal{N}(a)\\;\Longrightarrow\\; a\in N)].$
> 1. $N_1,N_2\in\mathcal{N}(a)\\;\Longrightarrow\\;N_1\cap N_2\in\mathcal{N}(a).$
> 1. $(N\in\mathcal{N}(a)\land N\subset M\subset X)\\;\Longrightarrow\\;M\in\mathcal{N}(a).$
> 1. ${}^\forall N\in\mathcal{N}(a),{}^\exists M\in\mathcal{N}(a)\\;\text{s.t.}\\;b\in M\\;\Longrightarrow\\;N\in\mathcal{N}(b).$

> [!proof]
> 1, 3 は定義より明らか.
>
> **2.**
> 
> $N_1,N_2\in\mathcal{N}(a)\\;\longrightarrow\\;a\in N_1,a\in N_1,N_2\\;\Longrightarrow\\;a\in N_1\cap N_2\in\mathcal{N}(a).$
> 
> **4.**
> 
> $M$ について $M=N^\circ\in\mathcal{N}(a)$ と置けばよい.