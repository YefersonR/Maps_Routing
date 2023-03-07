# https://python-visualization.github.io/folium/quickstart.html
# https://www.youtube.com/watch?v=xl_OFx7BgtA&ab_channel=RenzoCaceresRossi

import folium
from folium.plugins import MiniMap

def draw_solution(initialNode,goalNode,shorterPath):
    mapa = folium.Map(
        location=initialNode,
        zoom_start=16
    )

    folium.Marker(location=initialNode,popup=f"{initialNode}").add_to(mapa)
    folium.Circle(location=initialNode,color="green",radius=10,weight=10,fill_opacity=0.5,tooltip=f"{initialNode}").add_to(mapa)


    folium.Marker(location=goalNode,popup=f"{goalNode}").add_to(mapa)
    folium.Circle(location=goalNode,color="red",radius=10,weight=10,fill_opacity=0.5,tooltip=f"{goalNode}").add_to(mapa)

    folium.PolyLine(shorterPath, tooltip="Coast").add_to(mapa)
    # print(shorterPath)
    minimap = MiniMap()
    mapa.add_child(minimap)
    mapa
    mapa.save("mapa.html")