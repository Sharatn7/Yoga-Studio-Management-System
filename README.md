# Flex_assignment
Yoga application module done using HTML, CSS and Django.
 
* **This is a reception/help desk perspective based application, where a yoga student or prospective student can view their details or register as student respectively.**
* **The processes are based of the Id that's generated for each student uniquely upon registration, which is used for viewing their details, making payments, and requesting for slot change.**
* **Currently the application updates the data when the display function is called, for future upgrade it can be auto run using scheduler so that the data gets updated every day(maybe midnight)**

 
 ## In this application
* **Only people within the age limit of 18-65 can enroll for the monthly classes and they will
be paying the fees on a month on month basis. I.e. an individual will have to pay the fees
every month and he can pay it any time of the month.**
* **They can enroll any day but they will have to pay for the entire month. The monthly fee is
500/- Rs INR.**
* **There are a total of 4 batches a day namely 6-7AM, 7-8AM, 8-9AM and 5-6PM. The
participants can choose any batch in a month and can move to any other batch next
month. I.e. participants can shift from one batch to another in different months but in
same month they need to be in same batch**

# To run the Django project 

1) cd to development directory
2) mkvirtualenv flexproject
3) mkdir flexproject
4) clone repository to new directory
5) pip install -r requirements.txt
6) python manage.py runserver
7) https://localhost:8000 
