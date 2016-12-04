#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <vector>

using namespace std;

string part1()
{
	string s, ret = "";
	int num = 5;
	
	while(true) {
		cin >> s;
		if(s[0] == ';')
			break;
		for(auto &c : s) {
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
		}
		ret += to_string(num);
	}
	return ret;

}

int main(int argc, char **argv)
{
	cout << part1() << endl;
	return 0;
}
