#register recognition for R-type
def r_type(string):
    if string == "$s0," or string == "$s0":
        return bin(0)[2:].zfill(3)
    elif string == "$s1," or string == "$s1":
        return bin(1)[2:].zfill(3)
    elif string == "$s2," or string == "$s2":
        return bin(2)[2:].zfill(3)
    elif string == "$s3," or string == "$s3":
        return bin(3)[2:].zfill(3)
    elif string == "$s4," or string == "$s4":
        return bin(4)[2:].zfill(3)
    elif string == "$s5," or string == "$s5":
        return bin(5)[2:].zfill(3)
    elif string == "$s6," or string == "$s6":
        return bin(6)[2:].zfill(3)
    elif string == "$s7," or string == "$s7":
        return bin(7)[2:].zfill(3)
#register recognition for I-type
def i_type(string):
    if string == "$s0," or string == "$s0" or string == "0":
        return bin(0)[2:].zfill(3)
    elif string == "$s1," or string == "$s1" or string == "1":
        return bin(1)[2:].zfill(3)
    elif string == "$s2," or string == "$s2" or string == "2":
        return bin(2)[2:].zfill(3)
    elif string == "$s3," or string == "$s3" or string == "3":
        return bin(3)[2:].zfill(3)
    elif string == "$s4," or string == "$s4" or string == "4":
        return bin(4)[2:].zfill(3)
    elif string == "$s5," or string == "$s5" or string == "5":
        return bin(5)[2:].zfill(3)
    elif string == "$s6," or string == "$s6" or string == "6":
        return bin(6)[2:].zfill(3)
    elif string == "$s7," or string == "$s7" or string == "7":
        return bin(7)[2:].zfill(3)

#register recognition for load-store-type
def lw_sw(string):
    if string == "$s0," or string == "$s0":
        return bin(0)[2:].zfill(3)
    elif string == "$s1," or string == "$s1":
        return bin(1)[2:].zfill(3)
    elif string == "$s2," or string == "$s2":
        return bin(2)[2:].zfill(3)
    elif string == "$s3," or string == "$s3":
        return bin(3)[2:].zfill(3)
    elif string == "$s4," or string == "$s4":
        return bin(4)[2:].zfill(3)
    elif string == "$s5," or string == "$s5":
        return bin(5)[2:].zfill(3)
    elif string == "$s6," or string == "$s6":
        return bin(6)[2:].zfill(3)
    elif string == "$s7," or string == "$s7":
        return bin(7)[2:].zfill(3)

f = open("assembly_code.txt", "r")
r = open("output_bin.txt", "w")
for x in f:
    my_string = "" #taking a new string to store binary output
    s = x
    result = s.split() #here the assembly gets splitted into pieces by black spaces
    if result[0] == "add":
        my_string += bin(0)[2:].zfill(3)
        my_string += r_type(result[1])
        my_string += r_type(result[2])
        my_string += r_type(result[3])
    elif result[0] == "sub":
        my_string += bin(1)[2:].zfill(3)
        my_string += r_type(result[1])
        my_string += r_type(result[2])
        my_string += r_type(result[3])
    elif result[0] == "muli":
        my_string += bin(2)[2:].zfill(3)
        my_string += i_type(result[1])
        my_string += i_type(result[2])
        my_string += i_type(result[3])
    elif result[0] == "divi":
        my_string += bin(3)[2:].zfill(3)
        my_string += i_type(result[1])
        my_string += i_type(result[2])
        my_string += i_type(result[3])
    elif result[0] == "lw":
        my_string += bin(4)[2:].zfill(3)
        my_string += lw_sw(result[1])
        offset_reg = result[2]
        off_reg = offset_reg[2:5]
        my_string += lw_sw(off_reg)
        offset = result[2]
        off = offset[0]
        my_string += bin(int(off))[2:].zfill(3)
    elif result[0] == "sw":
        my_string += bin(5)[2:].zfill(3)
        my_string += lw_sw(result[1])
        offset_reg = result[2]
        off_reg = offset_reg[2:5]
        my_string += lw_sw(off_reg)
        offset = result[2]
        off = offset[0]
        my_string += bin(int(off))[2:].zfill(3)
    elif result[0] == "jmp":
        my_string += bin(6)[2:].zfill(3)
        my_string += bin(int(result[1]))[2:].zfill(9)
    elif result[0] == "beq":
        my_string += bin(7)[2:].zfill(3)
        my_string += i_type(result[1])
        my_string += i_type(result[2])
        my_string += i_type(result[3])
    r.write(my_string + "\n")
r.close()
f.close()
#files closed after making the binary file

#opening file for generating hex codes from the binary output file
b = open("output_bin.txt", "r")
h = open("output_hex.txt", "w")
h.write("v2.0 raw\n")#this is a line used for logisim to recognise the hex file
for x in b:
    #here i'm slicing the 12 bit binary output lines into slice of 4 bits so that I can convert it to hexadecimal
    hex_num1 = format(int(x[0:4],2),'x')
    hex_num2 = format(int(x[4:8],2),'x')
    hex_num3 = format(int(x[8:12],2),'x')
    h.write(hex_num1)
    h.write(hex_num2)
    h.write(hex_num3)
    h.write("\n")
b.close()
h.close()
#files closed for generating hex codes