from django import template

register = template.Library()

def search(central):
	return str('Mossad', 'MI5')

register.filter('search', search)