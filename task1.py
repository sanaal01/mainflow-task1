list=[1,24,5,6,2]
print("Original: ",list)
list.append(3)
print("Updated List: ",list)
list .remove(2)
print("Updated List: ",list)
list[4]=56
print("Updated List: ",list)

#Dictionaries
dict={"Name":"ABC","Age":18}
print("Original:",dict)
dict["Birth_year"]=2006
print("Updated Dictionary: ",dict)
dict.pop("Age")
print("Updated Dictionary: ",dict)
dict.update({"Name":"JKL"})
print("Updated Dictionary: ",dict)

#Set
set={"Ford","BMW","Toyota","Rolls Royce"}
print("Original: ",set)
set.add("Porsche")
print("Updated Set: ",set)
set.remove("Toyota")
print("Updated Set: ",set)