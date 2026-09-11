import pygame

pygame.init()

breite, hoehe = 800, 500
fenster = pygame.display.set_mode((breite, hoehe))
pygame.display.set_caption("Pygame-Demo")

uhr = pygame.time.Clock()
spieler = pygame.Rect(100, 200, 50, 50)
geschwindigkeit = 300
aktiv = True

while aktiv:
    sekunden = uhr.tick(60) / 1000

    for ereignis in pygame.event.get():
        if ereignis.type == pygame.QUIT:
            aktiv = False

    tasten = pygame.key.get_pressed()

    if tasten[pygame.K_LEFT]:
        spieler.x -= geschwindigkeit * sekunden
    if tasten[pygame.K_RIGHT]:
        spieler.x += geschwindigkeit * sekunden
    if tasten[pygame.K_UP]:
        spieler.y -= geschwindigkeit * sekunden
    if tasten[pygame.K_DOWN]:
        spieler.y += geschwindigkeit * sekunden

    spieler.clamp_ip(fenster.get_rect())

    fenster.fill((25, 30, 45))
    pygame.draw.rect(fenster, (255, 140, 50), spieler)
    pygame.display.flip()

pygame.quit()
