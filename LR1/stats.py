def median(list):

   if len(list) == 0:

       return 0

   list.sort()

   midIndex = len(list) / 2

   if len(list) % 2 == 1:

       return list[midIndex]

   else:

       return (list[midIndex] + list[midIndex - 1]) / 2

def mean(list):

   if len(list) == 0:

       return 0

   myRange = list
   myRange.sort()

   total = 0

   for number in myRange:

       total += number

   return total / len(list)

def mode(list):

   numberDictionary = {}

   for digit in list:

       number = numberDictionary.get(digit, None)

       if number == None:

           numberDictionary[digit] = 1

       else:

           numberDictionary[digit] = number + 1

   maxValue = max(numberDictionary.values())

   modeList = []

   for key in numberDictionary:

       if numberDictionary[key] == maxValue:

           modeList.append(key)

   return modeList

def main():


   print ("Mean of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: ", mean(range(1, 11)))

   print ("Mode of [1, 1, 1, 1, 4, 4]:", mode([1, 1, 1, 1, 4, 4]))

   print ("Median of [1, 2, 3, 4]:", median([1, 2, 3, 4]))

if __name__=="__main__":
    main()
