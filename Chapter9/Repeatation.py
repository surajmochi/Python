#Writing Files (Config Generation)
#Write mode (w)
with open("router.conf", "w") as f:
    f.write("hostname R1\n")
    f.write("interface eth0\n")
    f.write("ip add 192.168.1.1 255.255.255.0\n")
    f.write("no shutdown\n")



# Append mode(a) - Logging
with open("scan.log", "a") as f:
    f.write("port 22 open\n")









