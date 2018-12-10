def parse_area_coords(full_string: str) -> tuple:
    """Given a line describing an area of a matrix,
    return all the coordinates within that area and the square id.

    Ex: #1 @ 258,327: 19x22
        -> #1, [(258, 327), (259, 327), ..., (276, 327), ..., (276, 348)]"""
    square_id, _, left_top, area = full_string.split(' ')
    left, top = [int(num) for num in left_top[:-1].split(',')]
    width, height = [int(num) for num in area.split('x')]

    return square_id, [(i, j) for i in range(left, left + width) for j in range(top, top + height)]


if __name__ == "__main__":
    id_coords = {}

    with open('input.txt') as data:
        while True:
            line = data.readline()
            if not line:
                break
            square_id, coordinates = parse_area_coords(line)
            coord_set = set(coordinates)

            id_coords[square_id] = coord_set

    for sqid, coords in id_coords.items():
        intersection_found = False

        for compid, comp_coords in id_coords.items():
            if sqid == compid:
                continue

            if coords.intersection(comp_coords):
                intersection_found = True
                break

        if not intersection_found:
            print("This one has no intersections!")
            break

    print(f"The unique ID is {sqid}")