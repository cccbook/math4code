#include <stdio.h>
#include <string.h>
#define BYTE unsigned char

void encrypt(char plain[], char cipher[], int len, char key[], int keyLen) {
  int pi;
  for (pi=0; pi<len; pi++) {
      int ki = pi%keyLen;
      cipher[pi] = plain[pi] ^ key[ki];
  }
}

void decrypt(char cipher[], char plain[], int len, char key[], int keyLen) {
  int pi;
  for (pi=0; pi<len; pi++) {
      int ki = pi%keyLen;
      plain[pi] = cipher[pi] ^ key[ki];
  }
  plain[pi] = '\0';
}

void getKey(char cipher[], int from, char pattern[], char key[], int keyLen) {
  int i;
  for (i=from; i<from+keyLen; i++) {
    int ki = i % keyLen;
    key[ki] = pattern[i-from] ^ cipher[i];
  }
}

int inSetCount(char str[], int len, char set[]) {
  int i, count=0;
  for (i=0; i<len; i++) {
    if (strchr(set, str[i]) > 0)
      count++;
  }
  return count;
}

void printHex(char key[], int keyLen) {
  int i;
  for (i=0; i<keyLen; i++) {
    printf("%02x ", (BYTE) key[i]);
  }
}

char goodSet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ";

void hack(char cipher[], int len, char pattern[], char hackKey[], int keyLen, char hackPlain[], char maxKey[]) {
  int i;
  int maxScore = -10000;
  for (i=0; i<len-keyLen; i++) {
    getKey(cipher, i, pattern, hackKey, keyLen);
    decrypt(cipher, hackPlain, len, hackKey, keyLen);
    int score = inSetCount(hackPlain, len, goodSet);
    if (score > maxScore) {
      maxScore = score;
      strncpy(maxKey, hackKey, keyLen);
    }
    printf("i=%02d score=%02d key=", i, score);
    printHex(hackKey, keyLen);
    printf(" hackPlain=%s\n", hackPlain);
  }
}

int main() {
  char plain[] = "Zero-hour is July/4th 3.30 am";
  char cipher[100], plain2[100], hackPlain[100];
  int  len = strlen(plain);
  char key[] = { 0x6D, 0x3F, 0x76, 0xE3 };
  char hackKey[4], maxKey[4];
  int  keyLen = 4;
  
  printf("明文=%s\n", plain);
  encrypt(plain, cipher, len, key, keyLen);
  printf("密文=%s\n", cipher);
  hack(cipher, len, " is ", hackKey, keyLen, hackPlain, maxKey);  
  decrypt(cipher, plain2, len, maxKey, keyLen);
  // decrypt(cipher, plain2, len, key, keyLen);
  printf("還原=%s\n", plain2);
}
