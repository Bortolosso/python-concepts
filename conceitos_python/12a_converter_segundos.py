dias = int(input("Informe a quantidade de dias :"))
horas = int(input("Informe a quantidade de horas :"))
minutos = int(input("Informe a quantidade de minutos :"))
segundos = int(input("Informe a quantidade de segundos :"))

#dia pra segundos
dia_pra_segun = dias * 86400

#horas pra segundos
hora_pra_segun = horas * 3600

#minutos pra segundos
min_pra_segundo = minutos * 60

total_segundos = dia_pra_segun + hora_pra_segun + min_pra_segundo + segundos

print("Ao total deram",total_segundos , "segundos")


