import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Save query results to a csv file to a user specified location
    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in results:
            entry_dict = {'datetime_utc': datetime_to_str(entry.time), 'distance_au': float(entry.distance),
                          'velocity_km_s': float(entry.velocity), 'designation': entry.neo.designation,
                          'name': entry.neo.name or '', 'diameter_km': float(entry.neo.diameter) or '',
                          'potentially_hazardous': entry.neo.hazardous}
            writer.writerow(entry_dict)


def write_to_json(results, filename):
    """Converts query results into a JSON file saved to a user specified location.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    with open(filename, 'w') as outfile:
        entry_list = []
        for entry in results:
            entry_dict = {'datetime_utc': datetime_to_str(entry.time), 'distance_au': float(entry.distance),
                          'velocity_km_s': float(entry.velocity), 'neo': {'designation': entry.neo.designation,
                          'name': entry.neo.name or '', 'diameter_km': entry.neo.diameter,
                          'potentially_hazardous': entry.neo.hazardous}}
            entry_list.append(entry_dict)
        json.dump(entry_list, outfile)
