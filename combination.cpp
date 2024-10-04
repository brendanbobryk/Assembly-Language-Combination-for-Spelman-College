#include <cstdint>
#include <iostream>
using namespace std;

/*
 * *** STUDENTS SHOULD WRITE CODE FOR THIS FUNCTION ***
 */
uint16_t factorial(const uint16_t x)
{
    uint16_t value = 1;
    for (uint16_t i = 2; i <= x; ++i)
        value *= i;

    return value;
}

/*
 * *** STUDENTS SHOULD WRITE CODE FOR THIS FUNCTION ***
 */
int main()
{
    int n;
    int k;

    // get and validate user input
    cout << "Enter n: ";
    cin >> n;
    cout << "Enter k: ";
    cin >> k;
    if (n <= 0 || k <= 0)
    {
        cout << "result = -1" << endl;
        return -1;
    }

    // calculate C(n,k) = n! / (k! * (n-k)!)
    uint16_t numerator = factorial(n);
    uint16_t denominator = factorial(k) * factorial(n - k);
    uint16_t c_n_k = numerator / denominator;

    // write out results
    cout << "result = " << c_n_k << endl;

    return 0;
}