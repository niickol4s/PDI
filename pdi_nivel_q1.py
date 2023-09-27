import os

def salaryAdjustment(slr):
    
    if slr <= 280:
        newSlr = slr + (slr * 20 / 100)
        ics = newSlr - slr
        pct = (newSlr - slr) / slr * 100
        return pct, ics, newSlr
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

while True:

    print('Escolha uma opção:\n')
    print('1 - Inserir salário;')
    print('0 - Encerrar.')
    option = int(input('\nOpção: '))
    
    os.system('cls')
    
    match option:
        case 1:
            salary = float(input('\nSalário (R$): '))

            adjustment = salaryAdjustment(salary)

            percentage, increase, newSalary = adjustment

            print('\nInformações salariais: ')
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
