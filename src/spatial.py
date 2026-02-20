from shapely.geometry import Point as ShapelyPoint 

class SpatialObject: 
    """Base class for anything that exists in space.""" 
    def __init__(self, geometry): 
        self.geometry = geometry 
        
    def bbox(self): 
        """Return bounding box as (minx, miny, maxx, maxy).""" 
        return self.geometry.bounds 

class Point(SpatialObject): # <--- Inherit from SpatialObject
    def __init__(self, id, lon, lat, name=None, tag=None): 
        # 1. Validation Logic
        if not (-180 <= lon <= 180): 
            raise ValueError("Longitude must be between -180 and 180") 
        if not (-90 <= lat <= 90): 
            raise ValueError("Latitude must be between -90 and 90") 
        
        # 2. Create the shapely geometry
        geometry = ShapelyPoint(lon, lat) 
        
        # 3. Initialize the Parent class (SpatialObject)
        super().__init__(geometry) 

        # 4. Assign local attributes
        self.id = id 
        self.name = name 
        self.tag = tag 

    def to_tuple(self): 
        return (self.geometry.x, self.geometry.y)

    def distance_to(self, other): 
        return self.geometry.distance(other.geometry)
    
    
from spatial import SpatialObject

class Parcel(SpatialObject): 
    """ 
    Parcel = spatial object + structured attributes. 
    """ 
    def __init__(self, parcel_id, geometry, attributes: dict): 
        # These must be indented inside the __init__ method
        super().__init__(geometry) 
        self.parcel_id = parcel_id 
        self.attributes = attributes if attributes is not None else {}

from shapely.geometry import Point as ShapelyPoint

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry
    
    def bbox(self):
        return self.geometry.bounds

class Point(SpatialObject):
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180): raise ValueError("Invalid Longitude")
        if not (-90 <= lat <= 90): raise ValueError("Invalid Latitude")
        
        super().__init__(ShapelyPoint(lon, lat))
        self.id = id
        self.name = name
        self.tag = tag

    @classmethod 
    def from_dict(cls, d: dict):
        # Your logic here...
        return cls(d["id"], d["lon"], d["lat"], d.get("name"), d.get("tag"))

    def to_tuple(self):
        return (self.geometry.x, self.geometry.y)
    
    