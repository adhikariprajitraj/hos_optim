from utils.data_loader import load_data
from models.allocation_model import optimize_allocation
from visualization.visualize import create_map

def main():
    # Load the hospitals and available resources data from JSON files
    hospitals, resources = load_data('data/hospitals.json', 'data/resources.json')
    
    # Run the optimization model to allocate resources based on demand
    allocations, unmet_demand = optimize_allocation(hospitals, resources)
    
    # Generate a map visualizing the resource allocations and unmet demand
    create_map(hospitals, allocations, unmet_demand)

if __name__ == "__main__":
    main()
