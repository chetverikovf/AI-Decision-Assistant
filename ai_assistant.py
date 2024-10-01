from logic import *

rain = Symbol("rain")
heavyTraffic = Symbol("heavyTraffic")
construction = Symbol("construction")
earlyMeeting = Symbol("earlyMeeting")
strike = Symbol("strike")
doctorAppointment = Symbol("doctorAppointment")

wfh = And(
    Not(doctorAppointment),
    Or(
        rain,
        earlyMeeting,
        And(Or(heavyTraffic, construction), strike)
    )
)

publicTransport = And(
    Not(strike),
    Not(wfh)
)

drive = And(
    Not(wfh),
    Not(publicTransport)
)

road_1 = Not(Or(construction, heavyTraffic))
road_2 = And(Not(construction), heavyTraffic)
road_3 = And(construction, Not(heavyTraffic))
road_4 = And(construction, heavyTraffic)

def ai_assistant(scenario):
    wfh_v = model_check(scenario, wfh)
    publicTransport_v = model_check(scenario, publicTransport)
    drive_v = model_check(scenario, drive)

    if wfh_v:
        print("Work from home")
        return
    
    if publicTransport_v:
        print("take public transport")
        return
    
    if drive_v:
        print("drive")
        road_1_v = model_check(scenario, road_1)
        road_2_v = model_check(scenario, road_2)
        road_3_v = model_check(scenario, road_3)
        road_4_v = model_check(scenario, road_4)
        if road_1_v:
            print("take road 1")
        if road_2_v:
            print("take road 2")
        if road_3_v:
            print("take road 3")
        if road_4_v:
            print("take road 4")
        return
    
    print("no specific recomendation")
        

    
# scenario 1 
scenario1  = And(
    rain,
    heavyTraffic,
    Not(construction),
    Not(earlyMeeting),
    Not(strike),
    Not(doctorAppointment)
)
print("scenario 1: ")
ai_assistant(scenario1)

# scenario 2 
scenario2 = And(
    Not(rain),
    Not(heavyTraffic),
    Not(construction),
    Not(earlyMeeting),
    strike,
    Not(doctorAppointment)
)
print("scenario 2: ")
ai_assistant(scenario2)

# scenario 3 
scenario3 = And(
    Not(rain),
    Not(heavyTraffic),
    Not(construction),
    Not(earlyMeeting),
    Not(strike),
    Not(doctorAppointment)
)
print("scenario 3: ")
ai_assistant(scenario3)