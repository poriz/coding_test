from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = []
    graph = [[0 for _ in range(102)] for _ in range(102)]

    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = 2 * x1, 2 * y1, 2 * x2, 2 * y2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                graph[i][j] = 2

        for k in range(x1, x2 + 1):
            for m in range(y1, y2 + 1):
                if graph[k][m] != 2:
                    graph[k][m] = 1

    q = deque([])
    q.append([2 * characterX, 2 * characterY, 0])
    history = [[2 * characterX, 2 * characterY]]

    while q:
        x, y, count = q.popleft()

        if (x, y) == (2 * itemX, 2 * itemY):
            return count // 2

        else:
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 101 and 0 <= ny < 101 and [nx, ny] not in history and graph[nx][ny] == 1:
                    q.append([nx, ny, count + 1])
                    history.append([nx, ny])

    return answer