from flask import Flask, url_for, render_template

#render_ tamplate busca aquivo html envia variávieis para backen

#url_for cria url interna
#inicialização
app = Flask(__name__)


#rotas
@app.route("/")
def ola_mundo():
    return render_template("index.html")
#retorno pode ser string,json


@app.route("/sobre")
def pagina_sobre():
    return """
<b> Programarpython</b>:assista 
<a href ="https://youtu.be/lv5a80XgzlI?si=EPPGoBLtQWXxWx_b"> Cannal no youtube</a>

"""
#execução
if __name__=="__main__":
    app.run(debug=True)