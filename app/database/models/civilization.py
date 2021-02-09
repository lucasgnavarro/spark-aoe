from db import db
from flask import request

class CivilizationModel(db.Model):
    __tablename__ = 'civilizations'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=False)
    unique_unit = db.Column(db.String(80), db.ForeignKey('units.name'), nullable=False)
    unique_tech = db.Column(db.String(80), db.ForeignKey('technologies.name'), nullable=False)

    unit = db.relationship('UnitModel', lazy='dynamic', uselist=True)
    technology = db.relationship('TechnologyModel', lazy='dynamic', uselist=True)

    def __init__(self, name,
                 unique_unit, unique_tech):
        self.name = name
        self.unique_unit = unique_unit
        self.unique_tech = unique_tech