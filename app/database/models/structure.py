import base
from sqlalchemy import Column, Integer, String, Float

class Structure(base.Base):
    __tablename__ = 'structures'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    age = Column(String, nullable=False)
    cost_wood = Column(Float)
    build_time = Column(Integer)
    hit_points = Column(Integer)
    line_of_sight = Column(Integer)
    armor = Column(String, nullable=False)
    special = Column(String, nullable=False)

   
    def __init__(self, name, expansion, age, cost_wood, build_time, hit_points, line_of_sight, armor, special):
        self.name = name
        self.expansion = expansion
        self.age = age
        self.cost_wood = cost_fwod
        self.build_time = build_time
        self.hit_points = hit_points
        self.line_of_sight = line_of_sight
        self.armor = armor
        self.special = special


    def __repr__(self):
        return f'structures({self.id}, {self.name})'

    def __str__(self):
        return self.name