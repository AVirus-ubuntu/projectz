from dotenv import dotenv_values

class cfg:
    TOKEN = dotenv_values('.env')['TOKEN']
    DATABASE = dotenv_values('.env')['DATABASE']
    ADMINSID = [768784246]