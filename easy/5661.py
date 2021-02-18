class Solution:
    def maximumTime(self, time: str) -> str:
        latest_time = [':' if t == '?' or t == '?' else t for t in time]
        latest_time[3] = ('5' if time[3] == '?' else time[3])
        latest_time[4] = ('9' if time[4] == '?' else time[4])
        if time[0] == '0' or time[0] == '1':
            if time[1] == '?':
                latest_time[1] = '9'
        elif time[0] == '2':
            if time[1] == '?':
                latest_time[1] = '3'
        else:
            if time[0] == '?':
                if time[1] == '?':
                    latest_time[0] = '2'
                    latest_time[1] = '3'
                elif int(time[1]) >= 4:
                    latest_time[0] = '1'
                else:
                    latest_time[0] = '2'
        return ''.join(latest_time)


if __name__ == '__main__':
    s = Solution()
    time0 = '1?:??'
    time1 = "0?:3?"
    time2 = "2?:?0"
    time3 = "1?:22"
    time4 = "??:??"
    time5 = "?0:15"
    time6 = "?4:03"
    for i in range(7):
        time = eval('time%s' % i)
        print(s.maximumTime(time))
