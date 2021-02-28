from tkinter import *
import pathlib
from math import *
from tkinter import simpledialog, messagebox
from playsound import playsound

#functions from buttons go here:

def idealgaslaw():


    #functions for buttons
    def pressureunknown():
        pressureentry.delete(0,"end")
        pressureentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def volumeunknown():
        volumeentry.delete(0, "end")
        volumeentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def molsunknown():
        molentry.delete(0, "end")
        molentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def temperatureunknown():
        temperatureentry.delete(0, "end")
        temperatureentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def calculate():
        pressure = str(pressureentry.get())
        volume = str(volumeentry.get())
        mols = str(molentry.get())
        temperature = str(temperatureentry.get())




        if(pressure =="Unknown Variable" and volume != "Unknown Variable" and mols != "Unknown Variable" and temperature != "Unknown Variable"):
            answer = float((float(mols)*float(0.08206)*float(temperature))/float(volume))
            #result.destroy()
            #result = Label(iglmain, text="Pressure = "+str(answer)+" atm")
            #result.grid(row=5, column=2)
            result.config(text="Pressure = "+str(answer)+" atm")

            playsound("calculation_jingle.mp3")

        elif(volume == "Unknown Variable" and pressure != "Unknown Variable" and mols != "Unknown Variable" and temperature != "Unknown Variable"):
            answer = float((float(mols)*float(0.08206)*float(temperature))/float(pressure))
            #result.destroy()
            #result = Label(iglmain, text="Volume = " + str(answer) + " mL")
            #result.grid(row=5, column=2)
            result.config(text="Volume = " + str(answer) + " mL")

            playsound("calculation_jingle.mp3")

        elif(mols == "Unknown Variable" and pressure != "Unknown Variable" and volume != "Unknown Variable" and temperature != "Unknown Variable"):
            answer = float((float(pressure)*float(volume))/(float(0.08206)*float(temperature)))
            #result.destroy()
            #result = Label(iglmain, text="mols = " + str(answer) + " mols")
            #result.grid(row=5, column=2)
            result.config(text="mols = " + str(answer) + " mols")

            playsound("calculation_jingle.mp3")

        elif(temperature == "Unknown Variable" and pressure != "Unknown Variable" and volume != "Unknown Variable" and mols != "Unknown Variable"):
            answer = float((float(pressure)*float(volume))/(float(0.08206)*float(mols)))
            #result.destroy()
            #result = Label(iglmain, text="Temperature = " + str(answer) + " K")
            #result.grid(row=5, column=2)
            result.config(text="Temperature = " + str(answer) + " K")

            playsound("calculation_jingle.mp3")

        else:
            messagebox.showerror("Error!", "Cannot have two unknown variables or no unknown variables")
            playsound("error_jingle.mp3")



    #home screen
    global iglmain
    iglmain = Tk()
    iglmain.title("Ideal Gas Law Calculator")
    iglmain.geometry("500x300")

    iglmain.iconbitmap(str(pathlib.Path(__file__).parent.absolute()) + "/Icon.ico")

    #pressure
    pressurelabel = Label(iglmain, text="Enter Pressure in atmospheres:")
    pressurelabel.grid(row=0, column=0)

    pressureentry = Entry(iglmain, width=20)
    pressureentry.grid(row=0, column=1)

    pressureunknown = Button(iglmain, text="Press if this is your unknown variable", command=pressureunknown)
    pressureunknown.grid(row=0, column=2)

    #volume
    volumelabel = Label(iglmain, text="Enter Volume in milliLiters:")
    volumelabel.grid(row=1, column=0)

    volumeentry = Entry(iglmain, width=20)
    volumeentry.grid(row=1, column=1)

    volumeunknown = Button(iglmain, text="Press if this is your unknown variable", command=volumeunknown)
    volumeunknown.grid(row=1, column=2)

    #mols
    mollabel = Label(iglmain, text="Enter mols in mols:")
    mollabel.grid(row=2, column=0)

    molentry = Entry(iglmain, width=20)
    molentry.grid(row=2, column=1)

    molunknown = Button(iglmain, text="Press if this is your unknown variable", command=molsunknown)
    molunknown.grid(row=2, column=2)

    #temperature
    temperaturelabel = Label(iglmain, text="Enter Temperature in Kelvin:")
    temperaturelabel.grid(row=3, column=0)

    temperatureentry = Entry(iglmain, width=20)
    temperatureentry.grid(row=3, column=1)

    temperatureunknown = Button(iglmain, text="Press if this is your unknown variable", command=temperatureunknown)
    temperatureunknown.grid(row=3, column=2)

    #calculate button and other
    equationlabel = Label(iglmain, text="PV = nRT")
    equationlabel.grid(row=4, column=0)

    calculatebutton = Button(iglmain, text="Calculate for unknown variable", command=calculate)
    calculatebutton.grid(row=4, column=2)

    result = Label(iglmain, text="")
    result.grid(row=5, column=2)

    playsound("equation_select_jingle.mp3")

