#! /usr/bin/env python3

#action function
class CoffeeMachine:
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        global coffeeType
        coffeeType={
            '1':[250, 0, 16 ,1 ,4],
            '2':[350, 75, 20 ,1, 7],
            '3':[200, 100 ,12, 1, 6],
            'back':[0, 0, 0, 0, 0] }
        global currentState
        currentState = {'water': self.water,'milk': self.milk, 'coffee beans': self.beans, 'disposable cups': self.cups, 'money':self.money}
        self.UI_method()


    def UI_method(self):
        action=input('Write action (buy,fill,take,remaining,exit):')
        while action!='exit':
            if action=='buy':
                buy()
            elif action=='fill':
                fill()
            elif action=='take':
                take()
            elif action=='remaining':
                printState(currentState)
            action=input('Write action (buy,fill,take,remaining,exit):')

def printState(currentState):
    print('The coffee machine has:')
    for item in currentState:
        print(str(currentState[item])+' of '+ item)

def buy():
    chosedCoffee=coffeeType[input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')]
    if chosedCoffee!='back':
        currentAmount=[]
        for item in currentState:
            if item!='money':
                currentAmount.append(currentState[item])
        enoughSupplies=[1,1,1,1,1]

        def checkSupplies(currentAmount, chosedCoffee):
            h=0
            for a, b in zip(currentAmount, chosedCoffee):
                enoughSupplies[h]=int(a > b)
                h+=1
            return enoughSupplies
        checkSupplies(currentAmount, chosedCoffee[:-1])

        if 0 not in enoughSupplies:
            print('I have enough resources, making you a coffee!')
            def updateState(chosedCoffee):
                i=0
                for item in currentState:
                    if item!='money':
                        currentState[item]-=chosedCoffee[i]
                    elif item=='money':
                        currentState[item]+=chosedCoffee[i]
                    i+=1
            updateState(chosedCoffee)
        if 0 in enoughSupplies:
            for item in currentState:
                v=0
                if enoughSupplies[v]==0:
                    print('Sorry, not enough '+item)
                    break
                else:
                    v+=1

def fill():
    fillAmount=['ml of water',
    'ml of milk',
    'grams of coffee beans',
    'disposable cups of coffee' ]
    i=0
    for item in currentState:
        if item!='money':
                currentState[item]+=int(input('Write how many '+ fillAmount[i]+' do you want to add:'))
                i+=1

def take():
    print('I give you $'+ str(currentState['money']))
    currentState['money']=0

#run coffee machine
CoffeeMachine()
