# Plot the surface area productivity for hemispheroids
def hemispheroid_SAP():
  # Create meshgrid for oblate and prolate
  r_vals_oblate, e_vals_oblate = np.meshgrid(r, e_oblate)
  r_vals_prolate, e_vals_prolate = np.meshgrid(r, e_prolate)
  
  # Assuming you have defined the functions hemisphere_surface, prolate_surface, and oblate_surface somewhere in your code
  
  # Calculate the surface values for each shape
  hemisphere_vals = hemisphere_surface(r_vals_oblate, np.zeros_like(r_vals_oblate), G, rho)  # Hemisphere surface with e=0
  prolate_vals = prolate_surface(r_vals_prolate, e_vals_prolate, G, rho)
  oblate_vals = oblate_surface(r_vals_oblate, e_vals_oblate, G, rho)
  
  # Create 3D plot
  fig = plt.figure(figsize=(15, 15), dpi=600)
  ax = fig.add_subplot(111, projection='3d', adjustable='box', aspect="auto")
  
  # Plot hemisphere surface values as a line at e=0
  ax.plot(r_vals_oblate[0, :], np.zeros_like(r_vals_oblate[0, :]), hemisphere_vals[0, :], color='green', alpha=0.8)
  
  # Plot prolate surface values
  prolate_surface_plot = ax.plot_surface(r_vals_prolate, e_vals_prolate, prolate_vals, cmap='cool', edgecolor='none', alpha=0.8)
  
  # Plot oblate surface values
  oblate_surface_plot = ax.plot_surface(r_vals_oblate, e_vals_oblate, oblate_vals, cmap='hot', edgecolor='none', alpha=0.8)
  
  # Alter viewing angle
  ax.view_init(azim=30, elev=20)
  
  # Change the color of the axes planes
  ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))  # R, G, B, alpha
  ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  
  # Set labels and title
  plt.yticks(fontsize=10)
  plt.xticks(fontsize=10)
  ax.zaxis.set_tick_params(labelsize=10)
  
  ax.set_xlabel('Equatorial Radius (cm)', fontsize = 20)
  ax.set_ylabel('Eccentricity (e)', fontsize = 20)
  ax.set_zlabel('Surface Area Productivity (yr)', fontsize = 20)
  ax.set_title('Hemispheroid Surface Area Productivity', fontsize = 30)
  
  # Create custom legend proxy objects
  legend_proxy1 = plt.Line2D([0], [0], linestyle='-', color='red', label='Oblate Hemispheroid')
  legend_proxy2 = plt.Line2D([0], [0], linestyle='-', color='green', label='Hemisphere')
  legend_proxy3 = plt.Line2D([0], [0], linestyle='-', color='blue', label='Prolate Hemispheroid')
  
  # Add a legend with custom proxy objects
  ax.legend(handles=[legend_proxy1, legend_proxy2, legend_proxy3], fontsize = 20)
  
  # Show the plot
  plt.show()

# Plot the planar area productivity for hemispheroids
def hemispheroid_PAP():
  # Create meshgrid for oblate and prolate
  r_vals_oblate, e_vals_oblate = np.meshgrid(r, e_oblate)
  r_vals_prolate, e_vals_prolate = np.meshgrid(r, e_prolate)
  
  # Calculate the surface values for each shape
  hemisphere_vals = hemisphere_planar(r_vals_oblate, np.zeros_like(r_vals_oblate), G, rho)  # Hemisphere surface with e=0
  prolate_vals = prolate_planar(r_vals_prolate, e_vals_prolate, G, rho)
  oblate_vals = oblate_planar(r_vals_oblate, e_vals_oblate, G, rho)
  
  # Create 3D plot
  fig = plt.figure(figsize=(15, 15), dpi=600)
  ax = fig.add_subplot(111, projection='3d', adjustable='box', aspect="auto")
  
  # Plot hemisphere surface values as a line at e=0
  ax.plot(r_vals_oblate[0, :], np.zeros_like(r_vals_oblate[0, :]), hemisphere_vals[0, :], color='green', alpha=0.8)
  
  # Plot prolate surface values
  prolate_surface_plot = ax.plot_surface(r_vals_prolate, e_vals_prolate, prolate_vals, cmap='cool', edgecolor='none', alpha=0.8)
  
  # Plot oblate surface values
  oblate_surface_plot = ax.plot_surface(r_vals_oblate, e_vals_oblate, oblate_vals, cmap='hot', edgecolor='none', alpha=0.8)
  
  # Alter viewing angle
  ax.view_init(azim=30, elev=20)
  
  # Change the color of the axes planes
  ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))  # R, G, B, alpha
  ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  
  # Set labels and title
  plt.yticks(fontsize=10)
  plt.xticks(fontsize=10)
  ax.zaxis.set_tick_params(labelsize=10)
  
  # Set labels and title
  ax.set_xlabel('Base Radius (a)', fontsize = 20)
  ax.set_ylabel('Eccentricity (e)', fontsize = 20)
  ax.set_zlabel('Surface Area Productivity (yr)', fontsize = 20)
  ax.set_title('Hemispheroid Planar Area Productivity', fontsize = 30)
  
  # Create custom legend proxy objects
  legend_proxy1 = plt.Line2D([0], [0], linestyle='-', color='green', label='Hemisphere')
  legend_proxy2 = plt.Line2D([0], [0], linestyle='-', color='red', label='Oblate Hemispheroid')
  legend_proxy3 = plt.Line2D([0], [0], linestyle='-', color='blue', label='Prolate Hemispheroid')
  
  # Add a legend with custom proxy objects
  ax.legend(handles=[legend_proxy1, legend_proxy2, legend_proxy3])
  
  # Show the plot
  plt.show()

