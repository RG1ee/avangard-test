from src.apps.users.services import UserService
from src.apps.confidential_data.services import ConfidentialDataService


def validate_confidential_data(username, data_id):
    """
    Validates and retrieves confidential data for a specific user and data identifier.

    Parameters:
        username (str): The username of the user for whom the data is being validated.
        data_id (int): The identifier of the confidential data record to be validated.

    Returns:
        object: The confidential data record for the specified user and data identifier, or None if not found.
    """
    user = UserService.get_first_by_username(username=username)
    confidential_data = ConfidentialDataService.get_one(id=data_id, user_id=user.id)

    return confidential_data
