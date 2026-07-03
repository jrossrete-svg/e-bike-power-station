# 2) Schematics & Power Calculations

## Power Ceiling
- Formula: `Power (W) = Voltage (V) × Current (A)`
- Nominal system voltage: 51.2V
- Main fuse: 30A ANL
- Maximum protected draw: `51.2 × 30 = 1536W`
- Engineering cap: **1500W total combined load**

## Main Trunk Wiring (High-Level)
1. Battery positive -> 30A ANL fuse input
2. Fuse output -> master disconnect input
3. Master disconnect output -> positive bus bar
4. Battery negative -> smart shunt -> negative bus bar

## Branch Distribution
- Inverter input fed from 48V bus (AC zone switch controlled)
- 48V->12V converter fed from 48V bus (DC zone switch controlled)
- USB module fed from designated zone switch
- 12V converter output routed to XT60, Anderson, cigarette, and barrel outputs

## Grounding Requirements
- Inverter ground terminal bonded to bare metal enclosure
- No positive conductor must contact the aluminum chassis
- Verify continuity and isolation before first power-on
