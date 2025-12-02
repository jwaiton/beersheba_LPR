import matplotlib.pyplot as plt
import numpy as np

def plot_hits(hits, bins = None, pitch = 15.55):
    # then applying transformations to convert to 'SiPM outputs'
    fig, axes = plt.subplots(1, 3, figsize=(18, 4))
    if bins is None:
        print('No binning provided, extracting from hits')
        xx = np.arange(hits.X.min(), hits.X.max() + pitch, pitch)
        yy = np.arange(hits.Y.min(), hits.Y.max() + pitch, pitch)
        zz = np.sort(hits.Z.unique())
    else:
        xx = bins[0]
        yy = bins[1]
        zz = bins[2]
    # set weights to be either hits.Q or hits.E based on what the df has 
    if 'Q' in hits:
        weight = hits.Q
    else:
        weight = hits.E
    axes[0].hist2d(hits.X, hits.Y, bins=[xx, yy], weights=weight, cmin=0.0000000001);
    axes[0].set_xlabel('X (mm)');
    axes[0].set_ylabel('Y (mm)');

    axes[1].hist2d(hits.X, hits.Z, bins=[xx, zz], weights=weight, cmin=0.0000000001);
    axes[1].set_xlabel('X (mm)');
    axes[1].set_ylabel('Z (mm)');


    axes[2].hist2d(hits.Y, hits.Z, bins=[yy, zz], weights=weight, cmin=0.0000000001);
    axes[2].set_xlabel('Y (mm)');
    axes[2].set_ylabel('Z (mm)');

    fig.suptitle('Sensors Signal', fontsize=30)