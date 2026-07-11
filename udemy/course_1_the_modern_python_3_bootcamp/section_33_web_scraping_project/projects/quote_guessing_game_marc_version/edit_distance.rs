use std::cmp::min;

//  https://www.geeksforgeeks.org/edit-distance-dp-5/
pub fn edit_distance(str1: &str, str2: &str, m: usize, n: usize) -> usize {
    // If first string is empty, the only option is to
    // insert all characters of second string into first
    if m == 0 {
        return n;
    }

    // If second string is empty, the only option is to
    // remove all characters of first string
    if n == 0 {
        return m;
    }

    // If last characters of two strings are same, nothing
    // much to do. Get the count for
    // remaining strings.

    if str1.as_bytes()[m - 1] == str2.as_bytes()[n - 1] {
        return edit_distance(str1, str2, m - 1, n - 1);
    }

    return 1 + m_min(
        edit_distance(str1, str2, m, n - 1),     // Insert
        edit_distance(str1, str2, m - 1, n),     // Remove
        edit_distance(str1, str2, m - 1, n - 1), // Replace
    );
}

fn m_min(x: usize, y: usize, z: usize) -> usize {
    return min(min(x, y), z);
}

#[test]
fn test_edit_distance() {
    let str1 = "GEEXSFRGEEKKS";
    let str2 = "GEEKSFORGEEKS";
    let m = str1.len();
    let n = str2.len();
    assert_eq!(3, edit_distance(str1, str2, m, n))
}
