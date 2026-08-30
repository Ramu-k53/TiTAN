# TiTAN Electrical Calculator - Phase 2 Requirements

## Objective
Create an Electrical Calculator submenu within TiTAN v2.

## Entry
Selecting `2. Electrical Calculator` calls `electrical_calculator()`.

## Submenu
1. Calculate Power
2. Calculate Voltage
3. Calculate Current
4. Back to TiTAN

## Power
Inputs: voltage (V), current (A)
Processing: Power = Voltage x Current
Return the calculated power.
Example: 48 V and 10 A -> 480 W

## Voltage
Inputs: power (W), current (A)
Processing: Voltage = Power / Current
Return the calculated voltage.
Example: 480 W and 10 A -> 48 V

## Current
Inputs: power (W), voltage (V)
Processing: Current = Power / Voltage
Return the calculated current.
Example: 480 W and 48 V -> 10 A

## Invalid choice
Display an invalid-choice message and show the submenu again.

## Back
Option 4 returns to the TiTAN main menu; it does not terminate TiTAN.

## Design rule
Keep calculation responsibility separate from presentation as the project matures. Calculation functions should be reusable and return values rather than owning all user interaction.
