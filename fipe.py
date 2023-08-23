import requests
#http://deividfortuna.github.io/fipe/

import json
import ast


request = requests.get("http://parallelum.com.br/fipe/api/v2/cars/brands")
todos = json.loads(request.content)
print(todos[1]["name"])
