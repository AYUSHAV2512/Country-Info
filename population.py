import csv
def main():
        print("Input 1 for population info.")
        print("Input 2 for Covid info.")
        print("Input 3 to exit.")
        choice  = int(input("Your choice: "))
        while choice != 3:
            if ( choice == 1):
                populationInfo()
                print("Input 1 for population info.")
                print("Input 2 for Covid info.")
                print("Input 3 to exit.")
                choice = int(input("Your choice: "))
            if(choice == 2):
                covidInfo()
                print("Input 1 for population info.")
                print("Input 2 for Covid info.")
                print("Input 3 to exit.")
                choice = int(input("Your choice: "))
            if(choice == 3):
                break





def covidInfo():
    with open ("covid.csv") as C:
        reader = csv.reader(C)
        next(C)
        while (True):
            name = str(input("Enter the name of a country or input exit to exit: ", ))
            if name == "exit":
                break
            for lines in reader:
                country = str(lines[2]);
                total_cases = str(lines[4])
                new_cases = str(lines[5])
                totalDeath = str(lines[7])
                reproduction = str(lines[16])
                totalTests = str(lines[26])
                positivityRate = str(lines[31])
                vaccination = str(lines[34])

                if name == country:
                    print("Number of total cases are: ", total_cases)
                    print("Number of new cases are :", new_cases)
                    print("Total deaths: ", totalDeath)
                    print("Rate of reproduction is : "+reproduction+"%")
                    print("Total number of tests are :  ", totalTests)
                    print("Rate of positivity is :  ", positivityRate)
                    print("Total number vaccination :  ", vaccination)


            C.seek(0, 0)


def populationInfo():
    with open ("AsiaPopulation2020.csv") as F:
        reader = csv.reader(F)
        next(F)
        while (True):
            name = str(input("Enter the name of a country in Asia or input exit to exit: ", ))
            if name == "exit":
                break
            for lines in reader:
                all_details = str(lines)
                country = str(lines[0])
                population = str(lines[1])
                net_change = str(lines[3])
                density = str(lines[4])
                area = str(lines[5])
                share = str(lines[10])

                if name == country:
                    print("Population of the coutry is: ",population)
                    print("Yearly Net change of population is:",net_change)
                    print("Density per sq Km is : ",density)
                    print("Area of the country is: ",area+"P/sqKM")
                    print("% Share to the world population is ",share)

            F.seek(0, 0)





if __name__ == '__main__':
    main()