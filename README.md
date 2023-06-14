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



# Additional Resources

* Django Documentation
* Django Project Website
* Django GitHub Repository
