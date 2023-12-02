from fuckoff import FuckOff
from cross_platform_shutdown import shutdown

with FuckOff() as fuckoff:
    fuckoff.wait()
    shutdown()
