# easily_language_processing
このプロジェクトは文書ファイルをdocumentフォルダ内に入れればその文書内の文章、単語に対して言語処理を行うものです。  
例えば、文書全体や文章ごとのPN（ポジティブ・ネガティブ）値を算出することができます。  
次に各単語の関連語をwordnetにより提案することができ、言語データの増加（augmentation）を行うことができます。  
また、文書全体のトピックの抽出、ワードクラウドを用いた文書内の頻出単語の可視化ができるようになっています。  
あまり言語処理に慣れていない人が手軽に言語処理の代表的なアプローチを行うことができるシステムです。  
テキストコーパスには青空文庫の夏目漱石の作品やlivedoorコーパスを用いています。  

livedoorコーパスはhttps://www.rondhuit.com/download.html からダウンロードし、document以下に置いてください。
```
easily_language_processing/document/livedoor/...
```
