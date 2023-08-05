import math
import time

def get_first(block_size,nums,k):
  if nums is []:
    return k, None
  digit_num = 0
  while k > block_size:
    digit_num+=1
    k-=block_size
  return k,digit_num

def get_permutation(v, k):
  nums = list(range(1,v+1))
  digit = []
  while len(nums) > 0:
    block_size = math.factorial(len(nums)-1)
    k, d = get_first(block_size,nums,k)
    digit += str(nums[d])
    del nums[d]
  return ''.join(digit)


start = time.time()
print(get_permutation(2,2))
print(get_permutation(3,3))
print(get_permutation(4,4))
print(get_permutation(4,8))
print(get_permutation(10,1000000))
print(get_permutation(11,10000))
print(get_permutation(15,1000000))
print(get_permutation(10,1000012))
end = time.time()
print('-'*20)
print(f"Iteration: \tTime taken: {(end-start)*10**3:.03f}ms")