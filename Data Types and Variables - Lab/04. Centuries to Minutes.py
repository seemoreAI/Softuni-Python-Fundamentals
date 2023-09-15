centuries = int(input())
# 5	5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes
years = centuries * 100
days = int(years * 365.2422)
hours = int(days * 24)
minutes = int(hours * 60)
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

