## Prerequisites
Before setting up a Django project, ensure that you have the following prerequisites installed:

* Python (version 3.9 or later)
* pip (Python package installer)
* Virtual environment tool (e.g., venv or virtualenv)

### Setup Instructions
Follow these steps to set up a Django project:

1. Clone the project repository:
```bash
git clone <repository_url>
```
Alternatively, you can download the project source code as a ZIP file and extract it.

And create .env file with the following contents as mentioned below:
```
DEBUG=True
DJANGO_SECRET_KEY=django-insecure-#z9ho$ky
```
2. Create a virtual environment for the project:
```python
python3 -m venv env
```
Replace myenv with the desired name for your virtual environment.

3. Activate the virtual environment:

For Windows:
```bash
myenv\Scripts\activate
```
For macOS/Linux:
```bash
source myenv/bin/activate
```
4. Install the project dependencies:
```bash
pip install -r requirements.txt
```
This command will install all the required packages specified in the requirements.txt file.

5. Perform initial database migrations:

```python
python manage.py makemigrations
```
And then to run to reflect all the changes in the databases
```python
python manage.py migrate
```
This will create the necessary database tables.

6. (Optional) Create a superuser account:
```python
python manage.py createsuperuser
```
This will prompt you to enter a username, email, and password for the superuser account. The superuser account can be used to access the Django administration interface.

Run the development server:

```bash
python manage.py runserver
```
The development server will start running locally at http://localhost:8000/.

Open a web browser and visit http://localhost:8000/ to view the project.


## This repository create for Userprofile creating and updating and it contains 3 rest APIS

* To get Token for user authorization 
```python
import requests
import json

url = "http://127.0.0.1:8000/api-token-auth/"

payload = json.dumps({
  "username": "admin123",
  "password": "Qwaszx12@"
})
headers = {
  'Authorization': '"Token": "e592fe5f6b2957894ccc36ff812d61e945d3bd57"',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

* We will hit user_profile api to create a new required with authorization token 

```python 
import requests

url = "http://127.0.0.1:8000/profile/user_profile/"

payload = {
    'name': 'suman',
    'email': 'test@test.com',
    'bio': 'I am sonal'}
    files=[
    ('picture',('3.png',open('/C:/Users/Rajansahu/Pictures/3.png','rb'),'image/png'))
]
headers = {
  'Authorization': 'Token e592fe5f6b2957894ccc36ff812d61e945d3bd57'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```

* This endpoint is using to update the records of userproject data(if neccesary) 
```python
import requests

url = "http://127.0.0.1:8000/profile/user_profile/?id=5"

payload = {}
headers = {
  'Authorization': 'Token e592fe5f6b2957894ccc36ff812d61e945d3bd57'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
```



# Additional Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Project Website](https://www.djangoproject.com/)
- [Django GitHub Repository](https://github.com/django/django)
