import NeuralNetwork
import MLserver
import time

# Entrenamiento de la red neuronal
NeuralNetwork.training(model_name='best_model.pth')
NeuralNetwork.print_plots()
NeuralNetwork.eval()

# Evaluar datos nuevos
print(NeuralNetwork.predict([8, 30.5, 0], rounded=True))

# while True:
#     # Ejecutar tareas pendientes
#     MLserver.consulta()
#     time.sleep(60)
