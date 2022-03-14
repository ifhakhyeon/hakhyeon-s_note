#
# # 1.
# SIZE = 2 ** 16 + 1 # Size is too big... Isn't it?
#
# # 2.
# sieve = [255 for _ in range(SIZE // 8 + 1)]
#
# # 3.
# def set_composite(n):
#     sieve[n >> 3] &= ~(1 << (n & 7))
#
# # 4.
# set_composite(0)
# set_composite(1)
#
# # 5.
# def is_prime(n):
#     return True if sieve[n >> 3] & (1 << (n & 7)) else False
#
# # 6.
# for i in range(2, int(SIZE ** (1/2))+1):
#     if is_prime(i):
#         for j in range(i*i, SIZE+1, i):
#             set_composite(j)

# print(sieve)
# for i in sieve:
#     print(i)

SIZE = 2 ** 16 + 1 # Size is too big... Isn't it?
class Sieve:
    def __init__(self, size):
        self._size = size
        self._sieve = [255 for _ in range((SIZE >> 3) + 1)]

        self._set_composite(0)
        self._set_composite(1)

        for i in range(2, int(self._size ** (1/2))+1):
            if self.is_prime(i):
                for j in range(i*i, self._size+1, i):
                    self._set_composite(j)
        print(f"Sieve of size {size} is initialized")

    def is_prime(self, n):
        if n > self._size:
            raise ValueError(f"This sieve only support integers equal to or less than {self._size}")
        return True if self._sieve[n >> 3] & (1 << (n & 7)) else False

    def _set_composite(self, n):
        self._sieve[n >> 3] &= ~(1 << (n & 7))


sieve = Sieve(SIZE)

print(sieve.is_prime(1009))