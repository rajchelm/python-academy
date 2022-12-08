from basics.oop.calculator import Calculator

calculator = Calculator()

assert calculator.sum(1, 2) == 3
assert calculator.difference(1, 2) == -1
assert calculator.divisor(1, 2) == 0.5
assert calculator.divisor(1, 2) == 1.0