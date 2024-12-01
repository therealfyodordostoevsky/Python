subscribers = ["Jackson", "Apple", "West", "White"]
print(list(map(lambda x: x.upper(), subscribers)))
enlisters = [
    {'name': 'Avesta', 'lname': 'Sedghian', 'age': 12},
    {'name': 'Michael', 'lname': 'Jackson', 'age': 59},
    {'name': 'Franklin', 'lname': 'Clinton', 'age': 34},
    {'name': 'Trevor', 'lname': 'Philips', 'age': 56} 
]
lnames = map(lambda person: person['lname'], enlisters)
print(list(lnames))
def scheduleInterview(contestant):
    print(f"Scheduled meeting with {contestant['Name']} {contestant['LName']}")

contestants = [
    {
        'Name': 'Amirali',
        'LName': 'Moradi',
        'Age': 59,
        'Eye_Sight': 100,
        'Aircraft_Manuever': 70,
        'Gravity_resistor': True,
        'Academic_GPA': 4.0
    },
    {
        'Name': 'Mohammad',
        'LName': 'Nabavi',
        'Age': 23,
        'Eye_Sight': 73,
        'Aircraft_Manuever': 80,
        'Gravity_resistor': True,
        'Academic_GPA': 3.9
    },
    {
        'Name': 'Arian',
        'LName': 'Mahmoodi',
        'Age': 24,
        'Eye_Sight': 87,
        'Aircraft_Manuever': 62,
        'Gravity_resistor': False,
        'Academic_GPA': 2.6
    },
    {
        'Name': 'Yousef',
        'LName': 'Alizadeh',
        'Age': 46,
        'Eye_Sight': 62,
        'Aircraft_Manuever': 41,
        'Gravity_resistor': False,
        'Academic_GPA': 3.6
    },
    {
        'Name': 'Ehsan',
        'LName': 'Gholikhani',
        'Age': 51,
        'Eye_Sight': 64,
        'Aircraft_Manuever': 72,
        'Gravity_resistor': True,
        'Academic_GPA': 3.7
    },
]
for contestant in contestants:
    academicWinner = contestant['Academic_GPA'] >= 2.0
    eyeSightPercentage = contestant['Eye_Sight'] / 100
    eyeWinningPilot = eyeSightPercentage >= (50 / 100)
    younglings = contestant['Age'] <= 50
    aircraftManueveurWinner = contestant['Aircraft_Manuever'] > 50
    realMan = contestant['Gravity_resistor'] = True
    meetsCriteria= (
        academicWinner and
        eyeWinningPilot and
        younglings and
        aircraftManueveurWinner and
        realMan
    )
    if meetsCriteria:
        scheduleInterview(contestant)

myList = list(range(100))
evens = filter(lambda num: num % 2 == 0, myList)
print(evens)
