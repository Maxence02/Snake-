import sys,random
import pygame


class Snake:
    """
    crée un jeu similaire au snake avec un serpent qui doit manger des pommes sans se mordre ni depasser les limites 


    """
    def __init__(self):
        """

        
        """
        self.ecran = pygame.display.set_mode((1280, 860))# creer la fenetre 

        pygame.display.set_caption('Snake')# donne un titre a la fenetre
        self.jeu_encours = True

        # creer les variables de position et de direction du serpent lors du debut de la partie
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        self.serpent_corps = 20

        # creer la position pour la pomme

        self.pomme_position_x = random.randrange(110,690,20)
        self.pomme_position_y = random.randrange(110,590,20)
        self.pomme = 20
        # fixer les fps car sinon le serpent vas beaucoup trop vite
        self.clock = pygame.time.Clock()

        #creer une liste qui rescence toutes les positions du serpent
        self.positions_serpent = []

        # creer la variable en rapport avec la taille du serpent
        self.taille_du_serpent = 1

        self.ecran_du_debut = True

        self.image_tete_serpent = pygame.image.load('tete.png')


        # Charger l'image

        self.image = pygame.image.load("ecran_d'acceuil.jpg")
        # retrecir l'image
        self.image_titre = pygame.transform.scale(self.image,(730,500))

        # creer la variable score


        self.score = 0

    def evenement(self):

        # permet de gerer les evenements et d'afficher 

        while self.ecran_du_debut:

            for evenement in pygame.event.get():# verifier les evenements lorsque le jeu est en cours
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:

                        self.ecran_du_debut = False

                self.ecran.fill((0,0,0))

                self.ecran.blit(self.image_titre,(300,50,100,50))
                self.creer_message('moyenne','Appuyer sur Enter pour commencer', (500, 650, 200, 5),
                                    (255, 255, 255))

                pygame.display.flip()




        while self.jeu_encours == True :

            # tant que le jeu est en cours 

            for evenement in pygame.event.get():# verifier les evenements lorsque le jeu est en cours
                #print(evenement)
                if evenement.type == pygame.QUIT:
                    sys.exit()

                # creer les evenements qui permettent de bouger le serpent

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        # lorsque l'on presse la touche 'fleche droite'
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0
                        #print('Droite')

                    if evenement.key == pygame.K_LEFT:
                        # lorsque l'on presse la touche 'fleche gauche'

                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0
                        #print('LEFT')

                    if evenement.key == pygame.K_DOWN:
                        # lorsque l'on presse la touche 'fleche vers le  bas'

                        self.serpent_direction_y = 10
                        self.serpent_direction_x = 0
                        #print('En bas')

                    if evenement.key == pygame.K_UP:
                        # lorsque l'on presse la touche 'fleche vers le haut'

                        self.serpent_direction_y = -10
                        self.serpent_direction_x = 0
                        #print('En haut ')

            if self.serpent_position_x <= 100 or self.serpent_position_x >= 1170 \
                or self.serpent_position_y <= 100 or self.serpent_position_y >= 750 :
                # si la position du serpent depasse les limites alors le jeu s'arrete
                sys.exit()




            self.serpent_mouvement()

            # cree la condition si le serpent mange la pomme

            if self.pomme_position_y == self.serpent_position_y and self.serpent_position_x == self.pomme_position_x:

                print('miam')

                self.pomme_position_x = random.randrange(110,690,20)
                self.pomme_position_y = random.randrange(110,590,20)

                # augmenter la taille du serpent

                self.taille_du_serpent += 2
                #augmenter le score
                self.score += 1

            # creer une liste pour les qui stocke la position de la tete du serpent
            la_tete_du_serpent = []
            la_tete_du_serpent.append(self.serpent_position_x)
            la_tete_du_serpent.append(self.serpent_position_y)

            self.positions_serpent.append(la_tete_du_serpent)

            # cond pour resoudre le probleme des positions du serpent avec la taille du serpent
            if len(self.positions_serpent) > self.taille_du_serpent:

                self.positions_serpent.pop(0)
                


            self.affichage()
            self.se_mord_la_queue(la_tete_du_serpent)

            self.creer_message('grande','Snake', (590, 10, 100, 50), (255, 255, 255), )
            self.creer_message('grande','{}'.format(str(self.score)), (640, 50, 50, 50), (255, 255, 255), )

            # afficher les limites
            self.creer_limites()
            self.clock.tick(30)

            pygame.display.flip()# mettre a jour l'ecran


    # creer une fonction qui permet de creer un rectangle qui representera les limites du jeu (dimension 100,100,600,500),3


    def creer_limites(self):
        # afficher les limites du jeu

        pygame.draw.rect(self.ecran,(255,255,255),(100,100,1080,660),3)

    def serpent_mouvement(self):

        # faire bouger le serpent

        self.serpent_position_x += self.serpent_direction_x  # faire bouger le serpent a gauche ou a droite
        self.serpent_position_y += self.serpent_direction_y  # faire bouger le serpent en haut ou en bas

        # print(self.serpent_position_x,self.serpent_position_y)


    def affichage(self):

        self.ecran.fill((0, 0, 0))  # attriubue la couleur noir a l'ecran

        self.ecran.blit(self.image_tete_serpent,(self.serpent_position_x,self.serpent_position_y,
                                                 self.serpent_corps,self.serpent_corps))

        # afficher la pomme
        pygame.draw.rect(self.ecran, (255, 0, 0),
                         (self.pomme_position_x, self.pomme_position_y, self.pomme, self.pomme))

        self.afficher_Serpent()
        


    def afficher_Serpent(self):
        # afficher les autres parties du serpent

        for partie_du_serpent in self.positions_serpent[:-1]:#crée une boucle qui prend tous les element sauf le dernier 
            pygame.draw.rect(self.ecran, (0, 255, 0),
                             (partie_du_serpent[0], partie_du_serpent[1], self.serpent_corps, self.serpent_corps))

    def se_mord_la_queue(self,tete_serpent):


        # le seprent se mord

        for partie_serpent in self.positions_serpent[:-1]:#crée une boucle qui prend tous les element sauf le dernier 
            if partie_serpent == tete_serpent :
                sys.exit()
# creer une fonction qui permet d'afficher des messages

    def creer_message(self,font,message,message_rectangle,couleur):



        if font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)

        message = font.render(message,True,couleur)

        self.ecran.blit(message,message_rectangle)



if __name__ == '__main__':

    pygame.init()# initie pygame
    Snake().evenement()
    pygame.quit()# quitte pygame