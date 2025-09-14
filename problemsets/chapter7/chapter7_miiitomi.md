## 7. 2
### 問
 - 判定問題IntOnStringを考える.
    - 入力: プログラムPと入力文字列I
    - 解: P(I)が非負整数なら"yes", そうでなければ"no".
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
プログラムの作り方からYesOnEmpty($P^{\prime}$)$="\text{yes}"$のときかつそのときに限りEmptyOnEmpty($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnEmpty($P$)はEmptyOnEmpty($P^{\prime}$)を介して計算できることとなり, 還元が完成する.

### (b) 
#### 問
GAGAOnEmpty(空文字列に対して"GAGA"を返すか)問題: $P(\varepsilon)="\text{GAGA}"$?
#### 答 
YesOnEmpty問題は計算不能であることがわかっているので, YesOnEmpty$\le_{T}$GAGAOnEmptyを示すことでGAGAOnEmptyが計算不能であることの証明を行う. 
$P$をYesOnEmpty問題の任意の入力とする. 最初に$v=P(\varepsilon)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"GAGA"}$を返すプログラム$P^{\prime}$は簡単に作ることができる.
プログラムの作り方からYesOnEmpty($P^{\prime}$)$="\text{yes}"$のときかつそのときに限りGAGAOnEmpty($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnEmpty($P$)はGAGAOnEmpty($P^{\prime}$)を介して計算できることとなり, 還元が完成する.
### (c) 
#### 問
NoOnSome(何らかの文字列$I$に対して"no"を返すか)問題: あるIに対してP(I)="no"?
#### 答 
YesOnSome問題は計算不能であることがわかっているので, YesOnSome$\le_{T}$NoOnSomeを示すことでNoOnSomeが計算不能であることの証明を行う. 
$P$をNoOnSome問題の任意の入力とする. $I$を何らかの文字列とし, 最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"no"}$を返すプログラム$P^{\prime}$は簡単に作ることができる.
プログラムの作り方からYesOnSome($P^{\prime}$)$="\text{yes}"$のときかつそのときに限りNoOnSome($P^{\prime}$)$="\text{yes}"$となる.
ゆえに, YesOnSome($P$)はNoOnSome($P^{\prime}$)を介して計算できることとなり, 還元が完成する.

### (d) 
#### 問
YesOnGAGA("GAGA"に対して"yes"を返すか)問題: P("GAGA")="yes"?
#### 答 　
YesOnString問題は計算不能であることがわかっているので, YesOnString$\le_{T}$YesOnGAGAを示すことでYesOnGAGAが計算不能であることの証明を行う. 
P, IをYesOnString問題の任意の入力とする. 入力$"GAGA"$に対して最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"yes"}$を返すプログラム$IngnoreInput$は簡単に作ることができる.
プログラムの作り方からYesOnString($P, I$)$="\text{yes}"$のときかつそのときに限りYesOnGAGA(IngoreInput)$="\text{yes}"$となる.
ゆえに, YesOnSting($P, I$)はYesOnGAGA(IgnoreInput)を介して計算できることとなり, 還元が完成する.
### (e) 
#### 問
LongerThan3OnAll(すべての文字列に対して3文字より長い出力を返すか)問題: すべてのIに対し|P(I)|>3か?
#### 答 
問3.11と同様にLongerThan3OnString(入力Iの対して3文字より長い出力を返すか)は決定不能である.
LongerThan3OnString$\le_{T}$LongerThan3OnAllを示すことでLongerThan3OnAllが計算不能であることの証明を行う. 
P, IをLongerThan3OnString問題の任意の入力とする. すべての入力に対して最初に$v=P(I)$を計算し, $v="\text{yes}"$のときかつそのときに限り$\text{"yes"}$を返すプログラム$IngnoreInput$は簡単に作ることができる.
プログラムの作り方からLongerThan3OnString($P, I$)$="\text{yes}"$のときかつそのときに限りLongerThan3OnAll(IngoreInput)$="\text{yes}"$となる.
ゆえに, LongerThan3OnString
($P, I$)はLongerThan3OnAll(IgnoreInput)を介して計算できることとなり, 還元が完成する.

## 7. 7
### 問
 - 判定問題YesOnPosIntsを考える.
   - 入力: プログラムP.
   - 解: Pが「P(I)='yes' $\Leftrightarrow$ Iは正整数」というプログラムなら'yes', そうでなければ'no'.
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
#### 解答1
 - 任意の入力文字列に対し'yes'を返す次のプログラムP1を考える.
    >```
    >def constantYes(inString):
    >    return 'yes'
    >```
 - これはYesOnPosInts問題の負インスタンスである.
 - しかしyesOnPosIntsViaYoS(P1)は無限ループに入ってしまって'no'を返さない.
 - したがってこのプログラムはYesOnPosInts問題をYesOnString問題にチューリング還元できていない.

#### 解答2
 - 以下のプログラムP2は, YesOnPosInts問題の正インスタンスである.
    >```
    >def yesIffPosInt(inString):
    >    for i in range(len(inString)):
    >        if inString[i] not in '0123456789':
    >            return 'no'
    >    integer = int(inString)
    >    if integer == 0:
    >        return 'no'
    >    return 'yes'
 - しかしyesOnPosintsViaYoS(P2)は'yes'を返さない.
 - したがってYesOnPosInts問題はYesOnString問題にチューリング還元できていない.

## 7.10
### 問
停止性問題の4種類の変種が決定不能であることの証明(p.136)は細部を省略したものだった.「明示的Pythonプログラム」アプローチを使い, HaltsOnString問題からHaltsOnSome問題への還元を示すPythonプログラムを書いて, 省略した細部を埋めよ.
### 答

## 7.15
### 問
次のように定義される計算問題EchoesFirstCharacter(EFC)について考える. 入力はASCII文字列Pである. PがPythonプログラムでなければ, 解は"no"となる. そうでない場合, PはSISO Pythonプログラムであるという前提で, IとP(I)の最初の記号が同じならその記号を解とする. 例えば, P("banana")="breakfast"なら, "b"が解になる. EFC問題は計算不能であることを証明せよ.