import pygame
import pickle
import sys

# Инициализация PyGame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кликер")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.Font(None, 36)

# Кнопка для кликов
click_button = pygame.Rect(300, 200, 200, 100)
upgrade_button = pygame.Rect(300, 350, 200, 50)

def save_game():
    data={
        "score": score,
        "click_power": click_power,
        "upgrade_cost": upgrade_cost,
    }
    with open("save.pkl", "wb") as f:
        pickle.dump(data,f)

def load_game():
    global score,click_power,upgrade_cost
    try:
        with open("save.pkl","rb") as f:
            data = pickle.load(f)
            score = data['score']
            click_power = data['click_power']
            upgrade_cost = data['upgrade_cost']
    except FileNotFoundError:
        score = 0
        click_power = 1
        upgrade_cost = 10

def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    global score, click_power, upgrade_cost

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if click_button.collidepoint(mouse_pos):
                    score += click_power
                if upgrade_button.collidepoint(mouse_pos):
                    if score >= upgrade_cost:
                        score -= upgrade_cost
                        click_power += 1
                        upgrade_cost *= 2

        pygame.draw.rect(screen, GREEN, click_button)
        draw_text("Клик!", 370, 230)

        pygame.draw.rect(screen, RED, upgrade_button)
        draw_text(f"Улучшить ({upgrade_cost})", 310, 360)

        draw_text(f"Счет: {score}", 10, 10)

        pygame.display.flip()

    save_game()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    load_game()
    main()
