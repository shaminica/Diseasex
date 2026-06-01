## 7. 2
### 問
 - 判定問題IntOnStringを考える.
    - 入力: プログラムPと入力文字列I.
    - 解: P(I)が非負整数なら"yes". そうでなければ"no".
 - YesOnString問題をIntOnString問題へ還元する2つのPythonプログラムを書け.

### 答
 - `alterYesToInt.py`
    >```
    >from utils import DESS
    >from universal import universal
    >
    >def alterYesToInt(inString):
    >    (progString, newInString) = DESS(inString)
    >    val = universal(progString, newInString)
    >    if val == 'yes':
    >        return '1'
    >    else:
    >        return 'This is not an integer.'
    >```
 - `yesViaInt.py`
    >```
    >from intOnString import intOnString  # 神託関数
    >from utils import ESS, rf
    >
    >def yesViaInt(progString, inString):
    >    singleString = ESS(progString, inString)
    >    return intOnString(rf('alterYesToInt.py'), singleString)  # (1)
    >```
 - 神託プログラム`intOnString.py`（PとIが与えられ, P(I)が数字のみからなるなら'yes', それ以外なら'no'）が存在するとする.
 - (P, I)がYesOnString問題の正インスタンスなら, (1)でalterYesToInt(ESS(P, I))は'1'を返すはずなので, yesViaInt(P, I)は'yes'を返す.
 - (P, I)がYesOnString問題の負インスタンスなら, (1)でalterYesToInt(ESS(P, I))は数字を返さないので, yesViaInt(P, I)は'no'を返す.
 - したがってYesOnString問題はIntOnString問題に還元されるため, IntOnString問題は決定不能である.

## 7.5
### (a) 
#### 問
EmptyOnEmpty(空文字列に対して空文字列を返すか)問題: $P(\varepsilon)=\varepsilon$?
#### 答
YesOnEmpty問題は計算不能であることがわかっているので, YesOnEmpty$\le_{T}$EmptyOnEmptyを示すことでEmptyOnEmptyが計算不能であることの証明を行う. 
$P$をYesOnEmpty問題の任意の入力とする. 最初に$v=P(\varepsilon)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\varepsilon$を返すプログラム$P^{\prime}$は簡単に作ることができる.
プログラムの作り方からYesOnEmpty($P$)$="\text{yes}"$のときかつそのときに限りEmptyOnEmpty($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnEmpty($P$)はEmptyOnEmpty($P^{\prime}$)を介して計算できることとなり, 還元が完成する.

### (b) 
#### 問
GAGAOnEmpty(空文字列に対して"GAGA"を返すか)問題: $P(\varepsilon)="\text{GAGA}"$?
#### 答 
YesOnEmpty問題は計算不能であることがわかっているので, YesOnEmpty$\le_{T}$GAGAOnEmptyを示すことでGAGAOnEmptyが計算不能であることの証明を行う. 
$P$をYesOnEmpty問題の任意の入力とする. 最初に$v=P(\varepsilon)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"GAGA"}$を返すプログラム$P^{\prime}$は簡単に作ることができる.
プログラムの作り方からYesOnEmpty($P$)$="\text{yes}"$のときかつそのときに限りGAGAOnEmpty($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnEmpty($P$)はGAGAOnEmpty($P^{\prime}$)を介して計算できることとなり, 還元が完成する.
### (c) 
#### 問
NoOnSome(何らかの文字列$I$に対して"no"を返すか)問題: あるIに対してP(I)="no"?
#### 答 
YesOnSome問題は計算不能であることがわかっているので, YesOnSome$\le_{T}$NoOnSomeを示すことでNoOnSomeが計算不能であることの証明を行う. 
$P$をYesOnSome問題の任意の入力とする. $I$を何らかの文字列とし, 最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"no"}$を返すプログラム$P^{\prime}$は簡単に作ることができる.
プログラムの作り方からYesOnSome($P$)$="\text{yes}"$のときかつそのときに限りNoOnSome($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnSome($P$)はNoOnSome($P^{\prime}$)を介して計算できることとなり, 還元が完成する.

### (d) 
#### 問
YesOnGAGA("GAGA"に対して"yes"を返すか)問題: P("GAGA")="yes"?
#### 答 　
YesOnString問題は計算不能であることがわかっているので, YesOnString$\le_{T}$YesOnGAGAを示すことでYesOnGAGAが計算不能であることの証明を行う. 
P, IをYesOnString問題の任意の入力とする. 入力$"GAGA"$に対して最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"yes"}$を返すプログラムignoreInputは簡単に作ることができる.
プログラムの作り方からYesOnString($P, I$)$="\text{yes}"$のときかつそのときに限りYesOnGAGA(ignoreInput)$="\text{yes}"$となる.
ゆえに, YesOnSting($P, I$)はYesOnGAGA(ignoreInput)を介して計算できることとなり, 還元が完成する.
### (e) 
#### 問
LongerThan3OnAll(すべての文字列に対して3文字より長い出力を返すか)問題: すべてのIに対し|P(I)|>3か?
#### 答 
問3.11と同様にLongerThan3OnString(入力Iの対して3文字より長い出力を返すか)は決定不能である.
LongerThan3OnString$\le_{T}$LongerThan3OnAllを示すことでLongerThan3OnAllが計算不能であることの証明を行う. 
P, IをLongerThan3OnString問題の任意の入力とする. すべての入力に対して, 最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"yes"}$を返すプログラムignoreInputは簡単に作ることができる.
プログラムの作り方からLongerThan3OnString($P, I$)$="\text{yes}"$のときかつそのときに限りLongerThan3OnAll(ignoreInput)$="\text{yes}"$となる.
ゆえに, LongerThan3OnString
($P, I$)はLongerThan3OnAll(ignoreInput)を介して計算できることとなり, 還元が完成する.

