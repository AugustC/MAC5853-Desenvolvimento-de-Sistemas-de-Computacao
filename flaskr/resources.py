from flask import request, jsonify, abort
from flask_restful import Api, Resource
from . import api
from .models import MURL

class URLResource(Resource):
    def get(self,request):
        urls = MURL.get_all()
        results = []

        for url in urls:
            obj = {
                'id': url.id,
                'urlpath': url.urlpath
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    def post(self):
        urlpath = str(request.data.get('urlpath', ''))
        if urlpath:
            url = MURL(urlpath=urlpath)
            url.save()
            response = jsonify({
                'id': url.id,
                'urlpath': url.urlpath
            })
            response.status_code = 201
            return response



api.add_resource(URLResource, '/url')