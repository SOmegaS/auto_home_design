import compress_fasttext
small_model = compress_fasttext.models.CompressedFastTextKeyedVectors.load( 
   'https://github.com/avidale/compress-fasttext/releases/download/v0.0.1/ft_freqprune_100K_20K_pq_300.bin' ) 
print(small_model['Абоба'])
word = ['современный', 'актуальный', 'модный', 'сегодняшний', 'текущий', 'настоящий', 'крутой', 'новый', 'моментный', 'старый', 'древний', 'уютный', 'ностальгичный', 'ранний', 'давний', 'прошлый', 'предшествующий', 'классический', 'стандартный', 'нормальный', 'обычный', 'типичный', 'характерный', 'образцовый']
word1 = ['современный', 'актуальный', 'модный', 'сегодняшний', 'текущий', 'настоящий', 'крутой', 'новый', 'моментный']
word2 = ['старый', 'древний', 'уютный', 'ностальгичный', 'ранний', 'давний', 'прошлый', 'предшествующий']
word3 = ['классический', 'стандартный', 'нормальный', 'обычный', 'типичный', 'характерный', 'образцовый']
model = []
for x in range(len(word1)):
  model.append(1)
for x in range(len(word2)):
  model.append(2)
for x in range(len(word3)):
  model.append(3)
def emb_mod(words):
  vecs = []
  s = []
  for i in words:
    vecs.append(small_model[i])
  for j in range(300):
    col = 0
    n = 0
    for vec in vecs:
      col += vec[j]
      n += 1
    s.append(col / n)
  return s
models = []
models.append(emb_mod(word1))
models.append(emb_mod(word2))
models.append(emb_mod(word3))
print(models)
def simil(vec1, vec2):
  w = []
  for i in range(300):
    w.append(vec1[i] * vec2[i])
  return sum(w)
simil(models[0], models[1])
def pred_mod(us_words):
  us_vec = emb_mod(us_words)
  simils = []
  sim2model = {}
  for vec in models:
    simils.append(simil(vec, us_vec))
  sim_max = max(simils)
  model = 1
  for sim in simils:
    sim2model[sim] = model
    model += 1
  return sim2model[sim_max]

#Ввод:
#pred_mod(список прилагательных: ['уютный', 'модный'........])
#Вывод:
#1 цифра, означающая в каком из стилей делать дизайн
#ABOBA :)
