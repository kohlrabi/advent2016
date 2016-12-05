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

vector<vector<int>> grid =
{
	{ { 0, 0,  0,  0,  0, 0, 0 } },
	{ { 0, 0,  0,  1,  0, 0, 0 } },
	{ { 0, 0,  2,  3,  4, 0, 0 } },
	{ { 0, 5,  6,  7,  8, 9, 0 } },
	{ { 0, 0, 10, 11, 12, 0, 0 } },
	{ { 0, 0,  0, 13,  0, 0, 0 } },
	{ { 0, 0,  0,  0,  0, 0, 0 } }
};	

vector<unordered_map<char, int>> moves2 = 
{
	{ {'D', 3} },
	{ {'D', 6}, {'R', 3} }, 
	{ {'D', 7}, {'R', 4}, {'U', 1}, {'L', 2} },
	{ {'D', 8}, {'L', 3} },
	{ {'R', 6} },
	{ {'D', 10}, {'U', 2}, {'R', 7}, {'L', 5} },
	{ {'D', 11}, {'U', 3}, {'R', 8}, {'L', 6} },
	{ {'D', 12}, {'U', 4}, {'R', 9}, {'L', 7} },
	{ {'L', 8} },
	{ {'U', 6}, {'R', 11} }, 
	{ {'D', 13}, {'R', 12}, {'U', 7}, {'L', 10} },
	{ {'U', 8}, {'L', 11} },
	{ {'U', 11} }
};	

string part1(vector<string> const &s)
{
	string ret = "";
	int num = 5;
	
	for(auto const &l : s) {
		for(auto const &c : l)
			num += moves[c](num);
		ret += to_string(num);
	}
	return ret;
}

string part2(vector<string> const &s)
{
	vector<int> keys;
	stringstream ss;
	int num = 5;
	
	for(auto const &l : s) {
		for(auto const &c : l) {
			auto it = moves2[num-1].find(c);
			if(it != moves2[num-1].end())
				num = it->second;
		}
		keys.push_back(num);
	}
	
	for(auto &key : keys)
		ss << hex << uppercase << key;

	return ss.str();
}

string part2grid(vector<string> const &s)
{
	stringstream ss;
	vector<int> keys;
	pair<int, int> pos = { 4, 2 };
	
	for(auto const &l : s) {
		for(auto const &c : l) {
			pair<int, int> pos2 = pos;
			switch(c) {
				case 'U':
					pos2.first -= 1;
					break;
				case 'D':
					pos2.first += 1;
					break;
				case 'L':
					pos2.second -= 1;
					break;
				case 'R':
					pos2.second += 1;
					break;
			}
			if(grid[pos2.first][pos2.second] != 0)
				pos = pos2;
		}
		keys.push_back(grid[pos.first][pos.second]);
	}

	for(auto &key : keys)
		ss << hex << uppercase << key;
	
	return ss.str();
}

int main(int argc, char **argv)
{
	vector<string> in;
	string s;
	while(getline(cin, s, '\n'))
		in.push_back(s);

	cout << "part 1: " << part1(in) << endl;
	cout << "part 2: " << part2(in) << endl;
	cout << "part 2 (grid): " << part2grid(in) << endl;
	return 0;
}
