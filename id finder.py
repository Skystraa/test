from urllib.request import urlopen,Request

player = input("Insert Player username: ")
url = "http://www.boomlings.com/database/getGJUsers20.php"
p = "gameVersion=21&binaryVersion=35&gdw=0&str="+player+"&total=0&page=0&secret=Wmfd2893gb7"
p = p.encode()
data = urlopen(url,p).read().decode()
if data == "-1": 
    print("The request to the server has failed. Please try again later.") 
else:
    data = data.split('|')
    data = data[0].split(':')
    print("Player: "+player)
    print("Account ID: "+data[21])

print ("Want to find out another Account ID? (Please type 1 for yes, 0 for no.)")

check = input()
if check == "1":
    print("I'm still programming this bit, sorry.")
elif check == "0":
    print("You may now close the program.")
else:
    print("please read the instructions ffs")
