# TiTAN Architecture

## Current learning architecture
Keep TiTAN v2 in one Python file initially.

Conceptual hierarchy:

TiTAN Main Menu
- Profile
- Electrical Calculator
  - Power
  - Voltage
  - Current
- Robotics Lab
- AI Assistant
- Unit Converter
- Settings

## Responsibility model
`show_header(title)`: standard header display.

`show_menu()`: main menu display.

`profile()`: profile workflow.

`electrical_calculator()`: electrical submenu and coordination.

`calculate_power(...)`: calculate and return power.

`calculate_voltage(...)`: calculate and return voltage.

`calculate_current(...)`: calculate and return current.

Placeholder modules: robotics, AI assistant, unit converter, settings.

## Future modular architecture
When the project becomes sufficiently large, split related functions into files such as:
- `main.py`
- `ui.py`
- `profile.py`
- `electrical.py`
- `robotics.py`
- `ai.py`
- `converter.py`
- `settings.py`

Introduce `import` at that stage.
