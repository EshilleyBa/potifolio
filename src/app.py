from flask import app, Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

    
@app.route('/mais')
def mais():
    return render_template('mais.html')

if __name__ == '__main__':
    app.run('debug=True')
