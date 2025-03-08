# app.py
from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

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

# Home page route
@app.route('/')
def home():
    return render_template('index.html', active_page='home')

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
@app.route('/contact')
def contact():
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
            return redirect(url_for('admin'))
        return render_template('edit_project.html', project=projects_list[project_id], project_id=project_id, active_page='admin')
    return redirect(url_for('admin'))

@app.route('/admin/delete/<int:project_id>')
def delete_project(project_id):
    projects_list = get_projects()
    if 0 <= project_id < len(projects_list):
        projects_list.pop(project_id)
        save_projects(projects_list)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    # Create projects.json if it doesn't exist
    if not os.path.exists('projects.json'):
        save_projects([])
    app.run(debug=True)
