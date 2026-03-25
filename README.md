# RouteGuard

## Overview
## Project Purpose
## Target Users
## User Experience
## Data Model
## Features
## Future Features
## Technologies Used
## Testing
## Deployment
## Credits

## ⚠️ Challenges Faced & Solutions

### 🧩 Template Structure and Inheritance Issues

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

### 🗂️ File Structure Organisation

An early issue involved incorrectly placing static files within the templates directory. This prevented Django from properly distinguishing between templates and static assets.

**To resolve this:**

- Static files were moved into a dedicated `static/` directory  
- Templates were kept strictly within `templates/` directories  
- A clear separation between HTML structure and CSS styling was established  

This improved maintainability and aligned the project with Django best practices.

---

### 🔗 URL Routing Configuration

Initially, the homepage failed to render due to missing URL configuration between the project and the application.

**To resolve this:**

- A `urls.py` file was created within the `planner` app  
- The home view was mapped using `path('', views.home, name='home')`  
- The app URLs were included in the main `config/urls.py` file using `include()`  

This enabled correct routing and navigation within the application.

---

### 🧱 Template Rendering Output Issues

At one stage, the application displayed a blank page despite no visible errors. This was due to the absence of a `{% block content %}` placeholder in the base template.

**To resolve this:**

- A `{% block content %}` section was added to `base.html`  
- This allowed child templates to correctly inject content into the layout  

This reinforced understanding of Django’s template inheritance system.

---

### 🧠 Key Learning Outcomes

Through resolving these issues, several important development concepts were reinforced:

- The importance of correct file structure in Django projects  
- How Django locates and renders templates and static files  
- The role of `settings.py` in configuring application behaviour  
- The relationship between views, templates, and URL routing  
- Debugging techniques using error messages and browser developer tools  

These challenges strengthened understanding of Django’s architecture and contributed to the development of a more robust and maintainable application.