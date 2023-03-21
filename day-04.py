import sys

def set_from_range(range_str):
    """ returns 2 sets from a range string: 'x-y' """
    low, high = list(map(int, range_str.split('-')))
    return {x for x in range(low, high+1)}

if __name__ == "__main__":
    print(f'starting...')
 
    with open(sys.argv[1]) as file_handle:
        content = file_handle.read()
    lines = content.strip().split('\n')

    print(f'read {len(lines)} lines')

    # Part 1
    subset_count = 0
    for line in lines:
        set_1 = set_from_range(line.split(',')[0])
        set_2 = set_from_range(line.split(',')[1])
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            subset_count += 1
    print(f'found {subset_count} subsets')

    # Part 2
    intersection_count = 0
    for line in lines:
        set_1 = set_from_range(line.split(',')[0])
        set_2 = set_from_range(line.split(',')[1])
        if len(set_1 & set_2) > 0:
            intersection_count += 1
    print(f'found {intersection_count} intersections')


