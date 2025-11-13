from pyramid.response import Response
from pyramid.view import view_config

# @view_config menghubungkan 'route_name' dari __init__.py
# ke fungsi ini.
@view_config(route_name='home')
def home(request):
    return Response('<body>Visit <a href="/howdy">hello</a></body>')

# View ini terhubung ke rute 'hello' (URL '/howdy')
@view_config(route_name='hello')
def hello(request):
    return Response('<body>Go back <a href="/">home</a></body>')