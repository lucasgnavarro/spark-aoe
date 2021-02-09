from db import db
import json
from collections import OrderedDict

class StructureModel(db.Model):
    __tablename__ = 'structures'

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    expansion = db.Column(db.String(80), nullable=False)

    def __init__(self, name, expansion):
        self.name = name
        self.expansion = expansion

    def __repr__(self):
        return "<Structure: {}>".format(self.name)

    def json(self):
        structure = [('id', self._id),
                     ('name', self.name)]
        return OrderedDict([(k, v) for k, v in structure if v])