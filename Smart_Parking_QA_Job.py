# Testing for Full Parking Lot
print("\nTEST 1: Full Parking Lot")
vehicleType='Car'
carSlots=0

if vehicleType=='Car' and carSlots>0:
    slotAllocated=True
else:
    slotAllocated=False

if slotAllocated==False:
    print("PASS - Full parking lot detected")
else:
    print("FAIL")


# Testing for Wrong Vehicle-Slot Combination
print("\nTEST 2: Wrong Vehicle-Slot Combination")
vehicleType='Truck'
slotType='Bike'

if vehicleType=='Bike' and slotType=='Bike':
    validSlot=True
elif vehicleType=='Car' and slotType=='Car':
    validSlot=True
elif vehicleType=='SUV' and slotType=='SUV':
    validSlot=True
elif vehicleType=='Truck' and slotType=='Truck':
    validSlot=True
elif vehicleType=='Electric Vehicle' and slotType=='EV':
    validSlot=True
else:
    validSlot=False

if validSlot==False:
    print("PASS - Wrong vehicle-slot combination detected")
else:
    print("FAIL")


# Testing for Duplicate Vehicle
print("\nTEST 3: Duplicate Vehicle")
vehicleNo='TN01AB1234'
parkedVehicle='TN01AB1234'

if vehicleNo==parkedVehicle:
    duplicate=True
else:
    duplicate=False

if duplicate:
    print("PASS - Duplicate vehicle detected")
else:
    print("FAIL")


# Testing for Lost Ticket
print("\nTEST 4: Lost Ticket")
lostTicket=True

if lostTicket:
    parkingFee=1000
else:
    parkingFee=500

print("Parking Fee:", parkingFee)

if parkingFee==1000:
    print("PASS - Lost ticket charge applied")
else:
    print("FAIL")


# Testing for Early Exit
print("\nTEST 5: Early Exit")
entryTime=10
exitTime=11

parkingHours=exitTime-entryTime
hourlyRate=50
parkingFee=parkingHours*hourlyRate

print("Parking Hours:", parkingHours)
print("Parking Fee:", parkingFee)

if parkingHours==1 and parkingFee==50:
    print("PASS - Early exit calculated")
else:
    print("FAIL")


# Testing for Overnight Parking
print("\nTEST 6: Overnight Parking")
entryTime=22
exitTime=2

if exitTime<entryTime:
    parkingHours=(24-entryTime)+exitTime
else:
    parkingHours=exitTime-entryTime

hourlyRate=50
parkingFee=parkingHours*hourlyRate

print("Parking Hours:", parkingHours)
print("Parking Fee:", parkingFee)

if parkingHours==4:
    print("PASS - Overnight parking calculated")
else:
    print("FAIL")


# Testing for Peak-Hour Pricing
print("\nTEST 7: Peak-Hour Pricing")
entryTime=9
parkingHours=2
hourlyRate=50

parkingFee=parkingHours*hourlyRate

if entryTime>=8 and entryTime<=11:
    parkingFee=parkingFee*1.50

print("Peak-Hour Parking Fee:", parkingFee)

if parkingFee==150:
    print("PASS - Peak-hour pricing applied")
else:
    print("FAIL")


# Testing for EV Charging Fee
print("\nTEST 8: EV Charging Fee")
vehicleType='Electric Vehicle'
evCharging=True
chargingFee=0

if vehicleType=='Electric Vehicle' and evCharging:
    chargingFee=200

print("EV Charging Fee:", chargingFee)

if chargingFee==200:
    print("PASS - EV charging fee applied")
else:
    print("FAIL")


# Testing for Bike Slot Allocation
print("\nTEST 9: Bike Slot Allocation")
vehicleType='Bike'
bikeSlots=3

if vehicleType=='Bike' and bikeSlots>0:
    slotType='Bike'
    bikeSlots=bikeSlots-1
else:
    slotType='No Slot'

print("Allocated Slot:", slotType)

if slotType=='Bike':
    print("PASS - Bike slot allocated")
else:
    print("FAIL")


# Testing for Car Slot Allocation
print("\nTEST 10: Car Slot Allocation")
vehicleType='Car'
carSlots=3

if vehicleType=='Car' and carSlots>0:
    slotType='Car'
    carSlots=carSlots-1
else:
    slotType='No Slot'

print("Allocated Slot:", slotType)

if slotType=='Car':
    print("PASS - Car slot allocated")
else:
    print("FAIL")


# Testing for SUV Slot Allocation
print("\nTEST 11: SUV Slot Allocation")
vehicleType='SUV'
suvSlots=2

if vehicleType=='SUV' and suvSlots>0:
    slotType='SUV'
    suvSlots=suvSlots-1
else:
    slotType='No Slot'

print("Allocated Slot:", slotType)

if slotType=='SUV':
    print("PASS - SUV slot allocated")
else:
    print("FAIL")


# Testing for Truck Slot Allocation
print("\nTEST 12: Truck Slot Allocation")
vehicleType='Truck'
truckSlots=2

if vehicleType=='Truck' and truckSlots>0:
    slotType='Truck'
    truckSlots=truckSlots-1
else:
    slotType='No Slot'

print("Allocated Slot:", slotType)

if slotType=='Truck':
    print("PASS - Truck slot allocated")
else:
    print("FAIL")


# Testing for EV Slot Allocation
print("\nTEST 13: EV Slot Allocation")
vehicleType='Electric Vehicle'
evSlots=2

if vehicleType=='Electric Vehicle' and evSlots>0:
    slotType='EV'
    evSlots=evSlots-1
else:
    slotType='No Slot'

print("Allocated Slot:", slotType)

if slotType=='EV':
    print("PASS - EV slot allocated")
else:
    print("FAIL")


# Testing for VIP Parking
print("\nTEST 14: VIP Parking")
vip=True
parkingFee=1000

if vip:
    parkingFee=parkingFee*0.50

print("VIP Parking Fee:", parkingFee)

if parkingFee==500:
    print("PASS - VIP discount applied")
else:
    print("FAIL")

