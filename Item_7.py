from netmiko import ConnectHandler

router = {
    "device_type":"cisco_ios",
    "host":"192.168.52.131",
    "username":"cisco",
    "password":"cisco123!",
}

ssh = ConnectHandler(**router)

show_run = "show running-config"
show_interface = "show ip interface brief"
show_version =  "show version"


acceso = True

while acceso :
    print (""""
        (1) do show running-config 
        (2) do show ip interface brief
        (3) do show version
        (4) Salir del programa
    """)
    opcion = int(input("Ingrese número de opción que desee ejecutar: "))
    if opcion == 1:
        request = ssh.send_command(show_run)
        print (request)
       
    elif opcion == 2:
        request=ssh.send_command(show_interface)
        print (request)
       
    elif opcion == 3:
        request = ssh.send_command(show_version)
        print (request)
      
    else:
        print("Gracias por utilizar la aplicación")
        acceso = False