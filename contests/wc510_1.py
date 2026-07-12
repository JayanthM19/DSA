class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        """
        :type startTime: str
        :type endTime: str
        :rtype: int
        """
        
        sh=int(startTime[:2])
        sm=int(startTime[3:5])
        ss=int(startTime[6:8])

        eh=int(endTime[:2])
        em=int(endTime[3:5])
        es=int(endTime[6:8])

        start = sh*3600+sm*60+ss
        end = eh*3600+em*60+es

        if end<start:
            end+=24*3600

        return end-start

        
        
        