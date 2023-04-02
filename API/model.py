import sqlalchemy as sa
from config import db


class Rambouillet(db.Model):
    temperature = sa.Column(sa.String)
    pressure = sa.Column(sa.String)
    humidity = sa.Column(sa.String)
    IAQ = sa.Column(sa.String)
    iCO2 = sa.Column(sa.String)
    id = sa.Column(sa.Integer, primary_key=True)
