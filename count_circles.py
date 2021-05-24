def count_circles(list_of_circles, point):
    count = 0
    for dot in list_of_circles:

        ax = dot[0][0]
        ay = dot[0][1]
        bx = dot[1][0]
        by = dot[1][1]
        cx = dot[2][0]
        cy = dot[2][1]
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

        ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
        uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d

        r = ((dot[0][0] - ux) ** 2 + (dot[0][1] - uy) ** 2) ** 0.5

        if (point[0] - ux) ** 2 + (point[1] - uy) ** 2 <= r ** 2 + 0.00001:
            count += 1

    return count