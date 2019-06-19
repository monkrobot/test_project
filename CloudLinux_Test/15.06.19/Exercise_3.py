from collections import namedtuple


S = '''00:01:07,400-234-090
00:06:07,601-080-080
00:05:00,400-234-090'''

# call < 5 min => 3 cents for sec (00:01:07 => 3*67=201 cents)
# call > = 5 min => 150 cents for min (00:05:01 => 150*6=900 cents)
# calling to number with max time duration is free
# if there some numbers with max time duration, calling to the smallest phone number is free

def solution(s):
    calls = s.split("\n")
    calls_dict = {}

    for item in calls:
        call = item.split(',')

        call_dur = namedtuple('Call_Dur', 'hh mm ss')
        time = call_dur(*[int(x) for x in call[0].split(':')])
        time_sec = time.hh*3600 + time.mm*60 + time.ss

        if time_sec < 300:
            pay = time_sec*3
        elif time.ss:
            pay = (time.hh*60 + time.mm + 1)*150
        else:
            pay = (time.hh*60 + time.mm)*150

        # if phone number in calls_dict.keys
        if call[1] in calls_dict.keys():
            calls_dict[call[1]]['time'] += time_sec
            calls_dict[call[1]]['pay'] += pay
        else:
            calls_dict[call[1]] = {'time': time_sec, 'pay': pay}

    # Find max durations of calls to one number. First count sum of all payments, then subtract max_time_pay
    max_time = {'max_time': 0, 'max_time_pay': 0, 'max_time_numb': '999-999-999'}
    month_pay = 0
    for i in calls_dict.keys():
        if calls_dict[i]['time'] > max_time['max_time']:
            max_time['max_time_numb'] = i
            max_time['max_time'] = calls_dict[i]['time']
            max_time['max_time_pay'] = calls_dict[i]['pay']
            month_pay += calls_dict[i]['pay']

        # if there are some equal time durations, then subtract max_time_pay of smallest number
        elif calls_dict[i]['time'] == max_time['max_time']:
            if i < max_time['max_time_numb']:
                max_time['max_time_numb'] = i
                max_time['max_time'] = calls_dict[i]['time']
                max_time['max_time_pay'] = calls_dict[i]['pay']
                month_pay += calls_dict[i]['pay']
            else:
                month_pay += calls_dict[i]['pay']
        else:
            month_pay += calls_dict[i]['pay']

    print(max_time)
    month_pay -= max_time['max_time_pay']

    print(calls_dict)
    return month_pay


if __name__ == "__main__":
    print(solution(S))
