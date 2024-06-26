DEBUG = False


if DEBUG:
    from .settings import *
else:
    from .production import *