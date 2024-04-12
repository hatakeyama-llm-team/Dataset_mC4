
path_to_footer_word="/data/satori_hdd4/takumi/steve_ssd2/matsuo_llm/JapaneseWarcParser/mc4s/src/cleaner/hoji_dict/header_footer_keywords_ja.txt"
footer_keywords = []
# ファイルを読み込み、各行をリストに追加
with open(path_to_footer_word, "r", encoding="utf-8") as file:
    for line in file:
        # 改行文字を除去してリストに追加
        footer_keywords.append(line.strip())

def remove_footer(text):
    # テキストを行に分割
    lines = text.split('\n')
    #print(lines)
    # 末尾3行をチェック
    if len(lines)>3:
        new_lines = lines[:max(0, len(lines) - 3)]
        for i in range(max(0, len(lines) - 3), len(lines)):
            if any(keyword in lines[i] for keyword in footer_keywords):
                keyword_chars = sum(len(keyword) for keyword in footer_keywords if keyword in lines[i])
                # キーワードを含む文字が行の30%以上を占める場合、フッターと見なす
                if keyword_chars / len(lines[i]) < 0.3:
                    new_lines.append(lines[i])
            else:
                new_lines.append(lines[i])
        # テキストに戻して返す
        return '\n'.join(new_lines)
    return text