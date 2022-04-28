# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

# User input for encoded string
encodedString = input("Please input the encoded string: ")

#User input of location of K
digitalKplace = input("Please input the location of the number in the encoded string: ")

def decodedString():

    """  Function decodes encodedString 
 
    :return: string value of decoded string 'string_decoded    
    """""
    # K in integer value
    K = int(encodedString[(int(digitalKplace) - 1)])

    # characters of the string before K
    string_BeforeK = encodedString[0:(int(digitalKplace) - 1)]
    #characters of the string after k
    string_AfterK = encodedString[(int(digitalKplace)):len(encodedString)]
    #Character String before K multiplied by K
    KxString_Before = string_BeforeK * K

    #reverse string
    rev_KxString_before = KxString_Before[len(KxString_Before)::-1]

    rev_string_AfterK = string_AfterK[len(string_AfterK)::-1]

    string_decoded = rev_string_AfterK + rev_KxString_before

    return string_decoded

def find_keychar():

    """Function finds the key character location
    :return Integer location of key character """
    if len(decoded_string) % 2 == 0:
        key_Char = int((len(decoded_string) / 2 )+ 1 )

    else:

        key_Char = int((len(decoded_string)) / 2 )
    return key_Char


decoded_string = decodedString()
theKey = find_keychar()



print("The decoded string is:  " + decoded_string)

print("The key character of the decoded string is: " + decoded_string[(theKey -1)])

