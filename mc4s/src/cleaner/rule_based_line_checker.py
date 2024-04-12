# https://github.com/lighttransport/japanese-llama-experiment/blob/main/03_clean_step1/clean_text.py

import unicodedata
import re
broken_sentence_endings = """
...
... 
...　
\"
'
[…]
"""

broken_ending_list = broken_sentence_endings.split("\n")
broken_ending_list = [x for x in broken_ending_list if len(x) > 0]

broken_ending_list += [
    '続きを読む', '[続きを読む]', '(続きを読む)', '続きを見る', '続きをみる', '(続く)', '(続きを表示)', '(続きをみる)', '[続きをみる]', '[続きを見る]',
]
broken_ending_list += ['...(続きを表示)', '[ 続きを見る ]',
                       '・・・続きを見る', '... 続きを読む',
                       "詳細はこちら »",
                       "詳細>>>"
                       ]

import re

def remove_if_dominated_by_pattern(text, pattern, threshold=0.25):
    matches = re.findall(pattern, text)
    matched_length = sum(len(match) for match in matches)
    pattern_ratio = matched_length / len(text) if len(text) > 0 else 0

    if pattern_ratio > threshold:
        return ""
    return text

def remove_if_dominated_by_patterns(text, patterns, threshold=0.25):
    total_matched_length = 0
    for pattern in patterns:
        matches = re.findall(pattern, text)
        total_matched_length += sum(len(match) for match in matches)

    pattern_ratio = total_matched_length / len(text) if len(text) > 0 else 0
    if pattern_ratio > threshold:
        return ""

    return text


def pattern_filter(text):
    pattern_dic = {
    'date': r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{4}/\d{2}/\d{2}|\d{4}年\d{1,2}月\d{1,2}日|\d{1,2}月\d{1,2}日',
    'time': r'\d{2}:\d{2}(?::\d{2})?|\d{1,2}月\d{1,2}日',
    'URL': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    'Copyright': r'\(c\)|©',
    'Navigation menu': r'[\w\s]+>[^>]+',
    'HTML tag': r'<[^>]+>'
    }
    new_text=text
    for _pattern_name, pattern in pattern_dic.items():
        new_text = remove_if_dominated_by_pattern(new_text, pattern)
    new_text=remove_if_dominated_by_patterns(new_text, [pattern_dic['date'], pattern_dic['time']])
    return new_text



def clean(sent: str):
    pattern=pattern_filter(sent)
    if pattern=="":
        return ""
    for broken_ending in broken_ending_list:
        # print("aa", broken_ending)
        if sent.endswith(broken_ending):
            return None
        if len(sent) < 2:
            return None
    return sent
