#include<bits/stdc++.h>
#define V 4
#define INF 9999
using namespace std;
void pri(int d[][V]);
void dvr(int g[V][V]){
int d[V][V],i,j,k;
for(i=0;i<V;i++)
	for(j=0;j<V;j++)
	d[i][j]=g[i][j];
for(k=0;k<V;k++)
	for(i=0;i<V;i++)
		for(j=0;j<V;j++)
			if(d[i][j]>d[i][k]+d[k][j])
			d[i][j]=d[i][k]+d[k][j];

pri(d);
}


void pri(int d[][V])
{
for(i=0;i<V;i++)
	for(j=0;j<V;j++)
	{if(d[i][j]==INF)cout<<"INf"<<"   ";
	else 
	cout<<d[i][j]<<"   ";
}cout<<endl;
}
int main(){
int g[V][V]={ {0, 5, INF, 10},  
                        {INF, 0, 3, INF},  
                        {INF, INF, 0, 1},  
                        {INF, INF, INF, 0}  

};
dvr(g);
return 0;
}

