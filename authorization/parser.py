from flask_restful import reqparse


register_parse = reqparse.RequestParser()
register_parse.add_argument('name', required=True)
register_parse.add_argument('password', required=True)
register_parse.add_argument('role', required=True)
