from shapely.geometry import Point as ShapelyPoint 

class Point: 
    def __init__(self, id, lon, lat, name=None, tag=None): 
        # These validation checks are indented inside __init__
        if not (-180 <= lon <= 180): 
            raise ValueError("Longitude must be between -180 and 180") 
        if not (-90 <= lat <= 90): 
            raise ValueError("Latitude must be between -90 and 90") 
        
        # THESE LINES MUST BE INDENTED TOO:
        self.id = id 
        self.geometry = ShapelyPoint(lon, lat) 
        self.name = name 
        self.tag = tag 

    def to_tuple(self):
        # Indented inside the method
        return (self.geometry.x, self.geometry.y)
    
    def distance_to(self, other): 
        """Calculates the Euclidean distance to another Point object."""
        if not hasattr(other, 'geometry'):
            raise ValueError("The 'other' argument must be a Point object with geometry.")
        
        return self.geometry.distance(other.geometry)

