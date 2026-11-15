impl Solution {
    pub fn remove_vowels(s: String) -> String {
        const VOWELS: &str = "aeiou";
        let mut new_s: Vec<String> = vec![];
        for char in s.chars() {
            if !VOWELS.contains(char) {
                new_s.push(String::from(char));
            }
        }
        new_s.join("")
        }
}
