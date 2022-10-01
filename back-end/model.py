from select import select
import mysql.connector
from conexao import conexao
import re
import this



class model:
    def __init__(self):
        self.db_connection = conexao()
        self.db_connection = self.db_connection.conectar()
        self.con = self.db_connection.cursor()



    def inserirIdoso(self, cpf, nome, dataDeNascimento, cidadeDeNascimento, racaCor, moradia, cartaoSus, pai, mae, sabeLerEscrever, escolaridade, rua, cidade, bairro, numero, cep, municipio, estado, complemento, telefone, email, estacaoConjugal, profissao, convenio, deficiencia, tipoSanguineo, fatorRH, nomeResponsavel, vinculoResponsavel, telefoneResponsavel, enderecoResponsavel, moraResponsavel, dataCadastrada):
        try:
            
            #sql = "select * from cadastro where cpf = '{}';".format(cpf)
            #self.con.execute(sql)    
            #verificarLogin = self.con.fetchall()
            #if len(verificarLogin) > 0 :            
                sql2 = "insert into cadastro(cpf, nome, dataDeNascimento, cidadeDeNascimento, racaCor, moradia, cartaoSus, pai, mae, sabeLerEscrever, escolaridade, rua, cidade, bairro, numero, cep, municipio, estado, complemento, telefone, email, estacaoConjugal, profissao, convenio, deficiencia, tipoSanguineo, fatorRH, nomeResponsavel, vinculoResponsavel, telefoneResponsavel, enderecoResponsavel, moraResponsavel, dataCadastrada) values('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(cpf, nome, dataDeNascimento, cidadeDeNascimento, racaCor, moradia, cartaoSus, pai, mae, sabeLerEscrever, escolaridade, rua, cidade, bairro, numero, cep, municipio, estado, complemento, telefone, email, estacaoConjugal, profissao, convenio, deficiencia, tipoSanguineo, fatorRH, nomeResponsavel, vinculoResponsavel, telefoneResponsavel, enderecoResponsavel, moraResponsavel, dataCadastrada)
                self.con.execute(sql2)
                self.db_connection.commit()
                return "{} Cadastro feito!".format(self.con.rowcount)

            #else:
            #    return "CPF já cadastrado, faça login ou entre em contato pelo telefone: 2222-2222"

        except Exception as erro:
            return erro

    def cadastrarCuidadores(self, cpf, nome, data, referencia, telefone, experiencia, endereco, senha):
        try:
            sql = "select * from dadosDoCuidado where cpf = '{}';".format(cpf)
            self.con.execute(sql)
            verificarCadastro = self.con.fetchall()
            if len(verificarCadastro) > 0:
                return "CPF já cadastrado, faça login ou entre em contato pelo telefone: 2222-2222"
            else:
                sql2 = "insert into cuidador (cpf, nome, dataDeNascimentoDoCuidador, referencias, endereco, telefone, senha) values ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(cpf, nome, data, referencia, telefone, experiencia, endereco, senha)
                self.con.execute(sql2)
                self.db_connection.commit()
                return "{} Cadastro feito!".format(self.con.rowcount)


        except Exception as erro:
            return erro



    def consultar(self, cpf):
        try: 
            sql = "select * from cadastro where cpf = '{}';".format(cpf)
            self.con.execute(sql)

            for(cpf, nome, dataDeNascimento, cidadeDeNascimento, racaCor, moradia, cartaoSus, pai, mae, sabeLerEscrever, escolaridade, rua, cidade, bairro, numero, cep, municipio, estado, complemento, telefone, email, estacaoConjugal, profissao, convenio, deficiencia, tipoSanguineo, fatorRH) in self.con:
                msg = msg + "\nCPF: {}, Nome; {}, Nascimento: {}, Cidade que Nasceu: {}, Raça/Cor: {}, Moradia: {}, Cartão SUS: {}, Nome do Pai: {}, Nome da Mãe: {}, Sabe ler/escrever: {}, Escolaridade: {}, Rua: {}, Cidade: {}, Bairro: {}, Número da Casa: {}, CEP: {}, Municipio: {}, Estado: {}, Compelmento: {}, Telefone: {}, email: {}, Situação Conjugal: {}, Profissão: {}, Convenio: {}, Deficiencia: {}, Tipo Sanguineo: {}, Fator RH: {}" .format(cpf, nome, dataDeNascimento, cidadeDeNascimento, racaCor, moradia, cartaoSus, pai, mae, sabeLerEscrever, escolaridade, rua, cidade, bairro, numero, cep, municipio, estado, complemento, telefone, email, estacaoConjugal, profissao, convenio, deficiencia, tipoSanguineo, fatorRH)
                return msg 
        except Exception as erro:
            return erro

    def atualizar(self, cpf, campo, novoDado):
        try:
            sql = "update cadastro set {} = '{}' where cpf = '{}'". format(campo, novoDado, cpf) 
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!". format(self.con.rowcount)
        except Exception as erro:
            return erro           

    def excluir(self, cpf):
        try:
            sql = "delete from cadastro where cpf = '{}'". format(cpf)
            self.con.execute(sql)
            self.db_connection.commit()
            #return "{} Linha Excluida com Sucesso!".format(self.con.rowcount)#
        except Exception as erro:
            return erro

    def trataData(self, texto):
        separado = texto.split("/")
        dia = separado [0]
        mes = separado [1]
        ano = separado [2]
        return "{}-{}-{}".format(ano, mes,dia)                                        