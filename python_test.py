num1 = int(input('Please enter your first number: '))
sign = input('Enter the operator sign: ')
num2 = int(input('Please enter your second number: '))
if sign == '+':
    result = num1 + num2
    print('The result is: '+ str(result))
elif sign == '-':
    result = num1 - num2
    print('The result is: '+ str(result))
elif sign == '*':
    result = num1 * num2
    print('The result is: '+ str(result))
elif sign == '/':
    result = num1 / num2
    print('The result is: '+ str(result))    