# Mruzo/learn-django

# Getting started

1. Clone this project:

    ```bash
    git clone https://github.com/Mruzo/learn-django.git
    cd learn-django/
    ```

2. Activate the Python Virtual Environment:
    * Windows/cmd:

        ```cmd
        cd Scripts
        activate.bat
        ```

    * POSIX/bash:

        ```bash
        . bin/activate
        ```

    * POSIX/fish:

        ```fish
        . bin/activate.fish
        ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Start django server

    ```bash
    cd mysite/
    python manage.py runserver # or python3 manage.py runserver
    ```
