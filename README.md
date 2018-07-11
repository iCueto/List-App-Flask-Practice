# List-App-Flask-Practice
This is only a simple flask app for practice

## How run the app

1. Clone this repository

2. Install VirtualEnv ``` pip install virtualenv ```

3. Make the enviroment ``` virtualenv env ```

4. ``` source env/bin/activate ```

5. Install the requirements ``` pip install -r requirements.txt ```

6. Then connect to a data-base and make the migration.
     
     ``` python manage.py db migrate ```
     ``` python manage.py db upgrade ```
     
7. If there are no problems run the app: ``` python run.py ```
