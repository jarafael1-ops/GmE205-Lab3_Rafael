# GmE205-Lab3_Rafael

# Conceptual Reflection 
What changed in the internal representation of Point? 
From Attributes to Objects, the class point likely stored in x and y as primitive floats.  And refactor as geometry. In this laboratory before self.x = 121.0  after self.geometry in object format.  
What did not change n the external behavior? 
In this laboratory the ShapelyPoint object still types the exact same line of code p=Point ('A", 121.0, 14.6) the result still provides an ID, Lat and Long
Where does spatial computation now live?
Due to the Geometry Engine spatial computation lived directly. The geometry attribute handles the "math logic."

#Conceptual Reflection
Why is SpatialObject considered an abstraction, and what real-world idea does it 
represent in your system? 
This laboratory abstraction was the process of hiding complexity. But the spatialObject was a single GPS coordinate like a boundary line or entire shape.
How does inheritance reduce duplication between classes like Point, Parcel, or Building? 
Inheritance was defined as id, name and tags inside the every class, also manually update every single file.
Why is storing parcel attributes in a dictionary a structural decision rather than a 
behavioral one? 
dictionary structural was decided that the object is a dynamic container but the behavioral was involves logic, algorithms ans actions.
If you add a new method (e.g., distance_to()) in SpatialObject, what happens to all 
subclasses — and why? 
By adding the method the parent class is like adding a new feature to a genetic code. 
How does this hierarchical design make your spatial system more scalable 
compared to defining each class independently?
Hietarchy moves the complexity from quantity of code to quality of the design. It allowed the system to grow jorizontally more types of shapes and vertically more features with a fraction of the maintenace cost.
