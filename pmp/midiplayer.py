# ライブラリをインポート
import mido
import sys

# 他ファイルのインポート
import pmp.outport

# 他ファイルの設定
outport = pmp.outport

# ファイルの設定
def midiplayer():
    while True:
        try:
            user_input = input("ファイルを絶対パスで指定してください。\nアプリケーションを終了する場合は\"exit\"と入力してください。\n>")
            if user_input == "":
                continue
            if user_input == "exit":
                sys.exit
                return
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
    for msg in mid.play():
        outport.port.send(msg)
    midiplayer()