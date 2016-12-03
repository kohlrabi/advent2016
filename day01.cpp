#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <vector>

using namespace std;

int part1()
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
	return abs(loc.real())+abs(loc.imag());
}

int part2()
{
	string s;
	complex<double> loc=0, dir=1;
	vector<complex<double>> locs;
	
	locs.push_back(loc);
	while(true) {
		cin >> s;
		if(s[0] == 'L')
			dir *= 1if;
		else
			dir *= -1if;

		for(int i=0; i<stod(s.substr(1,s.size()-1)); i++) {
			loc += dir;
			for(auto &i : locs)
				if(i == loc)
					return abs(loc.real()) + abs(loc.imag());
			locs.push_back(loc);
		}
	}
}


int main(int argc, char **argv)
{
	cout << part2() << endl;
	return 0;
}
