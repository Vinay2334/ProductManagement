import json
from decouple import config

def update_zappa_settings():
    env_vars = {
        "DB_HOST": config('DB_HOST'),
        "DB_NAME": config('DB_NAME'),
        "DB_USER": config('DB_USER'),
        "DB_PASS": config('DB_PASS'),
    }

    with open('zappa_settings.json', 'r') as file:
        zappa_settings = json.load(file)
    
    zappa_settings['production']['environment_variables'] = env_vars

    print("Zappa-set")
    print(env_vars)
    print(zappa_settings)

    with open('zappa_settings.json', 'w') as file:
        json.dump(zappa_settings, file, indent=4)
    
if __name__=="main":
    update_zappa_settings()