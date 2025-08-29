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
