
import unicodedata

def nfkc_normalize(text):
    return unicodedata.normalize('NFKC', text)

def split_sentences(text):
    text2=text
    # 正規表現パターン: 「。」、「？」、「！」
    pattern = r'[。？！]+'
    # 正規表現で分割
    sentences = re.split(pattern, text2)
    # 空の要素を除去
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    return sentences

#句読点正規化
import re
# 正規表現を使用して、英数字の直前にある「，」と「.」を置換の対象から外す
def normalize_punctuation(text):
    if text =="":
        return ""
    # 記号「、」および「，」の出現回数を調べる
    comma_count = text.count('，')
    jp_comma_count = text.count('、')

    # 「，」が「、」より多く出現する場合、置換を行う
    if comma_count > jp_comma_count:
        text = re.sub(r'(?<![A-Za-z0-9])，', '、', text)

    # 記号「。」および「.」の出現回数を調べる
    period_count = text.count('.')
    jp_period_count = text.count('。')

    # 「.」が「。」より多く出現する場合、置換を行う
    if period_count > jp_period_count:
        text = re.sub(r'(?<![A-Za-z0-9])\.', '。', text)

    return text

# 品質(文字数)
def process_text(text):
    input_text=normalize_punctuation(unicodedata.normalize('NFKC', text))
    # 文字数 (400 文字未満)
    if len(input_text) < 100:
        #print(f"ながさ：{len(input_text)}")
        return ""

    # 平仮名の文字の割合 (0.2 未満)
    hiragana_count = sum(1 for char in input_text if char >= 'ぁ' and char <= 'ん')
    total_chars = len(input_text)
    hiragana_ratio = hiragana_count / total_chars
    if hiragana_ratio < 0.2:
        #print(f"ひらがなの割合：{hiragana_ratio}")
        return ""

    # カタカナの文字の割合 (0.5 以上)
    katakana_count = sum(1 for char in input_text if char >= 'ァ' and char <= 'ヶ')
    katakana_ratio = katakana_count / total_chars
    if katakana_ratio >= 0.5:
        #print(f"カタカナの割合：{katakana_ratio}")
        return ""

    # 日本語の文字 (平仮名、カタカナ、漢字、句読点)の割合 (0.5 未満)
    japanese_chars_count = sum(1 for char in input_text if char >= 'ぁ' and char <= 'ん' or char >= 'ァ' and char <= 'ヶ' or char >= '一' and char <= '龯' or char in ['。', '、', '！', '？', 'ー'])
    japanese_chars_ratio = japanese_chars_count / total_chars
    if japanese_chars_ratio < 0.5:
        #print(f"日本語の割合：{japanese_chars_ratio }")
        return ""

    # 文書中の文の文字数の平均 (20 未満、もしくは 90 よりも多い場合)
    sentences = split_sentences(input_text)
    avg_sentence_length = sum(len(sentence) for sentence in sentences) / len(sentences)
    if avg_sentence_length < 10 or avg_sentence_length > 120:
        #print(f"平均長：{avg_sentence_length}")
        return ""

    # 最も長い文の文字数 (200 文字以上)
    max_sentence_length = max(len(sentence) for sentence in sentences)
    if max_sentence_length >= 300:
        #print(f"長い文：{max_sentence_length}")
        #print(text)
        return ""


    # 文末が省略記号で終わる文の割合 (0.2 以上)
    #ellipsis_count = sum(1 for sentence in sentences if sentence.endswith('…'))
    #ellipsis_ratio = ellipsis_count / len(sentences)
    #if ellipsis_ratio >= 0.2:
        #print(f"省略：{ellipsis_ratio}")
        #return ""

    # 条件に合致しない場合は入力テキストをそのまま返す
    return input_text