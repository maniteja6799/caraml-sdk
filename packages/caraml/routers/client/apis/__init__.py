# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.ensembler_api import EnsemblerApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from routers.client.api.ensembler_api import EnsemblerApi
from routers.client.api.ensembling_job_api import EnsemblingJobApi
from routers.client.api.project_api import ProjectApi
from routers.client.api.router_api import RouterApi
