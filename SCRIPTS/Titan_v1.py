print('='*50)
print('     TiTAN v1.0')
print('='*50)

print('1. My profile')
print('2. Age Checker')
print('3. Dream Project')
print('4. Exit')

choice = input('Choose an option: ')

if choice == '1':
          print('======My Profile===')
          print('Name = Ramu K')
          print('Profession = Design Engineer')
          print('Current Goal = learn Python and sucessfully complete TiTAN project')
elif choice == '2':
        age = int(input('what is your Age: '))
        if age >= 18:
                print('You are an Adult.')
        else:
                print('You are Minor.')
elif choice == '3':
        print('dream project: Build Human Arm Robot')
elif choice == '4':
        print('Thank you for using TiTAN')

        print('Goodbye!')
else:
        print('Invalid Option')

        
