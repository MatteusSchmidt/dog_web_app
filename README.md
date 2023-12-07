# dog_web_app

Django based web app that pulls data from theDogsAPI and theCatsAPI

Site links include:

whatupdawg.co, whatupdawg.co/animals/cats, whatupdawg.co/animals/dogs, whatupdawg.co/animals/api/get_cats, whatupdawg.co/animals/api/get_dogs

## Django Framwork / set up documentation:

First `pip install requirements.txt` to download the necessary pipenv required to run the project.

### Settings file:
  To run the web app on a local host, make sure to: change `ALLOWED_HOSTS` to `'*'`, or `'local.host'` and remember to add the local hosting port number in the array of allowed hosts.  

Set:
```
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = False
    SECURE_SSL_REDIRECT = False
    SECURE_REFERRER_POLICY = "no-referrer"
```
  
### the power of Models.py // SQLite db:

Each class represents a single animal, primary key being "name" i.e. calls to cat model with a
specified structure. 

Under /animals/management/commands, you will find two files labeled as import_commands, each of which are classes which inherit the BaseCommand class offered by Django to create a command to import a cleanly formatted JSON which has items which fill each model in the SQLite db. If you'd like to use the data in other methods, use the predefined serialized apis to either create ajax calls to filter cats by data with integer values, or to export your data with a 'GET'. 
    
### import_command files:

Iterate through the JSON file printed by running main on data_cleaner modules. To import this data into the SQLite db, run `python manage.py cat_import_command clean_json_cats.txt` you can replace cats with dogs in the command to populate the DogModel as well. 

Make sure to `python manage.py makemigrations` followed by `python manage.py migrate` to inject the entire db. You can use sql shell commands to add personal cats or dogs, such as your precious toy poodle.

## Frontend

/animals/static/ contains the totality of the css, js, and images used for this project. Any additions to static files, or alterations, must be followed by the command `python manage.py collectstatic` to copy the files to the assets folder, to be read by the Django framework.

/animals/templates/ contains the totality of the HTML doc for the project. Inline python offered by the Django framework is encapsulated by `{%  %}` and functions to either pass new links to urls, or to reference static files.

/animals/urls/ defines the totality of url paths, of which pull the name of each instance of each animal model to serve the same html with different data. 

## Backend

/dog_data/data_collection/ This is the pathing of all data processing files. 

Data gathered from theCatsAPI, theDogsAPI Comments are added for additional aid, as the functions are self explanitory. 

Make sure to run main on both data_cleaner_cats.py as well as data_cleaner_dogs.py to create files in the /dog_web_app path to be read by the commands found in animals/management.
 

 

