import files
import easygui as eg

values = eg.multenterbox("Entrez trois nombres", "Identification", [
                         "nombre1", "nombre2", "nombre3"])

results = files.trinome(float(values[0]), float(values[1]), float(values[2]))

eg.msgbox("Résultats : " + str(results))
