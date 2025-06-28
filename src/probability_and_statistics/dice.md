# サイコロの合計が $n$ の倍数になる確率

> [!note] 問題
> どの目も出る確率が同様に確からしい $D$ 面サイコロを $n$ 個投げた.  
> このとき, 出た目の合計が $k$ の倍数である確率 $P\_{k,n,D}$ を求めよ.

この問題は **母関数 (生成関数)** を用いるととても巧妙に一般の確率を求めることができる.

---

## 生成関数による解法

生成関数 $f(z)$ を

$$f(z) = \left\\{\frac{1}{D}\sum\_{i=1}^{D}z^i\right\\}^n$$ と定義する.
すると, $f(z)$ の $x^m$ の係数 $c_m$ は, 出た目の合計が $k$ の倍数である確率と一致する.

ここで, $1$ の $k$ 乗根を $\xi\_k$ としよう (以降, 文脈から明らかな場合は単に $\xi$ と書く).

$$\xi\_k = e^{i2\pi/k} = \cos \frac{2\pi}{k} + i\sin \frac{2\pi}{k}.$$

求めたい確率は $P\_{k,n,D} = c\_k+c\_{2k}+c\_{3k}$ であるが, $k$ 乗根 $\xi$ を使うことで,
関係ない係数 $c_m$ は上手い事にすべて除去することができる.

$$
\begin{align}
P\_{k,n,D} 
&= \frac{1}{k}\left\\{\sum\_{m=1}^{k}f(\xi^m)\right\\}  \notag \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\sum\_{i=1}^{D}\xi^{im}\right)^n\right\\} \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{Dm})(1-\xi^m)^{-1}\right\\}^n\right\\}.
\end{align}
$$


---

## 特定の条件にある場合の確率

$k, D$ が特定の条件にある場合は, $P\_{k,n,D}$ は簡単に求めることができる.

> [!important] 補題1
> $$
> \begin{align}
>     \xi^{k} &= 1, \\\\
>     \xi^{1} + \xi^{2} + \dots + \xi^{k} &= 0. \\\\
> \end{align}
> $$

> [!proof]
> 式(3) は $k$ 乗根の定義より明らか.
>
> 式(4) は
> $$
> \begin{align*}
>   &\xi^{k} = 1 \\\\
>   \Longrightarrow\\;&
>   \xi^{k} -1 = 0 \\\\
>   \Longrightarrow\\;&
>   (\xi -1)(1+\xi+\dots+\xi^{k-1}) = 0 \\\\
>   \Longrightarrow\\;&
>   1+\xi+\dots+\xi^{k-1} = 0 \\\\
>   \Longrightarrow\\;&
>   \xi+\xi^2+\dots+\xi^{k} = 0.
> \end{align*}
> $$

> [!tip] 定理2
> $k$ が $D$ の約数ならば, $P\_{k,n,D}=1/k.$

> [!proof]
> 式(2), (4)より, 
> $$
> \begin{align*}
>   P\_{k,n,D} 
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{Dm})(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m\cdot 0 \cdot(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}. \\\\
> \end{align*}
> $$

> [!tip] 定理3
> $k=D+1$ ならば, $P\displaystyle P\_{k,n,D}=\frac{1}{k}(1-(-D)^{1-n}).$

> [!proof]
> 式(2), (4)より, 
> $$
> \begin{align*}
>   P\_{k,n,D} 
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{(k-1)m})(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}(-1)^n\right\\} \\\\
>   &= \frac{1}{k}(1-(-D)^{1-n}). \\\\
> \end{align*}
> $$

---

## 計算量を削減する方法の検討

定理2, 3 の条件に該当しない場合, 簡単に $P\_{k,n,D}$ を導出する方法は (おそらく) ないと思う.
ここでは, 少しでも計算量を削減するための工夫を考えよう.

改めて, 確率 $P\_{k,n,D}$ の確率は

$$P\_{k,n,D} = \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{Dm})(1-\xi^m)^{-1}\right\\}^n\right\\}$$

であった. ここで $|z|=e^{i\theta},\\;z\neq1,\\;\theta\in\mathbb{R}$ としたとき,

$$
\begin{align*}
|1-z|^2 &= (1-z)\overline{(1-z)} \\\\
&= (1-z)(1-\overline{z}) \\\\
&= 1 - (z + \overline{z}) \\\\
&= 1 - 2\cos\theta,
\end{align*}
$$

$$
\begin{align*}
\arg(1-z)
&= \frac{1}{2}\arg(1-z)^2 \\\\
&= \frac{1}{2}\arg\left(\frac{1-z}{|1-z|}\right)^2 \\\\
&= \frac{1}{2}\arg\frac{1-z}{1-\overline{z}}.
\end{align*}
$$

> [!default] draft
> 続きを執筆中です...