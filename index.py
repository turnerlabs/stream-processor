import vlc
import time
import os
import sys

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '++++++++++++++++++++ TIMING ++++++++++++++++++++++++++++++++++++'
        print ''
        print '%s function took %0.3f m' % (f.func_name, ((time2-time1)/60))
        print ''
        print '++++++++++++++++++++ TIMING ++++++++++++++++++++++++++++++++++++'
        return ret
    return wrap

@timing
def process_stream(stream, name, fps, skip):

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
        if length != 0 && length > count:
            if length <= count + 1:
                print("Completed")
                sys.exit(0)
                return

            time.sleep(fps + skip)
            # current_time = float(player.get_time())
            # count = int(current_time + (1000 * (fps + skip)))
            # player.set_time(count)
            #position = (player.get_length() - count) / float(player.get_length())
            #print('length:', player.get_length(), position)
            #player.set_position(position)
            current_time = float(player.get_time())
            count = current_time
            snap_name = '/tmp/' + name + '/' + str(float(count/1000)) + '_snap.png'
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
    name = os.environ.get('NAME', "snaps")
    fps = int(os.environ.get('FPS', 1))
    skip = int(os.environ.get('SKIP', 0))

    if stream == False:
        print("Must Provide ${STREAM}")
        sys.exit()
    
    try:
        os.system("rm -rf " + "/tmp/" + name)
    except Exception as e:
        print('ERROR', e)

    os.mkdir('/tmp/' + name)

    process_stream(stream, name, fps, skip)
