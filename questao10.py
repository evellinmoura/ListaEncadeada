class ArrayStack:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        return self._data.pop()
    
    def top(self):
        return self._data[-1]


def precedencia(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0


def eh_operador(char):
    return char in ['+', '-', '*', '/', '^']


def infixa_para_posfixa(expressao):
    pilha = ArrayStack()
    posfixa = []
    numero = ""
    
    for char in expressao:
        if char.isdigit():
            numero += char
        else:
            if numero:
                posfixa.append(numero)
                numero = ""
            
            if char == '(':
                pilha.push(char)
            elif char == ')':
                while not pilha.is_empty() and pilha.top() != '(':
                    posfixa.append(pilha.pop())
                pilha.pop()
            elif eh_operador(char):
                while (not pilha.is_empty() and 
                       pilha.top() != '(' and
                       precedencia(pilha.top()) >= precedencia(char)):
                    posfixa.append(pilha.pop())
                pilha.push(char)
    
    if numero:
        posfixa.append(numero)
    
    while not pilha.is_empty():
        posfixa.append(pilha.pop())
    
    return posfixa


def avalia_posfixa(posfixa):
    pilha = ArrayStack()
    
    for token in posfixa:
        if token.isdigit() or (token[0] == '-' and len(token) > 1):
            pilha.push(int(token))
        else:
            b = pilha.pop()
            a = pilha.pop()
            
            if token == '+':
                pilha.push(a + b)
            elif token == '-':
                pilha.push(a - b)
            elif token == '*':
                pilha.push(a * b)
            elif token == '/':
                pilha.push(int(a / b))
            elif token == '^':
                pilha.push(a ** b)
    
    return pilha.pop()


def calcular(expressao):
    expressao = expressao.replace(" ", "")
    posfixa = infixa_para_posfixa(expressao)
    resultado = avalia_posfixa(posfixa)
    return resultado, posfixa


while True:
    expressao = input("→ ")
    
    if expressao.lower() == 'sair':
        break
    
    if not expressao:
        continue
    
    try:
        resultado, posfixa = calcular(expressao)
        print(f"Pos-fixa: {' '.join(posfixa)}")
        print(f"Resultado: {resultado}")
    except Exception as e:
        print(" Erro: Expressao inválida")