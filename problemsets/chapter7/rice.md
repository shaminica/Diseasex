# ライスの定理に関する議論

## ComputesF

計算可能問題$F$に対して定義される
- 入力: プログラム$P$
- 解: $P$が$F$を計算するなら"yes", そうでなければ"no"

ライスの定理よりComputesFは計算不能

例: $F$:文字列$I$で最も多く含まれる文字を返す問題 


## ComputesOneOfS

問題の集合$S$に対して定義される
- 入力: プログラム$P$
- 解: $P$が$S$のいずれかを解けば"yes", そうでなければ"no".

ライスの定理より, $S$に含まれる計算可能問題が少なくとも1つあり, かつ, $S$に含まれない計算可能問題が少なくとも1つあるときComputesOneOfSは計算不能

例: $S=\{F$:すべての入力$I$に対して$Z$を含む文字列を返す問題\}  

## ProgramIsMemberQ
プログラムの集合$Q$に関して定義される

- 入力: プログラム$P$
- 解: $P$が$Q$に含まれれば"yes", そうでなければ"no".

[予想] ライスの定理と同様の証明より, $Q$に含まれるプログラムが少なくとも1つあり, かつ, $Q$に含まれないプログラムが少なくとも1つあるとき ProgramIsMemberQは計算不能

例: $Q=\{P$:すべての入力$I$に対して10ステップ以内で解を返すプログラム\} 

#### 予想の証明
YesOnString問題をProgramIsMemberQに還元する.
`alterYesToProgram.py`
```
import utils
from utils import rf
from universal import universal 

def alterYesToProgram(inString):
    progString = rf('progString.txt')
    newInString = rf('inString.txt')
    val = universal (progString, newInString)
    if val == 'yes':
        return rf('F.py') # FはQに含まれるプログラム
    else:
        return rf('G.py') # GはQに含まれないプログラム
```
`yesViaProgram.py`
```
from ProgramIsMemberQ import ProgramIsMemberQ  # 神託関数

def yesViaProgram(progString, inString):
    utils.writeFile('progString.txt', progString)
    utils.writeFile('inString.txt', inString)
    val = ProgramIsMemberQ(rf('alterYesToProgram.py'))
    if val == 'yes':
        return 'yes'
    else:
        return 'no'
```
- (P, I)がYesOnStringの正インスタンスなら, `alterYesToProgram.py`はQに含まれるプログラムを返すので, `yesViaProgram`内のvalは'yes'となり, "yes"を返す.
- 負インスタンスなら`alterYesToProgram.py`はQに含まれないプログラムを返すので, `yesViaProgram`内のvalは'no'となり, "no"を返す.