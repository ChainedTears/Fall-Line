The derivative of a function basically asks, *what is the slope of the function at this specific point?*, or, *How much is this function changing by if I nudge up a specific variable?* So, as an example:

```python
def f(x):
	return 3*x**2 + 2*x + 5
```

Since the derivative can be defined as 

$f'(x) = \lim_{h \to 0} \frac{f(x) - f(x-h)}{h}$

with the standard of $h$ approaching zero; the derivative of $f(x)$ can be expressed by setting $h$ to be a number slightly above or below $x$.

```python
x = 5
h = 0.00001
d = (f(x) - f(x - h))/(h)
```

Now what happens if there are multiple variables in the equation?

```python
a = 2
b = -3
c = 10
d1 = a*b + c 
a += h
d2 = a*b + c
slope = (d2 - d1)/h
```

In this case, the slope would represent the derivative of function `d1` with respect to `a`, or, the rate of which `d1` would increase as we scale `c`.


 