import time
import tempfile

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10

start_time = time.time()
result = binary_search(arr, target)
end_time = time.time()

execution_time = end_time - start_time

# Write execution time to a temporary file
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
  temp_file.write(f"Execution time: {execution_time:.6f} seconds")
  print(f"Execution time saved to: {temp_file.name}")

if result != -1:
  print("Element is present at index", str(result))
else:
  print("Element is not present in array")