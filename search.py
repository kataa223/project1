### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### source.csvを読み込み
open_file = open('source.csv', encoding='utf-8')
data = open_file.read()
source = data.split(',')
open_file.close()

### sorce、sorce.csvへの追加
def apeend_source(word):
    source.append(word)
    print("{}をsourceに追加しました".format(word))
    
    append_file = open('source.csv', 'a', encoding='utf-8')
    append_file.write(f',{word}')
    append_file.close()
    print("source.csvに{}を追加しました\n".format(word))

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました\n".format(word))
    else:
        print("{}は見つかりませんでした".format(word))        
        apeend_source(word)
        

if __name__ == "__main__":
    while True:
        search()