from tkinter import *
import math
import matplotlib.pyplot as plt

def pfr_calculate():
    inletconc = float(entry1.get())
    volflowrate = float(entry2.get())
    x = float(entry4.get())
    n = float(entry5.get())
    rateconst = float(entry6.get())
    a = float(entry7.get())
    b = float(entry8.get())
    epsilon = b/a - 1
    if (n != 1):
        n0 = x / 0.01
        integ = 1 + ((1 + epsilon * x) / (1 - x)) ** n
        for i in range(1, int(n0)):
            k = i * 0.01
            if i % 3 == 0:
                integ += 2 * ((1 + epsilon * k) / (1 - k)) ** n
            else:
                integ += 3 * ((1 + epsilon * k) / (1 - k)) ** n
        integ = 0.00375 * integ
        volflow = volflowrate * (1 + epsilon * x)
        fconc = inletconc * (1 - x) / (1 + epsilon * x)
        volume = integ * volflowrate / (rateconst * ((inletconc) ** (n - 1)))
        rtd = volume / volflowrate
        sv = volflowrate / volume
        label_vol.config(text="Volume of reactor needed (in L): %.8f" % volume)
        label_conc.config(text="Final Concentration (in mol/L): %.8f" % fconc)
        label_volflow.config(text="Final Volumetric Flow Rate (in L/sec): %.8f" % volflow)
        label_rtd.config(text="Mean Residence Time (in sec): %.8f" % rtd)
        label_sv.config(text="Space Velocity (in sec^-1): %.8f" % sv)
        return volume
    else:
        n0 = x / 0.01
        integ = 1 + ((1 + epsilon * x) / (1 - x)) ** n
        for i in range(1, int(n0)):
            k = i * 0.01
            if i % 3 == 0:
                integ += 2 * ((1 + epsilon * k) / (1 - k)) ** n
            else:
                integ += 3 * ((1 + epsilon * k) / (1 - k)) ** n
        integ = 0.00375 * integ
        volflow = volflowrate * (1 + epsilon * x)
        fconc = inletconc * (1 - x) / (1 + epsilon * x)
        volume = integ * volflowrate / (rateconst * ((inletconc) ** (n - 1)))
        rtd = volume / volflowrate
        sv = volflowrate / volume
        label_vol.config(text="Volume of reactor needed (in L): %.8f" % volume)
        label_conc.config(text="Final Concentration (in mol/L): %.8f" % fconc)
        label_volflow.config(text="Final Volumetric Flow Rate (in L/sec): %.8f" % volflow)
        label_rtd.config(text="Mean Residence Time (in sec): %.8f" % rtd)
        label_sv.config(text="Space Velocity (in sec^-1): %.8f" % sv)
        return volume

def pfr_graphcalculate(x):
    inletconc = float(entry1.get())
    volflowrate = float(entry2.get())
    n = float(entry5.get())
    rateconst = float(entry6.get())
    a = float(entry7.get())
    b = float(entry8.get())
    epsilon = b/a - 1
    if (n != 1):
        h = x / 100
        integ1 = 1 + (((1 + epsilon * x) / (1 - x)) ** n)
        for i in range(1, 100):
            k = i * h
            if i % 3 == 0:
                integ1 += 2 * ((1 + epsilon * k) / (1 - k)) ** n
            else:
                integ1 += 3 * ((1 + epsilon * k) / (1 - k)) ** n
        integ1 = 0.375 * h * integ1
        volume = (integ1 * volflowrate) / (rateconst * ((inletconc) ** (n - 1)))
        return volume

def cstr_calculate():
    inletconc = float(entry1.get())
    volflowrate = float(entry2.get())
    x = float(entry4.get())
    n = float(entry5.get())
    rateconst = float(entry6.get())
    a = float(entry7.get())
    b = float(entry8.get())
    epsilon = b/a - 1
    volume = (inletconc * volflowrate * x) / (rateconst * ((inletconc * (1 - x)) ** n))
    print(volume)
    volflow = volflowrate * (1 + epsilon * x)
    fconc = inletconc * (1 - x) / (1 + epsilon * x)
    rtd = volume / volflowrate
    sv = volflowrate / volume
    label_vol.config(text="Volume of reactor needed (in L): %.8f" % volume)
    label_conc.config(text="Final Concentration (in mol/L): %.8f" % fconc)
    label_volflow.config(text="Final Volumetric Flow Rate (in L/sec): %.8f" % volflow)
    label_rtd.config(text="Mean Residence Time (in sec): %.8f" % rtd)
    label_sv.config(text="Space Velocity (in sec^-1): %.8f" % sv)
    return volume

