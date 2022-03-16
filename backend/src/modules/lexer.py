import ply.lex as lex
# The result of the analysis
result_lex = [] 

# Reserved words
reserved = (
    'ABSTRACT',
    'ASSERT',
    'BREAK',
    'CASE',
    'CATCH',
    'CLASS',
    'CONST',
    'DEFAULT',
    'DO'
    'NEW',
    'PACKAGE',
    'PRIVATE',
    'PUBLIC'
    'RETURN',
    'THIS',
    'VOID'
    'SYSTEM',
    'OUT',
    'PRINTLN'
)

tokens = reserved + (
    'IDENTIFIER',
    'INTEGER',
    'STRING'
    'BOOLEAN',
    'LONG'
    'BYTE',
    'ASSIGN',

    # Mathematical operators
    'SUM',
    'SUBS',
    'MULTI',
    'DIV',
    'POWER',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    
    # Conditions
    'IF',
    'ELSE',
    
    #Loops
    'WHILE',
    'FOR',
    
    # Logic
    'AND',
    'OR',
    'NOT',
    'LESSTHAN',
    'MINOREQUAL',
    'GREATERTHAN',
    'GREATEREQUAL',
    'EQUAL',
    'DIFFERENT',

    # Symbols
    'NUMERAL',

    'PARLEFT',
    'PARRIGHT',
    'CORLEFT',
    'CORRIGHT',
    'KEYLEFT',
    'KEYRIGHT',
    
    # Others
    'SEMICOLON',
    'COMA',
    'COMDOB',
    'GREATHERRIGHT', #>>
    'GREATHERLEFT', #<<
)


t_SUM = r'\+'
t_SUBS = r'-'
t_MINUSMINUS = r'\-\-'

t_MULTI = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POWER = r'(\*{2} | \^)'

t_ASSIGN = r'='

# Logics expresions
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_SEMICOLON = ';'
t_COMA = r','
t_PARLEFT = r'\('
t_PARRIGHT = r'\)'
t_CORLEFT = r'\['
t_CORRIGHT = r'\]'
t_KEYLEFT = r'{'
t_KEYRIGHT = r'}'
t_COMDOB = r'\"'



def t_ABSTRACT(t):
    r'abstract'
    return t

def t_ASSERT(t):
    r'assert'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CONST(t):
    r'const'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_NEW(t):
    r'new'
    return t

def t_PACKAGE(t):
    r'package'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_THIS(t):
    r'this'
    return t

def t_VOID(t):
    r'void'
    return t

def t_SYSTEM(t):
    r'system'
    return t

def t_OUT(t):
    r'out'
    return t

def t_PRINTLN(t):
    r'println'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IF(t):
    r'if'
    return t

def t_RETURN(t):
   r'return'
   return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):
    r'for'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'\w+(_\d\w)*'
    return t

def t_STRING(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MINUSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_EQUAL(t):
    r'=='
    return t

def t_GREATERRIGHT(t):
    r'<<'
    return t

def t_GREATERLEFT(t):
    r'>>'
    return t

def t_DIFFERENT(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error(t):
    global result_lex
    state = "** Invalid Token in the line {:4} value {:16} position {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    result_lex.append(state)
    t.lexer.skip(1)

def test (data: str):
    """This method analysis the string and return list with the answers"""
    global result_lex

    analyzer = lex.lex() 
    analyzer.input(data)

    result_lex.clear()

    while True:
        tok = analyzer.token()
        if not tok:
            break
        state = "Line {:4} Type {:16} Value {:16} position {:4}".format(str(tok.lineno), str(tok.type), str(tok.value), str(tok.lexpos))
        result_lex.append(state)
    return result_lex