## 7. 7
### 問
 - 判定問題YesOnPosIntsを考える.
   - 入力: プログラムP.
   - 解: Pが「任意の正整数Iに対して, P(I)='yes'」を満たすなら'yes'. そうでなければ'no'.
 - 以下のプログラム7.9（`yesOnPosIntsViaYoS.py`）は, YesOnPosInts問題をYesOnString問題に還元しようとした試みである.
 - これが正しいチューリング還元でない理由を説明せよ.
   >```
   >from yesOnString import yesOnString
   >
   >def yesOnPosIntsViaYoS(progString):
   >    i = 1
   >    while True:
   >        if not yesOnString(progString, str(i)) == 'yes':
   >            return 'no'
   >        i += 1

### 答
 - 任意の入力文字列に対し'yes'を返すようなプログラムPを考える.
    >```
    >def constantYes(inString):
    >    return 'yes'
    >```
 - これは明らかにYesOnPosInts問題の正インスタンスである.
 - しかしyesOnPosIntsViaYoS(P)は無限ループに入ってしまって, 'yes'を返すことはない.
 - したがって, このプログラムではYesOnPosInts問題をYesOnString問題にチューリング還元できていない.

#### 補足
 - YesOnPosInts問題をYesOnString問題に還元できるかは分からないが, 逆（YesOnString問題のYesOnPosInts問題への還元）はYesOnEmpty問題などと同様にして簡単にできる.
      >```
      >from yesOnPosInts import yesOnPosInts  # 神託関数
      >from utils import writeFile, rf
      >
      >def yesViaPosInts(progString, inString):
      >    writeFile('progString.txt', progString)
      >    writeFile('inString.txt', inString)
      >    return yesOnPosInts(rf('ignoreInput.py'))
      >```

## 7.10
### 問
停止性問題の4種類の変種が決定不能であることの証明(p.136)は細部を省略したものだった.「明示的Pythonプログラム」アプローチを使い, HaltsOnString問題からHaltsOnSome問題への還元を示すPythonプログラムを書いて, 省略した細部を埋めよ.
### 答
以下の2つのpythonプログラムを用いることでHaltsOnString問題をHaltsOnSome問題を介して解くことができる.
- ```ignoreInput.py```
>```
> def ignoreInput(inString):
>     progString = rf('progString.txt')
>     newInString = rf('inString.txt')
>     return universal(progString, newInString)
>```

- ```HaltsOnStringViaSome.py```
>```
> from HaltsOnSome import HaltsOnSome # 神託関数
> 
> def HaltsOnStringViaSome(progString, inString):
>     utils.writeFile('progString.txt', progString)
>     utils.writeFile('inString.txt', inString)
>     return HaltsOnSome(rf('ignoreInput.py'))
>```

## 7.12
### 問
 - 次の判定問題SlowerThanInputLengthが決定不能であることを証明せよ.
   - 入力： プログラム$P$.
   - 解： 全ての$I$に対し$P(I)$の停止までのステップ数が$|I|$よりも多いなら'yes', そうでなければ'no'.
   （$P(I)$が未定義なら実行ステップは無限大とする)
### 答
 - HaltsOnString問題をSlowerThanInputLength問題に還元する.
   ```
   from slowertThanInputLength import slowerThanInputLength
   from utils import rf, writeFile

   def haltsViaSlower(progString, inString):
      writeFile('progString.txt', progString)
      writeFile('inString.txt', inString)
      val = slowerThanInputLength(rf(`ignoreInput.py`)) # (2)
      if val == 'yes':
         return 'no'
      else:
         return 'yes'
   ```
      - `ignoreInput.py`は入力を無視して$P(I)$を実行するので, その実行ステップ数は$P(I)$の実行ステップ数$+c$ (定数).
      - (P, I)がHaltsOnString問題の正インスタンスなら, 十分大きな$n$をとれば`ignoreInput.py`は$n$文字以上の入力に対して$n$未満のステップ数で止まる. したがって(2)のvalは'no'となり, haltsViaSlowerは'yes'を返す.
      - (P, I)がHaltsOnStringの負インスタンスなら, `ignoreInput`はどんな入力に対しても停止しない(実行ステップ無限大). したがって(2)のvalは'yes'となり, haltsViaSlowerは'no'を返す.

## 7.15
### 問
次のように定義される計算問題EchoesFirstCharacter(EFC)について考える. 入力はASCII文字列Pである. PがPythonプログラムでなければ, 解は"no"となる. そうでない場合, PはSISO Pythonプログラムであるという前提で, IとP(I)の最初の記号が同じならその記号を解とする. 例えば, P("banana")="breakfast"なら, "b"が解になる.そのような性質を持つIがなければ, インスタンスは負で解は"no"となる. EFC問題は計算不能であることを証明せよ.

### 答
- YesFirstCharacter問題を考え, 決定不能であることをライスの定理を用いて示す
- YesFirstCharacter問題がEFCに還元されることを示す
#### proof
YesFirstCharacter問題(YFC)を考える. 
   -  入力はASCII文字列Pである. PがPythonプログラムでなければ, 解は"no"となる. そうでない場合, PはSISO Pythonプログラムであるという前提で, ある入力Iに対してIとP(I)の最初の記号が同じなら解は"yes"となる.そのような性質を持つIがなければ, 解は"no"となる.

$S=\{F| ある入力Iに対してIとF(I)の最初の記号が等しい\}$を考える.
$S$には少なくとも1つの計算可能な関数, 例えば$P(I)=I$とする恒等写像のプログラム, が含まれ, 少なくとも1つの計算可能な関数, 例えばすべてのIに対して$P(I)=\varepsilon$とする定数関数のプログラム, が含まれない.
ライスの定理より, ComputesOneOf${}_{S}$は計算不能であるためYFCは計算不能である.
ここで, EFCが解をもつ場合に"yes"を出力するプログラムはEFCから容易に作ることができるため, YFCはEFCを介して計算できる. 
よって還元が成立し, YFC$\le_{T}$EFCより, EFCは計算不能である.

## 7.17
### 問
 - 次のTripleOnSome問題が計算不能であることを証明せよ.
   - 入力: プログラム$P$
   - 解: もし$P(M)=3M$となる正整数$M$が存在するなら$M$, そうでないなら'no'.
### 答
   - 以下でYesOnString問題をTripleOnSomeに還元する.
      ```
      from utils import universe

      def one_to_three(inString):
         progString = rf('progString.txt')
         newInString = rf('inString.txt')
         val = universe(progString, newInString)
         if val == 'yes' and inString == '1':
            return '3'
         else:
            return 'no'
      ```
      ```
      from tripleOnSome import tripleOnSome  # 神託関数
      from utils import rf, writeFile

      def yesViaTriple(progString, inString):
         writeFile('progString.txt', progString)
         writeFile('inString.txt', inString)
         val = tripleOnSome(rf('one_to_three.py'))   # (2)
         if val == '1':
            return 'yes'
         else:
            return 'no'
      ```
      - (P, I)がYesOnStringの正インスタンスなら, `one_to_three.py`は'1'に対し'3'を返すプログラムになるはずなので, (2)のvalは'1'. したがってyesViaTriple(P, I)は'yes'を返す.
      - 負インスタンスなら`one_to_three.py`は任意のinputに対して'no'または未定義となるプログラムになるはずなので, (2)のvalは'no'. したがってyesViaTriple(P, I)は'no'を返す.