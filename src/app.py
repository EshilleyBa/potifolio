from flask import app, Flask, render_template

jooj = Flask(__name__)

@jooj.route('/')
def home():
    return render_template('index.html')

@jooj.route('/projetos')
def projetos():
    return render_template('projetos.html')

    
@jooj.route('/mais')
def mais():
    return render_template('mais.html')

if __name__ == '__main__':
    jooj.run('0.0.0.0')