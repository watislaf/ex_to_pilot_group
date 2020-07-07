#include <set>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");
vector< vector< int> > vv;
int n, m, rejim;
vector< int> zn;
int checkMi = 1;
vector < pair<int, int> > FandE;
int getp()
{
	FandE.resize(n, { 0,0 });
	int sum = 0;
	for (int i = 0; i < n; i++)
		FandE[i] = { 0,0 };
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < vv[i].size(); j++)
		{
			int to = vv[i][j];
			if (zn[i] != zn[to])
				FandE[i].second += 1;
			else
				FandE[i].first += 1;

		}
		sum += n - 1 - FandE[i].second;
	}
		return sum;
	 
}

bool check()
{
	int check = 0;
	for (int i = 0; i < n; i++)
		check += zn[i];
	if (check == 0 || check == n)
		return false;
	for (int i = 0; i < n; i++)
	{
		int fr, nfr;
		fr = nfr = 0;
		for (int j = 0; j < vv[i].size(); j++)
		{
			if (zn[vv[i][j]] != zn[i])
				nfr++;
			else
				fr++;
		}
		if (fr < nfr)
		{
			return false;
		}
	}
	return true;
}
bool dfs(int v)
{
	zn[v] = 1;
	if (check())
	{
		return true;
	}
	for (int i = 0; i < vv[v].size(); i++)
	{
		int to = vv[v][i];
		if(zn[to]!=1)
			if (dfs(to) )
			{
				return true;
			}
	}
	zn[v] = 0;
	return false;
}
void myAlgo()
{
	int start = 0;

	for (int i = 0; i < n; i++) {
		zn[i] = 0;
		if (vv[i].size() < vv[start].size())
			start = i;
	}
	
	dfs(start);
	
}
int main()
{
	ofstream pout("output2.txt");
	cin >> n >> m >> rejim;

	vv.resize(n);
	zn.resize(n);
	if (rejim == 3)
	{
		rejim = 2;
		checkMi = 0;
	}
	int base = 2;
	int mask = 1;
	for (int i = 0; i <n; i++)
	{
		mask *= base;
	}
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		a--; b--;
		vv[a].push_back(b);
		vv[b].push_back(a);
	}
	bool fl = false;
	int price = -3;
	vector<int> anss;
	switch (rejim)
	{	
	case 1:
		for (int i = 0; i < n; i++)
		{
			cin >> zn[i];
		}
		cout << check();
		return 0;
	case 2:
		for (int bits = 1; bits <mask; bits++)
		{
			int tmp = bits;
			for (int i = 0; i < n; i++)
				zn[i] = 0;
			int k = 0;
			while (tmp)
			{
				zn[k] = tmp & 1;
				k++;
				tmp >>= 1;
			}
			if (check())
			{
				fl = true;
				if (checkMi==0)
				{
					int tmpp = getp();
					if (tmpp > price)
					{
						price = tmpp;
						anss.resize(zn.size());
						for(int g=0;g<zn.size();g++)
							anss[g] = zn[g];
					}
				}
			}

		}
		if (checkMi == 0 && fl==true)
		{
			cout << "OK ";
			for (int i = 0; i < n - 1; i++)
				cout << anss[i] << " ";
			cout << anss[n - 1];
		 
			pout << price;
			return 0;
		}
		break;
	}
	if (checkMi)
	{	
		if(vv.size()!=0)
			myAlgo();
		if (check() == fl)
		{
			if (fl == false)
			{
				cout << "NO";
				return 0;
			}
			else
			{
				cout << "OK ";
				for (int i = 0; i < n - 1; i++)
					cout << zn[i] << " ";
				cout << zn[n - 1];
				return 0;
			}
		}
		else
		{
			cout << "WrongAlgo ";
			for (int i = 0; i < n - 1; i++)
				cout << zn[i] << " ";
			cout << zn[n - 1];
			return 0;
		}
	}

	cout << "NO";
}
		
	
	  /*
	  Жадник
void update()
{
	 
	for (int i = 0; i < n; i++)
		FandE[i] = { 0,0 };
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < vv[i].size(); j++)
		{
			int to = vv[i][j];
			if (zn[i] != zn[to])
				FandE[i].second += 1;
			else
				FandE[i].first += 1;
		}
	}
}
int type(pair <int, int>  a)
{
	if (a.first > a.second)
		return 3;
	if (a.first == a.second)
		return 2;
	if (a.first < a.second)
		return 1;
}
bool cmp(int a, int b)
{
	return type(FandE[a]) < type( FandE[b]);
}
vector <int> myParts;
bool nestabilno()
{
	for (int i = 0; i < myParts.size(); i++)
	{
		if (type( FandE[ myParts[i] ] ) == 1)
			return true;
	}
	int count = 0;
	for (int i = 0; i < n; i++)
	{
		if (zn[i] == 1)
		{
			count++;
			if (FandE[i].first < FandE[i].second)
				return true;
		}
	}
	if (count == 0)
		return true;
	return false;
}
void myAlgo()
{
	if (vv.size() == 0)
		return;
	int start = 0;
 
	FandE.resize(n, { 0,0 });

	for (int i = 0; i < n; i++)
	{
		zn[i] = 0;
	}
	update();
	for (int i = 0; i < n; i++)
	{
		if (FandE[i].first<FandE[start].first)
			start = i;
	}
	myParts.push_back(start);
	while (nestabilno())
	{
		sort(myParts.begin(), myParts.end(), cmp);
		int toColor = myParts[0];
		myParts.erase(myParts.begin());
		zn[toColor] = 1;
		for (int i = 0; i < vv[toColor].size(); i++)
		{
			int canBeFriend = vv[toColor][i];
			if (zn[toColor] != zn[canBeFriend])
				myParts.push_back(canBeFriend);
		}
		update();
	}
	if (check() == false)
	{
		while (myParts.size())
		{
			int toColor = myParts[0];
			myParts.erase(myParts.begin());
			zn[toColor] = 1;
			for (int i = 0; i < vv[toColor].size(); i++)
			{
				int canBeFriend = vv[toColor][i];
				if (zn[toColor] != zn[canBeFriend])
					myParts.push_back(canBeFriend);
			}
		}
	}
}
*/
	  

