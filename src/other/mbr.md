# 最小包含矩形問題 (Minimum bounding rectangle, MBR)

> [!note] お知らせ
> この記事は続きを書くかもしれません.  
> あるいは書かないかもしれません...

Discord で気になるトピックとして挙がったので, 少し考えてみた.

> [!question] 問題&emsp;最小包含矩形問題 (Minimum bounding rectangle, MBR)
> 2次元 Euclid 空間 $\mathbb{E}^2$ 上に 集合 $S$ が与えられたとき, 
> 1. $S$ を包む面積が最小の長方形 $R$ は存在するのはどのような場合か? 
>    - 長方形は境界も含まれるものとする.
>    - 点・線分も長方形として認め, その場合は面積0とする.
>    - 線分・辺は有限の長さを持つものとする.
> 2. 実際にそのような長方形 $R$ を有限の時間内に見つけるアルゴリズムは存在するか?

---

## 存在性

$x$ を中心とする半径 $r$ の開円板を $B(x,r)$ と表記する.

> [!theorem] 定理1&emsp;有界でない集合
> $S$ を包む長方形は存在するならば, 集合 $\overline{S}$ は有界である.

> [!proof]
> 各長方形の頂点のうち, 原点からの距離が最も大きいものの距離を $d$ とすると $\overline{S} \subset B(0, d+1)$ である.

> [!lemma] 補題2&emsp;コンパクト性
> $\overline{S}$ を包む長方形が存在するならば $\overline{S}$ はコンパクト.

> [!proof]
> $\mathbb{E}^2$ では有界閉集合とコンパクトは同値であるから, 定理1より $\overline{S}$ はコンパクトである.

> [!lemma] 補題3&emsp;閉包の包含関係
> $A\subset B \\;\Longrightarrow\\; \overline{A} \subset \overline{B}.$

> [!proof]
> $$\begin{align*}
> A \subset B
> &\\;\Longleftrightarrow\\; B^c \subset A^c \\\\
> &\\;\Longleftrightarrow\\; \operatorname{Int}(B^c) \subset \operatorname{Int}(A^c) \\\\
> &\\;\Longleftrightarrow\\; \operatorname{Int}(A^c)^c \subset \operatorname{Int}(B^c)^c \\\\
> &\\;\Longleftrightarrow\\; \overline{A} \subset \overline{B}.
> \end{align*}$$

> [!theorem] 定理4&emsp;有界な集合
> 集合 $S$ を包む最小の長方形 $R$ が存在すれば, $R$ は $S$ の閉包 $\overline{S}$ を包む最小の長方形でもある.

> [!proof]
> 補題2より, $S \subset R\\;\Longleftrightarrow\\;\overline{S} \subset \overline{R} = R$ であるから,
> $R$ は $\overline{S}$ を包む.
> 
> また, $R$ より面積の小さい $\overline{S}$ を包む長方形 $R'$ が存在すると仮定すると $S\subset\overline{S}\subset R'$ となり, $R$ が $S$ を包む最小の長方形であることに矛盾.

> [!theorem] 定理5&emsp;長方形の存在条件
> 次の2条件は同値.
> 1. $S$ を包む最小の長方形 $R$ が存在する.
> 2. $S$ は有界.

> [!proof]
> $S$ が有界であることと $\overline{S}$ が有界であることは同値であるから, (1) $\Longrightarrow$ (2) は容易に示される.  
> 
> $\pi_x, \pi_y$ をそれぞれ $x$ 座標, $y$ 座標成分の射影とする.  
> 
> $\pi_x, \pi_y$ は連続であるから $\overline{S}$ のコンパクト性より $\pi_x, \pi_y$ の像は最大値・最小値を持つ.
> よって,
> $$[\min_{a\in S}\pi_x(a), \max_{a\in S}\pi_x(a)]\times[\min_{a\in S}\pi_y(a), \max_{a\in S}\pi_y(a)]$$
> が辺が $x$ 軸および $y$ 軸に平行なものに限定したときの $S$ を包む最小の長方形である.
>
> $a = (x,y)$ とするとき, $R(\theta,a) = R_\theta(a) = (x\cos\theta - y\sin\theta, x\sin\theta + y\cos\theta)$ は原点を中心に $a$ を $\theta$ 回転させる.
> 各 $\theta$に対して $R_{\theta}$ はコンパクトであり, $R$ は連続であるから, $R(\theta,a)$ を最小にするような $\theta, a$ が存在する.

---

ここまでは存在性の話なので, ここからは具体的な長方形の構成について考える.
定理4から閉集合 (閉包) のみを議論すれば十分なので, 以降の $S$ は有界閉集合に限定する.

---

## その他の性質

> [!theorem] 定理6&emsp;凸包
> 有界閉集合 $S$ を包む最小の長方形 $R$ は凸包 $\operatorname{Conv}(S)$ を包む最小の長方形でもある.

> [!proof]
> $R$ は閉包なので, $S$ 上の任意の2点 $a,b$ を結ぶ線分を含む.

> [!theorem] 定理7&emsp;長方形と凸包の接触
> 有界閉集合 $S$ を包む最小の長方形 $R$ の各辺 (各端も含む) は凸包 $\operatorname{Conv}(S)$ の境界点を少なくとも1点を含む.

> [!proof]
> 辺 $l$が $S$ とどの境界点とも接しないと仮定すると, $S$ の任意の境界点が $l$ から $\varepsilon$ 以上離れているような実数 $\varepsilon >0$ が存在する.
> しかし辺 $l$ を長方形の重心の方向へ $\varepsilon$ 平行移動しても $S$ を包むので矛盾. 

> [!theorem] 定理8&emsp;凸包の境界
> $\partial\operatorname{Conv}(S)$ は弧状連結.

> [!info] 証明について
> GPT 曰く
> 
> > Victor Klee, Some topological properties of convex sets, Trans. Amer. Math. Soc., volume 93, 1959, pp. 52-63
> 
> の Klee の定理により示されるらしいが, ネットで調べても該当部分のページが見つからない...
>
> 証明できる人いたら教えてください!

