#include <iostream>
#include <string>
#include <complex>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
	string s;
	complex<double> loc=0, dir=1;

	while(true) {
		cin >> s;
		if(s[0] == 'L')
			dir *= 1if;
		else
			dir *= -1if;
		loc += dir * stod(s.substr(1,s.size()-1));
		if(s.back() != ',')
			break;
	}

	cout << abs(loc.real())+abs(loc.imag()) << endl;
	return 0;
}
		

		





