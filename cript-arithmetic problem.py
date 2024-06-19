from itertools import permutations

def solve_cryptarithmetic():

    letters = 'SCOBYDLINK'
    digits = range(10)

    for perm in permutations(digits, 10):
       
        letter_to_digit = {letter: digit for letter, digit in zip(letters, perm)}
     
        s = letter_to_digit['S']
        c = letter_to_digit['C']
        o = letter_to_digit['O']
        b = letter_to_digit['B']
        y = letter_to_digit['Y']
        d = letter_to_digit['D']
        l = letter_to_digit['L']
        i = letter_to_digit['I']
        n = letter_to_digit['N']
        k = letter_to_digit['K']

        if s == 0 or d == 0 or b == 0:
            continue

        scooby = 100000 * s + 10000 * c + 1000 * o + 100 * o + 10 * b + y
        dooo = 1000 * d + 100 * o + 10 * o + o
        blinks = 100000 * b + 10000 * l + 1000 * i + 100 * n + 10 * k + s

        if scooby + dooo == blinks:
            return letter_to_digit
    
    return None

solution = solve_cryptarithmetic()
if solution:
    print("Solution found!")
    print(solution)
else:
    print("No solution exists.")
