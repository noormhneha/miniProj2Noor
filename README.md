# MiniProject 2 - Event Related Potentials (ERP) Analysis

## Description
This project analyzes brain signals (ECoG data) recorded while a patient moved their fingers. It calculates and visualizes the Event Related Potential (ERP) for each finger movement.

## Files
- `fingers_erp.py` - Contains the `calc_mean_erp` function
- `main.py` - Runs the analysis
- `brain_data_channel_one.csv` - Brain signal data
- `events_file_ordered.csv` - Finger movement events (starting point, peak, finger number)

## How to Run
```
python3 main.py
```

## Output
- A 5x1201 matrix with averaged brain response for each finger
- A plot showing ERP for all 5 fingers