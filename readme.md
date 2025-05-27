# Budget Buddy

**Budget Buddy** is a full-stack personal finance application designed to help users manage their finances with ease. It features a web-based frontend (Next.js), a mobile frontend (React Native), and a robust, dockerized backend (Django Rest Framework + PostgreSQL).

---

## 🚀 Features

- **User Registration & Authentication**
- **Bank Account Management**: Link and manage multiple accounts
- **Transaction Tracking**: Credit and debit transactions with categories
- **Financial Goals**: Set, track, and visualize savings or debt goals
- **Responsive Web App**: Built with Next.js for modern UX
- **Mobile App**: React Native for Android (iOS support planned)
- **API-first Design**: Django Rest Framework backend
- **Dockerized**: Easy local development and deployment

---

## 🛠️ Tech Stack

- **Frontend (Web):** [Next.js](https://nextjs.org/) (TypeScript)
- **Frontend (Mobile):** [React Native](https://reactnative.dev/)
- **Backend:** [Django Rest Framework](https://www.django-rest-framework.org/)
- **Database:** PostgreSQL
- **Containerization:** Docker, Docker Compose

---

## 📁 Project Structure

```
budget-buddy/
├── backend/                # Django backend (API, models, migrations)
│   ├── bankAccount/
│   ├── creditTransaction/
│   ├── debitTransaction/
│   ├── financialGoals/
│   ├── user/
│   ├── core/
│   ├── manage.py
│   └── ...
├── database/               # Database config/scripts
├── mobile/                 # React Native mobile app (Android)
│   ├── App.tsx
│   └── ...
├── web/                    # Next.js frontend (TypeScript)
│   ├── src/
│   ├── package.json
│   └── ...
├── .env
├── README.md
└── docker-compose.yml   
```

---

## 🏁 Getting Started

### 1. **Clone the repository**

```bash
git clone git@github.com:cswebdev/budget-buddy.git
cd budget-buddy
```

### 2. **Backend Setup**

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### **Run migrations (Dockerized)**
If using Docker Compose:
```bash
docker-compose up -d
docker exec -it django_app python manage.py makemigrations
docker exec -it django_app python manage.py migrate
```

#### **Or run locally**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 3. **Frontend (Web) Setup**

```bash
cd ../web
npm install
npm run dev
```
Visit [http://localhost:3000](http://localhost:3000) to view the web app.

### 4. **Frontend (Mobile) Setup**

```bash
cd ../mobile
npm install
npx react-native run-android
```

---

## ⚙️ Environment Variables

- **Backend:** See `backend/.env`
- **Web Frontend:** See `web/.env.local` (e.g., `NEXT_PUBLIC_API_URL=http://localhost:8000`)

---

## 🧑‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 📷 Screenshots

_Add screenshots or GIFs here to showcase your app UI and features!_

---

## 📫 Contact

- **Author:** Chelsea ([@cswebdev](https://github.com/cswebdev))
- **Email:** your.email@example.com

---

## ⭐️ Acknowledgements

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Next.js](https://nextjs.org/)
- [React Native](https://reactnative.dev/)
- [Faker](https://faker.readthedocs.io/en/master/) for fake data generation

---

> _Budget Buddy: Take control of your finances, one goal at a time!_
