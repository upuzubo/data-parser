import logging
import os
import re
import time
from datetime import datetime
from pathlib import Path

def parse_date(date_string):
    """Parse date string in various formats."""
    try:
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    except ValueError:
        try:
            return datetime.strptime(date_string, '%d/%m/%Y').date()
        except ValueError:
            try:
                return datetime.strptime(date_string, '%m/%d/%Y').date()
            except ValueError:
                raise ValueError('Invalid date format')

def get_file_size(file_path):
    """Get file size in bytes."""
    return os.path.getsize(file_path)

def human_readable_size(size):
    """Convert file size in bytes to human-readable format."""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(size) < 1024.0:
            return f"{size:3.1f} {unit}B"
        size /= 1024.0
    return f"{size:.1f} YiB"

def log_file_path(file_path):
    """Set up logging with file path."""
    logging.basicConfig(filename=file_path, level=logging.INFO)

def get_current_time():
    """Get current time in seconds since epoch."""
    return time.time()

def validate_email(email):
    """Validate email address using regular expression."""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(pattern, email))

def get_file_extension(file_name):
    """Get file extension from file name."""
    return os.path.splitext(file_name)[1]

def get_file_name(file_path):
    """Get file name from file path."""
    return os.path.basename(file_path)

def create_directory(directory_path):
    """Create directory if it does not exist."""
    Path(directory_path).mkdir(parents=True, exist_ok=True)