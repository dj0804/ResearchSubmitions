from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def deutsch_algorithm(oracle):
    """
    Implements Deutsch's Algorithm using a given oracle.
    The oracle represents a function f(x) which is either constant or balanced.
    """
    circuit = QuantumCircuit(2, 1)  # Two qubits, one classical bit for measurement
    
    # Step 1: Prepare the qubits
    circuit.x(1)  # Set the second qubit to |1⟩
    circuit.h([0, 1])  # Put both qubits in superposition
    
    # Step 2: Apply the oracle (encodes the function f)
    circuit.append(oracle.to_instruction(), [0, 1])
    
    # Step 3: Apply Hadamard to the first qubit again
    circuit.h(0)
    
    # Step 4: Measure the first qubit
    circuit.measure(0, 0)
    
    return circuit

# Example: Creating an oracle for a balanced function (XOR function)
def balanced_oracle():
    oracle = QuantumCircuit(2)
    oracle.cx(0, 1)  # Controlled-X gate (CNOT), flips target based on control
    return oracle

# Run Deutsch’s Algorithm with a balanced function
oracle = balanced_oracle()
qc = deutsch_algorithm(oracle)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

print("Measurement Results:", counts)
qc.draw()
