import folium
from folium.plugins import HeatMap

def create_map(hospitals, allocations, unmet_demand):
    # Create a base map centered around Kathmandu
    map = folium.Map(location=[27.7172, 85.3240], zoom_start=12)

    # Prepare data for the heat map (lat, lon, intensity)
    heat_data = [
        [info['lat'], info['lon'], sum(allocations[h].values())] 
        for h, info in hospitals.items()
    ]

    # Add HeatMap layer
    HeatMap(heat_data, min_opacity=0.4, radius=20, blur=15).add_to(map)

    # Add circle markers with popup info for each hospital
    for h, info in hospitals.items():
        total_resources = sum(allocations[h].values())
        unmet = sum(unmet_demand[h].values())

        popup_content = (
            f"<b>{h}</b><br>"
            f"Location: {info.get('location', 'N/A')}<br>"
            f"Total Resources: {total_resources}<br>"
            f"Unmet Demand: {unmet}<br>"
            f"Doctors Allocated: {allocations[h].get('doctors', 0)} / {hospitals[h]['demand']['doctors']}<br>"
            f"Nurses Allocated: {allocations[h].get('nurses', 0)} / {hospitals[h]['demand']['nurses']}<br>"
            f"Ventilators Allocated: {allocations[h].get('ventilators', 0)} / {hospitals[h]['demand']['ventilators']}<br>"
            f"Monitors Allocated: {allocations[h].get('monitors', 0)} / {hospitals[h]['demand']['monitors']}"
        )
        
        folium.CircleMarker(
            location=[info['lat'], info['lon']],
            radius=7,  # Adjust size as needed
            color='blue',
            fill=True,
            fill_color='blue',
            popup=popup_content,
            tooltip=f"{h}: {total_resources} resources"
        ).add_to(map)

    # Save the map
    map.save('results/index.html')
