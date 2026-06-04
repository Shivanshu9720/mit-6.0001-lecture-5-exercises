# mit-6.0001-lecture-5-exercises

Solutions to all coding exercises, projects, and homework assignments covered in Lecture 5 of MIT's 6.0001 Introduction to Computer Science course taught by Professor Ana Bell.

## 📝 Overview
* All projects cover **Floating-Point Representation**, **Approximation Methods**, and **Bisection Search**.
* In this section, we explore how computers store integers and fractions as **Binary (`0` and `1`)** data in memory.
* We move away from simple sequential Guess-and-Check to more optimized search algorithms.
* These algorithms drastically speed up execution time and handle complex floating-point calculations with precision.

## 🎯 Key Concepts Learned
* **Binary Architecture:** How integers and floating fractions map into memory bits.
* **Epsilon & Step Size:** Handling floating-point imprecision using the Approximation method.
* **Logarithmic Efficiency:** Dividing the search space in half with Bisection Search `O(log N)`.

---


## 📌 Project 1: Decimal Integer to Binary Converter (`lec5_p1_int-binary.py`)

* **⚙️ Work:** Converts any standard base-10 decimal integer (both positive and negative) into its exact base-2 binary string using successive division.
* **🚨 The Bug (Negative Numbers):** Without a flag, negative inputs cause errors in loop bounds, and printing directly would duplicate or break the output formatting.
* **💡 The Solution:** 
  1. **Boolean Flag:** Used a state tracking flag (`flag = True`) to safely process the absolute value (`abs(num)`) of negative numbers.
  2. **Successive Division:** Implemented a `while` loop that captures remainders using `num % 2` and shifts bits down using integer division `num // 2`.
  3. **String Concatenation:** Pre-pended strings (`str(num%2) + result`) to automatically keep the binary order correct.
  4. **Output Restoration:** Re-applied the negative sign (`'-' + result`) at the very end only if
     
 
 ## 📌 Project 2: Floating-Point to Binary Converter (`lec5_p2_float_to_binary.py`)

* **⚙️ Work:** Converts fractional decimal numbers (floats) into their exact binary representations using power-of-2 scaling.
* **🚨 The Challenge:** Computers cannot directly run successive division on fractions because the remainder logic breaks down for numbers behind the decimal point.
* **💡 The Solution:** 
  1. **Dynamic Scaling:** Used a `while` loop to find a power `p` where multiplying the float by `2**p` shifts the decimal out completely, turning it into a whole integer.
  2. **Core Binary Conversion:** Re-used the successive integer division algorithm (`num // 2`) on the newly scaled whole number.
  3. **Zero Padding:** Added a `for` loop to append leading zeros (`'0' + result`) if the binary string length was shorter than the power scale `p`.
  4. **String Slicing:** Utilized Python string slicing (`result[0:-p] + '.' + result[-p:]`) to precisely shift the decimal point back to its mathematically correct position.
     

## 📌 Project 3: Square Root Approximation ("Good Enough" Search) (`lec5_p3_approximation.py`)

* **⚙️ Work:** Finds an approximate square root of an integer using linear incremental steps instead of hunting for an exact whole number.
* **🚨 The Challenge:** Floating-point numbers cannot always map onto perfect integer roots. If you increment sequentially by whole numbers, the script will step right past fractional roots (like $\sqrt{2}$) and fall into an infinite loop.
* **💡 Solution (The Approximation Architecture):**
  1. **Epsilon (`epsilon`):** Introduced a user-defined mathematical margin of error. It defines the acceptable threshold (e.g., `0.01`) within which a fractional answer is considered "good enough."
  2. **Bounded Search Loop:** Implemented a fine-tuned `while` loop driven by two distinct logical boundaries:
     * `abs(guess**2 - x) >= epsilon`: Tracks the distance from the target value. The loop exits precisely when the guess falls safely inside the Epsilon bounds.
     * `guess**2 <= x`: Acts as an anti-overshoot safeguard to stop the loop instantly if the increments skip past the target area.
  3. **Performance Metrics:** Tracks total compute steps using `num_guess` and outputs clear fallback metrics (`Failed on square root`) if the step size skips the Epsilon target window completely.
