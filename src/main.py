from utils.data_loader import load_data
from models.allocation_model import optimize_allocation
from visualization.visualize import create_map

def main():
    hospitals, resources = load_data('data/hospitals.json', 'data/resources.json')
    allocations = optimize_allocation(hospitals, resources)
    create_map(hospitals, allocations)

if __name__ == "__main__":
    main()