# Plot the surface area to volume ratio for hemispheroids
def hemispheroid_SVR():
  # Create meshgrid for oblate and prolate
  r_vals_oblate, e_vals_oblate = np.meshgrid(r, e_oblate)
  r_vals_prolate, e_vals_prolate = np.meshgrid(r, e_prolate)
  
  # Calculate the surface values for each shape
  hemisphere_vals = hemisphere_svr(r_vals_oblate)  # Hemisphere surface with e=0
  prolate_vals = prolate_svr(r_vals_prolate, e_vals_prolate)
  oblate_vals = oblate_svr(r_vals_oblate, e_vals_oblate)
  
  # Create 3D plot
  fig = plt.figure(figsize=(15, 15), dpi=600)
  ax = fig.add_subplot(111, projection='3d', adjustable='box', aspect="auto")
  
  # Plot hemisphere surface values as a line at e=0
  ax.plot(r_vals_oblate[0, :], np.zeros_like(r_vals_oblate[0, :]), hemisphere_vals[0, :], color='green', alpha=0.8)
  
  # Plot prolate surface values
  prolate_surface_plot = ax.plot_surface(r_vals_prolate, e_vals_prolate, prolate_vals, cmap='cool', edgecolor='none', alpha=0.8)
  
  # Plot oblate surface values
  oblate_surface_plot = ax.plot_surface(r_vals_oblate, e_vals_oblate, oblate_vals, cmap='hot', edgecolor='none', alpha= 0.8)
  
  # Alter viewing angle
  ax.view_init(azim=30, elev=20)
  
  # Change the color of the axes planes
  ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))  # R, G, B, alpha
  ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  
  # Set labels and title
  ax.set_xlabel('Base Radius (a)')
  ax.set_ylabel('Eccentricity (e)')
  ax.set_zlabel('Surface Area to Volume Ratio (SVR)')
  ax.set_title('Hemispheroid Surface Area to Volume Ratio')
  
  # Create custom legend proxy objects
  legend_proxy1 = plt.Line2D([0], [0], linestyle='-', color='green', label='Hemisphere')
  legend_proxy2 = plt.Line2D([0], [0], linestyle='-', color='red', label='Oblate Hemispheroid')
  legend_proxy3 = plt.Line2D([0], [0], linestyle='-', color='blue', label='Prolate Hemispheroid')
  
  # Add a legend with custom proxy objects
  ax.legend(handles=[legend_proxy1, legend_proxy2, legend_proxy3])
  
  # Show the plot
  plt.show()

# Plot the surface area productivity for branching coral
def branching_SAP():
  # Create meshgrid for oblate and prolate
  h_vals, a_vals = np.meshgrid(h, a)
  
  # Calculate the surface values for each shape
  #hemisphere_vals = hemisphere_surface(h_vals/a_vals, 1, G, rho)  # Hemisphere surface with e=0
  branching_vals = branching_surface(h_vals, a_vals, G, rho)
  
  # Create 3D plot
  fig = plt.figure(figsize=(15, 15), dpi=600)
  ax = fig.add_subplot(111, projection='3d', adjustable='box', aspect="auto")
  
  # Plot oblate surface values
  branching_surface_plot = ax.plot_surface(h_vals, a_vals, branching_vals, cmap='hot', edgecolor='none', alpha=0.8)
  
  # Alter viewing angle
  ax.view_init(azim=30, elev=20)
  
  # Change the color of the axes planes
  ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))  # R, G, B, alpha
  ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  
  # Set labels and title
  plt.yticks(fontsize=15)
  plt.xticks(fontsize=15)
  ax.zaxis.set_tick_params(labelsize=15)
  
  ax.set_xlabel('Height/Length (cm)', fontsize = 20)
  ax.set_ylabel('Aspect Ratio', fontsize = 20)
  ax.set_zlabel('Surface Area Productivity (yr)', fontsize = 20)
  ax.set_title('Branching Surface Area Productivity',fontsize = 40)
  
  # Create custom legend proxy objects
  legend_proxy1 = plt.Line2D([0], [0], linestyle='-', color='green', label='Hemisphere')
  legend_proxy2 = plt.Line2D([0], [0], linestyle='-', color='red', label='Oblate Hemispheroid')
  
  # Show the plot
  plt.show()


# Plot the surface area to volume ratio for branching coral
def branching_SVR():
  # Create meshgrid for oblate and prolate
  h_vals, a_vals = np.meshgrid(h, a)
  
  # Calculate the surface values for each shape
  branching_vals = branching_svr(h_vals, a_vals, G, rho)
  
  # Create 3D plot
  fig = plt.figure(figsize=(15, 15), dpi=600)
  ax = fig.add_subplot(111, projection='3d', adjustable='box', aspect="auto")
  
  # Plot oblate surface values
  branching_surface_plot = ax.plot_surface(h_vals, a_vals, branching_vals, cmap='hot', edgecolor='none', alpha=0.8)
  
  # Alter viewing angle
  ax.view_init(azim=30, elev=20)
  
  # Change the color of the axes planes
  ax.w_xaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))  # R, G, B, alpha
  ax.w_yaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  ax.w_zaxis.set_pane_color((0.8, 0.8, 0.8, 1.0))
  
  # Set labels and title
  ax.set_xlabel('Height (h)')
  ax.set_ylabel('Alpha (a)')
  ax.set_zlabel('Surface Area to Volume Ratio (SVR)')
  ax.set_title('Branching Surface Area to Volume Ratio')
  
  # Create custom legend proxy objects
  legend_proxy1 = plt.Line2D([0], [0], linestyle='-', color='green', label='Hemisphere')
  legend_proxy2 = plt.Line2D([0], [0], linestyle='-', color='red', label='Oblate Hemispheroid')
  
  # Show the plot
  plt.show()
