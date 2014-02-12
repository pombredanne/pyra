from ply import *
from gcl_lex import tokens
import sys

precedence = (
    ('left','OP_BOUNDED_BY','OP_CONTAINING','OP_CONTAINED_IN'),
    ('left','OP_AND','OP_OR'),
    )

def p_gcl_expr(t):
    'gcl_expr : LPAREN gcl_expr RPAREN'
    t[0] = t[2]

def p_gcl_and(t):
    'gcl_expr : gcl_expr OP_AND gcl_expr'
    t[0] = ('And', t[1], t[3])

def p_gcl_or(t):
    'gcl_expr : gcl_expr OP_OR gcl_expr'
    t[0] = ('Or', t[1], t[3])

def p_gcl_bounded_by(t):
    'gcl_expr : gcl_expr OP_BOUNDED_BY gcl_expr'
    t[0] = ('BoundedBy', t[1], t[3])

def p_gcl_containing(t):
    'gcl_expr : gcl_expr OP_CONTAINING gcl_expr'
    t[0] = ('Containing', t[1], t[3])

def p_gcl_contained_in(t):
    'gcl_expr : gcl_expr OP_CONTAINED_IN gcl_expr'
    t[0] = ('ContainedIn', t[1], t[3])

def p_gcl_length(t):
    'gcl_expr : LSPAREN INT RSPAREN'
    t[0] = ('Length', t[2])

def p_gcl_position(t):
    'gcl_expr : INT'
    t[0] = ('Position', t[1])

def p_gcl_phrase(t):
    'gcl_expr : phrase'
    items = ['Phrase']
    items.extend(t[1])
    t[0] = tuple(items)

def p_gcl_phrase_cont(t):
    'phrase : STRING COMMA phrase'
    items = []
    items.append(t[1])
    items.extend(t[3])
    t[0] =  items

def p_gcl_token(t):
    'phrase : STRING'
    t[0] =  (t[1],)

def p_error(t):
        print("Syntax error at '%s'" % t.value)

yacc.yacc()

if __name__ == '__main__':
    expr = " ".join(sys.argv[1:])
    print yacc.parse(expr)