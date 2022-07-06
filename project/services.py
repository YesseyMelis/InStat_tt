from project.table_state import XOTable


def check_table(xo_table: XOTable):
    if not xo_table.started:
        return 'Пусто'
    else:
        won = None
        table = xo_table.table
        if table[0][0] == table[0][1] == table[0][2]:
            won = table[0][0]
        elif table[1][0] == table[1][1] == table[1][2]:
            won = table[1][0]
        elif table[2][0] == table[2][1] == table[2][2]:
            won = table[2][0]
        elif table[0][0] == table[1][0] == table[2][0]:
            won = table[0][0]
        elif table[0][1] == table[1][1] == table[2][1]:
            won = table[0][1]
        elif table[0][2] == table[1][2] == table[2][2]:
            won = table[0][2]
        elif table[0][0] == table[1][1] == table[2][2]:
            won = table[0][0]
        elif table[0][2] == table[1][1] == table[2][0]:
            won = table[0][2]
        if won:
            return f'Выиграла сторона: {won}'
        else:
            return 'Идет игра'
