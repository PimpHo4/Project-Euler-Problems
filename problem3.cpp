/* 
project euler problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include <iostream>
using namespace std;

int main() {
	long number, div;
	
	div = 2;
	cout << "number: ";
	cin  >> number;
	
	while (number != 0) {
		if (number % div != 0)
		{
			div = div + 1;
		}
		else {
			number = number / div;
			cout << "Prime Factor: " << div << endl;
			if (number == 1)
				break;
		}
	}
	
	return(0);
}
