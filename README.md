<!-- ```
virtualenv .
source Scripts/activate
```

You have to create the file in the root of the directory ```env.py```
```
import os

os.environ['CLIENT_ID'] = 
os.environ['SECRET'] = 
``` -->

# Introduction

Introducing my latest solo project - a News Website name **NewsWave** powered by the **Django framework**. I've designed it to deliver the latest news in a smart and sophisticated way, with easy navigation and a user-friendly interface. Join me on this exciting wave of news reporting!

# How to run the Project

1. You have to create the ```env.py``` file in the root of the directory.

```
import os

os.environ['CLIENT_ID'] = 'XXXXXXXXXXXXXXXXXXXXXXX'
os.environ['SECRET'] = 'XXXXXXXXXXXXXXXXXXXXXXX'
os.environ['API_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXX'
```

2. Create the virtual Environment in the root directory.

```
pip install virtualenv

virtualenv .
```

3. Run your virtualenv

- For Windows - PowerShell And Command Prompt

```
.\Scripts\activate
```

- For Linux And Git

```
source Scripts\activate
```

- For MacOs

```
source bin\activate
```

4. Install All dependencies from the requirements.txt File.

```
pip install -r requirements.txt
```

5. Refer this article <https://www.codesnail.com/google-authentication-in-django/> to add all necessary keys in ```env.py``` and **Django Admin**.

6. Now everythings is completed. Check by running the server. <http://localhost:8000/>

- For Windows

```
py manage.py runserver
```

- For MacOs

```
python3 manage.py runserver
```
# File Structure

```
.
|-- core
|    |-- __init__.py
|    |-- asgi.py
|    |-- settings.py
|    |-- urls.py
|    └── wsgi.py
|-- forum
|    |-- __init__.py
|    |-- admin.py
|    |-- apps.py
|    |-- models.py
|    |-- tests.py
|    |-- urls.py
|    └── views.py
|-- news
|    |── templatetags
|    |    └── custom_tags.py
|    |-- __init__.py
|    |-- admin.py
|    |-- apps.py
|    |-- models.py
|    |-- news.py
|    |-- tests.py
|    |-- urls.py
|    └── views.py
|-- static
|    |── assets
|    |    └── (contains website Images)
|    |── css
|    |    └── (contains website CSS)
|    |── js
|    |    └── (contains website Javascript)
|-- templates
|    └── (contains website Html)
|-- user
|    |-- __init__.py
|    |-- admin.py
|    |-- apps.py
|    |-- context_processors.py
|    |-- models.py
|    |-- options.py
|    |-- tests.py
|    |-- urls.py
|    └── views.py
|-- .gitignore
|-- manage.py
|-- README.md
└── requirements.txt
```