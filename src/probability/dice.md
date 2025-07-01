# サイコロの合計が $n$ の倍数になる確率

> [!note] 問題
> どの目も出る確率が同様に確からしい $D$ 面サイコロを $n$ 個投げた.  
> このとき, 出た目の合計が $k$ の倍数である確率 $P\_{n,k,D}$ を求めよ.

この問題は **母関数 (生成関数)** を用いるととても巧妙に一般の確率を求めることができる.

---

## 生成関数による解法

生成関数 $f(z)$ を

$$f(z) = \left\\{\frac{1}{D}\sum\_{j=1}^{D}z^i\right\\}^n$$ と定義する.
すると, $f(z)$ の $x^m$ の係数 $c_m$ は, 出た目の合計が $k$ の倍数である確率と一致する.

ここで, $1$ の $k$ 乗根を $\xi\_k$ としよう (以降, 文脈から明らかな場合は単に $\xi$ と書く).

$$\xi\_k = e^{i2\pi/k} = \cos \frac{2\pi}{k} + i\sin \frac{2\pi}{k}.$$

求めたい確率は $P\_{n,k,D} = c\_k+c\_{2k}+c\_{3k}$ であるが, $k$ 乗根 $\xi$ を使うことで,
関係ない係数 $c_m$ は上手い事にすべて除去することができる.

$$
\begin{align}
P\_{n,k,D} 
&= \frac{1}{k}\left\\{\sum\_{m=1}^{k}f(\xi^m)\right\\}  \notag \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\sum\_{j=1}^{D}\xi^{jm}\right)^n\right\\} \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{Dm})(1-\xi^m)^{-1}\right\\}^n\right\\}.
\end{align}
$$


---

## 特定の条件にある場合の確率

$k, D$ が特定の条件にある場合は, $P\_{n,k,D}$ は簡単に求めることができる.

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
> $k$ が $D$ の約数ならば, $P\_{n,k,D}=1/k.$

> [!proof]
> 式(2), (4)より, 
> $$
> \begin{align*}
>   P\_{n,k,D} 
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{Dm})(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m\cdot 0 \cdot(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}. \\\\
> \end{align*}
> $$

> [!tip] 定理3
> $k=D+1$ ならば, $\displaystyle P\_{n,k,D}=\frac{1}{k}(1-(-D)^{1-n}).$

> [!proof]
> 式(2), (4)より, 
> $$
> \begin{align*}
>   P\_{n,k,D} 
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left\\{\xi^m(1-\xi^{(k-1)m})(1-\xi^m)^{-1}\right\\}^n\right\\} \\\\
>   &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}(-1)^n\right\\} \\\\
>   &= \frac{1}{k}(1-(-D)^{1-n}). \\\\
> \end{align*}
> $$

---

## 計算量を削減する

定理2, 3 の条件に該当しない場合, 簡単に $P\_{n,k,D}$ を導出する方法は (おそらく) ないと思う.
ここでは, 少しでも計算量を削減するための工夫を考えよう.

> [!important] 補題4
> $\theta\in\mathbb{R},\\;e^{i\theta}\neq1$ のとき,
> $$\sum_{k=1}^{n} e^{ik\theta} = \frac{\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}e^{i(n+1)\theta/2}.$$

> [!proof]
> [$\sum_{k=0}^{n}\sin k\theta, \sum_{k=0}^{n}\cos k\theta$](../analysis/sum_sin_cos.md) のときと同様である.

補題4より,

$$
\begin{align*}
P\_{n,k,D} 
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\sum\_{j=1}^{D}\xi^{jm}\right)^n\right\\} \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\sum\_{j=1}^{D}e^{ij\frac{2m\pi}{k}}\right)^n\right\\} \\\\
&= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\frac{\sin\frac{Dm\pi}{k}}{\sin\frac{m\pi}{k}}e^{i(D+1)m\pi/k}\right)^n\right\\}.
\end{align*}
$$

更に, 虚部は $m=1,k-1$ や $m=2,k-2$ などの 合計が $k$ になる組で打ち消しあうことに注意すれば, 総和記号を削減して三角関数に置き換えることができる.

