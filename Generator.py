import random
import configuration
import Reader
import Writer
import string
def generate_password(config:configuration)->str:
    chain:string=""
    for i in range(config.size):
        chain =  chain + get_random_char(config)
    return chain

def get_random_char(config:configuration)->str:
    char:str =""
    selector = random.randint(1, 4); 
    if selector == 1:
        char = char + config.lower[random.randint(0, len(config.lower)-1)]
    elif selector == 2:
        char = char + config.upper[random.randint(0, len(config.upper)-1)]
    elif selector == 3:
        char = char + config.special[random.randint(0, len(config.special)-1)]
    else:
        char = char + config.number[random.randint(0, len(config.number)-1)]
    return char

print(generate_password(Reader.config_getter()))