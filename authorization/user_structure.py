from flask_restful import fields


user_structure = {
    'name': fields.String,
    'password': fields.String,
    'role': fields.String,
}
