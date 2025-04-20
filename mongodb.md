# mongodbのインストール
1. 以下のリンクの”1.MongoDBをインストール”に従って、本体のみインストールできる。binへのパスを登録すること
2. インストール後にPCを再起動すると、mongodbサーバープロセスは自動的に起動となる

https://note.com/mega_gorilla/n/ne318906c95ad


# mongo clientのインストール
1. mongo シェルは本体とは別にインストールが必要。
2. 以下のリンクの"3.PowerShellにてDBに接続する"に従って[mongodb shellダウンロードサイト](https://www.mongodb.com/try/download/shell)から、MongoDB Shell Downloadをダウンロードする。ダウンロードしたexeファイルは、mongoDB本体のbinフォルダーにコピーする。
3. コマンドラインからmongoshを入力すると、mongo シェルのプロンプトになる。上記のようにmongodb本体のbinディレクトリはパスを通しているので、コマンドラインはどのようなパスでもOK

https://note.com/mega_gorilla/n/ne318906c95ad

4. mongo clientからのデータベース操作
基本はpythonからダイレクトに操作するが、データベースの一覧、削除など、たまに使う。
コマンド集は以下の通り。

https://www.wakuwakubank.com/posts/784-server-mongodb-introduction/



# dump restoreツールのインストール
1. mongodbツールダウンロードサイトから"MongoDB Command Line Database Tools Download"をダウンロード  
https://www.mongodb.com/try/download/database-tools  
2. ダウンロードしたファイルは、mongo clientと同じく、mongodb本体のbin内にコピーする  
3. dump restoreはwindows コマンドラインから入力する。入力の例は以下のとおり。データベース名を指定せずに、mongodbに入っているデータベースを丸ごとdump restore できる

mongodump --host=localhost --port=27017 --out=C:\Users\uhoku\Dropbox\mongo_backup

mongorestore C:\Users\uhoku\Dropbox\mongo_backup

参考記事  
https://nodejs.keicode.com/mongodb/backup-and-restore.php  


4. 前の世代のPCから移行したmongodb dumpは、mongo_backup に入っている
