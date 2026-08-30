# TiTAN Decision Log

## D001 - Requirements-first workflow
Use Requirement -> Design/Algorithm -> Code -> Test -> Debug -> Refactor -> Git Commit.

## D002 - Keep TiTAN v2 in one file initially
Do not split into modules yet. Learn function composition first; introduce imports when modularization solves a real problem.

## D003 - Reusable header
Use `show_header(title)` instead of duplicating header code.

## D004 - Parameters and arguments
The function name identifies the function. The argument provides data to the parameter.

## D005 - Return-value design
Calculation functions should calculate and return values so callers can print, store, compare, or pass them elsewhere.

## D006 - Separate input from calculation as the project matures
Inputs may eventually come from sensors, other functions, files, databases, APIs, or modules.

## D007 - Menu order
Menu order is a UI choice, not a Python technical requirement. Mapping must match the displayed menu.

## D008 - Project memory
Do not treat one long chat as the sole project database. Important requirements, decisions, architecture, and current state belong in version-controlled documentation.
