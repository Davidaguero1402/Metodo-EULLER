from flask import request, jsonify, Blueprint
import json
from ..utils import metodo_euler


euler_bp = Blueprint('euler', __name__)

@euler_bp.route('euler', methods=['POST'])
def calcular_euler():
    data = request.get_json()
    
    try:
        x0 = float(data['x0'])
        y0 = float(data['y0'])
        xf = float(data['xf'])
        n = int(data['n'])
        
        # Definir la función de la EDO
        def f(x, y):
            return eval(data['edo'])  # Usar eval con precaución en entornos reales

        resultado = metodo_euler(f, x0, y0, xf, n)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

