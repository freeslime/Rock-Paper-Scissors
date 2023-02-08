import pygame
pygame.init()

#variables and constants here
BGCOLOR = ("#cccccc")
player_1 = ""


#load assets here
rock_image = pygame.image.load("rock.png")
rock_image = pygame.transform.scale(rock_image, (200, 200))
paper_image = pygame.image.load("paper.png")
paper_image = pygame.transform.scale(paper_image, (200, 200))
scissors_image = pygame.image.load("scissors.png")
scissors_image = pygame.transform.scale(scissors_image, (200, 200))


#functions to make interactable objects
def rock(x, y):
    pass
def paper(x, y):
    pass
def scissors(x, y):
    pass

def player_choice(text):
    setup_text = pygame.font.SysFont("arial", 60)
    textSurface = setup_text.render(text, True, "black")
    screen.blit(textSurface, (300, 500))
    
#initialize screen and set it up
screen = pygame.display.set_mode([800, 600])

running = True
while running:
    # get input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player_1 = "Rock"
            elif event.key == pygame.K_p:
                player_1 = "Paper"
            elif event.key == pygame.K_s:
                player_1 = "Scissors"
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if (mouse_x >= 100 and mouse_x <= 300) and (mouse_y >= 200 and mouse_y <=400):
                player_1 = "rock"


    #process input

    #update game state
    screen.fill(BGCOLOR)

    scissorz = screen.blit(scissors_image, (500, 200))
    rocky = screen.blit(rock_image, (100, 200))
    papery = screen.blit(paper_image, (300, 200))

    if player_1 != "":
        player_choice(f"You chose {player_1}")

    
    #draw screen
    pygame.display.flip()


pygame.quit
