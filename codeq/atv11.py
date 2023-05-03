#include <stdio.h>
int main()
{
    int p,q, cnt=0, i, dif;
    scanf("%d%d",&p,&q);
    int jump[q];
    for(i=0; i<q; i++)
    sscanf("%d", &jump[i]);
    for(i=1;i<q;i++)
}
{
if (jump[i]>jump[i-1])
dif = (jumpt[i] - jump[i-1]);
else 
dif = (jump[i-1]-jump[i]);
if (dif<=p)
cnt++;
}
{
if(cnt==q-1)
printf("You win");
else
printf("Game Over/n);
       return 0;
       }
