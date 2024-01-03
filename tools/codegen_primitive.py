"""
!!!注意 本脚本一定要提取的函数有类型注解才能生成
"""
import inspect

import pandas as pd


def get_function_annotation(module, startswith):
    m = __import__(module, fromlist=['*'])
    funcs = inspect.getmembers(m, inspect.isfunction)
    names = []
    modules = []
    for name, func in funcs:
        mstr: str = func.__module__
        if mstr.startswith(startswith):
            sig = inspect.signature(func)
            ps = sig.parameters
            # 一定得有类型注解
            vv = [v.annotation.__name__ for k, v in ps.items()]
            vv = [v for v in vv if v != '_empty']
            if len(vv) == 0:
                continue
            vv = ', '.join(vv).replace('Expr', 'np.ndarray')
            txt = f"pset.addPrimitive(dummy, [{vv}], np.ndarray, name='{name}')"
            names.append(txt)
            modules.append(mstr)
    return pd.DataFrame({'name': names, 'module': modules}).sort_values(by=['module', 'name'])


def gen_code(df: pd.DataFrame):
    txts = ["""# this code is auto generated by the tools/codegen_primitive.py
import numpy as np
from deap import gp

pset = gp.PrimitiveSetTyped("MAIN", [], np.ndarray)
dummy = None
"""]
    ll = df.groupby(by='module').agg(lambda x: x.to_list())
    dd = ll.to_dict(orient='dict')['name']
    for k, v in dd.items():
        txts.append(f'# {k}')
        for t in v:
            txts.append(t)
    txts.append('')
    return txts


def save(txts, module, write=False):
    m = __import__(module, fromlist=['*'])
    file = m.__file__
    print('save to', file)
    text = '\n'.join(txts)
    if write:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
    else:
        print(text)


if __name__ == '__main__':
    txts = []
    #
    module = 'polars_ta.prefix.wq'
    startswith = 'polars_ta.wq'
    names = get_function_annotation(module, startswith)
    txts += gen_code(names)
    #
    module = 'polars_ta.prefix.ta'
    startswith = 'polars_ta.ta'
    names = get_function_annotation(module, startswith)
    txts += gen_code(names)
    #
    module = 'polars_ta.prefix.talib'
    startswith = 'polars_ta.talib'
    names = get_function_annotation(module, startswith)
    txts += gen_code(names)
    #
    module = 'polars_ta.prefix.tdx'
    startswith = 'polars_ta.tdx'
    names = get_function_annotation(module, startswith)
    txts += gen_code(names)
    #
    save(txts, 'gp.primitives', write=True)
