
from __future__ import unicode_literals
import youtube_dl
import json
import pyglet


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')




while True:
    #C:\\Users\\PC\\Desktop\\C4T\\session12\\allsongs.json

    with open('/Users/heliadinh/Desktop/CS personal projects/C4T/session12/allsongs.json') as data_file:
        json_file_data = json.load(data_file)

    song_list = []
    song_list.extend(json_file_data)

    print('Pick one option:')
    print('1. Show ALL songs')
    print('2. Show detail of a song')
    print('3. Play a song')
    print('4. Search and download')
    print('5. Exit')

    choice = int(input('>>> '))

    if choice == 4:
        ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'default_search': "ytsearch5",
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

        name = input('Enter the name of a song you want to search: ')

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(name, download=False)

        for i,k in enumerate(info['entries']):
            print(i+1, '.', info['entries'][i]['title'])
            # print(info['entries'][1]['webpage_url'])

        download_action = input('Enter yes if you want to download a song. Enter no if you do not want to download anything. /n >>>')
        if download_action == 'yes':
            download = int(input('Choose the song you want to download: '))
            song_download_url = info['entries'][download-1]['webpage_url']
            song_download_name = info['entries'][download-1]['title']
            song_download_name = [song_download_name]
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # print(info['entries'][download-1]['webpage_url'])
                
                ydl.download([song_download_url])
            
            with open('allsongs.json', 'w') as outfile:
                json.dump( song_download_name, outfile)
            
    
#     elif choice == 2:


    elif choice == 1:


        if song_list == []:
            print('Song list is empty')
        else:
            for i in range(len(song_list)):
                print(i+1, '.', song_list[i])



    elif choice == 3:

        if song_list == []:
            print('Song list is empty')
        else:
            for i in range(len(song_list)):
                print(i+1, '.', song_list[i])

            play_choice = int(input('You want to play song number: '))
            player = pyglet.media.Player()
            path = '/Users/heliadinh/Desktop/CS personal projects/C4T/session12/' + song_list[play_choice - 1] + '.mp3'
            source = pyglet.media.load(path)
            player.queue(source)

            while True: 
                play_action = input('Enter action (play, pause, stop): ')

                if play_action == 'play':
                    player.play()
                elif play_action == 'pause':
                    player.pause()
                else:
                    player.delete()
                    break
            
            pyglet.app.run()

    elif choice == 5:
        break


#     else:
#         print('Try again!')

    

    

    


    





