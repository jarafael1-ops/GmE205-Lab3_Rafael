@classmethod
def from_dict(cls, d: dict):
    return cls(
        id=d["id"],
        lon=d["lon"],
        lat=d["lat"],
        name=d.get("name"),  # Returns None if "name" is missing
        tag=d.get("tag")     # Returns None if "tag" is missing
    )
       # Output: POI