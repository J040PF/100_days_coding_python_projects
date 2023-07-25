print("welcome to treasure island"
      "your mission is find the treasure")


first = input('left or right')

a = 'fall into a rolle game over'
b = 'attacked by trout game over'
cr = 'burned by fire'
cy = 'You win '
cb = 'eaten by beasts game over'

if first == 'left':
    second = input('swim or wait')

    if second == 'swim':
        third = input('which door , red , yellow, blue')
        if third == 'yellow':
            print(cy)
        elif third == 'red':
            print(cr)
        elif third == 'blue':
            print(cb)
        else:
            print('game over')

    else:
        print(b)
else:
    print(a)
