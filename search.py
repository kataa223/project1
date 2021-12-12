### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source = []

### source.csvを読み込み
def load_charactor_csv():
    with open("source.csv", "r", encoding="utf-8") as f:
        return f.read().split(",")

### sorce、sorce.csvへの追加
def apeend_source(word):
    source.append(word)
    print("{}をsourceに追加しました".format(word))
    
    with open("source.csv", "a", encoding="utf-8") as f:
        f.write(f',{word}')
    print("source.csvに{}を追加しました\n".format(word))

### 検索ツール
def search():
    source = load_charactor_csv()
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