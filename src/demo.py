from spatial import Point

# This will now work!
p = Point("A", 121.0, 14.6)
print(f"ID: {p.id}")
print(f"Coordinates: {p.to_tuple()}")

p1 = Point("A", 121.0, 14.6)
p2 = Point("X", 120.0, 14.0)

dist = p1.distance_to(p2)
print(f"The distance between {p1.id} and {p2.id} is {dist:.4f} degrees.")




