##
##File a.in :
## HH:MM:SS 00<=HH<=23 
## H:M:S , 00<=H,M,S<= 10^9
## 01:01:01
## 48:0:0
##File a.out :
## 01:01:01+2 days

##unix timestamp way - convert time to a timestamp,
##so we can easily add times to each other

def normalise_time(days, hours, minutes, seconds):
    
    # % - modulo остаток от деления
    # // - floor division целая часть от деления
    #seconds
    floor_division = seconds // 60
    seconds = seconds % 60
    minutes = minutes + floor_division
    #minutes
    floor_division = minutes // 60
    minutes = minutes % 60
    hours = hours + floor_division
    #hours
    floor_division = hours // 60
    hours = hours % 60
    days = days + floor_division
    normalised_time=(days,hours,minutes,seconds)
    #seconds = seconds % 60
    #minutes = minutes + (seconds // 60)
    #hours = hours + (minutes // 60)
    #minutes = minutes % 60
    # 00:11:12
    return normalised_time

def normalised_time_tuple(days,hours,minutes,seconds):
    #idea is to iterate over the tuple without
    #tuple variables name just by the numbers
    #maybe it will take less memory
    return normalised_time


def read_in(timetext):
    
    with open(timetext, "r") as input_file:
        input_file.read()
        #input_time=(days,hours,minutes,seconds)
        #counter_time=(days,hours,minutes,seconds)
        #   
        #
        input_time="some string"
        counter_time="some other string"
    output_time="00:00:00"
    #debug
    print(input_time)
    print(counter_time)
    #some computing
    # 
    # 
    return input_time, counter_time       

def write_out(timetext, file):
    with open(d, "w") as input_file:
        input_file.write() 



read_in("C:\\Users\\Nittiyam\\Documents\\code\\olympiad-tasks\\python\\task I-A - timer\\a.in")
output_time=read_in("./a.in")
write_out("./a.out")