def ptheorem():
    #functionsforbutton

    def aunknown():
        aentry.delete(0, "end")
        aentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def bunknown():
        bentry.delete(0, "end")
        bentry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def cunknown():
        centry.delete(0, "end")
        centry.insert(0, "Unknown Variable")

        playsound("unknown_jingle.mp3")

    def calculate():

        variablea = str(aentry.get())
        variableb = str(bentry.get())
        variablec = str(centry.get())

        if(variablea == "Unknown Variable" and variableb != "Unknown Variable" and variablec != "Unknown Variable"):
            csquared = float(float(variablec)**2)
            bsquared = float(float(variableb)**2)

            answer = float(sqrt(csquared - bsquared))
            result.config(text="a = "+str(answer))
            playsound("calculation_jingle.mp3")


        elif(variableb == "Unknown Variable" and variablea != "Unknown Variable" and variablec != "Unknown Variable"):
            csquared = float(float(variablec) ** 2)
            asquared = float(float(variablea) ** 2)

            answer = float(sqrt(csquared - asquared))
            result.config(text="b = " + str(answer))
            playsound("calculation_jingle.mp3")


        elif(variablec == "Unknown Variable" and variablea != "Unknown Variable" and variableb != "Unknown Variable"):
            asquared = float(float(variablea) ** 2)
            bsquared = float(float(variableb) ** 2)

            answer = float(sqrt(asquared + bsquared))
            result.config(text="c = " + str(answer))
            playsound("calculation_jingle.mp3")


        else:
            messagebox.showerror("Error!", "Cannot have more than one unknown variables or no unknown variables")
            playsound("error_jingle.mp3")



    #home screen
    global pythhome
    pythhome = Tk()
    pythhome.title("Pythagorian Thereom Calculator")
    pythhome.geometry("500x500")
    pythhome.iconbitmap(str(pathlib.Path(__file__).parent.absolute()) + "/Icon.ico")

    #a
    alabel = Label(pythhome, text="Enter variable a:")
    alabel.grid(row=0, column=0)

    aentry = Entry(pythhome, width=20)
    aentry.grid(row=0, column=1)

    aunknownbutton = Button(pythhome, text="Press if this is your unknown variable", command=aunknown)
    aunknownbutton.grid(row=0, column=2)


    #b
    blabel = Label(pythhome, text="Enter variable b:")
    blabel.grid(row=1, column=0)

    bentry = Entry(pythhome, width=20)
    bentry.grid(row=1, column=1)

    bunknownbutton = Button(pythhome, text="Press if this is your unknown variable", command=bunknown)
    bunknownbutton.grid(row=1, column=2)

    #c
    clabel = Label(pythhome, text="Enter variable c:")
    clabel.grid(row=2, column=0)

    centry = Entry(pythhome, width=20)
    centry.grid(row=2, column=1)

    cunknownbutton = Button(pythhome, text="Press if this is your unknown variable", command=cunknown)
    cunknownbutton.grid(row=2, column=2)

    #calculate button and others
    equationlabel = Label(pythhome, text="a\u00b2 + b\u00b2 = c\u00b2")
    equationlabel.grid(row=3, column=0)

    calculatebutton = Button(pythhome, text="Calculate for unknown variable", command=calculate)
    calculatebutton.grid(row=3, column=2)

    result = Label(pythhome, text="")
    result.grid(row=4, column=2)

    playsound("equation_select_jingle.mp3")

