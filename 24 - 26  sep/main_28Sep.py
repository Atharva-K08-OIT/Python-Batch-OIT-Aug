# filename = "text.txt"

# fp = open(filename,"w")
# fp.close()

# # -----------------------------

# fileName = "temp.txt"

# with open(fileName,"w") as fp:
#     fp.write("Hello, world!")

# # -------------------------------

# methods of fp

# filename = "zoo.txt"

# with open(filename, "r") as fp:
#     data = fp.readlines()
#     print(data[3])


# info = [
#         '\n',
#         'Animal 04\n',
#         '\n',
#         'Lion:\n',
#         'The lion is a large cat of the genus Panthera, native to Africa and India. \n',
#         'It has a muscular, broad-chested body; a short, rounded head; round ears; \n',
#         'and a dark, hairy tuft at the tip of its tail. \n', 'It is sexually dimorphic; \n',
#         'adult male lions are larger than females and have a prominent mane.\n',
#         '\n',
#         'Animal 05\n',
#         '\n', 'Cheetah:\n',
#         'The cheetah is a large cat and the fastest land animal. \n',
#         'It has a tawny to creamy white or \n',
#         'pale buff fur that is marked with evenly spaced, solid black spots. \n',
#         'The head is small and rounded, with a short snout and black tear-like facial streaks\n',
#         '\n',
#         'Animal 06\n',
#         '\n',
#         'Elephants:\n',
#         'Elephants are the largest living land animals. \n',
#         'Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. \n',
#         'They are the only surviving members of the family Elephantidae and the order Proboscidea; \n',
#         'extinct relatives include mammoths and mastodons\n'
#         ]


# with open(filename,"a") as fp:
#     fp.writelines(info)


# --------------------------------------------------------------

filename = "demo.txt"
with open(filename, 'w') as fp:
    fp.write(
        '''Raju is a curious and energetic young boy who loves exploring the world around him.
He is always eager to learn new things and never shies away from asking questions.
With his bright smile and positive attitude, Raju easily makes friends and is well-liked by everyone.
Raju enjoys spending his free time playing sports, reading books, and discovering new hobbies.
His teachers often praise him for his hard work and dedication to his studies.
Despite his playful nature, Raju is known for being responsible and caring, often helping his family and friends when needed.
        '''
    )


fp = open(filename,"r")
fp.seek(10)
data = fp.readline()
print(data)
fp.close()


fp = open(filename,"a")
fp.truncate(200)
fp.close()

