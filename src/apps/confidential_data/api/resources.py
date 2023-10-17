from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError

from src.apps.confidential_data.services import ConfidentialDataService
from src.apps.confidential_data.api.schemas import DataSchema
from src.apps.users.services import UserService
from src.apps.confidential_data.api.utils import validate_confidential_data
from src.apps.base.validations import validate_data


class DataResource(Resource):
    @jwt_required()
    def post(self):
        """
        Creates a new confidential data record.

        Expects input data in JSON format. Validates input data using DataSchema.
        If the data passes validation, it creates a new confidential data record and returns the created record in JSON format.

        Returns:
            JSON object with the created confidential data record.

        HTTP Status Codes:
            - 200 OK: Successful creation of the record.
            - 400 Bad Request: Input data validation error.
        """
        data = request.get_json()
        try:
            validate_data(DataSchema, data)
        except ValidationError as e:
            return e.messages_dict, 400

        current_user = UserService.get_first_by_username(username=get_jwt_identity())
        ConfidentialDataService.insert_data(
            name=data["name"], data=data["data"], user_id=current_user.id
        )

        return DataSchema().load(data)

    @jwt_required()
    def get(self):
        """
        Retrieves a list of confidential data records.

        Supports pagination using the `page` and `per_page` parameters in the request.

        Returns:
            JSON object with a list of confidential data records.

        HTTP Status Code:
            - 200 OK: Successful retrieval of the list.
        """
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=10, type=int)
        start_index = (page - 1) * per_page
        end_index = start_index + per_page

        schema = DataSchema()
        data = ConfidentialDataService.get_all()
        return schema.dump(data, many=True)[start_index:end_index]


class DataIdResource(Resource):
    @jwt_required()
    def get(self, data_id: int):
        """
        Retrieves information about a confidential data record by the specified identifier.

        Parameters:
            data_id (int): Identifier of the confidential data record.

        Returns:
            JSON object with information about the confidential data record.

        HTTP Status Codes:
            - 200 OK: Successful retrieval of the record.
            - 404 Not Found: Record with the specified identifier not found.
        """
        schema = DataSchema()
        data = ConfidentialDataService.get_one(id=data_id)
        if data is None:
            return {"Message": f"There is no data for such an {data_id} id"}, 404

        return schema.dump(data)

    @jwt_required()
    def delete(self, data_id: int):
        """
        Deletes a confidential data record by the specified identifier.

        Parameters:
            data_id (int): Identifier of the confidential data record.

        Returns:
            JSON object with a message about successful deletion of the record.

        HTTP Status Codes:
            - 200 OK: Successful record deletion.
            - 404 Not Found: Record with the specified identifier not found.
        """
        confidential_data = validate_confidential_data(get_jwt_identity(), data_id)
        if confidential_data is None:
            return {"Message": f"There is no data for such an {data_id} id"}, 404

        ConfidentialDataService.delete_one(confidential_data)
        return {"Message": "Successful deletion"}

    @jwt_required()
    def put(self, data_id: int):
        """
        Updates a confidential data record by the specified identifier.

        Parameters:
            data_id (int): Identifier of the confidential data record.

        Expects input data in JSON format. Validates input data using DataSchema.
        If the data passes validation, it updates the specified confidential data record.

        Returns:
            JSON object with a message about successful update of the record.

        HTTP Status Codes:
            - 200 OK: Successful record update.
            - 400 Bad Request: Input data validation error.
            - 404 Not Found: Record with the specified identifier not found.
        """
        data = request.get_json()
        try:
            validate_data(DataSchema, data)
        except ValidationError as e:
            return e.messages_dict, 400

        confidential_data = validate_confidential_data(get_jwt_identity(), data_id)
        if confidential_data is None:
            return {"Message": f"There is no data for such an {data_id} id"}, 404

        ConfidentialDataService.change_data(
            confidential_data, data["name"], data["data"]
        )

        return {"Message": f"Successful data update number {data_id}"}
