#Covid Data Analysis



Covid_Data = [["age bracket",["BC","AB","SK"]],
              [(12,17),[[212286,303122],[200521,315968],[51128,87621]]],
              [(18,29),[[576245,816781],[412013,695111],[100170,181751]]],
              [(30,39),[[561039,740505],[459399,715542],[106941,172421]]],
              [(40,49),[[514551,649358],[437833,608434],[102214,143466]]]]

Covid_Data_Province = [province for province in Covid_Data[0][1]  ]
Covid_Data_AgeRange = [age[0] for age in Covid_Data]
del Covid_Data_AgeRange[0]
ageRange_length = len(Covid_Data_AgeRange)

#print(ageRange_length)
#print (len(Covid_Data))
#print(Covid_Data_AgeRange.index((18,29)))
#Province = 'AB'
#ProvinceIndex = Covid_Data_Province.index(Province)


#print(Covid_Data[3][1][0][1])
#print(ProvinceIndex)


def prov_percent_vaccinated_in_age_range(Covid_Data,Province,lowAge,highAge ):
    x = 0
    vacPopulationTotal = 0
    totalPopulation = 0
    ProvinceIndex = Covid_Data_Province.index(Province)

    while x < ageRange_length:
        AgeIndex1 = Covid_Data_AgeRange[x][0]
        AgeIndex2 =Covid_Data_AgeRange[x][1]
        totalPopulationAgeProvince = Covid_Data[x+1][1][ProvinceIndex][1]
        vacPopulationAgeProvince = Covid_Data[x+1][1][ProvinceIndex][0]
        if lowAge in range(AgeIndex1, AgeIndex2 + 1):
            #print(vacPopulationTotal)
            vacPopulationTotal = vacPopulationTotal + vacPopulationAgeProvince

            totalPopulation = totalPopulation + totalPopulationAgeProvince

        if highAge in range(AgeIndex1, AgeIndex2 + 1):
            #print(vacPopulationTotal)
            vacPopulationTotal = vacPopulationTotal + vacPopulationAgeProvince

            totalPopulation = totalPopulation + totalPopulationAgeProvince

        x = x + 1


    percentProvAge = (vacPopulationTotal / totalPopulation) * 100

    return percentProvAge



def percent_vaccinated_in_age_range(Covid_Data,lowage, highage):
    print('In the age range '+str(lowage)+ ' to '+str(highage))
    j = 0
    while j < len(Covid_Data_Province):

        Prov = Covid_Data_Province[j]
        percent= prov_percent_vaccinated_in_age_range(Covid_Data, Prov, lowage, highage)
        print('\t in ' +Covid_Data_Province[j] +' '+str(round(percent,1))+ ' percentage of the people are fully vaccinated' )
        j = j + 1

call1 = percent_vaccinated_in_age_range(Covid_Data,30,49)
call2 = percent_vaccinated_in_age_range(Covid_Data,12,29)



#vacPopulationAgeProvince = Covid_Data[1][1][1][0]

def add_vaccinated_in_age_bracket(Covid_Data,province,agebracket,fullVacPop):

    Ageindex =Covid_Data_AgeRange.index(agebracket)

    provinceIndex = Covid_Data_Province.index(province)

    vacPopulationAgeProvince = Covid_Data[Ageindex +1][1][provinceIndex][0]

    Covid_Data[Ageindex +1][1][provinceIndex][0] = vacPopulationAgeProvince + fullVacPop

    return None
test = add_vaccinated_in_age_bracket(Covid_Data,'SK', (12,17),10000)
print("-- After High School Vaccination Blitz--")
call2 = percent_vaccinated_in_age_range(Covid_Data,12,29)