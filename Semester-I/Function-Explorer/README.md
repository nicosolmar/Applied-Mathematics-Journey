# Function Explorer

## Description

A simple Python program that evaluates a mathematical cost model for a subscription service.

The project connects a mathematical function with a computational implementation, using the function:

$$
C(x) = 5000 + 2000x
$$

where:

* \(5000\) is the fixed subscription cost.
* \(2000\) is the additional cost per movie.
* \(x\) is the number of movies.
* \(C(x)\) is the total cost.

## Mathematical model

The model represents a situation in which there is an initial fixed cost and an additional cost proportional to the number of movies selected.

For example:

$$
C(7) = 5000 + 2000(7) = 19000
$$

Therefore, selecting 7 movies produces a total cost of 19,000.

## Domain

In this model, \(x\) represents a quantity of movies. Therefore:

$$
x \in \mathbb{N}_0 = \{0,1,2,3,\ldots\}
$$

Negative values do not have a meaningful interpretation in this context.

The program therefore rejects negative inputs.

## Computational implementation

The program:

1. Requests the number of movies from the user.
2. Converts the input into an integer.
3. Verifies that the value is non-negative.
4. Evaluates the mathematical model.
5. Displays the total cost.

## Example

### Input

```text
cuantas peliculas vas a comprar: 7
```

### Output

```text
el costo total es de: 19000
```

## Concepts practiced

* Mathematical functions
* Function evaluation
* Domain and model interpretation
* Variables
* User input
* Integer data types
* Conditional statements
* Basic mathematical modeling
* Translating a mathematical model into Python

## Limitations

This is an introductory implementation. It currently evaluates only one predefined model and does not allow the user to define new functions dynamically.

## Future extensions

Possible future versions could include:

* Evaluating multiple mathematical models.
* Allowing the user to select a model.
* Graphing the function.
* Comparing different models.
* Extending the program to support more general mathematical functions.

These extensions will be considered as the necessary mathematical and computational foundations are developed.
