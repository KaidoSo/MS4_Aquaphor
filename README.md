<h1 align="center">
Data Centric Development - Milestone Project 4 - Aquaphor by Kaido Soomlais
</h1>

<div align="center">
    <img src="https://ibb.co/19YQv5B" href="https://https://kaidoso-ms4-aquaphor.herokuapp.com/" target="_blank" alt="" border="0">
</div>

[Aquaphor](https://https://kaidoso-ms4-aquaphor.herokuapp.com/) website created for a user to purchase water filter products. 
It has been made so that the user can easily read & navigate around the website. Functionality has been added to allow purchasing a product quick & easy.
Registration & log in has also been made simple & hassle-free along with information on user profile & order history. It makes a great website for purchasing products.
<br><br>

<h1>Table of Contents</h1>

1. [**UX**](#ux)
    - [**Project Purpose**](#project-purpose)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design Choises**](#design-choises)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
        - [Context Sensitive NavBar](#context-sensitive-navbar)
        - [Error Handling](#error-handling)
    - [**Features Left to Implement**](#features-left-to-implement)
        - [Reviews](#reviews)
        - [Pagination](#pagination)
        - [Forgot Password](#forgot-password)
3. [**Testing**](#testing)
    - [**Tools and Methods For Testing**](#tools-and-methods-for-testing)
        - [HTML](#html)
        - [CSS](#css)
4. [**Bugs**](#bugs)
    - [**Bugs During Development**](#bugs-during-development)
    - [**Known Bugs**](#known-bugs)
5. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choise)
    - [**Data Tables**](#database-tables)
6. [**Technologies Used**](#technologies-used)
    - [**Tools**](#tools)
    - [**Databases**](#databases)
    - [**Libraries**](#libraries)
    - [**Languages**](#languages)
7. [**Deployment**](#deployment)
    - [**Local IDE**](#local-ide)
    - [**Instructions**](#instructions)
    - [**Deploy to Heroku**](#deployment-to-heroku)
8. [**Credits**](#credits)
    - [**Acknowledgements**](#acknowledgements)
9. [**Disclaimer**](#disclaimer)




The main objective in creating the Aquaphor application is to provide the user with a simple shopping website to purchase water filter products.
As a side goal, I have left room for expansion once I have developed my skills further. I would like to develop this into a more viable website with added features as outlined below in the [**Features Left to Implement**](#features-left-to-implement).


## UX

#### Project Purpose

The goal of Aquaphor is to give the user an easy and quick experience when purchasing water filter products, 
ensuring that all actions are made as quick, simple & effective as possible such as:

- Registration
- Log in
- Finding a product
- Viewing a product
- Searching for a product
- Adding products to the cart
- Adjusting the quantity of item(s) in cart
- Removing item(s) from cart
- Easy payment process
- Viewing Order History


### User Stories

 **I want for a user to have:**
 1. A website that is easy to navigate.
 2. A website which is pleasant to look at.
 3. A way to see images of the products that are available on the website as soon as a user goes to the website.
 4. Buttons which are simple but informative & give a good indication of their purpose.
 5. An application that is fast, with very short load times.
 6. All of the relevant information given to user at the appropriate time.


### Wireframes

Wireframes were built in the early stages of development to get a rough outline of the structure needed for the planned features of the site. These can be viewed below:

- [Desktop](https://ibb.co/Jr75HcC)
- [Desktop Product View](https://ibb.co/Wft9qjL)
- [Mobile](https://ibb.co/0BvXrrN)

### Design Choices

The main approach to this application is made to easy to maintain, and easy to use database. To provide features that make the entire experience simple. The following design choices were made to reflect this:

**Fonts**

- The main body font **Roboto** was chosen due to it's simplistic yet professional design.

**Colours**

- The colour choices were made to be fit Aquaphor #0049bc blue logo.
- Colours of **light grey** and **off white** were chosed to not overload the user, and maintain a simple, clean look.

**Styling**

- **Bootstrap** framework was used to keep the site simple, only displaying relevant information, without drawing attention away from the content.
- **Buttons** have been styled with bootstrap & colors have been picked using bootstrap color shceme.


## Features

### Existing Features


1. **Context Sensitive NavBar**
    - The navbar has been created to change from a SignIn button and SignUp buttons when not logged in, to welcoming user and SignOut buttons when signed in.

2. **Error handling**
    - A system is in place should a user try to access the orders history page, and they are not logged in.
    - Should a user try the above, they will be immediately redirected to the login page. This also occurs with any registered user only features.
    

### Features Left to Implement

1. **Reviews**

I would like to impliment a system that allows user to review products.

2. **Pagination**

Current website would get very cluttered if lot more products are added. I want to add that option for a user to view different pages of products.

3. **Forgot Password**

User could definitely do with forgot password function.


## Testing

### Tools and Methods Used for Testing

- HTML

  - [The W3C Markup Validation Service](https://validator.w3.org/)

- CSS

  - [The W3C Markup Validation Service](https://jigsaw.w3.org/css-validator)

Both virtual and real device tests were run to test and access the functionality of the app and identify any potential errors. Although the app UI aesthetics are not 
a high priority requirement for this project, the app responsiveness was also tested by resizing the window. Below is a full list of devices used in the testing phase:

Simulated with Chrome DevTools:
Moto G4,
Galaxy S5,
Pixel 2,
Pixel 2 XL,
iPhone 5/SE,
iPhone 6/7/8,
iPhone 6/7/8 Plus,
iPhone X,
iPad,
iPad Pro

Physical Devices:
Samsung Galaxy S10E,
Sony Xperia XZ1 Compact,
Lenovo ThinkBook M-14 IML

Tested Sections HTML CSS:
 - Links to navigate within website and code authors GitHub repository.
 - Checked button sizes so, they were responsive and large enough to be clicked.
 - Spell checked all text content.
 - HTML and CSS validation via w3.org (only Bad Value errors with {url_for} links remained).
 - Created several users with and without intentional input errors during filling out the forms.

## Bugs

##Bugs During Development##

-**Fixtures**
When trying to dump data into fixtures and load to heroku, it kept giving me errors due to the fact that copied Product information included some non acii characters.
Solution - replaced all product description with Lorem Ipsum.

-**Products not displaying**
Locally products will not display when removing 'static' from MEDIA_ROOT. However they will not display in Heroku without removing it.
Solution - added 'static' to MEDIA_ROOT in my final commit, but did not upload it to Heroku. I know that there should be a better solution, but this is the best I could come up with for the time being.


### Known Bugs

- **Order History**
Order History not displaying in Heroku. It works locally, and when a user is making a purchase, it also logs it in admin database, but I could not understand why it is not in Heroku.

-**Favicon**
Favicon not displaying in Heroku.

- **Footer not sticking to bottom**
Footer is not on the bottom when there is not enough info to push it down naturally.
I left this minor thing in after trying to solve it and will fix it later, due to lack of time.

-**New Branch**
The reason behing having a new branch in the github was due to failure at first attempt to deploy to Heroku, messing up my code and not knowing how to go back to previous save locally.
I went back to GitHub and split the branch, then pulled from new branch to VSCode and continued my work. Later I learned how to revert locally using git log and git reset --hard commands.


## Information Architecture

### Database Choice

As default, sqlite3 is installed with Django so that was the choice of database to work with in development.
When deployed to Heroku, I used PostgreSQL database which was provided by Heroku.

### Database Tables

User Model already comes as standard.

**Category Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=250, unique=True | CharField
Slug | slug | max_length=250, unique=True | SlugField
Description | description | blank=True | TextField
Price | price | max_digits=10, decimal_places=2 | DecimalField
Image | image | upload_to='category', blank=True | ImageField


**Product Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Name | name | max_length=250, unique=True | CharField
Slug | slug | max_length=250, unique=True | SlugField
Description | description | max_length=250, blank=True | TextField
Price | price | max_digits=10, decimal_places=2 | DecimalField
Image | image | upload_to='product', blank=True | ImageField
Stock | stock | none | IntegerField
Available | available | default=True | BooleanField
Created | created | auto_now_add=True | DateTimeField
Updated | updated | auto_now=True | DateTimeField


**Cart Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Cart ID | cart_id | max_length=250, blank=True | CharField
Added | date_added | auto_now_add=True | DateTimeField

**Cart Item Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Product | product | Product, on_delete=models.CASCADE | ForeignKey
Cart | cart | Cart, on_delete=models.CASCADE | ForeignKey
Quantity | quantity | none | IntegerField
Active | active | default=True | BooleanField

**Order Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Token | token | max_length=250, blank=True | CharField
Total | total | max_digits=10, decimal_places=2 |DecimalField
EmailAddress | emailAddress | max_length=250, blank=True | EmailField
Created | created | auto_now_add=True | DateTimeField
Billing Name | billingName | max_length=250, blank=True | CharField
Billing Address | billingAddress1 | max_length=250, blank=True | CharField
Billing City | billingCity | max_length=250, blank=True | CharField
Billing Postcode | billingPostcode | max_length=250, blank=True | CharField
Billing Country | shippingCoutry | max_length=250, blank=True | CharField
Shipping Name | shippingName | max_length=250, blank=True | CharField
Shipping Address | shippingAddress1 | max_length=250, blank=True | CharField
Shipping City | shippingCity | max_length=250, blank=True | CharField
Shipping Postcode | shippingPostcode | max_length=250, blank=True | CharField
Shipping Country | shippingCoutry | max_length=250, blank=True | CharField

**Order Item Model**

| Name | Key in db | Validation | Field Type |
--- | --- | --- | ---
Product | product | max_length=250 | CharField
Quantity | quantity | none | IntegerField
Price | price | max_digits=10, decimal_places=2 | DecimalField
Order | order| Order, on_delete=models.CASCADE | ForeignKey



## Technologies Used

### Tools
- [Visual Studio Code](https://code.visualstudio.com/) This was the choice of IDE for this project. 
- [Django](https://www.djangoproject.com/) was used as part of the credentials for this project as it's a python web framework is used for accelerated custom web application development.
- [Stripe](https://stripe.com) is used for easy & secure payment.
- [AWS S3 Bucket](https://aws.amazon.com/) to store all images that are on the website.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) enables developers to create, configure, and manage AWS services.
- [PIPENV](https://pipenv-fork.readthedocs.io/en/latest/) provides users and developers of applications with an easy method to setup a working environment.
- [Gunicorn](https://pypi.org/project/gunicorn/) is a Python Web Server Gateway Interface HTTP server which is used to help the deployment of a Django project in Heroku.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is used to create nicely styled forms.
- [Psycopg2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for the Python programming language.
- [Pillow](https://pillow.readthedocs.io/en/stable/) is used to help the uploading of images in the database.
- [Django Heroku](https://pypi.org/project/django-heroku/) is used to view the deployed project.
- [Imgbb](https://imgbb.com) used to store images mainly for readme.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control of the website.
- [GitHub](https://github.com/) is used as a remote backup of code used in the project & used to showcase code remotely.
- [Balsamiq](https://balsamiq.com/) was used to create wireframes to show the layout of the website.


### Databases

- [SQlite3](https://www.sqlite.org/index.html) is installed with Django as default so that was the choice of database to use in development.
- [PostgreSQL](https://www.postgresql.org/) is the database I used which was provided by Heroku & this was used when my project was deployed to Heroku.


### Libraries
- [JQuery](https://jquery.com) has been used to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to assist with website layout & styling.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to apply informative icons used throughout the website.
- [Google Fonts](https://fonts.google.com/) is used to provide a **'Roboto'** font which is used throughout the website.


### Languages
- The languages used throughout the website are HTML, CSS, JavaScript & Python.




## Deployment

### Local IDE

The project was built using [Visual Studio Code](https://code.visualstudio.com/), through a built-in function called 'Git', I could commit my files.

- You must ensure that the following are installed on your machine before you can work with it in your IDE.
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

- You need to create an account for each of these to be able to get the website functioning properly
    - [Stripe](https://dashboard.stripe.com/register)
    - [Gmail](https://www.gmail.com/)
    - [AWS](https://aws.amazon.com/) which you want to set up an [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

### Instructions

1. Go to https://github.com/KaidoSo/MS4_Aquaphor and click the 'Clone or download' button and then click 'Download ZIP'
& extract to a folder of your choice. Ensuring you have Git installed on your system, you can clone the project into
your IDE through running the following command in the terminal
```console
git clone https://github.com/*username*/*repository*
```

2. Ensure you have open a terminal (Some IDE's such as Cloud9 & VSCode have a built-in terminal but if not, you may need to open one up on your desktop), cd to the correct location to where you have your ZIP file.

3. if running in Cloud9, you won't need to do this step as it comes with a built-in virtual environment but if it doesn't,
you need to run the following command to build a virtual environment:
```
python pipenv shell
```

4. Should you need to the latest version of pip, you can get it by running the following command.
```
pip install --upgrade pip
```

5. If your IDE requires a virtual environment, run the following command to activate it:
```
source venv\Scripts\activate 
```
_This may vary so be sure to check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) to make sure you're sure._

6. Install a requirements.txt file with of the correct packages that you need for the project with: 
```
pip -r requirements.txt
```
_Check to ensure that you have all of the required packages you need for the project._

7. You then need to set up environment variables, the following steps:
- Create an env.py file & a .gitignore on the root level of your project & add the text env.py to your .gitignore file.
- In your env.py file, add import os on the top line & create environment variables like this... os.environ["YOUR_VARIABLE_NAME"] = "Value goes in string here"

```
import os

os.environ["SECRET_KEY"] = "<secret key here>"
os.environ["DEVELOPMENT"] = "1"
os.environ["EMAIL_ADDRESS"] = "<email address here>"
os.environ["EMAIL_PASSWORD"] = "<email address password here>"
os.environ["STRIPE_PUBLISHABLE"] = "<stripe publishable key here>"
os.environ["STRIPE_SECRET"] = "<stripe secret key here>"
os.environ["DATABASE_URL"] = "<data url which can be found in heroku after you have deployed the project>"
os.environ["AWS_ACCESS_KEY_ID"] = "access key id here>"
os.environ["AWS_SECRET_ACCESS_KEY"] = "<secret access key here>"
```

- ^ Add that to your settings.py file under where you import os & then say for secret key, it should be SECRET_KEY = os.environ.get('SECRET_VARIABLE_SET_IN_env.py')
Then you can do a print(os.environ.get('SECRET_VARIABLE_SET_IN_env.py'))

- If you are using an IDE that has a `bashrc` file. Open that file & add variables that are listed above in this format:
```
SECRET_KEY = "<secret key here>"
DEVELOPMENT = "1"
EMAIL_ADDRESS = "<email address here>"
EMAIL_PASSWORD = "<email address password here>"
STRIPE_PUBLISHABLE = "<stripe publishable key here>"
STRIPE_SECRET = "<stripe secret key here>"
DATABASE_URL = "<data url which can be found in Heroku after you have deployed the project>"
AWS_ACCESS_KEY_ID = "<access key id here>"
AWS_SECRET_ACCESS_KEY = "<secret access key here>"
```

- `DEVELOPMENT` environment variable is only in development. It will not be shown in deployment so you can use this for things such as setting DEBUG mode to True in development & False if it's on the deployed website.

8. Restart your machine & reactivate your environment variable, use the command used in step 5.

9. Migrate all of the models & creating an SQLite database by using the commands:
```
python manage.py makemigrations
python manage.py migrate
```

10. Create a superuser to be able to gain access to the admin panel. You can do this by typing the following command & following the instructions

```
python manage.py createsuperuser
```

11. Run the project on your local machine using the command:
 ```
python manage.py runserver
```

12. You will now have the project up & running. At the end of the URL add `/admin` & login with the superuser credentials you created to get access, if you want to view products & banners on the website, you can start adding information into the models.

13. You should now be good to go. If you get stuck at any point, go back through all of the previous steps.

### Deploy to Heroku

1. If you haven't already, install a requirements.txt file with of the correct packages that you need for the project with: 
```
pip -r requirements.txt
```

2. You need to run the command `echo web: python app.py > Procfile` which will create a Procfile.

3. Use `git add .` to stage all of your files `git commit -m "<message here>"` to commit the changes ready to push to GitHub.

4. You must then create a repository in GitHub & follow the instructions in order to push your work up to GitHub.

5. Using `git push` & inputting your email & password when instructed, this will push all of the files.
that have been committed up to GitHub.
_Note that the password field will not change when you are inserting text_

6. Go to heroku [here](https://dashboard.heroku.com/) & ensure you are signed up.

7. Go to your Heroku dashboard & click "New" & click "Create New App".

8. Give any name you like & set the region to "Europe".

9. Ensure you link the Heroku application to the correct GitHub repository.

10. From the dashboard, go to "Settings" & click on "Reveal Config Vars"

11. Set the following Config Vars to:

| Key | Value|
--- | ---
SECRET_KEY | `<secret key here>`
DEVELOPMENT | `1`
EMAIL_ADDRESS | `<email address here>`
EMAIL_PASSWORD | `<email address password here>`
STRIPE_PUBLISHABLE | `<stripe publishable key here>`
STRIPE_SECRET | `<stripe secret key here>`
DATABASE_URL | `<data url which can be found in Heroku after you have deployed the project>`
AWS_ACCESS_KEY_ID | `<access key id here>`
AWS_SECRET_ACCESS_KEY | `<secret access key here>`


12. Go to the command line on your local IDE:
    - Add Heroky postres shell
    - migrate all of the data models using the following command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    - Create a superuser for your new database

    Click on [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql) to find steps on how this is done.

13. Go back to your Heroku & go to Deploy, Scroll down the page to find "Manually Deploy", select master & click "Deploy Branch".

14. Wait until the build is complete & click on "View".

15. You will now have the project up & running in Heroky. At the end of the URL add `/admin` & login with the superuser credentials you created to get access, if you want to view products & banners on the website, you can start adding information into the models.

16. You should now be good to go. If you get stuck at any point, go back through all of the previous steps.


## Credits

### Acknowledgements

Code for structure and layout was partially inspired by the [The Zero2Launch Team](https://zero2launch.io/)

I would like to thank Code Institute for giving me deadline extension to submit this project.

## Disclaimer
I completed this project whilst not having access to Code Institute support, Tutors or Mentor.
While this project does not look overly nice, has some bugs and could definitely do with some improvements,
I learned the most while working without independently and take pride in putting it together and deploying it with no outside help. 
Running into plethora of problems, errors, sweating, panic and despair,
but making it functional and working both on local and Heroku.
Please take that into account when grading it.

Images for the website were used with permission from the owner of [Aquaphor.eu](https://aquaphor.eu/), such as banners & products.

Please note that all code and images in this site are for educational purposes only. Created only to show my abilities in the language of Python/Django. 