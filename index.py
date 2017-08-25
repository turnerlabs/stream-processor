import vlc
import time
import os
import sys


def process_stream(stream, name="snaps", fps=1, skip=0):

    instance = vlc.Instance()

    #Create a MediaPlayer with the default instance
    player = instance.media_player_new()

    #Load the media file
    media = instance.media_new(stream)
    media_list = instance.media_list_new([stream])

    #Add the media to the player
    player.set_media(media)

    lp = instance.media_list_player_new()
    lp.set_media_player(player)
    lp.set_media_list(media_list)

    player.play()
    count = 0
    loading = 0
    fps = 1 / float(fps)
    while True:
        length = player.get_length()
        if length != 0:
            if length < count:
                print("Completed")
                sys.exit(0)

            time.sleep(fps + skip)
            count += float(fps)
            #position = (player.get_length() - count) / float(player.get_length())
            #print('length:', player.get_length(), position)
            #player.set_position(position)
            snap_name = '/tmp/' + name + '/' + str(count) + '_snap.png'
            out = player.video_take_snapshot(0, snap_name, 0, 0)
        elif loading == 30:
            print("Waited 30 seconds for Video to Load")
            sys.exit(1)
        else:
            loading += 1
            time.sleep(1)
            print("Loading...")


if __name__ == '__main__':
    stream = os.environ.get('STREAM', False)
    name = os.environ.get('NAME', None)
    fps = int(os.environ.get('FPS', 1))
    skip = int(os.environ.get('SKIP', 1))

    if stream == False:
        print("Must Provide ${STREAM}")
        sys.exit()
    
    try:
        os.system("rm -rf " + "/tmp/" + name)
    except Exception as e:
        print('ERROR', e)

    os.mkdir('/tmp/' + name)

    process_stream(stream, name, fps, skip)