def cstr_graphcalculate(x):
    inletconc = float(entry1.get())
    volflowrate = float(entry2.get())
    n = float(entry5.get())
    rateconst = float(entry6.get())
    a = float(entry7.get())
    b = float(entry8.get())
    epsilon = b/a - 1
    volume = (inletconc * volflowrate * x) / (rateconst * ((inletconc * (1 - x)) ** n))
    return volume

def pfr_graphing():
    a = []
    b = []
    for i in range(100):
        a += [0.01 * i]
        b += [pfr_graphcalculate(0.01 * i)]
    plt.plot(a, b)
    plt.xlabel('Conversion')
    plt.ylabel('Reactor Volume (in L)')
    plt.title('Volume vs Conversion for PFR')
    plt.show()

def cstr_graphing():
    a = []
    b = []
    for i in range(100):
        a += [0.01 * i]
        b += [cstr_graphcalculate(0.01 * i)]
    plt.plot(a, b)
    plt.xlabel('Conversion')
    plt.ylabel('Reactor Volume (in L)')
    plt.title('Volume vs Conversion for CSTR')
    plt.show()

def series_reaction_cstr():
    inletconc = float(entry1.get())
    rateconst = float(entry6.get())
    num_reactors = int(entry_series.get())
    outlet_conc = inletconc * (1 + rateconst) ** (-num_reactors)
    label_outlet_conc.config(text="Outlet Concentration (in mol/L): %.8f" % outlet_conc)

def parallel_reaction_cstr():
    inletconc = float(entry1.get())
    x = float(entry4.get())
    num_reactors = int(entry_parallel.get())
    outlet_conc = inletconc * (1 - x) ** num_reactors
    label_outlet_conc.config(text="Outlet Concentration (in mol/L): %.8f" % outlet_conc)

root = Tk()
root.title("Reactor Volume Calculator for A -> B in Isothermal conditions")

label1 = Label(root, text="Inlet Concentration (in mol/L)")
label1.pack()

entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Volumetric Flow Rate at Inlet (in L/sec)")
label2.pack()

entry2 = Entry(root)
entry2.pack()

label4 = Label(root, text="Required Conversion")
label4.pack()

entry4 = Entry(root)
entry4.pack()

label5 = Label(root, text="Reaction Order(n)")
label5.pack()

entry5 = Entry(root)
entry5.pack()

label6 = Label(root, text="Reaction Rate Constant with respect to Reactant (in (mol/L)^(1-n) /sec)")
label6.pack()

entry6 = Entry(root)
entry6.pack()

label7 = Label(root, text="Stoichiometry of Reactant A")
label7.pack()

entry7 = Entry(root)
entry7.pack()

label8 = Label(root, text="Stoichiometry of Product B")
label8.pack()

entry8 = Entry(root)
entry8.pack()

button_pfr_calculate = Button(root, text="PFR Calculate", command=pfr_calculate)
button_pfr_calculate.pack()

button_pfr_graphing = Button(root, text="PFR Graph", command=pfr_graphing)
button_pfr_graphing.pack()

button_cstr_calculate = Button(root, text="CSTR Calculate", command=cstr_calculate)
button_cstr_calculate.pack()

button_cstr_graphing = Button(root, text="CSTR Graph", command=cstr_graphing)
button_cstr_graphing.pack()

label_vol = Label(root, text="")
label_vol.pack()

label_conc = Label(root, text="")
label_conc.pack()

label_volflow = Label(root, text="")
label_volflow.pack()

label_rtd = Label(root, text="")
label_rtd.pack()

label_sv = Label(root, text="")
label_sv.pack()

label_series = Label(root, text="Number of Reactors in Series:")
label_series.pack()

entry_series = Entry(root)
entry_series.pack()

button_series_reaction_cstr = Button(root, text="Calculate Series Reaction in CSTR", command=series_reaction_cstr)
button_series_reaction_cstr.pack()

label_parallel = Label(root, text="Number of Reactors in Parallel:")
label_parallel.pack()

entry_parallel = Entry(root)
entry_parallel.pack()

button_parallel_reaction_cstr = Button(root, text="Calculate Parallel Reaction in CSTR", command=parallel_reaction_cstr)
button_parallel_reaction_cstr.pack()

label_outlet_conc = Label(root, text="")
label_outlet_conc.pack()

root.mainloop()
