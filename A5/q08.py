"""Question 8."""

# Jacky Zheng
# Gray Chen

"""Test cases should include coincident, intersect, and parallel."""


def line_intersect(line1, line2):  # We created the function
    slope1 = (line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0])
    slope2 = (line2[1][1] - line2[0][1]) / (line2[1][0] - line2[0][0])

    intercept1 = line1[0][1] - (slope1*line1[0][0])
    intercept2 = line2[0][1] - (slope2*line2[0][0])

    if slope1 - slope2 == 0 and intercept1 == intercept2:
        return line1

    elif slope1 == slope2:
        return None  # means the lines are parallel

    else:
        x_intersection = (intercept2 - intercept1) / (slope1 - slope2)
        y_intersection = (slope1 * x_intersection) + intercept1
        return [x_intersection, y_intersection]


class TestLineIntersect(TestCase):
    def test_line_intersect_coincident(self):
        coincident = line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.0, 0.0], [1.0, 3.0]])
        self.assertEqual(coincident, [[0.0, 0.0], [1.0, 3.0]])

    def test_line_intersect_parallel(self):
        parallel = line_intersect([[0.0, 1.0], [1.0, 4.0]], [[0.0, 0.0], [1.0, 3.0]])
        self.assertEqual(parallel, None)

    def test_line_intersect(self):
        intersect = line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.5, 0.75], [1, 0]])
        self.assertEqual(intersect, [0.3333333333333333, 1.0])

    def test_line_intersect_type(self):
        coincident = line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.0, 0.0], [1.0, 3.0]])
        self.assertIsInstance(coincident, list)

    def test_line_intersect_type_None(self):
        parallel = line_intersect([[0.0, 1.0], [1.0, 4.0]], [[0.0, 0.0], [1.0, 3.0]])
        self.assertIs(parallel, None)
