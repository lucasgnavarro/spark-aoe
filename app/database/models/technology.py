mport base
from sqlalchemy import Column, Integer, String, Float

class Technology(base.Base):
    __tablename__ = 'technologies'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    age = Column(String, nullable=False)
    develops_in = Column(String, nullable=False)
    cost_food = Column(Float)
    cost_gold = Column(Float)
    build_time = Column(Float)
    applies_to = Column(String, nullable=False)
   
    def __init__(self, name, description, expansion, age, develops_in, cost_food, cost_gold, build_time, applies_to):
        self.name = name
        self.description = description
        self.expansion = expansion
        self.age = age
        self.develops_in = develops_in
        self.cost_food = cost_food
        self.cost_gold = cost_gold
        self.build_time = build_time
        self.applies_to = applies_to

    def __repr__(self):
        return f'Technologies({self.id}, {self.name})'

    def __str__(self):
        return self.name