impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut brackets_to_check: Vec<char> = vec![];
        for bracket in s.chars() {
            match bracket {
                '{' => brackets_to_check.push('}'),
                '[' => brackets_to_check.push(']'),
                '(' => brackets_to_check.push(')'),
                _ => match brackets_to_check.pop() {
                    Some(valid_closing_bracket) if bracket == valid_closing_bracket => (),
                    _ => return false,
                },
            }
        }
        brackets_to_check.is_empty()
    }
}
