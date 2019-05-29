num_int = 5
num_float = 7.8
val_str = "STRING"
value = "VALOR :"

print("O valor :", num_float)
print("O valor : %.10f" %num_float)
# Os caracteres "%.10f" define quantas casas decimais ira ocorrer. No caso como declarado 10 casas
print("O valor : " + str(num_float))

print("Concatenando strings", val_str)
print("Concatenando strings %.s" %val_str)
print("Concatenando strings %.3s" %val_str)
print("Concatenando strings " + val_str)