# ライブラリをインポート
import sys

# 他ファイルのインポート
import pmp.outport
import pmp.midiplayer

# ライブラリの設定
args = sys.argv
args = args[1:]
try:
    arg1 = args[0]
except IndexError:
    pass

# 他ファイルの設定
outport = pmp.outport
player = pmp.midiplayer

# ヘルプメッセージ
help_message = "--help                  : Send this message"

# ヘルプメッセージを送信
try:
    if arg1 == "--help":
        print(help_message)
        sys.exit()
except NameError:
    pass

# midiデバイスを選択させる
if not args:
    try:
        selected_device = outport.select_midi_device()
    except KeyboardInterrupt:
        sys.exit()
    print(f"選択されたデバイス : {selected_device}")

# midiファイルを再生する
try:
    if arg1:
        try:
            selected_device = outport.auto_select_midi_device()
            player.midiplayerargs(arg1)
        except KeyboardInterrupt:
            sys.exit()
except NameError:
    pass
try:
    player.midiplayer()
except KeyboardInterrupt:
    sys.exit()