// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");

int solution(int N) {
    // write your code in C99 (gcc 6.2.0)
    int cnt = 0;
    int start = 0;
    int last_digit = 0;
    int binary_gap = 0;

    while (N != 0) {
        last_digit = N % 2;

        switch (last_digit) {
            case 0:
                if (start)
                    cnt++;
                break;
            case 1:
                if (start) {
                    if (cnt > binary_gap) {
                        binary_gap = cnt;
                        cnt = 0;
                    } else {
                        cnt = 0;
                    }
                } else {
                    start = 1;
                }
                break;
        }
        N /= 2;
    }
    return binary_gap;
}
