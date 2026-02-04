from fingers_erp import calc_mean_erp

# file paths for the input data
trial_points = "events_file_ordered.csv"
ecog_data = "brain_data_channel_one.csv"

# calculate 
fingers_erp_mean = calc_mean_erp(trial_points, ecog_data)

print(f"Output matrix shape: {fingers_erp_mean.shape}")
print(f"Expected shape: (5, 1201)")

print("\nMean amplitude for each finger:")
for i in range(5):
    print(f"  Finger {i+1}: {fingers_erp_mean[i, :].mean():.2f}")