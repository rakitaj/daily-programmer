from typing import List, Union

def bon_appetit(not_eaten_index: int, bill: List[int], anna_paid: int) -> Union[int, str]:
    bill[not_eaten_index] = 0
    anna_ideal_total = sum(bill) / 2
    if anna_ideal_total == anna_paid:
        return "Bon Appetit"
    else:
        return int(anna_paid - anna_ideal_total)

if __name__ == "__main__":
    first_line = input()
    anna_didnt_eat_index = [int(n) for n in first_line.split()][1]
    second_line = input()
    bill_items = list()
    [bill_items.append(int(n)) for n in second_line.split()]
    anna_paid_input = int(input())

    print(bon_appetit(anna_didnt_eat_index, bill_items, anna_paid_input))
