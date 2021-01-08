from flask import Flask, request
from insertDB import insertUsuario

app = Flask("ApiComFlask")

#Alterando aqui
@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()

    #valida preenchimento de campos
    if("nome" not in body):
        return geraResponse(400, "Nome obrigatorio")
    if ("email" not in body):
        return geraResponse(400, "email obrigatorio")
    if ("idade" not in body):
        return geraResponse(400, "idade obrigatorio")
    if ("sexo" not in body):
        return geraResponse(400, "sexo obrigatorio")
    #Valida preenchimento de campos FIM

    usuario = insertUsuario(body["nome"],body["email"],body["idade"],body["sexo"])

    return geraResponse(200, "Usuario Criado", "usuario", usuario)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    return response

app.run()
