
# * não há uma regra sobre a quantidade de imagens positivas ou negativas,
# * Primeiro teste: dobro de positivas em relção as negativas,
# * Se houver muitos falsos positivos, adotar a regra inversa,
# * Regras gerais: - se há falso positivo é preciso adicionar mais imagens negativas
#                 - se há muitos flasos negativos é preciso adicionar mais imagens positivas ou ajustar os parâmetros
# Para um classificador mais robusto: coletar imagens manualmente e em vários cenários
# Para objetos mais rígidos (logos) pode-se usar somente o createsamples
# Ao aumentar as imagens positivas vai aumentar a generalização do modelo (melhor características que descrevam o objeto)
# Em imagens nas quais o objeto está um pouco diferente do modelo treinado o algorítmo tem mais chances para encontrar o objeto
# Evita o sobreajuste(overfitting) do modelo, que ocorre quando o modelo se ajusta tão bem a esse conjunto de imagens de
# treinamento mas é ineficaz para prever novos resultados
# -minHitrate 0.99 (qt mais perto de 1 melhor, um bom valor usado é o 0.998 )/
# -maxFalseAlarmRate 0.1 ( qt menor o valor, melhor; é uma taxa máxima de alarme falso desejado para cada estágio - definição de qts recursos precisam ser adicionados)/
# -maxWeakCount 1000 (qt maior o valor melhor)
# O tempo de treinamento pode ficar extremamente lento, principalmente quando começa a chegar nos últimos estágios. Caso o número de imagens
# positivas e /ou negativas seja maior que 5000 o treinamento poderá levar dias ou até mesmo semanas
##
#Treinamento com LBP (precisa de muito mais imagens e é mais rápido)

# CONSIDERAÇÕES HAARCASCADES:
# Executa rápido (vários detectores pela webcam)
# Recomendável para objetos com pouca variação(logos) - poucas imagens para o treinamento
# Não muito recomendável para objetos com grande variação ( celular ligado, com capinha/ treinando muitas variações o classificador pode ficar fraco /
#Objetos que a cor é determinante/ canecas com estampas diferentes/ necessárias muitas imagens e muitos testes
#
#OUTRAS TÉCNICAS: * HOG + SVM (Dlib) / * Redes Neurais convolucionais

# TRATAMENTO DE IMAGENS
# Softwares peara edição de imagens, como GIMP ou Photoshop
# Ferramentas online
# Dar preferência para imagens que o fundo esteja totalmente branco e com iluminação para identificar bem o objeto
# Imagem que contenham somente o objeto, pois assim não será necessário realizar outros pré-processamento
# Em uma imagem original, retirar o fundo e o brilho: exemplo, aumentar o brilho para o valor 30, não pode aumentar muito pois o contraste ainda precisa ser aumentado
# aumentar o contraste até o fundo ficar branco, se usado para tirar a sombra, tomar cuidado para não descaracterizar a imagem
# se a imagem ainda tiver alguma coisa, usar a ferramenta borracha

# * createsamples - para geração de imagens positivas

# * traincascade - para treinar o detector

# * annotation - para marcação de imagens


#BIANCA

"""OpenCV"""
# Ler imagem
# cv2.imread('img.png') # abre a imagem

# Tratamento de imagens
# cv2.convertScaleAbs(img, 1.0, 1.0) # adicionar filtro na imagem ajustando o contraste e o brilho

# Classificadores e detecções
# cv2.CascadeClassifier('cascade.xml') # classificador Haarcascade
# cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte a imagem para a escala de cinza
# classifier.detectMultiScale(img_cinza, scaleFactor=1.1, minNeighbors=1) # usa o classificador para detectar o objeto
#
# scaleFactor - especifica o quanto o tamanho da imagem é reduzido em cada escala de imagem
# minNeighbors - janelas vizinhas minimas para ser considerado uma detecção válida
# minSize - tamanho minimo do objeto
# maxSize - tamanho maximo do objeto
# * minSize == maxSize - analise em escala unica
#
# A função retorna uma lista de tuplas com os elementos encontrados na imagem [x, y, a, l]
# [x, y, x + a, y + l]
# as coordenadas 'a' e 'l' são iguais
# As coordenadas formam um retangulo

# ROI - Região de Interesse
# roi = imagem[y:y+l, x:x+a] # imagem e as coordenadas da região de interesse
#
# Coordenadas da detecção pelo Classificador
# O ROI precisa estar dentro de um laço de repetição para mais de uma região de contorno
# Desenha dentro do retangulo de detecções ** depois do comando de draw

# Procurar contornos
# cv2.threshold(img_cinza/roi_cinza, 127, 255, 0) # imagem binária para procurar os contornos
# cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) # Retorna dois objetos, os contornos e a hierarquia
#

# CONTORNOS
# cv2.RETR_LIST - lista de todos os contornos sem nenhum tipo de hierarquia
# cv2.RETR_TREE - lista de todos os contornos e suas hierarquias em ordem

# cv2.RETR_CCOMP - lista de todos os contornos e suas hierarquias em 2 niveis
# cv2.RETR_EXTERNAL - lista de contornos externos pela hierarquia
# * Pode ser usado para algum tipo de classificação de linhas *
# [1,1,1,1] onde [próximo, anterior, filho, pai] # próximo e anterior são contornos no mesmo grau na hierarquia
# filho é o nível abaixo na hierarquia e pai o nível acima.
# quando os contornos não possuem uma dos atributos é representado por '-1'
#
# cv2.CHAIN_APPROX_NONE - retorna todos os pontos do contorno
# cv2.CHAIN_APPROX_SIMPLE - retorna apenas o ponto inicial e final do contorno(linhas)
# *Quase não geram diferenças no resultado mas possuem tamanhos diferentes

# Desenhar contornos
# cv2.drawContours(roi/img, contornos, -1, (0, 255, 0), 2,  hierarchy=hierarchy, maxLevel=2)
# desenha os contornos na imagem
#
# hierarchy - variavel com os niveis de hierarquia
# maxLevel - nivel maximo da hierarquia

# Mostrar imagem
# cv2.imshow('example', img) # mostra a imagem
# cv2.waitKey(0)
# cv2.destroyAllWindows() # encerra o programa quando a janela aberta fecha # retira o erro no terminal