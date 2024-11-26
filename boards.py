def create_boards(filepath):
    boards= []
    with open(filepath,'r') as file:
        curr_board = []

        for line in file:
            line = line.strip()
            if line == "":
                continue
            numbers = [int(num) for num in line.split()]

            if len(numbers) == 81:
                board = [numbers[i:i + 9] for i in range(0,81,9)]
                boards.append(board)
    return boards
