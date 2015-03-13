<img src='http://js-hosting.appspot.com/images/adder.png' width='70%' />
```
adder = MealyMachine('Binary addition')

carry = State('carry')
nocarry = State('no carry', initial=True)

nocarry[(1, 0), 1] = nocarry
nocarry[(0, 1), 1] = nocarry
nocarry[(0, 0), 0] = nocarry
nocarry[(1, 1), 0] = carry

carry[(1, 1), 1] = carry
carry[(0, 1), 0] = carry
carry[(1, 0), 0] = carry
carry[(0, 0), 1] = nocarry

number1 = list(int (i) for i in '0001010')
number2 = list(int (i) for i in '0001111')

inputs = zip(number1, number2)

print list(adder.process(inputs[::-1]))[::-1]
```
the code above will print `[0, 0, 1, 1, 0, 0, 1]`