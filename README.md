1. First of all you will need to intall packages from requirements.txt (there are a lot of them, I tried some things during development):

      pip install djangorestframework      
      pip install Django
   
2. Next open command line within the project folder and type
     
     manage.py migrate
   
3. Create super user, so you can access admin panel (localhost:8000/admin)

      manage.py createsuperuser      
   
4. Start local server

    manage.py runserver      
   
