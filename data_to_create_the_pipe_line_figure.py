import matplotlib.pyplot as plt
import numpy as np
import colorednoise as cn


def plot_test(x_,y_,color_x='C0',color_y='C1',linewidth=1,alpha_x=1,alpha_y=1):
  '''
  Plot two time series in sequence
  '''
  empty = np.empty_like(x_)
  empty[:] = np.nan
  y2 = np.append(empty,y_)
  plt.plot(x_,label='Input' ,color = color_x,linewidth=linewidth,alpha = alpha_x)
  plt.plot(y2,label='Target',color = color_y,linewidth=linewidth,alpha = alpha_y)


# Define the parameters
beta = 2
n_points = 2**8
n_display = n_points//3

# Generate 4 time series with beta = 2
# series = [cn.powerlaw_psd_gaussian(beta, n_points) for _ in range(4)]
# np.save('data/data_to_create_the_pipe_line_figure.npy',series)
# # Load 4 time series
series = np.load('data/data_to_create_the_pipe_line_figure.npy')

  
for i in range(len(series)):
    plt.figure(figsize=(6, 3), facecolor='none')  # No background
    plot_test(series[i][:n_display], series[i][n_display:], color_x='darkred', color_y='red', linewidth=5,alpha_y=1)
    plt.axis('off')  # Turn off axes
    plt.show()
    
for i in range(len(series)):

    plt.figure(figsize=(6, 3), facecolor='none')  # No background
    plot_test(series[i][:n_display], series[i][n_display:], color_x='darkred', color_y='red', linewidth=5,alpha_y=0)
    plt.axis('off')  # Turn off axes
    plt.show()

    # Second plot without background and axes
    plt.figure(figsize=(6, 3), facecolor='none')  # No background
    plot_test(series[i][:n_display], series[i][n_display:], color_x='darkred', color_y='red', linewidth=5,alpha_x=0)
    plt.axis('off')  # Turn off axes
    plt.show()


