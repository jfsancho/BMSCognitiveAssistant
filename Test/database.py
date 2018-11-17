import sys
sys.path.append('../')

from API.api_app.database.DBController import DBController



db = DBController()

#Create new deviceType

#nDeviceType = db.createDeviceType("Illumination","KNX")

#nDevice = db.createDevice("1.1.1","LED-Lighting","Zennio Lumento C4","Salon principal", nDeviceType)

#nDevice = db.createDevice("1.1.2","LED-Lighting","Zennio Lumento x3","Salon principal", nDeviceType)

#nPermission = db.createPermission("Administrator")
#nPermission = db.createPermission("Client")
#nPermission = db.getPermission(1)

#nUserType= db.createUserType("developer",nPermission)

#nUser= db.createUser("jfsancho","Javier","Sancho","Sancho16",nUserType )

#devices= db.getDevice("Illumination","salon principal")

#print(devices)
#for device in devices:
 #   print(device.DeviceID)