#ifndef SHA256_H
#define SHA256_H

#include <stdint.h> // for uint32_t definitions

#define SHA256_DIGEST_SIZE (256 / 8)
#define SHA256_BLOCK_SIZE (512 / 8)

// Macros needed for SHA256 transformations
#define SHFR(x, n) (x >> n)
#define ROTR(x, n) ((x >> n) | (x << (32 - n))) // Assumes 32-bit `x`
#define CH(x, y, z) ((x & y) ^ (~x & z))
#define MAJ(x, y, z) ((x & y) ^ (x & z) ^ (y & z))

#define SHA256_F1(x) (ROTR(x, 2) ^ ROTR(x, 13) ^ ROTR(x, 22))
#define SHA256_F2(x) (ROTR(x, 6) ^ ROTR(x, 11) ^ ROTR(x, 25))
#define SHA256_F3(x) (ROTR(x, 7) ^ ROTR(x, 18) ^ SHFR(x, 3))
#define SHA256_F4(x) (ROTR(x, 17) ^ ROTR(x, 19) ^ SHFR(x, 10))

// SHA256 context structure
typedef struct
{
	unsigned int tot_len;
	unsigned int len;
	unsigned char block[2 * SHA256_BLOCK_SIZE];
	uint32_t h[8];
} sha256_ctx;

// Function prototypes
void sha256_init(sha256_ctx *ctx);
void sha256_update(sha256_ctx *ctx, const unsigned char *message, unsigned int len);
void sha256_final(sha256_ctx *ctx, unsigned char *digest);
void sha256(const unsigned char *message, unsigned int len, unsigned char *digest);

#endif /* SHA256_H */    
