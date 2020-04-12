from flask import Flask, render_template, request, logging
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'fanboost'
app.config['MYSQL_PASSWORD'] = 'scylla123'
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/')
def index():
    return  render_template('home.html.jinja')

@app.route('/cadastrar/perito', methods=['GET', 'POST'])
def cadastrar_perito():
    if request.method == "POST":
        details = request.form
        nome = details['nome']
        email = details['email']
        telefone = details['telefone']
        ativo = int(details['ativo'])
        logradouro = details['logradouro']
        bairro = details['bairro']
        numero = details['numero']
        tipo_pessoa = details['t_pessoa']
        if tipo_pessoa == 'cpf':
            cpf = details['tipo_pessoa']
            cnpj = None
        else:
            cnpj = details['tipo_pessoa']
            cpf = None
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Perito(nome, email, telefone, ativo, logradouro, bairro, numero, cpf, cnpj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, email, telefone, ativo, logradouro, bairro, numero, cpf, cnpj))
        mysql.connection.commit()
        cur.close()
        return ('success')
    return  render_template('registers/perito.html.jinja', status=[{'id':1, 'name': 'ativo'}, {'id': 0, 'name': 'não ativo'}], t_pessoa=[{'name': 'cpf', 'tipo': 'Física'}, {'name': 'cnpj', 'tipo': 'Jurídica'}]);

if __name__ == '__main__':
    app.run(debug=True)
