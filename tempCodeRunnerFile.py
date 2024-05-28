# Solicitando entrada do usuário e armazenando os valores em variáveis
entrada = int(input("Digite um valor:"))  # Lê um valor inteiro do usuário
operador = input("Digite uma operação:")  # Lê um operador (string) do usuário
segundaEntrada = int(input("Digite um segundo valor:"))  # Lê um segundo valor inteiro do usuário

# Forma mais fácil de concatenar usando vírgula no print (automaticamente adiciona espaços)
print(entrada, operador, segundaEntrada)

# float = números com casas decimais
# double = faz a mesma coisa, só que melhor (consome mais espaço de memória) - Nota: em Python, temos apenas float
#Condicionais
if(operador == '+'):
    print('soma')
elif(operador == '-'):
    print('subtração')
elif(operador == '*'):
    print('multiplicação')
elif(operador == '/'):
    print('divisão')
else:
    print("Operador inválido")
# Laços de repetição

# Exemplo de laço while
# Continua a execução enquanto a condição entrada > 0 for verdadeira
while entrada > 0:
    print(entrada)
    entrada -= 1  # Decrementa o valor de entrada em 1 a cada iteração

# Exemplo de laço for
# Itera sobre um intervalo definido (de 0 até segundaEntrada - 1)
for entrada in range(0, segundaEntrada):
    print(entrada)

# Funções - realizam uma tarefa específica e podem retornar um valor. Podem ser chamadas em qualquer parte do programa.
#Os decoradores é um conceito em python onde uma função caceita outra função como parametro, e aprimora seu comportamento sem alterar seu código.
def decorador(funcao):
    def wrapper(a, b):
        resultado = funcao(a, b)
        return f"O resultado é: {resultado}"
    return wrapper

@decorador
def soma(a, b):
    return a + b
@decorador
def subtracao(a, b):
    return a - b

@decorador
def multiplicacao(a, b):
    return a * b

@decorador
def divisao(a, b):
    return a / b

# Chamando a função soma com os argumentos entrada e segundaEntrada
# No contexto atual, 'entrada' foi alterada pelo loop for anterior, então pode não ser o valor original
print(soma(entrada, segundaEntrada))

# Métodos - são funções que pertencem a um objeto e são invocados em instâncias de classes.

#recursão - muito útil para problemas que podem ser divididos em subproblemas menores
def fatorial(n):
    if n<1 :
        return 1
    return n*fatorial(n-1)

print(fatorial(5))

#Estrutura de dados

# Listas
lista = [1, 2, 3, 4, 5]  # Lista de números, indica-se que sejam valores homogeneos (mesma tipagem e significado), 
print(lista)  # Exibe a lista

# Tuplas
tupla = (lista, ['Enéas', "é", "foad"])  # Tupla de números inteiros (imutável), oculpa menos espaço de memória que uma lista
print(tupla)  # Exibe a tupla

#apesar de tuplas serem listas estaticas, podem conter listas dinamicas como atributos, assim podendo ser alteradas

tupla[0].append(6)  # Adiciona o valor 6 à lista dentro da tupla
print(tupla)  # Exibe a tupla

# Dicionários
dicionario = {'nome': 'João', 'idade': 20}  # Dicionário com chaves e valores, copia barata e na cara de pau de JSON
print(dicionario.items())  # Exibe o dicionário

# Conjuntos (sets)
conjunto = {1, 2, 3, 4, 5}  # Conjunto de números (não permite duplicatas)
print(conjunto)  # Exibe o conjunto

# Nota adicional: no Python moderno (Python 3.x), 'float' é a única representação de números de ponto flutuante. 
# 'double' é um termo mais comum em outras linguagens como C e Java, onde representa um número de ponto flutuante com precisão dupla (mais bits de precisão em comparação a float).

#classes
#Metodos que começam e terminam com `__` são metodos reservados do python, que executam ações especificaspré definidas
class Pessoa:
    def __init__(self, nome, idade):
        #__init__ é um método especial que é chamado quando uma instância da classe é criada AUTOMATICAMENTE garantindo que realmente seja criado
        #self é uma copia do 'this' de outras linguagens, onde atua como uma referencia para as variaveis do metodo
        self.nome = nome
        self.idade = idade

    def __str__(self):
        #Lembrando que o __str__ é um metodo reservado do python que é chamado quando a função print é chamada, garantindo que a saida padrão (toString de outras linguagens) seja exibida da forma que nos formatamos
        #return f'Nome: {self.nome}, Idade: {self.idade}'
        return f'Nome: {self.nome}\nIdade: {self.idade}'

pessoa=Pessoa('João', 20)
print(pessoa) #exibe o objeto pessoa

#Herança
#A herança é um conceito muito importante em programação orientada a objetos, pois permite a reutilização de código e a criação de uma hierarquia de classes.
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) #super() é uma função que retorna uma referência à classe pai, permitindo que você chame métodos da classe pai.
        self.matricula = matricula

    #Polimorfismo
    #O polimorfismo é um conceito que permite que objetos de diferentes classes sejam tratados de maneira uniforme.
    #Em Python, o polimorfismo é implementado por meio de métodos com o mesmo nome em classes diferentes.
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nMatrícula: {self.matricula}' #aqui a adicão do campo matricula faz o polimorfismo

    #Encapsulamento
    #O encapsulamento é um conceito que consiste em ocultar os detalhes de implementação de um objeto e expor apenas a interface.
    #Em Python, não existem modificadores de acesso como em outras linguagens (public, private, protected), mas é possível simular o encapsulamento usando métodos getters e setters.
    def get_matricula(self):
        return self.matricula
    def set_matricula(self, matricula):
        self.matricula = matricula

aluno = Aluno('Maria', 25, '12345')
print(aluno) #exibe o objeto aluno

#Aqui é um exemplo de polimorfismo, onde o objeto aluno é tratado como um objeto pessoa
pessoa = aluno
print(pessoa) #exibe o objeto pessoa

#Aqui é um exemplo de encapsulamento, onde o campo matricula é acessado e alterado por métodos
print(aluno.get_matricula())
aluno.set_matricula('54321')
print(aluno.get_matricula())