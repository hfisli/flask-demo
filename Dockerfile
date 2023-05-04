FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Run the command to start the app
CMD [ "flask", "run", "--host=0.0.0.0", "--port=8080" ]