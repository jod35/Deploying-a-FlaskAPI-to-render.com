from marshmallow import Schema, fields


class CatSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    age = fields.Integer()
