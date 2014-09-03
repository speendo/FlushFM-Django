from django import template
from players.lib.MPDProxy import mpd_proxy

register = template.Library()

register.inclusion_tag('no_mpd_alert.html')

def no_mpd_alert():
	
	return