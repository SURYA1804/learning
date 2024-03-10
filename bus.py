#inlcude the command line and pushed through git
#Seat is a class which consist of seat description.
#gghhg
class Seat:
    def __init__(self,type,price,place,id):
        self.type=type
        self.price=price
        self.place=place
        self.id=id
class Bus:
    def __init__(self,name,type,price,place,id):
        self.name=name
        self.s=Seat(type,price,place,id)
bus=[Bus("komban","semi_sleeper",1500,"window seat","KSSW"),Bus("komban","semi_sleeper",1500,"corner seat","KSSC"),Bus("komban","sleeper",2000,"window seat","KSW"),Bus("komban","sleeper",1500,"corner seat","KSC"),Bus("SRM","semi_sleeper",1600,"window seat","SSSW"),Bus("SRM","semi_sleeper",1600,"corner seat","SSSC"),Bus("SRM","sleeper",2100,"window seat","SSW"),Bus("SRM","sleeper",2100,"corner seat","SSC")]
class Booked:
    def __init__(self,bus_name,seat_type,seat_price,seat_place,id):
        self.bus_name=bus_name
        self.seat_type=seat_type
        self.seat_price=seat_price
        self.seat_place=seat_place
        self.id=id
booked=[]
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
            print(f"BUS:{bus[i].name} || SEAT_ID: {bus[i].s.id} || SEAT_TYPE:{bus[i].s.type} || SEAT_PRICE: {bus[i].s.price} || SEAT_PLACE: {bus[i].s.place} ")
        print("-------------------------------------")
    elif UserChoiceIsToBookTheSeats():
        seat=input("Enter the Seat id :")
        c=0
        for j in range(len(booked)):
            if seat==booked[j].id:
                print("*******The Seat is already book**********")
                c=c+1
        if c==0:
            for i in range(len(bus)):
                if seat==bus[i].s.id:
                    booked.append(Booked(bus[i].name,bus[i].s.type,bus[i].s.price,bus[i].s.place,bus[i].s.id))
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
                print(f"seat_id:{booked[i].id}")
            print("*****************************")
    elif UserChoiceIsToQuit():
        break
    else:
        print("Enter the valid option.")
    print("***************THANK YOU VISIT AGAIN***********")
