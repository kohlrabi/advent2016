#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <vector>

using namespace std;

int move(char const &c, int num) 
{
	switch(c) {
		case 'U':
			if(num > 3)
				num -= 3;
			break;
		case 'D':
			if(num < 7)
				num += 3;
			break;
		case 'L':
			if(num%3 != 1)
				num -= 1;
			break;
		case 'R':
			if(num%3 != 0)
				num += 1;
			break;
	}
	return num;
}

string part1(vector<string> const &s)
{
	string ret = "";
	int num = 5;
	
	for(auto &i : s) {
		for(auto &c : i)
			num = move(c, num);
		ret += to_string(num);
	}
	return ret;

}

int main(int argc, char **argv)
{
	vector<string> in;
	string s;
	while(getline(cin, s, '\n'))
		in.push_back(s);

	cout << "part 1: " << part1(in) << endl;
	return 0;
}
