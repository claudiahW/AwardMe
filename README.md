# Weaward

### 14th Dec 2021

## Author  
  
Claudiah Wanjiru
  
# Description  
Accolades is a platform where different creators get to  post their works,,,then they get to receive feedback based on certain criteria i.e,,design,usability and content,,.from the different reviewers.
  
##  Live Link  



 
## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page

  
## Setup and Installation  

## Clone the repository:  
 
https://github.com/lizgi/lit_awards

## Navigate into the folder and install requirements 

 cd accolades pip install -r requirements.txt 

## Install and activate Virtual 

python3 -m venv virtual - source virtual/bin/activate  

##### Install Dependencies  
 
 pip install -r requirements.txt
 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 bash 
python manage.py makemigrations photos
  
 Now Migrate  
 bash 
 python manage.py migrate 

##### Run the application  
 bash 
 python manage.py runserver 
 
##### Running the application  
 bash 
 python manage.py server 

##### Testing the application  
 bash 
 python manage.py test 

Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8]
* [Django==3.2.9] 
* [Heroku]
  
  
## Known Bugs  
* There are no known bug


## License