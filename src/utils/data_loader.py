import json

def load_data(hospitals_file, resources_file):
    """
    Loads hospitals and resources data from JSON files.

    :param hospitals_file: Path to the hospitals JSON file.
    :param resources_file: Path to the resources JSON file.
    :return: Tuple of hospitals and resources dictionaries.
    """
    # Load hospital data
    with open(hospitals_file, 'r') as f:
        hospitals = json.load(f)

    # Load resource data
    with open(resources_file, 'r') as f:
        resources = json.load(f)

    return hospitals, resources
