### 11.5
- (a) MLTIPLE("5, 10") = \{"50"\}
- (b) FACTOR("23") = \{"no"\}
- (c) FACTOR("30") = \{"2", "3", "5", "6", "10", "15"\}
- (d) IsPRIME("30") = \{"no"\}
- (e) IsCOMPOSITE("30") = \{"yes"\}
- (f) FACTORINRANGE("300 10 100") = \{"10", "15", "20", "30", "50", "60", "100"\}

### 11.10
#### (a) HaltInSomePoly問題は決定不能
- HISP問題を決定可能と仮定する
- 以下のようなalterYesToHISP.pyを以下のようにする
~~~
def alterYesToHISP(inString):
    (progString, newInString) = utils.DESS(inString)
    val = universal(progString, newInString):
    
    if val = "yes":
        for i in range(len(inString))
    else:
        for i in range(2 ** len(inString))
~~~

~~~
from HISP import HISP
def weirdHP(progString):
    if HISP(progString) == "yes":
        # some loop
        while true:
    else:
        # stop in polytime
        return "stop in polytime"
~~~
- この時, weirdHP(rf("weirdHP"))を考える.
- HISP(rf("weirdHP")) = "yes"の時, 
    - weirdHP(rf("weirdHP"))はloopする.
    - HISP(rf("weirdHP")) == "yes"に矛盾.

- この時, weirdHP(rf("weirdHP"))の実行時間をT(n)とする.
- T(n) < 2^n
