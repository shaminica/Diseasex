## 7.4

### 問
- F と G は一般的な計算問題，D は判定問題とする.
- F は G に，D は G に還元されるものとする.
- 次の条件のもとで言える結論があれば答えよ.

### 答
- (a) D が決定不能な場合
    - $ D \leq_T G $ より Gは計算不能

- (b) G が計算可能な場合
    - $ F \leq_T G $,$ D \leq_T G $ より Fは計算可能, Dは決定可能

- (c) F が計算可能な場合
    - $ F \leq_T G $ かつ $ D \leq_T G $ だが D,Gに言える結論はない

## 7.9
### 問
- 次のような計算問題 NumLonger を定義する.
    - 入力:プログラム P
    - 解: P(I) が定義されていて I よりも長くなるような別々の文字列 I の数である
        - $ \{ I \in ASCII* | |P(I)| > |I| \}$の濃度
        - 上記の集合が無限集合の場合, 解は"infinte"とする
    
- NumLongerは計算可能か？

### 答
#### 計算不能

- NumLongerを計算可能とする.
- `alterYesToStrLength.py`
    >```
    >from universal import universal
    >
    >def alterYesToStrLength(inString):
    >    progString = rf(’progString.txt’)
    >    val = universal(progString, inString)
    >    if val == 'yes':
    >        return InString + '!'
    >    else:
    >        return InString
    >```
 - `yesOnSomeViaNumLonger.py`
    >```
    >from NumLonger import NumLonger
    >from utils import rf
    >
    >def yesOnSomeViaNumLonger(progString):
    >    utils.writeFile(’progString.txt’, progString)
    >    if NumLonger(rf('alterYesToStrLength.py')) > 0　or NumLonger(rf('alterYesToStrLength.py')) == 'infinite':
    >       return 'yes'
    >    else:
    >       return 'no' 
    >```

- 神託プログラム'NumLonger'が与えられたとする
- 上記のように'alterYesToStrLength.py'と'yesOnSomeViaNumLonger.py'を定義する
- この時, 'yesOnSomeViaNumLonger'に入力したPに対して'yes'を返すようなIの数を'NumLonger'で知ることができる
- よってyesOnSome問題はNumLongerに還元できる
- yesOnSomeは決定不能であるからNumLongerも計算不能である.

## 7.14
### 問
- ライスの定理の変種のいずれかを使って(つまり，148 ページのテクニック 3)，次の各問題が計算 不能であることを証明せよ.

### 答
- (a) ComputesLength(長さを計算)
    - 入力:プログラム P
    - 解：解はすべての I に対して $P(I) = |I|$ のときかつそのときに限り “yes”

- ComputeLengthは以下の集合Sに対してComputeOneOfS問題である
    - $ S = \{ F | 全てのIに対して, F(I) = |I| \}$
- この時, 以下ふたつの計算可能関数が存在する
    - 常に入力を返す定数関数, F(I) = \{I\}, これはSに含まれ, 計算可能
    - 常に'a'を返す定数関数, F(I) = \{'a'\},  これはSに含まれず, 計算可能
- Riceの定理より, ComputeOneOfSは計算不能であるから, ComputeLengthも計算不能

- (b) SearchesForSubstring(部分文字列探索)
    - 入力:プログラム P
    - 解: P が何らかの定数部分文字列を探索するときかつそのときに限り “yes”.
    - つまり，s が I の部分文字列である ときかつそのときに限り $P(I) = “yes”$ となるような文字列 s が存在するかどうかを尋ねる.

- SearchesForSubstringは以下の集合Sに対してComputeOneOfS問題である
    - $ S = \{ F | あるsが存在して, $s \in I$ ならば F(I) = 'yes'　そうでないなら F(I)='no' \}$
- この時, 以下ふたつの計算可能関数が存在する
    - ContainGAGAはSに含まれる計算可能問題
    - isNum問題（入力が数字であればyes）はsに含まれない計算可能問題
- Riceの定理より, ComputeOneOfSは計算不能であるから, ComputeLengthも計算不能