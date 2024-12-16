def Sum_numbers(*args):
        total=0
        for number in args:
                if isinstance(number, (int,float)):
                        total += number
        return total
result = Sum_numbers(1, 2)
print(result)
result = Sum_numbers(1, 2, 3)
print(result)
result = Sum_numbers(1.5, 2.5, 3.5)
print(result)
result = Sum_numbers(1, 2, '3')
print(result)