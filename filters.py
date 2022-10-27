"""Provide filters for querying close approaches and limit the generated results.

The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

This function can be thought to return a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`.

The `limit` function simply limits the maximum number of values produced by an
iterator.

You'll edit this file in Tasks 3a and 3c.
"""
import itertools
import operator


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    """A general superclass for filters on comparable attributes."""
    def __init__(self, op, value):
        """
        :param op: A 2-argument predicate comparator (such as `operator.le`).
        :param value: The reference value to compare against.
        """
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach.

        Concrete subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`.

        :param approach: A `CloseApproach` on which to evaluate this filter.
        :return: The value of an attribute of interest, comparable to `self.value` via `self.op`.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"


"""A set of child classes to generate the filters necessary to return the requested dataset"""


class DateFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.time.date()


class DistanceFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.distance


class VelocityFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.velocity


class DiameterFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.diameter


class HazardFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.hazardous


def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    """Create a collection of filters from user-specified criteria.
        :param date: A `date` on which a matching `CloseApproach` occurs.
        :param start_date: A `date` on or after which a matching `CloseApproach` occurs.
        :param end_date: A `date` on or before which a matching `CloseApproach` occurs.
        :param distance_min: A minimum nominal approach distance for a matching `CloseApproach`.
        :param distance_max: A maximum nominal approach distance for a matching `CloseApproach`.
        :param velocity_min: A minimum relative approach velocity for a matching `CloseApproach`.
        :param velocity_max: A maximum relative approach velocity for a matching `CloseApproach`.
        :param diameter_min: A minimum diameter of the NEO of a matching `CloseApproach`.
        :param diameter_max: A maximum diameter of the NEO of a matching `CloseApproach`.
        :param hazardous: Whether the NEO of a matching `CloseApproach` is potentially hazardous.
        :return: A collection of filters for use with `query`.
        """

    filters = []
    if date is not None:
        f_d = DateFilter(operator.eq, date)
        filters.append(f_d)

    if start_date:

        f_start = DateFilter(operator.ge, start_date)
        filters.append(f_start)

    if end_date:
        f_end = DateFilter(operator.le, end_date)
        filters.append(f_end)

    if distance_min:
        f_dist_min = DistanceFilter(operator.ge, distance_min)
        filters.append(f_dist_min)

    if distance_max:
        f_dist_max = DistanceFilter(operator.le, distance_max)
        filters.append(f_dist_max)

    if velocity_min:
        f_v_min = VelocityFilter(operator.ge, velocity_min)
        filters.append(f_v_min)

    if velocity_max:
        f_v_max = VelocityFilter(operator.le, velocity_max)
        filters.append(f_v_max)

    if diameter_min:
        f_dia_min = DiameterFilter(operator.ge, diameter_min)
        filters.append(f_dia_min)

    if diameter_max:
        f_dia_max = DiameterFilter(operator.le, diameter_max)
        filters.append(f_dia_max)

    if hazardous is not None:
        f_hazard = HazardFilter(operator.eq, hazardous)
        filters.append(f_hazard)

    return filters


def limit(iterator, n=None):
    """Function to limit the number of generator items returned to the user
    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    if n:
        return itertools.islice(iterator, 0, n)
    return iterator
