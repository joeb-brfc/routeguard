# RouteGuard

A Django-based logistics planning application for managing drivers, routes, and scheduling.

## 📑 Table of Contents

- [RouteGuard](#routeguard)
  - [📑 Table of Contents](#-table-of-contents)
  - [📌 Overview](#-overview)
  - [🎯 Project Purpose](#-project-purpose)
  - [👥 Target Users](#-target-users)
  - [🧠 User Experience](#-user-experience)
  - [👤 User Stories](#-user-stories)
    - [Core User Stories](#core-user-stories)
    - [Availability \& Validation](#availability--validation)
    - [Feedback \& Risk](#feedback--risk)
  - [🗂️ Data Model](#️-data-model)
    - [Driver](#driver)
    - [Route](#route)
    - [Availability](#availability)
    - [Assignment](#assignment)
    - [Relationships](#relationships)
  - [⚙️ Features](#️-features)
  - [🚀 Future Features](#-future-features)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🧪 Testing](#-testing)
    - [Functional Testing](#functional-testing)
    - [Data Rendering Testing](#data-rendering-testing)
    - [UI Testing](#ui-testing)
    - [Error Handling](#error-handling)
  - [🚀 Deployment](#-deployment)
  - [🙌 Credits](#-credits)
  - [⚠️ Challenges Faced \& Solutions](#️-challenges-faced--solutions)
    - [Template Structure and Inheritance Issues](#template-structure-and-inheritance-issues)
    - [🎨 Static Files Not Loading](#-static-files-not-loading)
    - [File Structure Organisation](#file-structure-organisation)
    - [URL Routing Configuration](#url-routing-configuration)
    - [Template Rendering Output Issues](#template-rendering-output-issues)
    - [Key Learning Outcomes](#key-learning-outcomes)
    - [Data Not Displaying in Templates](#data-not-displaying-in-templates)
    - [🧾 Missing Form Import in View](#-missing-form-import-in-view)


## 📌 Overview

RouteGuard is a full-stack Django web application designed to support logistics planning by managing drivers, routes, availability, and assignments.

The system allows users to create and manage a shared dataset, ensuring that drivers are assigned efficiently while avoiding scheduling conflicts and highlighting potential planning risks.

---

## 🎯 Project Purpose

The purpose of RouteGuard is to provide a centralised system for managing logistics planning data that is often handled through fragmented tools such as spreadsheets, messaging platforms, or internal systems.

This application aims to:

- Improve visibility of driver availability  
- Prevent scheduling conflicts  
- Provide simple feedback on assignment risk  
- Streamline the planning process  

The project is inspired by real-world logistics operations, where planning efficiency and compliance are critical.

---

## 👥 Target Users

RouteGuard is designed for:

- Logistics planners  
- Transport coordinators  
- Operations teams managing driver schedules  

These users require a system that allows them to:

- Manage driver availability  
- Assign routes efficiently  
- Avoid double bookings  
- Monitor workload and risk  

---

## 🧠 User Experience

The application is designed with simplicity and clarity in mind:

- A clear navigation structure allows users to easily move between drivers, routes, and assignments  
- Forms are used for creating and updating records  
- Immediate feedback is provided after actions (e.g. success messages, validation errors)  
- The layout is responsive and accessible across different screen sizes  
- Colour indicators (green, amber, red) provide intuitive feedback on assignment risk  
- Data is displayed in structured tables to improve clarity and usability  

The goal is to ensure that users can perform tasks quickly without confusion.

---

## 👤 User Stories

### Core User Stories

- As a user, I want to create and manage drivers so that I can maintain an up-to-date workforce list  
- As a user, I want to create and manage routes so that I can define available work  
- As a user, I want to assign drivers to routes so that work can be scheduled efficiently  
- As a user, I want to view all assignments so that I can monitor planned work  
- As a user, I want to update or delete records so that data remains accurate  

### Availability & Validation

- As a user, I want to mark drivers as available, resting, or on holiday so that I can plan accurately  
- As a user, I want to prevent assigning unavailable drivers so that scheduling errors are avoided  
- As a user, I want to prevent assigning a driver to overlapping routes so that double-booking does not occur  

### Feedback & Risk

- As a user, I want to receive feedback when creating assignments so that I understand whether the action was successful  
- As a user, I want to see a simple risk indicator (green, amber, red) so that I can identify potential scheduling issues  

---

## 🗂️ Data Model

The application is built using a relational database with the following core models:

### Driver
- Stores driver information such as name and status  

### Route
- Stores route details including destination and estimated duration  

### Availability
- Records driver availability on specific dates (available, rest, holiday, etc.)  

### Assignment
- Links drivers to routes with a date and time  
- Used to track planned work and calculate scheduling risk  

### Relationships

- A driver can have many availability records  
- A driver can have many assignments  
- A route can be assigned multiple times  
- Each assignment links one driver to one route  

---

## ⚙️ Features

- User authentication (login/logout)  
- Full CRUD functionality for:
  - Drivers  
  - Routes  
  - Availability  
  - Assignments  
- Validation to prevent:
  - Assigning unavailable drivers  
  - Overlapping assignments  
- Basic risk indicator (green / amber / red)  
- Responsive layout using HTML and CSS  
- Admin panel for data management  
- Data displayed in structured table layouts for improved readability  
- Navigation links between all key data pages (Drivers, Routes, Assignments, Availabilities)  
- Dynamic data rendering from database using Django views and templates  

---

## 🚀 Future Features

- Drag-and-drop planning interface  
- Advanced legal driving hours calculations  
- Dashboard with analytics and summaries  
- Multi-user roles (admin vs standard user)  
- Integration with external logistics systems  
- Exporting reports  

---

## 🛠️ Technologies Used

- Python  
- Django  
- HTML  
- CSS  
- SQLite (development database)  
- Git & GitHub (version control)  
- Heroku (deployment)  

---

## 🧪 Testing

Manual testing was carried out throughout development to ensure functionality, usability, and data handling across the application.

### Functional Testing

- Verified that all models (Driver, Route, Availability, Assignment) could be created and viewed via the Django admin panel  
- Confirmed that data stored in the database is correctly retrieved and displayed in templates  
- Tested navigation links between pages to ensure correct routing  

### Data Rendering Testing

- Ensured that data passed from views is correctly rendered in templates  
- Tested scenarios where no data exists to confirm fallback messages (e.g. "No assignments have been added yet") display correctly  
- Used temporary debug outputs (e.g. `{{ assignments|length }}`) to confirm data was being passed correctly  

### UI Testing

- Confirmed that table layouts render correctly across all list pages  
- Verified consistent styling across pages using shared CSS  
- Checked responsiveness of layout on different screen sizes  

### Error Handling

- Identified and resolved issues where data was not appearing due to:
  - Incorrect variable names between views and templates  
  - Missing context being passed from views  
  - URL routing mismatches  

All identified issues were resolved and documented in the Challenges section.

---

## 🚀 Deployment

The application was deployed using Heroku.

Steps included:

- Creating a Heroku app  
- Configuring environment variables  
- Setting up a PostgreSQL database  
- Pushing code via GitHub  
- Running migrations on the live environment  

The deployed version was tested to ensure it matches the local development version.

---

## 🙌 Credits

- Django documentation  
- Code Institute learning materials  
- Bootstrap (if used later)  
- Online resources and tutorials used for guidance (referenced in code comments where applicable)  

## ⚠️ Challenges Faced & Solutions

###  Template Structure and Inheritance Issues

During development, an issue occurred where Django could not locate the base template (`TemplateDoesNotExist: base.html`). This was caused by an incorrect configuration of template directories and inconsistent file structure between project-level and app-level templates.

**To resolve this:**

- A global `templates` directory was configured in `settings.py` using the `DIRS` setting  
- App-specific templates were organised into `planner/templates/planner/`  
- The `base.html` file was placed in the root templates directory to allow reuse across the application  

This ensured that template inheritance using `{% extends "base.html" %}` functioned correctly.

---

### 🎨 Static Files Not Loading

The application initially failed to apply CSS styling despite correct linking in the template. This was due to Django not recognising the static files directory.

**To resolve this:**

- `{% load static %}` was added to the base template  
- Static file paths were corrected using `{% static 'css/style.css' %}`  
- The `STATICFILES_DIRS` setting was added in `settings.py` to define the static file location  

This ensured that static assets were correctly loaded and applied during development.

---

### File Structure Organisation

An early issue involved incorrectly placing static files within the templates directory. This prevented Django from properly distinguishing between templates and static assets.

**To resolve this:**

- Static files were moved into a dedicated `static/` directory  
- Templates were kept strictly within `templates/` directories  
- A clear separation between HTML structure and CSS styling was established  

This improved maintainability and aligned the project with Django best practices.

---

### URL Routing Configuration

Initially, the homepage failed to render due to missing URL configuration between the project and the application.

**To resolve this:**

- A `urls.py` file was created within the `planner` app  
- The home view was mapped using `path('', views.home, name='home')`  
- The app URLs were included in the main `config/urls.py` file using `include()`  

This enabled correct routing and navigation within the application.

---

### Template Rendering Output Issues

At one stage, the application displayed a blank page despite no visible errors. This was due to the absence of a `{% block content %}` placeholder in the base template.

**To resolve this:**

- A `{% block content %}` section was added to `base.html`  
- This allowed child templates to correctly inject content into the layout  

This reinforced understanding of Django’s template inheritance system.

---

### Key Learning Outcomes

Through resolving these issues, several important development concepts were reinforced:

- The importance of correct file structure in Django projects  
- How Django locates and renders templates and static files  
- The role of `settings.py` in configuring application behaviour  
- The relationship between views, templates, and URL routing  
- Debugging techniques using error messages and browser developer tools  

These challenges strengthened understanding of Django’s architecture and contributed to the development of a more robust and maintainable application.

### Data Not Displaying in Templates

During development, an issue occurred where database records (e.g. assignments) were not appearing in the frontend templates, despite being present in the Django admin panel.

This was caused by inconsistencies between views, templates, and URL routing.

**To resolve this:**

- Ensured that querysets were correctly retrieved in views using `.objects.all()`  
- Passed data to templates using context dictionaries (e.g. `{"assignments": assignments}`)  
- Verified that template variable names matched those passed from the view  
- Checked URL routing to ensure the correct views were being rendered  
- Used debug techniques such as displaying object counts in templates  

This improved understanding of how Django connects the database, views, and templates.

### 🧾 Missing Form Import in View

During development of the driver creation feature, a `NameError` occurred because `DriverForm` had not been imported into `views.py`.

**To resolve this:**

- The form was defined in `forms.py` using a Django `ModelForm`
- The missing import statement `from .forms import DriverForm` was added to `views.py`

This reinforced the importance of correctly connecting Django forms, views, and templates when building CRUD functionality.