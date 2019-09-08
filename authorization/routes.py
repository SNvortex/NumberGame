from flask_restful import Resource, marshal_with, abort
from flask import request, session
from models import GameUser
from .parser import register_parse
from db import db
from .user_structure import user_structure


class RegisterResources(Resource):
    @marshal_with(user_structure)
    def post(self):
        args = register_parse.parse_args()
        name = args['name']
        check_name = GameUser.query.filter_by(name=name).all()
        if check_name:
            abort(401)
        cur_user = GameUser(**args)
        db.session.add(cur_user)
        db.session.commit()
        return cur_user


class LoginResources(Resource):
    def get(self):
        name = request.args.get('name')
        cur_user = GameUser.query.filter_by(name=name).first()
        if request.args.get('password') == cur_user.password:
            session['logged_in'] = True
            session['user_id'] = cur_user.id
            session['role'] = cur_user.role
            return 'OK'
        return 'wrong password'


class LogoutResources(Resource):
    def get(self):
        session['login'] = False
        return 'logged out'
