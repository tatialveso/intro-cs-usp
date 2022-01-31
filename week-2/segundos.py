total = int(input("Por favor, entre com o número de segundos que deseja converter: "))

totalInDays = total // 86400
totalInHours = total // 3600
totalInSeconds = total % 3600
totalInMinutes = totalInSeconds // 60
restInSeconds = totalInSeconds % 60

if(totalInHours >= 24) :
    totalInDays = int(totalInHours / 24)
    totalInHours = int(totalInHours % 24)

print(totalInDays, "dias,", totalInHours, "horas,", totalInMinutes, "minutos e", restInSeconds, "segundos.")