mystr1 = 'TestSomething'
mystr2 = 'testsomething'

print([x for x in mystr1 if x.upper() == x])
print([x for x in mystr2 if x.upper() == x])

if [x for x in mystr1 if x.upper() == x]:
    print('mystr1 is True')

if [x for x in mystr2 if x.lower() == x]:
    print('mystr2 is True')

print(mystr2.upper())
print(mystr1.lower())


def validate_password(password):
    if len(password) >= 8 and [x for x in password if x.upper() == x] and [x for x in password if x.isdigit()]:
        print(f'Password: {password} is valid')
    else:
        print(f'Password: {password} is INVALID!')


validate_password('Alobutalo8')
