import random

def handle_response(message: str) -> str:       #code for handling responses from user
    p_message = message.lower()
    cmd_length = 1
    cmd = p_message[:cmd_length]         #separate command from message
    message = p_message[cmd_length:]     #separate message from command

    if cmd == '-':          #check for command
        #--ping
        if message == 'ping':
            return 'pong :ping_pong:'
        
        #--roll
        if message[:4] == 'roll':
            if message[4:] == '':
                return str(random.randint(1, 100))

            else:
                number = int(message[4:])
                randomnum = random.randint(1, number)
                return str(randomnum)
        
        if message[:4] == 'pick':
            


        #--help
        if message == 'help':
            return  "### __List of Commands__\n"+\
                    "```\n"+\
                    "1. -ping\n"+\
                    "2. -roll  <number> (default: 100)\n"+\
                    "3. -help\n"+\
                    "```"

        return 'I did not understand what your wrote, try again'