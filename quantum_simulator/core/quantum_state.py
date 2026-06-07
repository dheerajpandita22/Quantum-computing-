"""
Quantum State Representation
Core module for representing and manipulating quantum states
Author: Quantum Computing Project
"""

import numpy as np
from typing import Tuple, List, Union
import math


class QuantumState:
    """
    Represents a quantum state using statevector formalism.
    
    A quantum state is represented as a complex vector of size 2^n_qubits.
    For example:
    - 1 qubit: 2 amplitudes (|0⟩, |1⟩)
    - 2 qubits: 4 amplitudes (|00⟩, |01⟩, |10⟩, |11⟩)
    - 3 qubits: 8 amplitudes (|000⟩, |001⟩, ..., |111⟩)
    
    Attributes:
        n_qubits (int): Number of qubits
        statevector (np.ndarray): Complex amplitudes [shape: (2^n_qubits,)]
    """
    
    def __init__(self, n_qubits: int):
        """
        Initialize a quantum state in the |0...0⟩ state.
        
        Args:
            n_qubits (int): Number of qubits (max ~20 for practical simulation)
        
        Raises:
            ValueError: If n_qubits < 1 or > 20
        """
        if n_qubits < 1:
            raise ValueError("n_qubits must be at least 1")
        if n_qubits > 20:
            raise ValueError("n_qubits > 20 may cause memory issues")
        
        self.n_qubits = n_qubits
        self.dim = 2 ** n_qubits
        
        # Initialize in |0...0⟩ state (all zeros)
        # This is a vector with 1.0 at index 0, and 0 elsewhere
        self.statevector = np.zeros(self.dim, dtype=complex)
        self.statevector[0] = 1.0 + 0.0j
    
    def __repr__(self) -> str:
        """String representation of quantum state."""
        return f"QuantumState({self.n_qubits} qubits)"
    
    def __str__(self) -> str:
        """Readable string of quantum state amplitudes."""
        result = f"QuantumState with {self.n_qubits} qubits:\n"
        result += "-" * 50 + "\n"
        
        for i, amplitude in enumerate(self.statevector):
            # Only show non-zero amplitudes (with small threshold)
            if abs(amplitude) > 1e-10:
                # Convert index to binary representation
                binary = format(i, f'0{self.n_qubits}b')
                
                # Format amplitude nicely
                amplitude_str = f"{amplitude:.4f}"
                if abs(amplitude.imag) > 1e-10:
                    amplitude_str = f"({amplitude.real:.4f} + {amplitude.imag:.4f}i)"
                
                # Probability
                prob = abs(amplitude) ** 2
                prob_str = f"{prob * 100:.2f}%"
                
                result += f"|{binary}⟩: {amplitude_str:>20} (P = {prob_str})\n"
        
        result += "-" * 50
        return result
    
    def is_normalized(self) -> bool:
        """
        Check if state is properly normalized.
        A valid quantum state must satisfy: ∑|αᵢ|² = 1
        """
        norm_squared = np.sum(np.abs(self.statevector) ** 2)
        return abs(norm_squared - 1.0) < 1e-10
    
    def normalize(self) -> None:
        """
        Normalize the quantum state to have unit norm.
        This ensures ∑|αᵢ|² = 1
        """
        norm = np.linalg.norm(self.statevector)
        if norm > 0:
            self.statevector /= norm
    
    def measure(self, qubit_index: int = None) -> int:
        """
        Measure one or all qubits and return result.
        
        When measuring qubit i:
        - Probability of getting 0: sum of |αⱼ|² where j has bit i = 0
        - Probability of getting 1: sum of |αⱼ|² where j has bit i = 1
        
        Args:
            qubit_index (int): Which qubit to measure. If None, measure all qubits.
        
        Returns:
            int or list: Measurement result(s) (0 or 1 for each qubit)
        
        Note:
            This function DOES NOT collapse the state (returns result without modifying state).
            Use collapse_after_measurement() if you want to update the state.
        """
        # Calculate probabilities for each basis state
        probabilities = np.abs(self.statevector) ** 2
        
        if qubit_index is None:
            # Measure all qubits: randomly select basis state
            result = np.random.choice(self.dim, p=probabilities)
            return result
        else:
            # Measure specific qubit
            if qubit_index < 0 or qubit_index >= self.n_qubits:
                raise ValueError(f"qubit_index must be 0-{self.n_qubits - 1}")
            
            prob_0 = 0.0
            prob_1 = 0.0
            
            # Calculate probability for bit position (from right, 0-indexed)
            bit_position = self.n_qubits - 1 - qubit_index
            
            for i in range(self.dim):
                # Extract bit at position bit_position
                bit_value = (i >> bit_position) & 1
                if bit_value == 0:
                    prob_0 += probabilities[i]
                else:
                    prob_1 += probabilities[i]
            
            # Choose outcome based on probabilities
            return 0 if np.random.random() < prob_0 else 1
    
    def measure_all(self, shots: int = 1000) -> dict:
        """
        Perform multiple measurements and return histogram.
        
        Args:
            shots (int): Number of measurements to perform
        
        Returns:
            dict: Histogram of results {binary_string: count}
        
        Example:
            >>> state = QuantumState(2)
            >>> state.apply_hadamard(0)  # Create superposition
            >>> results = state.measure_all(shots=1000)
            >>> # Returns something like {'00': 250, '01': 250, '10': 250, '11': 250}
        """
        results = {}
        
        # Measure multiple times
        for _ in range(shots):
            # Choose basis state according to probabilities
            probabilities = np.abs(self.statevector) ** 2
            measured_state = np.random.choice(self.dim, p=probabilities)
            
            # Convert to binary string
            binary_str = format(measured_state, f'0{self.n_qubits}b')
            
            # Increment count
            results[binary_str] = results.get(binary_str, 0) + 1
        
        return results
    
    def get_probabilities(self) -> dict:
        """
        Get probability distribution without measuring (non-destructive).
        
        Returns:
            dict: Probability of each basis state {binary_string: probability}
        """
        probabilities = {}
        amplitudes_squared = np.abs(self.statevector) ** 2
        
        for i in range(self.dim):
            if amplitudes_squared[i] > 1e-10:  # Only show non-negligible
                binary_str = format(i, f'0{self.n_qubits}b')
                probabilities[binary_str] = amplitudes_squared[i]
        
        return probabilities
    
    def apply_unitary(self, unitary: np.ndarray) -> None:
        """
        Apply a unitary matrix to the quantum state.
        This is the most general operation: |ψ'⟩ = U|ψ⟩
        
        Args:
            unitary (np.ndarray): 2D complex array of shape (2^n_qubits, 2^n_qubits)
        
        Raises:
            ValueError: If unitary shape doesn't match state dimension
        """
        if unitary.shape != (self.dim, self.dim):
            raise ValueError(f"Unitary shape {unitary.shape} doesn't match state dimension {self.dim}")
        
        # Apply: |ψ'⟩ = U|ψ⟩
        self.statevector = unitary @ self.statevector
    
    def get_fidelity(self, other: 'QuantumState') -> float:
        """
        Calculate fidelity between this state and another.
        Fidelity = |⟨ψ|φ⟩|² (ranges from 0 to 1)
        
        Args:
            other (QuantumState): Another quantum state
        
        Returns:
            float: Fidelity value between 0 and 1
        """
        if self.n_qubits != other.n_qubits:
            raise ValueError("States must have same number of qubits")
        
        # Inner product
        inner_product = np.dot(np.conj(self.statevector), other.statevector)
        
        # Fidelity
        fidelity = abs(inner_product) ** 2
        return fidelity
    
    def copy(self) -> 'QuantumState':
        """Create a deep copy of this quantum state."""
        new_state = QuantumState(self.n_qubits)
        new_state.statevector = self.statevector.copy()
        return new_state
    
    @staticmethod
    def create_superposition(n_qubits: int) -> 'QuantumState':
        """
        Create an equal superposition of all basis states.
        State: (|0...0⟩ + |0...1⟩ + ... + |1...1⟩) / √(2^n)
        
        Args:
            n_qubits (int): Number of qubits
        
        Returns:
            QuantumState: Superposition state
        """
        state = QuantumState(n_qubits)
        state.statevector = np.ones(2 ** n_qubits, dtype=complex)
        state.normalize()
        return state
    
    @staticmethod
    def create_bell_state(pair: int = 0) -> 'QuantumState':
        """
        Create a Bell state (maximally entangled 2-qubit state).
        
        Args:
            pair (int): Which Bell state (0-3)
                0: (|00⟩ + |11⟩) / √2  [Φ⁺]
                1: (|00⟩ - |11⟩) / √2  [Φ⁻]
                2: (|01⟩ + |10⟩) / √2  [Ψ⁺]
                3: (|01⟩ - |10⟩) / √2  [Ψ⁻]
        
        Returns:
            QuantumState: Bell state
        """
        state = QuantumState(2)
        
        if pair == 0:
            state.statevector = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
        elif pair == 1:
            state.statevector = np.array([1, 0, 0, -1], dtype=complex) / np.sqrt(2)
        elif pair == 2:
            state.statevector = np.array([0, 1, 1, 0], dtype=complex) / np.sqrt(2)
        elif pair == 3:
            state.statevector = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
        else:
            raise ValueError("pair must be 0-3")
        
        return state


# Test code
if __name__ == "__main__":
    print("=" * 60)
    print("Testing Quantum State Module")
    print("=" * 60)
    
    # Test 1: Basic state creation
    print("\n1. Creating a 1-qubit state (should be |0⟩):")
    state = QuantumState(1)
    print(state)
    
    # Test 2: 2-qubit superposition
    print("\n2. Creating 2-qubit equal superposition:")
    state2 = QuantumState.create_superposition(2)
    print(state2)
    
    # Test 3: Bell state
    print("\n3. Creating Bell state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2:")
    bell = QuantumState.create_bell_state(0)
    print(bell)
    
    # Test 4: Measurement
    print("\n4. Measuring Bell state (1000 shots):")
    results = bell.measure_all(shots=1000)
    for outcome, count in sorted(results.items()):
        print(f"   {outcome}: {count} times ({count/10:.1f}%)")
    
    # Test 5: Normalization check
    print("\n5. Normalization check:")
    print(f"   State 1 normalized: {state.is_normalized()}")
    print(f"   State 2 normalized: {state2.is_normalized()}")
    print(f"   Bell state normalized: {bell.is_normalized()}")
