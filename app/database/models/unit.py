from db import db
import json
from collections import OrderedDict
from flask import request

class UnitModel(db.Model):
    __tablename__ = 'units'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    age = db.Column(db.String(80), nullable=False)
    created_in = db.Column(db.String(80), db.ForeignKey("structures.name"))

    structure = db.relationship('StructureModel', lazy='dynamic', uselist=True)

    def __init__(self, name, description, expansion, age):
        self.name = name
        self.description = description
        self.age = age
        self.expansion = expansion

    def __repr__(self):
        return "<Unit: {}>".format(self.name)