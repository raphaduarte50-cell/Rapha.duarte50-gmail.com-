from flask import Flask, request, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# conexão com Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# rota teste
@app.route("/")
def home():
    return "CRM rodando 🚀"

# listar clientes
@app.route("/clientes", methods=["GET"])
def get_clientes():
    data = supabase.table("clientes").select("*").execute()
    return jsonify(data.data)

# criar cliente
@app.route("/clientes", methods=["POST"])
def add_cliente():
    novo = request.json
    data = supabase.table("clientes").insert(novo).execute()
    return jsonify(data.data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
