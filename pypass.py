from os import name, system

letterSwaps = {'i':['1', '!'], 'e':['3'], 's':['5'], 'a':['4', '@'], 'p':['9'], 'l':['1'], 't':['7']}
targetInfo = {}
potentialPass = []
clear = lambda: system('cls' if name == 'nt' else 'clear') # OS-agnostic clear function

print('\n*** PyPass ***\n')
print("Answer question with 'n' if info is unknown.")
input('\n\nPress Enter to begin.')

clear()
targetInfo['lname'] = input("Enter person's last name: ")
clear()
targetInfo['dob'] = input("Enter person's DOB: ")
clear()
targetInfo['anniversary'] = input('Enter important date, such as an anniversary: ')
clear()
targetInfo['pet'] = input("Enter pet's name: ")
clear()
targetInfo['hometown'] = input("Enter hometown name: ")
clear()
targetInfo['state'] = input("Enter the state the person resides in (formatted with 2 letter state code): ")
clear()
targetInfo['hs'] = input("Enter the name of the person's high school: ")

for i in list(targetInfo):
    if targetInfo[i] == 'n':
        del targetInfo[i]

