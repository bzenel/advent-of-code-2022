
if __name__ == "__main__":
    print(f'starting...')

    with open('day-01.txt') as file_handle:
        contents = file_handle.read()

    elf_list_raw = contents.split('\n\n')
    print(f'read {len(contents)} chars, raw list is {len(elf_list_raw)}')

    sum_list = [sum([int(x) for x in y.split('\n')]) for y in elf_list_raw]

    # max_cal = 0
    # max_elf = 0
    # for index, value in enumerate(elf_list_raw):
    #     cal_list = value.split('\n')
    #     print(f'{index}: {cal_list}')
    #     if sum([int(x) for x in cal_list]) > max_cal:
    #         max_cal = sum([int(x) for x in cal_list])
    #         max_elf = index

    sum_list.sort(reverse=True)
    
    print(f'max cal is: {max(sum_list)}, top 3 sum is: {sum(sum_list[0:3])}')


