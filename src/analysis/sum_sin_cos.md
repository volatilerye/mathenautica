# $\sum_{k=0}^{n}\sin k\theta, \sum_{k=0}^{n} \cos k\theta$

> [!tip] 定理1&emsp;$\sum_{k=0}^{n}\sin k\theta, \sum_{k=0}^{n}\cos k\theta$
> $\theta \neq 2n\pi\\;(n\in\mathbb{Z})$ のとき,
> 1. $\displaystyle \sum_{k=0}^{n}\sin k\theta =\frac{\sin\frac{(n+1)\theta}{2}\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}.$
> 1. $\displaystyle \sum_{k=0}^{n}\cos k\theta =\frac{\sin\frac{(n+1)\theta}{2}\cos\frac{n\theta}{2}}{\sin\frac{\theta}{2}}.$

Euler の公式 $e^{i\theta} = \cos\theta +i\sin\theta$ を用いると証明しやすい.

> [!proof]
> $$
> \begin{align*}
> \left(\sum_{k=0}^{n}\cos k\theta\right)+ i\left(\sum_{k=0}^{n}\sin k\theta\right)
> &= \sum_{k=0}^{n} (\cos k\theta+i\sin k\theta) \\\\
> &= \sum_{k=0}^{n} e^{i\theta k} \\\\
> &= \frac{e^{i(n+1)\theta}-1}{e^{i\theta}-1} \\\\
> &= \frac{e^{i(n+1)\theta/2}-e^{-in\theta/2}}{e^{i\theta/2}-e^{-i\theta/2}}\cdot e^{in\theta/2} \\\\
> &= \frac{\frac{e^{i(n+1)\theta/2}-e^{-in\theta/2}}{2i}}{\frac{e^{i\theta/2}-e^{-i\theta/2}}{2i}}\cdot e^{in\theta/2} \\\\
> &= \frac{\sin\frac{(n+1)\theta}{2}}{\sin\frac{\theta}{2}}\left(\cos\frac{n\theta}{2}+i\sin\frac{n\theta}{2}\right) \\\\
> &= \frac{\sin\frac{(n+1)\theta}{2}\cos\frac{n\theta}{2}}{\sin\frac{\theta}{2}} + i\frac{\sin\frac{(n+1)\theta}{2}\sin\frac{n\theta}{2}}{\sin\frac{\theta}{2}}.
> \end{align*}
> $$
> 
> 実部と虚部でそれぞれの定理が示されている.