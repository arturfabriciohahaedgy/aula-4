numeroA = 2
numeroB = 3

#operadores aritimeticos

#soma
resposta = numeroA + numeroB
print("resposta da soma: ", resposta)
print("resposta da soma: ", (numeroA + numeroB)) 

#Subtração
respostaSubtracao = numeroA - numeroB
print("resposta da soma: ", respostaSubtracao)
print("resposta da soma: ", (numeroA - numeroB))

#Multiplicação
respostaMultiplicao = numeroA * numeroB
print("resposta da multiplicação: ", respostaMultiplicao)
print("resposta da multiplicação: ", numeroA * numeroB)

#Expoente
respostaExpoente = numeroA**numeroB
print("resposta do expoente: ", respostaMultiplicao)
print("resposta do expoente: ", numeroA**numeroB)

#Operadores  Lógicos e Relacionais
print("Operador logico AND(e): ", (numeroA < 5 and numeroB > 10 ))
print("resposta logico OR(ou): ", (numeroA < 5 or numeroB > 20))
print("resposta logico de NEGAÇÃO NOT(não): ", (not(numeroA < 5 and numeroB < 10)))
print("resposta relacional != (diferente): ", (numeroA < 5 and numeroB))
print("resposta relacional <> (diferentes): ", (numeroA != numeroB))

#usando input pra ler String
armazenaValorTecido = input("Digite um texto: ")
print("O tipo de dado: ", type(armazenaValorTecido)) 
print("O texto digitado: ", armazenaValorTecido)  
#usando input pra ler inteiro
armazenaValorTecladoInt = int(input("Digite um valor inteiro: ")) 
print("O tipo de dado: ", type(armazenaValorTecido)) 
print("o valor digitado: ", (armazenaValorTecladoInt)) 
#usando input pra ler float
armazenaValorTecladoInt = float(input("Digite um valor real:  (Exemplo 2.50")) 
print("O tipo de dado: ", type(armazenaValorTecido)) 
print("o valor digitado: ", (armazenaValorTecladoInt)) 