A derivative can be used for a function with a single input. A gradient is the same idea, just applied functions with multiple inputs. You take one derivative per input, and place them in a list (24.7041, 138.8338, etc). 

## Example
Say we have two numbers: a = 3, and b = 2, and you calculate

$f = a * b = 6$

Now if you ask, *if I nudge* $a$ *up a tiny bit, what happens to* $f$*?*

$f = 3.001 * 2 = 6.002$

Because $f$ changing by $0.002$ is the result of nudging $a$ up by $0.001$, and $\frac{0.002}{0.001} = 2$, we can say that *$f$ is $2$ times as sensitive to $a$*. We can do the same for $b$, too. If we nudge $b$ up by a tiny bit:

$f = 3 * 2.001 = 6.003$

we can see that $f$ changed by $0.003$ when $b$ was nudged by $0.001$. Because $\frac{0.003}{0.001} = 3$, we can say that *$f$ is 3 times as sensitive to $b$*.

**A gradient is just those numbers collected together. $f$ has two inputs, so it would have two results:**
- with respect to a: 2
- with respect to b: 3
If we put these numbers in a list, $(2, 3)$, that is the gradient. 

## Phrasing
"With respect to a" means that "a is the one we're nudging".
