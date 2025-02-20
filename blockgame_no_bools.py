lower, higher = sorted(map(int, input().split()))
outputs = ['win', 'lose']
index = 0
my_turn  = 1
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
    index = 1 - index
    my_turn = 1 - my_turn