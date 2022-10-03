import justpy as jp
import inspect
from webapp.about import About
from webapp.home import Home
from webapp.dictionary import Dictionary
from webapp import page

imports = list(globals().values())

# issubclass() function expects the first argument to be a class not a string. Therefore we need to inspect the
# obj before diving the if condtion. So this is why we created two-layer if checks
for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)


jp.Route(Home.path, Home.serve)
jp.Route(About.path, About.serve)
jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)