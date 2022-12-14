# Gibbs Algorithm 的範例
# 問題：機率式有限狀態機，P(a=>b)=0.3, P(b=>a)=0.5 ; P(a=>b)=0.7, P(b=>b)=0.5
# 目標：尋找該「機率式有限狀態機」的穩態，也就是 P(a) = ?, P(b)=? 時系統會達到平衡。
from prob import P
import math

def gibbs (P):
    P0 = {'a': P['a'], 'b': P['b'] }
    print('P0 = {}'.format(P0))
    while True:
        P1 = { # 下一輪的機率分布。
            'a': P0['a'] * P['a=>a'] + P0['b'] * P['b=>a'], 
            'b': P0['a'] * P['a=>b'] + P0['b'] * P['b=>b']
        }
        print('P1 = {}'.format(P1))
        da = P1['a'] - P0['a']
        db = P1['b'] - P0['b'] # 兩輪間的差異。
        step = math.sqrt(da * da + db * db) # 差異的大小
        P0 = P1
        if (step < 0.001): break # 假如差異夠小的時候，就可以停止了。

    print('標準答案:P(a)=5/8={} P(b)=3/8={}'.format(5 / 8, 3 / 8)) # 印出標準答案，以便看看我們找到的答案是否夠接近。

gibbs(P)
