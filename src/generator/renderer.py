from jinja2 import Environment, PackageLoader, select_autoescape

def render(fileName, imports, _vars):
    env = _build_env()
    template = env.get_template('template.jinja2')
    
    result = template.render(
            className=fileName,
            imports=imports,
            _vars=_vars
        )
    print(result)


def _build_env():
    return Environment(
        loader=PackageLoader('main', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )



if __name__ == "__main__":
    main()
