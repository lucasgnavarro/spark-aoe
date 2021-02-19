import base
from sqlalchemy import Column, Integer, String, Float

class Unit(base.Base):
    __tablename__ = 'units'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    age = Column(String, nullable=False)
    created_in = Column(String, nullable=False)
    cost_wood = Column(Float)
    cost_gold = Column(Float)
    build_time = Column(Integer)
    reload_time = Column(Float)
    attack_delay = Column(Float)
    movement_rate = Column(Integer)
    line_of_sight = Column(Integer)
    hit_points = Column(Integer)
    rangevalue = Column(Integer)
    attack = Column(Integer)
    armor = Column(String, nullable=False)
    accuracy = Column(String, nullable=False)

   
    def __init__(self, name, description, expansion, age, created_in, cost_wood, cost_gold, build_time, attack_delay, movement_rate, line_of_sight, hit_points, rangevalue, attack, armor, accuracy):
    self.name = name
    self.description = description
    self.expansion = expansion
    self.age = age
    self.created_in = created_in
    self.cost_wood = cost_wood
    self.cost_gold = cost_gold
    self.build_time = build_time
    self.reload_time = reload_time
    self.attack_delay = attack_delay
    self.movement_rate = movement_rate
    self.line_of_sight = line_of_sight
    self.hit_points = hit_points
    self.rangevalue = rangevalue
    self.attack = attack
    self.armor = armor
    self.accuracy = accuracy


    def __repr__(self):
        return f'units({self.id}, {self.name})'

    def __str__(self):
        return self.name