class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        arr = code * 2

        if k > 0:
            window_sum = sum(arr[1:k+1])
            for i in range(n):
                result[i] = window_sum
                window_sum += arr[i + k + 1]
                window_sum -= arr[i + 1]

        else:
            k = -k
            window_sum = sum(arr[n-k:n])
            for i in range(n):
                result[i] = window_sum
                window_sum += arr[i]
                window_sum -= arr[i + n - k]

        return result
