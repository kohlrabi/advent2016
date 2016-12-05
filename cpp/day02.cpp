#include <iostream>
#include <string>
#include <complex>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <functional>

using namespace std;

unordered_map<char, function<int(int)>> moves = 
{
	{ 'U', [](int num)->int{ return -3 * (num > 3); } },
	{ 'D', [](int num)->int{ return 3 * (num < 7); } },
	{ 'L', [](int num)->int{ return -1 * (num%3 != 1); } },
	{ 'R', [](int num)->int{ return 1 * (num%3 != 0); } },
};

string part1(vector<string> const &s)
{
	string ret = "";
	int num = 5;
	
	for(auto &i : s) {
		for(auto const &c : i)
			num += moves[c](num);
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
