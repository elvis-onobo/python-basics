# generators are a way to create iterators in an efficient manner

def count_up_to(max):
    count = 1
    while count <= max:
        yield count # uses yeild instead of return
        count += 1


counter = count_up_to(10)
for num in counter:
    print(num)


# TODO: find out why generators are considered efficient