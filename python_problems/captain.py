# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has
# an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel. 
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of k members per group where k ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries.
# The list consists of the room numbers for all of the tourists.
# The room numbers will appear k times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number. 
# The total number of tourists or the total number of groups of families is not known to you. 
# You only know the value of k and the room number list.

# Input Format
# The first line consists of an integer, k, the size of each group.
# The second line contains the unordered elements of the room number list.

# Constraints
# 1 < k < 1000

# Output Format
# Output the Captain's room number.

#from collections import defaultdict

#if __name__ == "__main__":
#    group_size = int(input())
#    room_number_list = map(int, input().split())
    
    # make a dictionary, {room_number : freq}
#    room_freq = defaultdict(int)
    
#    for num in room_number_list:
#        room_freq[num] += 1
#    for key in room_freq:
#        if room_freq[key] == 1:
#            print(key)
#            break


# Mathematical solution:

if __name__ == "__main__":
    k = int(input())
    room_number_list = list(map(int, input().split()))
    
    room_number_set = set(room_number_list)
    
    num_of_groups = (len(room_number_list) - 1)/k
    
    captain_number = (k*(sum(room_number_set)) - sum(room_number_list))/(k-1)
    
    print(int(captain_number))
