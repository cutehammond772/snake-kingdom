import pygame


class GameLauncher(object):
    def __init__(self):
        self.__running = True

        # pygame 초기화
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__frame = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("지렁의 왕국 (v0.1.0)")

    def launch(self):
        while self.__running:
            # 이벤트 처리
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            # 화면 업데이트
            pygame.display.update((0, 0, 1280, 720))

            # 틱
            self.__clock.tick(10)

        pygame.quit()


if __name__ == '__main__':
    game = GameLauncher()
    game.launch()
