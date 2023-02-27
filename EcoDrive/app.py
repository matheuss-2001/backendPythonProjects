from flask import Flask, jsonify, request

app = Flask(__name__)

veiculos = [
    {
        "id": 0,
        "placa": "RTB-4B5R",
        "veiculo_marca": "Tesla Motors",
        "veiculo_autonomia": "400 km/Carga"

    },


    {
        "id": 1,
        "placa": "RTB-4B6R",
        "veiculo_marca": "Volkisvagem",
        "veiculo_autonomia": "320 km/Carga"

    },

    {
        "id": 2,
        "placa": "RTB-4B7R",
        "veiculo_marca": "Nissan",
        "veiculo_autonomia": "380 km/Carga"

    }
]

# createVeiculo


@app.route("/veiculo", methods=["POST"])
def add_new_veiculo():
    new_veiculo = request.get_json()
    veiculos.append(new_veiculo)
    return jsonify(veiculos)


# getVeiculos
@app.route("/veiculo", methods=["GET"])
def get_veiculos():
    return jsonify(veiculos)

# getVeiculo por id


@app.route("/veiculo/<int:id>", methods=["GET"])
def get_veiculo_id(id):
    for veiculo in veiculos:
        if veiculo.get("id") == id:
            return jsonify(veiculo)

# editarVeiculo por id


@app.route("/veiculo/<int:id>", methods=["PUT"])
def edit_veiculo_id(id):
    veiculo_alterado = request.get_json()
    for indice, veiculo in enumerate(veiculos):
        if veiculo.get("id") == id:
            veiculos[indice].update(veiculo_alterado)
            return jsonify(veiculos[indice])


# excluir um Veiculo

@app.route("/veiculo/<int:id>", methods=["DELETE"])
def delete_veiculo_id(id):
    for indice, veiculo in enumerate(veiculos):

        if veiculo.get("id") == id:
            del veiculos[indice]
        return jsonify(veiculos)


app.run(port=5000, host="localhost", debug=True)
