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


def eh_operador(char):
    """Verifica se é um operador"""
    return char in ['+', '-', '*', '/', '^']


def prefixo_para_infixa(expressao):
    """Converte notacao prefixada para infixa"""
    pilha = ArrayStack()
    
    # le da direita para esquerda
    for i in range(len(expressao) - 1, -1, -1):
        char = expressao[i]
        
        if eh_operador(char):
            
            op1 = pilha.pop()
            op2 = pilha.pop()
            
            temp = f"({op1}{char}{op2})"
            pilha.push(temp)
        else:
            
            pilha.push(char)
    
    return pilha.pop()


def prefixo_para_posfixa(expressao):
    """Converte notacao prefixada para pos-fixada"""
    pilha = ArrayStack()
    
    # le da direita para esquerda
    for i in range(len(expressao) - 1, -1, -1):
        char = expressao[i]
        
        if eh_operador(char):
          
            op1 = pilha.pop()
            op2 = pilha.pop()
            
            temp = f"{op1}{op2}{char}"
            pilha.push(temp)
        else:
            
            pilha.push(char)
    
    return pilha.pop()

print("=" * 60)
print("CONVERSOR DE NOTACAO PREFIXADA")
print("=" * 60)
print("\nNotacao prefixada: operador vem antes dos operandos")
print("Exemplo: +AB significa (A+B)")
print("         *+ABC significa ((A+B)*C)")
print("=" * 60)

while True:
    print("\nDigite uma expressao prefixada:")
    expressao = input("→ ").replace(" ", "")
    
    if expressao.lower() == 'sair':
        print("Encerrando...")
        break
    
    if not expressao:
        print("Expressão vazia!")
        continue
    
    try:
        infixa = prefixo_para_infixa(expressao)
        posfixa = prefixo_para_posfixa(expressao)
        
        print("\nResultados:")
        print(f"  Prefixada:  {expressao}")
        print(f"  Infixa:     {infixa}")
        print(f"  Pos-fixada: {posfixa}")
        
    except:
        print(" Erro: Expressao invalida")
    
    print("-" * 60)


