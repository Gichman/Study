import xml.etree.ElementTree as ET
from collections import Counter

def load_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

def get_descriptions(xml_root):
    return [item.find('description').text for item in xml_root.findall('./channel/item')]

def extract_words(texts, min_length=7):
    words = []
    for text in texts:
        for word in text.lower().split():
            word = ''.join(filter(str.isalpha, word))
            if len(word) >= min_length:
                words.append(word)
    return words

def get_top_words(words, top_n=10):
    counter = Counter(words)
    return counter.most_common(top_n)

def main():
    file_path = 'newsafr.xml'
    xml_root = load_xml(file_path)
    descriptions = get_descriptions(xml_root)
    words = extract_words(descriptions)
    top_words = get_top_words(words)

    print("Топ 10 слов длиннее 6 символов:")
    for word, freq in top_words:
        print(f"{word}: {freq}")

if __name__ == "__main__":
    main()