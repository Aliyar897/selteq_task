# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Set the entrypoint for the container to run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
