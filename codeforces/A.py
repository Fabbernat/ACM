def block_game(a, b):
    if b == 0:
        return "win"
    if a % b == 0: 
        return "lose"
    return block_game(b, a % b)

a, b = map(int, input().split())
print(block_game(a, b))