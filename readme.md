# 🚗 Car Company Website

<p>
English | <a href="readme-cn.md">中文</a>
</p>

This is a backend database project for a car company, which enables a front-end web application to interact with the local database, perform queries, modifications, and display the results.

## 🌐 Environment

- Python
- Django
- MySQL 8.0.31
- WSL2

## 🛠️ Function Modules

The basic website includes the following function modules:

- Administrator: Directly use SQL command line to query.
- Dealer: Allow a dealer to search for local and other dealer inventories based on specific vehicle characteristics to meet customer needs.
- Online Customers: Design a web interface to facilitate finding dealers and searching for specific products, their inventory, and prices.
- Marketing Department: Provides a simple OLAP query interface for the marketing department.
- Customer Survey: Record customer information in the database after they fill out the information form.
- Services: Display the top sales of brand models and their prices for the current year.

## 👨‍💻 Usage

To run this project, you need to:

1. Clone this repository to your local machine

   ```shell
   git clone https://github.com/WitchPuff/car-company-website
   cd mysite
   ```

2. Install the necessary dependencies

3. Create or connect a MySQL database

   The structure of the default database is defined in `/data/DDL.sql`, and the data is randomly generated by `/data/DataGeneration.py`, stored in `/data/relations.sql`.

   You could connect your own database in `/mysite/mysite/settings.py`:

   ```python
   DATABASES = {
       'default': {
           # 'ENGINE': 'django.db.backends.sqlite3',
           # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
             'ENGINE':'django.db.backends.mysql',
             'NAME':'*', # name of your database
             'USER':'root',
             'PASSWORD':'*',
             'HOST':'localhost',
             'PORT':'3306',
       }
   }
   ```

   Then generate new models:

   ```shell
   python manage.py inspectdb > <your app name>/models.py
   ```

   Add your apps in `mysite/settings.py`:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'company' # add your app(document name)
   ]
   ```

   Migrate your database:

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```

   Finally, modify the interfaces of the models in `mysite/<your app name>/views.py` and the corresponding HTML files.

4. Run the server

   ```shell
   cd mysite
   python manage.py runserver
   ```

Visit here: [http://127.0.0.1:8000](http://127.0.0.1:8000/)

## ⭐It may look like

<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202303231912195.png" alt="image-20230109141624915" style="zoom: 67%;" />



<img src="https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202303231912425.png" alt="image-20230109141821701" style="zoom:67%;" />




![image-20230109143125058](https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202303231912308.png)



![image-20230109141434063](https://raw.githubusercontent.com/WitchPuff/typora_images/main/img/202303231912301.png)



## 💡Reference

[Source code of the front end design](https://www.youtube.com/watch?v=dbTe7pmqLv4)

## 🤝 Contribution

This project is still under development and may have some bugs or incomplete features. Any contributions or suggestions are welcome.
