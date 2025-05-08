# JSON Utility Tool

A comprehensive Flask-based web application that serves as a JSON utility tool with two main modules:

1. **Dummy JSON Generator** - Allows users to create custom JSON templates and generate dummy data
2. **JSON Validator** - Validates JSON against schemas or syntax rules

## Features

### Dummy JSON Generator Module
- Field Configuration Panel with various data types
- Type-specific options for each field type
- Template management (save/load)
- Generate multiple objects
- Preview, copy, and download generated JSON

### JSON Validator Module
- Syntax validation
- Schema validation
- Error highlighting

## Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/yourusername/json-utility-tool.git
cd json-utility-tool
\`\`\`

2. Create a virtual environment and activate it:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. Install the required packages:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Run the application:
\`\`\`bash
python app.py
\`\`\`

5. Open your browser and navigate to:
\`\`\`
http://127.0.0.1:5000/
\`\`\`

## Usage

### Dummy JSON Generator

1. Click on "Add Field" to add a new field to your template
2. Configure the field properties (name, type, and type-specific options)
3. Add as many fields as needed
4. Set the number of objects to generate
5. Click "Generate JSON" to create the dummy data
6. Use the "Copy" or "Download" buttons to export the generated JSON

### JSON Validator

1. Enter or paste your JSON in the input area
2. Click "Validate Syntax" to check for syntax errors
3. For schema validation, enter a JSON Schema and click "Validate Schema"
4. View validation results and any errors

## Technical Stack

- **Backend**: Python Flask (RESTful API endpoints)
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Libraries**: Faker for generating realistic data, JSONSchema for validation

## License

MIT
\`\`\`

```python file="utils/__init__.py"
# This file is intentionally left empty to make the directory a Python package
