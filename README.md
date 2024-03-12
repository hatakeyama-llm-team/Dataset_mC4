# Dataset_mC4
mC4のデータ加工を検討するためのレポジトリ

## hatakeyama dev for pretraining
- cleanしすぎないようにしてみる

# setup
~~~
conda create -n webclean -y
conda activate webclean
conda install pip -y
pip install requests
pip install warcio
pip install beautifulsoup4
pip install tqdm
pip install bunkai
pip install emoji==1.7.0
pip install nltk
pip install mecab-python3
pip install fughashi
pip install ja-sentence-segmenter
pip install datasets
pip install hojichar
pip install scikit-learn
pip install python-tlsh

#torch
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

#mecab 日本語の解析に使います
sudo apt install mecab -y
sudo apt install libmecab-dev -y
sudo apt install mecab-ipadic-utf8 -y
pip instal
~~~
