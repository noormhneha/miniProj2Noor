import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calc_mean_erp(trial_points, ecog_data):
    """
    Calculate the mean Event Related Potential (ERP) for each finger movement.
    
    Parameters:
    -----------
    trial_points : str
        Path to CSV file with three columns: starting_point, peak_point, finger
        Contains the indices of movement start, peak, and which finger (1-5)
    ecog_data : str
        Path to CSV file with brain signal time series data
        
    Returns:
    --------
    fingers_erp_mean : numpy.ndarray
        Matrix of shape (5, 1201) containing averaged brain response for each finger
        Rows are ordered by finger number (1, 2, 3, 4, 5)
    """
    # load trial points data (int)
    events = pd.read_csv(trial_points, dtype=int)
    
    # load data
    brain_data = pd.read_csv(ecog_data, header=None).values.flatten()
    
    # define epoch parameters
    pre_samples = 200
    post_samples = 1000
    total_samples = pre_samples + 1 + post_samples  # 1201
    
    fingers_erp_mean = np.zeros((5, total_samples))
    
    # process each finger (1 through 5)
    for finger in range(1, 6):
        # get all trials for this finger
        finger_events = events[events['finger'] == finger]
        starting_points = finger_events['starting_point'].values
        
        # collect all epochs for this finger
        epochs = []
        for start_idx in starting_points:
            # calc epoch boundaries
            epoch_start = start_idx - pre_samples
            epoch_end = start_idx + post_samples + 1  # +1 to include the endpoint
            
            # epoch is within bounds of the data?
            if epoch_start >= 0 and epoch_end <= len(brain_data):
                epoch = brain_data[epoch_start:epoch_end]
                epochs.append(epoch)
        
        # average across all trials for this finger
        if epochs:
            epochs_array = np.array(epochs)
            fingers_erp_mean[finger - 1, :] = np.mean(epochs_array, axis=0)
    
    # plot the averaged brain response for each finger
    plt.figure(figsize=(12, 8))
    time_axis = np.arange(-pre_samples, post_samples + 1)  # -200 to 1000
    
    finger_names = ['Thumb (1)', 'Index (2)', 'Middle (3)', 'Ring (4)', 'Pinky (5)']
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    
    for finger in range(5):
        plt.plot(time_axis, fingers_erp_mean[finger, :], 
                 label=finger_names[finger], color=colors[finger], linewidth=1.5)
    
    plt.axvline(x=0, color='black', linestyle='--', linewidth=1, label='Movement onset')
    plt.xlabel('Time (ms)', fontsize=12)
    plt.ylabel('Brain Signal Amplitude', fontsize=12)
    plt.title('Event Related Potentials (ERP) for Each Finger Movement', fontsize=14)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('erp_plot.png', dpi=150)
    plt.show()
    
    return fingers_erp_mean