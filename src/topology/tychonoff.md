# 積位相のコンパクト性と Tychonoff の定理

> [!theorem] 定理1&emsp;Tychonoff の定理
> 空でない位相空間族 $\\{(X_\lambda,\mathcal{O}_\lambda)\\}\_\{\lambda\in\Lambda\}$ の直積空間を $(X,\mathcal{O})$ とする.
> 
> 任意の因子空間 $(X_\lambda, \mathcal{O}_\lambda)$ がコンパクト空間ならば, $(X, \mathcal{O})$ もコンパクト空間である.

> [!remark] 注意&emsp;選択公理
> 後述するが, Tychonoff の定理は**選択公理と同値**である.
> なお, $\Lambda$ が有限の濃度である場合は選択公理を用いなくても証明は可能である.

---

# 位相空間が2つのとき

> [!lemma] 補題2 Tychonoff の定理 ($\operatorname{card}\Lambda = 2$ のとき)
> $\operatorname{card}\Lambda = 2$ のとき, Tychonoff の定理は成立する.

> [!proof]
> 位相空間をそれぞれ $(X_1, \mathcal{O}_1),\\;(X_2, \mathcal{O}_2)$ としよう.  
> 直積位相 $\mathcal{O}$ は定義より $\mathcal{B}=\\{O_1\times O_2 \mid O_1\in\mathcal{O}_1, O_2\in\mathcal{O}_2\\}$ を開基とするから,
> $X_1\times X_2$ のコンパクト性を示すには $\mathcal{B}$ を要素とする開被覆が有限な部分被覆を持つことを示せば十分である.
>
> 直積 $X_1\times X_2$ の開被覆を $\mathcal{U}=\\{\mathcal{U}\_{1,\mu}\times\mathcal{U}\_{2,\mu}\mid\mathcal{U}\_{1,\mu}\in\mathcal{O}\_1,\mathcal{U}\_{2,\mu}\in\mathcal{O}\_2,\\}\_{\mu\in\Mu}$ とする. ここで, $x_1\in X_1$ を固定すると, 
> $\\{x_1\\}\times X_2$ は $X_2$ と同相であるからコンパクトであり, $\mathcal{U}$ は $\\{x_1\\}\times X_2$ の $X_1\times Y_2$ における開被覆である. よって, コンパクト性より $x$ を含む $\mathcal{O}\_1$-開集合 $O_x$ と有限個の空でない $\mathcal{O}\_2$-開集合 $O_{x,1},\dots O_{x,n}$ を選択することで,
> $$\\{x\\} \times X_2 \subset \bigcup_{i=1}^{n}(O_x\times O_{x,i})$$ 
> とできる. 
>
> さて, 