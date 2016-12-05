#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <vector>

using namespace std;

int part1(string const &in)
{
	stringstream ss;
	ss.str(in);
	string s;
	complex<double> loc=0, dir=1;
	
	while(true) {
		getline(ss, s, ' ');
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

int part2(string const &in)
{
	stringstream ss;
	ss.str(in);
	string s;
	complex<double> loc=0, dir=1;
	vector<complex<double>> locs;
	
	locs.push_back(loc);
	while(true) {
		getline(ss, s, ' ');
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
	string s;
	getline(cin, s, '\n');
	cout << "part 1: " << part1(s) << endl;
	cout << "part 2: " << part2(s) << endl;
	return 0;
}
