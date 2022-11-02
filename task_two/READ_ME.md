 Solution Info

API is a Flask app with a simple SQLAlchemy ORM to interact with the DB.

Given the simplicity of the requirements, these were both choices based on being relatively lightweight and quick to develop.

The app accepts JSON requests with a 'city' key, and returns JSON response with a 'temp' key.
If a city was requested in the last two hours, the last result is read out of the DB (note this is following instruction 4, which seems at slight odds with instruction 3 below which says 4 hours)

### How to run the project

**Activate the venv**

(example given for windows from within task_two directory:)
```
flask_env\Scripts\activate 
```
(Would usually instructions/requirements for a venv, but including as requested)

**Run the server**
```
cd app
python app.py
```
**Invoke API**

Send requests from e.g. a python console:
```
import requests
r = requests.post('http://127.0.0.1:5000/', json={'city':'Bangkok'})
r.content
```


