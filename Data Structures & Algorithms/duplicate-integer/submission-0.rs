impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut unique_nums: HashSet<i32> = HashSet::new();
        for num in nums {
            if !unique_nums.contains(&num) {
                unique_nums.insert(num);
            } else {
                return true;
            }
        }
        false
    }
}
