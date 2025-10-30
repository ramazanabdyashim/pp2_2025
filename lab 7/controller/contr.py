import pygame
import os
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100, 100))

current = 0
tracks = []

def load_tracks(path):
    global tracks
    tracks = []
    for f in os.listdir(path):
        if f.endswith('.mp3'):
            track_path = os.path.join(path, f)
            tracks.append(track_path)
    print(f"Загруженные треки: {tracks}")

def play_track(track_name):
    pygame.mixer.music.load(track_name)
    pygame.mixer.music.play()
    print(f"Играет {track_name}")

def stop_track():
    pygame.mixer.music.stop()
    print("Музыка остановлена")

def next_track():
    global current
    current += 1
    if current >= len(tracks):
        current = 0
    play_track(tracks[current])

def previous_track():
    global current
    current -= 1
    if current < 0:
        current = len(tracks) - 1
    play_track(tracks[current])

load_tracks(r'C:\\Users\\ramaz\\Desktop\\lab 7\\controller\\music')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if not pygame.mixer.music.get_busy():
                    play_track(tracks[current])
                else:
                    print("Музыка уже играет")
            elif event.key == pygame.K_s:
                stop_track()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                previous_track()
            elif event.key == pygame.K_q:
                pygame.quit()
                exit()
    
    time.sleep(0.1)
