"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Load NEO data from dataset and return list of NearEarthObject instances"""
    neos = []
    with open(neo_csv_path, 'r') as csvfile:
        neo_reader = csv.DictReader(csvfile)
        for row in neo_reader:
            hazardous = True if row['pha'] == 'Y' else False
            new_object = NearEarthObject(designation=row['pdes'], hazardous=hazardous)
            if row['diameter']:
                new_object.diameter = float(row['diameter'])
            if row['name']:
                new_object.name = row['name']

            neos.append(new_object)
    return neos


def load_approaches(cad_json_path):
    cads = []
    with open(cad_json_path, 'r') as cad_json:
        cad_data = json.load(cad_json)
        for e in cad_data['data']:
            cads.append(CloseApproach(e[0], e[3], float(e[4]), float(e[7])))

    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    return cads
