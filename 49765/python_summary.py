Python is a high-level, interpreted, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python's design
philosophy emphasizes code readability with its notable use of significant
indentation.

Key Features:
- Easy to learn and use (simple syntax)
- Interpreted language (no compilation step, runs directly)
- Dynamically typed (no need to declare variable types)
- Extensive standard library (includes modules for various tasks)
- Cross-platform (runs on Windows, macOS, Linux, etc.)
- Supports multiple programming paradigms (object-oriented, imperative, functional)
- Large and active community support

Common Applications:
- Web Development (Django, Flask, FastAPI)
- Data Science & Machine Learning (NumPy, Pandas, scikit-learn, TensorFlow, PyTorch)
- Artificial Intelligence
- Automation & Scripting
- Scientific Computing
- Game Development (less common, but possible)
"""

# Simple Python example: A function to calculate the nth Fibonacci number
def fibonacci(n):
    """Calculates the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print the first 10 Fibonacci numbers
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"Fibonacci({i}): {fibonacci(i)}")

# Another simple example: List comprehension
squares = [x**2 for x in range(10)]
print(f"\nSquares of numbers from 0-9: {squares}")
```
