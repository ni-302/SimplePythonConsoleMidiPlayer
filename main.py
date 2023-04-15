# ライブラリをインポート
import sys

# 他ファイルのインポート
import pmp.outport
import pmp.midiplayer

# 他ファイルの設定
outport = pmp.outport
player = pmp.midiplayer

# midiデバイスを選択させる
selected_device = outport.select_midi_device()
print(f"選択されたデバイス : {selected_device}")

# midiファイルを再生
try:
    player.midiplayer()
except KeyboardInterrupt:
    sys.exit
