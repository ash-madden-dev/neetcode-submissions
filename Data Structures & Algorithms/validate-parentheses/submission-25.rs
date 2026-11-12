impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = vec![];
        for b in s.chars() {
            match b {
                '{' => stack.push('}'),
                '[' => stack.push(']'),
                '(' => stack.push(')'),
                _ => match stack.pop() {
                    Some(expected) if b == expected => (),
                    _ => return false,
                },
            }
        }
        stack.is_empty()
    }
}
