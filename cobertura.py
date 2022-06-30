import os
import functions
import dashboards
from flask import Blueprint, Flask
from flask import render_template

# Time to wait script execute, in seconds
TIME_WAIT_SCRIPTS = 15

cobertura = Blueprint('cobertura', __name__)

@cobertura.route('/', defaults={'id': 'salaDeGuerraMatricula'})
def dashboard(id):
    selectedDashboard = getattr(dashboards, id, None)
    return render_template('dashboard.html', spaces=selectedDashboard)

@cobertura.route('/render/<script>')
def renderSpace(script):
    cmd = 'python scripts/{}.py'.format(script)
    std, out = functions.run(cmd, TIME_WAIT_SCRIPTS)
    return out

@cobertura.route('/example')
def example():
    return render_template('example.html')

if __name__ == '__main__':
    context = os.environ.get('SERVER_CONTEXT_PATH', '/')
    app = Flask(__name__, static_url_path='{}static'.format(context))
    app.register_blueprint(cobertura, url_prefix='{}'.format(context))
    app.run('0.0.0.0', 5000, True)
