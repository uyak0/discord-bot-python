import random
import json
import os
import time

def load_json_file(file_path):
       with open(file_path, 'r') as file:
           data = json.load(file)
       return data

def is_file_modified(file_path, last_modified_time):
    current_modified_time = os.path.getmtime(file_path)
    return current_modified_time > last_modified_time

def handle_response(message: str) -> str:       #code for handling responses from user
    p_message = message.lower()
    file_path = 'settings.json'
    
    settings = load_json_file(file_path)

    pf_length = settings['pf_length']   

    # RELOADS SETTINGS
    last_modified_time = os.path.getmtime(file_path)
    while True:
        if is_file_modified(file_path, last_modified_time):
            data = load_json_file(file_path)
            last_modified_time = os.path.getmtime(file_path)
        time.sleep(1)  
        break

    message = p_message[pf_length:]     #separate message from prefix

    ### RESPONSES ###
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
    
    #--pick
    if message[:4] == 'pick':   
        if message[4:] == '':
            return 'Please enter some choices!'
        
        else:
            choices = message[4:].split()
            choice = random.choice(choices)
            return choice

    #--setprefix
    if message[:9] == 'setprefix':
        new_pf = message[10:]

        data = load_json_file(file_path)

        # Update the dictionary based on user input
        data['prefix'] = new_pf
        data['pf_length'] = len(new_pf)

        # Write the updated dictionary back to the JSON file
        with open('settings.json', 'w') as file:
            json.dump(data, file)
        file.close()
        
        return 'Your new prefix is: "' + new_pf + '"'   #success message

    #--help
    if message == 'help':
        return  "### __List of Commands__\n"+\
                "```\n"+\
                "1. -ping\n"+\
                "2. -roll  <number> (default: 100)\n"+\
                "3. -help\n"+\
                "4. -pick <choice 1> <choice 2> <choice 3>...\n"+\
                "5. -setprefix <new prefix>\n"+\
                "```"

    return 'I did not understand what your wrote, try again'    #error message

    ### END OF RESPONSES ###