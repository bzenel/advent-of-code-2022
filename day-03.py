def priority(val):
    if val.islower() is True:
        return ord(val) - ord('a') + 1
    else:
        return ord(val) - ord('A') + 27

if __name__ == "__main__":
    print(f'starting...')

    with open('day-03.txt') as file_handle:
        lines = file_handle.readlines()
    print(f'read {len(lines)} lines')
    # total = 0
    # for line in lines:
    #     half_line_len = int(len(line.strip())/2)
    #     print(f'half line len: {half_line_len}')
    #     part_1 = set(line[0:half_line_len])
    #     part_2 = set(line[half_line_len:])
    #     separator = str(list(part_1 & part_2)[0])
    #     print(f'separator is {separator}, priority is {priority(separator)}')
    #     total += priority(separator)
    # print(f'Total is {total}')

    total = 0
    for index in range(0, len(lines), 3):
        part_1 = set(lines[index].strip())
        part_2 = set(lines[index+1].strip())
        part_3 = set(lines[index+2].strip())

        badge = str(list(part_1 & part_2 & part_3)[0])
        print(f'group: {int(index/3)}, badge is {badge}, priority is {priority(badge)}')
        total += priority(badge)
    print(f'Total is {total}')




