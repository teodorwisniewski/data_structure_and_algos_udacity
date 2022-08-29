

def draw_christmas_tree(nb_of_rows: int) -> None:
    counter = 1
    for row_nb in range(nb_of_rows):
        row_to_print = " " * (nb_of_rows - row_nb) + "*" * counter
        print(row_to_print)
        counter += 2


draw_christmas_tree(6)