from engpy.tools.exprs import Expr
from engpy.tools.math import trigs, core
from engpy.errors.exceptions import *
from engpy.misc.gen import getter

def Var(*var):
    
    return [Expr(var_) for var_ in var] if len(var) > 1 else Expr(var[0])

def Str(*var):
    return [str(var_) for var_ in var]

def log(sym,base = 10):
    if getter(sym,'Expr'):
        raise UnaccepatbleToken('Argument must be a Expr-object')
    return Var(f'log{base}({sym})')

def ln(sym):
    return log(sym,'.e')

def sin(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'sin({sym})')

def cos(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'cos({sym})')

def tan(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'tan({sym})')

def cosec(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'sin-({sym})')

def sec(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'cos-({sym})')
def cot(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'tan-({sym})')

def arcsin(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'arcsin({sym})')

def arccos(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return trigs.trig(f'arccos({sym})')

def arctan(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return Var(f'arctan({sym})')

def sqrt(sym):
    if not isinstance(sym, Expr):
        raise UnacceptableToken('Argument must be a Expr-object')
    return sym ** .5


def _complex():
    global i, j, k, _i, _k, _j
    i, j, k = Var('.i', '.j', '.k')
    _i, _j,_k = Str(i, j, k)

zero = Var('')
class Function:
    def __call__(self, *args):
        self.var = args
