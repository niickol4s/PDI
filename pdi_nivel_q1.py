# Nickolas Davi Vieira Lima

import os

def salaryAdjustment(slr): # Função para cálculo de reajuste e porcentagem. Recebe o salário.
    
    if slr <= 280: # Verificação do valor do salário.
        newSlr = slr + (slr * 20 / 100) # Cálculo do salário.
        ics = newSlr - slr # Cálculo do valor do aumento
        pct = (newSlr - slr) / slr * 100 # Cálculo da porcentagem.
        return pct, ics, newSlr # Retorno do percentual, valor do aumento e novo salário.
    elif 280 < slr < 700:
        newSlr = slr + (slr * 15 / 100)
        ics = newSlr - slr
        pct = (newSlr - slr) / slr * 100
        return pct, ics, newSlr
    elif 700 < slr < 1500:
        newSlr = slr + (slr * 10 / 100)
        ics = newSlr - slr
        pct = (newSlr - slr) / slr * 100
        return pct, ics, newSlr
    elif slr >= 1500:
        newSlr = slr + (slr * 5 / 100)
        ics = newSlr - slr
        pct = (newSlr - slr) / slr * 100
        return pct, ics, newSlr

while True: # Loop While True.

    print('Escolha uma opção:\n') # Menu de opções.
    print('1 - Inserir salário;')
    print('0 - Encerrar.')
    option = int(input('\nOpção: ')) # Leitura da opção.
    
    os.system('cls')
    
    match option: # Match Case da opção.
        case 1:
            salary = float(input('\nSalário (R$): ')) # Leitura do salário.

            adjustment = salaryAdjustment(salary) # Variável reajuste recebe função.

            percentage, increase, newSalary = adjustment # Atribuição dos respectivos valores retornados.

            print('\nInformações salariais: ') # Saída.
            print(f'Salário original (R$): {salary:.2f}')
            print(f'Aumento salarial (%): {percentage:.0f}')
            print(f'Valor do aumento (R$): {increase:.2f}')
            print(f'Salário atual (R$): {newSalary:.2f}')
        case 0:
            print('Programa encerrado.')
            break
        case _:
            print('Opção iválida.')
            option = int(input('Opção: '))
