def gen(n):
    def dfs(binary, result):
        if len(binary) == n:
            result.append(binary)
            return result

        return dfs(binary + '0', result) and dfs(binary + '1', result)

    return dfs('', [])







