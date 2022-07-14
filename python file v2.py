import pygame





pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

test_font = pygame.font.Font(None, 50)
proccesed_font_content = 'you win 5 dollars'



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break



    test_font_surf = test_font.render(proccesed_font_content, False, 'RED', None)
    test_font_rect = test_font_surf.get_rect(topleft= (20, 20))

    screen.blit(test_font_surf, test_font_rect)
    clock.tick(60)
    pygame.display.update()



