# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

encodedString = input("Please input the encoded String: ")

digitalKplace = input("Please input the location of the number in the encoded string: ")

# def decodedString():


K = int(encodedString[(int(digitalKplace) - 1)])

string_BeforeK = encodedString[0:(int(digitalKplace) - 1)]

string_AfterK = encodedString[(int(digitalKplace)):len(encodedString)]

KxString_Before = string_BeforeK * K

rev_KxString_before = KxString_Before[len(KxString_Before)::-1]

rev_string_AfterK = string_AfterK[len(string_AfterK)::-1]

string_decoded = rev_string_AfterK + rev_KxString_before

print("The decoded string is:  " + string_decoded)


keyChar = int((len(string_decoded)) / 2 + 1)

print(K)
