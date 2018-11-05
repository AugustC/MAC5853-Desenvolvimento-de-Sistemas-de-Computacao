from flask import request, jsonify, abort
from flask_restful import Api, Resource
from . import api
from .models import MURL, MPROHIBITIONTYPE, MSTATUSTYPE

class URLResource(Resource):

    def get(self):
        urlpath = str(request.json.get('urlpath'))
        url = MURL.query.filter_by(urlpath=urlpath).first()
        if url:
            response = jsonify(url.serialize())
            response.status_code = 202
            return response
        else:
            return {'urlpath':'not found'}, 404

    def post(self):
        urlpath = str(request.json.get('urlpath'))
        if urlpath:
            url = MURL(urlpath=urlpath)
            url.save()
            response = jsonify({
                'id': url.id,
                'urlpath': url.urlpath
            })
            response.status_code = 201
            return response

    def delete(self):
        urlpath = str(request.json.get('urlpath'))
        url = MURL.query.filter_by(urlpath=urlpath).first()
        MURL.delete(url)
        response = jsonify({
            'note': 'Delete successful'
        })
        response.status_code = 200
        return response

class ProhibitionTypeResource(Resource):
    def get(self):
        id = str(request.json.get('id'))
        prohibitiontype = MPROHIBITIONTYPE.query.filter_by(id=id).first()
        if prohibitiontype:
            response = jsonify(prohibitiontype.serialize())
            response.status_code = 202
            return response
        else:
            return {'id':'not found'}, 404

    def post(self):
        description = str(request.json.get('description'))
        if description:
            prohibitiontype = MPROHIBITIONTYPE(description=description)
            prohibitiontype.save()
            response = jsonify({
                'id': prohibitiontype.id,
                'description': prohibitiontype.description
            })
            response.status_code = 201
            return response

    def delete(self):
        id = str(request.json.get('id'))
        prohibitiontype = MPROHIBITIONTYPE.query.filter_by(id=id).first()
        MPROHIBITIONTYPE.delete(prohibitiontype)
        response = jsonify({
            'note': 'Delete successful'
        })
        response.status_code = 200
        return response

class StatusTypeResource(Resource):
    def get(self):
        id = str(request.json.get('id'))
        statustype = MSTATUSTYPE.query.filter_by(id=id).first()
        if statustype:
            response = jsonify(statustype.serialize())
            response.status_code = 202
            return response
        else:
            return {'id':'not found'}, 404

    def post(self):
        description = str(request.json.get('description'))
        if description:
            statustype = MSTATUSTYPE(description=description)
            statustype.save()
            response = jsonify({
                'id': statustype.id,
                'description': statustype.description
            })
            response.status_code = 201
            return response

    def delete(self):
        id = str(request.json.get('id'))
        statustype = MSTATUSTYPE.query.filter_by(id=id).first()
        MSTATUSTYPE.delete(statustype)
        response = jsonify({
            'note': 'Delete successful'
        })
        response.status_code = 200
        return response

api.add_resource(URLResource, '/url')
api.add_resource(ProhibitionTypeResource, '/prohibition_type')
api.add_resource(StatusTypeResource, '/status_type')