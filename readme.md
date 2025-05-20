# Budget Buddy Overview
Budget buddy is a personal finance application harnessing full-stack functionality with mobile and web based front-ends along with a centralized and dockerized Python Django Rest Framework backend paired with a Postgresql database. 

The web based front-end will be written in Next JS. 
The mobile based front-end will be written in React Native. 
This application will be tailored to run on Android. 

## Project file structure
```
personal-budget-app/
├── backend/                # Django backend
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── app/
├── database/               # PostgreSQL configuration (or part of docker-compose)
│   └── init.sql
├── mobile/                 # React Native for Android (Expo or bare RN)
│   ├── App.tsx
│   └── ...
├── web/                    # Next.js frontend
│   ├── Dockerfile
│   └── ...
├── .env
├── README.md
└── docker-compose.yml   
```

## How to run the application
Clone the application from github
`git clone git@github.com:cswebdev/budget-buddy.git`

# Create a venv file
Move into the backend folder
`cd backend`
Create venv file
`python3 -m venv venv`
Activate venv 
`python3 venv/bin/activate`

### Run migration commands in docker container
Since our Django app and Postgres database are running in containers, we can 
get into the Django app container and run the migration commands from there.

```bash

# Create your migration files
docker exec -it django_app python manage.py makemigrations -n name-of-your-migration

# Apply your migration to the database
docker exec -it django_app python manage.py migrate
```