> [!tip] 定理5
> どの目も出る確率が同様に確からしい $D$ 面サイコロを $n$ 個投げたときの出た目の合計が $k$ の倍数である確率を $P\_{n,k,D}$ とすれば, 
> $$
> \begin{align*}
> P\_{n,k,D} 
> &= \frac{1}{k}\left\\{1+D^{-n}\sum\_{m=1}^{k-1}\left(\frac{\sin\frac{Dm\pi}{k}} {\sin\frac{m\pi}{k}}\right)^n\cos\frac{(D+1)mn\pi}{k}\right\\} \\\\
> &= \begin{cases}
> \frac{1}{k}\left\\{1+2D^{-n}\sum\_{m=1}^{k/2 -1}\left(\frac{\sin\frac{Dm\pi}{k}}{\sin\frac{m\pi}{k}}\right)^n\cos\frac{(D+1)mn\pi}{k} + D^{-n}{\sin^n\frac{D\pi}{2}}\cos\frac{(D+1)n\pi}{2}
> \right\\}  & \text{if $k$ is even,}\\\\
> \frac{1}{k}\left\\{1+2D^{-n}\sum\_{m=1}^{(k-1)/2}\left(\frac{\sin\frac{Dm\pi}{k}}{\sin\frac{m\pi}{k}}\right)^n\cos\frac{(D+1)mn\pi}{k} \right\\} & \text{if $k$ is odd.}
> \end{cases} \\\\
> \end{align*}
> $$

---

## 例: $D=6$ のとき

実際に6面サイコロが2から10までの倍数である確率を実際に計算して求めてみよう.

$$
P\_{n,k,6} 
= \frac{1}{k}\left\\{1+2\cdot6^{-n}\sum\_{m=1}^{\lceil{k/2}\rceil-1}\left(\frac{\sin\frac{6m\pi}{k}} {\sin\frac{m\pi}{k}}\right)^n\cos\frac{7mn\pi}{k}\right\\}.
$$

$k=2,3,6$ のときは定理2, $k=7$ のときは定理3が適用できることにも注意する.

> [!caution] 注意
> $(-1)^n=\cos n\pi,\\;-\cos(x) = \cos(x+n\pi)$ を使うことで, より式を簡潔にできる場合がある.

|$k$|$P_{n,k,6}$|
|--|--|
|2|$\displaystyle\frac{1}{2}$|
|3|$\displaystyle\frac{1}{3}$|
|4|$\displaystyle\frac{1}{4}\left\\{1+2\left(\frac{\sqrt{2}}{6}\right)^n\cos\frac{3n\pi}{4}\right\\}$|
|5|$\displaystyle\frac{1}{5}\left\\{1+2\cdot6^{-n}\left(\cos\frac{2n\pi}{5}+\cos\frac{4n\pi}{5}\right)\right\\}$|
|6|$\displaystyle\frac{1}{6}$|
|7|$\displaystyle\frac{1}{7}\left\\{1-(-6)^{1-n}\right\\}$|
|8|$\displaystyle\frac{1}{8}\left\\{1+2\left(\frac{\sqrt{2}}{6}\right)^n\cos\frac{3n\pi}{8}+2\left(\frac{\sqrt{2-\sqrt{2}}}{6}\right)^n\cos\frac{5n\pi}{8}+2\left(\frac{\sqrt{2+\sqrt{2}}}{6}\right)^n\cos\frac{7n\pi}{8}\right\\}$|
|9|$\displaystyle\frac{1}{9}\left\\{1+2\left(\frac{\sqrt{2\cos(\pi/9)-1}}{6}\right)^n\cos\frac{n\pi}{9}+2\left(\frac{\sqrt{3+2\sin(\pi/18)-4\cos(2\pi/9)}}{6}\right)^n\cos\frac{2n\pi}{9}+2\left(\frac{\sqrt{1+2\cos(\pi/18)}}{6}\right)^n\cos\frac{4n\pi}{9}\right\\}$|
|10|$\displaystyle\frac{1}{10}\left\\{1+2\cos\frac{n\pi}{5}+2\cos\frac{2n\pi}{5}+2\left(\frac{\sqrt{5-2\sqrt{5}}}{6}\right)^n\cos\frac{n\pi}{10}+2\left(\frac{\sqrt{5+2\sqrt{5}}}{6}\right)^n\cos\frac{3n\pi}{10}\right\\}$|
