def user_info(name, surname, year_of_birth, city, email, contact_number):
    result = f"{name}, {surname}, {year_of_birth}, {city}, {email}, {contact_number}"
    return result

print(user_info(input("Имя "), input("Фамилия "), int(input("Год рождения ")), input("Город проживания "), input("Эл. почта "), int(input("Номер телефона "))))