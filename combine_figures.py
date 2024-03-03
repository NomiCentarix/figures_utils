import matplotlib.pyplot as plt
import numpy as np

def combine_figures(figures, output_path=None, dpi=300):
    """
    Plot a list of Matplotlib figures in a single figure and optionally save it to a file.

    Parameters:
    - figures: List of Matplotlib.figure.Figure objects
    - output_path: Optional. Path to save the combined figure. If None, the figure is not saved.
    - dpi: Dots per inch for saving the figure (default is 300).
    """
    # Calculate the number of rows and columns based on the number of figures
    num_figures = len(figures)
    rows = int(num_figures**0.5)
    cols = (num_figures + rows - 1) // rows

    # Create a new figure to contain all the subplots
    combined_fig, combined_axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 5))  # Adjust figsize as needed

    # Flatten the axes array if it's a multi-dimensional array
    combined_axes = combined_axes.flatten()

    # Loop through each figure and plot it in the combined figure
    for i, fig in enumerate(figures):

        # Extract image data from the figure
        img_data = np.array(fig.canvas.renderer.buffer_rgba())

        # Add the subplot to the combined figure
        combined_axes[i].imshow(img_data)
        combined_axes[i].axis('off')  # Turn off axis for each subplot

    # Adjust layout to prevent overlap of subplots
    combined_fig.tight_layout()

    # Save the figure if output_path is provided
    if output_path:
        combined_fig.savefig(output_path, dpi=dpi)

    #remove empty subplots
    idx_to_remove = list(range(rows*cols-1,num_figures-1,-1))
    for i in idx_to_remove:
        combined_fig.delaxes(combined_axes[i])

    # Show the combined figure
    plt.show()
    
