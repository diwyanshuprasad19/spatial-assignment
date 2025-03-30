# Spatial Data Platform - Django API

This Django RESTful service provides APIs to manage spatial data objects including Points, LineStrings, and Polygons using PostGIS.

---

## 🚀 Features

- Add and retrieve:
  - 📍 Points (e.g., locations)
  - 📏 LineStrings (e.g., roads or routes)
  - 🗺️ Polygons (e.g., zones or boundaries)
- Custom error handling and API responses
- PostGIS-powered spatial storage
- Clean, modular structure for easy testing and extension

---

## 🛠️ Setup Instructions

### 1. Clone & Activate Environment

-git clone <repo-url>
-cd spatial_backend
-python3 -m venv env
-source env/bin/activate

## Install Dependencies

-pip install -r requirements.txt

## Configure PostgreSQL + PostGIS

-psql -U postgres
-CREATE DATABASE spatial_db;
-\c spatial_db;
-CREATE EXTENSION postgis;
-\q

## Update Database Settings in settings.py

-DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'spatial_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Apply Migrations & Run

-python manage.py makemigrations
-python manage.py migrate
-python manage.py runserver

## API Testing

To test API endpoints and edge cases, refer to the file:

📁 api_testing.txt

It contains all curl commands and expected responses for verification.

## Folder Structure

spatial_backend/
├── spatial/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── services.py
│   ├── constants.py
│   ├── exceptions.py
│   └── urls.py
├── spatial_backend/
│   └── urls.py
└── api_testing.txt

