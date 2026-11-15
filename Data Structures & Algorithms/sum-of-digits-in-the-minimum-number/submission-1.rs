impl Solution {
    pub fn sum_of_digits(nums: Vec<i32>) -> i32 {
        let smallest_num = nums.iter().min();
        match smallest_num {
            Some(num) => {
                let mut sum = 0;
                for digit in num.to_string().split("") {
                    sum += digit.parse::<i32>().unwrap_or(0);
                }
                if sum % 2 == 0 { 1 } else { 0 }
            }
            None => return 0,
        }
    }
}
