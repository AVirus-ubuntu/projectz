# created By AVirus 🦊
### This is simple tg-bot for mailing
> ___`bash: Installing `___
> ```bash
> sh _install.sh
> ```

> ___`edtr: Configuring`___
> ```py
> # .env
> 
> TOKEN =    "_" # bot Token     ("SECRET")
> DATABASE = "_" # database path ("./database/_.sql")
> ```
>
> ```py
> # __config__.py
> 
> from dotenv import dotenv_values
> 
> class cfg:
>     TOKEN = dotenv_values('.env')['TOKEN']
>     DATABASE = dotenv_values('.env')['DATABASE']
>     ADMINSID = [0, 1, 2] # admins userid ("SECRET")
> ```

> ___`bash: Running    `___
> ```bash
> sh _run.sh
> ```