import torch
import numpy as np
import pandas as pd
from torch import nn, optim
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

data = pd.read_csv('dataset.csv')

# Preprocesar los datos
dataset = data.drop('PP', axis=1).values
labels = data['PP'].values

# Crear el normalizador
scaler = StandardScaler()

# Ajustar el normalizador a los datos de entrenamiento y transformarlos
dataset = scaler.fit_transform(dataset)

# Separar los datos en entrenamiento y prueba
dataset_train, dataset_test, labels_train, labels_test = train_test_split(dataset, labels, test_size=0.1,
                                                                          random_state=2)

# Ajustar el normalizador a los datos de entrenamiento y transformarlos
dataset_train = scaler.fit_transform(dataset_train)

# Utilizar el mismo normalizador para transformar los datos de entrenamiento
dataset_train = scaler.transform(dataset_train)
dataset_test = scaler.transform(dataset_test)

# Convertir los datos a tensores
dataset_train = torch.FloatTensor(dataset_train).to('cpu')
dataset_test = torch.FloatTensor(dataset_test).to('cpu')
labels_train = torch.FloatTensor(labels_train).to('cpu')
labels_test = torch.FloatTensor(labels_test).to('cpu')

labels_train = labels_train[:, None]
labels_test = labels_test[:, None]


class RedNeuronal(nn.Module):
    def __init__(self):
        super(RedNeuronal, self).__init__()
        self.fc1 = nn.Linear(dataset_train.shape[1], 64)
        self.relu1 = nn.ReLU()
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(64, 8)
        self.relu2 = nn.ReLU()
        self.fc3 = nn.Linear(8, 1)
        self.relu3 = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, input):
        output = self.fc1(input)
        output = self.relu1(output)
        output = self.dropout(output)
        output = self.fc2(output)
        output = self.relu2(output)
        output = self.fc3(output)
        output = self.relu3(output)
        output = self.sigmoid(output)
        return output


def training(model_name='model', lr=0.0001, epochs=100000, prints=1000):
    higher_accuracy = 0
    model = RedNeuronal()
    loss_fn = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    history = pd.DataFrame()

    for epoch in range(epochs):
        predictions = model(dataset_train)
        loss = loss_fn(predictions, labels_train)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if epoch % prints == 0:
            print(f'Epoch: {epoch}, Loss: {round(loss.item(), 4)}')

        with torch.no_grad():
            predictions = model(dataset_test)
            predictions = predictions.round()
            accuracy = predictions.eq(labels_test).sum() / float(labels_test.shape[0]) * 100
            if epoch % prints == 0:
                print(f'Accuracy: {round(accuracy.item(), 4)}%\n')

        df_tmp = pd.DataFrame(data={
            'Epoch': epoch,
            'Loss': round(loss.item(), 4),
            'Accuracy': round(accuracy.item(), 4),
        }, index=[0])
        history = pd.concat([history, df_tmp], ignore_index=True)

        # Se almacena el modelo en el punto con mayor precisión
        if accuracy > higher_accuracy:
            higher_accuracy = accuracy
            history.to_csv(f'results/best_{model_name}_results.csv', index=False, header=True)
            torch.save(model.state_dict(), f'models/best_{model_name}.pth')

        if epoch % prints == 0:
            print(f'Higher accuracy: {round(higher_accuracy.item(), 4)}%\n')

    history.to_csv(f'results/{model_name}_results.csv', index=False, header=True)
    torch.save(model.state_dict(), f'models/{model_name}.pth')


def print_plots(model_name='model'):
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = pd.read_csv(f'results/{model_name}_results.csv')
    df = df.melt(id_vars=['Epoch'], value_vars=['Loss', 'Accuracy'])

    plt.figure(figsize=(12, 8))
    sns.lineplot(x='Epoch', y='value', hue='variable', data=df)
    plt.savefig(f'plots/{model_name}_plot.png')
    plt.clf()


def create_confusion_matrix(true_labels, predicted_labels):
    # Crea la matriz de confusión
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(true_labels, predicted_labels)
    return cm


def eval(model_name='model'):
    import matplotlib.pyplot as plt
    import seaborn as sns
    model = RedNeuronal()
    model.load_state_dict(torch.load(f'models/{model_name}.pth'))
    model.eval()

    with torch.no_grad():
        predictions = model(dataset_test)
        predictions = predictions.round()
        accuracy = predictions.eq(labels_test).sum() / float(labels_test.shape[0]) * 100
        print(f'Accuracy: {round(accuracy.item(), 4)}%\n')

    cm = create_confusion_matrix(labels_test, predictions)
    sns.heatmap(cm, annot=True)
    plt.savefig(f'plots/{model_name}_matrix.png')
    plt.clf()


def predict(data, model_name='model', rounded=False):
    # Carga el modelo
    model = RedNeuronal()
    model.load_state_dict(torch.load(f'models/{model_name}.pth'))
    model.eval()

    # Normaliza los datos
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)

    # Convierte los datos a tensores de PyTorch y asegúrate de que estén en el mismo dispositivo que el modelo
    data = torch.tensor(data).float().to('cpu')  # Cambia 'cpu' a 'cuda' si estás usando una GPU

    # Haz la predicción
    with torch.no_grad():
        predictions = model(data)
        if rounded:
            predictions = predictions.round()

    # Convierte las predicciones a una lista y devuélvelas
    return predictions.tolist()
