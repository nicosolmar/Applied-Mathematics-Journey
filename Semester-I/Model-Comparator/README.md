# Model Comparator

## Description

A Python program that compares two mathematical cost models and determines which option is more economical for a given number of orders.

The project uses the models:

$$
A(x) = 5000 + 2000x
$$

$$
B(x) = 10000 + 1000x
$$

where \(x\) represents the number of orders.

The program evaluates both models and determines which option has the lower cost.

## Mathematical model

### Option A

$$
A(x) = 5000 + 2000x
$$

Option A has a lower initial cost but a higher cost per order.

### Option B

$$
B(x) = 10000 + 1000x
$$

Option B has a higher initial cost but a lower cost per order.

This creates a trade-off: the better option depends on the value of \(x\).

## Equilibrium point

To determine when both options have the same cost:

$$
A(x) = B(x)
$$

$$
5000 + 2000x = 10000 + 1000x
$$

$$
1000x = 5000
$$

$$
x = 5
$$

Therefore:

* If \(x < 5\), **Option A** is cheaper.
* If \(x = 5\), both options have the same cost.
* If \(x > 5\), **Option B** is cheaper.

The value \(x=5\) is the equilibrium point of the two models.

## Computational implementation

The program:

1. Requests a non-negative number of orders.
2. Validates the input.
3. Calculates the cost of both options.
4. Compares the two results.
5. Reports the cheaper option.
6. If both costs are equal, allows the user to choose between the two options.

## Example

For:

$$
x=2
$$

we obtain:

$$
A(2)=5000+2000(2)=9000
$$

$$
B(2)=10000+1000(2)=12000
$$

Therefore, Option A is cheaper.

For:

$$
x=10
$$

we obtain:

$$
A(10)=25000
$$

$$
B(10)=20000
$$

Therefore, Option B is cheaper.

## Concepts practiced

* Mathematical functions
* Mathematical models
* Function evaluation
* Comparison of functions
* Equilibrium points
* Domain restrictions
* Conditional statements
* `while` loops
* Input validation
* Decision rules
* Translating mathematical reasoning into an algorithm
* Python implementation

## Limitations

The current version requires the user to provide a specific value of \(x\).

It does not automatically determine the equilibrium point from arbitrary functions; the value \(x=5\) was obtained through mathematical analysis before implementing the program.

The models are also fixed rather than being entered dynamically by the user.

## Future extensions

Possible future versions could:

* Calculate the equilibrium point automatically.
* Accept different mathematical models.
* C
