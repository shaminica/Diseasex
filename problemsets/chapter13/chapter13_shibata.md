## 13.2
### 問　
$A$と$B$はともに判定問題で, $A\le_{P}B$ かつ$B\le_{P}A$ということがわかっている. 以下の命題の中で必ず真となるもをを答えよ.
(a) $A$と$B$はともにクラスPolyに属する.  
(b) $A$と$B$はともに超多項式時間を必要とする.  
(c) 両方の問題($A$と$B$)がクラスPolyに属するか, 両方が超多項式時間を必要とするかのどちらかである.  
(d) 両方の問題($A$と$B$)がクラスPolyに属するか, 両方がクラスPolyに属さないかのどちらかである.  
(e) 両方の問題($A$と$B$)がクラスPolyに属するか, 両方がクラスExpoに属するかのどちらかである.  
### 答
(d)は必ず真となる.
    - $A$がクラスPolyに属するとき, $B\le_{P}A$によって$B$もクラスPolyに属する
    - $A$がクラスPolyに属さないとき, $A\le_{P}B$によって$B$もクラスPolyに属さない
その他は両方が計算不能な場合に偽となる.

## 13.12
### 問　
主張13.4の方法を使って演習問題13.11の3-SATインスタンスをCIRCUITSATインスタンスに変換せよ. 得られたインスタンスは正インスタンスか負インスタンスか, 理由を説明せよ
### 答
w1 = x1 OR x2 OR NOT x3  
w2 = NOT x2 OR NOT x3
w3 = x1 OR x3  
w4 = NOT x1 OR NOT x2
w5 = NOT x1 OR x2
output w1 AND w2 AND w3 AND w4 AND w5  
演習問題13.11と同値より負インスタンスである.

## 13.13
### 問　
SAT$\le_{P}$3-SAT(主張13.7)を証明したときの方法を使って, 次のSATインスタンスを3-SATインスタンスに変換せよ.  
$(\lnot x_1 \lor \lnot x_2 \lor \lnot x_3 \lor x_4)\land (x_1 \lor x_2 \lor x_4 \lor \lnot x_5)$

### 答
$(\lnot x_1 \lor \lnot x_2 \lor d_1) \land (\lnot d_1 \lor \lnot x_3 \lor x_4)\land (x_1 \lor x_2 \lor d_2) \land (\not d_2 \lor x_4 \lor \lnot x_5)$

それぞれの節をダミー変数を導入すること3個以下のリテラルで構成されるように分離する.

## 13.17
### 問　
演習問題12.14の判定問題SubsetSumWithFivesを思い出そう. SubsetSum問題と同じであるが, 部分集合を作るときに, 必要に応じて重さの5の重しを10個まで使えることだけが異なる. SubsetSum$equiv_{P}$SubsetSumWithFivesを証明せよ.

### 答
(i) SubsetSum$\le_{P}$SubsetSumWithFivesを示す.  
SubsetSumWithFives問題の入力インスタンスの重みに5を10個加えたものを考える. このインスタンスの作成は定数時間で実行できる. SubsetSumWithFives問題の解が"yes"のとき, 新しく作成されたインスタンスはSubsetSum問題で"yes"を返し, SubsetSumWithFives問題の解が"no"のとき, 新しく作成されたインスタンスはSubsetSum問題で"no"を返す. 

(ii) SubsetSumWithFives$\le_{P}$SubsetSumを示す.  
SubsetSumWithFives問題を解けるアルゴリズムAを仮定し, 次のプログラムを考える. Aを用いてSubsetSum問題の入力インスタンスを解いたのち, 入力におけるしきい値を5ずつ増やしながら10回同様にAを適用し, これらの11回の試行においてすべて"yes"を返せば"yes", そうでなければ"no"を返す.

このプログラムはAの計算量のたかだか定数倍で実行できる. また, SubsetSum問題の正インスタンスに対して適用すると"yes"を返す.  
このプログラムの正インスタンスがSubsetSum問題の正インスタンスであることは次のように説明される（されない）. 
- このプログラムで実行された最小のしきい値を$w$とすると, 各重しと10個の重さ5の重しによって$w+5l$($l$は0以上10以下の整数)を生成することができる
- $w+5l$と$w+5(l+1)$両方生成できるので, $w+5(l+1)$を生成した際には重さ5の重しを少なくとも1つ余らせている.
- 反例: "1,1,1,10;8"




