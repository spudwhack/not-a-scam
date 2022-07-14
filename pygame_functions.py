import pygame
clock = pygame.time.Clock()






letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n''o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def typing(event, letters, font_list):
    for letter in letters:
        if event == pygame.KEYDOWN:
            if event == pygame.K_a:
                return



def bs_typing(event, list):
    if event == pygame.KEYDOWN:
        if event == pygame.K_a:
            list.append('a')