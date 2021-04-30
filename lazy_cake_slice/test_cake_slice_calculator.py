import math

import pytest

from cake_slice_calculator import CakeSlice


def test_triangle_area_calculator():
    base = 20
    height = 10
    assert CakeSlice.triangle_area_calculator(base, height) == 100


@pytest.fixture(scope="class", params=[(3, 1_000), (4, 0.15), (8, 5)])
def slice_of_cake(request):
    total_cake_slices, cake_radius = request.param
    return CakeSlice(total_cake_slices, cake_radius)


@pytest.mark.usefixtures("slice_of_cake")
class TestCakeSlice:
    def test_point_angle_valid(self, slice_of_cake):
        assert 180 > slice_of_cake.point_angle and slice_of_cake.point_angle > 0

    def test_corner_angle_valid(self, slice_of_cake):
        assert 180 > slice_of_cake.corner_angle and slice_of_cake.corner_angle > 0

    def test_angles_make_triangle(self, slice_of_cake):
        assert 2 * slice_of_cake.corner_angle + slice_of_cake.point_angle == 180

    def test_total_cake_area_from_slice(self, slice_of_cake):
        total_cake_area = math.pi * (slice_of_cake._cake_radius ** 2)
        assert (
            abs(
                slice_of_cake.slice_area * slice_of_cake._total_cake_slices
                - total_cake_area
            )
            # Precise to thousandths of area units
            < 0.001
        )

    def test_total_rim_area_from_slice(self, slice_of_cake):
        total_cake_area = math.pi * (slice_of_cake._cake_radius ** 2)
        total_rim_area = total_cake_area - (
            slice_of_cake.triangle_area * slice_of_cake._total_cake_slices
        )
        assert (
            slice_of_cake.rim_area == total_rim_area / slice_of_cake._total_cake_slices
        )

    def test_knife_angles_valid(self, slice_of_cake):
        beta, gamma, _, _ = slice_of_cake.knife_angles()
        assert beta + gamma + slice_of_cake.point_angle

    @pytest.mark.parametrize("precision, tolerance", [(0.001, 0.01)])
    def test_piece_areas_equal(self, slice_of_cake, precision, tolerance):
        _, _, piece_area, _ = slice_of_cake.knife_angles(
            precision=precision, tolerance=tolerance
        )
        tolerance *= math.pi * slice_of_cake._cake_radius ** 2
        error = abs((slice_of_cake.slice_area / 2) - piece_area)
        assert error < tolerance

    @pytest.mark.parametrize("precision, tolerance", [(1.0, 0.01), (0.009, 0.01)])
    def test_precision_tolerance_exception(self, slice_of_cake, precision, tolerance):
        with pytest.raises(ValueError):
            slice_of_cake.knife_angles(precision, tolerance)
