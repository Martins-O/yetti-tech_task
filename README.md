# YETTI-TECH_TASK

#### This repository contains a Django project that demonstrates user authentication and includes comprehensive tests. Follow the instructions below to set up the project and run the tests.
## Installation and Setup
1. Clone the repository to your local machine:
```bash
git clone https://github.com/Martins-O/yetti-tech_task.git
cd yetti-tech_task
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
```
3. Install the project dependencies:
```bash
pip install -r requirements.txt
```
4. Apply database migrations:
```bash
python manage.py migrate
```
5. Create a superuser account for admin access:
```bash
python manage.py createsuperuser
```
#### Follow the prompts to create an admin account
6. Start the development server:
```bash
python manage.py runserver
```
The application will be accessible at: ``http://127.0.0.1:8000``.

### Running Tests
To run the tests for users authentication and security:
```bash
python manage.py test
```
### Project Structure
- 'yetties-tech/': The Django app containing views, templates and tests.
- 'yetties-tech/': The Django app project settings and URL configuration.
- 'template/registration': HTML templates for registration and login forms.

### Usage
1. Register a new user:

   - Open your browser and navigate to ``http://127.0.0.1:8000/register/``.
   - Fill out the registration form with a username and password.

2. Log in as the registered user:

   - Go to ``http://127.0.0.1:8000/login/``.
   - Enter the username and password you used during registration.

3. Access the "Hello World" page:

   - After logging in, go to ``http://127.0.0.1:8000/hello_world/``.

4. Log out:

   - To log out, visit ``http://127.0.0.1:8000/logout/``.

### Additional Notes:
- User registration, login, and access control have been implemented and tested.
- Security features like CSRF protection and session management are included by default.
- Edge cases and error scenarios have been tested to ensure robustness.
- Feel free to explore and modify the code to fit your specific project requirements.