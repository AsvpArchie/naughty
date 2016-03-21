# -*- coding: utf-8 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys

plugin_handle = int(sys.argv[1])
xbmcplugin.setContent(plugin_handle, 'movies')
icon = xbmc.translatePath("special://home/addons/plugin.video.korea-xxx/icon.png")
	
def add_video_item(url, infolabels, img=''):
    #url = 'http://edge2.everyon.tv/etv2/'+url+'/BratuMarian.m3u8'
    # rtmp://edge2.everyon.tv/etv2/phd1003
    #url = 'rtmp://lm7.everyon.tv/ptv7/'+url+' live=1'
    #url = 'http://lm7.everyon.tv/ptv7/'+url+'/BratuMarian.m3u8'
    #url = 'http://edge2.everyon.tv/etv2sb/'+url+'.m3u8'
    if 'rtmp://' in url: url = url + ' live=1' 
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return


add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd927',{ 'title': 'Penthouse'}, icon)
add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd766',{ 'title': 'XXX M19'}, icon)
add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd765',{ 'title': 'Viki Premium'}, icon)
add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd497',{ 'title': 'Playboy'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd968',{ 'title': 'Korea XXX 968'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd991',{ 'title': 'Korea XXX 991'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd992',{ 'title': 'Korea XXX 992'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd993',{ 'title': 'Korea XXX 993'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd59',{ 'title': 'Korea HOTGiRL'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd60',{ 'title': 'Korea Red On'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd61',{ 'title': 'Korea OKADAi'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd62',{ 'title': 'Korea XXX'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd63',{ 'title': 'Korea DeilghtEmpire'}, icon)
add_video_item('rtmp://main2sb.everyon.tv:1935/etv2sb/_definst_/phd64',{ 'title': 'Korea LiVETRiNG'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd499',{ 'title': 'Korea Playboy'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd501',{ 'title': 'Korea Girls TV'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd511',{ 'title': 'Korea South Korea 511'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd769',{ 'title': 'Korea PLAYY'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd770',{ 'title': 'Korea PLAYY HD'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd771',{ 'title': 'Korea THE O'}, icon)
add_video_item('rtmp://edge2.everyon.tv/etv2sb/phd772',{ 'title': 'Korea ButGO'}, icon)
add_video_item('http://edge2.everyon.tv/etv2/phd1003/BratuMarian.m3u8',{ 'title': 'Korea JAV TV'}, icon)
add_video_item('http://edge2.everyon.tv/etv2/phd1005/BratuMarian.m3u8',{ 'title': 'Korea Ask TV'}, icon)
add_video_item('http://edge2.everyon.tv/etv2/phd1006/BratuMarian.m3u8',{ 'title': 'Korea Livething Premium'}, icon)
add_video_item('http://edge2.everyon.tv/etv2/phd1008/BratuMarian.m3u8',{ 'title': 'Korea Paradise'}, icon)
xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)

