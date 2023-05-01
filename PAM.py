class PAM():
    issue_comment_raw:int
    open_issue_raw:int
    open_pr_raw:int
    review_comment_raw:int
    pr_merged_raw:int
    watch_raw:int
    fork_raw:int

    issue_comment:dict
    open_issue:dict
    open_pr:dict
    review_comment:dict
    pr_merged:dict
    watch:dict
    fork:dict

    time_period:list = list()

    def __init__(self, issue_comment, open_issue, open_pr, review_comment, pr_merged, watch, fork) -> None:
        self.issue_comment = issue_comment
        self.open_issue = open_issue
        self.open_pr = open_pr
        self.review_comment = review_comment
        self.pr_merged = pr_merged
        self.watch = watch
        self.fork = fork
        return
    
    def getPAM(self, timePeriod:list) -> dict:
        self.setTimeSlice(timePeriod)
        weights = [1,2,3,4,2,1,2]
        ret:dict = dict()
        for time in self.time_period:
            data = list()
            data = [
                self.issue_comment[time],
                self.open_issue[time],
                self.open_pr[time],
                self.review_comment[time],
                self.pr_merged[time],
                self.watch[time],
                self.fork[time]
            ]
            pam = 0
            cnt = 0
            while cnt < 7:
                pam += data[cnt]*weights[cnt]
                cnt += 1

            ret[time] = pam
        
        return ret

    def setTimeSlice(self, timePeriod:list) -> None:
        # check if timePeriod is valid
        try:
            if len(timePeriod) != 2:
                raise ValueError("Invalid time period input")
        except ValueError:
            exit()
                        
        # Time Period format YYYY-MM
        start = timePeriod[0]
        end = timePeriod[1]
        time = timeByMonth(0,0)
        time.timeInit_strTime(start)
        time_t = timeByMonth(0,1)
        self.time_period.append(str(time))
        while str(time) != end:
            time += time_t
            self.time_period.append(str(time))
        
        print(self.time_period)

# time calss, has YYYY-MM records
class timeByMonth():
    year:int
    month:int

    def __init__(self, year, month) -> None:
        self.year = year
        self.month = month

    def __str__(self) -> str:
        # format convert to YYYY-MM
        ret:str = "%04d" % self.year
        ret += '-'
        ret += "%02d" % self.month

        return ret

    def __add__(self, other):
        ret = timeByMonth(0,0)
        ret.year = self.year + other.year
        ret.month = self.month + other.month
        while ret.month > 12:
            ret.month -= 12
            ret.year += 1
        return ret

    def timeInit_strTime(self, strTime:str) -> None:
        self.year = int(strTime[0:4])
        self.month = int(strTime[6:])
        return