# TiTAN Current State

## Python concepts understood
- Variables and assignment (`=`)
- `input()` and `print()`
- `if`, `elif`, `else`
- Comparisons including `>`, `>=`, `==`, `!=`
- `while` loops
- Counting up/down and loop termination
- Functions and function calls
- Parameters and arguments
- `return`
- Difference between `print()` and `return`
- Basic PEP 8 / four-space indentation

## Important function understanding
`show_header(title)` is understood as a reusable function.
The function name identifies the function; the argument provides data to the parameter.

## TiTAN v1
Completed a console menu with Profile, Age Checker, Dream Project, and Exit.

## TiTAN v2 Phase 1
Main menu target:
1. My Profile
2. Electrical Calculator
3. Robotics Lab
4. AI Assistant
5. Unit Converter
6. Settings
7. Exit

Current functions:
- `show_header(title)`
- `show_menu()`
- `profile()`
- `electrical_calculator()`
- `robotics_lab()`
- `ai_assistant()`
- `unit_converter()`
- `settings()`

The main menu uses a `while` loop and maps choices to functions.

## Immediate next task
Implement `electrical_calculator()` as:
1. Calculate Power
2. Calculate Voltage
3. Calculate Current
4. Back to TiTAN

Calculation functions should return values; surrounding code should handle interaction and display.
