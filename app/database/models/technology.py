from db import db
import json
from collections import OrderedDict
from api.models.factory import get_model


from flask import request


class TechnologyModel(db.Model):
    __tablename__ = 'technologies'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    develops_in = db.Column(db.String(80), db.ForeignKey("structures.name"), nullable=False)

    structure = db.relationship('StructureModel', lazy='dynamic', uselist=True)
