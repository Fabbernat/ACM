import enum


class Dirs(enum.Enum):
    fd = 'forward'
    bd = 'backward'
    lt = 'turn_left'
    rt = 'turn_right'

# ha közel van a 0 vagy a 359 fokhoz, akkor szinte a teljes value-t hozzá kell adni, de ha 120, vagy 180, akkor az is lehet, hogy közelít a `fd` és távolít a `bd`
'''
            elif command == 'fd':
                dist += 1 + int(value * degree % 180)
'''