print('-------------------------------- OPTION 1 --------------------------------')

phrase = "Seven"
plist = list(phrase)
print(phrase)
print(plist)


for i in range(2):
    plist.pop()

plist.pop(0)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

print('-------------------------------- OPTION 2 --------------------------------')

phrase2 = "Seven"
plist2 = list(phrase2)
print(phrase2)
print(plist2)

new_phrase2 = ''.join(plist2[1:3]) + ''.join(plist2[3:5])
print(plist2)
print(new_phrase2)
