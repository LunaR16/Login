from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return '''
        <p>Por favor, ingresa tanto el nombre de usuario como la contraseña.</p>
        <a href="/">Volver atrás</a>
        '''

    # Aquí puedes verificar el usuario y la contraseña
    # y realizar la autenticación

    return f'<center><h1><p> Bienvenido {username}</p></h1></center>'

if __name__ == '__main__':
    app.run(debug=True)
