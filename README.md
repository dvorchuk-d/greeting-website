# Greeting_website

This project allows you to say 'Hello' to the world
using your email as an alias.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The Python 3.8 should be installed on your local machine.

### Installing

To run locally, do the usual:
1. Create a Python 3.8 virtualenv
2. Install dependencies:

```
pip install -r requirements.txt
npm install
```

3. Set your SECRET_KEY in greeting_site/settings.py:

```
SECRET_KEY = 'YOUR_KEY'
```

4. Create a superuser:

```
python manage.py createsuperuser
```

5. Run the server:

```
python manage.py runserver
```

## Running Locally with Docker

1. Build the image:

```
docker build -t greeting_site .
```

2. Spin up the container:

```
docker run -d -p 8000:8000 --rm greeting_site
```

3.View the site at http://localhost:8000/

## Built With

* [Django](https://docs.djangoproject.com/en/4.0/) - The web framework used


## Author

* **Danil Dvorchuk** 



