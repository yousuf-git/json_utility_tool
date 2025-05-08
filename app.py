from flask import Flask, render_template, request, jsonify
from utils.generator import generate_json
from utils.validator import validate_json, validate_schema
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def api_generate():
    try:
        data = request.json
        count = data.get('count', 1)
        template = data.get('template', {})
        
        results = generate_json(template, count)
        
        return jsonify({
            'success': True,
            'count': count,
            'template': template,
            'results': results
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/validate/syntax', methods=['POST'])
def api_validate_syntax():
    try:
        data = request.json
        json_str = data.get('json', '')
        
        result, errors = validate_json(json_str)
        
        return jsonify({
            'success': result,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/validate/schema', methods=['POST'])
def api_validate_schema():
    try:
        data = request.json
        json_data = data.get('json', {})
        schema = data.get('schema', {})
        
        result, errors = validate_schema(json_data, schema)
        
        return jsonify({
            'success': result,
            'errors': errors
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
