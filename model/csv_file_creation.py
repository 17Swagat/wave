# 2
import os
import pandas as pd

import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

data = []
labels = []
for dataset_num, dir_ in enumerate(os.listdir(DATA_DIR)):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []

        x_ = []
        y_ = []

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append([dataset_num] + data_aux)
            labels.append(dir_)

# Create a pandas DataFrame from the data and labels
column_names = ['dataset'] + [f'x_{i}' for i in range(len(data[0]) // 2)] + [f'y_{i}' for i in range(len(data[0]) // 2)]
df = pd.DataFrame(data, columns=column_names)
# df['label'] = labels

# Save the DataFrame to a CSV file
df.to_csv('handlandmarks_data.csv', index=False)
