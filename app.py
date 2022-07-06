from project.services import check_table
from project.table_state import XOTable


if __name__ == '__main__':
    table = XOTable()
    print(check_table(xo_table=table))
    table.add_x(1, 1)
    table.add_o(0, 1)
    table.add_x(0, 2)
    table.add_o(2, 0)
    table.add_x(2, 2)
    table.add_o(1, 2)
    print(check_table(xo_table=table))
    table.add_x(0, 0)
    print(check_table(xo_table=table))
