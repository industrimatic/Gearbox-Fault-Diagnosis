import pandas as pd
import numpy as np
import pywt
import torch
from model.model import ResNet

model = ResNet()
model.eval()
model.load_state_dict(torch.load(r'weight\2026_4_23\epoch20_9_ac100.pth'))
wavename = 'cmor1.5-1.0'
scales = np.geomspace(2, 256, num=256)

label_list = ['Health', 'Chipped', 'Miss', 'Root', 'Surface']

df = pd.read_csv(r'dataset\gearset\Health_30_2.csv', sep='\t', skiprows=16, header=None)
serial_datas = df.dropna(axis=1, how='all').values[0:256, :]

img_list = []
for i in range(8):

    coeffs, _ = pywt.cwt(serial_datas[:, i], scales, wavename)
    amp = np.abs(coeffs)

    ch_min, ch_max = amp.min(), amp.max()
    if ch_max > ch_min:
        img = (amp - ch_min) / (ch_max - ch_min)
    else:
        img = np.zeros_like(amp)

    img_list.append(img)

data_tensor = torch.tensor(np.stack(img_list, axis=0), dtype=torch.float32)
data_tensor = data_tensor.reshape(1, 8, 256, 256)

with torch.no_grad():
    predicted_label = model(data_tensor)
    _, result = torch.max(predicted_label, axis=1)


print(label_list[result.item()])
