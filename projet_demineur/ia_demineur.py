import numpy as np
import random
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D
from keras.optimizers import Adam

def create_model(input_shape):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def generate_board(size, num_mines):
    board = np.zeros((size, size), dtype=int)
    mines = random.sample(range(size * size), num_mines)
    for mine in mines:
        x, y = divmod(mine, size)
        board[x, y] = 1
    return board

def get_neighbors(x, y, size):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and (dx != 0 or dy != 0):
                neighbors.append((nx, ny))
    return neighbors

def reveal(board, x, y, size):
    revealed = np.zeros((size, size), dtype=int)
    revealed[x, y] = 1
    if board[x, y] == 0:
        for nx, ny in get_neighbors(x, y, size):
            if revealed[nx, ny] == 0:
                reveal(board, nx, ny, size)
    return revealed

def play_game(model, board, size, num_mines):
    revealed = np.zeros((size, size), dtype=int)
    scores = [0, 0]
    player = 0
    while np.sum(revealed) < size * size - num_mines:
        x, y = -1, -1
        max_prob = -1
        for i in range(size):
            for j in range(size):
                if revealed[i, j] == 0:
                    input_data = np.stack((board, revealed), axis=-1)
                    prob = model.predict(input_data[np.newaxis, ...])[0, 0]
                    if prob > max_prob:
                        max_prob = prob
                        x, y = i, j
        revealed = reveal(board, x, y, size)
        if board[x, y] == 1:
            scores[player] += 1
            revealed[x, y] = 0
        else:
            player = 1 - player
    return scores

size = 10
num_mines = 20
input_shape = (size, size, 2)
model = create_model(input_shape)
board = generate_board(size, num_mines)
scores = play_game(model, board, size, num_mines)
print("Scores des joueurs:", scores)
