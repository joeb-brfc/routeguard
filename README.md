# RouteGuard

A Django-based logistics planning application for managing drivers, routes, and scheduling.

## Table of Contents

- [RouteGuard](#routeguard)
  - [Table of Contents](#table-of-contents)
  - [Live Application](#live-application)
  - [Overview](#overview)
  - [Project Purpose](#project-purpose)
  - [Target Users](#target-users)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
    - [Core User Stories](#core-user-stories)
    - [Availability \& Validation](#availability--validation)
    - [Feedback](#feedback)
  - [Data Model](#data-model)
    - [Driver](#driver)
    - [Route](#route)
    - [Availability](#availability)
    - [Assignment](#assignment)
    - [Relationships](#relationships)
  - [Features](#features)
  - [Screenshots](#screenshots)
    - [Homepage](#homepage)
    - [Driver Management](#driver-management)
    - [Route Management](#route-management)
    - [Availability Management](#availability-management)
    - [Assignment Management](#assignment-management)
    - [Record Creation Form](#record-creation-form)
    - [Edit Functionality](#edit-functionality)
    - [Delete Confirmation](#delete-confirmation)
    - [Authentication](#authentication)
  - [Data Flow and Application Logic](#data-flow-and-application-logic)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [Functional Testing](#functional-testing)
    - [Data Rendering Testing](#data-rendering-testing)
    - [UI Testing](#ui-testing)
    - [Form Submission Testing](#form-submission-testing)
    - [Assignment Validation Testing](#assignment-validation-testing)
    - [Update Functionality Testing](#update-functionality-testing)
    - [Delete Functionality Testing](#delete-functionality-testing)
    - [Availability CRUD Testing](#availability-crud-testing)
    - [User Feedback Testing](#user-feedback-testing)
    - [UI Polish Testing](#ui-polish-testing)
    - [Authentication Testing](#authentication-testing)
    - [Live Deployment Testing](#live-deployment-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Testing](#lighthouse-testing)
  - [Deployment](#deployment)
    - [Deployment Steps](#deployment-steps)
      - [Environment Variables](#environment-variables)
  - [Credits](#credits)
  - [Challenges Faced \& Solutions](#challenges-faced--solutions)
    - [Template Structure and Inheritance Issues](#template-structure-and-inheritance-issues)
    - [Static Files Not Loading](#static-files-not-loading)
    - [File Structure Organisation](#file-structure-organisation)
    - [URL Routing Configuration](#url-routing-configuration)
    - [Template Rendering Output Issues](#template-rendering-output-issues)
    - [Data Not Displaying in Templates](#data-not-displaying-in-templates)
    - [Missing Form Import in View](#missing-form-import-in-view)
    - [Missing Redirect Import in View](#missing-redirect-import-in-view)
    - [Form Handling and View Integration Issues](#form-handling-and-view-integration-issues)
    - [Edit View Errors and Debugging](#edit-view-errors-and-debugging)
    - [Availability Delete URL Error](#availability-delete-url-error)
    - [Incorrect Messages Import](#incorrect-messages-import)
    - [Deployment Issue: Missing `dj_database_url`](#deployment-issue-missing-dj_database_url)
    - [Deployment Issue: Virtual Environment Included in Repository](#deployment-issue-virtual-environment-included-in-repository)
    - [Deployment Issue: Static Files Configuration Error](#deployment-issue-static-files-configuration-error)
    - [Deployment Issue: Gunicorn Not Installed](#deployment-issue-gunicorn-not-installed)
    - [Deployment Issue: Missing WhiteNoise Dependency](#deployment-issue-missing-whitenoise-dependency)
    - [Deployment Issue: Application Crash After Successful Build](#deployment-issue-application-crash-after-successful-build)
    - [JavaScript Message Dismissal Issue](#javascript-message-dismissal-issue)
  - [Conclusion](#conclusion)

## Live Application

The deployed application can be accessed here:

[RouteGuard Live Site](https://routeguard-4a6f16cc8505.herokuapp.com/)

---

## Overview

RouteGuard is a full-stack Django web application designed to support logistics planning by managing drivers, routes, availability, and assignments.

It provides a central system for creating, updating, and viewing planning data through a structured and user-friendly interface.

---

## Project Purpose

The purpose of RouteGuard is to provide a centralised system for managing logistics planning data that is often handled through fragmented tools such as spreadsheets, messaging platforms, or internal systems.

This application aims to:

- Improve visibility of driver availability
- Prevent scheduling conflicts
- Streamline the planning process
- Provide clear user feedback during record management

The project is inspired by real-world logistics operations, where planning efficiency and accuracy are important.

---

## Target Users

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

## User Experience

The application is designed with simplicity and clarity in mind:

- A clear navigation structure allows users to move easily between drivers, routes, and assignments
- Forms are used for creating and updating records
- Immediate feedback is provided after actions, such as success messages and validation errors
- Data is displayed in structured tables to improve clarity and usability
- Users can create new records directly from the interface without using the admin panel
- Shared styling was applied across navigation, tables, forms, and messages to improve visual consistency
- Brief descriptive text was added to key pages to help users understand the purpose of each section

The goal is to ensure that users can complete common planning tasks quickly and clearly.

---

## User Stories

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
- As a user, I want to prevent drivers being assigned more than once on the same day so that duplicate daily bookings do not occur

### Feedback

- As a user, I want to receive feedback when creating assignments so that I understand whether the action was successful

---

## Data Model

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

## Features

- Full CRUD functionality for Drivers, Routes, Availability, and Assignments
- Frontend forms built using Django ModelForms to allow users to create and update records without using the admin panel
- Dynamic data rendering from the database using Django views and templates
- Navigation links between all key data pages (Drivers, Routes, Assignments, Availabilities)
- Data displayed in structured table layouts for improved readability and usability
- Automatic redirection after successful form submission to improve user workflow
- Validation to support data integrity, including prevention of duplicate driver records, unavailable driver assignments, invalid time ranges, and duplicate same-day bookings
- Delete confirmation pages to reduce accidental data removal
- User feedback messages displayed after create, update, and delete actions
- User authentication with signup, login, and logout functionality
- Protected create, update, and delete views so only authenticated users can modify data
- Admin panel for backend data management
- Responsive layout using HTML and CSS
- JavaScript used to enhance user experience by automatically dismissing feedback messages after a short delay

---

## Screenshots

### Homepage

![Homepage](docs/screenshots/homepage.png)

The homepage introduces RouteGuard and provides access to the main areas of the application.

### Driver Management

![Driver Management](docs/screenshots/drivers.png)

The driver page displays driver records and provides create, edit, and delete functionality.

### Route Management

![Route Management](docs/screenshots/routes.png)

The route page allows users to manage route details including destination and estimated hours.

### Availability Management

![Availability Management](docs/screenshots/availabilities.png)

The availability page allows users to record and manage driver availability by date and status.

### Assignment Management

![Assignment Management](docs/screenshots/assignments.png)

The assignment page shows driver-route assignments and displays key scheduling information.

### Record Creation Form

![Create Form](docs/screenshots/create-form.png)

Frontend forms allow users to create records directly from the application.

### Edit Functionality

![Edit Functionality](docs/screenshots/edit-form.png)

Existing records can be updated through pre-filled edit forms.

### Delete Confirmation

![Delete Confirmation](docs/screenshots/delete-confirmation.png)

Delete confirmation pages help prevent accidental removal of records.

### Authentication

![Authentication](docs/screenshots/login.png)

User authentication was implemented to protect restricted functionality.

---

## Data Flow and Application Logic

The application follows Django’s Model-View-Template (MVT) architecture:

- **Models** define the database structure and relationships
- **Views** retrieve and process data from the database
- **Templates** render data dynamically for the user

User interactions follow this flow:

1. A user submits a form (e.g. create driver, route, availability or assignment)
2. The view processes the request and validates the data
3. If valid, the data is saved to the database
4. The user is redirected to a list page where updated data is displayed

This structure ensures clear separation of concerns and maintainable code.

---

## Future Features

- Drag-and-drop planning interface
- Advanced legal driving hours calculations
- Dashboard with analytics and summaries
- Multi-user roles (admin vs standard user)
- Integration with external logistics systems
- Exporting reports
- More advanced time-based validation, including rest-gap checks and cumulative driver-hours rules
- Colour indicators (green, amber, red) provide intuitive feedback on assignment risk

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite (used as the development database)
- Gunicorn (used as the production web server)
- WhiteNoise (used to serve static files in production)
- Git & GitHub (version control)
- Heroku (deployment platform)
- Django ModelForms (for form handling and validation)

---

## Testing

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

### Form Submission Testing

- Verified that Driver and Route forms render correctly on the frontend
- Confirmed that valid form submissions create new database records
- Ensured users are redirected to the appropriate list page after submission
- Tested invalid inputs to confirm validation errors are displayed

### Assignment Validation Testing

- Verified that assignments cannot be created if the end time is earlier than the start time
- Confirmed that drivers marked as unavailable cannot be assigned on that date
- Tested that drivers cannot be assigned more than once on the same date
- Confirmed that validation errors are displayed clearly to the user on the form
- Confirmed that assignment validation also applies during record updates, preventing a driver from being edited onto an unavailable date

### Update Functionality Testing

- Verified that existing driver records can be edited through the frontend
- Confirmed that forms load with existing values pre-filled
- Ensured updated data is saved and displayed immediately in the relevant table

### Delete Functionality Testing

- Verified that driver records can be deleted through the frontend
- Confirmed that delete confirmation pages display the correct record details
- Ensured records are removed from the database and no longer appear in the list view

### Availability CRUD Testing

- Verified that availability records can be created, viewed, updated, and deleted through the frontend
- Confirmed that edit forms pre-populate with existing data and save changes correctly
- Tested delete confirmation flow to ensure records are only removed after user confirmation
- Ensured deleted records no longer appear in the availability list
- Confirmed validation rules continue to apply during updates

### User Feedback Testing

- Verified that success messages are displayed after creating, updating, and deleting records
- Confirmed messages appear consistently across all models (Drivers, Routes, Assignments, Availabilities)
- Ensured messages improve user feedback and confirm successful actions

### UI Polish Testing

- Verified that shared styling was applied consistently across all main pages
- Confirmed that tables, navigation, and success messages display clearly
- Checked that descriptive page text improves clarity without affecting functionality

### Authentication Testing

- Verified that new users can register using the signup form
- Confirmed that existing users can log in and log out successfully
- Tested protected create, update, and delete pages to ensure unauthenticated users are redirected to the login page
- Confirmed authenticated users can access protected functionality normally

### Live Deployment Testing

- Verified that the deployed Heroku application loads successfully
- Confirmed that static files such as CSS are served correctly in production
- Tested login, logout, and signup functionality on the live site
- Confirmed that CRUD functionality works as expected on the deployed version
- Verified that validation rules continue to work in production
- Confirmed that protected pages redirect unauthenticated users to the login page

All identified issues were resolved and documented in the Challenges section.

### HTML Validation

![HTML](docs/screenshots/html-validator.png)

HTML templates were tested using the W3C Markup Validation Service. Minor issues were identified and corrected during development.

### CSS Validation

![CSS](docs/screenshots/css-validator.png)

The stylesheet was tested using the W3C CSS Validation Service to confirm valid CSS syntax.

### Lighthouse Testing

![Lighthouse](docs/screenshots/lighthouse.png)

Lighthouse testing was carried out in Chrome Developer Tools to review performance, accessibility, best practices, and SEO. The results helped identify frontend improvements and confirm that the site follows good usability standards.

---

## Deployment

The application was deployed to Heroku using Git and the Heroku CLI.

### Deployment Steps

1. Created a Heroku application
2. Added deployment-related packages including:
   - `gunicorn`
   - `whitenoise`
   - `dj-database-url`
3. Updated `requirements.txt` to ensure all dependencies were included
4. Created a `Procfile` to define the web process:

```Procfile
web: gunicorn config.wsgi
```

5. Updated `settings.py` for deployment by:
   - moving `SECRET_KEY` to an environment variable
   - controlling `DEBUG` with an environment variable
   - adding Heroku-compatible `ALLOWED_HOSTS`
   - configuring static files using `STATIC_ROOT`
6. Added Heroku config vars for:
   - `SECRET_KEY`
   - `DEBUG`
7. Removed the local virtual environment folder from version control and added `.venv/` to `.gitignore`
8. Pushed the project to Heroku using:

```bash
git push heroku main
```

9. Ran migrations on the deployed application
10. Tested the live application to ensure that pages, authentication, CRUD features, validation, and styling all worked as expected

#### Environment Variables

The following environment variables were used in deployment:

- `SECRET_KEY`
- `DEBUG`

---

## Credits

- Django documentation, particularly for ModelForms, form validation, authentication, template logic, production settings, and static files
- Code Institute learning materials
- Heroku documentation and deployment guidance
- GeeksforGeeks for guidance on CSS `:nth-child` pseudo-class usage for alternating table row styling
- Visual Studio Code was used as the primary development environment, including IntelliSense and auto-completion features
- VS Code Markdown Preview tools, Markdown Preview Mermaid Support, and markdownlint were used to help structure and format the README
- JavaScript `setTimeout` functionality was implemented to enhance user experience, inspired by general JavaScript learning resources such as Mimo (https://mimo.org/glossary/javascript/settimeout)

---

## Challenges Faced & Solutions

### Template Structure and Inheritance Issues

Django was unable to locate the base template (`TemplateDoesNotExist: base.html`) due to incorrect template directory configuration and inconsistent file structure.

This was resolved by defining a global `templates` directory in `settings.py`, organising app templates within `planner/templates/planner/`, and placing `base.html` in the root templates directory.

This ensured template inheritance using `{% extends "base.html" %}` worked correctly.

---

### Static Files Not Loading

CSS styling was not being applied due to Django not correctly recognising the static files configuration.

This was resolved by loading the static template tag, correcting static file paths, and defining `STATICFILES_DIRS` in `settings.py`.

This ensured static assets were correctly served during development.

---

### File Structure Organisation

Static files were initially placed within the templates directory, causing Django to misinterpret file types and fail to load assets correctly.

This was resolved by separating static files into a dedicated `static/` directory and keeping templates within `templates/`.

This improved maintainability and aligned the project with Django best practices.

---

### URL Routing Configuration

The homepage initially failed to render due to missing URL configuration between the project and app-level routing.

This was resolved by defining routes in the app’s `urls.py` and including them in the main `config/urls.py` using `include()`.

This enabled correct page rendering and navigation across the application.

---

### Template Rendering Output Issues

The application displayed a blank page due to a missing `{% block content %}` placeholder in the base template.

This was resolved by adding the block to `base.html`, allowing child templates to correctly render content.

This reinforced understanding of Django’s template inheritance system.

---

### Data Not Displaying in Templates

Database records were not appearing in templates despite being present in the admin panel, due to inconsistencies between views, context data, and template variable names.

This was resolved by correctly retrieving querysets in views, passing them through context dictionaries, and ensuring template variables matched.

This improved understanding of how Django connects models, views, and templates.

---

### Missing Form Import in View

A `NameError` occurred when creating a driver due to `DriverForm` not being imported into `views.py`.

This was resolved by importing the form from `forms.py`, allowing the view to process form submissions correctly.

This reinforced the importance of properly linking forms, views, and templates in Django.

---

### Missing Redirect Import in View

A `NameError` occurred during form submission because `redirect` had not been imported into `views.py`.

This was resolved by importing `redirect` from `django.shortcuts`, allowing successful form submissions to redirect correctly.

This reinforced the importance of including all required imports when handling view logic.

---

### Form Handling and View Integration Issues

Errors occurred during form submission due to missing imports and incorrect handling of request methods in views.

This was resolved by importing the required ModelForms, adding `redirect`, and ensuring correct handling of `GET` and `POST` requests.

This improved understanding of how Django processes form submissions and connects forms, views, and templates.

---

### Edit View Errors and Debugging

Errors occurred when implementing the edit functionality due to mismatched URL parameters and missing imports.

This was caused by inconsistency between the parameter name passed in the URL and the view function, as well as a missing `get_object_or_404` import.

The issue was resolved by aligning parameter names between `urls.py` and `views.py`, and importing the required function.

This ensured the edit view loaded correctly and reinforced the importance of consistent naming and correct imports in Django.

---

### Availability Delete URL Error

A `NoReverseMatch` error occurred when implementing delete functionality due to a mismatch between the URL name in `urls.py` and the template reference.

This was resolved by ensuring consistent naming between URL patterns and template tags.

This reinforced the importance of alignment between Django views, URLs, and templates.

---

### Incorrect Messages Import

An `ImportError` occurred when implementing feedback messages due to importing `messages` from the wrong module.

This was resolved by importing `messages` from `django.contrib` instead of `django.shortcuts`.

This ensured feedback messages displayed correctly and reinforced understanding of Django’s module structure.

---

### Deployment Issue: Missing `dj_database_url`

The application failed to run locally after importing `dj_database_url` in `settings.py` before the package had been installed.

This was resolved by installing the dependency and updating `requirements.txt`.

This reinforced the importance of keeping project dependencies aligned with imported modules.

---

### Deployment Issue: Virtual Environment Included in Repository

The Heroku build failed because the local `.venv` directory had been committed to the repository.

This was resolved by removing the directory from version control and adding it to `.gitignore`.

This reinforced the importance of excluding machine-specific files from deployment.

---

### Deployment Issue: Static Files Configuration Error

The deployment failed during `collectstatic` due to incomplete static files configuration in `settings.py`.

This was resolved by correctly defining `STATIC_ROOT` alongside existing static settings.

This improved understanding of the differences between local and production static file handling.

---

### Deployment Issue: Gunicorn Not Installed

The application crashed after deployment because the Gunicorn web server was not installed.

This was resolved by installing Gunicorn and updating `requirements.txt`.

This ensured the application could run correctly on Heroku.

---

### Deployment Issue: Missing WhiteNoise Dependency

The application crashed after adding `WhiteNoiseMiddleware` due to the `whitenoise` package not being installed.

This was resolved by installing the dependency and updating `requirements.txt`.

This ensured static files could be served correctly in production.

---

### Deployment Issue: Application Crash After Successful Build

The application deployed successfully but still displayed a Heroku error page due to runtime issues.

This was resolved by checking logs, identifying missing dependencies, and redeploying until the application ran correctly.

This highlighted the importance of distinguishing between build success and runtime success.

### JavaScript Message Dismissal Issue

An issue occurred where feedback messages did not disappear as expected. This was caused by using `querySelectorAll()` instead of `querySelector()`, which returned a NodeList rather than a single element.

After correcting the selector, the message dismissal worked as intended, improving frontend interactivity and user experience.

## Conclusion

RouteGuard was successfully developed and deployed as a full-stack Django application that supports real-world logistics planning tasks. The project includes full CRUD functionality, authentication, validation, user feedback, and deployment to a live environment.

Throughout development and deployment, several issues were identified and resolved, strengthening the final application and improving understanding of Django, Git, and Heroku workflows.

Future improvements have been identified to expand the project further, particularly around more advanced driver-hours logic and planning intelligence.
