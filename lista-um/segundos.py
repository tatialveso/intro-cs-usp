total = int(input("Por favor, entre com o número de segundos que deseja converter: "))

totalInDays = round(total / 86400)
totalInHours = round(total / 3600)
totalInMinutes = round(total / 60)
totalInSeconds = round(total % 60)

print(totalInDays, "dias,", totalInHours, "horas,", totalInMinutes, "minutos e", totalInSeconds, "segundos.")