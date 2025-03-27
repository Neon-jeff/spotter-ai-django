# Next.js ELD Mapping Web App Documentation

## Overview
This web application is built with Django and integrates the following features:
- Storing the trips created by the driver from the frontend in a sqlite database
- retrieve th stored trip by its primary key from the database


## Technologies Used
- **UV** (Rust based tool to setup python project and manage dependencies)
- **Django** (Python web framework)
- **Django rest framework** (Framework for integration RESTful services with django)
- **SQLite** (Database)



## Installation & Setup
### Prerequisites
- Python(3.10+ recommended)
- pip or uv package manager


### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Neon-jeff/spotter-ai-django.git
   cd spotter-ai-django
   ```
2. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   # or
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   Create a `.env` file and add:
  ```env
  SECRET_KEY=your-secret-key
```
4. **Run the development server:**
   ```bash
   uv run manage.py migrate
   uv run manage.py runserver
   # or
   python manage.py migrate
   python manage.py runserver
   ```
5. **Open the app in your browser:**
   ```
   http://127.0.0.1:8000
   ```

## Frontend Integration
1. Frontend App built with next js and react
2. Live API URL : https://web-production-7a56.up.railway.app/api
3. Frontend Repo : https://github.com/Neon-jeff/spotter-ai-nextjs-react-.git
4. Frontend URL : https://spotter-ai-nextjs-react.vercel.app/






