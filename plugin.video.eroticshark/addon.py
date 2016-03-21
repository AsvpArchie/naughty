import os
import sys
import urllib
import urllib2
import re
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin
import time

thisAddon = xbmcaddon.Addon(id='plugin.video.eroticshark')
thisAddonDir = xbmc.translatePath(thisAddon.getAddonInfo('path'))
sys.path.append(os.path.join(thisAddonDir, 'resources', 'lib'))

def open_search_panel():
               
    search_text = ''
    keyb = xbmc.Keyboard('','Type your search text.')
    keyb.doModal()
 
    if (keyb.isConfirmed()):
        search_text = keyb.getText()

    return search_text

def find_read_error(top_url):
    try:
        req = urllib2.Request(top_url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        url_content = urllib2.urlopen(req).read()

    except:
        url_content = 'HIBA'
        addon = xbmcaddon.Addon()
        addonname = addon.getAddonInfo('name')
        line1 = 'Sorry! Cannot connect to Database server!'
        line2 = 'Please try again later!'
        xbmcgui.Dialog().ok(addonname, line1, line2)
        return url_content
    return url_content

def just_beta(file_host):
    addon = xbmcaddon.Addon()
    addonname = addon.getAddonInfo('name')
    line1 = 'Sorry! Cannot connect to Database server!'
    line2 = 'Please try again later!'
    xbmcgui.Dialog().ok(addonname, line1, line2)  
    return

def just_removed(file_host):
    addon = xbmcaddon.Addon()
    addonname = addon.getAddonInfo('name')
    line1 = 'Sorry! Cannot connect to Database server!'
    line2 = 'Please try again later!'
    xbmcgui.Dialog().ok(addonname, line1, line2)  
    return

def no_video(file_host):
    addon = xbmcaddon.Addon()
    addonname = addon.getAddonInfo('name')
    line1 = 'Sorry! Could not find any video!'
    line2 = 'Please try to search anything else!'
    xbmcgui.Dialog().ok(addonname, line1, line2, file_host)  
    return

def build_supported_sites_directorys():
    url = build_url({'mode': 'beeg', 'foldername': 'Beeg'})
    li = xbmcgui.ListItem('Beeg.com', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'tube8', 'foldername': 'Tube8'})
    li = xbmcgui.ListItem('Tube8.com', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'xvideos', 'foldername': 'Xvideos'})
    li = xbmcgui.ListItem('XVideos.com', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)

    url = build_url({'mode': 'freepornsite', 'foldername': 'Freepornsite'})
    li = xbmcgui.ListItem('Freepornsite.me', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

    return

def build_beeg_main_directorys():

    url = build_url({'mode': 'beeg_tags', 'foldername': 'Tags'})
    li = xbmcgui.ListItem('Categories', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

    return

def build_beeg_tag_directorys():
    top_url = 'http://beeg.com'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    category_links = re.compile('(/tag/.+)" ?>(.+)</a>').findall(url_content)

    for cic in range(0, 8):
        url = build_url({'mode': 'beeg_tfolder', 'foldername': category_links[cic][0], 'pagenum': '0'})
        li = xbmcgui.ListItem(category_links[cic][1], iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle) 

    return

def build_beeg_video_links(foldername, pagenum):
    pagenum = int(pagenum)
    pagenum += 1
    pagenum = str(pagenum)
    top_url = 'http://beeg.com' + foldername + '/page-' + pagenum

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    porn_links = re.compile('tumb.+?=\[(.+)\]').findall(url_content)
    porn_links[1] = porn_links[1] + ','
    porn_numbers = re.compile('([0-9]+)').findall(porn_links[0])
    porn_names = re.compile('\'(.+?)\',').findall(porn_links[1])

    if len(porn_names) >= 15:
        max_len = 15
    else:
        max_len = len(porn_names)

    for cic in range(0, max_len):
        url = build_url({'mode': 'beeg_vfolder', 'foldername': porn_numbers[cic], 'title': porn_names[cic]})
        li = xbmcgui.ListItem(porn_names[cic], iconImage='http://img.beeg.com/236x177/' + porn_numbers[cic] + '.jpg')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle) 

    return

def find_beeg_videourl(foldername, foldertitle):
    top_url = 'http://beeg.com/' + foldername
            
    url_sock = urllib.urlopen(top_url)
    url_content = url_sock.read()
    url_sock.close()

    direct_url = re.compile('file\':.?\'(.+mp4)').findall(url_content)

            
    if direct_url:
        videoitem = xbmcgui.ListItem(label=foldertitle, thumbnailImage='http://img.beeg.com/236x177/' + foldername + '.jpg')
        videoitem.setInfo(type='Video', infoLabels={'Title': foldertitle})
        xbmc.Player().play(direct_url[0], videoitem)
    else:
        just_removed('Video')
    return

def build_tube8_main_directorys():

    url = build_url({'mode': 'tube8_categories', 'foldername': 'Categories'})
    li = xbmcgui.ListItem('Categories', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

    return

def build_tube8_category_directorys():
    top_url = 'http://www.tube8.com'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    category_links = re.compile('(/cat/.+)">([a-zA-Z]+)').findall(url_content)

    for cic in range(0, 8):
        url = build_url({'mode': 'tube8_cfolder', 'foldername': category_links[cic][0], 'pagenum': '0'})
        li = xbmcgui.ListItem(category_links[cic][1], iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle) 

    return

def build_tube8_video_links(foldername, pagenum):
    pagenum = int(pagenum)
    pagenum += 1
    pagenum = str(pagenum)
    top_url = 'http://www.tube8.com' + foldername + 'page/' + pagenum + '/'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    porn_links = re.compile('"sh2">(.+)<[^w]+(.+/)"').findall(url_content)
    porn_images = re.compile('src="(.+jpg)"').findall(url_content)
    next_page = re.compile('/(page/[0-9]{1,3})/.+id').findall(url_content)

    if len(porn_links) >= 15:
        max_len = 15
    else:
        max_len = len(porn_links)

    for cic in range(0, max_len):
        url = build_url({'mode': 'tube8_vfolder', 'foldername': porn_links[cic][1], 'title': porn_links[cic][0], 'folderimage': porn_images[cic]})
        li = xbmcgui.ListItem(porn_links[cic][0], iconImage=porn_images[cic])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

    return

def find_tube8_videourl(foldername, foldertitle, folderimage):
    top_url = 'http://' + foldername
            
    url_sock = urllib.urlopen(top_url)
    url_content = url_sock.read()
    url_sock.close()

    direct_url = re.compile('default_video_url[^h]+(.+)\'').findall(url_content)

            
    if direct_url:
        videoitem = xbmcgui.ListItem(label=foldertitle, thumbnailImage=folderimage)
        videoitem.setInfo(type='Video', infoLabels={'Title': foldertitle})
        xbmc.Player().play(direct_url[0], videoitem)
    else:
        just_removed('Video')
    return

def build_xvideos_main_directorys():

    url = build_url({'mode': 'xvideos_categories', 'foldername': 'Categories'})
    li = xbmcgui.ListItem('Categories', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

    return

def build_xvideos_category_directorys():
    top_url = 'http://www.xvideos.com'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    category_links = re.compile('href="/c/([^"]+)">([a-zA-Z ]+)').findall(url_content)
   
    for cic in range(1, 9):
        url = build_url({'mode': 'xvideos_cfolder', 'foldername': category_links[cic][0], 'pagenum': '0'})
        li = xbmcgui.ListItem(category_links[cic][1].lstrip(), iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle) 

    return

def build_xvideos_video_links(foldername, pagenum):
    top_url = 'http://www.xvideos.com/c/' + pagenum + '/' + foldername

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    porn_links = re.compile('(/video[0-9]+[^"]+)"[^"]+"([^"]+)').findall(url_content)

    if len(porn_links) >= 30:
        max_len = 30
    else:
        max_len = len(porn_links)

    for cic in range(0, max_len, 2):
        url = build_url({'mode': 'xvideos_vfolder', 'foldername': porn_links[cic][0], 'title': porn_links[cic+1][1], 'folderimage': porn_links[cic][1]})
        li = xbmcgui.ListItem(porn_links[cic+1][1], iconImage=porn_links[cic][1])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

    return

def find_xvideos_videourl(foldername, foldertitle, folderimage):
    top_url = 'http://www.xvideos.com' + foldername
            
    url_sock = urllib.urlopen(top_url)
    url_content = url_sock.read()
    url_sock.close()

    find_url = re.compile('flv_url=([^&]+)&amp').findall(url_content)
    direct_url = urllib.unquote(find_url[0]).decode('utf8')
       
    if direct_url:
        videoitem = xbmcgui.ListItem(label=foldertitle, thumbnailImage=folderimage)
        videoitem.setInfo(type='Video', infoLabels={'Title': foldertitle})
        xbmc.Player().play(direct_url, videoitem)
    else:
        just_removed('Video')
    return

def build_freepornsite_main_directorys():

    url = build_url({'mode': 'freepornsite_categories', 'foldername': 'Categories'})
    li = xbmcgui.ListItem('Categories', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                listitem=li, isFolder=True)
    
    xbmcplugin.endOfDirectory(addon_handle)

    return

def build_freepornsite_category_directorys():
    top_url = 'http://www.freepornsite.me/categories/'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    category_links = re.compile('me(/categories/[^/]+/)"[^"]+"([^"]+)').findall(url_content)

    for cic in range(0, 8):
        url = build_url({'mode': 'freepornsite_cfolder', 'foldername': category_links[cic][0], 'pagenum': '0'})
        li = xbmcgui.ListItem(category_links[cic][1], iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle) 

    return

def build_freepornsite_video_links(foldername, pagenum):
    pagenum = int(pagenum)
    pagenum += 1
    pagenum = str(pagenum)
    top_url = 'http://www.freepornsite.me' + foldername + pagenum + '/'

    url_content = find_read_error(top_url)
    if url_content == 'HIBA':
        return

    porn_links = re.compile('f="(/video/[^"]+)"[^"]+"([^"]+)[^/]+//([^"]+)').findall(url_content)

    if len(porn_links) >= 15:
        max_len = 15
    else:
        max_len = len(porn_links)

    for cic in range(0, max_len):
        url = build_url({'mode': 'freepornsite_vfolder', 'foldername': porn_links[cic][0], 'title': porn_links[cic][1], 'folderimage': 'http://' + porn_links[cic][2]})
        li = xbmcgui.ListItem(porn_links[cic][1], iconImage='http://' + porn_links[cic][2])
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                    listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

    return

def find_freepornsite_videourl(foldername, foldertitle, folderimage):
    top_url = 'http://www.freepornsite.me' + foldername
            
    url_sock = urllib.urlopen(top_url)
    url_content = url_sock.read()
    url_sock.close()

    direct_url = re.compile('videoFile="([^"]+)').findall(url_content)
       
    if direct_url:
        videoitem = xbmcgui.ListItem(label=foldertitle, thumbnailImage=folderimage)
        videoitem.setInfo(type='Video', infoLabels={'Title': foldertitle})
        xbmc.Player().play(direct_url[0], videoitem)
    else:
        just_removed('Video')
    return

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:

    build_supported_sites_directorys()

elif mode[0] == 'beeg':

    build_beeg_main_directorys()

elif mode[0] == 'tube8':

    build_tube8_main_directorys()

elif mode[0] == 'xvideos':

    build_xvideos_main_directorys()

elif mode[0] == 'freepornsite':

    build_freepornsite_main_directorys()

elif mode[0] == 'beeg_tags':

    build_beeg_tag_directorys()

elif mode[0] == 'tube8_categories':

    build_tube8_category_directorys()

elif mode[0] == 'xvideos_categories':

    build_xvideos_category_directorys()

elif mode[0] == 'freepornsite_categories':

    build_freepornsite_category_directorys()

elif mode[0] == 'beeg_tfolder':

    build_beeg_video_links(args['foldername'][0], args['pagenum'][0])

elif mode[0] == 'tube8_cfolder':

    build_tube8_video_links(args['foldername'][0], args['pagenum'][0])

elif mode[0] == 'xvideos_cfolder':

    build_xvideos_video_links(args['foldername'][0], args['pagenum'][0])

elif mode[0] == 'freepornsite_cfolder':

    build_freepornsite_video_links(args['foldername'][0], args['pagenum'][0])

elif mode[0] == 'freepornsite_vfolder':

    find_freepornsite_videourl(args['foldername'][0], args['title'][0], args['folderimage'][0])

elif mode[0] == 'beeg_vfolder':

    find_beeg_videourl(args['foldername'][0], args['title'][0])

elif mode[0] == 'tube8_vfolder':

    find_tube8_videourl(args['foldername'][0], args['title'][0], args['folderimage'][0])

elif mode[0] == 'xvideos_vfolder':

    find_xvideos_videourl(args['foldername'][0], args['title'][0], args['folderimage'][0])

else:

    just_beta(mode[0])
