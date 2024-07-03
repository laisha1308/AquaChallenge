import NeuralNetwork
import MLserver
import time

model_name = f'best_model2'
# Entrenamiento de la red neuronal
# NeuralNetwork.training(model_name)
# NeuralNetwork.print_plots(model_name)
# NeuralNetwork.eval(model_name)

# Evaluar datos nuevos
print(NeuralNetwork.predict([1, 16.1, 1009.2, 64], model_name=model_name, rounded=True))
# while True:
#     # Ejecutar tareas pendientes
#     MLserver.consulta()
#     time.sleep(60)
