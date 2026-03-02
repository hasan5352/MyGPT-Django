from django.urls import path

def route_with_slash(route: str, view):
	""" :param route: should not have a trailing / at the end. function already adds a /.
	"""
	if route == '': return [path('', view)]
	return [path(route, view), path(route + '/', view)]