from source.class_UserLogin import UserLogin

def input_data():
    use = UserLogin('', '', '', '')

    login = input("Введите свой логин: ")
    use.login = login

    while True:
        name = input("Введите своё ФИО: ")
        if use.check_fio(name):
            use.fio = name
            break
        else:
            print("Некорректное ФИО")

    while True:
        password = input("Введите свой пароль: ")
        if use.check_password(password):
            use.password = password
            break
        else:
            print("Некорректный пароль")

    while True:
        email = input("Введите свой email: ")
        if use.check_email(email):
            use.email = email
            break
        else:
            print("Некорректный email")

    return {'name': use.fio, 'login': use.login, 'password': use.password, 'email': use.email}
