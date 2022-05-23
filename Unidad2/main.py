import ip_functions as ipf

if __name__ == '__main__':

    print("[192.168.0.0.1] Falla por cantidad de bytes ❌")
    ipf.print_ip_bytes("192.168.0.0.1")
    print("[192.168.300.1] Falla por que un byte es mayor a 255 ❌")
    ipf.print_ip_bytes("192.168.300.1")
    print("[Extra] [aaa.168.300.1] Falla por que sus uno de sus bytes no es un numero ❌")    
    ipf.print_ip_bytes("aaa.168.300.1")
    print("[192.168.0.1] Direccion IP Valida ✅")
    ipf.print_ip_bytes("192.168.0.1")

    

    


