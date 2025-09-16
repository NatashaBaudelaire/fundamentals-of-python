print('Hello, world!')
msg = input('Enter your message:')
print('You wrote: ' + msg)

print('I liked your message! This is Lumi speaking. ')
name = input('What is your name? ')
print('Hello! Nice to meet you, ' + name + '.')

print('That\'s a brilliant name! I\'m glad we\'re talking, ' + name + '.')


response = input('Do you like programming in Python? (yes/no) ')
if response.lower() == 'yes':
    print('That\'s awesome, ' + name + '! Programming in Python is like magic, isn\'t it?')

elif response.lower() == 'no':
    print('No worries, ' + name + '. There are many other cool things to enjoy.')
else:
    print('Interesting answer, ' + name + '! I\'m learning something new every day.')
    

hobby = input('By the way, ' + name + ', what is your favorite hobby? ')
print('Wow, ' + hobby + ' sounds really fun! I\'d like to learn more about it someday.')


mood = input('How are you feeling today? ')
if 'good' in mood.lower() or 'happy' in mood.lower():
    print('I\'m glad to hear that, ' + name + '! Keep smiling 😄')
elif 'sad' in mood.lower() or 'not good' in mood.lower():
    print('I\'m sorry to hear that, ' + name + '. I hope your day gets better!')
else:
    print('Thanks for sharing, ' + name + '. I appreciate your honesty.')


msg = input('Enter your message:')
def display_message():
    global msg
    print(msg)

    print('It was lovely talking with you today, '+ name +'. See you next time!')