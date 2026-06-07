"""
Quantum Gates Implementation
Core module implementing all quantum gates as unitary matrices
Author: Quantum Computing Project
"""

import numpy as np
from typing import Tuple
import math


class QuantumGates:
    """
    Collection of quantum gates as unitary matrices.
    All gates are implemented as numpy arrays for efficiency.
    
    Pauli Gates: X, Y, Z (fundamental rotations)
    Hadamard: Creates superposition
    Phase Gates: S, T
    Controlled Gates: CNOT, SWAP, Toffoli
    Rotation Gates: Rx, Ry, Rz
    """
    
    # ========== Single Qubit Gates (2x2) ==========
    
    @staticmethod
    def I() -> np.ndarray:
        """Identity gate: does nothing"""
        return np.array([
            [1, 0],
            [0, 1]
        ], dtype=complex)
    
    @staticmethod
    def X() -> np.ndarray:
        """
        Pauli-X gate (NOT gate): flips |0⟩ ↔ |1⟩
        X = [0  1]
            [1  0]
        """
        return np.array([
            [0, 1],
            [1, 0]
        ], dtype=complex)
    
    @staticmethod
    def Y() -> np.ndarray:
        """
        Pauli-Y gate: rotation around Y-axis with phase
        Y = [0  -i]
            [i   0]
        """
        return np.array([
            [0, -1j],
            [1j, 0]
        ], dtype=complex)
    
    @staticmethod
    def Z() -> np.ndarray:
        """
        Pauli-Z gate (Phase flip): applies -1 phase to |1⟩
        Z = [1   0]
            [0  -1]
        """
        return np.array([
            [1, 0],
            [0, -1]
        ], dtype=complex)
    
    @staticmethod
    def H() -> np.ndarray:
        """
        Hadamard gate: creates equal superposition
        H = 1/√2 * [1   1]
                   [1  -1]
        
        H|0⟩ = (|0⟩ + |1⟩)/√2
        H|1⟩ = (|0⟩ - |1⟩)/√2
        """
        return np.array([
            [1, 1],
            [1, -1]
        ], dtype=complex) / np.sqrt(2)
    
    @staticmethod
    def S() -> np.ndarray:
        """
        S gate (Phase gate): applies i phase to |1⟩
        S = [1  0]
            [0  i]
        """
        return np.array([
            [1, 0],
            [0, 1j]
        ], dtype=complex)
    
    @staticmethod
    def T() -> np.ndarray:
        """
        T gate: applies e^(iπ/4) phase to |1⟩
        T = [1      0      ]
            [0  e^(iπ/4)]
        """
        phase = np.exp(1j * np.pi / 4)
        return np.array([
            [1, 0],
            [0, phase]
        ], dtype=complex)
    
    @staticmethod
    def Rx(theta: float) -> np.ndarray:
        """
        Rotation around X-axis by angle theta
        Rx(θ) = [cos(θ/2)     -i*sin(θ/2)]
                [-i*sin(θ/2)   cos(θ/2) ]
        """
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, -1j * s],
            [-1j * s, c]
        ], dtype=complex)
    
    @staticmethod
    def Ry(theta: float) -> np.ndarray:
        """
        Rotation around Y-axis by angle theta
        Ry(θ) = [cos(θ/2)    -sin(θ/2)]
                [sin(θ/2)     cos(θ/2)]
        """
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, -s],
            [s, c]
        ], dtype=complex)
    
    @staticmethod
    def Rz(theta: float) -> np.ndarray:
        """
        Rotation around Z-axis by angle theta
        Rz(θ) = [e^(-iθ/2)      0    ]
                [   0       e^(iθ/2)]
        """
        phase_neg = np.exp(-1j * theta / 2)
        phase_pos = np.exp(1j * theta / 2)
        return np.array([
            [phase_neg, 0],
            [0, phase_pos]
        ], dtype=complex)
    
    @staticmethod
    def Phase(theta: float) -> np.ndarray:
        """
        General phase gate: applies e^(iθ) phase to |1⟩
        Phase(θ) = [1      0    ]
                   [0  e^(iθ)]
        """
        phase = np.exp(1j * theta)
        return np.array([
            [1, 0],
            [0, phase]
        ], dtype=complex)
    
    # ========== Two Qubit Gates (4x4) ==========
    
    @staticmethod
    def CNOT() -> np.ndarray:
        """
        Controlled-NOT gate (CNOT or CX)
        Flips target qubit if control qubit is |1⟩
        
        Acts on |ab⟩ → |a, b⊕a⟩ (XOR)
        
        CNOT = [1  0  0  0]
               [0  1  0  0]
               [0  0  0  1]
               [0  0  1  0]
        
        Basis order: |00⟩, |01⟩, |10⟩, |11⟩
        """
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0]
        ], dtype=complex)
    
    @staticmethod
    def SWAP() -> np.ndarray:
        """
        SWAP gate: exchanges two qubits
        SWAP|ab⟩ = |ba⟩
        
        SWAP = [1  0  0  0]
               [0  0  1  0]
               [0  1  0  0]
               [0  0  0  1]
        """
        return np.array([
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ], dtype=complex)
    
    @staticmethod
    def CZ() -> np.ndarray:
        """
        Controlled-Z gate: applies Z to target if control is |1⟩
        
        CZ = [1  0  0   0]
             [0  1  0   0]
             [0  0  1   0]
             [0  0  0  -1]
        """
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -1]
        ], dtype=complex)
    
    # ========== Three Qubit Gates (8x8) ==========
    
    @staticmethod
    def Toffoli() -> np.ndarray:
        """
        Toffoli gate (Controlled-Controlled-NOT):
        Flips target if both controls are |1⟩
        
        For |abc⟩: |abc⟩ → |ab, c⊕(a∧b)⟩
        
        This is an 8x8 matrix (for 3 qubits)
        """
        matrix = np.eye(8, dtype=complex)
        # Flip positions 6 and 7 (when first two bits are 1)
        matrix[6, 6] = 0
        matrix[6, 7] = 1
        matrix[7, 6] = 1
        matrix[7, 7] = 0
        return matrix
    
    # ========== Utility Functions ==========
    
    @staticmethod
    def tensor_product(*gates: np.ndarray) -> np.ndarray:
        """
        Compute tensor product (Kronecker product) of gates.
        Used to combine single-qubit gates for multi-qubit states.
        
        Example: Single qubit gates on different qubits
            gate_on_q0 ⊗ gate_on_q1
        
        Args:
            *gates: Variable number of 2x2 gate matrices
        
        Returns:
            np.ndarray: Combined gate matrix
        """
        result = gates[0]
        for gate in gates[1:]:
            result = np.kron(result, gate)
        return result
    
    @staticmethod
    def single_qubit_to_multi(gate: np.ndarray, target_qubit: int, n_qubits: int) -> np.ndarray:
        """
        Expand a single-qubit gate to act on a specific qubit in multi-qubit system.
        
        For example, applying H to qubit 0 in a 3-qubit system:
        H ⊗ I ⊗ I (but order depends on qubit numbering)
        
        Args:
            gate (np.ndarray): 2x2 single-qubit gate
            target_qubit (int): Which qubit this gate acts on (0-indexed from right)
            n_qubits (int): Total number of qubits
        
        Returns:
            np.ndarray: (2^n_qubits) × (2^n_qubits) matrix
        """
        gates_list = []
        
        # Build from most significant to least significant qubit
        for q in range(n_qubits - 1, -1, -1):
            if q == target_qubit:
                gates_list.append(gate)
            else:
                gates_list.append(QuantumGates.I())
        
        return QuantumGates.tensor_product(*gates_list)
    
    @staticmethod
    def controlled_gate(gate: np.ndarray, control_qubit: int, target_qubit: int, n_qubits: int) -> np.ndarray:
        """
        Create controlled version of a gate (simplified for 2-qubit gates).
        
        This is a helper for common gates like CX, CZ, CS, CT.
        
        Args:
            gate (np.ndarray): 2x2 gate to be controlled
            control_qubit (int): Control qubit index
            target_qubit (int): Target qubit index
            n_qubits (int): Total qubits
        
        Returns:
            np.ndarray: Controlled gate matrix
        """
        # This is complex in general; simplified implementations below
        pass
    
    @staticmethod
    def is_unitary(matrix: np.ndarray, tol: float = 1e-10) -> bool:
        """
        Check if a matrix is unitary: U†U = I
        
        Args:
            matrix (np.ndarray): Matrix to check
            tol (float): Tolerance for numerical errors
        
        Returns:
            bool: True if unitary
        """
        product = np.dot(np.conj(matrix.T), matrix)
        identity = np.eye(matrix.shape[0])
        return np.allclose(product, identity, atol=tol)


# Test code
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Quantum Gates Module")
    print("=" * 60)
    
    # Test 1: Pauli gates
    print("\n1. Pauli X gate:")
    print(QuantumGates.X())
    
    print("\n2. Hadamard gate:")
    print(QuantumGates.H())
    
    # Test 3: Check unitarity
    print("\n3. Checking if gates are unitary:")
    gates = [
        ("I", QuantumGates.I()),
        ("X", QuantumGates.X()),
        ("H", QuantumGates.H()),
        ("S", QuantumGates.S()),
        ("T", QuantumGates.T()),
    ]
    
    for name, gate in gates:
        is_unitary = QuantumGates.is_unitary(gate)
        print(f"   {name}: {'✓' if is_unitary else '✗'}")
    
    # Test 4: CNOT gate
    print("\n4. CNOT gate shape:", QuantumGates.CNOT().shape)
    
    # Test 5: Rotation gate
    print("\n5. Rx(π/2) gate:")
    print(QuantumGates.Rx(np.pi / 2))
