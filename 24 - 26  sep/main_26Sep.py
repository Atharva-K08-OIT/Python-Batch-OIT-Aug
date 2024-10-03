# Ex. 1
# filename = "zoo.txt"

# fp = open(filename,"w")

# data = '''
# Animal 01

# Lion:
# The lion is a large cat of the genus Panthera, native to Africa and India. 
# It has a muscular, broad-chested body; a short, rounded head; round ears; 
# and a dark, hairy tuft at the tip of its tail. 
# It is sexually dimorphic; 
# adult male lions are larger than females and have a prominent mane

# Animal 02

# Cheetah:
# The cheetah is a large cat and the fastest land animal. 
# It has a tawny to creamy white or 
# pale buff fur that is marked with evenly spaced, solid black spots. 
# The head is small and rounded, with a short snout and black tear-like facial streaks
# '''

# fp.write(data)
# fp.close()

# newData = '''
# Animal 03

# Elephants:
# Elephants are the largest living land animals. 
# Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. 
# They are the only surviving members of the family Elephantidae and the order Proboscidea; 
# extinct relatives include mammoths and mastodons
# '''

# fp = open(filename,"a")

# fp.write(newData)
# fp.close()


# filename = "zoo.txt"

# fp = open(filename,"r")

# info = fp.read()

# print(info)

# fp.close()
# --------------------------------------------------------------

# # Ex.2 
# filename = "itProjects.txt"

# # fp = open(filename,"x") # create mode

# fp = open(filename,"w")

# data = '''
# Project 01

# Facial recognition system:
# The facial recognition system is 
# a biometric system that uses facial features to identify or verify an individual.
# It is a type of biometric authentication that uses a camera to capture images of a person's face
# and then compares them to a database of known faces to determine if there is a match.

# Project 02

# Credit card safety application
# The credit card safety application is a mobile application that helps 
# users protect their credit cards from fraud.
# It uses machine learning algorithms to detect suspicious transactions 
# and alerts the user if a transaction is flagged as suspicious.
# '''

# fp.write(data)

# fp.close()


# fp = open(filename,"a")

# newData = '''
# Project 03

# Airline ticketing system:
# The airline ticketing system is a web-based application that allows users to book flights, manage their bookings
# and access their flight information.
# '''

# fp.write(newData)

# fp.close()

# --------------------------------------------------

# filename = "itProjects.txt"

# fp = open(filename,"r")

# details = fp.read()

# print(details)

# fp.close()