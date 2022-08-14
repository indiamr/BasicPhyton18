#Class Chapter
class mentee():
#    name = 'Default'
#    age = 'Default'

   def __init__(self, name, age):
    self.name = name
    self.age = age
   

   def belajar(self):
      print (self.name, "sedang belajar")
   def bermain(self, tambahan):
      print (self.name, "berumur" , self.age, "tahun", "sedang bermain", tambahan)

   
#main program
sari = mentee("Sari Musaeri",27)
jeje = mentee("Jeje Marhenje",23)
bonge = mentee("Bonge Marenge",25)

print(sari.name)
print(sari.age)
# sari.name = "Sari Musaeri"
# jeje.name = "Jeje Marhenje"
# bonge.name = "Bonge Saringe"

# sari.age = 27
# jeje.age = 23
# bonge.age = 25

# print(sari.name)
# print(jeje.name)
# print(bonge.name)

# sari.bermain()
# jeje.belajar()