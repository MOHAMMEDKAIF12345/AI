import numpy as np

def relu(n):
 return max(0, n)

def feedforward(input_data, weights):
 node0 = relu(np.dot(input_data, weights[0]))
 node1 = relu(np.dot(input_data, weights[1]))
 node2 = relu(np.dot(np.array([node0, node1]), weights[2]))
 node3 = relu(np.dot(np.array([node0, node1]), weights[3]))
 output = relu(np.dot(np.array([node2, node3]), weights[4]))
 return node0, node1, node2, node3, output

inp = np.array([[-1, 2], [2, 2], [3, 3]])
weights = [np.array([3, 3]), np.array([1, 5]), np.array([3, 3]), np.array([1, 5]), np.array([2, -1])]

for x in inp:
 node0, node1, node2, node3, output = feedforward(x, weights)
 print(f"Input: {x}, Output: {output}")
 print("Neural Network Diagram:")
 print("Input Layer -> Hidden Layer 1 -> Hidden Layer 2 -> Output Layer")
 print("       |          |                  |                  |")
 print(f"       {x[0]:.2f}     ->   {node0:.2f}      ->   {node2:.2f}      ->   {output:.2f}")
 print(f"       {x[1]:.2f}     ->   {node1:.2f}      ->   {node3:.2f}")
print("")
