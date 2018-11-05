from flask import request, jsonify, abort
from flask_restful import Api, Resource
from . import api
from .models import MURL

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




api.add_resource(URLResource, '/url')