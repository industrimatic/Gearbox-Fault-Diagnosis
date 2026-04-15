import torch
import matplotlib.pyplot as plt
import seaborn as sns
from time import time
from sklearn.metrics import confusion_matrix
from dataloader.dataloader import get_seu_dataloaders
from model.model import ResNet

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATASET_PATH = './dataset/gearset/'
WEIGHT_PATH = './weight/model1_epoch10_ac99_8.pth'
CLASS_NAME = ['Health', 'Chipped', 'Miss', 'Root', 'Surface']

model = ResNet()
model.load_state_dict(torch.load(WEIGHT_PATH))
model.to(DEVICE)
model.eval()


def plot_confusion_matrix(true_labels: list,
                          predicted_labels: list,
                          class_names: list,
                          start_time: int,
                          end_time: int,):

    matrix = confusion_matrix(true_labels, predicted_labels)

    plt.figure(figsize=(8, 6))

    # annot=True 表示在格子中显示具体数值，fmt='d' 表示显示整数，cmap 设置颜色主题
    sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)

    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel(f'Predicted Label | From {start_time}s to {end_time}s')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    start_time = time()
    val_start_time = 20
    val_end_time = 100
    _, _, val_loader = get_seu_dataloaders(data_dir=DATASET_PATH, need_val_dataset=True,
                                           val_start_time=val_start_time, val_end_time=val_end_time)
    all_iteration = len(val_loader)
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for iteration_index, (x_data, y_data) in enumerate(val_loader):
            x_data = x_data.to(DEVICE)
            y_data = y_data.to(DEVICE)

            outputs = model(x_data)
            _, preds = torch.max(outputs, dim=1)

            all_preds.extend(preds.tolist())
            all_labels.extend(y_data.tolist())
            if iteration_index % 5 == 4:
                print(f'All: {all_iteration} Now: {iteration_index+1}|Cost Time:{time()-start_time:.2f}s')

    plot_confusion_matrix(all_labels, all_preds, CLASS_NAME, val_start_time, val_end_time)
