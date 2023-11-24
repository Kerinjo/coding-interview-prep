//https://leetcode.com/problems/3sum/

static void printNestedList(IList<IList<int>> list) {
    foreach (List<int> nested_list in list) {
        foreach (int elem in nested_list) {
            System.Console.Write($"{elem}  ");
        }
        System.Console.WriteLine();
    }
}

// Problem solution
Solution solution = new Solution();

int[] arr = {-1,0,1,2,-1,-4};
IList<IList<int>> result = solution.ThreeSum(arr);

System.Console.WriteLine("LIST:");
printNestedList(result);


