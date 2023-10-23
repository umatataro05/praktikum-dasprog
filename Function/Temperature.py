print('Pilih temperatur :')
print('1. Celcius')
print('2. Fahrenheit')
select = int(input(':'))

if(select == 1):
    vals = int(input('Input Celcius: '))
else:
    vals = int(input('Input Fahrenheit: '))

def temperatur(vals, select):
    fahrenheit = 32
    value = 0
    temp = ''
    if(select == 1):
        value = (vals * 9/5 ) + 32
        temp = 'Farenheit'
    else:
        value = (vals - 32) * 5/9
        temp = 'Celcius'
    print(value, temp)

if(select == 1):
    print(vals, 'Celcius adalah :')
else:
    print(vals, 'Fahrenheit adalah :')

temperatur(vals,select)
