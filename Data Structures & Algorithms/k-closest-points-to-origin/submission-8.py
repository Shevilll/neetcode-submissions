class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def sort_temp(temp, s, e):
            if e - s + 1 <= 1:
                return temp

            pivot = temp[e]
            j = s
            for i in range(s, e):
                if temp[i] < pivot:
                    temp[i], temp[j] = temp[j], temp[i]
                    j += 1
            temp[j], temp[e] = temp[e], temp[j]
            sort_temp(temp, s, j-1)
            sort_temp(temp, j+1, e)        
       
        res = []
        temp = []

        for i, j in points:
            dist = ((i**2) + (j**2))**0.5
            temp.append((i, j, dist))
        
        print(temp)
        sort_temp(temp, 0, len(temp) - 1)
        print(temp)

        for i in range(k):
            if i < len(temp):
                res.append([temp[i][0], temp[i][1]])

        return res

        