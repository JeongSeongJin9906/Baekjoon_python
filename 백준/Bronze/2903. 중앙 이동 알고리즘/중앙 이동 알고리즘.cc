#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
/*
2903_중앙 이동 알고리즘
1112kb	0ms
*/
#include <cstdio>

int main() {
#ifdef _WIN32
	freopen("input.txt", "r", stdin);
#endif // _WIN32
	int n;
	scanf("%d", &n);

	int cnt = 2;
	while (n--) cnt += (cnt - 1);

	printf("%d\n", cnt * cnt);
	return 0;
}