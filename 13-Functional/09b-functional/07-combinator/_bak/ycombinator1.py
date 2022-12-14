# https://medium.com/@adambene/fixed-point-combinators-in-javascript-c214c15ff2f6

Y = lambda g:g(lambda:Y(g))

fact = Y(
    lambda g: # g for self-referencing
        lambda x: # this curryed function is returned by g()
            1 if x == 0 else x * g()(x - 1) # recursion
)

print('fact(5)=', fact(5))
