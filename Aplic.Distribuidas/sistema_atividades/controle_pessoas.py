from flask import Flask,jsonify,abort
from flask import make_response, request, url_for


app = Flask(__name__)
professores = [
        {'nome':"joao", 'id_professor': 1},
        {'nome':"jose", 'id_professor': 2},
        {'nome':"maria", 'id_professor': 3}
        ]

alunos = [
        {'nome':"alexandre", 'id_aluno':1},
        {'nome':"miguel", 'id_aluno':2},
        ]

disciplinas = [
        {'nome':"distribuidos", 'id_disciplina':1, 'alunos':[1,2], 'professores':[1], 'publica': 'False'},
        {'nome':"matematica financeira", 'id_disciplina':2, 'alunos':[2], 'professores':[3], 'publica': 'True'},
        {'nome':"matematica basica", 'id_disciplina':3, 'alunos':[1,2], 'professores':[3,2], 'publica': 'False'}
        
        ]

'''
Você consegue abrir a pagina que geramos abaixo?

Troque o texto!
'''
@app.route('/')
def index():
        return "Nome mudado"

'''
Vou deixar a primeira URL definida, pra facilitar o debug
'''
@app.route('/pessoas/ver_tudo/', methods=['GET'])
def get_all():
     return jsonify([professores,alunos,disciplinas])

'''
Vamos fazer dois exemplos de URLs. Duas versoes da URL /professor/<int:professor_id> 
para vermos os dados de um professor.

Com isso, veremos como implementar as boas praticas recomendadas na aula passada
'''
@app.route('/nao_encapsulada/professor/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    for professor in professores:
        if professor['id_professor'] == id_professor:
           copia = dict(professor) #é importante copiarmos o dicionario, como fizemos aqui.
           #se tivessemos feito copia = professor, teriamos duas variaveis apontando
           #para o mesmo objeto, de forma que ao adicionar a url em copia,
           #adicionariamos tambem na variavel professor
           copia['url'] = url_for('get_professor',id_professor=copia['id_professor'])
           #note a funcao url_for. Ela recebe uma string, que é um nome de funcao,
           # e as variaveis, na forma  nome_variavel = valor_da_variavel;
           #Se quisessemos a url para o professor 200, fariamos
           # url_for('get_professor',id_professor=200)
           resposta = jsonify(copia)
           return resposta

'''
Segunda versao da URL /professor/<int:professor_id> 
'''
@app.route('/professor/<int:id_professor>', methods=['GET'])
def get_professor_completa(id_professor):
    for professor in professores:
        if professor['id_professor'] == id_professor:
           copia = dict(professor)
           copia['url'] = url_for('get_professor_completa',id_professor=copia['id_professor'])
           resposta = jsonify({'response':'True','professor':copia})
           #agora a resposta tem um formato padrao, tanto para erro quanto para correto.
           #é um dicionario que sempre contem o campo response.
           return resposta
    #e estamos devolvendo um erro quando ele ocorre
    resposta = jsonify({'response':'False','error':'id de professor inválida'})
    return resposta,404

'''
Crie uma URL /leciona/<int:id_professor>/<int:id_disciplina>

Ela deve retornar se um professor leciona ou nao uma determinada disciplina

Se ele leciona, o retorno deve ser
{'response':'True', 'leciona':'True'}

Caso contrario,
{'response':'True', 'leciona':'False'}

Se a disciplina nao for encontrada, retorne
{'response':'False', 'error':'disciplina nao encontrada'}

e o codigo de status 404
'''
@app.route('/leciona/<int:id_professor>/<int:id_disciplina>/', methods=['GET'])
def leciona(id_professor,id_disciplina):
    var = None
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            var = True
            if id_professor in disciplina['professores']:
                leciona = {'response':'True','leciona':'True'}
                return jsonify(leciona), 200
            else:
                nao_leciona = {'response':'True','leciona':'False'}
                return jsonify(nao_leciona), 200
        if var == None:
            erro = {'response':'False','error':'disciplina nao encontrada'}
            return jsonify(erro), 404

'''
Agora, vá para o arquivo acesso.py
'''

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
