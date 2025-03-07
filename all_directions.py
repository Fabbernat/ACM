import math

def process_directions(x, y, directions):
    parts = directions.split()
    i = 0
    current_x, current_y = x, y
    angle = 0

    while i < len(parts):
        if parts[i] == 'start':
            angle = float(parts[i + 1])
            i += 2
        elif parts[i] == 'turn':
            angle += float(parts[i + 1])
            i += 2
        elif parts[i] == 'walk':
            distance = float(parts[i + 1])
            radian_angle = math.radians(angle)
            current_x += distance * math.cos(radian_angle)
            current_y += distance * math.sin(radian_angle)
            i += 2

    return current_x, current_y

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


while True:
    n = int(input())
    if n == 0:
        break

    final_positions = []
    for _ in range(n):
        line = input().strip()
        space_index = line.find(' ', line.find(' ') + 1)
        x, y = map(float, line[:space_index].split())
        directions = line[space_index + 1:]

        end_x, end_y = process_directions(x, y, directions)
        final_positions.append((end_x, end_y))

    average_x = sum(pos[0] for pos in final_positions) / n
    average_y = sum(pos[1] for pos in final_positions) / n

    max_distance = 0
    for pos_x, pos_y in final_positions:
        distance = calculate_distance(pos_x, pos_y, average_x, average_y)
        max_distance = max(max_distance, distance)

    print(f'{average_x: .4f} {average_y: .4f} {max_distance:.5f}'.rstrip('0').rstrip('.') if '.0000' in f'{max_distance:.5f}' else f'{average_x: .4f} {average_y: .4f} {max_distance:.5f}')