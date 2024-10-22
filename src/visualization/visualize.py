import folium
from folium.plugins import HeatMap

def create_map(hospitals, allocations):
    # Create a base map centered around Kathmandu
    map = folium.Map(location=[27.7172, 85.3240], zoom_start=12)

    # Prepare data for the heat map (lat, lon, intensity)
    heat_data = [
        [info['lat'], info['lon'], sum(allocations[h].values())] 
        for h, info in hospitals.items()
    ]

    # Add HeatMap layer
    HeatMap(heat_data, min_opacity=0.4, max_val=max([sum(allocations[h].values()) for h in hospitals]), radius=20, blur=15).add_to(map)

    # Add circle markers with popup info for each hospital
    for h, info in hospitals.items():
        total_resources = sum(allocations[h].values())
        
        # Only add markers if resources are allocated
        if total_resources > 0:
            folium.CircleMarker(
                location=[info['lat'], info['lon']],
                radius=7,  # Adjust size as needed
                color='blue',
                fill=True,
                fill_color='blue',
                popup=folium.Popup(
                    f"<b>{h}</b><br>"
                    f"Location: {info.get('location', 'N/A')}<br>"
                    f"Total Resources: {total_resources}<br>"
                    f"Doctors: {allocations[h].get('doctors', 'N/A')}<br>"
                    f"Nurses: {allocations[h].get('nurses', 'N/A')}<br>"
                    f"Ventilators: {allocations[h].get('ventilators', 'N/A')}<br>"
                    f"Monitors: {allocations[h].get('monitors', 'N/A')}",
                    max_width=300
                ),
                tooltip=f"{h}: {total_resources} resources"
            ).add_to(map)

    # Save the map
    map.save('results/hospital_density_map.html')
