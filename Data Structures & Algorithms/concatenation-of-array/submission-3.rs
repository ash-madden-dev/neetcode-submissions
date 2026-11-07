impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let concatenated_vec: Vec<i32> = nums.iter().cycle().take(nums.len() * 2).copied().collect();
        concatenated_vec
    }
}
