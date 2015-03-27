
//Project Euler problem 1
#include <iostream>
using namespace std;

int main() {
	int countSum;
	
	for(int i = 0; i < 1000; i++) {
		if (i % 3 == 0) {
			if (i % 5 == 0) {
				cout << i << " is divisible by 3 and 5." << endl;
				countSum = countSum + i;
			}
		}
	}
	
	cout << "Sum: " << countSum << endl;
	
	return(0);
}
