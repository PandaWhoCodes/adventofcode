def parse_area_coords(string):
    """Given a line describing an area of a matrix,
    return all the coordinates within that area.

    Ex: #1 @ 258,327: 19x22
        -> [(258, 327), (259, 327), ..., (276, 327), ..., (276, 348)]"""
    _, _, left_top, area = string.split(' ')
    left, top = [int(num) for num in left_top[:-1].split(',')]
    width, height = [int(num) for num in area.split('x')]

    return [(i, j) for i in range(left, left + width) for j in range(top, top + height)]


if __name__ == "__main__":
    coord_ct = {}
    overlap_ct = 0
    with open('input.txt') as data:
        while True:
            line = data.readline()
            if not line:
                break
            coordinates = parse_area_coords(line)
            for coord in coordinates:
                coord_ct.setdefault(coord, 0)
                coord_ct[coord] += 1

    for key, val in coord_ct.items():
        if val > 1:
            overlap_ct += 1
    print(overlap_ct)
