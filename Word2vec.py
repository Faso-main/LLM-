from gensim import models


"https://habr.com/ru/articles/801807/"
"""
Две основные архитектуры модели Word2Vec:
CBOW (Continuous Bag of Words): Этот подход предсказывает текущее слово на основе контекста вокруг него. Например, 
для фразы "синее небо над головой", модель CBOW будет пытаться предсказать слово "небо" на основе 
контекстных слов "синее", "над", "головой". CBOW быстро обрабатывает большие объемы данных, но менее эффективен для редких слов.

Skip-Gram: В этом подходе наоборот, используется текущее слово для предсказания слов в его контексте. 
Для того же примера, модель Skip-Gram будет пытаться предсказать слова "синее", "над", "головой" на основе слова "небо". 
Skip-Gram медленнее обрабатывает данные, но лучше работает с редкими словами и менее частыми контекстами."""

sents = ['люблю собак',
   'люди нелюди так сказать',
   'самое высокое здание в мире было спроектировано с моего скипетра']


sents = [sent.split() for sent in sents]
print(sents)

custom_model = models.Word2Vec(sents, min_count=1,vector_size=300,workers=4)

#vect=custom_model.most_similar('собак')

