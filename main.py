from re import fullmatch


RE_LOGIN = '[a-zA-Z0-9._]{3,10}'
RE_PWD = '[a-zA-Z0-9._!&#]{8,15}'

users_db = {}


def check_input(reg_exp, user_input):

    if not fullmatch(reg_exp, user_input):
        raise ValueError(f'Input should be {reg_exp}')

    return True


def check_if_login_exists(login):

    global users_db

    return False if login in users_db else True


def register():

    login_check_result = False
    pwd_check_result = False
    user_login = ''
    user_pwd = ''

    while True:

        if not login_check_result:
            user_login = input('New login: ')
            login_check_result = check_if_login_exists(user_login)
            continue

        try:
            login_check_result = check_input(RE_LOGIN, user_login)
        except ValueError as error:
            print(error)

        if not pwd_check_result:
            user_pwd = input('New password: ')

        try:
            pwd_check_result = check_input(RE_PWD, user_pwd)
        except ValueError as error:
            print(error)

        return user_login, user_pwd


def login():

    global users_db

    {'asd': {'pwd': 'asdkhgajsdg'}}

    user_login = input('Login: ')
    user_pwd = input('Password: ')

    try:
        return True if users_db[user_login]['pwd'] == user_pwd else False
    except KeyError:
        return False


while True:

    action = input('Register or login: ')

    if action == 'register':
        user_login, user_pwd = register()
        users_db[user_login] = {'pwd': user_pwd}
        print(users_db)

    elif action == 'login':
        if login():
            print('Welcome')
        else:
            print('Try again')
