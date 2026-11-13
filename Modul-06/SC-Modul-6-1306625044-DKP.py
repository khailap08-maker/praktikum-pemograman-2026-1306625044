import sys

import numpy as np
import pygame


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
GROUND_Y = 520
SCALE = 80.0
BALL_RADIUS = 20
GRAVITY = 9.81
INITIAL_HEIGHT = 5.0
BOUNCE_RESTITUTION = 0.72
MIN_BOUNCE_SPEED = 1.0
FPS = 60

WHITE = (250, 250, 250)
BLACK = (35, 35, 35)
PINK = (255, 192, 203)


def create_bounce_sound():
    sample_rate = 44100
    duration = 0.12
    samples = np.arange(int(sample_rate * duration), dtype=float)
    envelope = np.exp(-samples / (sample_rate * 0.035))
    waveform = np.sin(2.0 * np.pi * 180.0 * samples / sample_rate)
    audio = (waveform * envelope * 12000).astype(np.int16)
    return pygame.mixer.Sound(buffer=audio.tobytes())


def reset_ball():
    position = np.array([SCREEN_WIDTH / 2.0, INITIAL_HEIGHT], dtype=float)
    velocity = np.array([0.0, 0.0], dtype=float)
    return position, velocity, 0.0, False


def draw_scene(screen, font, position, velocity, elapsed, started, landed, bounces):
    screen.fill(PINK)
    pygame.draw.rect(screen, BLACK, (0, GROUND_Y, SCREEN_WIDTH, 8))

    pixel_x = int(position[0])
    pixel_y = int(GROUND_Y - position[1] * SCALE)
    pygame.draw.circle(screen, WHITE, (pixel_x, pixel_y), BALL_RADIUS)

    speed = float(np.linalg.norm(velocity))
    text_lines = [
        "Simulasi Bola Jatuh Bebas",
        "Gravitasi: %.2f m/s^2" % GRAVITY,
        "Waktu: %.2f s" % elapsed,
        "Ketinggian: %.2f m" % max(0.0, float(position[1])),
        "Kecepatan: %.2f m/s" % speed,
        "Jumlah pantulan: %d" % bounces,
    ]

    if landed:
        text_lines.append("Bola berhenti - klik atau tekan R untuk mengulang")
    elif started:
        text_lines.append("Tekan R untuk mengulang, Esc untuk keluar")
    else:
        text_lines.append("Klik atau tekan Spasi untuk mulai jatuh")

    y = 18
    for line in text_lines:
        label = font.render(line, True, BLACK)
        screen.blit(label, (18, y))
        y += 28

    pygame.display.flip()


def main():
    pygame.init()
    bounce_sound = create_bounce_sound()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulasi Bola Jatuh Bebas")
    font = pygame.font.SysFont(None, 26)
    clock = pygame.time.Clock()

    position, velocity, elapsed, started = reset_ball()
    landed = False
    bounces = 0
    running = True

    while running:
        delta_time = clock.tick(FPS) / 1000.0
        if delta_time > 0.05:
            delta_time = 0.05

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    position, velocity, elapsed, started = reset_ball()
                    landed = False
                    bounces = 0
                elif event.key == pygame.K_SPACE:
                    if landed:
                        position, velocity, elapsed, started = reset_ball()
                        landed = False
                        bounces = 0
                    started = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if landed:
                    position, velocity, elapsed, started = reset_ball()
                    landed = False
                    bounces = 0
                started = True

        if started and not landed:
            acceleration = np.array([0.0, -GRAVITY], dtype=float)
            position += velocity * delta_time
            velocity += acceleration * delta_time
            elapsed += delta_time

            minimum_height = BALL_RADIUS / SCALE
            if position[1] <= minimum_height:
                position[1] = minimum_height
                impact_speed = abs(float(velocity[1]))
                bounces += 1
                bounce_sound.set_volume(max(0.25, min(1.0, impact_speed / 8.0)))
                bounce_sound.play()
                if impact_speed > MIN_BOUNCE_SPEED:
                    velocity[1] = impact_speed * BOUNCE_RESTITUTION
                else:
                    velocity[:] = 0.0
                    landed = True

        draw_scene(screen, font, position, velocity, elapsed, started, landed, bounces)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()