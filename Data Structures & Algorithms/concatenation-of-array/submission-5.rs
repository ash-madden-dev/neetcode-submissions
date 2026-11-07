impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let nums_len = nums.len();
        let mut new_vec = vec![0; nums_len * 2];
        for i in 0..nums_len {
            new_vec[i] = nums[i];
            new_vec[i + nums_len] = nums[i];
        }
        new_vec
    }
}
