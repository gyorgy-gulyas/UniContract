def check_python(results):
    """
    Compiles and executes every emitted Python module (the class/enum definitions actually run,
    which catches bad base classes, TypeVars, etc.). Each module is executed in its own fresh
    namespace, so single-namespace contracts need no cross-module imports.
    Returns (ok, error_text).
    """
    for code in results:
        try:
            code_object = compile(code.content, code.fileName, "exec")
        except SyntaxError as e:
            return False, f"{code.fileName}: syntax error: {e}"
        try:
            exec(code_object, {})
        except Exception as e:
            return False, f"{code.fileName}: {type(e).__name__}: {e}"
    return True, ""
