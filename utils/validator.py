import json
import jsonschema

def validate_json(json_str):
    """
    Validate JSON syntax.
    
    Args:
        json_str (str): JSON string to validate
        
    Returns:
        tuple: (is_valid, errors)
    """
    try:
        json.loads(json_str)
        return True, []
    except json.JSONDecodeError as e:
        return False, [{'line': e.lineno, 'column': e.colno, 'message': str(e)}]

def validate_schema(json_data, schema):
    """
    Validate JSON against a JSON Schema.
    
    Args:
        json_data (dict): JSON data to validate
        schema (dict): JSON Schema to validate against
        
    Returns:
        tuple: (is_valid, errors)
    """
    try:
        jsonschema.validate(instance=json_data, schema=schema)
        return True, []
    except jsonschema.exceptions.ValidationError as e:
        return False, [{'path': '.'.join(str(p) for p in e.path), 'message': e.message}]
    except jsonschema.exceptions.SchemaError as e:
        return False, [{'message': f"Schema error: {str(e)}"}]
