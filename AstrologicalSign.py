day = int(input("Дата на раждане: "))
month = input("Месец на раждане: ")
month = month.lower()

if month == 'december':
	sign = 'Стрелец' if (day < 22) else 'Козирог'

elif month == 'january':
	sign = 'Козирог' if (day < 20) else 'Водолей'

elif month == 'february':
	sign = 'Водолей' if (day < 19) else 'Риби'

elif month == 'march':
	sign = 'Риби' if (day < 21) else 'Овен'

elif month == 'april':
	sign = 'Овен' if (day < 20) else 'Телец'

elif month == 'may':
	sign = 'Телец' if (day < 21) else 'Близнаци'

elif month == 'june':
	sign = 'Близнаци' if (day < 21) else 'Рак'

elif month == 'july':
	sign = 'Рак' if (day < 23) else 'Лъв'

elif month == 'august':
	sign = 'Лъв' if (day < 23) else 'Дева'

elif month == 'september':
	sign = 'Дева' if (day < 23) else 'Везни'

elif month == 'october':
	sign = 'Везни' if (day < 23) else 'Скорпион'

elif month == 'november':
	sign = 'Скорпион' if (day < 22) else 'Стрелец'

print(f"Астрологичен знак: {sign}")