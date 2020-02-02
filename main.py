import os
import ast

def _import(filename):
    with open(filename) as f:
        basenode = ast.parse(f.read(), filename)
    
    funcname = os.path.splitext(os.path.basename(filename))[0]
    fnode = ast.FunctionDef(
        name=funcname,
        args=ast.arguments(
            args=[],
            kwonlyargs=[],
            defaults=[],
            kw_defaults=[],
            returns=None,
            type_comment=None),
        body=basenode.body,
        decorator_list=[],
        returns=None,
        type_comment=None)
    basenode.body = [fnode]
    ast.fix_missing_locations(basenode)

    namespace = {}
    code = compile(basenode, filename=filename, mode='exec')
    exec(code, namespace)
    return namespace[funcname]
    

f = _import('testfunc.py')
f()
