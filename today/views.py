from django.shortcuts import render, HttpResponse
import os

albums = {'lyh':'罗永浩干货日记', 'wj':'硅谷来信', 'xy':'熊逸书院', 'yss':'西方艺术史'}

def index(request):
    root_dir = '/Users/gniu/Temp.localized/get'
    album_list = list()

    album_dirs = os.listdir(root_dir)

    for d in album_dirs:
        dir = os.path.join(root_dir, d)
        if os.path.isdir(dir):
            album_list.append(albums[d])

    return render(request, 'today/index.html', {'albums':album_list})


def album(request):
    pass