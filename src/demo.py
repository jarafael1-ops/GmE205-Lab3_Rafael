from spatial import Point

# This will now work!
p = Point("A", 121.0, 14.6)
print(f"ID: {p.id}")
print(f"Coordinates: {p.to_tuple()}")

p1 = Point("A", 121.0, 14.6)
p2 = Point("X", 120.0, 14.0)

dist = p1.distance_to(p2)
print(f"The distance between {p1.id} and {p2.id} is {dist:.4f} degrees.")

from spatial import Point 
p = Point("A", 121.0, 14.6) 
print("BBox:", p.bbox()) 
print("Tuple:", p.to_tuple()) 

# from spatial import Point 
# p = Point("A", 121.0, 14.6) 
# print("BBox:", p.bbox()) 
# print("Tuple:", p.to_tuple()) 

from shapely.geometry import Polygon 
from spatial import Parcel 

# a simple rectangle polygon sample 
geom = Polygon([ 
(0, 0), 
(10, 0), 
(10, 5), 
(0, 5) 
])

# Dictionary for added structure 
attrs = { 
"area": 50.0, 
"zone": "Residential", 
"is_active": True 
} 
parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs) 
print("Parcel BBox:", parcel.bbox()) 
print("Parcel Zone:", parcel.attributes["zone"])


