from db import db
import json
from collections import OrderedDict

class StructureModel(db.Model):
    __tablename__ = 'structures'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    expansion = db.Column(db.String(80), nullable=False)