def es_entero(byte):
    return byte.isdigit()

def menor_a_256(byte):
    byte_int = (int(byte))
    return ( byte_int < 256)

def print_ip_bytes(ip_address):
    bytes_ip_address = ip_address.split('.')
    
    #Checkeo por la cantida de bytes
    if len(bytes_ip_address) != 4:
        print("Error, there must be 4 bytes in the ip address")
        return False

    #Checkeo extra de si los bytes son numeros
    all_bytes_areInt = all(map(es_entero, bytes_ip_address))
    if not all_bytes_areInt:
        print("Error, not all bytes in ip address are numbers")
        return False
        
    #Checkeo que todos los bytes son menores a 256
    all_bytes_lessthan256 = all(map(menor_a_256, bytes_ip_address))
    if not all_bytes_lessthan256:
        print("Error, byte cannot by greater than 255")
        return False

    #Print final si todo esta bien en strig de ip_address
    for byte in bytes_ip_address:
        print(byte)
    
