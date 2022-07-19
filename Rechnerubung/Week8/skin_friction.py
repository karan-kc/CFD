#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat June 11 15:15:00 2022

@author: Karan Chodankar
"""

tau = 8.312409e-03  # Magnitude of Maximum Wall Shear Stress is taken from postProcessing at top-Wall
u_bulk = 1.3452
rho = 1.225
re = 18000

c_f = tau / (0.5 * rho * u_bulk ** 2)
c_f_dean = 0.073 * 18000 ** (-1 / 4)
dev = (c_f - c_f_dean) / c_f_dean  # The Deviation is about 19%

print("The deviation from Dean-Correlation is "+str(dev*100)+"%")
