outputs = ['win', 'lose']
index = False
my_turn  = True

lower, higher = sorted(map(int, input().split()))

while True:
    if lower == 1:
        print(outputs[index])
        break
    elif higher % lower == 0:
        print(outputs[index])
        break
    else:
        oszto = higher // lower
        higher -= oszto * lower
        if oszto > 1:
            if my_turn:
                print('win')
                break
            else:
                print('lose')
                break
        higher, lower = lower, higher
    index = not index
    my_turn = not my_turn