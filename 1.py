from iminuit import Minuit
import numpy as np
import math as m
import cmath
from sympy import symbols, solve, Interval
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

def kappa(ub,ube,uc,uce,ut,ute,utau,utaue,uw,uwe,uz,uze,ug,uge,ugma,ugmae,umu,umue,uzgma,uzgmae):
  kh=1
  for kg,kb,kc,kt,ktau,kw,kz,kgma,kmu in zip(range(0,2),range(0,2),range(0,2),range(0,2),range(0,2),range(0,2),range(0,2),range(0,2),range(0,2)):
    ub - ube     <= (m.pow(kg,2)) * (m.pow(kb,2)) / (m.pow(kh,2)) <=  ub + ube
    uc - uce     <= (m.pow(kg,2)) * (m.pow(kc,2)) / (m.pow(kh,2)) <= uc + uce
    ut - ute     <= (m.pow(kg,2)) * (m.pow(kt,2)) / (m.pow(kh,2)) <= ut + ute
    utau - utaue <= (m.pow(kg,2)) * (m.pow(ktau,2)) / (m.pow(kh,2)) <= utau + utaue
    uw - uwe     <= (m.pow(kg,2)) * (m.pow(kw,2)) / (m.pow(kh,2)) <= uw + uwe
    uz - uze     <= (m.pow(kg,2)) * (m.pow(kz,2)) / (m.pow(kh,2)) <= uz + uze
    ug - uge     <= (m.pow(kg,2)) * (m.pow(kg,2)) / (m.pow(kh,2)) <= ug + uge
    ugma -ugmae  <= (m.pow(kg,2)) * (m.pow(kgma,2)) / (m.pow(kh,2)) <= ugma + ugmae
    umu - umue   <=(m.pow(kg,2)) * (m.pow(kmu,2)) / (m.pow(kh,2)) <= umu + umue
    uzgma - uzgma <= (m.pow(kg,2)) * (m.pow(kgma,2)) / (m.pow(kh,2)) <= uzgma + uzgma

    Thbb =2379 #KeV
    Thtautau = 256
    Thmumu= 0.89
    ThWW = 883
    Thgg = 335
    ThZZ =108
    Thgmagma =9.3
    ThZgma =6.3

    kh^2 == (Thbb * (m.pow(kb,2)) + Thtautau * (m.pow(ktau,2)) + Thmumu * (m.pow(kmu,2)) + ThWW * (m.pow(kw,2)) + ThZZ * (m.pow(kz,2)) + Thgmagma * (m.pow(kgma,2)) + ThZgma * kz*kgma)/6.1
  return (ub, uc, ut, utau, uw, uz, ug, ugma, umu,uzgma)

# print('kappaSM',kappa(1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1))
print('kappaSM',kappa(1.1,0.2,1.2,0.5,1.23,0.32,1.12,0.06,1.09,0.22,1.13,0.56,1.5,0.12,1.11,0.1,1.1432,0.16,1.73,0.32))