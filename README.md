# DiffHTML
Highlights differences between two texts in HTML format - Python + Django  

To setup the Django env follow the following commands
1. Go to the folder you want to place the file
2. Create a virtual env
3. pip install django djangorestframework
4. pip install django dj
5. cd textDiff
6. py manage.py runserver


This app can be run using the URL obtained after running the Django server and also using Postman

Using the app using the webpage
1. Go to http://127.0.0.1:8000/form
2. Add the two texts you want to compare in "before" and "After" boxes
3. Click on submit to see the differences highlighted(in three colors) between the two texts

using Postman
1. Select the Post mode 
2. Paste http://127.0.0.1:8000/api 
3. Select form-data under Body
4. Enter a "before" key
5. In the value field add text1
6. Enter "after" key
7. In the value field add text2 that you wish to compare with text1
8. click on send
