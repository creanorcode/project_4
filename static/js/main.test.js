// Part 1: Import the getCookie function from main.js
const { getCookie } = require('./main.js');

// Part 2: Test getCookie when the cookie is absent.
// This test verifies that getCookie returns null if the specified cookie does not exist.
test('getCookie returns null when cookie is absent', () => {
    // Clear cookies for testing
    document.cookie = '';
    // Expect getCookie to return null for the 'csrftoken' cookie when not set.
    expect(getCookie('csrftoken')).toBeNull();
});