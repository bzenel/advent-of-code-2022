
if __name__ == "__main__":
    print(f'starting...')

    player_score = [0,0]
    points_part_1 = {
        'AX': [1+3, 1+3],
        'AY': [1+0, 2+6],
        'AZ': [1+6, 3+0],
        'BX': [2+6, 1+0],
        'BY': [2+3, 2+3],
        'BZ': [2+0, 3+6],
        'CX': [3+0, 1+6],
        'CY': [3+6, 2+0],
        'CZ': [3+3, 3+3]
    }

    points_part_2 = {
        'AX': [1+3, 3+0],  # loss (rock v. scissor)
        'AY': [1+0, 1+3],  # draw (rock v. rock)
        'AZ': [1+6, 2+6],  # win (rock v. paper)
        'BX': [2+6, 1+0],  # loss (paper v. rock)
        'BY': [2+3, 2+3],  # draw (paper v. paper)
        'BZ': [2+0, 3+6],  # win (paper v. scissor)
        'CX': [3+0, 2+0],  # loss (scissor v. paper)
        'CY': [3+6, 3+3],  # draw (scissor v. scissor)
        'CZ': [3+3, 1+6]   # win (scissor v. rock)
    }

    with open('day-02.txt') as file_handle:
        lines = file_handle.readlines()
    print(f'read {len(lines)} lines')
    for line in lines:
        # print(f'line: {line}')
        index = line.strip().replace(' ', '')
        player_score[0] += points_part_2[index][0]
        player_score[1] += points_part_2[index][1]

    print(f'player 0: {player_score[0]}, player 1: {player_score[1]}')




