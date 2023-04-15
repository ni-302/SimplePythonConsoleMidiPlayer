# ライブラリをインポート
import mido
import sys
import time

# 他ファイルのインポート
import pmp.outport

# 他ファイルの設定
outport = pmp.outport

# ファイルの設定
def midiplayer():
    while True:
        try:
            user_input = input("ファイルを絶対パスで指定してください。 : ")
            if user_input == "":
                continue
            if not user_input.endswith(".mid"):
                if not user_input.endswith(".midi"):
                    if not user_input.endswith(".mid\""):
                        if not user_input.endswith(".midi\""):
                            print(".midまたは.midiファイルを指定してください。")
                            continue
                        else:
                            user_input = user_input.strip('"')
                            midifile = user_input
                            break
                    else:
                        user_input = user_input.strip('"')
                        midifile = user_input
                        break
                else:
                    midifile = user_input
                    break
            else:
                midifile = user_input
                break
        except KeyboardInterrupt:
            sys.exit()
    mid = mido.MidiFile(midifile)
    mido.Message('reset')
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
    for message in mid:
        time.sleep(message.time)
        if not message.is_meta:
            outport.port.send(message)
    midiplayer()
