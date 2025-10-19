from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    stats = {"users": 120, "tasks": 58, "messages": 12}
    return render_template('dashboard.html', stats=stats, title="Dashboard")

@bp.route('/dashboard')
def dashboard():
    stats = {"users": 120, "tasks": 58, "messages": 12}
    return render_template('dashboard.html', stats=stats, title="Dashboard")