def phcalculator():
    #functions for buttons
    def calculate():
        hplus = str(phentry.get())

        answer = float(-log(float(hplus)))
        if(answer == 0):
            answer = float(-answer)

        result.config(text="pH = "+str(answer))

        poh.config(text="pOH = "+str(14-answer))
        poh.grid(row=2, column=1)

        playsound("calculation_jingle.mp3")

    #main
    phhome = Tk()
    phhome.title("pH Calculator")
    phhome.geometry("400x150")
    phhome.iconbitmap(str(pathlib.Path(__file__).parent.absolute()) + "/Icon.ico")

    phlabel = Label(phhome, text="enter concentration of H\u207a")
    phlabel.grid(row=0, column=0)

    phentry = Entry(phhome, width=20)
    phentry.grid(row=0, column=1)

    calculatebutton = Button(phhome, text="Calculate for pH", command=calculate)
    calculatebutton.grid(row=0, column=2)

    result = Label(phhome, text="")
    result.grid(row=1, column=1)

    poh = Label(phhome, text="")
    poh.grid(row=2, column=1)

    playsound("equation_select_jingle.mp3")

def pohcalculator():
    # functions for buttons
    def calculate():
        ohminus = str(pohentry.get())

        answer = float(-log(float(ohminus)))
        if (answer == 0):
            answer = float(-answer)

        result.config(text="pOH = " + str(answer))

        ph.config(text="pH = " + str(14-answer))
        ph.grid(row=2, column=1)

        playsound("calculation_jingle.mp3")

    # main
    pohhome = Tk()
    pohhome.title("pOH Calculator")
    pohhome.geometry("400x150")
    pohhome.iconbitmap(str(pathlib.Path(__file__).parent.absolute()) + "/Icon.ico")

    pohlabel = Label(pohhome, text="enter concentration of OH\u207b")
    pohlabel.grid(row=0, column=0)

    pohentry = Entry(pohhome, width=20)
    pohentry.grid(row=0, column=1)

    calculatebutton = Button(pohhome, text="Calculate for pOH", command=calculate)
    calculatebutton.grid(row=0, column=2)

    result = Label(pohhome, text="")
    result.grid(row=1, column=1)

    ph = Label(pohhome, text="")
    ph.grid(row=2, column=1)

    playsound("equation_select_jingle.mp3")

