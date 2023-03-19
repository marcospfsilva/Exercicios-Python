#exercício que simula funcionamento de uma TV

class Televisao:
    # A função abaixo define a tv como desligada e com canal 1
    def __init__(self):
        self.ligada = False
        self.canal = 1
    
    # A função power vai desligar caso a tv esteja ligada e ligar caso esteja desligada.
    def power(self):
        if self.ligada == True:
            self.ligada = False
        else:
            self.ligada = True
    
    #A função aumenta_canal, caso acionada, vai aumentar apenas se a tv estiver ligada
    def aumenta_canal(self):
        if self.ligada == True:
            self.canal +=1
    
    #A função diminui_canal, caso acionada, vai diminuir também se a tv estiver ligada
    def diminui_canal(self):
        if self.ligada ==True:
            self.canal -=1
    

televisao = Televisao()

print("A tv está ligada?: {}" .format(televisao.ligada))

#Abaixo ocorre a ligação da TV.
televisao.power()
print("A tv está ligada?: {}" .format(televisao.ligada))

#Aumentou um canal se entender que a tv está ligada
televisao.aumenta_canal()
print("Canal: {}".format(televisao.canal))

