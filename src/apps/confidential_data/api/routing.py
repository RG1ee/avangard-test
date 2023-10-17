from flask import Blueprint
from flask_restful import Api

from src.apps.confidential_data.api.resources import (
    DataIdResource,
    DataResource,
    MyDataResource,
)


api_data = Blueprint("data", __name__)
api = Api(api_data, prefix="/api/v1/data")

api.add_resource(DataResource, "/", endpoint="data-create")
api.add_resource(DataIdResource, "/<int:data_id>", endpoint="data-id")
api.add_resource(MyDataResource, "/my-data", endpoint="data-user")
