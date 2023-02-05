# Event Management System

This is an event management system that allows users to send POST data requests in JSON format to
store event information in a database. The system uses Django and the Django Rest Framework to 
provide a REST API for managing events.


## Getting Started

1. Clone the repository:
```
git clone https://github.com/Rocky-04/event-management-system.git
```
2. Change into the project directory:
```
cd event-management-system
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```
5. Apply the database migrations:
```
python manage.py migrate
```
6. Create a superuser:
```
python manage.py createsuperuser
```
7. Run the development server:
```
python manage.py runserver
```

The system should now be running at http://localhost:8000/. You can log in to the Django admin
at http://localhost:8000/admin/ to manage events and event types. The API for creating events is 
available at http://localhost:8000/events/api/create.

## Testing

To run the test suite, use the following command:
```
pytest
```