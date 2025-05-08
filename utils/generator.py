import random
import string
import datetime
import uuid
import re
from faker import Faker

fake = Faker()

def generate_json(template, count=1):
    """
    Generate JSON data based on the provided template.
    
    Args:
        template (dict): Template configuration with fields
        count (int): Number of objects to generate
        
    Returns:
        list: List of generated JSON objects
    """
    results = []
    fields = template.get('fields', [])
    
    for _ in range(count):
        obj = {}
        for field in fields:
            field_name = field.get('name')
            field_type = field.get('type', 'string')
            options = field.get('options', {})
            
            obj[field_name] = generate_field_value(field_type, options)
            
        results.append(obj)
        
    return results

def generate_field_value(field_type, options):
    """Generate a value for a field based on its type and options."""
    if field_type == 'string':
        return generate_string(options)
    elif field_type == 'number':
        return generate_number(options)
    elif field_type == 'boolean':
        return generate_boolean(options)
    elif field_type == 'date':
        return generate_date(options)
    elif field_type == 'array':
        return generate_array(options)
    elif field_type == 'object':
        return generate_object(options)
    elif field_type == 'enum':
        return generate_enum(options)
    else:
        return None

def generate_string(options):
    """Generate a string value based on options."""
    format_type = options.get('format')
    
    if format_type == 'email':
        return fake.email()
    elif format_type == 'uuid':
        return str(uuid.uuid4())
    elif format_type == 'name':
        return fake.name()
    elif format_type == 'address':
        return fake.address()
    elif format_type == 'phone':
        return fake.phone_number()
    elif format_type == 'url':
        return fake.url()
    elif format_type == 'regex':
        pattern = options.get('pattern', '[a-zA-Z0-9]{5,10}')
        try:
            # Using faker's regex provider
            return fake.pystr_format(pattern)
        except:
            # Fallback to basic random string
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    else:
        # Default string generation
        min_length = options.get('min_length', 5)
        max_length = options.get('max_length', 10)
        length = random.randint(min_length, max_length)
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_number(options):
    """Generate a number value based on options."""
    is_integer = options.get('integer', True)
    min_value = options.get('min', 0)
    max_value = options.get('max', 100)
    
    # Convert string values to numbers if needed
    if isinstance(min_value, str) and min_value.strip():
        min_value = int(min_value) if is_integer else float(min_value)
    else:
        min_value = 0
        
    if isinstance(max_value, str) and max_value.strip():
        max_value = int(max_value) if is_integer else float(max_value)
    else:
        max_value = 100
    
    if is_integer:
        return random.randint(min_value, max_value)
    else:
        decimal_places = options.get('decimal_places', 2)
        if isinstance(decimal_places, str) and decimal_places.strip():
            decimal_places = int(decimal_places)
        else:
            decimal_places = 2
        value = random.uniform(min_value, max_value)
        return round(value, decimal_places)

def generate_boolean(options):
    """Generate a boolean value."""
    probability = options.get('probability', 0.5)
    
    # Convert string value to float if needed
    if isinstance(probability, str) and probability.strip():
        try:
            probability = float(probability)
        except ValueError:
            probability = 0.5
    
    return random.random() < probability

def generate_date(options):
    """Generate a date value based on options."""
    format_type = options.get('format', 'iso8601')
    
    # Parse min and max dates
    min_date_str = options.get('min', '2000-01-01')
    max_date_str = options.get('max', datetime.datetime.now().strftime('%Y-%m-%d'))
    
    try:
        min_date = datetime.datetime.strptime(min_date_str, '%Y-%m-%d')
        max_date = datetime.datetime.strptime(max_date_str, '%Y-%m-%d')
    except ValueError:
        # Default dates if parsing fails
        min_date = datetime.datetime(2000, 1, 1)
        max_date = datetime.datetime.now()
    
    # Generate random date between min and max
    delta = max_date - min_date
    random_days = random.randint(0, delta.days)
    random_date = min_date + datetime.timedelta(days=random_days)
    
    # Format the date according to the specified format
    if format_type == 'iso8601':
        return random_date.isoformat() + 'Z'
    elif format_type == 'timestamp':
        return int(random_date.timestamp())
    elif format_type == 'custom':
        custom_format = options.get('custom_format', '%Y-%m-%d')
        return random_date.strftime(custom_format)
    else:
        return random_date.strftime('%Y-%m-%d')

def generate_array(options):
    """Generate an array value based on options."""
    min_length = options.get('min_length', 1)
    max_length = options.get('max_length', 5)
    
    # Convert string values to integers if needed
    if isinstance(min_length, str) and min_length.strip():
        min_length = int(min_length)
    else:
        min_length = 1
        
    if isinstance(max_length, str) and max_length.strip():
        max_length = int(max_length)
    else:
        max_length = 5
        
    length = random.randint(min_length, max_length)
    
    item_type = options.get('item_type', 'string')
    item_options = options.get('item_options', {})
    
    return [generate_field_value(item_type, item_options) for _ in range(length)]

def generate_object(options):
    """Generate an object value based on options."""
    fields = options.get('fields', [])
    obj = {}
    
    for field in fields:
        field_name = field.get('name')
        field_type = field.get('type', 'string')
        field_options = field.get('options', {})
        
        obj[field_name] = generate_field_value(field_type, field_options)
    
    return obj

def generate_enum(options):
    """Generate a value from an enum list."""
    values = options.get('values', [])
    weights = options.get('weights', None)
    
    if not values:
        return None
    
    if weights and len(weights) == len(values):
        return random.choices(values, weights=weights, k=1)[0]
    else:
        return random.choice(values)
