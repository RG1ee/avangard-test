from marshmallow import ValidationError


def validate_data(schema, data):
    schema = schema()
    errors = schema.validate(data)

    if errors:
        raise ValidationError({"Errors": errors})
