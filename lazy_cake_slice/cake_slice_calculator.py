#!/usr/bin/env python

"""
Let's say we had a slice of cake and we wanted to split it equally with a
friend. We could bisect the narrow, "point" angle as a reasonable person might,
but let's say we're being lazy and we want don't want to cut the slice of cake
along its long axis.

The associated figure shows the a stylized version of the cut we want to make,
which should adhere to the following points:

1. The cut equally divides the slice of cake into two pieces of equal size
2. The line segment formed by the cut made by the knife has one endpoint on a
   "corner" and the other on a straight edge opposite this "corner"

(See the associated graphic for an illustration of the desired cut.)

A few other definitions & assumptions:

- A "corner" of a cake slice is defined as the intersection of a straight cake
  edge and the arc formed by the outer rim of the slice of cake. (Hence, there
  are two "corners". We'll call the where the two straight edges meet the
  "point" of the slice.
- The cake's depth (when looked upon from above) is uniform.
- The cake is circular and initially divvied up into equal slices formed by
  cutting along the diameter of the cake. That is to say the circular cake was
  sliced in the "traditional" way initially.
- Assume the circular cake was originally sliced into at least 3 equal slices.
- Treat all angles in degrees unless otherwise noted.
"""


import math


class CakeSlice:

    TOLERANCE = 0.01

    def __init__(self, total_cake_slices: int, cake_radius: float):
        if total_cake_slices < 3:
            raise ValueError("There must be at least three total cake slices!")
        self._total_cake_slices = total_cake_slices
        self._cake_radius = cake_radius

    @staticmethod
    def triangle_area_calculator(base: float, height: float) -> float:
        return 0.5 * base * height

    @property
    def point_angle(self):
        self._point_angle = 360 / self._total_cake_slices
        return self._point_angle

    @property
    def corner_angle(self):
        self._corner_angle = (180 - self.point_angle) / 2
        return self._corner_angle

    @property
    def apothem(self):
        self._apothem = self._cake_radius * math.cos(math.radians(self.point_angle) / 2)
        return self._apothem

    @property
    def slice_berth(self):
        self._slice_berth = (
            math.sin(math.radians(self.point_angle) / 2) * self._cake_radius * 2
        )
        return self._slice_berth

    @property
    def triangle_area(self):
        self._triangle_area = CakeSlice.triangle_area_calculator(
            self.slice_berth, self.apothem
        )
        return self._triangle_area

    @property
    def rim_area(self):
        total_cake_area = math.pi * (self._cake_radius ** 2)
        self._rim_area = (
            total_cake_area - (self._total_cake_slices * self.triangle_area)
        ) / self._total_cake_slices
        return self._rim_area

    @property
    def slice_area(self):
        self._slice_area = self.triangle_area + self.rim_area
        return self._slice_area

    # TODO: Fix float precision; method fails tests at large scales
    def knife_angles(self, precision: float = 0.001) -> float:
        """
        Returns the knife angles which divides the cake slice into equal parts
        and that conforms to the requirements in the module docstring
        """

        def piece_details(beta: float) -> tuple:
            """
            Helper function that calculates area of one piece of slice
            """
            alpha = self.point_angle
            gamma = 180 - (alpha + beta)
            side_b = (
                math.sin(math.radians(beta))
                * self._cake_radius
                / math.sin(math.radians(gamma))
            )
            piece_altitude = side_b * math.sin(math.radians(alpha))
            return (
                CakeSlice.triangle_area_calculator(self._cake_radius, piece_altitude),
                gamma,
            )

        equal_piece_area = self.slice_area / 2
        beta = self.corner_angle
        piece_area, gamma = piece_details(beta)
        delta = piece_area - equal_piece_area

        while delta > self.TOLERANCE:
            beta -= precision
            piece_area, gamma = piece_details(beta)
            delta = piece_area - equal_piece_area

        return beta, gamma, piece_area


if __name__ == "__main__":
    slice_of_cake = CakeSlice(4, 8)
    print(slice_of_cake.knife_angles(0.001))
