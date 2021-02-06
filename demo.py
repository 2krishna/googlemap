from geopy.geocoders import Nominatim
geolocator=Nominatim()
import pandas as pd
import io



data = """Name,Address
EU,"Rue de la Loi/Wetstraat 175, Brussel, Belgium"
Apple,"1 Apple Park Way, Cupertino, CA"
Google,"1600 Amphitheatre Parkway Mountain View, CA 94043"
UN,"760 United Nations Plaza; Manhattan, New York City"
 """

data1="""Name,Address
up,noida sector 14,
delhi,delhi patelnagr,
gurgaon,huda ciy center,
vihar,bada bajar vihar,
gonda,paraspur,
medanipur,east medanipur,
lucknow,ambedkar road,
gautambudh nagar,noida sector 12/22,
"""

# Here we need csc file data
#  
df = pd.read_csv(io.StringIO(data1))

df["loc"] = df["Address"].apply(geolocator.geocode)
df["point"]= df["loc"].apply(lambda loc: tuple(loc.point) if loc else None)
print(df["point"])
df[['lat', 'lon', 'altitude']] = pd.DataFrame(df['point'].to_list(), index=df.index)

# Using Folium to show images in google map

import folium
from folium.plugins import MarkerCluster
m = folium.Map(location=df[["lat", "lon"]].mean().to_list(), zoom_start=2)
for i,r in df.iterrows():
    location = (r["lat"], r["lon"])
    folium.Marker(location=location,
                      popup = r['Name'],
                      tooltip=r['Name'])\
    .add_to(marker_cluster)

m.save('index.html')