from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

client_route = Blueprint('cliente', __name__)

@client_route.route('/')
def lista_clientes():
    return render_template('listar_clientes.html', clientes=CLIENTES)

@client_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

@client_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@client_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')

@client_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')

@client_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

@client_route.route('/<int:cliente_id>/delete' , methods=['DELETE'])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES  = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'deleted': 'ok'}