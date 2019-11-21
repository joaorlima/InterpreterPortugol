from sly import Lexer

class CalcLexer(Lexer):
    tokens = {ID, NUM, PLUS, TIMES, MINUS, DIVIDE, MOD, LPAREN, RPAREN, EQ, GT, LT,
              INTEGER, BEGIN, END, IF, THEN, ELSEIF, ENDIF, FOR, TO, INCREMENT,
              ENDFOR, PRINT, INPUT, ATTRIB, SEMICOLON, COLON, STRING}

    ignore = '\t'

    STRING = r'\".*\"'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUM = r'\d+'
    PLUS = r'\+'            # addition (+)
    MINUS = r'-'            # subtraction (-)
    TIMES = r'\*'           # multiplication (*)
    DIVIDE = r'/'           # division (/)
    MOD = r'\%'             # reminder (%)
    EQ = r'=='              # equals (comparison)
    LPAREN = r'\('          # left parenthesis
    RPAREN = r'\)'          # right parenthesis
    LT = r'\<'              # less than (<)
    GT = r'\>'              # greater than (>)
    SEMICOLON = r'\;'       # semicolon (end line)
    COLON = r'\:'           # colon (value attribution)
    ATTRIB = r'='           # equal sign (variable attribution)

    # ---------- reserved words ----------
    ID['inteiro'] = INTEGER

    ID['inicio'] = BEGIN
    ID['fim'] = END

    ID['se'] = IF
    ID['entao'] = THEN
    ID['senao'] = ELSEIF
    ID['fim_se'] = ENDIF

    ID['para'] = FOR
    ID['ate'] = TO
    ID['passo'] = INCREMENT
    ID['fim_para'] = ENDFOR

    ID['imprima'] = PRINT
    ID['leia'] = INPUT
    # ---------- reserved words ----------

    ignore_newline = r'\n+'
    ignore_space = r' '

    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def ignore_space(self, t):
        self.lineno += t.value.count(' ')

    def error(self, t):
        print('Caractere %s não definido.' % t.value[0])
        self.index += 1