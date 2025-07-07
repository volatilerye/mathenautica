# 主成分分析と固有値・固有ベクトルの関係

>
> **お知らせ**  
> このページは未完成です！（現在執筆中）

> [!note] 前提知識
> **主成分分析** (*principal component analysis; PCA*) は学習データの次元 (変数) を削減することで,
> 回帰・分類問題の計算量を抑える手法である.
>
> 主成分分析に明るくない読者は, パターン認識に関する文献を参照されたい.

> [!question] 主成分分析への疑問
> 主成分分析は $k$ 番目に大きい固有値に対応する固有値ベクトルを第 $k$ 主成分とすることで,  
> 学習データの分散が最大になるような線形変換を求めることができる.
> 
> しかし, なぜここで固有値・固有ベクトルが現れるのか？ その理由を実際に計算して理解しよう.

---

## 固有値と諸性質

> [!definition] 定義1&emsp;固有値・固有ベクトル
> 体 $K$ 上の $n$ 次正方行列 $A$ に対して 
> $$\begin{equation}A\bm{x}=\lambda\bm{x}\end{equation}$$
> であるような $\lambda\in K$ と $\bm{x}\in K^n-\\{\bm{0}\\}$ が存在するとき,   
> $\lambda$ を **固有値** (*eigenvalue*), $\bm{x}$ を **固有ベクトル** (*eigenvector*) という.

> [!Theorem] 定理2&emsp;固有値の求め方
> $\lambda$ が固有値であるための必要十分条件は $\det(A-\lambda E) = 0$ である ($E$ は単位行列).

> [!proof]
> 式1より, $A\bm{x}=\lambda\bm{x}
> \\;\Longleftrightarrow\\;
> (A-\lambda E)\bm{x}=\bm{0}.$  
> 正則行列の性質より, $A\bm{x}=\bm{0}$ が自明な解$\bm{x}=0$ のみを持つことと $A$ が正則であることは同値であるから, $(A-\lambda E)\bm{x}=\bm{0}\\;\Longleftrightarrow\\;\det(A-\lambda E)=0.$ 

> [!corollary] 系3&emsp;固有値・固有ベクトルの存在
> - $n$ 次実行列は重複度を含め固有値を 0 個以上 $n$ 個以下持つ.
> - $n$ 次複素行列は重複度を含め固有値を $n$ 個持つ.

> [!proof]
> $n$ 複正方素行列の行列式 $\det(A-\lambda E)$ は $n$ 次方程式なので, 
> 代数学の基本定理より重複度を含め根 (固有値) を $n$ 個持つ.
>
> 実正方行列の場合は複素数から実数に $\lambda$ の定義域を縮小すればよい.



> [!acknowledgment] 参考文献
> - 書籍
>   - 平井 勇三. はじめてのパターン認識, 森北出版株式会社. 2012.
>   - Christopher M. Bishop. パターン認識と機械学習 上, 元田 浩, 丸善出版. 2012
>   - Christopher M. Bishop. パターン認識と機械学習 下, 元田 浩, 丸善出版. 2012
> - Website
>   - [主成分分析 - Wikipedia](https://ja.wikipedia.org/wiki/主成分分析)
