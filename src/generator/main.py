import json
import renderer


def main():
    
    data = read_file()
    
    # todo: data structure
    build_schema_files(data['components']['schemas'])

    # todo: api files
    # todo: create maven
    

def read_file():

    apiFile = '../api.json'

    with open(apiFile) as f:
        return json.load(f)


def build_schema_files(schemas):

    for schema in schemas:
        properties = schemas[schema]['properties']
        build_schema_file(schema, properties)


def build_schema_file(schema, properties):
    
    _vars = []

    for _property in properties:

        _type = properties[_property]['type']
        java_type = _openapi_type_to_java(_type)

        entry = { 
                "java_type": java_type, 
                "property_name": _property
            }

        _vars.append(entry)
    
    renderer.render(schema, schema_imports(), _vars)


def _openapi_type_to_java(arg):
    data = {
        'string': 'String',
        'int32': 'int'
    }
    return data[arg]

def schema_imports():
    return [
        'io.quarkus.hibernate.orm.panache.PanacheEntity',
        'javax.persistence.Column',
        'javax.persistence.Entity',
        'javax.validation.constraints.NotBlank',
        'java.util.List'
    ]

def print_json_pretty(data):
    json_formatted = json.dumps(data, indent=2)
    print(json_formatted)


if __name__ == "__main__":
    main()
