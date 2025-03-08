# Flask Portfolio Website

A professional portfolio website built with Python and Flask to showcase your projects.

## Features

- Responsive design that works on desktop, tablet, and mobile devices
- Home page with hero section, featured projects, and skills showcase
- About page to share your background and expertise
- Projects page with filtering capability to organize your work
- Individual project detail pages to highlight specific projects
- Contact page with a form for visitors to reach out
- Admin dashboard to easily add, edit, and delete projects
- Projects stored in a JSON file for simple management without a database

## Installation

1. Clone the repository or download the source code

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install the required dependencies:
```bash
pip install flask
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and go to http://127.0.0.1:5000/

## Project Structure

```
portfolio-website/
├── app.py              # Main Flask application
├── filters.py          # Custom Jinja template filters
├── projects.json       # JSON file to store project data
├── README.md           # Project documentation
├── static/             # Static files directory
│   ├── css/            
│   │   └── style.css   # CSS styles
│   ├── js/
│   │   └── script.js   # JavaScript functionality
│   └── img/            # Image directory
│       └── projects/   # Project images
└── templates/          # HTML templates
    ├── base.html       # Base template with common elements
    ├── index.html      # Home page
    ├── about.html      # About page
    ├── projects.html   # Projects list page
    ├── project_detail.html  # Individual project page
    ├── contact.html    # Contact page
    ├── admin.html      # Admin dashboard
    ├── add_project.html  # Add project page
    └── edit_project.html  # Edit project page
```

## Customization

### Personal Information

Edit the HTML templates to add your personal information:

- Update the name, title, and description in `templates/index.html`
- Add your biography, education, and experience in `templates/about.html`
- Update contact information in `templates/contact.html`
- Modify social media links in `templates/base.html`

### Styling

- The main CSS file is located at `static/css/style.css`
- Colors can be changed by editing the CSS variables at the top of the file
- Background images can be changed by replacing the images in the `static/img` directory

### Projects

Projects can be added in two ways:

1. Through the admin interface at http://127.0.0.1:5000/admin
2. By directly editing the `projects.json` file

Each project requires the following information:
- Title
- Description
- Technologies (as an array of strings)
- Image URL
- GitHub repository URL (optional)
- Live demo URL (optional)
- Date

## Deployment

For deployment to a production server, consider the following:

1. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

2. Set `debug=False` in app.py
3. Use environment variables for sensitive information
4. Consider adding a proper database for larger applications
5. Deploy to platforms like Heroku, PythonAnywhere, or a VPS

## Adding Authentication

The admin section currently has no authentication. To add basic authentication:

1. Install Flask-Login:
```bash
pip install flask-login
```

2. Create a users.py file with a simple user model
3. Add login and registration routes
4. Secure admin routes with @login_required decorator

## Future Enhancements

- Add a blog section
- Implement a database backend (SQLAlchemy)
- Add user authentication for the admin area
- Create a contact form that sends emails
- Add social media integration
- Implement a theme switcher (light/dark mode)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
