#1a

val1 = "Python 2023"
val2 = "Python 2023"
val3 = "Python 2023"

#a
print(val1 == val2)
print(val2 == val3)

#b
print(id(val1), type(val1), int.from_bytes(val1.encode('utf-8'), byteorder='big'))
print(id(val2), type(val2), int.from_bytes(val2.encode('utf-8'), byteorder='big'))
print(id(val3), type(val3), int.from_bytes(val3.encode('utf-8'), byteorder='big'))

#1b

val3 = "Java 11"

#a
print(val1 == val2)
print(val2 == val3)

#b
print(id(val1), type(val1), int.from_bytes(val1.encode('utf-8'), byteorder='big'))
print(id(val2), type(val2), int.from_bytes(val2.encode('utf-8'), byteorder='big'))
print(id(val3), type(val3), int.from_bytes(val3.encode('utf-8'), byteorder='big'))
