import folium 
import io
import os
from PIL import Image
import base64

class ImageGenerator:
    def __init__ ( self ):
        self.bounds = [-8.8850, -63.9077]
        self.basemap = 'https://geoportal.sedam.ro.gov.br/mosaicos/sentinel/072024/{z}/{x}/{y}.png'

    def generate ( self, coords ):
        m = folium.Map(
            location=self.bounds,
            control_scale=False,
            zoom_control=False,
            attribution_control=False,
            zoom_start=7,
            tiles=self.basemap,
            attr='<a/>Protege</a>'
        )

        geometry = folium.Polygon(locations=coords, color="#3388ff", weight=3, fillColor="#3388ff", fillOpacity=0.2).add_to(m)

        m.fit_bounds(geometry.get_bounds())
    
        img_data = m._to_png(5)
        img = Image.open(io.BytesIO(img_data))
        img.save('image.png', format='png')

        # img_base64 = base64.b64encode(img_data)
        
        # print(img_base64)
        
if __name__ == "__main__":
    image_generator = ImageGenerator()
    image_generator.generate([[
        [-8.8404, -63.8480],
        [-8.8404, -63.8500],
        [-8.8304, -63.8480],
        [-8.8304, -63.8500],
    ]])

