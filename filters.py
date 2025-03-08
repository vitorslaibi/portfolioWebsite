# filters.py
from datetime import datetime
from flask import Blueprint, current_app

blueprint = Blueprint('filters', __name__)

@blueprint.app_template_filter('format_date')
def format_date(value, format='%B %d, %Y'):
    """Format a date string from ISO format to a more readable format."""
    if not value:
        return ''
    try:
        date_obj = datetime.strptime(value, '%Y-%m-%d')
        return date_obj.strftime(format)
    except ValueError:
        return value

@blueprint.app_template_filter('truncate_words')
def truncate_words(s, num=30):
    """Truncate a string to a certain number of words."""
    try:
        words = s.split()
        if len(words) > num:
            return ' '.join(words[:num]) + '...'
        return s
    except (AttributeError, TypeError):
        return s

@blueprint.app_template_global('now')
def now(format_string='%Y'):
    """Return the current date formatted according to format_string."""
    return datetime.now().strftime(format_string)