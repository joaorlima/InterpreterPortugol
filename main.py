# ---------- Projeto 1 ----------
# -- Main --
# -- Disciplina: Construção de Interpretadores --
# -- Aluno: João Pedro Rodrigues de Lima --
# -- Professor: Gregory Moro Puppi Wanderley --

from Lexer import CalcLexer
from Parser import CalcParser

lexer = CalcLexer()
parser = CalcParser()

file_name = 'test1.txt'
fp = open(file_name, 'r')
text = fp.read()
fp.close()

success_str = "--- código analisado (%s) pertence à linguagem ---" % file_name
error_str = "--- código analisado (%s) não pertence à linguagem ---" % file_name

def code_belongs(res):
    return success_str if res is not None else error_str

for tok in lexer.tokenize(text):
    print('token = %r, lexema = %r' % (tok.type, tok.value))

result = parser.parse(lexer.tokenize(text))

print('\n', code_belongs(result))


