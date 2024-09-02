import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

from matplotlib.widgets import Button, Slider

fixed_sig_2= 2.0
varied_y2_arr= np.arange(-5, 5.5, 0.5)
store_x_hat_varied_y2=[]

fixed_y2= 1.0
varied_sig2_arr= np.arange(0, 5.5, 0.5)
varied_sig2_arr_sq= [i**2 for i in varied_sig2_arr]
store_x_hat_varied_sig2=[]

y1, sig1= 0.0, 1.0
y2, sig2= 1.0, 2.0 

def compute_x_hat(y_means, y_var):
    y_var_sq= [i**2 for i in y_var]
    x_hat_num= np.sum([y_means[i]/y_var_sq[i] for i in range(len(y_means))])
    x_hat_denom= np.sum([1/i for i in y_var_sq])
    x_hat= x_hat_num/ x_hat_denom
    sig= np.sqrt(1/x_hat_denom)
    return x_hat, sig

x_hat, sig= compute_x_hat(y_means=[y1, y2], y_var= [sig1, sig2])

fig, ax = plt.subplots()
x1 = np.linspace( y1 - 3.0* sig1 , y1 + 3.0*sig1 , 100 )
x2 = np.linspace( y2 - 3.0* sig2 , y2 + 3.0*sig2 , 100 )
x = np.linspace( x_hat - 3.0* sig , x_hat + 3.0*sig , 100 )

line1,= ax.plot( x1, sp.stats.norm.pdf(x , loc=y1 , scale=sig1 ) , ":" , label= "N(y1, sigma1)")
line2,=ax.plot( x2, sp.stats.norm.pdf(x , loc=y2 , scale=sig2 ) , "-." , label= "N(y2, sigma2)")
line3,=ax.plot( x, sp.stats.norm.pdf(x , loc=x_hat , scale=sig), label= "N(x_hat, sigma)")

# adjust the main plot to make room for the sliders
fig.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the frequency.
axs = fig.add_axes([0.25, 0.1, 0.65, 0.03])
sig_slider = Slider(
    ax=axs,
    label='sigma2',
    valmin=0.1,
    valmax=5,
    valinit=sig2,
)
# Make a horizontal slider to control the frequency.
axy = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
y_slider = Slider(
    ax=axy,
    label='y2',
    valmin=-5,
    valmax=5,
    valinit=y2,
    orientation="vertical"
)

def update(val):
    line2.set_ydata(sp.stats.norm.pdf(x , loc=y_slider.val , scale=sig_slider.val ))
    new_x_hat, new_sig= compute_x_hat(y_means=[y1, y_slider.val], y_var= [sig1, sig_slider.val])
    line3.set_ydata(sp.stats.norm.pdf(x , loc=new_x_hat , scale=new_sig))
    fig.canvas.draw_idle()

sig_slider.on_changed(update)
y_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    y_slider.reset()
    sig_slider.reset()
button.on_clicked(reset)
ax.legend()
plt.show()

#code was created using code from https://matplotlib.org/stable/gallery/widgets/slider_demo.html 