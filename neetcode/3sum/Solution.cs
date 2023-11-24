
public class Solution {
    public (int, int) GetComplements(int value, int[] nums) {
        // in: value
        // out: indices of countervalues
        HashSet<int> seenNumbers = new HashSet<int>();
        int target = -value;
        foreach (int num in nums)
        {
            int complement = target - num;
            if (num == value | complement == value)
                continue;

            if (seenNumbers.Contains(complement))
            {
                return (num, complement);
            }
            seenNumbers.Add(num);
        }
        return (0,0);
    } 
    
    public IList<IList<int>> ThreeSum(int[] nums) {
        IList<IList<int>> nestedList = new List<IList<int>>();

        for (int i = 0; i < nums.Length; i++) {
            HashSet<int> seenNumbers = new HashSet<int>();
            int target = -nums[i];
            for (int j = 0; j < nums.Length; j++)
            {
                if (j != i) {
                    int complement = target - nums[j];
                    if (seenNumbers.Contains(complement)) {
                        System.Console.WriteLine(
                            $"FOUND: {nums[i]}, {nums[j]}, {complement}"
                        );
                        List<int> result = new List<int>(){nums[i], nums[j], complement};

                        System.Console.WriteLine(nestedList.Count);
                        if (nestedList.Count == 0)
                            nestedList.Add(result);

                        foreach (List<int> item in nestedList)
                        {
                            if(item.ToHashSet().SetEquals(result.ToHashSet()))
                            {
                                System.Console.WriteLine("Added to list");
                                nestedList.Add(result);
                                break;
                            }
                        }
                    }
                    seenNumbers.Add(nums[j]);
                }
            }
        }
        // //     // Write CounterElems


                        
        // IList<int> results = new List<int>(){nums[i], complements.Item1, complements.Item2};
            
        //     bool addFlag = true;
        //     foreach (List<int> item in nestedList)
        //     {
        //         if (item.ToHashSet().SetEquals(results.ToHashSet()))
        //             addFlag = false;
        //     }
        //     if (addFlag)
        //         nestedList.Add(results);
        // } 
        return nestedList;
    }
}
