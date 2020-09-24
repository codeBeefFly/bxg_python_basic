index = 1
while index < 5:
    print('*' * index)
    index += 1

print('\n' + '#' * 5 + '\n')

index = 5
while index > 0:
    print('*' * index)
    index -= 1

print('\n' + '#' * 5 + '\n')

index_max = 5
index = index_max
while index > 0:
    # space_count = index - 1
    # star_count = index - space_count
    star_count = index
    space_count = index_max - star_count
    print(' ' * space_count + '*' * star_count)
    index -= 1