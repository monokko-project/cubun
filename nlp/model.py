import spacy
# from transformers import pipeline

ban_keywards = ["上", "前", "後", "横", "右", "左", "部屋"]

class NLPmodel:
    def __init__(self, spacy_model="en_core_web_sm") -> None:
        self.spacy_model = spacy.load(spacy_model)
        # self.translate_model = pipeline('translation', model='staka/fugumt-en-ja')
        self.result = None

    def analyze(self, text):
        self.result = self.spacy_model(text)


    def remove_keyword(self, noun_list):
        
        for n in noun_list:
            if n in ban_keywards:
                noun_list.remove("n")
        return noun_list
    
    def extract_noun(self, text):
        self.analyze(text)
        noun_list = []
        
        print(self.result)
        for token in self.result:
            if token.pos_ == "NOUN":
                # print(token.text)
                noun_list.append(token.text)
        

        normalized_noun_list = self.remove_keyword(noun_list)

        return normalized_noun_list
    
    # def trans_en_to_jp(self, text):
    #     result = self.translate_model(text)
    #     print(result)

# nlp = NLPmodel("ja_ginza")
# text = "あの花は緑の山から取ってきた"
# result = nlp.extract_noun(text)
# print(result)

    