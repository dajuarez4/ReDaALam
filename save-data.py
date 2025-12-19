import numpy as np

def parse_lammps_log(filename, outname="step_temp_toteng_press.dat"):
    steps = []
    temps = []
    totengs = []
    pressures = []

    in_table = False

    with open(filename, "r") as f:
        for line in f:
            stripped = line.strip()

            # Detect the thermo header line
            if stripped.startswith("Step") and "Temp" in stripped and "TotEng" in stripped:
                in_table = True
                continue

            # If we are inside a thermo block, parse numeric lines
            if in_table:
                parts = stripped.split()
                if len(parts) == 0:
                    in_table = False
                    continue

                # Check if first token looks like an integer step
                first = parts[0]
                if not (first.lstrip("-").isdigit()):
                    in_table = False
                    continue

                # Expect columns: Step Temp E_pair E_mol TotEng Press
                try:
                    step = int(parts[0])
                    temp = float(parts[1])
                    toteng = float(parts[4])
                    press = float(parts[5])

                    steps.append(step)
                    temps.append(temp)
                    totengs.append(toteng)
                    pressures.append(press)
                except (ValueError, IndexError):
                    in_table = False
                    continue

    # Save to file
    data = np.column_stack([steps, temps, totengs, pressures])
    header = "Step Temp TotEng Press"
    np.savetxt(outname, data, header=header)

    print(f"Parsed {len(steps)} lines. Saved to '{outname}'.")

if __name__ == "__main__":
    parse_lammps_log("log.lammps")

