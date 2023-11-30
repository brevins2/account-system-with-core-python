# login, register and authentication system for users
import random

user_dict = {'username': '', 'email': '', 'password': ''}
count = 0


def login():
    username = input('Enter username: ')
    password = input('Enter password: ')

    if (username == user_dict['username']) and (password == user_dict['password']):
        print('login successful')
        print(user_dict['email'])
        auth()
        return
    elif (username == user_dict['username']) and (password != user_dict['password']):
        print('invalid password please try again later')
    elif (username != user_dict['username']) and (password == user_dict['password']):
        print('invalid username please try again later')
    else:
        print('wrong credentials')


def register():
    username = input('please enter username: ')
    password = input('please enter password: ')
    email = input('please enter email: ')

    user_dict.update({'username': username, 'email': email, 'password': password})
    print('please login now')


def auth():
    token_size = []

    for x in range(6):
        digit = str(random.randint(0, 9))
        token_size.append(digit)

    print("Generated Token:", ''.join(token_size))


while count < 4:
    if user_dict.get('username') == '':
        print("please register")
        register()
    elif user_dict.get('username') != '':
        print('login first')
        login()
    else:
        print('reset your password')

    count += 1
