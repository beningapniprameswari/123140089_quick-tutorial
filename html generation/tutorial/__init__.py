from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # 1. Definisikan rute (URL)
    config.add_route('home', '/')
    config.add_route('hello', '/howdy') # Rute baru!
    
    # 2. Perintah "ajaib": Pindai file .views untuk @view_config
    config.scan('.views') 
    
    return config.make_wsgi_app()
from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    # --- TAMBAHKAN BARIS INI ---
    config.include('pyramid_chameleon') 
    # ---------------------------
    
    config.add_route('home', '/')
    config.add_route('hello', '/howdy')
    config.scan('.views')
    return config.make_wsgi_app()