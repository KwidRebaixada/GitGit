Segredo = 'zeit'
Digitadas = []
Chances = 10

print('Basicamente voce precisa ir digitando uma letra até completar a palavra, Voce tem 10 chances ok?. ( Lembrando que não tem letras em maísculo por preguiça da dev. Boa sorte :3')

while True:
    if Chances <= 0:
        print('Puts, Voce perdeu.')
  
    Letra = input('Digite uma Letra: ')
    
    if len(Letra) > 1:
        print('Ei! Isso não vale, digite apenas UMA letra.')
        continue 
    Digitadas.append(Letra) # Adcionar letras que já foram digitadas a sua lista
    
    if Letra.isnumeric():
        print('Opa, Não tem Números na Palavra secreta ok?')
        Digitadas.pop()
        continue


    if Letra in Segredo:
        print(f'Eba! a Letra {Letra} está na Palavra secreta rs. ')
    else:
        print(f'Puts! a Letra {Letra} não está na Palavra secreta :c ')
        Digitadas.pop() # Não permitir que letras que não existem na frase secreta fiquem em sua lista.
 
    Letra_Temp = '' 
    for Letra_Secreta in Segredo:
        if Letra_Secreta in Digitadas: 
            Letra_Temp += Letra_Secreta
        else:
            Letra_Temp += '*'
    print(Letra_Temp)

    if Letra_Temp == Segredo:
        print(f'Boa! Voce descobriu que a palavra secreta é {Segredo} ') #Usar f' se vc precisar colocar algo dentro das aspas como o {}
        break
    else:
        print(f'A palavra secreta está Assim: {Letra_Temp}')

    if Letra not in Segredo:
        Chances -= 1
    print(f'Voce ainda tem {Chances} Chances')
    print()

    