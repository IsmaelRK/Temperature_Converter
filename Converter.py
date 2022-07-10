from pytemp import pytemp


def temp_converter():
    print('Choose: \n (1) ºC to ºF \n (2) ºC to K \n (3) ºF to ºC \n (4) ºF to K \n (5) K to ºC \n (6) K to ºF')
    print('Type exit to exit')
    user = input('Enter the correspondent number or exit: ')
    if user == 'exit':
        exit()

    user_temp = input('Temperature to Convert: ')

    try:
        user_temp = int(user_temp)
    except:
        print('\n Invalid, try again \n')
        temp_converter()

    if user == '1':
        print(pytemp(user_temp, 'C', 'F'))

    elif user == '2':
        print(pytemp(user_temp, 'C', 'K'))

    elif user == '3':
        print(pytemp(user_temp, 'F', 'C'))

    elif user == '4':
        print(pytemp(user_temp, 'F', 'K'))

    elif user == '5':
        print(pytemp(user_temp, 'K', 'C'))

    elif user == '6':
        print(pytemp(user_temp, 'K', 'F'))

    else:
        print('\n Invalid, try again \n')

    temp_converter()


temp_converter()
