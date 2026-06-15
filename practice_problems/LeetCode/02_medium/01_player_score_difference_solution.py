def score_difference(nums: list[int]) -> int:
    # Input is an array of positive integers with a minimum of 1 element
    # Output is a positive/negative integer
    # Only two players
    # Take an array of two players with their scores -> arr[0]: player1Score, arr[1]: player2Score
    # num[i] % 2 == 0, swap
    # (i + 1) % 6 == 0, swap

    players = [0, 0]
    active_player_index = 0

    for i, num in enumerate(nums):
        active_player_index = get_active_player_index(active_player_index, nums[i], i)
        players[active_player_index] += nums[i]

    return players[0] - players[1]


def get_active_player_index(current_active_player_index, game_points, current_game_index):
    swap_lambda = lambda a: 1 if a == 0 else 0
    active_player_index = current_active_player_index

    if game_points % 2 != 0:
        active_player_index = swap_lambda(active_player_index)
    if (current_game_index + 1) % 6 == 0:
        active_player_index = swap_lambda(active_player_index)

    return active_player_index
