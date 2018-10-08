from app import DB
from app.db.models.query import Queryset


class Blacklist(DB.Model, Queryset):
    __tablename__ = 'blacklists'

    id = DB.Column(DB.Integer, primary_key=True)
    jti = DB.Column(DB.String(200), nullable=False)

    def __init__(self, jti):
        self.jti = jti