def consolecalculator():


    def idealGasLaw():
        print("Ideal Gas Law: PV=nRT")
        print("Choose variable.(example: \"P\" will solve for pressure")
        select = str(input())

        if (select == "P" or select =="p"):
            print("Solving for pressure.")
            moles = float(input("Input moles"))
            temp = float(input("Input temperature (K)"))
            vol = float(input("Input volume (mL)"))
            ans = ((moles * temp * .08206) / vol)
            print("Answer: ", ans, " atm")

        elif (select == "V" or select == "v"):
            print("Solving for volume.")
            moles = float(input("Input moles"))
            temp = float(input("Input temperature (K)"))
            pres = float(input("Input pressure (atm)"))
            ans = ((moles * temp * .08206) / pres)
            print("Answer: ", ans, " mL")

        elif (select == "n" or select == "N"):
            print("Solving for moles.")
            pres = float(input("Input pressure (atm)"))
            vol = float(input("Input volume (mL)"))
            temp = float(input("Input temperature (K)"))
            ans = ((pres * vol) / (temp * .08206))
            print("Answer: ", ans, " moles")

        elif (select == "T" or select =="t"):
            print("Solving for temperature.")
            pres = float(input("Input pressure (atm)"))
            vol = float(input("Input volume (mL)"))
            moles = float(input("Input moles"))
            ans = ((pres * vol) / (moles * .08206))
            print("Answer: ", ans, " C")

        else:
            print("Invalid Input. Action Cancelled.")
            start()


    def pythagoreanTheorem():
        print("Pythagorean theorum: a^2 + b^2 = c^2")
        print("Hypotenuse or Leg? (Input h or l)")
        select = str(input())

        if (select == "h"):
            print("Solving for hypotenuse.")
            a = float(input("Input first leg's length"))
            b = float(input("Input second leg's length"))
            ans = sqrt((a ** 2) + (b ** 2))
            print("Answer: ", ans, " units)")

        elif (select == "l"):
            print("Solving for leg.")
            c = float(input("Input hypotenuse's length"))
            b = float(input("Input other leg's length"))
            ans = sqrt((c ** 2) - (b ** 2))
            print("Answer: ", ans, " units)")

        else:
            print("Invalid Input. Action Cancelled.")
            start()



    def findpH():
        print("ph = -log([H+})")
        conc = float(input("Input H+ concentration"))
        if (conc > 1):
            print("Out of Domain. Action Cancelled.")
            start()

        elif (conc <= 0):
            print("Out of Domain. Action Cancelled.")
            start()

        else:
            ans = (-log(conc, 10))
            print("Answer: ", ans, " pH units)")



    def findpOH():
        print("ph = -log([OH-})")
        conc = float(input("Input OH- concentration"))
        if (conc > 1):
            print("Out of Domain. Action Cancelled.")
            start()
        elif (conc <= 0):
            print("Out of Domain. Action Cancelled.")
            start()
        else:
            ans = (-log(conc, 10))
            print("Answer: ", ans, " pOH units)")



    def massEnergy():
        print("Mass-Energy Equivalence: e=mc^2")
        print("Find Mass or Energy? (m/e)")
        select = str(input())

        if (select == "e"):
            print("Solving for energy.")
            mass = float(input("Input mass (kg)"))
            ans = (mass * (299792458 ** 2))
            print("Answer: ", ans, " Joules)")

        elif (select == "m"):
            print("Solving for mass.")
            en = float(input("Input energy (J)"))
            ans = (en / (299792458 ** 2))
            print("Answer: ", ans, " kg)")

        else:
            print("Invalid Input. Action Cancelled.")
            start()



    def newtSecond():
        print("Newton's second law: F = ma")
        print("Choose variable.")
        select = str(input())

        if (select == "F"):
            print("Solving for force.")
            mass = float(input("Input mass (kg)"))
            accel = float(input("Input acceleration (m/s^2)"))
            ans = (mass * accel)
            print("Answer: ", ans, " N")

        elif (select == "m"):
            print("Solving for mass.")
            accel = float(input("Input acceleration (m/s^2)"))
            force = float(input("Input Force (N)"))
            ans = (accel / force)
            print("Answer: ", ans, " kg)")

        elif (select == "a"):
            print("Solving for mass.")
            mass = float(input("Input mass (kg)"))
            force = float(input("Input Force (N)"))
            ans = (mass / force)
            print("Answer: ", ans, " m/s^2)")

        else:
            print("Invalid Input. Action Cancelled.")
            start()



    def gravAccel():
        print("Gravitational acceleration (weight): W = mg")
        print("Choose variable.")
        select = str(input())

        if (select == "W"):
            print("Solving for weight.")
            mass = float(input("Input mass (kg)"))
            grav = float(input("Input gravitational constant (m/s^2)"))
            ans = (mass * grav)
            print("Answer: ", ans, " N")

        elif (select == "m"):
            print("Solving for mass.")
            weight = float(input("Input weight (N)"))
            grav = float(input("Input gravitational constant (m/s^2)"))
            ans = (weight / grav)
            print("Answer: ", ans, " kg)")

        elif (select == "g"):
            print("Solving for mass.")
            weight = float(input("Input weight (N)"))
            mass = float(input("Input mass (kg)"))
            ans = (weight / mass)
            print("Answer: ", ans, " m/s^2)")

        else:
            print("Invalid Input. Action Cancelled.")
            start()


    def start():
        print(" 1: Ideal Gas Law \n 2: Pythagorean Theorem \n 3: pH \n 4: pOH \n 5: Einstein's theory of relativity \n 6: Newton's second law \n 7: Gravitational Acceleration")
        initial = str(input("Please enter the number next to the calculator you wish to use from the list above: "))

        if (initial == "1"):
            idealGasLaw()

        elif (initial == "2"):
            pythagoreanTheorem()

        elif(initial == "3"):
            findpH()

        elif(initial == "4"):
            findpOH()

        elif(initial == "5"):
            massEnergy()

        elif(initial == "6"):
            newtSecond()

        elif(initial == "7"):
            gravAccel()

        else:
            print("hmmmm... Your'e number was not found. Please try again...")
            start()

    start()

#main screen
main = Tk()
main.title("Equation Calculator by Peteous")
main.geometry("500x500")
main.iconbitmap(str(pathlib.Path(__file__).parent.absolute()) + "/Icon.ico")

welcome = Label(main, text="Welcome! click one of the buttons below to open a calculator.")
welcome.pack()

idealgaslawbutton = Button(main, text="Ideal Gas Law Calculator", command=idealgaslaw)
idealgaslawbutton.pack()

pythagorian = Button(main, text="Pythagorean Theorem Calculator", command=ptheorem)
pythagorian.pack()

ph = Button(main, text="pH Calculator", command=phcalculator)
ph.pack()

poh = Button(main, text="pOH Calculator", command=pohcalculator)
poh.pack()

consolecalc = Button(main, text="Press to activate console calculators", command=consolecalculator)
consolecalc.pack()

main.mainloop()