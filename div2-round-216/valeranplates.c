#include<stdio.h>

int n,m,k,type,wash_count;
int i = 0;

int main() {
	scanf("%d %d %d", &n, &m, &k);
	for(i = 0; i < n; i++) {
		scanf("%d", &type);
		if(type == 1) {
			if(m != 0) {
				m--;
			}
			else {
				wash_count++;
			}
		}
		else if(type == 2) {
			if(k != 0) {
				k--;
			}
			else if(m != 0) {
				m--;	
			}
			else {
				wash_count++;
			}	
		}
	}
	printf("%d", wash_count);
	return 0;
}
