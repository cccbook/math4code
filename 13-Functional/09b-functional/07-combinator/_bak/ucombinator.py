# https://medium.com/@adambene/fixed-point-combinators-in-javascript-c214c15ff2f6

U = lambda g: g(g)

fact = U(
    lambda g: # g for self-referencing
        lambda x: # currying is for passing the halting condition
            1 if x == 0 else x * g(g)(x - 1) # recursion
)

print('fact(5)=', fact(5))

