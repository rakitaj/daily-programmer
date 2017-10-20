def create_lists_from_input(path):
    rows = list()
    with open(path, "r") as raw_input:
        for row in raw_input:
            numbers_as_ints = [int(i) for i in row.split()]
            rows.append(numbers_as_ints)
    return rows

def find_consecutive_distance(row):
    total_distance = 0
    sep = 1
    done_pairs = list()
    for i in range(0, len(row)):
        for j in range(i + 1, len(row)):
            pair = (min(i, j), max(i, j))
            if abs(row[i] - row[j]) == 1 and pair not in done_pairs:
                distance = j - i
                total_distance += distance
                done_pairs.append(pair)
    return total_distance

if __name__ == "__main__":
    rows = create_lists_from_input("cd_challenge_input.txt")
    for row in rows[1:]:
        print(find_consecutive_distance(row)) 