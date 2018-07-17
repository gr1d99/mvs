"""Provides methods that simplify model queries"""

from app import DB


class Queryset:
    """
    Queryset class that is extended by all models in the application
    """

    @staticmethod
    def commit():
        DB.session.commit()

    def create(self):
        DB.session.add(self)
        self.commit()

    def delete(self):
        DB.session.delete(self)
        self.commit()
