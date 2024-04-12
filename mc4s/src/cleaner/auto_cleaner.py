
import sys
sys.path.append('/data/satori_hdd4/takumi/steve_ssd2/matsuo_llm/JapaneseWarcParser/mc4s/src/cleaner')
from .splitter import text_to_paragraph_sentences
from .text_normalizer import normalize
from . import text_checker
from . import rule_based_line_checker
from . import rule_based_docment_checker
from . import repeated_phrase
from . import footer
#from . import parts_filter

from .line_end_cleaner import clean_line_endings
from .hojichar_filter import hoji_filter


def text_to_cleaned_paragraphs(text):
    text = normalize(text)  # 正規化
    text = text_checker.check(text)  # ひらがなを含まないテキストは除外
    text=rule_based_docment_checker.process_text(text)
    text=repeated_phrase.repeated_id(text)
    text=repeated_phrase.is_repetitive_japanese(text)#n-gramの計算(計算量が多そうな場合、削る)
    
    # パラグラフと文章に分割
    paragraphs = text_to_paragraph_sentences(text)

    new_paragraphs = []
    for paragraph in paragraphs:
        new_lines = []
        old_line = ""
        for line in (paragraph):
            # ルールベースの行チェック
            #print(line)
            new_line = rule_based_line_checker.clean(line)
            if new_line=="":
                continue
            # 名詞だらけのlineを除外(filterかfilter2のいずれかにする)
            #new_line = parts_filter.filter(new_line)
            #new_line = parts_filter.filter2(new_line) #n-gramの計算を行う場合(計算量が多そうな場合、filterにする)
            
            
            if new_line:
                if new_line == old_line:
                    continue
                old_line = new_line
                # ppl=perp_checker(new_line)
                # print(ppl,new_line)
                new_lines.append(new_line)

        if new_lines:
            new_paragraphs.append(new_lines)

    # 文末が｡などでおわらないパラグラフ中の文章を削除
    clean_line_endings(new_paragraphs)

    # パラグラフにまとめる
    cleaned_paragraphs = []
    old_lines = ""
    for paragraph in new_paragraphs:
        lines = "".join(paragraph)
        if lines == old_lines:
            continue
        cleaned_paragraphs.append(lines)
        old_lines = lines

    return cleaned_paragraphs


def clean_text(original_text):
    paragraphs = text_to_cleaned_paragraphs(original_text)
    text = "\n".join(paragraphs)
    if text != "":
        # pass
        text = hoji_filter(text)
        text=footer.remove_footer(text)
    return text
