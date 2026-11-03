import ast


def validate_python(code):

    try:
        ast.parse(code)
        return True

    except Exception:
        return False