class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """

        self._P = 0  # number of pixels (int)
        self._x = 0.0  # x-coordinate of center of mass (float)
        self._y = 0.0  # y-coordinate of center of mass (float)

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """

        self._x = (self._x * self._P + i) / (self._P + 1)
        self._y = (self._y * self._P + j) / (self._P + 1)
        self._P += 1

    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """

        return self._P

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """

        d = (other._x - self._x) ** 2.0 + (other._y - self._y) ** 2.0
        return d ** 0.5

    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)
