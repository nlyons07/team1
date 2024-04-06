This application creates a very simple online bakery store.
The application uses Django 'sessions' to manage the cart. The Django 4.0 by example textbook also includes a
version of this application for your reference. This version is simpler than the version detailed in the textbook, however.
The shopping cart has specific items defined in the settings.py file. 

This version is updated to work with Django 5 and Python 3.11 and implements product inventory.
The number of items that can be added to the cart is based on the number in inventory.
See the 'cart/forms.py'

This application was created as a group project for the ISQA Web Application Development Course

To use this application:
Start PyCharm and close any projects


Run the application server by entering the following command in the Terminal window:
python manage.py runserver

Run the server as Admin to add new Categories and Products to the database.
http://127.0.0.1:8000/admin

View the application in your browser and add and remove items to and from the cart. Place an order
http://127.0.0.1:8000

Project Organization:
1. 'myshop' is the main project app
2. 'orders' and 'shop' are apps created as part of this project
3. 'cart' is the shopping cart managed through Django sessions.

If an Error occurs when installing Pillow:
To use Pillow with Python 3.8.x - upgrade pip to the most recent version (20.x)
easy_install -U pip

Then, install the requirements for the project:
pip install -r requirements.txt

Then create the database:
python manage.py makemigrations
python manage.py migrate
