// C++ program to find the array 
// element that appears only once 
#include <iostream> 
using namespace std; 

int findSingle(int ar[], int ar_size) 
	{ 
		// Do XOR of all elements and return 
		int res = ar[0]; 
		for (int i = 1; i < ar_size; i++) 
			res = res ^ ar[i]; 

		return res; 
	} 

// Driver code 
int main() 
	{ 
		int ar[] = {2, 3, 5, 4, 5, 3, 4}; 
		int n = sizeof(ar) / sizeof(ar[0]); 
		cout << "Element occurring once is "
			<< findSingle(ar, n); 
		return 0; 
	} 

