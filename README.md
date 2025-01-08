# Selteq Task Django Project

This README provides step-by-step instructions on how to set up and run the Selteq Task Django project on Windows.

## Cloning the Repository

First, you need to clone the repository from GitHub.

```bash
git clone https://github.com/Aliyar897/selteq_task.git
```

## Setting Up a Virtual Environment

Navigate into the cloned repository directory and create a virtual environment.

```bash
cd selteq_task
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

## Installing Dependencies

Install the required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

## Running the Django Development Server

To start the Django development server, use the following command:

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

## Setting Up Celery Workers

To start the Celery worker, use the following command:

```bash
celery -A selteq_task worker --pool=solo -l info
```

## Starting Celery Beat Scheduler

To start the Celery Beat scheduler, use the following command:

```bash
celery -A selteq_task beat -l info
```

## Notes

- Ensure that you have RabbitMQ or another message broker running if required by your Celery configuration.
- For production deployment, additional steps such as configuring a web server (e.g., Gunicorn, Nginx) and using a production-ready database are recommended.

## Troubleshooting

If you encounter any issues, make sure:

- You have activated the virtual environment.
- All dependencies are installed correctly.
- RabbitMQ or another message broker is running.

## postman collections
 - open the attached postman collection in postman or thunder client
 - Get the token using Get token api
 - The token expriry is 5 min
 - Use other api's to add, update and delete task 

This project is licensed under the MIT License. See the LICENSE file for more details.

