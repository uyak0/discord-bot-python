import random

def handle_response(message: str) -> str:       #code for handling responses from user

    p_message = message.lower()
    cmd = p_message[:1]         #separate command from message
    message = p_message[1:]     #separate message from command

    if cmd == '!':          #check for command
        if message == 'hello':
            return 'Hey there'
        
        if message == 'roll':
            return str(random.randint(1, 6))
        
        if message == '!help':
            return "`this is a help message that you can modify`"
        
        return 'I did not understand what your wrote, try again'