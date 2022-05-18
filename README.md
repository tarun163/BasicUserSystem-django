# BasicUserSystem-django

# Requirements
Python 3.8
And additional requirements are in requirements.txt and will be installed through the below steps

# Download
https://github.com/tarun163/BasicUserSystem-django.git

# Run
Install the requirements: $ pip install -r requirements.txt

Make migrations $ python manage.py makemigrations

Migrate the changes to the database $ python manage.py migrate

Run the server $ python manage.py runserver --noreload

# For API
first register your self
create token by  ' http POST http://127.0.0.1:8000/api/gettoken/ username="admin" password="admin" '
verify token , refresh token, get data, post data, update and delete data by JWT token 

