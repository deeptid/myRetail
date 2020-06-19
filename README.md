# myRetail App

This project is built using the Django Rest framework.

* First clone this repository.

   ```bash
   $ git clone https://github.com/deeptid/myRetail.git
   $ cd myRetail
   ```

* Create a virtual Environment.

   ```bash
   $ python manage.py venv venv
   $ source venv/bin/activate
   ```

* Create the database and run migrations.

   ```bash
   $ python manage.py migrate products
   ```

* Start the server.

   ```bash
   $ python manage.py runserver
   ```

Open any browser and visit http://localhost:8000. You can see the product search page