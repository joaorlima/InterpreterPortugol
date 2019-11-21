from sly import Parser
from Lexer import CalcLexer

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (('left', PLUS, MINUS), ('left', TIMES, DIVIDE))

    def __init__(self):
        self.vars = {}
        print('--- iniciando parser  ---')

    @_('BEGIN expr END')
    def start_program(self, p):
        print(p.expr)
        return p.expr

    @_('ID')
    def numerical(self, p):
        try:
            return self.vars[p.ID]
        except:
            return p.ID

    # ---------- numerical expressions ----------
    @_('NUM')
    def numerical(self, p):
        return int(p.NUM)

    @_('numerical PLUS numerical')
    def numerical(self, p):
        return p.numerical0 + p.numerical1

    @_('numerical MINUS numerical')
    def numerical(self, p):
        return p.numerical0 - p.numerical1

    @_('numerical TIMES numerical')
    def numerical(self, p):
        return p.numerical0 * p.numerical1

    @_('numerical DIVIDE numerical')
    def numerical(self, p):
        if p.numerical1 != 0:
            return p.numerical0 / p.numerical1
        else:
            raise ZeroDivisionError('Erro! Divisão por 0 não aceita.')

    @_('numerical MOD numerical')
    def numerical(self, p):
        return p.numerical0 % p.numerical1

    @_('numerical EQ numerical')
    def condition(self, p):
        return p.numerical0 == p.numerical1

    @_('numerical GT numerical')
    def condition(self, p):
        return p.numerical0 > p.numerical1

    @_('numerical LT numerical')
    def condition(self, p):
        return p.numerical0 < p.numerical1
    # ---------- numerical expressions ----------

    # ---------- structure rule (statement) ----------
    @_('rule')
    def expr(self, p):
        return str(p.rule)

    @_('rule expr')
    def expr(self, p):
        return str(p.rule) + '\n' + p.expr
    # ---------- structure rule (statement) ----------

    # ---------- attribution statement rule ----------
    @_('attribution')
    def rule(self, p):
        return p.attribution

    @_('INTEGER COLON ID SEMICOLON')
    def attribution(self, p):
        self.vars[p.ID] = 0
        return '%s: (%s = 0)' % ('atribuição', p.ID)

    @_('INTEGER COLON ID ATTRIB numerical SEMICOLON')
    def attribution(self, p):
        self.vars[p.ID] = p.numerical
        return '%s: (%s = %s)' % ('atribuição', p.ID, p.numerical)

    # ---------- attribution statement rule ----------

    # ---------- if statement rule ----------
    @_('rule_if')
    def rule(self, p):
        return p.rule_if

    @_('IF condition THEN expr ENDIF')
    def rule_if(self, p):
        if p.condition:
            return p.expr
        else:
            pass

    @_('IF condition THEN expr ELSEIF expr ENDIF')
    def rule_if(self, p):
        return p.expr0 if p.condition else p.expr1
    # ---------- if statement rule ----------

    # ---------- for statement rule ----------
    @_('rule_for')
    def rule(self, p):
        return p.rule_for

    @_('FOR numerical TO numerical INCREMENT numerical expr ENDFOR')
    def rule_for(self, p):
        st = ''
        for x in range(p.numerical0, p.numerical1, p.numerical2):
            st += '\n' + p.expr
        return st
    # ---------- for statement rule ----------

    # ---------- print statement rule ----------
    @_('rule_print')
    def rule(self, p):
        return p.rule_print

    @_('PRINT LPAREN STRING RPAREN SEMICOLON')
    def rule_print(self, p):
        return '%s(%s)' % ('imprima', p.STRING)

    @_('PRINT LPAREN numerical RPAREN SEMICOLON')
    def rule_print(self, p):
        return '%s(%s)' % ('imprima', p.numerical)
    # ---------- print statement rule ----------

    # ---------- input statement rule ----------
    @_('rule_input')
    def rule(self, p):
        return p.rule_input

    @_('INPUT LPAREN ID RPAREN SEMICOLON')
    def rule_input(self, p):
        c = input('\ndigite um valor para c: ')
        self.vars[p.ID] = int(c)
        return '%s(%s)' % ('leia', c)
    # ---------- input statement rule ----------
