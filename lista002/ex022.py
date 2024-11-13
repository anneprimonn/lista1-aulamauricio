def fahrenheit_para_celsius(fahrenheit):
    c = (fahrenheit - 32) / 1.8
    return c
v_fahrenheit = float(input('Digite o valor em fahrenheit: '))
result = fahrenheit_para_celsius(v_fahrenheit)
print('A temperatura em celsius é',result)