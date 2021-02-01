def people_with_age_drink(age):
    return ["drink toddy", "drink coke", "drink beer", "drink whisky"][(age>=21) + (age>=18) + (age>=14)]


def people_with_age_drink(age):
    if age > 20: return 'drink whisky'
    if age > 17: return 'drink beer'
    if age > 13: return 'drink coke'
    return 'drink toddy'



def people_with_age_drink(age):
    if age <= 13:
        beverage = 'toddy'
    elif age > 13 and age <= 17:
        beverage = 'coke'
    elif age > 17 and age <= 20:
        beverage = 'beer'
    elif age > 20:
        beverage = 'whisky'
    return 'drink ' + beverage



def people_with_age_drink(age):
    return 'drink ' + ('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')