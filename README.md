# Flask app sample for GAE.

## Google App Engineに元からはいっていないライブラリを使う

libs/ ディレクトリを作り、
```pip install -t libs ライブラリ名```
で、libs以下にライブラリをインストールします。


main.pyに以下を追加して、libsへのパスをアプリケーションに追加してください。

```
import sys
sys.path.insert(0, 'libs')
```
