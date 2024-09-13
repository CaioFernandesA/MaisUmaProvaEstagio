# Exercicio 1 Fibonacci

def fibonacci_pertence(numero):
    a, b = 0, 1
    sequencia = [a, b]
    while b < numero:
        a, b = b, a + b
        sequencia.append(b)

    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."


numero_informado = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))


resultado = fibonacci_pertence(numero_informado)
print(resultado)


# Exercicio 2 checa string M ou m

def verifica_letra_a(string):
    quantidade_a = string.lower().count('a')
    
    if quantidade_a > 0:
        return f"A letra 'a' ocorre {quantidade_a} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."


string_informada = input("Informe uma string: ")


resultado = verifica_letra_a(string_informada)
print(resultado)


# Exercicio 3 soma

int INDICE = 12, SOMA = 0, K = 1;

enquanto K < INDICE faça {
    K = K + 1;
    SOMA = SOMA + K;
}

imprimir(SOMA);
# De acordo com o código, a soma vai dar 77.



# Exercicio 4 de lógica

# a)9 b)128 c)49 d)100 e)13 f)20


# Exercicio 5 interruptor

# Para descobrir qual interruptor controla cada lâmpada com 
# apenas uma ida à sala das lâmpadas, é só fazer isso: 
# ligue o interruptor (A) e deixe eleligado por 
# alguns minutos, depois desligue-o e ligue o segundo 
# interruptor (B). Agora é só ir até a sala de lâmpadas. 
# A lâmpada que estiver acesa será controlada pelo interruptor B;
#  a lâmpada apagada, mas ainda quente, será controlada pelo interruptor A; 
# e a lâmpada apagada e fria será controlada pelo interruptor C.
#  Assim, podemos idengtificar cada interruptor em apenas uma ida à sala.