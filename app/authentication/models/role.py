"""Role database model"""

from app import DB
from app.db.models.query import Queryset


class Role(DB.Model, Queryset):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String, nullable=False)

    def __init__(self, name):
        self.name = name
