#### 補題
$a\ (= \mathrm{ASCII文字の数})$は正定数とする. $\frac{n!}{((n/a)!)^a}$は任意の多項式 $p(n)$ に支配されない.

#### 証明
$n$ は $a$ の倍数で $n \ge 2a$ とする. $\frac{n!}{((n/a)!)^a}$は分母分子ともにかけている項は$n$項あるので$n/a$ずつ分けると,
    $$
        \frac{n!}{((n/a)!)^a}
        = \frac{n\cdot(n-1) \dots (n- \frac{n}{a}+1)}{(n/a)!}\cdot
        \frac{(n-\frac{n}{a}) \dots (n-\frac{2n}{a}+1)}{(n/a)!}\dots
        \underbrace{\frac{\frac{2n}{a}\dots (\frac{n}{a}+1)}{(n/a)!}}_{= A}
        \cdot\frac{(n/a)!}{(n/a)!}
    $$
    となり, 後から2番目の部分は,
    $$
        A = \frac{\frac{2n}{a}\dots (\frac{n}{a}+1)}{(n/a)!}
        = \frac{2n/a}{n/a}\cdot \frac{2n/a -1}{n/a-1}\dots \frac{n/a+1}{1}
        > 2\cdot 2 \dots 2
        = 2^{n/a}
    $$
と$2^{n/a}$より大きくなる. 最初の部分から, 後から3番目の部分までも同様. したがって,
    $$ \frac{n!}{((n/a)!)^a} > \underbrace{2^{n/a} \cdot 2^{n/a} \dots 2^{n/a}}_{(a-1)\text{個}} \cdot 1 = 2^{\frac{n(a-1)}{a}} $$
となる. $a$は正定数なので, $2^{\frac{n(a-1)}{a}}$は任意の多項式に支配されない. Q.E.D.
