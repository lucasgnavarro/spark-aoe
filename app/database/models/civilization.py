import base
from sqlalchemy import Column, Integer, String, Float

class Civilization(base.Base):
    __tablename__ = 'civilizations'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    army_type = Column(String, nullable=False)
    unique_unit = Column(String, nullable=False)
    unique_tech = Column(String, nullable=False)
    team_bonus = Column(String, nullable=False)
    civilization_bonus = Column(String, nullable=False)

    def __init__(self, name, expansion, army_type, unique_unit, unique_tech, team_bonus, civilization_bonus):
        self.name = name
        self.expansion = expansion
        self.army_type = army_type
        self.unique_unit = unique_unit
        self.unique_tech = unique_tech
        self.team_bonus = team_bonus
        self.civilization_bonus = civilization_bonus

    def __repr__(self):
        return f'civilizations({self.id}, {self.name})'

    def __str__(self):
        return self.name