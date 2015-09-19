import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'rtmp://streamer.a1.net:1935/rtmplive/redundant/channels/Sporttime/SporttimeTV/mp4:channel2_800'
li = xbmcgui.ListItem('rtmp!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://lihattv.toh.info/jhos/beib3.m3u8'
li = xbmcgui.ListItem('http!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'plugin://program.plexus/?mode=1&url=acestream://dc5310a7e47fcd52cf1d9d7c4db089d72cf3d9e5&name=BT+Sports+Europe'
li = xbmcgui.ListItem('acestream!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://tvenbcsn-i.Akamaihd.net/hls/live/218235/nbcsnx/4296k/prog.m3u8|X-Forwarded-For=66.171.228.102'
li = xbmcgui.ListItem('nbc!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)