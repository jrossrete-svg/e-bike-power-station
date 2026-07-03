# 3) Detailed Picture Assembly Guide

Use this as a shot-by-shot build script. For each step, capture the listed photos and place them in `/home/runner/work/e-bike-power-station/e-bike-power-station/assets/images/`.

---

## Photo Naming Convention
Use sequential filenames so your build log is easy to follow:
- `01_chassis_layout_overview.jpg`
- `02_battery_cradle_mount.jpg`
- `03_inverter_converter_mount.jpg`
- ...

---

## Step 1 — Chassis Layout & Component Mounting

### Goal
Mount the battery cradle, inverter, and DC-DC converter on the internal aluminum plate with safe spacing.

### Photos to Capture
1. **Full top-down layout** before drilling (all major components placed)
   - Suggested file: `01_chassis_layout_overview.jpg`
2. **Battery cradle bolted down** with hardware visible
   - Suggested file: `02_battery_cradle_mount.jpg`
3. **Inverter and converter mounted** with standoffs/insulation shown
   - Suggested file: `03_inverter_converter_mount.jpg`

### What the photo should clearly show
- Clearance between modules and plate edges
- Non-conductive stand-off/insulation under electronics
- Fastener quality and orientation

---

## Step 2 — Faceplate Machining & External Hardware

### Goal
Prepare and install front-panel UI and output hardware.

### Photos to Capture
4. **Faceplate marked with cut layout** (screen, switches, USB, DC ports)
   - Suggested file: `04_faceplate_layout_marks.jpg`
5. **Cut panel openings and de-burred edges**
   - Suggested file: `05_faceplate_cutouts.jpg`
6. **Grommets + handle installed**
   - Suggested file: `06_grommets_handle_install.jpg`

### What the photo should clearly show
- Opening alignment and spacing
- Rubber grommet protection in pass-through holes
- Carry handle mounting symmetry and hardware backing

---

## Step 3 — Main Power Trunk & Safety Chain

### Goal
Build the protected high-current path from battery to distribution.

### Wiring Sequence
1. Battery positive -> 30A ANL fuse holder (8 AWG red)
2. Fuse output -> master disconnect input (8 AWG)
3. Master disconnect output -> positive bus bar
4. Battery negative -> smart shunt -> negative bus bar

### Photos to Capture
7. **Fuse holder wiring close-up**
   - Suggested file: `07_fuse_holder_wiring.jpg`
8. **Master disconnect wiring and labeling**
   - Suggested file: `08_master_disconnect_wiring.jpg`
9. **Bus bar + shunt routing overview**
   - Suggested file: `09_busbar_shunt_layout.jpg`

### What the photo should clearly show
- Correct order of safety devices
- Lug terminations and strain relief
- Polarity labeling at each major node

---

## Step 4 — Output Zone Distribution

### Goal
Distribute 48V and 12V branches to controlled output zones.

### Photos to Capture
10. **Zone switches wired (AC/DC/USB)**
    - Suggested file: `10_zone_switch_wiring.jpg`
11. **48V branch lines from bus bars**
    - Suggested file: `11_48v_branch_distribution.jpg`
12. **12V output harness to XT60/Anderson/cigarette/barrel**
    - Suggested file: `12_12v_output_harness.jpg`

### What the photo should clearly show
- Parallel branch structure from bus bars
- Switch placement and zone grouping
- Appropriate gauge for 12V output harness

---

## Step 5 — Grounding, Isolation, and First Boot

### Goal
Validate electrical safety before final enclosure closure.

### Photos to Capture
13. **Inverter ground bond to enclosure**
    - Suggested file: `13_ground_bond_point.jpg`
14. **Multimeter continuity/isolation test in progress**
    - Suggested file: `14_continuity_test.jpg`
15. **Final internal plate inserted + front/back panels closed**
    - Suggested file: `15_final_enclosure_assembly.jpg`

### What the photo should clearly show
- Ground wire terminal and bare metal bond point
- Meter mode and probe points during checks
- Clean cable routing before first power-on

---

## Safety Checklist (Pre-Flight)
- [ ] No positive line has continuity to chassis
- [ ] Negative path passes through shunt as designed
- [ ] Main fuse installed and correctly rated (30A ANL)
- [ ] Master disconnect functional
- [ ] All pass-throughs protected with grommets
- [ ] Inverter chassis ground bonded to enclosure
- [ ] Expected total load planned below 1500W

---

## Suggested Build Log Entry Template
Use this template below each photo set:

- **Step:**
- **Date:**
- **What was installed:**
- **Wire gauge used:**
- **Test performed:**
- **Result:**
- **Next action:**

