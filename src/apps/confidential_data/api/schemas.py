from marshmallow import fields

from src.settings import ma
from src.apps.confidential_data.models import ConfidentialData


class DataSchema(ma.Schema):
    name = fields.Str(required=True)
    data = fields.Str(required=True)

    class Meta:
        model = ConfidentialData
        fields = ("id", "name", "data")
