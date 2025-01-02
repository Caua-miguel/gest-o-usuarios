from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

client_route = Blueprint('cliente', __name__)

@client_route.route('/')
def lista_clientes():
    clientes = Cliente.select()
    return render_template('listar_clientes.html', clientes=clientes)

@client_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json
    
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item_cliente.html', cliente=novo_usuario)

@client_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@client_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)

@client_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)

@client_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    data = request.json
    
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente=cliente_editado)

@client_route.route('/<int:cliente_id>/delete' , methods=['DELETE'])
def deletar_cliente(cliente_id):
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}