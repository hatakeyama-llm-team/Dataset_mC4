# %%

"""
mc4を掃除して､fasttextでgood/badを分類して､テキストを出力するコード
"""
import os
#from src.classifier.DatasetAnnotator import DatasetAnnotator
from src.cleaner.auto_cleaner import clean_text
from src.cleaner import url_filter
from datasets import load_dataset
from tqdm import tqdm
import json
# mc4の読み込み
mc4_dataset = load_dataset('mc4', 'ja', split='train', streaming=True)

"""
#oscarなども読み込める
#ignore_verifications=Trueをつけないとエラーとなる
oscar_dataset = load_dataset('oscar', 'unshuffled_original_ja', 
                       split='train', 
                       ignore_verifications=True,
                       streaming=True)

"""

out_path="/data/fairy_hdd4/takumi/corpus/cleaned/mc4_ja_1"



dataset = mc4_dataset

# テキストを分類するためのannotator
#annotator = DatasetAnnotator(dataset, clean_func=clean_text, n_preload=50000)

# 何行ごとにファイルを分割するか
n_split = 10**5

corpus_dir = "corpus"
if not os.path.exists(corpus_dir):
    os.makedirs(corpus_dir)

cnt = 0
record_id = -1
for record in tqdm(dataset):
    record_id += 1

    try:
        text = record['text']
        url=record['url']
        #urlフィルター
        is_rejected=url_filter.u_filter(url)
        if is_rejected==True:
            continue
        # テキストクリーン
        text = clean_text(text)
        if text == "":
            continue

        # 記事の判定
        #is_noise = annotator.predict(text)
        #if is_noise == 1:
          #  continue

        d = {
            "id": record_id,
            "text": text,
        }
        file_name = f"{out_path}/{cnt//n_split}.jsonl"
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(json.dumps(d) + '\n')
    except Exception as e:
        print(e)
        continue
