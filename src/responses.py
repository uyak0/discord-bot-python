import random
import json
import os
import time
import discord

def load_json_file(file_path):
       with open(file_path, 'r') as file:
           data = json.load(file)
       return data

def is_file_modified(file_path, last_modified_time):        #temporary way to have a settings without setting up backend
    current_modified_time = os.path.getmtime(file_path)
    return current_modified_time > last_modified_time

def accept_reply(message: discord.Message):
    return message.content

def handle_response(message: discord.Message):       #code for handling responses from user

    #Note: at this point, variable "message" is of class discord.Message
    file_path = 'config/config.json'
    
    settings = load_json_file(file_path)

    pf_length = settings['pf_length']       #prefix length

    # RELOADS SETTINGS each second 
    # so that prefix can get updated when its changed 
    last_modified_time = os.path.getmtime(file_path)
    while True:
        if is_file_modified(file_path, last_modified_time):
            data = load_json_file(file_path)
            last_modified_time = os.path.getmtime(file_path)
        time.sleep(1)  
        break
    
    strMessage = str(message.content)            #convert variable 'message' to string, 'message' remains of class discord.Message, 'strMessage' is used for matching user messages
    strMessage = strMessage[pf_length:]          #separate message from prefix

    ### RESPONSES ###
    match strMessage:
        #--ping
        case 'ping':
            return 'pong :ping_pong:'
    
        #--roll
        case 'roll':
            if strMessage[4:] == '':
                return str(random.randint(1, 100))

            else:
                number = int(strMessage[4:])
                randomnum = random.randint(1, number)
                return str(randomnum)
        
        #--pick
        case 'pick':   
            if strMessage[4:] == '':
                return 'Please enter some choices!'
            
            else:
                choices = message[4:].split()
                choice = random.choice(choices)
                return choice

        #--setprefix
        case 'setprefix':
            new_pf = strMessage[10:]

            data = load_json_file(file_path)

            # Update the dictionary based on user input
            data['prefix'] = new_pf
            data['pf_length'] = len(new_pf)

            # Write the updated dictionary back to the JSON file
            with open(file_path, 'w') as file:
                json.dump(data, file)
            file.close()
            
            return 'Your new prefix is: "' + new_pf + '"'   #success message

        #--leguess
        case 'leguess':
            answer = random.choice(['🍎','🍌','🍊'])
            return 'Take a guess', ['🍎','🍌','🍊']
            
        #--help
        case 'help':
            with open('help.txt', 'r') as file:
                helptext = file.read()
            return helptext
        
        #default case
        case _:
            return 'I did not understand what your wrote, try again'    #error message
    
    ### END OF RESPONSES ###