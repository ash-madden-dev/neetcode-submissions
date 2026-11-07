impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut record: Vec<i32> = vec![];
        let mut sum = 0;
        for op in operations {
            if op == String::from("+") {
                let total = record[record.len() - 1] + record[record.len() - 2];
                record.push(total);
                sum += total;
            } else if op == String::from("D") {
                let double = record[record.len() - 1] * 2;
                record.push(double);
                sum += double;
            } else if op == String::from("C") {
                match record.pop() {
                    Some(value) => sum -= value,
                    _ => sum += 0,
                }
            } else {
                match op.parse::<i32>() {
                    Ok(value) => {
                        record.push(value);
                        sum += value;
                    }
                    _ => sum += 0,
                }
            }
        }
        sum
    }
}
