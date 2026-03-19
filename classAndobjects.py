

class Statistics:
    def __init__(self, ages):
        self.ages = ages
    
    def sum(self):
        totalSum = 0
        for line in self.ages:
            totalSum += line
        return f"Total sum: {totalSum}"
    
    def minNum(self):
        miniNum = self.ages[0]
        for Num in self.ages:
            if Num < miniNum:
                miniNum = Num
        return f"Minimum Value: {miniNum}"
    
    def maxNum(self):
        maxNum = self.ages[0]
        for MyNum in self.ages:
            if MyNum > maxNum:
                maxNum = MyNum
        return f"Maximum Value: {maxNum}"
    
    def range(self):
        MyRange = self.maxNum - self.minNum
        return f"Range: {MyRange}"
    
    def Mycount(self):
        countVal = 0
        for line in self.ages:
            countVal += 1
        return f"Count: {countVal}"
    
    def Mymean(self):
        MeanVal = self.sum / self.Mycount
        return f"Mean: {MeanVal}"
    
    def median(self):
        sorted_ages = sorted(self.ages)
        n = len(sorted_ages)
        middle = n // 2
        if n % 2 == 0:
            med = (sorted_ages[middle - 1] + sorted_ages[middle] ) / 2
        else:
            med = sorted_ages[middle]

        return f"Median {med}"
    
    def mode(self):
     frequency = {}
     for age in self.ages:
        if age in frequency:
            frequency[age] += 1
        else:
            frequency[age] = 1

    max_freq = 0
    for count in frequency.values():
        if count > max_freq:
            max_freq = count

    modes = []
    for age, count in frequency.items():
        if count == max_freq:
            modes.append(age)

    print(f"Mode: {modes}")
    

def variance(self):
    mean = self.sum() / self.count()
    total = 0
    for age in self.ages:
        total += (age - mean) ** 2
    var = total / self.count()
    print(f"Variance: {var:.2f}")
    return var

def sd(self):
    std = self.variance() ** 0.5
    print(f"Standard Deviation: {std:.2f}")
    return std

def frequency_distribution(self):
    frequency = {}
    for age in self.ages:
        if age in frequency:
            frequency[age] += 1
        else:
            frequency[age] = 1

    sorted_freq = sorted(frequency.items())   # sort by age
    print(f"\nFrequency Distribution:")
    print(f"{'Age':<10}{'Frequency':<10}")
    print("-" * 20)
    for age, count in sorted_freq:
        print(f"{age:<10}{count:<10}")
    return sorted_freq

    

    




        
        

        

