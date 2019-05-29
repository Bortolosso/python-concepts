num_int = 5
num_float = 7.8
val_str = "STRING"
value = "VALOR :"

print(value, num_int)

# Em Python o simbulo "%" = valor, definindo o tipo de dado.

#Os dois caracteres "%i" devem substituido por um numero.
print("1 O VALOR FICA:%i" %num_int)
print("2 O VALOR FICA: " + str(num_int))

print("3 O valor :", num_float)
print("4 O valor : %.10f" %num_float)
# Os caracteres "%.10f" define quantas casas decimais ira ocorrer. No caso como declarado 10 casas
print("5 O valor : " + str(num_float))

print("6 Concatenando strings", val_str)
print("7 Concatenando strings %.s" %val_str)
print("8 Concatenando strings %.3s" %val_str)
print("9 Concatenando strings " + val_str)