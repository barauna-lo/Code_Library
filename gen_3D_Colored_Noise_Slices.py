import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.fftpack import fftn, ifftn

def colored_noise(shape, beta):
    random_noise = np.random.normal(size=shape)
    kx = np.fft.fftfreq(shape[0]).reshape(-1, 1, 1)
    ky = np.fft.fftfreq(shape[1]).reshape(1, -1, 1)
    kz = np.fft.fftfreq(shape[2]).reshape(1, 1, -1)
    freq_grid = np.sqrt(kx**2 + ky**2 + kz**2)
    freq_grid[0, 0, 0] = 1  # Avoid division by zero
    spectrum = fftn(random_noise) * np.power(freq_grid, -beta / 2.0)
    colored = np.real(ifftn(spectrum))
    return colored
# Generate data    
betas = np.linspace(1, 5, 5)
noise_cubes = []
for i, beta in enumerate(betas):
    noise_cubes.append(colored_noise((64, 64, 64), beta))


selected_slice = 15  # Change this value to select a different slice

for selected_slice in range(64):

  fig = plt.figure(figsize=(25, 10))#,dpi=300)
  for i, beta in enumerate(betas):
      noise_cube = noise_cubes[i]
      # Plot 3D noise cube in the first row
      ax = fig.add_subplot(2, 5, i+1, projection='3d')
      x, y, z = np.indices((64, 64, 64))
      mask = noise_cube > noise_cube.mean() + 0.2 * noise_cube.std()
      ax.scatter(x[mask], y[mask], z[mask], alpha=0.05, color='blue',s=0.3)
      
      # Extract the selected slice for 3D plotting
      central_slice = noise_cube[selected_slice, :, :]
      Y, Z = np.meshgrid(range(64), range(64))
      X = np.full(Y.shape, selected_slice)
      
      # Plot the selected slice on the 3D plot
      colors = plt.cm.viridis((central_slice - central_slice.min()) / (central_slice.max() - central_slice.min()))
      ax.plot_surface(X, Y, Z, facecolors=colors, rstride=1, cstride=1, shade=False,alpha=0.5)
      
      ax.set_title(f'Beta = {beta:.2f}',fontsize=32)
      ax.axis('off')
      
      # Plot 2D slice in the second row
      ax2 = fig.add_subplot(2, 5, i+6)
      ax2.imshow(central_slice, cmap='viridis')
      # ax2.set_title(f'Beta = {beta:.2f}')
      ax2.axis('off')

  plt.tight_layout()
  path = ''#'figures/'
  plt.savefig(f'{path}noise_slice_{selected_slice}.png') 
  # plt.show()

