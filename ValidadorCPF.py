while True:
    CPF = input(' Digite seu CPF: ')
    
    if not CPF.isnumeric():
        print('Digite apenas números.')
        break
    
    if len(CPF) < 11 or len(CPF) > 11:
        print("Voce precisa digitar os 11 Números do seu CPF")
    
    NewCPF = CPF[:-2]
    Reverse = 10
    Total = 0 
    
    for index in range(19):
        if index > 8:
            index -=9
            
        Total += int(NewCPF[index]) * Reverse
        
        Reverse-= 1
        if Reverse <2:
            Reverse = 11
        Digito = 11 - (Total % 11)
        
        if Digito > 9:
            Digito = 0
        Total = 0
        NewCPF += str(Digito)
        
    if CPF == NewCPF:
        print(f'CPF {CPF} é Válido.')
    else:
        print(f'CPF {CPF} é Inválido.')
        
# algoritimo: """ CPF = 168.995.350-09
# 1 * 10 = 10           #    1 * 11 = 11 <-
# 6 * 9  = 54           #    6 * 10 = 60
# 8 * 8  = 64           #    8 *  9 = 72
# 9 * 7  = 63           #    9 *  8 = 72
# 9 * 6  = 54           #    9 *  7 = 63
# 95 * 5  = 25          #    5 *  6 = 30
# 3 * 4  = 12           #    3 *  5 = 15
# 5 * 3  = 15           #    5 *  4 = 20
# 0 * 2  = 0            #    0 *  3 = 0
                        # -> 0 *  2 = 0
#    297            #             343
# 11 - (297 % 11) = 11    #     11 - (343 % 11) = 9
# 11 > 9 = 0              #
# Digito 1 = 0            #   Digito 2 = 9