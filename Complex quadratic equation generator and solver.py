# 'Nice number' quadratic equation generator and solver with complex coefficients of x with real or complex roots
#Program will generate quadratic equations of the form ax^2+bx+c where a is a nonzero real, b is complex and c is real.
#Program will only output quadratic equations that provide an answer where the roots have integer real components
#and an imaginary component less than 5 digits total.
#Program will generate answers to each of these equations

import cmath #necessary for handling the complex numbers

def generate_quadratic_equations():
    for a in range(-25, 26):
        if a != 0: #a obviously can't be 0 to still be a quadratic eqn
            for b_real in range(-25, 26):
                for b_imag in range(-25, 26): 
                    b = complex(b_real, b_imag) #generates a complex number with real part in [-25,25] and imaginary part in same domain
                    for c in range(-25, 26):
                        if c != 0: #c can be 0 and still be a quadratic eqn but the equations are more exam-like if c is nonzero
                            d = (b**2) - (4*a*c) 
                            #find two solutions
                            sol1 = (-b-cmath.sqrt(d))/(2*a)
                            sol2 = (-b+cmath.sqrt(d))/(2*a)
                            if sol1.real == int(sol1.real) and sol2.real == int(sol2.real):
                                if len(str(sol1.imag)) < 5 and len(str(sol2.imag)) < 5:
                                    print(f"{a}x^2 + ({b})x + {c} = 0 \n answer = {sol1} and {sol2}")

generate_quadratic_equations()

#Todo: there is probably some way of determining if solution will satisfy conditions of int real and <5len imaginary parts before solving it
#but the loops are small enough that O(n^4) is still fast enough for the code's purposes
#solving this problem would be fun but trivial

#easier but unnecessary for same reason: complex roots come in conjugate pairs so if sol1 is complex sol2 need not be calculauted.
