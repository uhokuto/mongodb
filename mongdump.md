# mongodb のデータ移行（dump, restore)

1. データ移行ツールのダウンロード  
   mongodb本体とは別に移行ツールをダウンロードする必要がある。手順は[こちら](https://www.osumoi-stdio.com/pyarticle/book/107/5)の準備から。
2. データベースのバックアップ(dump)  
   windows command promptを管理者権限で起動して、上記ツールをダウンロードしたディレクトリに移動し、以下のコマンドを入力する。これで、指定したデータベース名のフォルダがこのディレクトリ内に作成されて、必要なデータベース群が書き出される。

   >mongodump --db=cookpad_nii_database

3. データベースのリストア(restore)
   上記でバックアップしたフォルダを移行先のmongodbにリストアする。コマンドは以下。なお、2.と同様に、管理者権限でwindows command promptを起動し、移行ツールをダウンロードしたディレクトリに移動してから以下のコマンドを入力する

   >mongorestore フォルダ名

   [参考サイト](https://nodejs.keicode.com/mongodb/backup-and-restore.php)