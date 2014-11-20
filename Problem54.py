# Handle poker hands
#

# #hand values:
# #	2-13, rest = high card
# #	16-112, rest = pair (pair x 8, e.g. 2x8)
# #	114-3458, rest = two pair (pair x pair x 19)
# #	3460-24220, rest = three of a kind (3 x 1730)
# #	24222-72720, 0 = straight (total x 1212)
# #	72740-218220, 0 = flush (total x 3637)
# #	218232-1236648, 0 = full house (, (triple x 3 + double x 2) x 18186)
# #	1236650-8656550, rest = four of a kind (total x 618325)
# #	8656560-25969680, 0 = straight flush (total x 432828)
# #	99999999 = royal flush
# # pair = 8
# # two_pair = 19
# # three = 1730
# # straight = 1212
# # flush = 3637
# # full = 18186
# # four = 618325
# # str_flush = 432828
# # royal = 99999999


high = 0
pair = 1
two_pair = 2
three = 3
straight = 4
flush = 5
full = 6
four = 7
str_flush = 8
royal = 9

def convert_card_to_num(card):
	if card.isdigit():
		return int(card)
	else:
		return {
			'T': 10,
			'J': 11,
			'Q': 12,
			'K': 13,
			'A': 14
			}[card]
			
def is_straight(cards):
	cards.sort()
	start_num = cards[0]
	index = 1
	while index < 5 and start_num + index == cards[index]:
		index += 1
	if index == 5 and start_num + (index-1) == cards[index-1]:
		return True
	else:
		return False
		
def hand_sum(hand_dict):
	total = 0
	for key, val in hand_dict.items():
		total += key * val
	return total
	
def handle_flush(hand):
	cards = list(hand.keys())
	cards.sort(reverse=True)

	if is_straight(cards):
		cards.sort(reverse=True)
		if hand.has_key(14):
			result = royal, 0
			print("Royal Flush")
		else:
			result = str_flush, cards
			print("Straight Flush: ", result)
	else:
		cards.sort(reverse=True)
		result = flush, cards
		print("Flush: ", result)
		
	return result
	
def handle_others(hand):
	cards = list(hand.keys())
	cards.sort(reverse=True)
	max_pair = max(hand.values())
	
	if max_pair == 1:
		#no pairs, check for straight, otherwise we are high card
		if is_straight(cards):
			cards.sort(reverse=True)
			result = straight, cards
			print("Straight: ", result)
		else:
			cards.sort(reverse=True)
			result = high, cards
			print("High card: ", result)
	else:
		max_keys = []
		other_keys = []
		for key, val in hand.items():
			if val == max_pair:
				max_keys.append(key)
			else:
				other_keys.append(key)
		other_keys.sort(reverse=True)
		
		if max_pair == 4:
			result = four, max_keys[0:1]+other_keys
			print("Four of a kind: ", result)
		elif max_pair == 3:
			#check if we have a pair to go along with the three of a kind
			if len(other_keys) == 1:
				result = full, max_keys[0:1]+other_keys
				print("Full house: ", result)
			else:
				result = three, max_keys[0:1] + other_keys
				print("Three of a kind: ", result)
		elif max_pair == 2:
			#check for two pairs
			if len(max_keys) == 2:
				max_keys.sort(reverse=True)
				result = two_pair, max_keys[0:2]+other_keys
				print("Two pair: ", result)
			else:
				result = pair, max_keys[0:1]+other_keys
				print("Pair: ", result)
	return result
	
def detect_flush(hand):
	#check for same suit, if we find a different suit, we can eliminate flushes of all sorts
	suit = hand[0][1]
	card = 1
	
	while card < 5 and suit == hand[card][1]:
		card += 1
	
	if card == 5 and suit == hand[card-1][1]:
		return True
	else:
		return False

def calculate_hand(hand):
	result = 0,0
	
	vals = dict()
	
	for i in range(len(hand)):
		num = convert_card_to_num(hand[i][0])
		if num in vals:
			vals[num] += 1
		else:
			vals[num] = 1	
		
	if detect_flush(hand):
		#we have a flush, now what kind?
		result = handle_flush(vals)
	else:
		result = handle_others(vals)
		
	return result

def compare_hands(first_hand, second_hand):
	first_result = calculate_hand(first_hand)
	second_result = calculate_hand(second_hand)
	
	if first_result > second_result:
		print("Player 1 wins\n")
		return 1
	elif second_result > first_result:
		print("Player 2 wins\n")
		return 2
	else:
		print("Nobody wins\n")
		return 0

p1 = p2 = 0

with open("poker.txt") as f:
	content = f.readlines()

line_num = 1
for line in content:
	print("Hand at line: ", line_num)
	vals = line.split(" ")
	res = compare_hands(vals[:5], vals[5:])
	if res == 1:
		p1 += 1
	elif res == 2:
		p2 += 1
	else:
		print("Uh Oh, tie")
	line_num += 1
	
print(p1)
##376

# first_hands = [["5H", "5C", "6S", "7S", "KD"],
			# ["5D", "8C", "9S", "JS", "AC"],
			# ["2D", "9C", "AS", "AH", "AC"],
			# ["4D", "6S", "9H", "QH", "QC"],
			# ["2H", "2D", "4C", "4D", "4S"]]

# second_hands = [["2C", "3S", "8S", "8D", "TD"],
			# ["2C", "5C", "7D", "8S", "QH"],
			# ["3D", "6D", "7D", "TD", "QD"],
			# ["3D", "6D", "7H", "QD", "QS"],
			# ["3C", "3D", "3S", "9S", "9D"]]


# for i in range(len(first_hands)):
	# print(compare_hands(first_hands[i], second_hands[i]))

	