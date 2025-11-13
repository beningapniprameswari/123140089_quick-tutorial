# package
from pyramid.config import Configurator
from pyramid.response import Response

# View function kita masih sama
def hello_world(request):
    return Response('<body><h1>Hello World!</h1></body>')

# --- INI BAGIAN BARU ---
# Ini adalah "app factory" yang dipanggil oleh pserve
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    return config.make_wsgi_app()