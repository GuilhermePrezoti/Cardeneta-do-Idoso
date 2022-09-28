from ast import Import
from flask import Flask, render_template, request
from model import model
import this
import datetime

this.dataCadastrada = datetime.date.today()

this.dados = ""
this.campo = ""
this.msg = ""
this.modelo = model()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        this.cpf = request.form['tNovoCpf']
        this.nome = request.form['tNovoNome']
        this.dataDeNascimento= request.form['tNovoDataDeNascimento']
        this.cidadeDeNascimento = request.form['tNovoDataDeNascimento']
        this.racaCor = request.form['tNovoRacaCor']
        this.moradia = request.form['tNovaMoradia']
        this.cartaoSus = request.form['tNovoCartaoSus']
        this.pai = request.form['tNovoPai']
        this.mae = request.form['tNovaMae']
        this.sabeLerEscrever = request.form['tNovaSabeLerEscrever']
        this.escolaridade = request.form['tNovaEscolaridade']
        this.rua = request.form['tNovaRua']
        this.cidade = request.form['tNovaCidade']
        this.bairro = request.form['tNovaBairro']
        this.numero = request.form['tNovaNumero']
        this.cep = request.form['tNovaCep']
        this.municipio = request.form['tNovaMunicipio']
        this.estado = request.form['tNovaEstado']
        this.complemento =  request.form['tNovaComplemento']
        this.telefone =request.form['tNovaTelefone']
        this.email = request.form['tNovaEmail']
        this.conjugue = request.form['tNovoConjugue']
        this.profissao = request.form['tNovaProfissao']
        this.convenio = request.form['tNovaConvenio']
        this.deficiencia = request.form['tNovaDeficiencia']
        this.tipoSanguineo = request.form['tNovaTipoSanguineo']
        this.fatorRH = request.form['tNovaFatorRH']
        this.nomeResponsavel = request.form['tNovoNomeResponsavel']
        this.vinculoResponsavel = request.form['tNovaVinculoResponsavel']
        this.telefoneResponsavel = request.form['tNovaTelefoneResponsavel']
        this.enderecoResponsavel = request.form['tNovaEnderecoResponsavel']
        
          


        this.dados = this.modelo.inserirIdoso(this.cpf, this.nome, this.dataDeNascimento, this.cidadeDeNascimento, this.racaCor, this.moradia, this.cartaoSus, this.pai, this.mae, this.sabeLerEscrever, this.escolaridade, this.rua, this.cidade, this.bairro, this.numero, this.cep, this.municipio, this.estado, this.complemento, this.telefone, this.email, this.conjugue, this.profissao, this.convenio, this.deficiencia, this.tipoSanguineo, this.fatorRH, this.nomeResponsavel, this.vinculoResponsavel, this.telefoneResponsavel, this.enderecoResponsavel, this.moraResponsavel, this.dataCadastrada)
    

    return render_template('index.html', titulo="PaginaInicial", resultado = this.dados)

@app.route('/atualizar.html', methods=['GET', 'POST'])
def atualizarDado():
    if request.method =='POST':
        this.cpf = request.form['tNovaCpf'] 
        this.campo = request.form['tCampo']
        this.dado = request.form['tDado']
        this.msg = this.modelo.atualizar(this.cpf, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)     


if __name__ == '__main__':
    app.run(debug=True, port=5000)