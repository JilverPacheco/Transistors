from tkinter import Tk, ttk
from matplotlib import pyplot as plt

class GUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("UDIstror")
        self.configTransistor = ttk.LabelFrame(self.root,
                                               text='Tipo de configuración')
        self.configTransistor.grid(column=1, row=0, padx=5, pady=5)
        self.setConfigTransistor()
        self.FormulaeHelp = ttk.LabelFrame(self.root, text='Formulas')
        self.FormulaeHelp.grid(column=2, row=0, padx=5, pady=5)
        self.getFormulaeHelp()
        self.root.mainloop()

    def setConfigTransistor(self):
        self.btn = ttk.Button(self.configTransistor,text="Tipica",command=self.getTypicalEntries)
        self.btn.grid(column=0, row=0, padx=4, pady=4)
        self.btn = ttk.Button(self.configTransistor, text="Estabilizada", command=self.getStabilizedEntries)
        self.btn.grid(column=0, row=1, padx=4, pady=4)
        self.btn = ttk.Button(self.configTransistor, text="Divisor de tension", command=self.getTensionDividerEntries)
        self.btn.grid(column=0, row=2, padx=4, pady=4)
        self.btn = ttk.Button(self.configTransistor,text="Salir",command=self._quit)
        self.btn.grid(column=0, row=3, padx=4, pady=4)

    def getFormulaeHelp(self):
        self.btn = ttk.Button(self.FormulaeHelp,
                              text="típica",
                              command=self._typicalFormuale)
        self.btn.grid(column=0, row=0, padx=4, pady=4)
        self.btn = ttk.Button(self.FormulaeHelp,
                              text="Estabilización en el emisor",
                              command=self._stabilizedFormuale)
        self.btn.grid(column=0, row=1, padx=4, pady=4)
        self.btn = ttk.Button(self.FormulaeHelp,
                              text="Divisor de tension",
                              command=self._tensionDividerFormulae)
        self.btn.grid(column=0, row=2, padx=4, pady=4)

    def _quit(self):
        self.root.quit()
        self.root.destroy()

    def _typicalFormuale(self):
        typical_IB = 'IB = VBB - VBE / RB'
        typical_IC = 'IC = B * IB'
        typical_IE = 'IE = IB + IC'
        typical_VCE = 'VCE = VCC - IC * (RC)'
        typical_VB = 'VB = VBE'
        typical_VC = 'VC = VCE'
        typical_ICsat = 'ICsat = VCC / RC'
        typical_VCEoff = 'VCEoff = VCC'
        self.typicalFormulae = ttk.LabelFrame(self.root,text='Polarizacion típica')
        self.typicalFormulae.grid(column=0, row=1, padx=5, pady=5)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_IB)
        self.label_tyical.grid(column=0, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_IC)
        self.label_tyical.grid(column=1, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_IE)
        self.label_tyical.grid(column=0, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_VCE)
        self.label_tyical.grid(column=1, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_VB)
        self.label_tyical.grid(column=0, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_VC)
        self.label_tyical.grid(column=1, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae, text=typical_ICsat)
        self.label_tyical.grid(column=0, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.typicalFormulae,text=typical_VCEoff)
        self.label_tyical.grid(column=1, row=3, padx=4, pady=2)

    def _stabilizedFormuale(self):
        stabilized_IB = 'IB = VBB - VBE / RB + (B+1) * RE'
        stabilized_IC = 'IC = B * IB'
        stabilized_IE = 'IE = IB + IC'
        stabilized_VCE = 'VCE = VCC - IC * (RC - RE)'
        stabilized_VB = 'VB = VBE + VE | VB = VCC - IB * RB'
        stabilized_VC = 'VC = VCE + VE | VC = VCC - IC * RC'
        stabilized_VE = 'VE = IE * RE'
        stabilized_ICsat = 'ICsat = VCC / RC + RE'
        stabilized_VCEoff = 'VCEoff = VCC'
        self.stabilizedFormulae = ttk.LabelFrame(
            self.root, text='Polarizacion estabilizada en el emisor')
        self.stabilizedFormulae.grid(column=1, row=1, padx=5, pady=5)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_IB)
        self.label_tyical.grid(column=0, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_IC)
        self.label_tyical.grid(column=1, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_IE)
        self.label_tyical.grid(column=0, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_VB)
        self.label_tyical.grid(column=1, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_VC)
        self.label_tyical.grid(column=0, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_VE)
        self.label_tyical.grid(column=1, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_VCE)
        self.label_tyical.grid(column=0, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_ICsat)
        self.label_tyical.grid(column=1, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.stabilizedFormulae,
                                      text=stabilized_VCEoff)
        self.label_tyical.grid(column=0, row=4, padx=4, pady=2)

    def _tensionDividerFormulae(self):
        tensionDivider_VTH = 'VTH = VCC (R2 / R1 + R2)'
        tensionDivider_RTH = 'RTH = R1 * R2 / R1 + R2'
        tensionDivider_IB = 'IB = VTH - VBE / RTH'
        tensionDivider_IC = 'IC = B * IB'
        tensionDivider_IE = 'IE = IB + IC'
        tensionDivider_VCE = 'VCE = VCC - IC * (RC - RE)'
        tensionDivider_VB = 'VB = VBE + VE | VB = VCC - IB * RTH'
        tensionDivider_VC = 'VC = VCE + VE | VC = VCC - IC * RC'
        tensionDivider_VE = 'VE = IE * RE'
        tensionDivider_ICsat = 'ICsat = VCC / RC + RE'
        tensionDivider_VCEoff = 'VCEoff = VCC'
        self.tensionDividerFormulae = ttk.LabelFrame(
            self.root, text='Polarizacion estabilizada en el emisor')
        self.tensionDividerFormulae.grid(column=2, row=1, padx=5, pady=5)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_VTH)
        self.label_tyical.grid(column=0, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_RTH)
        self.label_tyical.grid(column=1, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_IB)
        self.label_tyical.grid(column=0, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_IC)
        self.label_tyical.grid(column=1, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_IE)
        self.label_tyical.grid(column=0, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_VCE)
        self.label_tyical.grid(column=1, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,
                                      text=tensionDivider_VB)
        self.label_tyical.grid(column=0, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,text=tensionDivider_VC)
        self.label_tyical.grid(column=1, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,text=tensionDivider_VE)
        self.label_tyical.grid(column=0, row=4, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,text=tensionDivider_ICsat)
        self.label_tyical.grid(column=1, row=4, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.tensionDividerFormulae,text=tensionDivider_VCEoff)
        self.label_tyical.grid(column=0, row=5, padx=4, pady=2)

    def getTypicalEntries(self):
        self.TypicalEntries = ttk.LabelFrame(self.root, text='Ingrese valores')
        self.TypicalEntries.grid(column=0, row=2, padx=5, pady=5)
        self.typical_Beta = ttk.Label(self.TypicalEntries, text='Beta')
        self.typical_Beta.grid(column=0, row=0, padx=4, pady=2)
        self.entryTypical_Beta = ttk.Entry(self.TypicalEntries)
        self.entryTypical_Beta.grid(column=1, row=0, padx=4, pady=2)
        self.typical_VBB = ttk.Label(self.TypicalEntries, text='VBB')
        self.typical_VBB.grid(column=0, row=1, padx=4, pady=2)
        self.entryTypical_VBB = ttk.Entry(self.TypicalEntries)
        self.entryTypical_VBB.grid(column=1, row=1, padx=4, pady=2)
        self.typical_VCC = ttk.Label(self.TypicalEntries, text='VCC')
        self.typical_VCC.grid(column=0, row=2, padx=4, pady=2)
        self.entryTypical_VCC = ttk.Entry(self.TypicalEntries)
        self.entryTypical_VCC.grid(column=1, row=2, padx=4, pady=2)
        self.typical_RB = ttk.Label(self.TypicalEntries, text='RB')
        self.typical_RB.grid(column=0, row=3, padx=4, pady=2)
        self.entryTypical_RB = ttk.Entry(self.TypicalEntries)
        self.entryTypical_RB.grid(column=1, row=3, padx=4, pady=2)
        self.typical_RC = ttk.Label(self.TypicalEntries, text='RC')
        self.typical_RC.grid(column=0, row=4, padx=4, pady=2)
        self.entryTypical_RC = ttk.Entry(self.TypicalEntries)
        self.entryTypical_RC.grid(column=1, row=4, padx=4, pady=2)
        self.btn = ttk.Button(self.TypicalEntries, text="Evaluar", command=self.ResultTypicalEntries)
        self.btn.grid(column=1, row=5, padx=4, pady=4)

    def ResultTypicalEntries(self):
        self.TypicalOut = ttk.LabelFrame(self.root, text='Resultados')
        self.TypicalOut.grid(column=0, row=3, padx=5, pady=5)
        self.valBeta_Typical = int(self.entryTypical_Beta.get())
        self.valVBB_Typical = int(self.entryTypical_VBB.get())
        self.valVCC_Typical = int(self.entryTypical_VCC.get())
        self.valRB_Typical = int(self.entryTypical_RB.get())
        self.valRC_Typical = int(self.entryTypical_RC.get())

        self.valIB_Typical = (self.valVBB_Typical - 0.7) / self.valRB_Typical
        self.valIC_Typical = self.valBeta_Typical * self.valIB_Typical
        self.valIE_Typical = self.valIB_Typical + self.valIC_Typical
        self.valVCE_Typical = self.valVCC_Typical - self.valIC_Typical * self.valRC_Typical
        self.valICSat_Typical = self.valVCC_Typical / self.valRC_Typical

        self.label_tyical = ttk.Label(self.TypicalOut,text="IB")
        self.label_tyical.grid(column=0, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text=self.valIB_Typical)
        self.label_tyical.grid(column=1, row=0, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text="IC")
        self.label_tyical.grid(column=0, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text=self.valIC_Typical)
        self.label_tyical.grid(column=1, row=1, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text="IE")
        self.label_tyical.grid(column=0, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text=self.valIE_Typical)
        self.label_tyical.grid(column=1, row=2, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text="VCE")
        self.label_tyical.grid(column=0, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text=self.valVCE_Typical)
        self.label_tyical.grid(column=1, row=3, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text="ICsat")
        self.label_tyical.grid(column=0, row=4, padx=4, pady=2)
        self.label_tyical = ttk.Label(self.TypicalOut,text=self.valICSat_Typical)
        self.label_tyical.grid(column=1, row=4, padx=4, pady=2)

        self.btn = ttk.Button(self.TypicalOut,text="Graficar",command=self.getTypicalGraph)
        self.btn.grid(column=1, row=5, padx=4, pady=4)

    def getTypicalGraph(self):
        val_VCCoff = [self.valVCC_Typical, 0]
        val_ICsat = [0, self.valICSat_Typical]
        val_VCE = self.valVCE_Typical
        val2_IC = self.valIC_Typical

        plt.plot(val_VCCoff, val_ICsat, 'd-')
        plt.title('Polarización típica')
        plt.xlabel('VCE [V]')
        plt.ylabel('IC [A]')
        plt.axhline(y=val2_IC,color='purple',linestyle='--',xmin=0.05,xmax=0.95)
        plt.axvline(x=val_VCE,color='purple',linestyle='--',ymin=0.05,ymax=0.95)
        plt.show()

    def getStabilizedEntries(self):
        self.StabilizedEntries = ttk.LabelFrame(self.root, text='Ingrese valores')
        self.StabilizedEntries.grid(column=1, row=2, padx=5, pady=5)
        self.stabilized_Beta = ttk.Label(self.StabilizedEntries, text='Beta')
        self.stabilized_Beta.grid(column=0, row=0, padx=4, pady=2)
        self.entryStabilized_Beta = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_Beta.grid(column=1, row=0, padx=4, pady=2)
        self.stabilized_VBB = ttk.Label(self.StabilizedEntries, text='VBB')
        self.stabilized_VBB.grid(column=0, row=1, padx=4, pady=2)
        self.entryStabilized_VBB = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_VBB.grid(column=1, row=1, padx=4, pady=2)
        self.stabilized_VCC = ttk.Label(self.StabilizedEntries, text='VCC')
        self.stabilized_VCC.grid(column=0, row=2, padx=4, pady=2)
        self.entryStabilized_VCC = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_VCC.grid(column=1, row=2, padx=4, pady=2)
        self.stabilized_RB = ttk.Label(self.StabilizedEntries, text='RB')
        self.stabilized_RB.grid(column=0, row=3, padx=4, pady=2)
        self.entryStabilized_RB = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_RB.grid(column=1, row=3, padx=4, pady=2)
        self.stabilized_RC = ttk.Label(self.StabilizedEntries, text='RC')
        self.stabilized_RC.grid(column=0, row=4, padx=4, pady=2)
        self.entryStabilized_RC = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_RC.grid(column=1, row=4, padx=4, pady=2)
        self.stabilized_RE = ttk.Label(self.StabilizedEntries, text='RE')
        self.stabilized_RE.grid(column=0, row=5, padx=4, pady=2)
        self.entryStabilized_RE = ttk.Entry(self.StabilizedEntries)
        self.entryStabilized_RE.grid(column=1, row=5, padx=4, pady=2)
        self.btn = ttk.Button(self.StabilizedEntries, text="Evaluar", command=self.ResultStabilizedEntries)
        self.btn.grid(column=1, row=6, padx=4, pady=4)

    def ResultStabilizedEntries(self):
        self.StabilizedOut = ttk.LabelFrame(self.root, text='Resultados')
        self.StabilizedOut.grid(column=1, row=3, padx=5, pady=5)
        self.valBeta_Stabilized = int(self.entryStabilized_Beta.get())
        self.valVBB_Stabilized = int(self.entryStabilized_VBB.get())
        self.valVCC_Stabilized = int(self.entryStabilized_VCC.get())
        self.valRB_Stabilized = int(self.entryStabilized_RB.get())
        self.valRC_Stabilized = int(self.entryStabilized_RC.get())
        self.valRE_Stabilized = int(self.entryStabilized_RE.get())

        self.valIB_Stabilized = (self.valVBB_Stabilized - 0.7) / (self.valRB_Stabilized + (self.valBeta_Stabilized + 1) * self.valRE_Stabilized)
        self.valIC_Stabilized = self.valBeta_Stabilized * self.valIB_Stabilized
        self.valIE_Stabilized = self.valIB_Stabilized + self.valIC_Stabilized
        self.valVCE_Stabilized = self.valVCC_Stabilized - self.valIC_Stabilized * (self.valRC_Stabilized + self.valRE_Stabilized)
        self.valVB_Stabilized = self.valVCC_Stabilized - self.valIB_Stabilized * self.valRB_Stabilized
        self.valVC_Stabilized = self.valVCC_Stabilized -self.valIC_Stabilized * self.valRC_Stabilized
        self.valVE_Stabilized = self.valIE_Stabilized * self.valRE_Stabilized
        self.valICSat_Stabilized = self.valVCC_Stabilized / (self.valRC_Stabilized + self.valRE_Stabilized)

        self.label_stabilized = ttk.Label(self.StabilizedOut, text="IB")
        self.label_stabilized.grid(column=0, row=0, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valIB_Stabilized)
        self.label_stabilized.grid(column=1, row=0, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut, text="IC")
        self.label_stabilized.grid(column=0, row=1, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valIC_Stabilized)
        self.label_stabilized.grid(column=1, row=1, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut, text="IE")
        self.label_stabilized.grid(column=0, row=2, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valIE_Stabilized)
        self.label_stabilized.grid(column=1, row=2, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut, text="VCE")
        self.label_stabilized.grid(column=0, row=3, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valVCE_Stabilized)
        self.label_stabilized.grid(column=1, row=3, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text="VB")
        self.label_stabilized.grid(column=0, row=4, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valVB_Stabilized)
        self.label_stabilized.grid(column=1, row=4, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text="VC")
        self.label_stabilized.grid(column=0, row=5, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valVC_Stabilized)
        self.label_stabilized.grid(column=1, row=5, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text="VE")
        self.label_stabilized.grid(column=0, row=6, padx=4, pady=2)
        self.label_stabilized = ttk.Label(self.StabilizedOut,text=self.valVE_Stabilized)
        self.label_stabilized.grid(column=1, row=6, padx=4, pady=2) 


        self.Beta_Stabilized = ttk.Label(self.StabilizedOut, text="IC Sat")
        self.Beta_Stabilized.grid(column=0, row=7, padx=4, pady=2)
        self.ICSat_Stabilized = ttk.Label(self.StabilizedOut,text=self.valICSat_Stabilized)
        self.ICSat_Stabilized.grid(column=1, row=7, padx=4, pady=2)
        self.btn = ttk.Button(self.StabilizedOut,text="Graficar",command=self.getStabilizedGraph)
        self.btn.grid(column=1, row=8, padx=5, pady=4)

    def getStabilizedGraph(self):
        val_VCCoff = [self.valVCC_Stabilized, 0]
        val_ICsat = [0, self.valICSat_Stabilized]
        val_VCE_Graph = self.valVCE_Stabilized
        val_IC_Graph = self.valIC_Stabilized

        plt.plot(val_VCCoff, val_ICsat, 'd-')
        plt.title('Polarización estabilizada en el emisor')
        plt.xlabel('VCE [V]')
        plt.ylabel('IC [A]')
        plt.axhline(y=val_IC_Graph,color='purple',linestyle='--',xmin=0.05,xmax=0.95)
        plt.axvline(x=val_VCE_Graph,color='purple',linestyle='--',ymin=0.05,ymax=0.95)
        plt.show()

    def getTensionDividerEntries(self):
        self.DividerTensionEntries = ttk.LabelFrame(self.root, text='Ingrese valores')
        self.DividerTensionEntries.grid(column=2, row=2, padx=5, pady=5)
        self.dividerTension_Beta = ttk.Label(self.DividerTensionEntries, text='Beta')
        self.dividerTension_Beta.grid(column=0, row=0, padx=4, pady=2)
        self.entryDividerTension_Beta = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_Beta.grid(column=1, row=0, padx=4, pady=2)
        self.dividerTension_R1 = ttk.Label(self.DividerTensionEntries, text='R1')
        self.dividerTension_R1.grid(column=0, row=1, padx=4, pady=2)
        self.entryDividerTension_R1 = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_R1.grid(column=1, row=1, padx=4, pady=2)
        self.dividerTension_R2 = ttk.Label(self.DividerTensionEntries, text='R2')
        self.dividerTension_R2.grid(column=0, row=2, padx=4, pady=2)
        self.entryDividerTension_R2 = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_R2.grid(column=1, row=2, padx=4, pady=2)
        self.dividerTension_RC = ttk.Label(self.DividerTensionEntries, text='RC')
        self.dividerTension_RC.grid(column=0, row=3, padx=4, pady=2)
        self.entryDividerTension_RC = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_RC.grid(column=1, row=3, padx=4, pady=2)
        self.dividerTension_RE = ttk.Label(self.DividerTensionEntries, text='RE')
        self.dividerTension_RE.grid(column=0, row=4, padx=4, pady=2)
        self.entryDividerTension_RE = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_RE.grid(column=1, row=4, padx=4, pady=2)
        self.dividerTension_VCC = ttk.Label(self.DividerTensionEntries, text='VCC')
        self.dividerTension_VCC.grid(column=0, row=5, padx=4, pady=2)
        self.entryDividerTension_VCC = ttk.Entry(self.DividerTensionEntries)
        self.entryDividerTension_VCC.grid(column=1, row=5, padx=4, pady=2)
        self.btn = ttk.Button(self.DividerTensionEntries, text="Evaluar", command=self.ResultTensionDividerEntries)
        self.btn.grid(column=1, row=6, padx=4, pady=4)

    def ResultTensionDividerEntries(self):
        self.DividetTensionOut = ttk.LabelFrame(self.root, text='Resultados')
        self.DividetTensionOut.grid(column=2, row=3, padx=5, pady=5)
        self.valBeta_DividerTension = int(self.entryDividerTension_Beta.get())
        self.valR1_DividerTension = int(self.entryDividerTension_R1.get())
        self.valR2_DividerTension = int(self.entryDividerTension_R2.get())
        self.valRC_DividerTension = int(self.entryDividerTension_RC.get())
        self.valRE_DividerTension = int(self.entryDividerTension_RE.get())
        self.valVCC_DividerTension = int(self.entryDividerTension_VCC.get())

        self.valVTH_DividerTension = self.valVCC_DividerTension * (self.valR2_DividerTension / (self.valR1_DividerTension + self.valR2_DividerTension))
        self.valRTH_DividerTension = (self.valR1_DividerTension * self.valR2_DividerTension) / (self.valR1_DividerTension + self.valR2_DividerTension)
        if self.valRE_DividerTension == 0:
            self.valIB_DividerTension = (self.valVTH_DividerTension - 0.7) / (self.valRTH_DividerTension)
        else:
            self.valIB_DividerTension = (self.valVTH_DividerTension - 0.7) / (self.valRTH_DividerTension + ((self.valBeta_DividerTension + 1) * self.valRE_DividerTension))
            self.valICSat_DividerTension = (self.valVCC_DividerTension / (self.valRC_DividerTension + self.valRE_DividerTension))
        self.valIC_DividerTension = self.valBeta_DividerTension * self.valIB_DividerTension
        self.valIE_DividerTension = self.valIC_DividerTension + self.valIB_DividerTension
        self.valVCE_DividerTension = self.valVCC_DividerTension - (self.valIC_DividerTension * (self.valRC_DividerTension +self.valRE_DividerTension))

        self.valVB_DividerTension = (self.valVCC_DividerTension - (self.valIB_DividerTension * self.valRTH_DividerTension))
        self.valVC_DividerTension = (self.valVCC_DividerTension -(self.valIC_DividerTension * self.valRC_DividerTension))
        self.valVE_DividerTension = (self.valIE_DividerTension * self.valRE_DividerTension)

        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="VTH")
        self.label_DividerTension.grid(column=0, row=0, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valVTH_DividerTension)
        self.label_DividerTension.grid(column=1, row=0, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="RTH")
        self.label_DividerTension.grid(column=0, row=1, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valRTH_DividerTension)
        self.label_DividerTension.grid(column=1, row=1, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="IB")
        self.label_DividerTension.grid(column=0, row=2, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valIB_DividerTension)
        self.label_DividerTension.grid(column=1, row=2, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="IC")
        self.label_DividerTension.grid(column=0, row=3, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valIC_DividerTension)
        self.label_DividerTension.grid(column=1, row=3, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="IE")
        self.label_DividerTension.grid(column=0, row=4, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valIE_DividerTension)
        self.label_DividerTension.grid(column=1, row=4, padx=4, pady=2)

        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text="VB")
        self.label_DividerTension.grid(column=0, row=5, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text=self.valVB_DividerTension)
        self.label_DividerTension.grid(column=1, row=5, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text="VC")
        self.label_DividerTension.grid(column=0, row=6, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text=self.valVC_DividerTension)
        self.label_DividerTension.grid(column=1, row=6, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text="VE")
        self.label_DividerTension.grid(column=0, row=7, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text=self.valVE_DividerTension)
        self.label_DividerTension.grid(column=1, row=7, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="VCE")
        self.label_DividerTension.grid(column=0, row=8, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text=self.valVCE_DividerTension)
        self.label_DividerTension.grid(column=1, row=8, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut, text="IC Sat")
        self.label_DividerTension.grid(column=0, row=9, padx=4, pady=2)
        self.label_DividerTension = ttk.Label(self.DividetTensionOut,text=self.valICSat_DividerTension)
        self.label_DividerTension.grid(column=1, row=9, padx=4, pady=2)

        self.btn = ttk.Button(self.DividetTensionOut,text="Graficar",command=self.getTensionDividerGraph)
        self.btn.grid(column=1, row=10, padx=4, pady=4)




    def getTensionDividerGraph(self):
        val_VCCoff = [self.valVCC_DividerTension, 0]
        val_ICsat = [0, self.valICSat_DividerTension]
        val_VCE_Graph = self.valVCE_DividerTension
        val_IC_Graph = self.valIC_DividerTension

        plt.plot(val_VCCoff, val_ICsat, 'd-')
        plt.title('Polarización por dívisor de voltaje')
        plt.xlabel('VCE [V]')
        plt.ylabel('IC [A]')
        plt.axhline(y=val_IC_Graph,color='purple',linestyle='--',xmin=0.05,xmax=0.95)
        plt.axvline(x=val_VCE_Graph,color='purple',linestyle='--',ymin=0.05,ymax=0.95)
        plt.show()        

windows = GUI()
