# ライブラリをインポート
import mido
import sys

# 変数の初期設定
result = None
port = None

# midiデバイスを選択させる
def select_midi_device():
    midi = mido.get_output_names()
    midi_devices = {}
    for i, device in enumerate(midi):
        device_name = device.rsplit(' ', 1)[0]
        device_var_name = f"{i+1}"
        midi_devices[device_var_name] = device_name
    while True:
        n = len(midi_devices)
        try:
            for key, value in midi_devices.items():
                print(f"{key} : {value}")
            user_input = int(input(f"midiデバイスを選択してください。[1-{n}] : "))
            if user_input < 1 or user_input > n:
                print(f"入力された値が不正です。1から{n}までの数字を入力してください。")
            else:
                global port
                port = mido.open_output(result)
                return midi_devices[str(user_input)]
        except ValueError:
            print("数字を入力してください。")
        except KeyboardInterrupt:
            sys.exit

# midiデバイスを閉じる
def close_midi_device():
    port.close()