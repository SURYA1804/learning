class Seat:
    def __init__(self,type,price,place,id):
        self.type=type
        self.price=price
        self.place=place
        self.id=id
class Bus:
    def __init__(self,id,name,type,price,place,seat_id):
        self.id=id
        self.name=name
        self.s=Seat(type,price,place,seat_id)
bus=[Bus("K1","komban","semi_sleeper",1500,"window seat","SSW"),
    Bus("K1","komban","semi_sleeper",1500,"corner seat","SSC"),
    Bus("K1","komban","sleeper",2000,"window seat","SW"),
    Bus("K1","komban","sleeper",1500,"corner seat","SC"),
    Bus("S1","SRM","semi_sleeper",1600,"window seat","SSW"),
    Bus("S1","SRM","semi_sleeper",1600,"corner seat","SSC"),
    Bus("S1","SRM","sleeper",2100,"window seat","SW"),
    Bus("S1","SRM","sleeper",2100,"corner seat","SC")]
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
                if booked[i].seat_id==bus[j].s.id and booked[i].bus_id==bus[j].id:
                    return bus[j].s.price-(bus[j].s.price*d[0].discount_rate/100)
        else:
            for j in range(len(bus)):
                if booked[i].seat_id==bus[j].s.id and booked[i].bus_id==bus[j].id:
                    return bus[i].s.price




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
            print(f"BUS:{bus[i].name} ||Bus_ID:{bus[i].id} || SEAT_ID: {bus[i].s.id} || SEAT_TYPE:{bus[i].s.type} || SEAT_PRICE: {bus[i].s.price} || SEAT_PLACE: {bus[i].s.place} ")
        print("-------------------------------------")
    elif UserChoiceIsToBookTheSeats():
        buss=input("Enter the bus_id:")
        seat=input("Enter the Seat id :")
        c=0
        for j in range(len(booked)):
            if seat==booked[j].seat_id and buss==booked[j].bus_id:
                print("*******The Seat is already book**********")
                c=c+1
        if c==0:
            for i in range(len(bus)):
                if seat==bus[i].s.id and buss==bus[i].id:
                    booked.append(Booked(bus[i].id,bus[i].s.id))
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
