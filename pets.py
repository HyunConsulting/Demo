class Pet:

    """
        This is class example documentation...
    """
    file_path = r"D:\Data\Text\\"
    def __init__(self,name:str=None,animal:str=None,colour:str=None):
        # pass
        self.name = name
        self.animal = animal
        self.colour = colour
        self._ifrecorded = None
    def __str__(self):
        # return readable text for this object
        return "{0} is a {1} and {2}".format(self.name,self.animal,self.colour)
    # @classmethod
    # def from_line(cls,line_of_text:str):
    #     # create a new pet object from this line of text
    #     nam, anima, colou = line_of_text.split(",")
    #     this_pet = cls(nam,anima,colou)
    #     return this_pet
    def save(self,file_name:str):
        # open file for writing
        with open(self.file_path + file_name,"a") as pet_file:
            pet_file.write("{0},{1},{2}\n".format(self.name,self.animal,self.colour))
    # get clause for property
    @property
    def ifrecorded(self):
        # initialise the hidden attribute
        self._ifrecorded = False
        # does this pet exist in the text file
        with open(self.file_path + "pet.txt","r") as pet_file:
            for line in pet_file:
                if line.upper().startswith(self.name.upper()+","):
                    self._ifrecorded = True
                    break
        return self._ifrecorded
    # set clause for property
    @ifrecorded.setter
    def ifrecorded(self,value):
        # if setting the value to be false, don't need to do anything

        self._ifrecorded=value
        if value == False:
            return
        # save this pet
        self.save("pet.txt")
    # deleting the property
    # @ifrecorded.deleter
    # def ifrecorded(self):
    #     del self._ifrecorded
# create a new pet
# annie = Pet()
# pet = Pet()
alfie = Pet("alfie","dog","black")
neo = Pet("neo","cat","black")
annie = Pet("Annie","cat","white")
    
# print them out
# print(neo.name,annie.animal,annie.colour)
# print(annie.name,pet.animal,pet.colour)

# instance attributes created on the fly
# class attribute

# put pets in list and print
pets = [alfie,neo,annie]
for pet in pets:
    print(pet.name,pet.animal,pet.file_path)
    # if not already in text file, add this pet
    # if not pet.ifrecorded:
    #     pet.ifrecorded = True
# Print documentation for class
print(Pet.__doc__)
print(annie)
# pets = []
# with open(r"D:\Data\Text\pet.txt") as pet_file:
#     #read in all but first line
#     lines = pet_file.read().splitlines()[1:]
#     #create per from each line
#     for line in lines:
#         # print(line)
#         new_pet = Pet.from_line(line)
#         pets.append(new_pet)

# list out pets
# for pet in pets:
#     print(pet.name,pet.animal,pet.colour)
# annie.ifrecorded = True
# print(annie.ifrecorded)
# import pandas
# df = pandas.DataFrame()