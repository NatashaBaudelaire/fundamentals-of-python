def show_message():
    print('Message shown from the function')

def return_message(message):
    new_message = message + ' Returned Message'
    return new_message

show_message()
msg = 'test'
print(return_message(msg))