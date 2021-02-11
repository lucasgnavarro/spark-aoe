from db import db
from flask import request

class CivilizationModel(db.Model):
    __tablename__ = 'civilizations'

    _id = db.Column(db.Integer, primary_key=True)
    name = Column(String, nullable=False)
    expansion = Column(String, nullable=False)
    army_type = Column(String, nullable=False)
    unique_unit = Column(String, nullable=False)
    unique_tech = Column(String, nullable=False)
    team_bonus = Column(String, nullable=False)
    civilization_bonus = Column(String, nullable=False)

    unit = db.relationship('UnitModel', lazy='dynamic', uselist=True)
    technology = db.relationship('TechnologyModel', lazy='dynamic', uselist=True)

    def __init__(self, name, expansion, army_type, unique_unit, unique_tech, team_bonus, civilization_bonus):
        self.name = name
        self.expansion = expansion
        self.army_type = army_type
        self.unique_unit = unique_unit
        self.unique_tech = unique_tech
        self.team_bonus = team_bonus
        self.civilization_bonus = civilization_bonus