from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """
        Class to represent the near earth objects that are making the close approaches to earth.
    """
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False):
        """Create a new `NearEarthObject`."""
        self.designation = designation
        self.name = name
        self.diameter = float(diameter)
        self.hazardous = hazardous

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f'{self.designation} {self.name}' if self.name else f'{self.designation}'

    def __str__(self):
        """Return a human-readable and full description of the NEO"""
        return f"{self.fullname} is a {'dangerous' if self.hazardous else 'harmless'} NearEarthObject with a " \
               f"diameter of {self.diameter:.3f} km"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A class to store data about the close approaches various NEOs make to earth"""
    def __init__(self, designation, time, distance, velocity):
        """Create a new `CloseApproach`"""
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity

        # Create an attribute to the NEO that is making the approach.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return human-readable description of a close approach"""
        return f"A CloseApproach by {self.neo.fullname} occurred at {self.time_str} with a velocity of {self.velocity} " \
               f"km/s and distance of {self.distance} au"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
