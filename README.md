# SimplePythonConsoleMidiPlayer
コンソールで動作するシンプルなMIDIプレイヤー

# 使用方法
1. pythonをインストールしてください。
2. pipなどで`mido`と`python-rtmidi`をインストールしてください。
3. リリースからzipをダウンロードして解凍して、お好きなフォルダに配置してください。
- `SimplePythonConsoleMidiPlayer`フォルダの名前は変えても問題ありませんが、中のファイル(main.pyなど)の名前を変えたり位置関係を変えたりしないでください。
4. `python main.py`で実行できます。
5. 画面に従ってMIDIデバイスを設定して、ファイルを選択すると再生が始まります。
- Windowsの場合(Linuxでは未検証)はコマンドプロンプトにファイルをドラッグ&ドロップでもファイルを選択できます。
6. 再生が終わると、またファイルを選択できる状態になります。
7. 以降無限ループのため、終了には`Ctrl+C`を使用してください。
8. アンインストールは`SimplePythonConsoleMidiPlayer`フォルダを消すだけでOKです。
