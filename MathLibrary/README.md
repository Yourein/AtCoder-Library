# AtCoder-Library

[AtCoder](https://atcoder.jp/) のライブラリを保管しています。

(*stores AtCoder-Library.*)  

## MathLibrary
|File Name|Algorithm|Explanation|
|:--:|:--:|:--:|
|[BinaryToDecimal.py](BinaryToDecimal.py)|2進数 -> 10進数への変換|2進数を10進数に変換してくれる|
|DecimalToBinary.py|10進数 -> 2進数への変換|10進数を2進数に変換してくれる|
|DigitSum_1.py|桁和(1)|intのまま桁和を求められる|
|DigitSum_2.py|桁和(2)|strに変換した後に桁和を求められる|
|divisor.py|約数列挙|約数の列挙を行ってくれる|
|ExtGCD.py|拡張ユークリッドの互除法|ap + bq = d := gcd(a, b)となる (p, q, d) を返す|
|FromFloatToInt.py|float -> int|floatの誤差計算を防ぐためにintに変換して計算する|
|factorization.py|素因数分解|素因数分解を行ってくれる|
|PrimaryCheck.py|素数判定|その数が素数かどうかの判定を行ってくれる  一般的には十分高速だが, 競プロ界隈だと遅い|
|SieveOfEratosthenes_1.py|エラトステネスの篩 (Ver.1) |O(√N)よりも高速に素数を列挙してくれる （緑Diff以上になってくると使用するタイミングが出てくる）|
|SieveOfEratosthenes_2.py|エラトステネスの篩 (Ver.2) |Ver.1 の時よりも高速に素数を列挙することができる|
|XorToN_1.py|０〜NまでのXORをとる(Ver.1)|計算量はO(logN)|
|XorToN_2.py|０〜NまでのXORをとる(Ver.2)|Ver.1よりも高速に処理する, 計算量はO(1)|
|CumulativeSum.py|累積和|累積和を行ってくれる|
|MaxCumulativeSum.py|区間累積和の最大・最小問題|区間累積和の最大・最小を求められる|
|nCk.py|combinationの計算|nCkの計算を高速に行える, 計算量はO(K)|
|nCk_2.py|combinationの計算|nCk.pyのpowを最後に持ってきたから高速?, 計算量はO(K)|