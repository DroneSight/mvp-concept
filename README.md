## DroneSight Pipeline Overview

![DroneSight Architecture design](system-design-update.png "DroneSight Pipeline design")



# Interactive Ship Tracker

This project is a ship tracking and hazard visualization application built with Django and JavaScript. It allows users to view a customizable map, enter parameters for location and zoom, and add hazard markers to indicate areas of potential danger.

## Project Structure

```
.
├── env/                # Virtual environment directory (excluded from version control)
├── shiptracker/        # Main Django application for ship tracking
├── tracker/            # Core Django project files
├── .env                # Environment variables configuration file
├── db.sqlite3          # SQLite database file
├── manage.py           # Django's management script
```

## Features

- **Dynamic Map Loading**: The map is dynamically centered based on user inputs for latitude, longitude, and zoom level.
- **Hazard Markers**: Add visual hazard indicators on the map by entering specific coordinates.
- **Django Framework**: Backend support for future enhancements such as database storage and user management.
- **Responsive Design**: Interactive map display with a toggleable parameter panel.

## Prerequisites

- Python 3.10+ 
- Django 4.2+ 
- Virtual environment for dependency management

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Create a `.env` file in the root directory with your settings:
     ```
     SECRET_KEY=your-secret-key
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Use the **Toggle Parameters** button to show or hide the settings panel.
3. Enter desired map parameters:
   - **Latitude** and **Longitude** for the map center.
   - **Zoom Level** (range: 1 to 18).
   - Click **Load Map** to apply changes.
4. To add a hazard marker:
   - Enter the **Latitude** and **Longitude** for the hazard.
   - Click **Add Hazard** to display the marker.

## Future Enhancements

- Integrate database storage for hazard markers.
- Add authentication for user-specific settings.
- Support additional map styles and layers.
