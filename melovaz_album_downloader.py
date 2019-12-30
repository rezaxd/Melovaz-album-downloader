import requests as re
from bs4 import BeautifulSoup as bs
from zipfile import ZipFile
import os

url = input("Enter url of album that u want download:\n")
# url = "https://melovaz.net/this-is-dua-lipa"

inf_album = bs(re.get(url).text, 'html.parser')

print("[*] Please w8!")
print("[*] Getting album title...")

album_title = inf_album.select(".AL-Si")[0].text
album_by    = inf_album.select(".AR-Si")[0].text
print("### Album Title: %s"%album_title)
print("### %s\n"%album_by)

print("[*] Getting album musics title...")
album_musics= inf_album.select('[data-title]')
for i in album_musics:
    print("### %s"%i['data-title'])
print("")

print("[*] Getting album musics url...")
musics_urls = inf_album.select('.audioplayer-source')
print("[*] Done!\n")

print("[*] Starting download musics...")
for i in range(len(album_musics)):
    print("[*] Downloading %s..."%album_musics[i]['data-title'])
    music_download = re.get(musics_urls[i]['data-src'])
    with open('%s.mp3'%album_musics[i]['data-title'], 'wb') as music:
        music.write(music_download.content)
    print("[*] %s Downloaded successfully!"%album_musics[i]['data-title'])
    print("")    
print("\n[*] All musics downloaded successfully!")
print("-------------------------------------------------------------------")

print("[*] Creating zip file, as '%s.zip'"%album_title)
with ZipFile("%s.zip"%album_title, "w") as music_zip_file:
    for each_music in album_musics:
        print("[*] Adding %s.mp3 \t into %s.zip..."%(each_music['data-title'], album_title))
        music_zip_file.write('%s.mp3'%each_music['data-title'])
print("[*] Done!\n")
print("[*] Deleting music files...")

try:
    for m in album_musics:
        print("[*] Deleting %s.mp3..."%m['data-title'])
        os.remove('%s.mp3'%m['data-title'])
    print("[*] Done!")
except:
    print("[*] Cant Delete music files...")