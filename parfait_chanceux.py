import parfait_chanceux_m as pcm
import easygui as eg

parfait = []
chanceux = []

for i in range(2, 1000):
    if pcm.estParfait(i):
        parfait.append(i)
    if pcm.estChanceux(i):
        chanceux.append(i)

eg.msgbox("Les nombres parfaits sont: " + str(parfait) +
          "\nLes nombres chanceux sont: " + str(chanceux))
