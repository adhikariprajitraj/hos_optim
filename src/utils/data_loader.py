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

    # Add latitude and longitude for hospitals (example values, to be updated as needed)
    hospitals["Bir Hospital"]['lat'] = 27.7047
    hospitals["Bir Hospital"]['lon'] = 85.3097
    hospitals["Kathmandu Valley Hospital"]['lat'] = 27.7056
    hospitals["Kathmandu Valley Hospital"]['lon'] = 85.3127
    hospitals["Civil Service Hospital of Nepal"]['lat'] = 27.7005
    hospitals["Civil Service Hospital of Nepal"]['lon'] = 85.3384
    hospitals["Vayodha Hospital"]['lat'] = 27.6771
    hospitals["Vayodha Hospital"]['lon'] = 85.3016
    hospitals["Grande City Hospital"]['lat'] = 27.7262
    hospitals["Grande City Hospital"]['lon'] = 85.3334
    hospitals["Teaching Hospital"]['lat'] = 27.7390
    hospitals["Teaching Hospital"]['lon'] = 85.3423

    # Adding minimum resource needs for each hospital (example values)
    for hospital in hospitals:
        hospitals[hospital]['min_resources'] = 10  # Arbitrary number, adjust as needed
    
    return hospitals, resources
