Backend API for the e-commerce built with Django, DRF

## Installation
1. Create `.env` file in the project directory with
```
DATABASE_URL=postgresql://postgres:postgres@db/postgres
SECRET_KEY=SECRET
ALLOWED_HOSTS=*
DEBUG=True
```
2. Install with Docker
```
docker-compose build
```
3. Run migrations
```
docker-compose exec gifter python manage.py migrate
```
4. Create superuser
```
docker-compose exec gifter python manage.py createsuperuser
```
## Usage
1. `docker-compose up`
2. Go to localhost:8000/admin and authenticate
3. Create some categories, gifts
4. Play with DRF (django interface is supported, so just visit those pages, cURL is not a mandatory)
   - GET /categories 
   - GET /categories/slug
   - GET /gifts/slug
   - POST /orders
   - GET /orders/uuid


## Pytest with flake8 and coverage
```
docker-compose exec gifter pytest
```

## Format with Black
```
docker-compose exec gifter ./format
```
