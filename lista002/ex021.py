def celsius_para_fahrenheit(celsius):
    f = celsius * 1.8 + 32
    return f
v_celsius = float(input('Digite o valor para celsius: '))
result = celsius_para_fahrenheit(v_celsius)
print('O valor em fahrenheit é de',result)