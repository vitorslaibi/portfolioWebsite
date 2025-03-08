# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime
from filters import blueprint as filters_blueprint

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flash messages

# Register custom filters
app.register_blueprint(filters_blueprint)

# Load projects from JSON file
def get_projects():
    try:
        with open('projects.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty list if file doesn't exist or is invalid
        return []

# Save projects to JSON file
def save_projects(projects):
    with open('projects.json', 'w') as file:
        json.dump(projects, file, indent=4)

# Create example projects for demonstration
def create_example_projects():
    example_projects = [
        {
            'title': 'Personal Blog',
            'description': 'A responsive blog website built with Flask and SQLAlchemy. Features include user authentication, comments, and a custom admin dashboard for content management.',
            'technologies': ['Python', 'Flask', 'SQLAlchemy', 'HTML', 'CSS', 'JavaScript'],
            'image': '/static/img/projects/blog.jpg',
            'github': 'https://github.com/yourusername/blog-project',
            'live_demo': 'https://example.com/blog',
            'date': '2023-11-15'
        },
        {
            'title': 'Weather App',
            'description': 'A web application that displays weather information based on user location or search. Utilizes the OpenWeatherMap API to fetch current weather data and forecasts.',
            'technologies': ['JavaScript', 'HTML', 'CSS', 'APIs', 'Responsive Design'],
            'image': '/static/img/projects/weather.jpg',
            'github': 'https://github.com/yourusername/weather-app',
            'live_demo': 'https://example.com/weather',
            'date': '2023-09-20'
        },
        {
            'title': 'E-commerce Platform',
            'description': 'A full-featured e-commerce platform with product catalog, shopping cart, user accounts, and payment integration using Stripe. Built with Flask and MongoDB.',
            'technologies': ['Python', 'Flask', 'MongoDB', 'Stripe API', 'HTML', 'CSS', 'JavaScript'],
            'image': '/static/img/projects/ecommerce.jpg',
            'github': 'https://github.com/yourusername/ecommerce-platform',
            'live_demo': 'https://example.com/shop',
            'date': '2024-01-10'
        },
        {
            'title': 'Task Manager',
            'description': 'A productivity application for managing tasks and projects. Features include drag-and-drop organization, priority levels, due dates, and collaborative features.',
            'technologies': ['JavaScript', 'React', 'CSS', 'Node.js', 'Express', 'MongoDB'],
            'image': '/static/img/projects/taskmanager.jpg',
            'github': 'https://github.com/yourusername/task-manager',
            'live_demo': 'https://example.com/tasks',
            'date': '2023-12-05'
        }
    ]
    return example_projects

# Home page route
@app.route('/')
def home():
    projects = get_projects()[:3]  # Get only first 3 projects for featured section
    return render_template('index.html', active_page='home', projects=projects)

# About page route
@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

# Projects page route
@app.route('/projects')
def projects():
    projects_list = get_projects()
    return render_template('projects.html', projects=projects_list, active_page='projects')

# Individual project page route
@app.route('/project/<int:project_id>')
def project_detail(project_id):
    projects_list = get_projects()
    if 0 <= project_id < len(projects_list):
        return render_template('project_detail.html', project=projects_list[project_id], active_page='projects')
    return redirect(url_for('projects'))

# Contact page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # In a real application, you would process the form data here
        # For example, send an email or save to a database
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', active_page='contact')

# Admin routes (you would add authentication in a real application)
@app.route('/admin')
def admin():
    projects_list = get_projects()
    return render_template('admin.html', projects=projects_list, active_page='admin')

@app.route('/admin/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        projects_list = get_projects()
        new_project = {
            'title': request.form.get('title'),
            'description': request.form.get('description'),
            'technologies': request.form.get('technologies').split(','),
            'image': request.form.get('image'),
            'github': request.form.get('github'),
            'live_demo': request.form.get('live_demo'),
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        projects_list.append(new_project)
        save_projects(projects_list)
        flash('Project added successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('add_project.html', active_page='admin')

@app.route('/admin/edit/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    projects_list = get_projects()
    if 0 <= project_id < len(projects_list):
        if request.method == 'POST':
            projects_list[project_id] = {
                'title': request.form.get('title'),
                'description': request.form.get('description'),
                'technologies': request.form.get('technologies').split(','),
                'image': request.form.get('image'),
                'github': request.form.get('github'),
                'live_demo': request.form.get('live_demo'),
                'date': projects_list[project_id].get('date')
            }
            save_projects(projects_list)
            flash('Project updated successfully!', 'success')
            return redirect(url_for('admin'))
        return render_template('edit_project.html', project=projects_list[project_id], project_id=project_id, active_page='admin')
    return redirect(url_for('admin'))

@app.route('/admin/delete/<int:project_id>')
def delete_project(project_id):
    projects_list = get_projects()
    if 0 <= project_id < len(projects_list):
        projects_list.pop(project_id)
        save_projects(projects_list)
        flash('Project deleted successfully!', 'success')
    return redirect(url_for('admin'))

# Create the necessary directories
def setup_application():
    # Create static directories if they don't exist
    for directory in ['static/css', 'static/js', 'static/img', 'static/img/projects']:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create example projects.json if it doesn't exist
    if not os.path.exists('projects.json'):
        example_projects = create_example_projects()
        save_projects(example_projects)

if __name__ == '__main__':
    # Setup application directories and example data
    setup_application()
    
    # Run the Flask application
    app.run(debug=True)