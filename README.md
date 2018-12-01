# Genetic Algorithms with Python

Not optimized. Made for educational purposes. 

The script reads 6 values from STDIN: 

- Amount of populations
- K value of elitism
- Amount of epochs
- Selection threshold
- Crossover threshold
- Mutation threshold

The fitness evaluator is a function defined as :

```python3
def f(x,y):
  return -(x * sin(x)**2 * cos(x)**3 + (y * sin(y)**2 * cos(y)**3))
```

This function can be replaced with any other fitness evaluator function.  

The files `test.in` and `test.out` are examples of input and output.

The population size is hardcoded to 60.

The script will be refactored in the future so it's easier to understand and more flexible.
