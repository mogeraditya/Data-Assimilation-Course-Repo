import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import scipy.linalg as linalg
import numpy as np
import scipy as scp

def solve_eq(vec, pars):
  dvec= pars@vec.T
  return dvec

def solve_eq_backwards(vec, pars, dt):
  A= (np.eye(pars.shape[0]))- dt*pars
  A_inv= np.linalg.inv(A)
  dvec= A_inv@pars@vec
  return dvec

def generate_true(xin, time, pars):
  frhs = xin*0.0
  store_vec= []
  
  vec= xin
  for t in range(1, len(time)):
    store_vec.append(vec)
    dvec= pars@vec.T
    dt= time[t]-time[t-1]
    
    print(np.array(dt*dvec)[0]); print(type(dt*dvec))
    vec= vec + np.array(dt*dvec)[0]
  store_vec.append(vec)

  return np.array(store_vec)

def lotka_volterra_forward(xin, time, pars, K, y_obs, H):
  frhs = xin*0.0
  store_vec= []
  # a, b, d, g = pars
  # x, y = xin
  vec= xin
  for t in range(1, len(time)):
    store_vec.append(vec)
    gain_vec= K*(y_obs[t].T- H@vec.T)
    dvec= solve_eq(vec, pars) + gain_vec
    dt= time[t]-time[t-1]
    # print(dt*dvec)
    vec= vec + np.array(dt*dvec)[0]
  store_vec.append(vec)

  return np.array(store_vec)

def lotka_volterra_backward(x_tilda, time, pars, K_prime, y_obs, H):

  store_vec= []
  vec= x_tilda.copy()
  
  for t in range(len(time)-1, 0, -1):
    store_vec.append(vec)
    gain_vec= K_prime*(y_obs[t].T- H@vec.T)
    dt= time[t]-time[t-1]
    dvec= solve_eq_backwards(vec, pars, dt) - gain_vec
  
    # print(dt*dvec)
    vec= vec - np.array(dt*dvec)[0]
  store_vec.append(vec)

  return np.flip(store_vec, axis=0)


def back_forth_nudge(pars, t, K, K_back, H, y_obs, number_of_iterations): #once
  store_backward, store_forward=[], []
  #tilta, normal
  xin= np.mean(y_obs, axis=0)
  nudge= lotka_volterra_forward(xin, t, pars, 0.2, y_obs, H)
  store_forward.append(nudge)
  for it in range(number_of_iterations):
    nudge_back= lotka_volterra_backward(nudge[-1], t, pars, K_back, y_obs, H)
    nudge= lotka_volterra_forward(nudge_back[0], t, pars, K, y_obs, H)
    store_backward.append(nudge_back)
    store_forward.append(nudge)
  return store_forward, store_backward


