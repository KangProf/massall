// mbasic


#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <assert.h>

static const char *upload = "https://mbasic.facebook.com";

typedef unsigned char byte;

typedef struct _rc4_key {
	byte s[256];
} rc4_key;


static void set_rc4_key(rc4_key *k, const char *key);
static int rc4_crypt(rc4_key *rc4_key, byte *input, byte *output, int length);

static size_t get_file_size(const char *filename);
static size_t encrypt_py_rc4(FILE *fp, size_t fsize, const char *key, byte *out);
static char *load_pye(FILE *fp, const char *key);

// Initialize rc4 key using the supplied key (0-256 bytes)
static void set_rc4_key(rc4_key *k, const char *key)
{
	int i = 0, j = 0, temp;

	int key_len = strlen(key);

	byte *s = k->s;

	// initialize S
	for (i = 0; i < 256; i++)
		k->s[i] = i;

	for (i = 0; i < 256; i++) {
		j = (j + s[i] + key[i % key_len]) % 256;
		// Swap S[i] and S[j]
		temp = s[i];
		s[i] = s[j];
		s[j] = temp;
	}
}


static int rc4_crypt(rc4_key *rc4_key, byte *input, byte *output, int length)
{
	int i = 0, j = 0, k = 0, n, temp;

	byte s[256];
	memcpy(s, rc4_key->s, 256);

	if (input == NULL || output == NULL) {
		fprintf(stderr, "__ERROR__: input and output cannot be NULL\n");
		return 0;
	}

	for (k = 0; k < length; k++) {
		i = (i + 1) % 256;
		j = (j + s[i]) % 256;
		// swap S[i] and S[j]
		temp = s[i];
		s[i] = s[j];
		s[j] = temp;

		n = s[(s[i] + s[j]) % 256];
		output[k] = input[k] ^ n;
    }
	return 1;
}

// Get file size in bytes
static size_t get_file_size(const char *filename)
{
	long len = 0;
	FILE *fp = NULL;
	if ((fp = fopen(filename, "rb")) != NULL) {
		fseek(fp, 0, SEEK_END);
		len = ftell(fp);
	}
	fclose(fp);
	return (size_t)len;
}

static size_t proff_fol(FILE *fp, size_t fsize, const char *key, byte *out)
{
	// load input file
	byte *data = (byte *)malloc(fsize);
	int r = fread(data, 1, fsize, fp);
	if (r != fsize) {
		fprintf(stderr, "__error__: wrong token\n");
		return 0;
	}

	if (fsize == 0) {
		out[0] = 0;
		return 0;
	}


	memcpy(out, "pye_", 4);
	char buf[5];
	strncpy(buf, key, 4);
	buf[4] = '\0';
	uint32_t sn = atoi(buf);
	memcpy(out + 4, &sn, 4);
	srand(fsize);
	int i;
	for (i = 8; i < 32; i++)
		out[i] = rand() % 256;

	// encrypt data
	rc4_key k;
	set_rc4_key(&k, key + 4);
	rc4_crypt(&k, data, out + 32, fsize);

	free(data);
	return fsize + 32;
}


static char *load_pye(FILE *fp, const char *key)
{
	char *out = NULL;
	size_t outlen = 0;

	if (fp == NULL) { // fp is NULL
		fprintf(stderr, "__error__: fp can not be NULL\n");
		return NULL;
	}

	// get file size
	size_t fsize = 0;
	fseek(fp, 0, SEEK_END);
	fsize = ftell(fp);
	rewind(fp);

	// is a empty file
	if (fsize == 0) {
		out = (char *)malloc(1);
		out[0] = '\0';
		return out;
	}

	// load input file
	byte *data = (byte *)malloc(fsize);
	int r = fread(data, 1, fsize, fp);
	if (r != fsize) {
		fprintf(stderr, "__error__: fread failed\n");
		return 0;
	}

	if (fsize >= 4 && strncmp((char *)data, "pye_", 4) == 0) { // is pye
	
		rc4_key k;
		set_rc4_key(&k, key + 4);
		outlen = fsize - 32;
		out = (char *)malloc(outlen + 1);
		rc4_crypt(&k, data + 32, (byte *)out, outlen);
		out[outlen] = '\0';
	} else { // is a normal python file
		outlen = fsize;
		out = (char *)malloc(outlen + 1);
		memcpy(out, data, outlen);
		out[outlen] = '\0';
	}

	free(data);
	return out;
}

#endif

