class Seat:
    def __init__(self,stype,price,place,id):
        self.stype=stype
        self.price=price
        self.place=place
        self.id=id
seat=[ Seat("semi_sleeper",1500,"corner seat","SSC"),
       Seat("semi_sleeper",2000,"window seat","SSW"),
       Seat("sleeper",1200,"corner seat","SC"),
       Seat("sleeper",1250,"window seat","SW"),
       Seat("seater",1000,"corner seat","SEC"),
       Seat("seater",1050,"window seat","SEW")]
class Bus:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.s=[]
    def setter(self,stype,price,place,seat_id):
        self.s.append(Seat(stype,price,place,seat_id))
bus=[Bus("K1","Komban"),Bus("S1","SRM")]
for i in range(len(bus)):
    for j in range(len(seat)):
        bus[i].setter(seat[j].stype,seat[j].price,seat[j].place,seat[j].id)
class Booked:
    def __init__(self,bus_id,seat_id):
        self.bus_id=bus_id
        self.seat_id=seat_id
booked=[]
class discount:
    def __init__(self,bus_id,seat_id,discount_rate):
        self.seat_id=seat_id
        self.bus_id=bus_id
        self.discount_rate=discount_rate
d=[discount("K1","SSW",5)]
def calculation():
    for i in range(len(booked)):
        if booked[i].seat_id==d[0].seat_id and booked[i].bus_id==d[0].bus_id:
            for j in range(len(bus)):
                if booked[i].bus_id==bus[j].id:
                    for k in range(len(bus[j].s)):
                        if booked[i].seat_id==bus[j].s[k].id:
                            return bus[j].s[k].price-(bus[j].s[k].price*d[0].discount_rate/100)
        else:
            for j in range(len(bus)):
                if booked[i].bus_id==bus[j].id:
                    for k in range(len(bus[j].s)):
                        if booked[i].seat_id==bus[j].s[k].id:
                            return bus[i].s[k].price

def UserChoiceIsToViewTheSeats():
    return ch==1
def UserChoiceIsToBookTheSeats():
    return ch==2
def UserChoiceIsToViewBookedSeats():
    return ch==3
def UserChoiceIsToQuit():
    return ch==4
while True:
    print("*********WELCOME TO RED BUS**********")
    print("1.To view the seats\n2.To Book the seat\n3.To view the Booked Seats\n4.Exit")
    ch=int(input("Enter your choice:"))
    if UserChoiceIsToViewTheSeats():
        print("******DISPLAYING THE SEATS********")
        for i in range(len(bus)):
            for j in range(len(bus[i].s)):
                print(f"BUS:{bus[i].name} ||Bus_ID:{bus[i].id} || SEAT_ID: {bus[i].s[j].id} || SEAT_TYPE:{bus[i].s[j].stype} || SEAT_PRICE: {bus[i].s[j].price} || SEAT_PLACE: {bus[i].s[j].place} ")
        print("-------------------------------------")
    elif UserChoiceIsToBookTheSeats():
        buss=input("Enter the bus_id:")
        seat=input("Enter the Seat id :")
        c=0
        for i in range(len(booked)):
            if buss==booked[i].bus_id and seat==booked[i].seat_id:
                print("*******The Seat is already book**********")
                c=c+1
        if c==0:
            for i in range(len(bus)):
                if  buss==bus[i].id:
                    for j in range(len(bus[i].s)):
                        if seat==bus[i].s[j].id:
                            booked.append(Booked(bus[i].id,bus[i].s[j].id))
                            print("After Discount You have to PAY:",calculation())
                            print("*******BOOKING CONFORMIED***********")
                else:
                    if i==len(bus):
                        print("**********Invalid Seat ID*********")
    elif UserChoiceIsToViewBookedSeats():
        print("**********BOOKRD SEATS************")
        if len(booked)==0:
            print(" STILL  NO SEATS IS BOOKED ")
        else:
            for i in range(len(booked)):
                print(f"bus_id:{booked[i].bus_id} || SEAT_ID:{booked[i].seat_id}")
            print("*****************************")
    elif UserChoiceIsToQuit():
        break
    else:
        print("Enter the valid option.")
print("***************THANK YOU VISIT AGAIN***********")
