"""Role database model"""

from app import DB
from app.db.models.query import Queryset


class Role(DB.Model, Queryset):
    """roles table model"""

    __tablename__ = 'roles'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    description = DB.Column(DB.Text)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id
