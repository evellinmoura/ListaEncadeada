class ArrayStack:
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        return self._data.pop()


def verifica_parenteses(expressao):
    """Verifica se os parênteses estão bem formados"""
    pilha = ArrayStack()
    
    for char in expressao:
        if char == '(':
            pilha.push(char)
        elif char == ')':
            if pilha.is_empty():
                return False
            pilha.pop()
    
    return pilha.is_empty()


# Programa principal
print("=" * 50)
print("VERIFICADOR DE PARÊNTESES")
print("=" * 50)

while True:
    print("\nDigite uma expressão (ou 'sair' para encerrar):")
    expressao = input("→ ")
    
    if expressao.lower() == 'sair':
        print("Encerrando...")
        break
    
    if verifica_parenteses(expressao):
        print("✓ Parênteses bem formados!")
    else:
        print("✗ Parênteses mal formados!")
    
    print("-" * 50)