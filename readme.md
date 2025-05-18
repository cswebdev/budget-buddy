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

