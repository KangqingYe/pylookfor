"""
pylookfor
======
A lightweight module searching methods in the current python environment by keywords.

Like 'lookfor' in Matlab,
it can print modules, methods and the first line of their documents
if any of them contain the keywords.

Example:

    import pylookfor as lf

    lf.lookfor('sort')

It can search methods in specify modules,

Example:

    import pylookfor as lf

    lf.lookfor('sort', modules = ['scipy', 'numpy'])

It can limit the number of method printed.

Example:

    import pylookfor as lf

    lf.lookfor('sort', modules = ['scipy','numpy'], num_print = 5)
"""
import os
import sys
import inspect
import pkgutil
import importlib

__all__ = ['lookfor']

_dev_null = open(os.devnull, 'w')
_std_out = sys.stdout
_srd_err = sys.stderr


def _is_legal_method(obj):
    return (inspect.isfunction(obj) or
            inspect.ismethod(obj) or
            inspect.isbuiltin(obj)) and obj.__name__[0] != '_'


def _silent_import(name):
    def disable_std():
        sys.stderr = _dev_null
        sys.stdout = _dev_null

    def enable_std():
        sys.stdout = _std_out
        sys.stderr = _srd_err

    disable_std()
    mod = importlib.__import__(name, fromlist=[''])
    enable_std()
    return mod


def _get_doc_firstline(doc):
    if doc.__doc__:
        docs = doc.__doc__.splitlines()
        for d in docs:
            line = d.strip()
            if len(line) == 0:
                continue
            else:
                return line
    return 'No Documentation Found.'


def _scan_modules(key: str) -> dict:
    modules = {}
    print('--------------------Modules----------------------')

    def mod_name_concat_doc(mod_name):
        try:
            mod = _silent_import(mod_name)
            ret = mod_name + ' - ' + _get_doc_firstline(mod), mod
        except Exception:
            ret = None, None
        return ret

    def onerror(_):
        pass

    def scan_sys_mod():
        # search system modules
        for modname in sys.builtin_module_names:
            if modname != '__main__' and modname[0] != '_':
                concat_str, concat_obj = mod_name_concat_doc(modname)
                if concat_str is not None:
                    modules[concat_obj.__name__] = concat_obj
                    if concat_str.lower().find(key) >= 0:
                        print(concat_str, flush=True)

    def scan_ins_mod():
        # search installed modules
        for _, modname, ispkg in pkgutil.walk_packages(onerror=onerror):
            if ispkg and modname[0] != '_':
                concat_str, concat_obj = mod_name_concat_doc(modname)
                if concat_str is not None:
                    modules[concat_obj.__name__] = concat_obj
                    if concat_str.lower().find(key) >= 0:
                        print(concat_str, flush=True)
    scan_sys_mod()
    scan_ins_mod()
    return modules


def _scan_methods(key:str,modules:dict,num_print:int):
    num = 0

    def method_name_concat_doc(method):
        return method.__name__ + ' - ' + _get_doc_firstline(method)

    print('--------------------Methods----------------------')
    for _, module in modules.items():
        try:
            for method_name in dir(module):
                method_obj = getattr(module, method_name)
                if _is_legal_method(method_obj):
                    concat_str = method_name_concat_doc(method_obj)
                    if concat_str is not None and concat_str.lower().find(key) >= 0:
                        print(module.__name__ + '.' + concat_str, flush=True)
                        if num_print != 0:
                            num += 1
                            if num >= num_print:
                                return
                        pass

        except Exception:
            continue


def _check_alpha(s:str):
    try:
        if not s.isalpha():
            raise Exception("Invalid Syntax: all characters in the string should be alphabetic")
    except Exception:
        raise Exception("Invalid Syntax: all characters in the string should be alphabetic")


def _check_args(n:int, modules: list):
    if type(n) != int:
        raise Exception("Invalid Syntax: num_print should be 'int'")
    if n < 0:
        raise Exception("Invalid Syntax: num_print should be greater than or equal to 0")
    if type(modules) != list:
        raise Exception("Invalid Syntax: modules should be 'list', like modules = ['module1','module2']")
    typelist = [type(x) == str for x in modules]
    if typelist.count(False) > 0:
        raise Exception("Invalid Syntax: module name should be str, like modules = ['module1','module2']")


def lookfor(key: str, num_print=0, modules=[]):
    """
    Searching methods in the current python environment by keywords.
    Print modules, methods and the first line of their documents if any of them contain the keywords.

    Parameters
    ----------
    :param key: str
            The keywords.
    :param num_print: int, optional
            The number of the methods that printed.
            default: 0 means no limit.
    :param modules: list, optional
            Search methods in these modules.
            default: [] means search all the modules.

    Notes
    -----
    It can only find methods in modules which can be imported
    Search all of the modules might take a little time.
    Search methods in specific modules will be much quicker.
    """
    _check_alpha(key)
    _check_args(num_print, modules)
    key = key.lower()

    _modules = {}
    if len(modules) == 0:
        _modules = _scan_modules(key)
    else:
        for mod_name in modules:
            _check_alpha(mod_name)
            try:
                mod = _silent_import(mod_name)
            except Exception:
                raise Exception("ImportError: modules can't be import")
            _modules[mod.__name__] = mod

    _scan_methods(key, _modules, num_print)

    _dev_null.close()