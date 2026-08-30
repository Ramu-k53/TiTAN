# TiTAN v2 Phase 1 Requirements

## Objective
Build the navigation skeleton. Individual modules can remain placeholders.

## Main menu
1. My Profile
2. Electrical Calculator
3. Robotics Lab
4. AI Assistant
5. Unit Converter
6. Settings
7. Exit

## Behavior
- Show the menu repeatedly until option 7.
- 1 calls `profile()`.
- 2 calls `electrical_calculator()`.
- 3 calls `robotics_lab()`.
- 4 calls `ai_assistant()`.
- 5 calls `unit_converter()`.
- 6 calls `settings()`.
- 7 prints a goodbye message and exits.
- Invalid choices display an error and continue.

Menu order is a UI decision, not a Python requirement. The displayed menu and choice mapping must agree.
