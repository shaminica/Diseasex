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
def alterYesToHISP(n):
    progString = rf("progString.txt")
    inString = rf("inString.txt")
    val = universal(progString, inString)
    
    if val == "yes":
        for i in range(len(n))
    else:
        for i in range(2 ** len(n))
~~~

- 仮に, valの戻り値がyesの場合, 入力文字列nの長さはuniversal(progString, newInString)の実行時間に影響を与えないのでP(I)の実行は$O(1)$で実行可能
- この時, alterYesToHispをHISPを使って実行する.

~~~
import HISP from HISP

def yesViaHisp(progString, inString):
    utils.writeFile("progString.txt", progString)
    utils.writeFile("inString.txt", inString)
    return HISP(rf(alterYesToHISP.py))
~~~
- もしPがIに対してyesを返すならば,  universal(progString, inString) の実行時間は$O(1)$であり, その後$O(n)$の時間で停止する.
- もしPがIに対してyesを返さないならば, 少なくとも$O(2^n)$の時間動作する.
- よってHISPはyesOnStringに還元されるため, 決定不能.

#### (b) Pが必ず停止する場合に絞ったとしてもHISPは決定不能.
- yesOnStringは$P(I)$が停止するとしても決定不能であるため, (a)から決定不能.