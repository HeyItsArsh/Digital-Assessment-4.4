vehicleNo='TN01AB1234'
vehicleType='Car'
entryTime=10
exitTime=14
vip=False
lostTicket=False
evCharging=False
bikeSlots=5
carSlots=5
suvSlots=3
truckSlots=2
evSlots=2

# Calculating the Slot Allocation
if vehicleType=='Bike' and bikeSlots>0:
    slotType='Bike'
    bikeSlots=bikeSlots-1
elif vehicleType=='Car' and carSlots>0:
    slotType='Car'
    carSlots=carSlots-1
elif vehicleType=='SUV' and suvSlots>0:
    slotType='SUV'
    suvSlots=suvSlots-1
elif vehicleType=='Truck' and truckSlots>0:
    slotType='Truck'
    truckSlots=truckSlots-1
elif vehicleType=='Electric Vehicle' and evSlots>0:
    slotType='EV'
    evSlots=evSlots-1
else:
    slotType='No Slot'

# Calculating the Parking Fee
parkingHours=exitTime-entryTime
if vehicleType=='Bike':
    hourlyRate=20
elif vehicleType=='Car':
    hourlyRate=50
elif vehicleType=='SUV':
    hourlyRate=70
elif vehicleType=='Truck':
    hourlyRate=100
else:
    hourlyRate=50
parkingFee=parkingHours*hourlyRate

# Calculating the VIP Parking
if vip:
    parkingFee=parkingFee*0.50

# Calculating the Peak Hour Pricing
if entryTime>=8 and entryTime<=11:
    parkingFee=parkingFee*1.50

# Calculating the Overnight Parking
if exitTime<entryTime:
    parkingHours=(24-entryTime)+exitTime
    parkingFee=parkingHours*hourlyRate

# Calculating the Lost Ticket
if lostTicket:
    parkingFee=1000

# Calculating the EV Charging
if vehicleType=='Electric Vehicle' and evCharging:
    chargingFee=200
else:
    chargingFee=0
totalFee=parkingFee+chargingFee

print("Vehicle Number:", vehicleNo)
print("Vehicle Type:", vehicleType)
print("Entry Time:", entryTime)
print("Exit Time:", exitTime)
print("Allocated Slot:", slotType)
print("Parking Hours:", parkingHours)
print("Parking Fee:", parkingFee)
print("EV Charging Fee:", chargingFee)
print("Total Fee:", totalFee)

if slotType!='No Slot':
    print("Vehicle Entry: Allowed")
else:
    print("Vehicle Entry: Rejected")

