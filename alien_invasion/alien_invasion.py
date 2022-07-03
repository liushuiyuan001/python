import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

pygame.init()
pygame.display.set_caption("Alien Invasion")


class AlienInvasion:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        # 监视鼠标和键盘时间
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 响应按键
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        # 响应松开
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_screen(self):
        # 更新屏幕上的图像，并切换到新屏幕

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _update_bullets(self):
        # 更新子弹的位置并删除消失的子弹
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()

            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
