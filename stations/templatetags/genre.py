from django import template

register = template.Library()

tagStart = ('<span {:s}class="label genre{:s}" style="background-color:#{:s};">'
	'<span class="glyphicon glyphicon-music"></span>'
	'<span class="genre_name"> {:s} </span>'
)
tagEnd = '</span>'
tagRemove = '<span class="glyphicon glyphicon-remove remove"></span>'

jsStart = '<script id="{:s}_template" type="text/x-handlebars-template">'
jsEnd = '</script>'

@register.simple_tag
def genre_def_js():
	return (jsStart + genre_def("{{{{genre}}}}", "{{{{color}}}}", "{{{{css_id}}}}", "{{{{css_class}}}}") + jsEnd).format("genre_def")

@register.simple_tag
def genre_add_js():
	return (jsStart + genre_add("{{{{genre}}}}", "{{{{color}}}}", "{{{{css_id}}}}", "{{{{css_class}}}}") + jsEnd).format("genre_add")

@register.simple_tag
def genre_def(name, color, css_id="", css_class=""):
	if css_id != "":
		css_id = 'id="' + css_id + '" '

	if css_class != "":
		css_class = ' ' + css_class

	return (tagStart + tagEnd).format(css_id, css_class, color, name)

@register.simple_tag
def genre_add(name, color, css_id="", css_class=""):
	if css_id != "":
		css_id = 'id="' + css_id + '" '

	if css_class != "":
		css_class = ' ' + css_class

	return (tagStart + tagRemove + tagEnd).format(css_id, css_class, color, name)

@register.simple_tag
def genre(genre_obj, css_id="", css_class=""):
	return genre_def(genre_obj.name, genre_obj.color, css_id, css_class)