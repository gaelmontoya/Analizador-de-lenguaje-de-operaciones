from django.shortcuts import render
from antlr4 import InputStream, CommonTokenStream
# importa tus módulos generados por ANTLR desde la misma app
from antlr4 import *
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .MiniLangvisitoropcional import MiniLangVisitorImpl    

def evaluate_expression(input_expr):
    input_stream = InputStream(input_expr)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.expr()
    visitor = MiniLangVisitorImpl()
    return visitor.visit(tree)

def index(request):
    return render(request, 'index.html')

def calcular(request):
    if request.method == 'POST':
        # si quieres usar ANTLR en lugar de los números, reemplaza estas dos líneas
        x = int(request.POST.get('x', 0))
        y = int(request.POST.get('y', 0))
        z = (x * y) + 10
        x_incrementado = x + 1
        resultado = {'z': z, 'x': x_incrementado}
        return render(request, 'index.html', {'resultado': resultado})
    return render(request, 'index.html')
