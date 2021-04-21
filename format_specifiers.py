#format specifiers
print("I have {0:d} cats".format(6))
print("I have {0:03d} cats".format(6))
print("I have {0:3d} cats".format(6))
print("I have {3:d} cats".format(6,3,4,7))
print("I have {1:d} cats".format(6,3,4,7))

print("I have {1:04d} cats".format(6,3,4,7))
print("I have {1:f} cats".format(6,3,4,7))
print("I have {2:.2f} cats".format(6,3,4,7))
