import random
from tqdm import tqdm
import pyglet
import sounds

n = 10000
array = [random.randint(1, 1000000) for _ in range(n)]

def bubble_sort(arr):
    length = len(arr)
    for i in tqdm(range(length), desc="Sorting"):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(array)
print(array)
song = pyglet.media.load('../../../sounds/Готов.mp3')
song.play()
pyglet.app.run()