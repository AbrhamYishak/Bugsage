import ast

def codetree(code):
    print(code)
    print(ast.parse(code))
    print(ast.Name(code))