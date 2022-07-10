# 1376. Time Needed to Inform All Employees

# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        res = 0
        
        # create graph which key is manager, and value is subordinates
        graph = collections.defaultdict(list)
        for index, managerId in enumerate(manager):
            graph[managerId].append(index)
        
        # create queue to perform BFS
        # each queue object contains workerId and informTime
        # initialize with the head of company (top of the graph)
        queue = collections.deque([(headID, informTime[headID])])
        
        # BFS
        while queue:
            cur_worker, cur_time = queue.popleft()
            
            res = max(res, cur_time)
            
            for subordinateID in graph[cur_worker]:
                # append to queue if there are subordinates
                # the time of the subordinate needed to inform is the manager time + self time
                queue.append([subordinateID, cur_time + informTime[subordinateID]])
            
        return res

    # Time -> O(N) + O(N) = O(2N) ==> O(N)
    # Space -> O(N) + O(N) = O(2N) ==> O(N)
        
        
        