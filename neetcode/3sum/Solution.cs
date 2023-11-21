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
        // integer array as input
        // [-1, 0, 1, 2, -1, 4]

        // return ALL triplets that:
        // don't equal to each other AND
        // sum up to 0!

        // repeat for each elem:
        // look at one -> i
        // find two that sum up to -i 

        for (int i = 0; i < nums.Length; i++) {
            // Write CounterElems
            var complements = GetComplements(nums[i], nums);

            Console.Write($"[{nums[i]}, {complements.Item1}, {complements.Item2}]");           
            
            


            Console.WriteLine();
        } 




        // array of arrays as output
        IList<IList<int>> nestedList = new List<IList<int>>();
        return nestedList;
    }
}