from data_coffe import *


def rescus():
    # this report what is in machine
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']

    print('water: {}ml\n'
          'milk: {}ml\n'
          'coffee: {}g\n'
          'money: ${}'.format(water, milk, coffee, money))


def sub_res(option):
    '''
    analyze if there are sufficient ingredients to make the option
    get out of the machine resources
    '''

    coffee_ing = MENU[option]['ingredients']
    possible = True

    for y in coffee_ing.keys():
        ing_sub = coffee_ing[y]
        if ing_sub > resources[y]:
            possible = False

    if possible is True:
        mone = process_money(option)

        if mone:
            for x in coffee_ing.keys():
                ing_sub = coffee_ing[x]
                resources[x] -= ing_sub

    else:
        print('We are out of resources for making your {} , sorry'.format(option))


def process_money(coff):
    # take the coins, and give the change
    while True:
        valor = MENU[coff]['cost']

        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01

        res = valor - total
        if res == 0:
            print('making you coffee')
            resources['money']+= valor
            return True
        elif res < 0:
            print('insufficient money')
        else:
            print('you tip is {}'.format(res))
            print('making your coffe')
            resources['money'] += valor
            return True


def main():
    # it make the primary screen
    while True:

        try:

            op = input('What would you like? (espresso/latte/cappuccino):\n')

            if op == 'off':
                print('Turning off...')
                break
            elif op == 'report':
                rescus()
            else:
                sub_res(op)

        except:

            print('sorry your option is not available, please give another option')


main()
