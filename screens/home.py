from select import select
import pygame
import sys
from pygame.locals import *


class Home():
    def __init__(self, screen, mylcd, speed, direction, laps) -> None:
        self.is_running = True
        self.screen = screen
        self.my_lcd = mylcd
        self.OPTIONS = [
            {
                'option': 'Speed',
                'text': f'Velocidad:{speed}%'
            },
            {
                'option': 'Direction',
                'text': f'Sentido:{direction}'
            },
            {
                'option': 'Laps',
                'text': f'Vueltas:{laps}'
            },
            {
                'option': 'Start',
                'text': 'Iniciar'
            }
        ]
        self.selected = 0

    def __show_menu(self, is_going_down):

        self.my_lcd.lcd_clear()
        new_options = self.OPTIONS[self.selected -
                                   is_going_down:self.selected+2-is_going_down]

        self.my_lcd.lcd_display_string(new_options[0].get('text'), 1)
        self.my_lcd.lcd_display_string(new_options[1].get('text'), 2)
        self.my_lcd.lcd_display_string('*', is_going_down+1, 15)

    def show_screen(self) -> str:
        self.__show_menu(0)
        while self.is_running:
            self.screen.fill((255, 255, 255))
            # 2.- Se comprueban los eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and len(self.OPTIONS) > self.selected+1:
                        self.selected += 1
                        self.__show_menu(1)
                    elif event.key == pygame.K_UP and 0 < self.selected:
                        self.selected -= 1
                        self.__show_menu(0)
                    elif event.key == pygame.K_RETURN:
                        self.is_running = False
            pygame.display.update()

        return self.OPTIONS[self.selected].get('option')
