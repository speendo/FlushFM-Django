from django.shortcuts import render
from players.lib.MPDProxy import mpd_proxy
import urllib.request
from django.http import HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    print("Index loaded")
    return render(request, 'players/index.html',)

def status(request):
    return render(request, 'players/status.html')

def play(request):
    print("button pressed")
    uri = request.POST['uri']
    if 'play' in request.POST:
        print("Play-button pressed")
        start_replay(get_uri(uri))
    else:
        print("Stop-button pressed")
        stop_repay()
    return render(request, 'players/index.html', {'uri': uri})

def get_uri(uri):
    print(uri)
    if uri.endswith(".m3u"):
                
        file = urllib.request.urlopen(uri)
        for line in file:
            line = line.decode(encoding='utf8')
            print(line)
            if line.startswith('http'):
                word = line.strip()
                print("Word: " + word)
                print("Ok, returning " + word)
                return word
    else:
        return uri
    

def start_replay(uri):
    print("Sending \"" + uri + "\" to the client.")
    print(mpd_proxy.clear())
    print(mpd_proxy.add(uri))
    print(mpd_proxy.play())


def stop_repay():
    mpd_proxy.stop()

def currently_playing(request):
    if 'title' in mpd_proxy.currentsong():
        return HttpResponse(mpd_proxy.currentsong()['title'])
    else:
        return HttpResponse("waiting for song info")