# 🌱 Plant Keeper

A Django web application to help you manage and track your plant collection. Keep track of watering schedules, care tasks, and plant health all in one place.

## Features

- **Plant Management**
  - Add, edit, and delete plants
  - Track plant species and watering frequency
  - Add notes and care instructions
  - View plant details and history

- **Watering Records**
  - Record when plants are watered
  - View watering history
  - Track last watering date
  - Add notes to watering records

- **Care Tasks**
  - Create custom care tasks (fertilizing, pruning, repotting)
  - Set task frequency
  - Track task completion
  - Associate tasks with multiple plants

- **User Authentication**
  - Secure user accounts
  - Personal plant collections
  - Protected routes and resources

## Tech Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Bootstrap 5)
- **Authentication**: Django's built-in auth system

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Isaacj3000/django-crud-app-lab.git
   cd plantkeeper
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. **Register/Login**
   - Create an account or log in to access your plant collection

2. **Add Plants**
   - Click "Add Plant" to create a new plant entry
   - Enter plant details and watering frequency

3. **Record Watering**
   - View plant details
   - Click "Record Watering" to log a watering event
   - Add optional notes

4. **Manage Care Tasks**
   - Create care tasks from the "Care Tasks" page
   - Associate tasks with plants
   - Mark tasks as completed

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- Isaac Baptiste
- GitHub: [@Isaacj3000](https://github.com/Isaacj3000)

## Acknowledgments

- Django Documentation
- Bootstrap 5
- PostgreSQL 